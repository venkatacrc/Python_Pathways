# ARTIFACT 5 — Office Hours Agendas: Track A (5th Graders)

**Format:** 60 minutes, weekly. Held synchronously on Zoom. Recorded.
**Suggested time slot for Track A:** Saturday 10:30–11:30 AM PST (parent-friendly weekend, before lunch).
**Tone:** patient, playful, celebratory. Lots of encouragement; "let's try it together."

Each week follows the same structure:
- **0–10 min** — Open Q&A on this week's assignment.
- **10–30 min** — Top 3 anticipated confusion points (predicted from the curriculum).
- **30–50 min** — "Go further" optional demo for early finishers.
- **50–60 min** — Preview next week + a one-minute motivational moment.

---

## Week 1 Office Hours — Sat Jun 20, 2026

**0–10 — Open Q&A (Assignment: "Meet My Mascot")**
- "My turtle window won't open." | "How do I share my Replit link?" | "What's `f"..."` again?"

**10–30 — Top 3 Confusion Points**
1. **`input()` returns a string, even if you type a number.**
   - Demo: `age = input("Age? ")` then `age + 1` → error. Fix: `age = int(input(...))`.
2. **Indentation matters in Python.**
   - Show common error: `IndentationError`. Fix together: 4 spaces, consistent.
3. **Turtle window closes immediately.**
   - Fix: end every turtle program with `turtle.done()`.

**30–50 — "Go Further" Demo**
*"Make your turtle draw a rainbow!"* — show the simple `colors` list cycling.
```python
colors = ["red","orange","yellow","green","blue","purple"]
for c in colors:
    t.color(c); t.forward(60); t.right(60)
```

**50–60 — Preview Week 2 + Motivational Minute**
*"Next week: your computer LEARNS TO DECIDE. We'll make a Magic 8 Ball, and you'll write your first GAME on Thursday — Guess the Number!"* End on: *"Tonight, show your mascot to a parent. Make them say its name."*

---

## Week 2 Office Hours — Sat Jun 27, 2026

**0–10 — Open Q&A (Assignment: "Pet-Care Decision Helper")**
- "My loop won't stop." | "`elif` vs `else`?" | "Why does `==` need two equals signs?"

**10–30 — Top 3 Confusion Points**
1. **Infinite `while` loops:** `while True:` with no `break` or no condition update.
   - Fix together: stop with Ctrl+C in Replit; add the right exit condition.
2. **`=` vs `==`.** *= is "make this equal to," == is "ask if these are equal."*
3. **`if x = 5` vs `if x == 5`.** Type-along the bug, then fix it.

**30–50 — "Go Further"**
- Build a Magic Calculator: keep asking the user for two numbers + an operator, do it, until they type `quit`.

**50–60 — Preview Week 3 + Motivational Minute**
*"Next week: your GAME WINDOW OPENS. PYGAME. Real graphics. Real movement. Bring your imagination."* End on: *"You can already make the computer THINK. Just wait until you make it MOVE."*

---

## Week 3 Office Hours — Sat Jul 5, 2026 *(post July 4 weekend — likely smaller turnout; Async students prioritized)*

**0–10 — Open Q&A (Assignment: "My Animated Window")**
- "My Pygame window opened then closed." | "Why is my circle invisible?" | "Holiday catch-up — where am I?"

**10–30 — Top 3 Confusion Points**
1. **Forgot `pygame.display.flip()` (or `pygame.init()`).** Live demo: nothing draws → add the line → it draws.
2. **Coordinates are upside-down.** `(0, 0)` is top-left, y increases downward. Visually demo on whiteboard.
3. **Frame rate dependency.** Without `clock.tick(60)`, the bouncing ball looks weirdly fast or slow. Fix together.

**30–50 — "Go Further"**
- Make a *follower*: a small circle that always moves toward the mouse position (`pygame.mouse.get_pos()`).

**50–60 — Preview Week 4 + Motivational**
*"Next week: ARROW KEYS. Your character will MOVE when YOU press a key."* End on: *"You opened a real game window this week. There are professional programmers who haven't done that. You did, in 6th grade."*

---

## Week 4 Office Hours — Sat Jul 11, 2026

