# ARTIFACT 1 — GitHub Pages Setup Guide

> **Why this replaces the Canvas guide:** Instructure permanently discontinued **Canvas Free for Teachers (FFT)**. We pivoted to a free, future-proof, fully-owned alternative: **GitHub Pages + MkDocs Material + GitHub Actions**, augmented by Google Forms (assignments) and giscus / GitHub Discussions (forum). Total cost: **$0**.

**Audience:** Venkata Chintapalli, Instructor of Record.
**Goal:** Have the site live at `https://densesparse.github.io/python-pathways/` by Sunday, June 14, 2026, 8 PM PST — 22 hours before Week 1 unlocks.

This guide walks you through every command and click. The course content is already written; this guide configures the platform that delivers it.

---

## 0. Pre-flight checklist

- [ ] A GitHub account in good standing for the **`densesparse`** organization (or your personal account).
- [ ] Local Python 3.11+ installed.
- [ ] `git` installed.
- [ ] A **Google Workspace / Gmail** account for Google Forms (assignment submission) and the private grades sheet.
- [ ] A **Zoom** account (any tier — free covers 60-min sessions).
- [ ] The roster as `roster.csv` (use `roster.example.csv` in this repo as a template).

> **Domain decision:** the default `densesparse.github.io/python-pathways/` URL is fine. If you want a custom domain (e.g., `pathways.densesparse.com`), do that in §11 — it's optional.

---

## 1. Create the GitHub repository

```bash
# From your local machine
cd ~/code
git clone git@github.com:densesparse/python-pathways.git
cd python-pathways
```

If the repo doesn't exist yet:

1. Go to `https://github.com/organizations/densesparse/repositories/new`.
2. **Repo name:** `python-pathways`
3. **Description:** *Python Pathways: From Zero to Builder — 7-week course by Dense Sparse, Inc.*
4. **Public.** (Public repos get free GitHub Pages + free GitHub Actions minutes. Per-student PII lives in private Google Sheets, not the repo.)
5. **No README, .gitignore, or license** — the existing repo content has these.
6. Push your local content:
   ```bash
   git remote add origin git@github.com:densesparse/python-pathways.git
   git push -u origin main
   ```

---

## 2. Enable GitHub Pages (build via Actions)

1. Open `https://github.com/densesparse/python-pathways/settings/pages`.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. Save.

That's it. The first push to `main` will trigger `.github/workflows/deploy.yml`, which builds the MkDocs site and publishes it to GitHub Pages.

---

## 3. Local install + first build

Verify everything builds locally before pushing:

```bash
python3 -m venv .venv
source .venv/bin/activate              # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/build_quizzes.py        # builds course/quizzes/track_a/week_1.html (sample)
mkdocs serve                            # http://127.0.0.1:8000/
```

You should see the entire site at `http://127.0.0.1:8000/`. If a page errors out, the terminal tells you which file. Fix locally before pushing.

To deploy: just `git push origin main`. The Actions workflow runs in ~60 seconds and the live site updates.

---

## 4. Configure each student's enrollment

Replace Canvas's email-invite + section-assignment workflow with two clean pieces:

### 4.1 Build the roster

Copy `roster.example.csv` to `roster.csv` (the latter is gitignored), and fill in real data:

```csv
first_name,last_name,email,track,parent_email,slug
Ada,Lovelace,ada@example.com,A,parent.ada@example.com,
Marie,Curie,marie@example.com,B,parent.marie@example.com,
Alan,Turing,alan@example.com,C,,
```

Then generate UUID slugs (used for private wallet/certificate URLs):

```bash
python scripts/update_wallet.py --new
```

This appends a 12-character slug to each row and writes back to `roster.csv`. Slugs are private — never commit `roster.csv` (the `.gitignore` blocks it).

### 4.2 Send the invitation emails

The 3 invitation templates already exist at [Artifact 3](03_invitation_emails.md). For each student:

1. Open the matching template (Track A / B / C).
2. Replace `[CANVAS_LINK]` with `https://densesparse.github.io/python-pathways/`.
3. Add this paragraph at the bottom of every email:
   > *Your private Progress Wallet:* `https://densesparse.github.io/python-pathways/wallets/{slug}/` *— bookmark this URL. It updates every Sunday night with your earnings.*
4. Send from your Gmail. Done.

> **Why no Canvas-style "section override":** The site shows all three tracks publicly. Each student is told which track is theirs. The invitation email is the only "enrollment" — there is no login. We trade strict access control for radical simplicity. Practical security: per-student wallets are at unguessable URLs, and the actual grading data lives in a private Google Sheet only Venkata can see.

---

## 5. Set up assignment submission via Google Forms

Each weekly assignment needs a "submit" channel. Free Google Forms is perfect.

### 5.1 Create one master form

