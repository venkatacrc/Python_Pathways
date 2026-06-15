---
title: Certificates
---

# Certificates of Completion

Every student who completes the course receives a **printable HTML certificate** at their unique URL on **Monday, August 3, 2026** (Certificate Day).

Three designs:

- **Track A** — colorful, fun, game-themed border (5th graders).
- **Track B** — clean, professional, science-themed (10th graders).
- **Track C** — minimal, dark, elegant, with a code-block listing of the `train0..train5` progression (professionals).

## Preview the templates

- [Track A — sample](../07_certificates/track_a_certificate.html)
- [Track B — sample](../07_certificates/track_b_certificate.html)
- [Track C — sample](../07_certificates/track_c_certificate.html)

> Open in a new tab to see the design. Your real certificate will have your name in place of `[STUDENT NAME]`.

## How they're generated

On Aug 3, the instructor runs:

```bash
python scripts/make_cert.py        # generates one HTML per student under course/certificates/{slug}.html
git add course/certificates && git commit -m "Certificates issued — Aug 3, 2026" && git push
```

GitHub Actions deploys, and each student/parent receives an email containing:
- Their unique certificate URL: `https://densesparse.github.io/python-pathways/certificates/{slug}.html`
- Instructions to **Print → Save as PDF** (Letter, landscape, no margins).
- Their final wallet payout method (Venmo / Zelle / check).

## Why HTML?

- Looks beautiful in any modern browser.
- Prints cleanly to PDF on any device — Mac/Windows/Linux/Chromebook/iPad/iPhone all work.
- Is permanently archived in this Git repo.
- Easy to re-print if a student ever loses theirs.
