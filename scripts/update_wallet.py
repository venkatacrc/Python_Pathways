#!/usr/bin/env python3
"""
update_wallet.py — update a per-student Progress Wallet page on the static site.

Reads roster.csv (gitignored, instructor-only) for students + their UUID slug.
Reads grades.yml (also gitignored) for current week's totals.
Writes course/wallets/{slug}.md with the rendered wallet card.

Usage:
    python scripts/update_wallet.py                          # update all students
    python scripts/update_wallet.py --student "Ada Lovelace" # one student
    python scripts/update_wallet.py --new                    # generate fresh slugs for new students

roster.csv columns:
    first_name,last_name,email,track,parent_email,slug

grades.yml shape:
    "Ada Lovelace":
      track: B
      quizzes:    [1.00, 1.00, 0.50, 0.00, 1.00, 0.00, 0.00]   # 7 entries (use 0 for not-yet)
      assignments:[1.50, 1.50, 1.50, 0.00, 0.00, 0.00, 0.00]
      capstone:   0.00
"""
from __future__ import annotations

import argparse
import csv
import sys
import uuid
from datetime import datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
ROSTER = REPO_ROOT / "roster.csv"
GRADES = REPO_ROOT / "grades.yml"
OUT_DIR = REPO_ROOT / "course" / "wallets"

PAGE = """---
title: Progress Wallet — {first}
hide:
  - navigation
  - toc
search:
  exclude: true
---

<!--
  Private wallet page. Reachable only by direct URL.
  Updated weekly by the instructor (Venkata Chintapalli) via scripts/update_wallet.py.
  Last updated: {updated}
-->

# 💰 Progress Wallet — {first}

<div class="wallet">
  <h2>{first}'s Wallet</h2>
  <p>Track: <strong>Track {track}</strong> &middot; Last updated: <strong>{updated}</strong></p>
  <table>
    <tr><th>Item</th><th class="amt">Earned</th><th class="amt">Max</th></tr>
    <tr><td>Quizzes (W1–W7)</td><td class="amt">${quiz_total:.2f}</td><td class="amt">$7.00</td></tr>
    <tr><td>Assignments (W1–W7)</td><td class="amt">${asn_total:.2f}</td><td class="amt">$10.50</td></tr>
    <tr><td>Capstone</td><td class="amt">${cap_total:.2f}</td><td class="amt">$12.50</td></tr>
    <tr class="total"><td>TOTAL</td><td class="amt">${grand:.2f}</td><td class="amt">$30.00</td></tr>
  </table>
  <div class="bar"><div style="width: {pct:.1f}%;"></div></div>
  <p class="pct">{pct:.1f}% of $30 earned</p>
</div>

### Week-by-week breakdown

| Week | Quiz | Assignment |
|---:|:---:|:---:|
{week_rows}

!!! tip "How money is earned"
    - Quizzes: ≥70% earns $1.00, 50–69% earns $0.50, below earns $0.
    - Assignments: graded on completion + effort, $1.50 each.
    - Capstone: rubric-graded at the showcase, max $12.50.

*If anything looks wrong, email **{instructor_email}** with subject `[WALLET] {first}`.*
"""


def load_roster() -> list[dict]:
    if not ROSTER.exists():
        print(
            f"roster.csv not found at {ROSTER}. "
            f"See roster.example.csv for the format.",
            file=sys.stderr,
        )
        sys.exit(1)
    with ROSTER.open() as f:
        return list(csv.DictReader(f))


def load_grades() -> dict:
    if not GRADES.exists():
        print(f"grades.yml not found at {GRADES} — using zeros.", file=sys.stderr)
        return {}
    with GRADES.open() as f:
        return yaml.safe_load(f) or {}


def render_one(row: dict, grades: dict) -> Path:
    name = f"{row['first_name']} {row['last_name']}"
    g = grades.get(name, {})
    quizzes = (g.get("quizzes") or []) + [0.0] * 7
    asgs = (g.get("assignments") or []) + [0.0] * 7
    quizzes = quizzes[:7]
    asgs = asgs[:7]
    cap = float(g.get("capstone") or 0.0)
    qt = sum(quizzes)
    at = sum(asgs)
    grand = qt + at + cap
    pct = (grand / 30.0) * 100.0

    week_rows = "\n".join(
        f"| {i + 1} | ${quizzes[i]:.2f} | ${asgs[i]:.2f} |" for i in range(7)
    )
    out_path = OUT_DIR / f"{row['slug']}.md"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        PAGE.format(
            first=row["first_name"],
            track=row["track"],
            updated=datetime.now().strftime("%Y-%m-%d %H:%M"),
            quiz_total=qt,
            asn_total=at,
            cap_total=cap,
            grand=grand,
            pct=pct,
            week_rows=week_rows,
            instructor_email="venkata@densesparse.com",
        )
    )
    return out_path


def cmd_new(roster: list[dict]):
    """Add a UUID slug to any roster row missing one."""
    changed = False
    for row in roster:
        if not row.get("slug"):
            row["slug"] = uuid.uuid4().hex[:12]
            changed = True
    if not changed:
        print("All students already have slugs.")
        return
    fields = list(roster[0].keys())
    if "slug" not in fields:
        fields.append("slug")
    with ROSTER.open("w") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(roster)
    print(f"Wrote new slugs to {ROSTER}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--student", help="Limit to one student (Full Name)")
    p.add_argument("--new", action="store_true", help="Generate UUID slugs for any rows missing one")
    args = p.parse_args()

    roster = load_roster()

    if args.new:
        cmd_new(roster)
        return 0

    grades = load_grades()
    targets = roster
    if args.student:
        targets = [
            r for r in roster
            if f"{r['first_name']} {r['last_name']}" == args.student
        ]
        if not targets:
            print(f"No student named {args.student!r}", file=sys.stderr)
            return 1

    for row in targets:
        if not row.get("slug"):
            print(
                f"  SKIP {row['first_name']} — no slug. Run with --new first.",
                file=sys.stderr,
            )
            continue
        out = render_one(row, grades)
        print(f"  wrote {out.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
