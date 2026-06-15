# ARTIFACT 6 — Capstone Project Rubrics

**General Rules — apply to all 3 tracks:**
- Capstone graded on Thursday, July 30, 2026 during the live Showcase.
- Maximum: **$12.50** per student. Sub-criteria are graded all-or-nothing **unless** half-credit is explicitly listed.
- Instructor scores live during demo; reviews recording before final disbursement on **Aug 3**.
- Borderline cases: instructor uses good judgment + documents reasoning in the wallet update note.
- "Student can explain" criteria require *verbal* explanation in the showcase. Half-credit if the student attempts an explanation but with substantive gaps.

---

## Track A — Game Rubric (Total $12.50) { #track-a-rubric }

| # | Criterion | $ | Half-credit allowed? | What "full credit" looks like |
|---|---|---|---|---|
| 1 | **Game runs without errors** | $2.50 | Yes ($1.25 if it crashes once but recovers; $0 if it fails to start) | The game starts cleanly, the title screen appears, gameplay starts on key press, and runs at least 60 seconds without an error. |
| 2 | **Player can control character** | $2.00 | Yes ($1.00 if only 2 of 4 directions work) | All 4 arrow keys (or WASD or mouse — any documented control scheme) move the character smoothly and the character stays on screen. |
| 3 | **Game has win/lose condition** | $2.00 | Yes ($1.00 if only one of the two is reachable) | Both a victory state (score reached, level finished, etc.) AND a loss state (lives = 0, time out, etc.) can be triggered during the demo. |
| 4 | **Score or lives displayed on screen** | $1.50 | No (either present and updating, or not) | A live counter for score and/or lives is rendered in-game and visibly updates as the game progresses. |
| 5 | **Visual polish (title screen + game-over screen)** | $1.50 | Yes ($0.75 for one of the two) | Distinct title screen with game name + start instruction, and a game-over screen with final score + restart instruction. |
| 6 | **Code organized with functions** | $1.50 | Yes ($0.75 if at least 2 functions but main loop is a wall of code) | At least 3 named functions or class methods structure the code (e.g., `draw_title`, `reset_game`, `update_player`). No giant `while`-loop monolith. |
| 7 | **Student can explain their code in the showcase** | $1.50 | Yes ($0.75 if explanation has gaps) | In the 3-min Q&A, the student can verbally walk through the structure of their game (event loop, state machine, score logic) and answer one follow-up question without panic. |

**Earnings notes:**
- A student who builds a complete, working game with all polish but cannot explain a single piece of it in the showcase **caps at $11.00**. This is intentional — the verbal explanation tests for understanding vs copy-paste.
- A student who has a partially-working game but explains beautifully what they intended and what they hit can earn **$8–10** depending on the components present.

---

## Track B — Patient Risk Tool Rubric (Total $12.50) { #track-b-rubric }

