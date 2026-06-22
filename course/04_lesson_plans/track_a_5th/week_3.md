# Track A — Week 3: "Functions & Your First Pygame Window"

**Dates:** Tue Jun 30 + Thu Jul 2, 2026 · 6:30 PM PST · Replit (Pygame)
**Big Picture:** *Week 3 of 7 — today the GAME WINDOW OPENS! 🎮 Real Pygame, real graphics, your name in the title bar.*
**⚠️ July 4th note:** Thursday July 2 is *not* the holiday-week session — that's Week 3 Thu **July 2**. We've handled the calendar so you're not asked to attend on July 3 or 4. The async make-up applies to anyone who *still* travels for the long weekend; see the bottom of this page.

> **Calendar clarification for Track A:** Per the master schedule, Week 3 sessions are **Tue Jun 30** and **Thu Jul 2**. The "July 3rd Thursday session" referenced in course-wide materials applies to other weekly schedules; for our Tue/Thu cadence, **Thu Jul 2** is the at-risk session because some families leave town Thursday afternoon. The async option below covers exactly that.

---

## SESSION 1 — Tuesday, June 30, 2026

### Learning Objectives
By the end of this session, students can:
1. Define and call a function with parameters.
2. Open a Pygame window with a title and background color.
3. Draw rectangles, circles, and lines on the Pygame screen.

### Active Recall (3 min)
*No notes.* "How do you write an `if/else`? What does `range(5)` produce? What's a variable?" One question per student.

### Big Picture (1 min)
Step 3 of 7 lit. *"Tonight, your game window opens. The title bar has your name on it. This is the first night you can say 'I'm making a video game.'"*

### Block 1 — 25 min — Functions + first Pygame window
1. **Functions (10 min):**
   ```python
   def greet(name):
       print(f"Hello, {name}!")

   greet("Sparky")
   greet("Mochi")

   def add(a, b):
       return a + b

   print(add(3, 4))
   ```
   Hammer the mental model: *function = a recipe with a label*.
2. **First Pygame window (15 min):** in Replit, install Pygame is automatic (or run `pip install pygame` once). Live code:
   ```python
   import pygame, sys
   pygame.init()
   screen = pygame.display.set_mode((640, 480))
   pygame.display.set_caption("Sparky's First Game")  # student personalizes!

   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
       screen.fill((30, 30, 80))   # dark blue
       pygame.draw.rect(screen, (255, 200, 0), (100, 100, 80, 80))
       pygame.draw.circle(screen, (255, 255, 255), (320, 240), 50)
       pygame.display.flip()

   pygame.quit()
   sys.exit()
   ```
   Each student replaces `"Sparky's First Game"` with their own title — instructor pauses for everyone to confirm the window opened on their screen.

### 5-min Pomodoro Break
"Show me one snack" — everyone holds up a snack to the camera. Vote on whose looks tastiest.

### Block 2 — 25 min — Lab: "Decorate Your Window"
Students add:
- 3 different shapes
- 3 different colors (RGB tuples)
- A function `draw_face(screen, x, y, color)` that draws a smiley at a given position. Call it 3 times with different positions/colors.

```python
def draw_face(screen, x, y, color):
    pygame.draw.circle(screen, color, (x, y), 40)
    pygame.draw.circle(screen, (0, 0, 0), (x - 12, y - 10), 5)
    pygame.draw.circle(screen, (0, 0, 0), (x + 12, y - 10), 5)
    pygame.draw.arc(screen, (0, 0, 0), (x - 18, y - 5, 36, 25), 3.14, 0, 3)
```

### 2-min Diffuse Mode Reflection
*"Your game window opened tonight. What's the first thing you'd put on the screen if you could draw it perfectly?"*

### Homework Preview
Thursday: animate a circle bouncing in your window. (Hint: change x, y each frame.)

---

## SESSION 2 — Thursday, July 2, 2026 *(at-risk session — see async option below)*

### Stuck Check Opener (3 min)
"Anyone's window not open yet? Anyone got a colored rectangle to actually appear?" Triage live.

### Big Picture (1 min)
Step 3 still. *"You decorated. Today: stuff MOVES."*

### Block 1 — 25 min — Animation in Pygame
Concept: a Pygame game is a **loop that redraws everything 60 times per second**. To animate, change a variable each loop.
```python
import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

x = 50
speed = 4
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = x + speed
    if x > 600 or x < 40:
        speed = -speed
    screen.fill((20, 20, 40))
    pygame.draw.circle(screen, (255, 100, 100), (x, 240), 30)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
```
Live-code this. Watch the circle bounce. Cheers from students.

### 5-min Pomodoro Break
"Wave to the world" — everyone waves at the camera. Then sit back down.

### Block 2 — 25 min — Lab: "Build a Bouncing Friend"
Students customize:
- Choose: bouncing on the X-axis (horizontal) or Y-axis (vertical) or BOTH (advanced).
- Pick the color, size, and starting speed.
- Add a second bouncing shape.
- Wrap the bouncing logic into a function `update_position(x, speed, max_x)` that returns new x and new speed.

### 2-min Diffuse Mode Reflection
*"That bouncing circle — what would you turn it into in your final game?"*

### Homework Preview
Assignment W3 below — due Mon Jul 6, 11:59 PM PST.

---

### 🌭 ASYNC ALTERNATIVE for Thursday July 2 (or anyone affected by July 4 weekend)
*If you're traveling or busy, you can fully replace the Thursday live session with this async packet. You will still earn the full $1.50 for the assignment and full $1.00 for the quiz.*

