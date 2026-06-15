# Track A — Week 6: "Polish Your Game"

**Dates:** Tue Jul 21 + Thu Jul 23, 2026 · 6:30 PM PST · Replit + Pygame
**Big Picture:** *Week 6 of 7 — your game already WORKS. This week you make it FEEL like a real game: title screen, sounds, difficulty levels, comments. Next week, you demo it.*

---

## SESSION 1 — Tuesday, July 21, 2026

### Learning Objectives
By the end of this session, students can:
1. Build a title screen and a game-over screen using a `state` variable.
2. Add sound effects with `pygame.mixer`.
3. Comment their code so a friend (or future self) can understand it.

### Active Recall (3 min)
"What's `colliderect()`? Where do you initialize `score = 0`? What's the difference between a list and a tuple?"

### Big Picture (1 min)
Step 6 of 7. *"Tonight: real game vibes. Title screen with PRESS SPACE TO START. Game over with PRESS R TO RESTART."*

### Block 1 — 25 min — Game States
Pattern: a `state` variable controls which screen we draw.
```python
state = "title"   # "title" -> "playing" -> "game_over"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if state == "title" and event.key == pygame.K_SPACE:
                state = "playing"
            elif state == "game_over" and event.key == pygame.K_r:
                # reset everything
                score = 0; lives = 3; player.x = 320; player.y = 240
                state = "playing"

    if state == "title":
        screen.fill((0, 0, 30))
        big = pygame.font.SysFont(None, 72)
        small = pygame.font.SysFont(None, 32)
        screen.blit(big.render("DONUT DASH", True, (255, 200, 0)), (180, 160))
        screen.blit(small.render("Press SPACE to start", True, (200, 200, 200)), (210, 280))
    elif state == "playing":
        # all your existing gameplay code goes here
        ...
    elif state == "game_over":
        screen.fill((30, 0, 0))
        big = pygame.font.SysFont(None, 72)
        screen.blit(big.render(f"GAME OVER  Score: {score}", True, (255, 80, 80)), (80, 200))
        small = pygame.font.SysFont(None, 32)
        screen.blit(small.render("Press R to restart", True, (255, 255, 255)), (220, 280))

    pygame.display.flip()
```

### 5-min Pomodoro Break
"Sing your game's theme song" — make up a 5-second jingle for your game. Each person performs.

### Block 2 — 25 min — Lab: Add States to *Your* Game
Students wrap their Week 5 game in this state pattern. Three screens minimum: title, playing, game-over.

### 2-min Diffuse Mode Reflection
*"What's your game's TITLE? Tell us in 1 sentence what makes it special."*

### Homework Preview
Thursday: sounds + difficulty levels.

---

## SESSION 2 — Thursday, July 23, 2026

### Stuck Check Opener (3 min)
"Whose state machine works? Whose Restart actually resets? Whose Title Screen looks the coolest?" Quick screen-share circle.

### Big Picture (1 min)
Step 6 still. *"SOUND. The big upgrade. Coin pickups go ding! Hits go thud!"*

### Block 1 — 25 min — Sound + Difficulty
1. **`pygame.mixer` (10 min):**
   ```python
   pygame.mixer.init()
   coin_sound = pygame.mixer.Sound("coin.wav")  # any free .wav
   hit_sound  = pygame.mixer.Sound("hit.wav")
   bg_music   = pygame.mixer.music
   bg_music.load("background.mp3")
   bg_music.play(-1)   # -1 = loop forever
   ```
   In collision handler: `coin_sound.play()` / `hit_sound.play()`. Free sound source: `freesound.org` (point students at instructor-curated 3 files linked from this week's page).
2. **Difficulty (10 min):** add a level variable. Every 10 points, level += 1, enemy speeds increase. Show "LEVEL 2!" briefly on screen.
3. **High score with file I/O (5 min, optional intro):**
   ```python
   try:
       with open("highscore.txt") as f: high = int(f.read())
   except: high = 0
   if score > high:
       with open("highscore.txt", "w") as f: f.write(str(score))
   ```

### 5-min Pomodoro Break
"Imitate your game's death sound." Out loud. Yes.

### Block 2 — 25 min — Lab: Polish Pass
Each student adds:
- 2 sounds to their game.
- 1 difficulty mechanic (faster enemies, more enemies, smaller player, time pressure — choice).
- Comments at the top of the file describing what the game does and how to play.

### 2-min Diffuse Mode Reflection
*"Your game now has SOUND. What's the most fun difference it makes?"*

### Homework Preview
Assignment W6 → final polish before Capstone Showcase. Save your game proudly.

---

## WEEK 6 QUIZ — Track A (10 questions)

> **Spaced repetition:** Q9 reviews W4 (lists/classes). Q10 reviews W4 (keyboard input).

**Easy (5)**

1. To play a sound in Pygame:
   - A) `pygame.play("ding.wav")` · B) `pygame.mixer.Sound("ding.wav").play()` ✅ · C) `print("ding")` · D) `pygame.audio.play(...)`