| # | Criterion | $ | Half-credit allowed? | What "full credit" looks like |
|---|---|---|---|---|
| 1 | **Tool accepts patient input correctly** | $2.00 | Yes ($1.00 if input partially works or only via hard-coded values) | Colab form widgets (or `input()` calls) accept all required inputs (≥5 fields), with type coercion handled (e.g., string → float for BMI). No silent crashes on valid inputs. |
| 2 | **Risk calculation is medically logical** | $2.50 | Yes ($1.25 if some weights are arbitrary or contradict published guidelines) | Each input contributes to the risk score with a justification cited in markdown (Framingham, JNC 8, NCEP/ATP, ADA, etc.). Weights are monotonic (higher BP → higher score, never negative). |
| 3 | **Output is color-coded or clearly categorized** | $2.00 | No | The tool produces both a numeric score AND a categorical label (Low/Moderate/High or comparable), with at least the label color-coded in the visual output. |
| 4 | **At least one chart or visualization included** | $2.00 | Yes ($1.00 if a chart is present but lacks title or axis labels) | A bar chart, scatter, or other visualization showing the patient's score against a scale or against the dataset distribution. Must have title + axis labels + units. |
| 5 | **BioPython or real medical dataset used** | $1.50 | Yes ($0.75 if BioPython is present but cosmetic, OR a dataset is loaded but not used in the tool's logic) | Either the tool's calculation references a real public dataset (Heart, PIMA, etc.) for validation/calibration, OR a BioPython-derived "genetic modifier" feeds into the score. |
| 6 | **Student can explain design choices in the showcase** | $2.50 | Yes ($1.25 if some choices are explained, others handwaved) | Student verbally justifies: (a) the choice of 5 inputs; (b) the threshold/weight reasoning; (c) the validation approach; (d) at least 2 honest limitations. |

**Earnings notes:**
- A polished tool that can't be explained tops out at **$10.00**.
- A modest-looking tool with strong reasoning + honest limitations can hit **$11.50+** even without bells and whistles.
- "Color-coded" includes any clear visual distinction — colored chart bar, emoji indicator, ANSI color in console — anything that lets a non-coder see the category without reading code.

---

## Track C — microGPT Rubric (Total $12.50) { #track-c-rubric }

| # | Criterion | $ | Half-credit allowed? | What "full credit" looks like |
|---|---|---|---|---|
| 1 | **`train0` through `train5` all run correctly** | $3.00 | Yes — partial credit per file: `train0=$0.50, train1=$0.50, train2=$0.50, train3=$0.50, train4=$0.50, train5=$0.50` | All 6 progression scripts are committed to GitHub, each file runs end-to-end on the showcase machine without modification. Any breakage drops the corresponding $0.50. |
| 2 | **Custom dataset successfully tokenized and trained** | $2.50 | Yes ($1.25 if data loads + tokenizes but training is incomplete or unstable) | Student's chosen corpus (≥100 KB) loads, tokenizes (char or byte), and trains for ≥5,000 steps without divergence. Final loss visible to instructor in the showcase. |
| 3 | **Model generates coherent (not random) output text** | $2.00 | Yes ($1.00 if output is recognizable patterns but not coherent words/structures) | Sampled output exhibits domain structure: real words for natural language, valid syntax tokens for code, line/stanza patterns for poetry/song lyrics. Better than the train0 baseline qualitatively. |
| 4 | **Student can explain the attention mechanism verbally** | $2.50 | Yes ($1.25 if explanation has gaps in Q/K/V or causal masking) | In the showcase Q&A, student articulates: (a) Q, K, V derivation from input; (b) the dot-product → softmax → weighted-sum; (c) the role of the causal mask; (d) why scale by √D_h. Bonus topic: multi-head intuition. |
| 5 | **Code is clean and commented** | $1.00 | Yes ($0.50 if clean but uncommented, or commented but messy) | Files use consistent style, descriptive variable names, function-level docstrings on the non-trivial parts (Adam.step, attention forward), and no dead code. |
| 6 | **Student presents takeaways and next steps in showcase** | $1.50 | Yes ($0.75 if one of the two is missing or thin) | Student gives at least 2 takeaways from the project (architectural insight, hyperparameter learning, etc.) AND describes a concrete next step they intend to pursue (paper to read, system to build, contribution to make). |

**Earnings notes:**
- A working microGPT trained well but with shaky verbal attention explanation tops out at **$11.25**.
- A clean implementation that doesn't reach a custom-dataset run can still earn **$8–9** if other criteria are strong.
- Penalty for inappropriate library use: if the student silently swapped in `torch.nn` to make life easier and didn't disclose, criteria 1 and 4 both drop to $0 — the whole point of the track is from-scratch.

---

## Live Scoring Sheet (Instructor's Showcase Notebook)

Use this template per student during showcase. Print or keep in a Google Doc.

```
Student: ____________________   Track: A / B / C   Date: 2026-07-30

Track A (Game)                              $    Notes
1. Runs without errors          [_/$2.50]   ___  ____________________
2. Player control               [_/$2.00]   ___  ____________________
3. Win/lose condition           [_/$2.00]   ___  ____________________
4. Score/lives displayed        [_/$1.50]   ___  ____________________
5. Visual polish                [_/$1.50]   ___  ____________________
6. Code organized w/ functions  [_/$1.50]   ___  ____________________
7. Can explain code             [_/$1.50]   ___  ____________________
                              SUBTOTAL = $______ / $12.50

(Repeat structure for Track B and Track C — see rubrics above.)

Quiz total (W1–W7):     $______ / $7.00
Assignment total (W1–W7): $______ / $10.50
Capstone:                $______ / $12.50
GRAND TOTAL:             $______ / $30.00
Disbursement method (Venmo / Zelle / Check):  ____________
Notes / Carry-overs:  __________________________________________
```