1. **Watch:** the recorded Tuesday Jun 30 session (link on this week's course-site page; ~50 min, you can skip the lab portions you've already done).
2. **Read:** the course-site page **"Animating in Pygame — A Visual Walkthrough"** (provided as a 10-screen comic-strip explainer — moves at the speed of one click per concept).
3. **Code-along:** the bouncing circle starter on Replit (link in module), step by step. Estimated time 30 min.
4. **Post in Forum:** drop a screenshot in `[A] Track A Forum` with the tag `#share` and a one-sentence description: *"My bouncing circle is [color] and it's [doing what]."*
5. **Post `#stuck`** if anything broke — instructor responds within 24 hours.

That's it. You're caught up.

---

## WEEK 3 QUIZ — Track A (10 questions, 15 min)

> **Spaced repetition:** Q9 reviews Week 1 (variables/print). Q10 reviews Week 1 (turtle).

**Easy (5)**

1. To define a function in Python, you write:
   - A) `function greet():` · B) `def greet():` · C) `func greet():` · D) `make greet():`

2. What does `pygame.display.set_mode((400, 300))` do?
   - A) Sets the volume · B) Creates a 400×300 game window · C) Saves a file · D) Imports pygame

3. Which is an RGB color for pure red?
   - A) `(0, 255, 0)` · B) `(255, 255, 255)` · C) `(255, 0, 0)` · D) `(0, 0, 255)`

4. To make the game close when you click the X, you check for:
   - A) `pygame.CLOSE` · B) `pygame.QUIT` · C) `pygame.EXIT` · D) `pygame.STOP`

5. What does `return` do in a function?
   - A) Prints something · B) Sends a value back to whoever called the function · C) Stops the program · D) Loops

**Medium (3)**

6. What does this function return?
   ```python
   def double(x):
       return x * 2
   ```
   When you call `double(5)`?
   - A) 5 · B) 7 · C) 10 · D) 25

7. To make a circle bounce off the right edge of a 640-wide window, what condition flips its speed?
   - A) `if x > 0` · B) `if x > 640 - radius` (the circle's right edge crosses the wall) · C) `if x < 0` · D) `if speed > 0`

8. Which line draws a yellow filled rectangle at x=50, y=80, width=100, height=40?
   - A) `pygame.draw.rect(screen, (255, 255, 0), (50, 80, 100, 40))`   - B) `pygame.draw.rect(screen, "yellow", 50, 80, 100, 40)`
   - C) `pygame.rect(screen, yellow, (50, 80, 100, 40))`
   - D) `pygame.draw.rectangle((50, 80), 100, 40)`

**Hard (2)**

9. *(Week 1 review)* What does this print?
   ```python
   name = "Mochi"
   print(f"Hi {name}, you have {3 + 4} treats.")
   ```
   - A) `Hi Mochi, you have 3 + 4 treats.`
   - B) `Hi Mochi, you have 7 treats.`   - C) `Hi {name}, you have 7 treats.`
   - D) Error

10. *(Week 1 review)* After `import turtle` and `t = turtle.Turtle()`, which line draws a square?
    - A) `for i in range(4): t.forward(100); t.right(90)`    - B) `for i in range(3): t.forward(100); t.right(120)`
    - C) `t.square(100)`
    - D) `t.forward(400)`

### Answer Key
1.B  2.B  3.C  4.B  5.B  6.C  7.B  8.A  9.B  10.A

---

## WEEK 3 ASSIGNMENT — Track A

**Title:** *"My Animated Window"*
**Due:** Mon Jul 6, 11:59 PM PST · 45–60 min

### Instructions
Build a Pygame window that contains:
1. A custom title with your name (`set_caption(...)`).
2. A background color *you* choose.
3. **At least 2 shapes** that move (bounce, slide, or change color over time).
4. **At least one function** you defined (e.g., `draw_friend(screen, x, y)`).
5. The window closes cleanly when you click the X.

### Starter Code (linked from this page as a fork-able Replit)
```python
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("[YOUR NAME]'s Window")
clock = pygame.time.Clock()

# TODO: your variables for moving shapes
x = 50
speed = 5

def draw_scene(screen):
    # TODO: draw your shapes here (use the x variable)
    pygame.draw.circle(screen, (255, 200, 0), (x, 240), 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: update positions
    x += speed
    if x > 620 or x < 20:
        speed = -speed

    screen.fill((20, 30, 60))
    draw_scene(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```

### Grading Criteria — $1.50 when:
- [ ] Runs and shows a window (0.40)
- [ ] At least 2 shapes move (0.50)
- [ ] At least 1 student-defined function used (0.30)
- [ ] Custom title bar with student's name (0.10)
- [ ] Closes cleanly on X-click (0.20)

### Stretch
Make a shape change *color* every second. Add a third shape that follows the first one (offset by 100px). Make sound — `pygame.mixer.Sound("boing.wav").play()` when bouncing.

---

## Cumulative Mind Map (Week 3)

Branches grow:

- **🟢 Talking** (W1)
- **🟦 Storing** (W1)
- **🟡 Drawing** — now expands: turtle ↔ **🆕 Pygame** (`set_mode`, `draw.rect`, `draw.circle`, `display.flip`)
- **🟠 Tools** — now: Replit + Pygame
- **🔵 Deciding** (W2)
- **🟣 Repeating** (W2) — now used inside the Pygame loop!
- **🆕 🔴 Functions** — `def`, parameters, `return` — sits between Deciding and Repeating because functions package both.

New connecting line: **Functions** → **Pygame** caption: *"We use functions to organize the drawing of every frame."*
