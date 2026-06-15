# Track A — Week 2: "Making Decisions & Repeating Things"

**Dates:** Tue Jun 23 + Thu Jun 25, 2026 · 6:30 PM PST · Replit
**Big Picture:** *Week 2 of 7 — last week the computer talked. This week, it thinks ("if/else") and it works without getting tired (loops). With these two superpowers, you can already make tiny games.*

---

## SESSION 1 — Tuesday, June 23, 2026

### Learning Objectives
By the end of this session, students can:
1. Use `if`, `elif`, and `else` to make a program decide what to do.
2. Use a `while` loop to repeat actions until something is true.
3. Use a `for` loop with `range()` to draw a turtle pattern.

### Active Recall Opener (3 min)
"No notes, no Replit. Tell me — what does `print()` do? What does `input()` do? What does `t.forward(100)` do?" Each student answers one. If anyone is stuck, the group helps.

### Big Picture (1 min)
Highlight Step 2 of 7. *"Decisions + repeats. Almost every video game alive today is built on these two ideas."*

### Block 1 — 25 min (Instructor-led live coding)
1. **`if/else` (8 min):**
   ```python
   age = int(input("How old are you? "))
   if age >= 13:
       print("You're a teenager!")
   else:
       print("You're a kid (so am I, kind of).")
   ```
   Then add `elif`:
   ```python
   if age >= 18:   print("Adult!")
   elif age >= 13: print("Teen!")
   else:           print("Kid!")
   ```
2. **`while` loop (8 min):** "Keep asking until they say *quit*":
   ```python
   word = ""
   while word != "quit":
       word = input("Say something (type 'quit' to stop): ")
       print("You said:", word)
   ```
3. **`for` loop with range (9 min):** turtle spiral:
   ```python
   import turtle
   t = turtle.Turtle()
   t.speed(0)
   for size in range(1, 100):
       t.forward(size * 2)
       t.right(91)
   turtle.done()
   ```

### 5-min Pomodoro Break
Stand up. Spin slowly in a full circle. Sit down. Tell the group one thing in your room that's the same color as your favorite Pokémon.

### Block 2 — 25 min (Students try)
**Mini-Lab — "Magic 8 Ball"** Random answers + `if/elif`:
```python
import random
ball = ["Yes!", "No way", "Ask me later", "Definitely", "Hmm... maybe"]
question = input("Ask the 8-ball anything: ")
choice = random.choice(ball)
print("🎱", choice)
```
Extension: also draw a black circle with the answer written inside using turtle.

### 2-min Diffuse Mode Reflection
Course-site journal (post in the discussion): *"What's a real-life decision you made today that was like an `if/else`?"* (E.g., "If it was raining, I wore boots, else sneakers.")

### Homework Preview
Mini "Guess the Number" game on Thursday. Try a `while` loop on your own before then.

---

## SESSION 2 — Thursday, June 25, 2026

### Stuck Check Opener (3 min)
"What broke between Tuesday and now?" — capture each student's stuck point on screen.

### Big Picture (1 min)
Step 2 still. *"You build the first game today. A real one. With a winner."*

### Block 1 — 25 min — Live Build: "Guess the Number"
Instructor and students together write the same code in real-time:
```python
import random
secret = random.randint(1, 20)
guess = 0
tries = 0
print("I'm thinking of a number from 1 to 20.")
while guess != secret:
    guess = int(input("Your guess? "))
    tries = tries + 1
    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
print(f"You got it in {tries} tries! 🎉")
```
Stop after each line. Ask: *"What do you think happens next?"* This builds prediction muscle.

### 5-min Pomodoro Break
"Quietest 30 seconds" — everyone mutes; first to break the silence loses. Then everyone laughs.

### Block 2 — 25 min — Student Choice Mini-Lab
Pick one:
- **Option A:** Modify Guess the Number — limit to 5 tries, lose if they run out.
- **Option B:** Loop a turtle pattern (rosette of 12 squares rotated 30° each).
- **Option C:** Combine — draw a turtle X each wrong guess, draw a smiley each correct guess.

Instructor circulates. Each student shares their screen for 30 seconds at the end.

### 2-min Diffuse Mode Reflection
*"Today the computer guessed YOUR number — wait, the other way around. What's one thing you wish the computer would do for you?"*

### Homework Preview
Assignment W2 (below) — due Mon Jun 29, 11:59 PM.

---

## WEEK 2 QUIZ — Track A (10 questions, 15 min, closed-notes)

> **Spaced repetition note:** Week 1 retro. Q9 + Q10 are Week 1 review.

