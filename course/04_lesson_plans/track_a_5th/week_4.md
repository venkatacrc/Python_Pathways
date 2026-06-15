# Track A — Week 4: "Move It! Sprites & Keyboard Control"

**Dates:** Tue Jul 7 + Thu Jul 9, 2026 · 6:30 PM PST · Replit + Pygame
**Big Picture:** *Week 4 of 7 — your character now MOVES when YOU press a key. This is the moment "drawing on a screen" becomes "playing a game."*

---

## SESSION 1 — Tuesday, July 7, 2026

### Learning Objectives
By the end of this session, students can:
1. Use a Python `list` to store multiple things (like coordinates of bullets, enemies).
2. Read keyboard input with Pygame's event loop.
3. Move a player rectangle/sprite using arrow keys.

### Active Recall (3 min)
"What is `pygame.QUIT` for? What does `clock.tick(60)` do? What's the difference between a function's *parameter* and a *return value*?"

### Big Picture (1 min)
Step 4 of 7. *"Tonight: arrow keys move your guy."*

### Block 1 — 25 min
1. **Lists (8 min):**
   ```python
   colors = ["red", "blue", "green"]
   print(colors[0])
   colors.append("purple")
   print(len(colors))
   for c in colors:
       print(c)
   ```
2. **Reading keys in Pygame (17 min):** *option 1 — `KEYDOWN` event:*
   ```python
   for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:  player_x -= 10
           if event.key == pygame.K_RIGHT: player_x += 10
   ```
   *option 2 — continuous keys (preferred for smooth movement):*
   ```python
   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT]:  player_x -= 5
   if keys[pygame.K_RIGHT]: player_x += 5
   if keys[pygame.K_UP]:    player_y -= 5
   if keys[pygame.K_DOWN]:  player_y += 5
   ```
   Live build a complete moving-square program. Students follow along.

### 5-min Pomodoro Break
"Animal walk break": waddle like a penguin for 30 seconds. (Yes, on camera. Yes, instructor goes first.)

### Block 2 — 25 min — Lab: "My Character Moves!"
Students design their character — a rectangle, circle, or simple Pygame `Surface` they decorate. They make it move with all 4 arrow keys. Constraint: keep it on the screen (clamp x and y to window bounds).

```python
player_x = 320
player_y = 240
size = 30

# inside loop:
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:  player_x -= 5
if keys[pygame.K_RIGHT]: player_x += 5
if keys[pygame.K_UP]:    player_y -= 5
if keys[pygame.K_DOWN]:  player_y += 5

# clamp
if player_x < size:        player_x = size
if player_x > 640 - size:  player_x = 640 - size
if player_y < size:        player_y = size
if player_y > 480 - size:  player_y = 480 - size

screen.fill((10, 10, 30))
pygame.draw.rect(screen, (255, 200, 0), (player_x - size//2, player_y - size//2, size, size))
```

### 2-min Diffuse Mode Reflection
*"Your character now obeys you. What's the FIRST thing you want it to do next?"*

### Homework Preview
Thursday: tiny baby classes. Then we add an enemy.

---

## SESSION 2 — Thursday, July 9, 2026

### Stuck Check Opener (3 min)
"Whose character won't move? Whose moves but goes off-screen? Whose moves too fast?"

### Big Picture (1 min)
Step 4 still. *"Today you organize your character into a 'class' so the game gets easier as it gets bigger."*

### Block 1 — 25 min — Tiny Baby Classes
Why a class? *"Imagine if every enemy has its own x, y, color, and speed. We'd lose track. A class is a 'cookie cutter' for making lots of similar things."*
```python
class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x - 15, self.y - 15, 30, 30))

    def move(self, keys):
        if keys[pygame.K_LEFT]:  self.x -= 5
        if keys[pygame.K_RIGHT]: self.x += 5
        if keys[pygame.K_UP]:    self.y -= 5
        if keys[pygame.K_DOWN]:  self.y += 5

p = Player(320, 240, (0, 255, 100))
# in main loop:
keys = pygame.key.get_pressed()
p.move(keys)
p.draw(screen)
```
Convert Tuesday's working code into this class form. Students rewrite their own.

### 5-min Pomodoro Break
"Type your name with eyes closed" challenge. Show what you typed. Laugh.

### Block 2 — 25 min — Add a Second Thing on Screen
Each student picks: a **food/coin** (collectible, doesn't move), a **wandering enemy** (moves randomly), or a **friendly NPC** (follows the player slowly).

```python
import random
class Coin:
    def __init__(self):
        self.x = random.randint(20, 620)
        self.y = random.randint(20, 460)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 215, 0), (self.x, self.y), 8)

coin = Coin()
# in main loop:
coin.draw(screen)
```

### 2-min Diffuse Mode Reflection
*"You have a player + a coin/enemy/friend on screen now. What rule should the game follow next? (e.g., 'when player touches coin, score +1.')"*

### Homework Preview
Assignment W4 — give your character a *story*.

---

## WEEK 4 QUIZ — Track A (10 questions)

> **Spaced repetition:** Q9 reviews W2 (loops). Q10 reviews W2 (if/else).

**Easy (5)**

1. To check if the LEFT arrow is held down:
   - A) `keys[pygame.LEFT]` · B) `keys[pygame.K_LEFT]` ✅ · C) `keys.LEFT` · D) `keys.left()`

