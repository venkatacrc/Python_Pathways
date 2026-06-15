# Track A — Week 1: "Hello, Python!"

**Dates:** Tue Jun 16 + Thu Jun 18, 2026 · 6:30 PM PST · Replit (Python 3 + turtle)
**Big Picture:** *Week 1 of 7 — today is the day you learn how to make a computer talk back. Every cool thing we build later starts here.*

---

## SESSION 1 — Tuesday, June 16, 2026

### Learning Objectives
By the end of this session, students can:
1. Open a Replit project and run a Python program.
2. Use `print()` and `input()` to make the computer respond by name.
3. Draw their first turtle-graphics picture (a smiley face or their initial).

### Active Recall Opener
*Skipped — first session of the course.* Instead: 3-min icebreaker — "What's your favorite video game? What do you wish you could change about it?"

### Big Picture (1 min)
Show a slide: a 7-step staircase. Step 1 is highlighted: *"Today: make the computer say your name and draw a face."* Steps 2–7 are dimmed (decisions → functions → window → moving sprites → collisions → polish → SHOWCASE).

### Block 1 — 25 min (Instructor-led, live coding)
1. **Replit tour (4 min):** create a Python project named `hello-week-1`, identify the editor pane, console pane, and ▶ Run button.
2. **`print()` (5 min):** live code:
   ```python
   print("Hello, world!")
   print("My name is Venkata.")
   print("I am 11 years old.")
   ```
3. **Variables (8 min):** introduce as "labeled boxes":
   ```python
   name = "Venkata"
   age = 11
   print("Hello,", name, "you are", age)
   ```
4. **`input()` (8 min):** the computer asks the student a question:
   ```python
   your_name = input("What is your name? ")
   print("Nice to meet you,", your_name + "!")
   ```

### 5-min Pomodoro Break (Track A flavor)
Stand up. Hop on one foot 10 times. Tell the screen one fact about your favorite animal. (Yes, out loud. Yes, the instructor goes first.)

### Block 2 — 25 min (Students try, instructor circulates)
**Mini-Lab 1 — "The Silly Greeter"**

Students complete this scaffold:
```python
name = input("What's your name? ")
food = input("What's your favorite food? ")
animal = input("What's your favorite animal? ")
print(name, "loves", food, "and the", animal, "agrees!")
print("🎉 You just made the computer talk!")
```

**Mini-Lab 2 — "Smiley Face Turtle"**
```python
import turtle
t = turtle.Turtle()
t.circle(100)
t.penup(); t.goto(-35, 110); t.pendown()
t.dot(20)
t.penup(); t.goto(35, 110); t.pendown()
t.dot(20)
t.penup(); t.goto(-50, 60); t.pendown(); t.right(90)
t.circle(50, 180)
turtle.done()
```
Students change colors, sizes, and add their initial as text using `t.write("V", font=("Arial", 64, "bold"))`.

### 2-min Diffuse Mode Reflection
Course-site journal prompt (post in the discussion): *"What's one thing the computer did today that surprised you?"* (One sentence is enough. We're letting it sink in.)

### Homework Preview
Tuesday-to-Thursday: Try one new turtle command from the Replit tutorials. Bring a screenshot of *anything* you drew to Thursday class.

---

## SESSION 2 — Thursday, June 18, 2026

### Stuck Check Opener (3 min)
Each student shares one thing that confused them since Tuesday. Instructor lists them on screen. Promise: "We'll hit each of these by the end of class."

### Big Picture (1 min)
Step 1 still highlighted. *"Tuesday I showed you. Today you drive. Same step, your hands on the keyboard."*

### Block 1 — 25 min (Quick instructor demo + student-led practice)
1. **Math operators (5 min):** `+ - * / //` and `**`. Quick demo:
   ```python
   print(5 + 3); print(10 / 3); print(10 // 3); print(2 ** 8)
   ```
2. **String tricks (5 min):** `"ha" * 5`, `"-" * 30`, mixing strings + numbers with `f"You are {age} years old"`.
3. **Show-off challenge (15 min):** *"The Computer's Silly Voice"* — students chain `print()` calls to make a one-line poem about themselves using their name, age, favorite food, and a multiplication trick.

### 5-min Pomodoro Break
Two-minute drawing race: draw a square, a triangle, and a circle on paper. Show each other on Zoom.

### Block 2 — 25 min — "Star Pattern Lab" (turtle, no loops yet)
Students draw a 5-pointed star by repeating `t.forward(120); t.right(144)` five times — this previews next week's `for` loop. Bonus: change the color each time using a list of colors `colors = ["red", "blue", "green", "purple", "orange"]` and `t.color(colors[0])` etc.

### 2-min Diffuse Mode Reflection
*"If the computer were a pet, would yours be a puppy or a robot? Why?"*

### Homework Preview
**Assignment W1 due Mon Jun 22, 11:59 PM PST.** See assignment block below.

---

## WEEK 1 QUIZ — Track A (10 questions, 15 min, closed-notes)

> **Spaced repetition note:** No prior weeks → all 10 are current-week.

**Easy (5 questions, 1 pt each)**

1. Which line will print exactly: `Hello, Sparky!`?
   - A) `print(Hello, Sparky!)`
   - B) `print("Hello, Sparky!")` ✅
   - C) `Print("Hello, Sparky!")`
   - D) `print "Hello, Sparky!"`

