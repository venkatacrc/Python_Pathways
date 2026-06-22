# Track A — Week 5: "Collision & Scoring"

**Dates:** Tue Jul 14 + Thu Jul 16, 2026 · 6:30 PM PST · Replit + Pygame
**Big Picture:** *Week 5 of 7 — your player and your stuff INTERACT now. Touch a coin → score goes up. Touch a spike → lose a life. This is the heart of every game.*

---

## SESSION 1 — Tuesday, July 14, 2026

### Learning Objectives
By the end of this session, students can:
1. Detect collisions between two rectangles using `pygame.Rect.colliderect()`.
2. Maintain game-state variables (score, lives) across frames.
3. Display the score on screen using `pygame.font`.

### Active Recall (3 min)
"How does a class differ from a function? What's `self`? How do you read which key is pressed?"

### Big Picture (1 min)
Step 5 of 7. *"You can already make stuff move and a window open. Tonight, things start to collide and KEEP SCORE."*

### Block 1 — 25 min — Live build: Coin Collector
1. **Rectangles for collision:**
   ```python
   player_rect = pygame.Rect(player.x - 15, player.y - 15, 30, 30)
   coin_rect = pygame.Rect(coin.x - 8, coin.y - 8, 16, 16)
   if player_rect.colliderect(coin_rect):
       score += 1
       coin.x = random.randint(20, 620)
       coin.y = random.randint(20, 460)
   ```
2. **State variables (5 min):** `score = 0`, `lives = 3`. Initialize *outside* the main loop.
3. **Drawing text (8 min):**
   ```python
   font = pygame.font.SysFont(None, 36)
   text = font.render(f"Score: {score}   Lives: {lives}", True, (255, 255, 255))
   screen.blit(text, (10, 10))
   ```

### 5-min Pomodoro Break
"3 high-fives" — high-five your camera 3 times. Then sit down.

### Block 2 — 25 min — Lab: "Coin Collector v1"
Students build a complete tiny game:
- Player moves with arrows.
- 1 coin on screen — when collected, it teleports to a new random spot, score += 1.
- Score visible at top-left.
- A "win condition" at score = 10 → print `"YOU WIN!"` on screen and stop the game.

### 2-min Diffuse Mode Reflection
*"You just made a game where you can WIN. Describe the moment your score went up the first time."*

### Homework Preview
Thursday: enemies that move on their own. Lose a life when one touches you.

---

## SESSION 2 — Thursday, July 16, 2026

### Stuck Check Opener (3 min)
"Whose collision works? Whose coin disappears too soon? Whose score number doesn't update?"

### Big Picture (1 min)
Step 5 still. *"Coins are rewards. Today: ENEMIES."*

### Block 1 — 25 min — Enemies + Lives
1. **Enemy class with auto-movement (10 min):**
   ```python
   class Enemy:
       def __init__(self):
           self.x = random.randint(20, 620)
           self.y = random.randint(20, 460)
           self.vx = random.choice([-3, 3])
           self.vy = random.choice([-3, 3])
       def update(self):
           self.x += self.vx; self.y += self.vy
           if self.x < 10 or self.x > 630: self.vx = -self.vx
           if self.y < 10 or self.y > 470: self.vy = -self.vy
       def draw(self, s):
           pygame.draw.circle(s, (255, 60, 60), (self.x, self.y), 14)
       def rect(self):
           return pygame.Rect(self.x - 14, self.y - 14, 28, 28)
   ```
2. **Lose a life on collision (8 min):** when player touches enemy, lives -= 1, briefly flash player invisible (`if frame % 4 < 2: draw player`), end game when lives == 0.
3. **Game over screen (7 min):**
   ```python
   if lives <= 0:
       text = font.render("GAME OVER", True, (255, 0, 0))
       screen.blit(text, (240, 220))
       pygame.display.flip()
       pygame.time.delay(3000)
       running = False
   ```

### 5-min Pomodoro Break
"Best monster face" — everyone makes a scary face on camera. Vote.

### Block 2 — 25 min — Lab: "Coin & Spike Game"
Students extend with:
- A list of 3 enemies, all bouncing.
- Score goes up on coin pickup, lives go down on enemy collision.
- Win at score 15. Lose at lives = 0.