**0–10 — Open Q&A (Assignment: "Hero on the Move")**
- "Why does my Player class need `self`?" | "How do lists work again?" | "My player teleports off the screen."

**10–30 — Top 3 Confusion Points**
1. **Forgetting `self.` inside class methods.** Live walkthrough: `def move(self, keys): self.x -= 5` not `x -= 5`.
2. **Player moves too fast.** Tune speed in pixels-per-frame; show the `clock.tick(60)` connection.
3. **Forgetting to redraw on each frame.** Show: if you draw the player but don't `screen.fill(...)` first, you get smear-tracks (sometimes that's actually a cool feature — show how to keep it on purpose).

**30–50 — "Go Further"**
- Add a 2nd character that moves with `WASD` keys — first multiplayer game!

**50–60 — Preview Week 5 + Motivational**
*"Next week: COLLISIONS. Your player can pick up coins, lose lives, and win games."* End on: *"You made a character obey you tonight. That's basically what magicians do."*

---

## Week 5 Office Hours — Sat Jul 18, 2026

**0–10 — Open Q&A (Assignment: "Win-or-Lose Mini Game")**
- "My collision doesn't trigger." | "Score won't update." | "Game keeps crashing on game-over."

**10–30 — Top 3 Confusion Points**
1. **Stale `Rect`** — defining `player_rect` once outside the loop and never updating its position.
   - Fix: rebuild the Rect every frame from the current x,y.
2. **Score reset every frame.** Initializing `score = 0` *inside* the main loop. Fix: move it outside.
3. **Game-over loop trap.** Code that ends the game leaves you in a weird state. Show the clean `running = False` pattern.

**30–50 — "Go Further"**
- Add a *power-up*: a special coin that, when collected, makes the player invincible for 5 seconds (use `pygame.time.get_ticks()`).

**50–60 — Preview Week 6 + Motivational**
*"Next week: POLISH. Title screen. Sounds. Difficulty. Your game will FEEL like a real game."* End on: *"You made a game with a winner and loser tonight. That's a video game."*

---

## Week 6 Office Hours — Sat Jul 25, 2026

**0–10 — Open Q&A (Assignment: "My Game, Polished")**
- "Sound won't play in Replit." | "How do I make a Restart key work?" | "Title screen freezes."

**10–30 — Top 3 Confusion Points**
1. **`pygame.mixer` not initialized.** Fix: `pygame.mixer.init()` after `pygame.init()`.
2. **State machine bugs:** restart doesn't actually reset the score / lives / position. Walk through a clean reset function.
3. **Audio file paths.** Replit needs the file uploaded; show how to use the file pane.

**30–50 — "Go Further"**
- Build a *high-score file* using `open("highscore.txt")`. Persist across game runs.

**50–60 — Preview Week 7 + Motivational**
*"Next week: SHOWCASE. You demo to the class. You explain what you built and what was hard. This is the BIG moment. Bring confidence."* End on: *"Tonight your game is officially polished. Take a screenshot. Save it forever."*

---

## Week 7 Office Hours — Sat Aug 1, 2026 — *Showcase Reflection + Capstone Q&A*

**0–10 — Open Q&A**
*"Anyone want help getting their final game to run on a parent's laptop? Anyone want to keep coding after this?"*

**10–30 — Top 3 Confusion Points**
1. **Was my showcase score the same as my wallet payout?** Walk through how the rubric translates to dollars.
2. **What do I do next? — recommendations:** keep building on Replit, try Scratch's harder features, look at codecombat.com, or move into web with HTML/JS.
3. **Can I share my game with friends?** Yes — Replit's "Share" link works publicly. Demo it.

**30–50 — "Go Further"**
- Demo of upgrading the game with **levels**: each level loads enemies/coins from a list, harder each time.

**50–60 — Wrap & Motivational**
- Read the names of every student who completed the course aloud.
- Confirm the certificate URL & wallet payout method (Venmo/Zelle/check, parent's preference).
- *"Aug 3 = Certificate Day. Aug 4 = the rest of your life as a coder. You are now a Python builder. You can put that on a school project, on a website, on anything you make. Go make something."*
