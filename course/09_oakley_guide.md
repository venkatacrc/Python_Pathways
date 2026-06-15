# ARTIFACT 9 — Barbara Oakley Technique Implementation Guide

*A 1-page instructor reference (and parent talking-points sheet). Eight techniques from Barbara Oakley's *Learning How to Learn*, where each appears in this 7-week course, and one concrete example from each track.*

---

### How to use this page

When a parent asks *"How does this course teach my kid to LEARN, not just to code?"* — open this page. Each row gives you (a) the technique, (b) the everyday name parents will recognize, (c) **where it lives in this course**, and (d) **one concrete example per track** so you can speak from a place of specificity.

---

### 1. Pomodoro Technique
**Plain English:** *Focused 25-minute work blocks separated by 5-minute breaks.*
**Where it lives:** Every single 60-minute live session is structured 25–5–25–5. Same in office hours.
- **Track A example (5th):** Week 4 Tuesday — Block 1 is 25 min "Lists + reading keys" instructor-led; the break is "waddle like a penguin"; Block 2 is 25 min "My Character Moves!" hands-on lab; close with 2 min reflection.
- **Track B example (10th):** Week 3 Tuesday — Block 1 is 25 min matplotlib instructor-led; break is the 20-20-20 eye rule; Block 2 is 25 min "3 charts" lab.
- **Track C example (Pro):** Week 2 Tuesday — Block 1 is 25 min "MLP math by hand"; break is discretionary; Block 2 is 25 min `train1.py` live build.
**Why parents care:** Kids' attention spans cap out around this length. Adults' too. We respect the limit.

---

### 2. Spaced Repetition
**Plain English:** *You forget faster than you'd think. We bring back old material on purpose.*
**Where it lives:** Every weekly quiz from Week 3 onward includes 2 questions revisiting content from 2 weeks prior.
- **Track A example:** Week 3 Quiz Q9 reviews Week 1 f-strings; Q10 reviews Week 1 turtle.
- **Track B example:** Week 4 Quiz Q9–Q10 review Week 2 `groupby` + multi-condition filters.
- **Track C example:** Week 5 Quiz Q9–Q10 review Week 3 `Value` autograd dunder methods.
**Why parents care:** It's the difference between "I learned that once" and "I can use that next year."

---

### 3. Retrieval Practice
**Plain English:** *Closed-book quizzes; pulling answers from memory rather than recognizing them on a page.*
**Where it lives:** Every weekly quiz is **closed-notes**, 15-min timed, single attempt, no backtracking. Assignments, by contrast, allow all resources — different muscles for different tools.
- **Track A example:** Week 5 quiz — student must remember `pygame.Rect.colliderect()` without searching.
- **Track B example:** Week 4 quiz — student must recall the formula for an independent t-test interpretation.
- **Track C example:** Week 6 quiz — student must derive Adam's update rule structure from memory.
**Why parents care:** Recognition is shallow; recall is deep.

---

### 4. Interleaving
**Plain English:** *Mix new material with review problems in the same session.*
**Where it lives:** Every Block 2 lab includes at least one element from a previous week. Every Tuesday opener has a 3-min Active Recall on prior content.
- **Track A example:** Week 5 Block 2 ("Coin Collector v1") uses lists (W4), classes (W4), keyboard input (W4), and brand-new collision code (W5). All in 25 min.
- **Track B example:** Week 6 risk-tool builds on pandas filtering (W2), visualization (W3), and statistical reasoning (W4) — interleaved into one project.
- **Track C example:** Week 4 `train3.py` reuses the autograd `Value` (W3), the bigram corpus (W1), and SGD/lr concepts (W2) all at once.
**Why parents care:** Real-world problems never come labeled with a chapter. Practicing the mix builds transfer.

---

