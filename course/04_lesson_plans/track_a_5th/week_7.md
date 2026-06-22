# Track A — Week 7: "SHOWCASE — Your Complete Game"

**Dates:** Tue Jul 28 + Thu Jul 30, 2026 · 6:30 PM PST · Replit + Pygame
**Big Picture:** *Week 7 of 7 — final week. Tuesday is dress-rehearsal + last polish. Thursday is THE SHOWCASE — you demo your finished game to the class. Then certificates and the Progress Wallet payout.*

---

## SESSION 1 — Tuesday, July 28, 2026 — *Dress Rehearsal & Final Polish*

### Learning Objectives
By the end of this session, students can:
1. Demo their game cleanly from start to game-over.
2. Explain *what they built* and *what was hardest* in 2 sentences.
3. Help a peer fix one bug in their game.

### Active Recall (3 min)
"What's a state variable for? How do you play a sound? How do you reset the game? Where do score and lives live?"

### Big Picture (1 min)
Step 7 of 7 — almost lit. *"You built a game. From zero. In 6 weeks. Tonight we polish. Thursday, you demo it."*

### Block 1 — 25 min — Demo Practice
- Each student gets 4 minutes:
  - 60 sec — share screen, run game from title screen
  - 90 sec — walkthrough (title → play → die → restart → win)
  - 90 sec — answer instructor's question: *"What's the part you're proudest of?"*
- Instructor + peers give 1 specific compliment + 1 specific suggestion.

### 5-min Pomodoro Break
"Group photo with your game" — everyone shows their title screen on camera. Screenshot. (Posted in Forum after class.)

### Block 2 — 25 min — Pair Bug Hunt
Random pairs swap Replit links. Each student tries to crash their partner's game and reports back any bug they find. Then they help fix one bug together. (This builds *reading-other-people's-code* muscle.)

### 2-min Diffuse Mode Reflection
*"Your game is almost done. What does it feel like to know YOU made this?"*

### Homework Preview
Thursday: bring your A-game. 6-min slot per student. Final code locked Wednesday 11:59 PM.

---

## SESSION 2 — Thursday, July 30, 2026 — *🏆 THE SHOWCASE 🏆*

### Cold Open — 2 min
Instructor: *"Six weeks ago none of you had ever written a line of Python. Tonight you all walk in with a game. Let's go."* Round of applause from each rectangle on screen.

### Big Picture (1 min)
Step 7 of 7 LIT. The whole staircase glows. Caption: *"You're at the top."*

### Showcase Block — ~50 min total (5 students × ~9 min each = 45 min, plus buffer)
Each student gets 9 minutes:
- 4 min — live demo of their game
- 2 min — *"What I built. What was hardest. What I'm most proud of."*
- 3 min — Q&A from peers + instructor

Instructor uses Capstone Rubric (Artifact 6) live, scoring each section as the student demos.

### Closing Ritual (5 min)
- Each student writes one sentence in the course-site journal (discussion thread): *"On June 15, I couldn't __. Today, I can __."*
- Instructor reveals: *"Monday Aug 3 = Certificate Day. Your wallet payout is being calculated tonight. Check your Progress Wallet page tomorrow morning."*
- Group screenshot. End on: *"You are now Python builders. Period."*

### 2-min Diffuse Mode Reflection
*"What's the next thing you want to make?"* (No homework. Just the question.)

---

## WEEK 7 QUIZ — Track A (10 questions)
*Optional — graded on completion + earning $1.00 if attempted seriously. This is a fun closing review, not a gatekeeper.*

> **Spaced repetition:** Q9 reviews W5 (collisions). Q10 reviews W5 (text rendering).

**Easy (5)**

1. The function `pygame.display.flip()` does:
   - A) Flips the window upside-down · B) Updates the screen with everything you drew this frame · C) Closes the game · D) Saves the game

2. To restart your game after game-over, you reset the state variable to:
   - A) `"reset"` · B) `"playing"` (and reset score/lives/positions) · C) `"game_over"` · D) Stop the program

3. The capstone showcase is on:
   - A) Aug 1 · B) Jul 30 · C) Aug 3 · D) Jul 28

4. Comments in Python start with:
   - A) `//` · B) `#` · C) `--` · D) `/*`

5. The certificate is delivered:
   - A) Through the mail · B) On Aug 3 via a course-site URL + email · C) Never · D) On Day 1

**Medium (3)**

6. To draw the title screen and skip the gameplay code, you wrap gameplay in:
   - A) `if state == "playing":` · B) `if score > 0:` · C) `if running:` · D) `while True:`

7. To play a sound only ONCE per coin pickup, where do you call `.play()`?
   - A) Inside the title screen branch · B) Inside the collision-detect block, right after score += 1 · C) Every frame · D) In the import section

8. To time the game (e.g., 30 seconds to win), you use:
   - A) `pygame.time.get_ticks()` to read milliseconds since `pygame.init()`   - B) `time.now()` · C) `pygame.timer()` · D) `pygame.frame.count`

**Hard (2)**

9. *(Week 5 review)* `pygame.Rect(100, 50, 30, 40)` — what does each number mean?
   - A) (x, y, width, height) · B) (color components) · C) (window size, x, y) · D) (start, end, step, count)

10. *(Week 5 review)* What's wrong with this snippet?
    ```python
    text = font.render("Hi", True, (255, 255, 255))
    screen.blit(text)   # missing position!
    ```
    - A) Color is wrong · B) `screen.blit` needs a position argument like `(10, 10)` · C) `True` should be False · D) Nothing wrong

### Answer Key
1.B  2.B  3.B  4.B  5.B  6.A  7.B  8.A  9.A  10.B

---

## WEEK 7 ASSIGNMENT (Capstone-Adjacent, *only* needed if a student didn't complete Showcase)

**Title:** *"Submit your Game for Showcase"*
**Due:** Wed Jul 29, 11:59 PM PST (locked before Thursday's showcase)

### Instructions
Submit:
1. A working Replit link to your final game.
2. A 2-minute (max) screen recording of your gameplay (Replit's screen recording or any tool).
3. A short text post in the Track A Forum:
   - Game name
   - Genre (Snake/Space Invaders/Flappy/Tetris/Other)
   - One thing you're proud of
   - One thing that was hardest

### Grading
This is the **Capstone**, graded against the rubric in Artifact 6. Up to **$12.50** earned.

### No stretch this week — go play outside.

---

## Final Cumulative Mind Map (Week 7)

The whole tree:

```
                          PYTHON
        /        |         |         |        |       \
      Talk     Store     Draw      Tools   Decide   Repeat
       |        |         |         |        |        |
     print     vars     turtle    Replit    if/elif   for
     input    nums       |        Pygame    else      while
     f-str    str       Pygame   console    ==,!=     loops
                lists     |
                       window
                       shapes        Functions ── Classes
                       colors           |             |
                                    parameters    self/__init__
                                     return        methods
                                                       |
                                                  Player/Coin/Enemy
                                                       |
                                              Keyboard ── Collisions ── Game State
                                                  |          |               |
                                              get_pressed  Rect.col      score, lives
                                              K_LEFT...    iderect       win/lose
                                                                              |
                                                                  Game States ── Sound ── Difficulty
                                                                       |          |          |
                                                                  title/play   mixer    speed scaling
                                                                  /game_over   load     levels
                                                                              .play()
                                                                              music loop
```

Caption: *"On June 15, you saw the word `print()` for the first time. Today, you built a complete game using all of the above. That's mastery. Take a screenshot of this map. Save it forever."*