**Easy (5)**

1. Which keyword starts a "decision" in Python?
   - A) `decide` · B) `if` ✅ · C) `choose` · D) `case`

2. How many times does this run?
   ```python
   for i in range(4):
       print("hi")
   ```
   - A) 0 · B) 3 · C) 4 ✅ · D) 5

3. `if pet == "cat":` — what does `==` mean?
   - A) Assign a value · B) Compare values for equality ✅ · C) Add · D) Print

4. Which line picks a random item from a list?
   - A) `random.pick(...)` · B) `random.choice(...)` ✅ · C) `random.item(...)` · D) `pick.random(...)`

5. What does `range(3)` give us?
   - A) `1, 2, 3` · B) `0, 1, 2` ✅ · C) `0, 1, 2, 3` · D) `3, 2, 1`

**Medium (3)**

6. What does this print?
   ```python
   x = 5
   if x > 10:
       print("big")
   elif x > 3:
       print("medium")
   else:
       print("small")
   ```
   - A) `big` · B) `medium` ✅ · C) `small` · D) Nothing

7. The `while` loop below stops when:
   ```python
   lives = 3
   while lives > 0:
       lives = lives - 1
   ```
   - A) `lives` becomes 0 ✅ · B) `lives` becomes 1 · C) Never · D) After 1 step

8. Which combo draws a square with a `for` loop?
   - A) `for i in range(4): t.forward(50); t.right(90)` ✅
   - B) `for i in range(3): t.forward(50); t.right(90)`
   - C) `for i in range(4): t.forward(50); t.right(60)`
   - D) `while True: t.forward(50); t.right(90)`

**Hard (2)**

9. *(Week 1 review)* What does `print("ha" * 3)` print?
   - A) `ha3` · B) `hahaha` ✅ · C) `ha * 3` · D) Error

10. *(Week 1 review)* After `name = input("Name? ")` and the user types `Sparky`, what type is the variable `name`?
    - A) integer · B) float · C) string ✅ · D) list

### Answer Key
1.B  2.C  3.B  4.B  5.B  6.B  7.A  8.A  9.B  10.C

---

## WEEK 2 ASSIGNMENT — Track A

**Title:** *"Pet-Care Decision Helper"*
**Due:** Mon Jun 29, 11:59 PM PST · 45–60 min · Submit Replit share-link via the [Assignment Google Form](https://forms.gle/REPLACE_WITH_REAL_FORM)

### Instructions
Write a program that helps decide what to do for a pet based on a few inputs:
1. Ask the user: *species* (dog/cat/fish), *hunger level* (1–10), *energy level* (1–10).
2. Use `if/elif/else` to print **at least 3 different recommendations** (e.g., "Feed Whiskers!", "Take Buddy for a walk!", "Goldie just needs a clean tank.").
3. Use a `while` loop so the user can ask again until they type `quit`.
4. **Bonus turtle:** draw a happy face if both hunger and energy are below 5; sad face otherwise.

### Starter Code
```python
import turtle

while True:
    species = input("Pet species (dog/cat/fish/quit)? ")
    if species == "quit":
        print("Goodbye!")
        break

    hunger = int(input("Hunger 1-10? "))
    energy = int(input("Energy 1-10? "))

    # TODO: write your if/elif/else logic here

    # TODO: turtle drawing here
```

### Grading Criteria — $1.50 when:
- [ ] Runs without errors (0.50)
- [ ] Uses `if/elif/else` for at least 3 distinct outcomes (0.40)
- [ ] Loops with `while` and exits on "quit" (0.30)
- [ ] Some turtle output exists (any shape) (0.30)

### Stretch (bragging only)
Add a fourth species. Add an emoji to each recommendation. Make the turtle drawing change with the species too.

---

## Cumulative Mind Map (Week 2)

Center: **PYTHON**. Branches:

- **🟢 Talking** (W1): `print` · `input` · f-strings
- **🟦 Storing** (W1): variables · numbers · strings
- **🟡 Drawing** (W1): turtle · forward/right · color
- **🟠 Tools** (W1): Replit · Run · console
- **🆕 🔵 Deciding** (W2): `if` · `elif` · `else` · `==`, `!=`, `<`, `>`
- **🆕 🟣 Repeating** (W2): `for ... in range()` · `while ...:` · loop body indented

Add a connecting arrow from **🟣 Repeating** → **🟡 Drawing**: "We can now draw spirals, stars, mandalas — anything that repeats!" Caption: *"Next week: a real Pygame WINDOW opens for the first time."*
