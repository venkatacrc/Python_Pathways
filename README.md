# Python Pathways: From Zero to Builder

A 7-week, 3-track Python course taught by **Venkata Chintapalli** at **Dense Sparse, Inc.**, June 16 – August 3, 2026.

> **Platform note:** Originally designed for Canvas Free for Teachers. Instructure discontinued FFT, so the course was migrated to **GitHub Pages + MkDocs Material**. See [`course/MIGRATION.md`](course/MIGRATION.md) for the full Canvas → GH Pages mapping. Cost remains $0.

🌐 **Live site:** `https://densesparse.github.io/python-pathways/` *(builds automatically on push to `main`)*

---

## Quickstart for the instructor

```bash
git clone git@github.com:densesparse/python-pathways.git
cd python-pathways
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Build all interactive quizzes from YAML
python scripts/build_quizzes.py

# Preview locally
mkdocs serve   # → http://127.0.0.1:8000/
```

When ready: `git push origin main` → GitHub Actions builds and deploys to Pages in ~60 seconds.

---

## Repo layout

```
.
├── README.md                          ← you are here
├── mkdocs.yml                         ← site config (theme, nav, plugins)
├── requirements.txt                   ← MkDocs + plugins
├── roster.example.csv                 ← copy to roster.csv (gitignored)
├── grades.example.yml                 ← copy to grades.yml (gitignored)
├── overrides/main.html                ← site-wide announce bar + giscus hook
├── .github/workflows/deploy.yml       ← GH Actions: build + deploy on push
├── scripts/
│   ├── build_quizzes.py               ← YAML → interactive HTML quizzes
│   ├── update_wallet.py               ← roster + grades → per-student wallet pages
│   └── make_cert.py                   ← roster → per-student certificate HTMLs
└── course/                            ← MkDocs `docs_dir`; everything below is published
    ├── index.md                       ← landing page
    ├── 01_github_pages_setup.md       ← Artifact 1 (formerly Canvas setup)
    ├── 02_parent_onboarding.md        ← Artifact 2
    ├── 03_invitation_emails.md        ← Artifact 3
    ├── 04_lesson_plans/{a,b,c}/       ← Artifact 4 — 21 weekly lesson plans
    ├── 05_office_hours/               ← Artifact 5 — 21 office-hour agendas
    ├── 06_capstone_rubrics.md         ← Artifact 6
    ├── 07_certificates/*.html         ← Artifact 7 — 3 certificate templates
    ├── 08_resources.md                ← Artifact 8
    ├── 09_oakley_guide.md             ← Artifact 9
    ├── MIGRATION.md                   ← Canvas → GH Pages decisions
    ├── assets/
    │   ├── css/extra.css              ← track badges, wallet card, quiz UI
    │   └── js/{quiz.js,unlock.js}     ← interactive quiz + module unlock
    ├── quizzes/
    │   ├── index.md
    │   ├── data/track_*/week_N.yml    ← quiz source-of-truth
    │   └── track_*/week_N.html        ← built by scripts/build_quizzes.py
    ├── wallets/                       ← per-student `{slug}.md` (built by script)
    └── certificates/                  ← per-student `{slug}.html` (built by script)
```

## Course calendar

- **Live sessions:** Tuesdays + Thursdays, 6:30–7:30 PM PST on Zoom
- **First session:** Tue Jun 16, 2026
- **Capstone Showcase:** Thu Jul 30, 2026
- **Certificate Day:** Mon Aug 3, 2026 (no live session — disbursements + certificates)

| Week | Tue | Thu | Notes |
|---:|:---|:---|:---|
| 1 | Jun 16 | Jun 18 | |
| 2 | Jun 23 | Jun 25 | |
| 3 | Jun 30 | **Jul 2** | Async option in all 3 Week-3 plans for July 4 weekend |
| 4 | Jul 7  | Jul 9  | |
| 5 | Jul 14 | Jul 16 | |
| 6 | Jul 21 | Jul 23 | |
| 7 | Jul 28 | **Jul 30** | 🏆 Capstone Showcase |

## Tracks

- **Track A — 5th Graders** · Replit · Pygame games — [overview](course/04_lesson_plans/track_a_5th/index.md)
- **Track B — 10th Graders** · Google Colab · Medical Python — [overview](course/04_lesson_plans/track_b_10th/index.md)
- **Track C — Professionals** · Pure Python · microGPT — [overview](course/04_lesson_plans/track_c_pro/index.md)

## Hard-constraint compliance

- ✅ Track A code runs in Replit; Track B code runs in Colab on a Chromebook; Track C uses Python stdlib only.
- ✅ Every session ends with a parent-showable artifact.
- ✅ Week 3 Thursday async alternatives in all 3 tracks.
- ✅ Track A quiz scenarios use only games / animals / food.
- ✅ Track B medical examples use only public datasets (UCI, Kaggle, NCBI).
- ✅ Track C matches Karpathy's microGPT philosophy (minimal, readable, no magic).
- ✅ Course is fully deliverable on **GitHub Pages free tier** — no paid plugins.

## Instructor

**Venkata Chintapalli** · Founder & Instructor, *Dense Sparse, Inc.* · `venkata@densesparse.com`