2. What does `input()` do?
   - A) Prints something on the screen
   - B) Asks the user a question and waits for them to type an answer ✅
   - C) Closes the program
   - D) Imports a library

3. After `pet = "cat"`, what does `print(pet)` show?
   - A) `pet`
   - B) `"cat"`
   - C) `cat` ✅
   - D) Nothing

4. Which symbol means "multiply" in Python?
   - A) `x`
   - B) `*` ✅
   - C) `×`
   - D) `m`

5. What does `print("ha" * 3)` print?
   - A) `ha 3`
   - B) `hahaha` ✅
   - C) `ha * 3`
   - D) Error

**Medium (3 questions, 1 pt each)**

6. What does this code print?
   ```python
   age = 10
   age = age + 1
   print(age)
   ```
   - A) `age`
   - B) `10`
   - C) `11` ✅
   - D) `age + 1`

7. What does `print(7 // 2)` print?
   - A) `3.5`
   - B) `3` ✅
   - C) `4`
   - D) Error

8. Which line uses an *f-string* correctly?
   - A) `print("Hi, name")`
   - B) `print("Hi, " + name)` (works but not an f-string)
   - C) `print(f"Hi, {name}")` ✅
   - D) `print(f"Hi, name")`

**Hard (2 questions, 1 pt each)**

9. The turtle is at position (0, 0) facing right. It runs `t.forward(50); t.left(90); t.forward(50)`. Where is it now?
   - A) (50, 0)
   - B) (50, 50) ✅
   - C) (100, 0)
   - D) (0, 50)

10. What does this code print?
    ```python
    name = input("Name? ")     # user types: Sparky
    print("Hi", name + name)
    ```
    - A) `Hi Sparky`
    - B) `Hi SparkySparky` ✅
    - C) `Hi Sparky Sparky`
    - D) Error

### Answer Key
1.B  2.B  3.C  4.B  5.B  6.C  7.B  8.C  9.B  10.B

---

## WEEK 1 ASSIGNMENT — Track A

**Title:** *"Meet My Mascot" — Make the Computer Introduce Your Pet, Toy, or Hero*
**Due:** Mon Jun 22, 11:59 PM PST · 45–60 min · Submit a Replit share-link via the [Assignment Google Form](https://forms.gle/REPLACE_WITH_REAL_FORM)

### Instructions
Build a small Python program that:
1. Asks the user 3 questions (name, color, super-power) using `input()`.
2. Prints a 3-line "introduction" using f-strings.
3. Uses turtle graphics to draw the mascot's "face" — at minimum a colored circle with two dots for eyes.
4. Adds the mascot's name written under the face using `t.write(...)`.

### Starter Code
```python
import turtle

mascot_name = input("What is your mascot's name? ")
mascot_color = input("What color is your mascot? ")
power = input("What is its super-power? ")

print(f"Meet {mascot_name}!")
print(f"{mascot_name} is {mascot_color} and can {power}.")
print(f"Watch out, world — here comes {mascot_name}!")

t = turtle.Turtle()
t.color(mascot_color)
t.begin_fill()
t.circle(80)
t.end_fill()

# TODO: add two eyes
# TODO: write the mascot's name below the face

turtle.done()
```

### Grading Criteria — full $1.50 earned when:
- [ ] Program runs without errors in Replit (0.50)
- [ ] All 3 `input()` questions used and printed back (0.30)
- [ ] Turtle drawing has at least a face + 2 eyes + name (0.50)
- [ ] Student personalized the mascot (custom name/color/power, not the example) (0.20)

### Optional Stretch (no extra $$ — just bragging rights)
Make the mascot have **a tail, a hat, or a third eye**. Post a screenshot in the Track A Forum with the tag `#share`.

---

## Cumulative Mind Map (Week 1)

A visual concept map for the course-site weekly page. Center node = **PYTHON**. From it, 4 branches:

- **🟢 Talking** → `print()` → `input()` → `f"strings"`
- **🟦 Storing** → variables → numbers (`+ - * / //`) → strings (`+ *`)
- **🟡 Drawing** → `import turtle` → `t.forward()` / `t.right()` → `t.color()` / `t.dot()` / `t.write()`
- **🟠 Tools** → Replit → Run button → console

Render the mind map as a PNG (free tool: `https://app.diagrams.net` or hand-drawn on iPad), commit it to `course/assets/mindmaps/track_a/week_1.png`, and reference it from this page. Add a label: *"This is everything we know so far. Next week: making the computer DECIDE."*