1. Go to `https://forms.google.com` → **Blank form**.
2. **Title:** `Python Pathways · Assignment Submission`
3. Add fields:
   - **Email** (Google auto-collects)
   - **Your full name** — short answer, required
   - **Track** — multiple choice (A / B / C), required
   - **Week** — multiple choice (1–7), required
   - **Submission link** — short answer (Replit URL / Colab URL / GitHub URL), required
   - **What you're proud of** — paragraph, optional
   - **Anything that broke / questions** — paragraph, optional
4. **Settings → Responses → Collect email addresses:** ON.
5. **Send → 🔗 Get link → Shorten URL → Copy.** This is `https://forms.gle/XXXXXXX`.
6. Paste this link into each weekly lesson plan's *"Submit Assignment"* section. (One form serves all 21 assignments — the Track + Week fields disambiguate.)

### 5.2 Set up a second form for quiz score self-reports

1. New form. **Title:** `Python Pathways · Quiz Score Self-Report`.
2. Fields: Name, Track, Week, Score (0–10), Time taken (optional).
3. Same shortened URL → paste into `course/quizzes/data/track_*/week_*.yml` under `submit_url:`.
4. Re-run `python scripts/build_quizzes.py` so the live quiz pages link to the new URL.

> **The honor-system trade-off:** The interactive quiz timer + no-backtracking enforce closed-notes feel, but a student could take the quiz, refresh, and retry. We accept this. The wallet rewards real understanding because the **assignments and capstone reveal whether a student actually internalized the quiz material**. Cheating on a $1 quiz to fail the $12.50 capstone is a poor trade and students figure that out fast.

---

## 6. Set up the discussion forum

We're replacing Canvas Discussions. The right tool varies by track:

### 6.1 Tracks B + C → giscus (GitHub Discussions)

1. Go to `https://github.com/densesparse/python-pathways/settings` → **Features** → enable **Discussions** ✅.
2. Categories — create three:
   - `Track A · 5th Graders` (visibility: announcements-only by maintainer; see §6.2)
   - `Track B · 10th Graders`
   - `Track C · Professionals`
3. Install the **giscus app** at `https://github.com/apps/giscus` and grant it access to this repo.
4. Get your config from `https://giscus.app`: pick the repo, the discussion category, and reaction settings.
5. Copy the resulting `<script src="https://giscus.app/client.js" ...>` block.
6. Open `overrides/main.html` and add a `{% block content %}` section with the giscus embed conditioned on track (we left a hook in the template). For example, add a per-page partial:

    ```html
    {% block content %}
      {{ super() }}
      {% if page.meta and page.meta.giscus_category %}
        <div class="giscus-wrapper">
          <h3>💬 Discussion</h3>
          <script src="https://giscus.app/client.js"
                  data-repo="densesparse/python-pathways"
                  data-repo-id="R_xxx"
                  data-category="{{ page.meta.giscus_category }}"
                  data-category-id="DIC_xxx"
                  data-mapping="pathname"
                  data-strict="0"
                  data-reactions-enabled="1"
                  data-emit-metadata="0"
                  data-input-position="bottom"
                  data-theme="preferred_color_scheme"
                  data-lang="en"
                  crossorigin="anonymous"
                  async>
          </script>
        </div>
      {% endif %}
    {% endblock %}
    ```

7. In each Track B / C lesson plan front matter, add `giscus_category: "Track B · 10th Graders"` (or C). The discussion auto-appears at the bottom of each weekly page.

### 6.2 Track A → Padlet (kid-friendly, no GitHub account required)

5th graders can't sign in to GitHub (COPPA). Use **Padlet** instead:

1. `https://padlet.com` → free account (3 boards).
2. Create a board: *"Track A · Show & Tell"* — Wall layout, posts allowed by anyone with the link, **moderation ON** (Venkata approves before public).
3. Settings → Privacy → **Secret with password**. Share password in the Track A invitation email.
4. Add the Padlet embed snippet to `overrides/main.html` for any page with `padlet_board: "trackA"` in its front matter.

Alternative if Padlet's free tier becomes restrictive: use a **dedicated Gmail label** (`venkata+tracka@densesparse.com`) and have parents email submissions; Venkata curates a weekly "Show & Tell" page committed to the repo on Sunday nights. (Slower but completely free and zero dependencies.)

---

## 7. Set up the gradebook (private Google Sheet)

The public site only shows each student their own wallet card. Real grades live in a private sheet.

1. New Google Sheet → name `Python Pathways · Gradebook · Summer 2026`.
2. **Tab: `Roster`** — paste your roster.csv contents.
3. **Tab: `Quizzes`** — columns: `Student | Track | W1 | W2 | W3 | W4 | W5 | W6 | W7 | Total $`.
4. **Tab: `Assignments`** — same column shape.
5. **Tab: `Capstone`** — `Student | Score | $ Earned | Notes`.
6. **Tab: `Wallet`** — formulas summing the prior tabs into the $30 max.
7. **Sharing:** Restricted, only your own account. Do not share publicly.
8. Optional: connect via **`pygsheets`** in `update_wallet.py` so the wallet updates pull straight from the Sheet (out-of-scope for v1; the YAML file in §8 is enough).

