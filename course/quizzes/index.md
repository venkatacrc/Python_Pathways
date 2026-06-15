---
title: Quizzes
---

# Weekly Quizzes

Every week, every track has a 10-question, 15-minute, no-backtrack quiz. Quizzes open after Tuesday's live session and close Sunday 11:59 PM PST.

> 🧠 **Closed-notes.** The timer + no-backtracking enforce a Canvas-equivalent retrieval-practice setting. Honor system on whether you actually closed your notes — your wallet will reflect what you really know.
>
> ✅ **70%+** earns the full **$1.00** for that week.
> 🟡 **50–69%** earns **$0.50** (partial credit).
> ❌ **< 50%** earns **$0** but you keep your dignity and learn for next week.

## How to take a quiz

1. Click your week's quiz below.
2. Click **▶ Start the quiz** — the timer begins.
3. Pick an answer for each question, click **Next →**.
4. Final question: **Submit**. Your score appears immediately.
5. Click **📨 Report your score to the instructor** — opens a Google Form pre-filled with your week + score.

## Track A — 5th Graders

- [Week 1 — Hello, Python!](track_a/week_1.html) *(example interactive quiz — fully working)*
- *Weeks 2–7 follow the same template; build with `python scripts/build_quizzes.py`.*

## Track B — 10th Graders

- *Weeks 1–7: build with `python scripts/build_quizzes.py` from `course/quizzes/data/track_b/week_*.yml`.*
- The questions are already written in [the lesson plans](../04_lesson_plans/track_b_10th/index.md) — they need only to be entered into the YAML files (template provided).

## Track C — Professionals

- *Weeks 1–7: same workflow as Track B.*

---

## Authoring new quizzes (instructor)

1. Edit or create `course/quizzes/data/track_X/week_N.yml` with this shape:

    ```yaml
    title: "Track A — Week 1 Quiz: Hello, Python!"
    track: A
    week: 1
    time_limit_min: 15
    shuffle: true
    no_backtrack: true
    passing_pct: 70
    submit_url: "https://forms.gle/your-form-here"
    questions:
      - q: "Which line will print exactly: Hello, Sparky!?"
        options:
          - "print(Hello, Sparky!)"
          - 'print("Hello, Sparky!")'
          - 'Print("Hello, Sparky!")'
          - 'print "Hello, Sparky!"'
        answer: 1
        level: easy
      # ... 9 more
    ```

2. Run `python scripts/build_quizzes.py` — generates the matching `.html` page in `course/quizzes/track_X/week_N.html`.
3. Commit + push. The next deploy publishes them.
