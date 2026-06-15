#!/usr/bin/env python3
"""
make_cert.py — fill the [STUDENT NAME] placeholder in each track's certificate
template, write a per-student copy under course/certificates/{slug}.html, and
optionally print to PDF (browser headless).

Usage:
    python scripts/make_cert.py                      # generate for all students in roster
    python scripts/make_cert.py --student "Ada"      # one student (matches first name)
"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ROSTER = REPO_ROOT / "roster.csv"
TEMPLATES = REPO_ROOT / "course" / "07_certificates"
OUT_DIR = REPO_ROOT / "course" / "certificates"


def render_one(row: dict) -> Path:
    track = row["track"].upper()
    template_path = TEMPLATES / f"track_{track.lower()}_certificate.html"
    if not template_path.exists():
        raise FileNotFoundError(f"No template at {template_path}")

    name = f"{row['first_name']} {row['last_name']}"
    initials = (row["first_name"][:1] + row["last_name"][:1]).upper()
    slug = row.get("slug")
    if not slug:
        raise ValueError(f"Student {name} has no slug — run update_wallet.py --new first")

    html = template_path.read_text()
    html = html.replace("[STUDENT NAME]", name)
    html = html.replace("[STUDENT-INITIALS]", initials)
    html = html.replace("XXXX", slug[:4].upper())

    out_path = OUT_DIR / f"{slug}.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html)
    return out_path


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--student", help="Limit to one student (matches first_name)")
    args = p.parse_args()

    if not ROSTER.exists():
        print(f"roster.csv not found at {ROSTER}", file=sys.stderr)
        return 1

    with ROSTER.open() as f:
        rows = list(csv.DictReader(f))

    if args.student:
        rows = [r for r in rows if r["first_name"] == args.student]
        if not rows:
            print(f"No student matched {args.student!r}", file=sys.stderr)
            return 1

    print(f"Generating certificates · {datetime.now():%Y-%m-%d %H:%M}")
    for row in rows:
        try:
            out = render_one(row)
            print(f"  {row['first_name']:>15s}  →  {out.relative_to(REPO_ROOT)}")
        except Exception as e:
            print(f"  ERROR  {row['first_name']}: {e}", file=sys.stderr)
            return 1
    print(f"\nDone. Each student's certificate is at /certificates/{{slug}}.html on the live site.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