---

## 8. Update student wallets weekly

Every Sunday night:

```bash
# Update grades.yml with this week's earnings (one entry per student)
nano grades.yml

# Regenerate all wallet pages
python scripts/update_wallet.py

# Commit and deploy
git add course/wallets
git commit -m "Wallet update — Week 3 (2026-06-30)"
git push
```

GitHub Actions deploys in ~60 seconds. Each student's wallet URL now reflects the new totals. (Each student's wallet URL never changes — only the contents.)

> **First-time setup tip:** before week 1 even runs, generate everyone's wallet at $0 so the URL exists when you email it:
>
> ```bash
> python scripts/update_wallet.py --new   # create slugs
> python scripts/update_wallet.py         # render with empty grades
> git add course/wallets && git commit -m "Initial wallets" && git push
> ```

---

## 9. Module unlock schedule (client-side)

Canvas had server-side date locks. We have client-side date locks via `course/assets/js/unlock.js`. To gate a weekly module:

1. At the **very top** of any weekly markdown file (before the `# Week N — ...` heading), add:

    ```html
    <script type="application/json" id="unlock-config">
    {"unlock": "2026-07-07T06:00:00-07:00", "label": "Track A · Week 4"}
    </script>
    ```

2. The script in `unlock.js` checks the date in the user's browser. If `now < unlock`, the page content is hidden behind a friendly *"comes back later"* banner.

3. Append `?preview=1` to any locked URL to bypass the gate (useful for instructor preview + parent walkthroughs).

> **Caveat:** this is honor-system gating (a student could disable JS or use `?preview=1`). For a 7-week, 15-student, friend-and-family course this is fine. Real-world locks aren't worth the complexity.

The unlock dates per week (apply to all 3 tracks):

| Week | Unlock (PST) |
|---:|:---|
| 1 | 2026-06-15 06:00 |
| 2 | 2026-06-22 06:00 |
| 3 | 2026-06-29 06:00 |
| 4 | 2026-07-06 06:00 |
| 5 | 2026-07-13 06:00 |
| 6 | 2026-07-20 06:00 |
| 7 | 2026-07-27 06:00 |

---

## 10. Live session links (Zoom)

1. In Zoom → **Schedule a recurring meeting** for each track:
   - Track A — Tue & Thu 6:30–7:30 PM PST, recurring through Jul 30, 2026.
   - Track B — same time slot (you'll run B and C alternately or back-to-back; or co-instruct).
   - Track C — same.
2. Copy the join URL.
3. Add a fenced code block to each Track index page (`04_lesson_plans/track_*/index.md`):

    ```markdown
    ## Zoom

    Tuesdays + Thursdays, 6:30 PM PST → [join here](https://zoom.us/j/XXXXXXXXX) (passcode: ****)
    ```

4. Commit + push.

---

## 11. (Optional) Custom domain

Want `pathways.densesparse.com`?

1. In your DNS provider, add a `CNAME` record for `pathways` pointing to `densesparse.github.io`.
2. In GitHub: **Settings → Pages → Custom domain** → enter `pathways.densesparse.com` → **Enforce HTTPS**.
3. Wait 1–24 hours for DNS to propagate.

---

## 12. Final verification (Sun Jun 14 by 8 PM PST)

- [ ] `https://densesparse.github.io/python-pathways/` loads and shows the home page.
- [ ] All three track index pages render with their week-list.
- [ ] At least one interactive quiz page works end-to-end (start → answer → submit → score).
- [ ] One sample wallet renders at `/wallets/{example-slug}/`.
- [ ] Sample certificate HTML opens cleanly: `/07_certificates/track_a_certificate.html`.
- [ ] Google Form for assignments has been test-submitted by you.
- [ ] giscus appears at the bottom of one Track B page (you posted a test thread).
- [ ] Padlet board for Track A is created + password-locked.
- [ ] All 15 student wallets exist (even if at $0).
- [ ] All 15 invitation emails are drafted in Gmail and ready to send.
- [ ] The 3 welcome announcements are written as `course/news/2026-06-15-welcome.md` (one file with all three).
- [ ] You can build the site cleanly: `mkdocs build --strict` returns exit code 0.

You're ready. Push the welcome announcements at 6:01 AM PST on Mon Jun 15. Send invitations 5 minutes later. Go to bed.

---

## Cheat sheet — common commands

```bash
# Edit content, preview locally
mkdocs serve

# Build the site (strict; fails on broken links)
mkdocs build --strict

# Build all interactive quizzes from YAML
python scripts/build_quizzes.py

# Generate / refresh all wallet pages from grades.yml
python scripts/update_wallet.py

# Generate certificates for everyone (run on Aug 3)
python scripts/make_cert.py

# Push to deploy (Actions handles the rest)
git add . && git commit -m "Week N update" && git push
```