### 5. Chunking
**Plain English:** *Break a big idea into the smallest piece a brain can hold; only THEN connect chunks.*
**Where it lives:** Every concept introduced in stages. Every session opens with a "Big Picture" slide that places today inside the 7-week ladder.
- **Track A example:** Week 4 introduces *classes* via the smallest possible Player class with 3 methods, before adding a Coin/Enemy/Friend class.
- **Track B example:** Week 4 introduces statistics in the order: `mean` → `std` → `correlation` → `t-test`. Each chunk lands before the next.
- **Track C example:** Week 3 introduces `Value` one operator at a time (`__add__`, then `__mul__`, then `__pow__`, etc.) before composing into an MLP.
**Why parents care:** Overwhelm shuts learning down. Chunking keeps the pump primed.

---

### 6. Diffuse Mode
**Plain English:** *Sometimes the brain solves problems best when you AREN'T trying — like in the shower.*
**Where it lives:** Every session ends with a 2-min reflection prompt the student writes in the course-site discussion thread for that week. After class, they're encouraged to walk away. The journal is informal and ungraded.
- **Track A example:** Week 3 close: *"Your game window opened tonight. What's the first thing you'd put on the screen if you could draw it perfectly?"*
- **Track B example:** Week 5 close: *"You're 30 lines of code away from doing something a lab tech does. What WOULD a clinical genetics lab do next that you couldn't yet?"*
- **Track C example:** Week 6 close: *"You built a GPT in 200 lines. What does that tell you about what GPT-4 is — and isn't?"*
**Why parents care:** Telling kids "go play outside, your brain will figure it out" is now backed by neuroscience. We trust the diffuse mode.

---

### 7. Active Recall (Opener variant)
**Plain English:** *Start every session by trying to remember last time's content from scratch — no notes.*
**Where it lives:** Every Tuesday session begins with a 3-min, no-notes recall challenge from the previous session. Thursday begins with a "Stuck Check" — students name one thing that confused them.
- **Track A example:** Week 4 Tuesday opener: *"What is `pygame.QUIT` for? What does `clock.tick(60)` do? What's the difference between a function's *parameter* and a *return value*?"*
- **Track B example:** Week 5 Tuesday opener: *"What's a t-test for? What's a p-value? What's the strongest correlation we found last week?"*
- **Track C example:** Week 4 Tuesday opener: *"What's `Value.backward()` doing? What's `softmax(logits) - onehot(y)` give you? Why accumulate (`+=`) gradients?"*
**Why parents care:** This 3-minute warmup teaches the student that *trying to remember* IS studying — not the same as re-reading.

---

### 8. Mind Maps
**Plain English:** *A growing visual diagram that shows how every concept connects.*
**Where it lives:** Each week's course-site page ends with an updated cumulative mind map. By Week 7, the map covers everything from Day 1.
- **Track A example:** Week 7's final mind map fans from PYTHON into Talk → Store → Draw → Decide → Repeat → Functions/Classes → Keyboard → Collisions → Game States → Sound → Difficulty.
- **Track B example:** Week 7's final mind map shows MEDICAL PYTHON branching into Python core → Pandas → Visualization → Statistics → BioPython → The Risk Tool, with cross-links between Cohorts ↔ Charts ↔ p-values.
- **Track C example:** Week 7's final mind map is the microGPT staircase: bigram → MLP → autograd → 1-head attention → multi-head + LN → Adam → showcase, with each rung annotated with the Python concept it taught.
**Why parents care:** Math and code can feel like a heap of rules. The mind map is *proof of structure* — your kid will see it as one connected idea by week 7, not 49 unrelated days.

---

### 30-second elevator pitch (for Venkata to repurpose)

> "Most coding bootcamps teach Python. We also teach how to learn. Eight specific techniques from Barbara Oakley's research are baked into every session: focused work blocks, brain-friendly breaks, deliberate forgetting and re-encountering, mixing new with old, breaking ideas into chunks, taking the brain seriously when it's NOT trying, recalling instead of re-reading, and visualizing concept maps. By the end of seven weeks, your child not only built a [game / risk tool / GPT], they also have a learning operating system they can apply to anything next."