2. A *state variable* in our game holds:
   - A) The score · B) Which screen we're on right now ("title", "playing", "game_over") ✅ · C) The player's color · D) The window size

3. To loop background music forever, the argument is:
   - A) 0 · B) -1 ✅ · C) 1 · D) `loop=True`

4. Reasons to add comments to code:
   - A) Make it run faster · B) Help future you (or a teammate) understand it ✅ · C) Hide the code · D) None

5. To start the game from the title screen we listen for:
   - A) Mouse only · B) `pygame.K_SPACE` keypress (or any chosen key) ✅ · C) Game time > 5 sec · D) Random chance

**Medium (3)**

6. To restart the game after Game Over, we have to:
   - A) Reload Replit · B) Reset score, lives, and the player's position, then change state back to "playing" ✅ · C) Just change state · D) Just reset score

7. Adding `pygame.mixer.init()` is necessary because:
   - A) Pygame doesn't auto-init the audio system; you must turn it on ✅ · B) It loads images · C) It opens the screen · D) It's optional

8. A clean way to make enemies harder over time:
   - A) Multiply their `vx` and `vy` by 1.1 every level-up ✅ · B) Reduce screen size · C) Disable the player · D) Print "harder"

**Hard (2)**

9. *(Week 4 review)* If `coins = [Coin() for _ in range(5)]`, how do you draw them all?
   - A) `coins.draw(screen)` · B) `for c in coins: c.draw(screen)` ✅ · C) `Coin.draw_all()` · D) `pygame.draw_list(coins)`

10. *(Week 4 review)* `pygame.key.get_pressed()` returns:
    - A) The last key pressed · B) A list-like object you can index by `K_LEFT`, `K_UP`, etc. that's True if held ✅ · C) The number of keys · D) None

### Answer Key
1.B  2.B  3.B  4.B  5.B  6.B  7.A  8.A  9.B  10.B

---

## WEEK 6 ASSIGNMENT — Track A

**Title:** *"My Game, Polished"*
**Due:** Mon Jul 27, 11:59 PM PST

### Instructions
Take your Week 5 game and add **all of the following**:
1. A title screen with the game's name and "Press SPACE to start."
2. A game-over screen with score + "Press R to restart."
3. At least 1 sound effect on a meaningful event (pickup, hit, win).
4. At least 1 difficulty mechanic (e.g., enemies speed up over time).
5. Comments at the top of the file: game name, your name, how to play.
6. The code is split into at least 2 functions (e.g., `draw_title(screen)`, `reset_game()`).

### Grading Criteria — $1.50 when:
- [ ] Title screen and game-over screen both work (0.40)
- [ ] At least one sound plays on the right event (0.30)
- [ ] One difficulty mechanic is visible in play (0.30)
- [ ] Header comment explains the game (0.20)
- [ ] Code is at least somewhat organized (uses ≥2 functions) (0.30)

### Stretch
Add a high-score file. Add a "credits" screen. Add a "pause" key (P).

---

## Cumulative Mind Map (Week 6)

- All previous branches, **plus:**
- **🆕 🎬 Game States** → title · playing · game_over · restart logic
- **🆕 🔊 Sound** → `mixer.init` → `Sound(...)` → `.play()`, music loop
- **🆕 🎚️ Difficulty** → level variable, speed scaling
- **🆕 📝 Code Quality** → comments, function organization

Caption: *"Next week: SHOWCASE. You demo. We celebrate. Certificate."*