2. What does `colors.append("yellow")` do?
   - A) Removes "yellow" · B) Adds "yellow" to the end of the list ✅ · C) Sorts the list · D) Replaces all colors

3. `len([1, 2, 3, 4])` returns:
   - A) 3 · B) 4 ✅ · C) 5 · D) 0

4. The `__init__` method of a class is the:
   - A) destructor · B) constructor (runs when you make a new object) ✅ · C) drawer · D) saver

5. Which is **NOT** a list?
   - A) `[1, 2, 3]` · B) `["a", "b"]` · C) `(1, 2, 3)` ✅ · D) `[]`

**Medium (3)**

6. What does this print?
   ```python
   nums = [10, 20, 30]
   total = 0
   for n in nums:
       total += n
   print(total)
   ```
   - A) 10 · B) 30 · C) 60 ✅ · D) `[10, 20, 30]`

7. In a class, `self` refers to:
   - A) The class itself · B) The current object/instance ✅ · C) The screen · D) Pygame

8. To keep a player from leaving the right edge of a 640-wide window (player size 30):
   - A) `if x > 640: x = 640` · B) `if x > 610: x = 610` ✅ (if x is the left edge of the player) · C) `if x < 0: x = 0` · D) `if x > 30: x = 30`

**Hard (2)**

9. *(Week 2 review)* What does this print?
   ```python
   for i in range(3):
       for j in range(2):
           print(i, j)
   ```
   - A) 6 lines: `0 0, 0 1, 1 0, 1 1, 2 0, 2 1` ✅
   - B) 3 lines · C) 2 lines · D) 5 lines

10. *(Week 2 review)*
    ```python
    score = 7
    if score > 10:    print("A")
    elif score > 5:   print("B")
    elif score > 0:   print("C")
    else:             print("D")
    ```
    What prints?
    - A) `A` · B) `B` ✅ · C) `C` · D) `D`

### Answer Key
1.B  2.B  3.B  4.B  5.C  6.C  7.B  8.B  9.A  10.B

---

## WEEK 4 ASSIGNMENT — Track A

**Title:** *"Hero on the Move"*
**Due:** Mon Jul 13, 11:59 PM PST

### Instructions
Use a `Player` class to control a character with the arrow keys. Add a second on-screen object (coin, enemy, or friend) that:
- Has its own class.
- Has at least one method besides `__init__` (e.g., `draw`, `move`, or `wander`).

### Starter Code
```python
import pygame, random, sys
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, color):
        self.x = x; self.y = y; self.color = color; self.size = 30
    def draw(self, s):
        pygame.draw.rect(s, self.color, (self.x - self.size//2, self.y - self.size//2, self.size, self.size))
    def move(self, keys):
        # TODO

class Coin:
    def __init__(self):
        self.x = random.randint(20, 620); self.y = random.randint(20, 460)
    def draw(self, s):
        # TODO

p = Player(320, 240, (0, 255, 100))
c = Coin()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False
    keys = pygame.key.get_pressed()
    p.move(keys)
    screen.fill((10, 10, 30))
    c.draw(screen)
    p.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit(); sys.exit()
```

### Grading Criteria — $1.50 when:
- [ ] Player class with `__init__`, `draw`, `move` (0.50)
- [ ] Player moves with all 4 arrow keys (0.30)
- [ ] Stays on screen (no flying off) (0.20)
- [ ] Second class (Coin/Enemy/Friend) with at least 2 methods (0.30)
- [ ] Custom personality: chosen colors, sizes, names (0.20)

### Stretch
Add a *list of 5 coins* using a list comprehension `[Coin() for _ in range(5)]` and draw all of them. (Foreshadows Week 5.)

---

## Cumulative Mind Map (Week 4)

- **🟢 Talking** · **🟦 Storing** (now expanded → **🆕 Lists** ⤴) · **🟡 Drawing/Pygame** · **🟠 Tools**
- **🔵 Deciding** · **🟣 Repeating** · **🔴 Functions** (now expanded → **🆕 Classes** as "fancy functions that hold their own variables")
- New cluster: **🆕 ⌨️ Keyboard** → `pygame.key.get_pressed()` → `K_LEFT/RIGHT/UP/DOWN` → calls into Player.move

Caption: *"Next week: when player meets coin → SCORE!"*