### 2-min Diffuse Mode Reflection
*"You have a real game with a winner and loser. What's the BEST feeling and what's the WORST feeling so far?"*

### Homework Preview
Assignment W5 — your first complete win/lose game.

---

## WEEK 5 QUIZ — Track A (10 questions)

> **Spaced repetition:** Q9 reviews W3 (functions). Q10 reviews W3 (Pygame setup).

**Easy (5)**

1. Which method tests if two `pygame.Rect` objects overlap?
   - A) `.collide()` · B) `.colliderect()` · C) `.overlap()` · D) `.touch()`

2. To make text on screen, you first need a:
   - A) `pygame.Font` object via `pygame.font.SysFont(None, 36)`   - B) `pygame.write()` call · C) text variable only · D) print() statement

3. `pygame.font.SysFont(None, 36)` returns:
   - A) the screen · B) a font object you call `.render()` on · C) a number · D) a string

4. To put a rendered text on the screen, you call:
   - A) `screen.put(text)` · B) `screen.blit(text, (x, y))` · C) `pygame.text(...)` · D) `text.draw()`

5. `random.randint(1, 10)` returns:
   - A) Always 1 · B) A random int from 1 to 10 inclusive · C) A float · D) Always 10

**Medium (3)**

6. Score is initialized as `score = 0`. Where is the right place?
   - A) Inside the main `while` loop (resets every frame) — wrong
   - B) Before the main `while` loop — preserves across frames
   - C) Inside `pygame.event.get()` · D) After `pygame.quit()`

7. Why might your collision *seem* not to work?
   - A) Forgot to import pygame · B) Created the rect once outside the loop and never updated its position with the player · C) Wrong color · D) Window too small

8. To make an enemy bounce off walls horizontally, you flip its velocity when:
   - A) `enemy.x < 0 or enemy.x > screen_width` · B) `time > 5` · C) `score > 10` · D) Never

**Hard (2)**

9. *(Week 3 review)* What does this function return?
   ```python
   def is_close(a, b):
       return abs(a - b) < 5
   ```
   When called with `is_close(10, 12)`?
   - A) True · B) False · C) 2 · D) Error

10. *(Week 3 review)* What's wrong with this Pygame setup?
    ```python
    import pygame
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Hi")
    ```
    - A) Forgot `pygame.init()` · B) Wrong resolution · C) Caption can't be "Hi" · D) Nothing wrong

### Answer Key
1.B  2.A  3.B  4.B  5.B  6.B  7.B  8.A  9.A  10.A

---

## WEEK 5 ASSIGNMENT — Track A

**Title:** *"Win-or-Lose Mini Game"*
**Due:** Mon Jul 20, 11:59 PM PST

### Instructions
Build a complete one-screen mini-game with:
1. A player controlled by arrow keys (using a class).
2. **At least 3 collectibles** (coins or whatever — bones, donuts, hearts).
3. **At least 1 enemy** that moves on its own.
4. Visible **score and lives** on screen.
5. A **win condition** (e.g., score >= 5) and a **lose condition** (lives == 0).
6. A **game-over** or **win** message displayed on screen for 2-3 seconds.

### Grading Criteria — $1.50 when:
- [ ] Game runs without errors (0.30)
- [ ] Player collisions with collectibles increase score (0.30)
- [ ] Player collisions with enemies decrease lives (0.30)
- [ ] Score and lives shown on screen (0.20)
- [ ] Both a win-state and a lose-state can occur (0.30)
- [ ] Personalized: chosen colors, theme, custom title (0.10)

### Stretch
Add 2 enemies. Make the enemies' speed increase as score grows. Show different game-over messages depending on which condition ended the game.

---

## Cumulative Mind Map (Week 5)

- **🟢 Talking** · **🟦 Storing** (vars + lists) · **🟡 Drawing/Pygame**
- **🔵 Deciding** · **🟣 Repeating** · **🔴 Functions / Classes**
- **⌨️ Keyboard**
- **🆕 💥 Collisions** → `Rect.colliderect()` → score++/lives--
- **🆕 🔢 Game State** → score, lives, win/lose conditions
- **🆕 🔤 Text on Screen** → font → render → blit

Connect arrows: **Collisions** ↔ **Game State** ↔ **Text on Screen** as the new "gameplay loop" cluster. Caption: *"Next week: polish — title screens, sounds, difficulty."*
