#!/usr/bin/env python3
"""
build_quizzes.py — convert YAML quiz definitions into interactive HTML pages.

Reads:    course/quizzes/data/track_*/week_*.yml
Writes:   course/quizzes/track_*/week_*.html

Each output page:
- includes a JSON <script> the front-end quiz.js library reads
- pulls quiz.js + extra.css via relative paths
- renders inside the MkDocs site even though it's a raw HTML page

Run from repo root:
    python scripts/build_quizzes.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "course" / "quizzes" / "data"
OUT_DIR = REPO_ROOT / "course" / "quizzes"

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="stylesheet" href="../../assets/css/extra.css" />
  <style>
    body {{
      font-family: -apple-system, "Inter", "Helvetica Neue", Arial, sans-serif;
      max-width: 820px; margin: 0 auto; padding: 24px;
      background: #fafafa; color: #212121;
    }}
    @media (prefers-color-scheme: dark) {{
      body {{ background: #0d0d10; color: #e0e0e0; }}
    }}
    .nav-back {{ display: inline-block; margin-bottom: 16px; }}
    h1, h2 {{ margin-top: 0; }}
    .md-button {{
      display: inline-block; padding: 6px 14px; border-radius: 4px;
      background: #3F51B5; color: white; border: none; cursor: pointer;
      font-size: 0.95rem; text-decoration: none;
    }}
    .md-button:hover {{ background: #303F9F; }}
    .md-button--primary {{ background: #FF7043; }}
    .md-button--primary:hover {{ background: #E64A19; }}
  </style>
</head>
<body>
  <a class="nav-back" href="../index.html">&larr; Back to all quizzes</a>
  <div id="quiz-root" class="quiz"></div>

  <script type="application/json" id="quiz-data">
{quiz_json}
  </script>
  <script src="../../assets/js/quiz.js"></script>
</body>
</html>
"""


def build_one(yml_path: Path) -> Path:
    with yml_path.open() as f:
        spec = yaml.safe_load(f)

    # Validate
    required = {"title", "track", "week", "questions"}
    missing = required - spec.keys()
    if missing:
        raise ValueError(f"{yml_path}: missing keys: {missing}")
    for i, q in enumerate(spec["questions"]):
        if not all(k in q for k in ("q", "options", "answer")):
            raise ValueError(f"{yml_path}: question {i} missing fields")
        if not (0 <= q["answer"] < len(q["options"])):
            raise ValueError(
                f"{yml_path}: question {i} answer index {q['answer']} out of range"
            )

    track = spec["track"].lower()
    week = int(spec["week"])
    out_path = OUT_DIR / f"track_{track}" / f"week_{week}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    html = PAGE_TEMPLATE.format(
        title=spec["title"],
        quiz_json=json.dumps(spec, indent=2),
    )
    out_path.write_text(html)
    return out_path


def main():
    if not DATA_DIR.exists():
        print(f"No quiz data dir at {DATA_DIR} — nothing to build.")
        return 0
    yml_files = sorted(DATA_DIR.rglob("*.yml"))
    if not yml_files:
        print("No quiz YAML files found.")
        return 0
    for y in yml_files:
        try:
            out = build_one(y)
            print(f"  built  {out.relative_to(REPO_ROOT)}")
        except Exception as e:
            print(f"  ERROR  {y.relative_to(REPO_ROOT)}: {e}", file=sys.stderr)
            return 1
    print(f"Built {len(yml_files)} quizzes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
