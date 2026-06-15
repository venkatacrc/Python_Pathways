# Track C — Week 1: "Python Foundations + train0.py — The Bigram Baseline"

**Dates:** Tue Jun 16 + Thu Jun 18, 2026 · 6:30 PM PST · Python 3 (local or Colab)
**Big Picture:** *Week 1 of 7 — fastest possible Python tour for experienced engineers, then `train0.py`: a bigram count-table that "speaks" Shakespeare. Zero libraries. Reading code is the sport.*
**Reference:** Karpathy, *microGPT* — `https://karpathy.github.io/2026/02/12/microgpt/`

---

## SESSION 1 — Tuesday, June 16, 2026

### Learning Objectives
By the end of this session, professionals can:
1. Run Python 3.x locally or in Colab and confidently navigate types, classes, file I/O, and the standard library — fast, no hand-holding.
2. Read Karpathy's `train0.py` line by line and explain what each block does.
3. Train a character-level bigram count table on the Tiny Shakespeare corpus and sample from it.

### Active Recall Opener
*Skipped — first session.* Instead: 3-min round — *"In one sentence: what's your hypothesis for the dataset you'd run microGPT on by Week 7?"*

### Big Picture (1 min)
The 7-step microGPT staircase: bigram → MLP → autograd → embeddings + attention → multi-head + LN → Adam → custom-data showcase. Today's the bottom step. Everything we do next is *measurably better than this baseline*.

### Block 1 — 25 min — Python crash + bigram theory
1. **Python crash (10 min):** `dataclasses`, type hints, `dict.get(default)`, list/dict comprehensions, `with open(...)`, `Counter`, `random.choices`. Live-coded in one cell.
2. **Bigram intuition (10 min):** for a vocabulary `V`, count `P(c_t | c_{t-1})` from the corpus → an `|V| × |V|` matrix. Sampling = walk the chain.
3. **The corpus (5 min):** Tiny Shakespeare (`https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt`, ~1.1 MB plaintext).

### Block 2 — 25 min — `train0.py` live build
```python
# train0.py — character-level bigram count table
import urllib.request, random
from collections import Counter, defaultdict

URL = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
text = urllib.request.urlopen(URL).read().decode("utf-8")

# Vocab
vocab = sorted(set(text))
stoi = {c: i for i, c in enumerate(vocab)}
itos = {i: c for c, i in stoi.items()}
V = len(vocab)
print(f"Corpus chars: {len(text):,} | Vocab: {V}")

# Counts: bigram[(prev, next)] = count
bigram = defaultdict(Counter)
for a, b in zip(text, text[1:]):
    bigram[a][b] += 1

# Sample
def sample(start: str, n: int = 200) -> str:
    out = [start]
    cur = start
    for _ in range(n):
        counts = bigram[cur]
        if not counts:
            cur = random.choice(vocab)
        else:
            chars, weights = zip(*counts.items())
            cur = random.choices(chars, weights=weights, k=1)[0]
        out.append(cur)
    return "".join(out)

print(sample("R", 300))
```
Run live, observe the gibberish — *"This sets your floor."*

### 5-min Pomodoro Break
Stand. Coffee or water. Glance out the window. (No fluffy break activity for this track — peer-to-peer, you know what to do.)

### Block 2 Continued — Lab
Each pro implements train0 themselves (no copy-paste), pushes to a personal `python-pathways-microgpt` GitHub repo as `train0.py`, and pastes their generation sample in the Track C Forum.

### 2-min Diffuse Mode Reflection
Course-site journal (Track C Discussion): *"What's one thing about the bigram baseline that's worse than you expected? Better than you expected?"*

### Homework Preview
Thursday: a 3-gram extension and a perplexity calculation, then we set the stage for `train1.py`.

---

## SESSION 2 — Thursday, June 18, 2026

### Stuck Check (3 min)
Instructor invites each pro to name their hardest moment since Tuesday — *"What broke?"*

### Big Picture (1 min)
Step 1 of 7. *"Tuesday: bigram. Today: extend it; measure it; understand why it can't go further."*

### Block 1 — 25 min — Trigrams + Perplexity
1. **n-gram generalization:** the same code with `text[:-2], text[1:-1], text[2:]`. Show that 3-gram is qualitatively better but explodes in memory at higher n.
2. **Perplexity (with care):**
   ```python
   import math
   def log_prob(seq):
       lp = 0.0
       for a, b in zip(seq, seq[1:]):
           total = sum(bigram[a].values())
           p = (bigram[a].get(b, 0) + 1) / (total + V)  # add-1 smoothing
           lp += math.log(p)
       return lp

   N = 1000
   lp = log_prob(text[:N])
   ppl = math.exp(-lp / N)
   print(f"Perplexity (bigram, add-1, first {N} chars): {ppl:.2f}")
   ```
   Discuss why character-level perplexity is in a familiar range (15-30 for bigrams on Shakespeare).

### 5-min Pomodoro Break
Whatever you want. We're adults.

### Block 2 — 25 min — Lab: Compare bigram vs trigram
Each pro extends `train0.py` to support `n=2,3` via a CLI flag. Compute perplexity for both. Post numbers in the Forum with one observation about diminishing returns.

### 2-min Diffuse Mode Reflection
*"Why does the bigram fail to imitate Shakespeare? What's structurally missing?"*

### Homework Preview
**Assignment W1 below.** And: skim Karpathy's micrograd intro before next Tuesday.

---

## WEEK 1 QUIZ — Track C (10 questions, 15 min, closed-notes)

> **Spaced repetition:** None yet (first week).

**Easy (5)**

1. Tiny Shakespeare's vocabulary size is approximately:
   - A) ~26 · B) ~65 ✅ (lowercase + uppercase + punctuation + whitespace) · C) ~256 · D) ~10000

2. `defaultdict(Counter)` gives you, for any new key:
   - A) An empty Counter that you can `+=` into ✅ · B) None · C) An error · D) Zero

3. `random.choices(items, weights=w, k=1)` returns:
   - A) A length-1 list with a sample drawn proportionally to `w` ✅ · B) An int · C) The same item every time · D) An error

4. `for a, b in zip(text, text[1:])` iterates:
   - A) Adjacent character pairs of `text` ✅ · B) Just text · C) Reversed pairs · D) Skips every other

5. The bigram model fails on Shakespeare primarily because:
   - A) Wrong tokenizer · B) It can only condition on the immediate previous character — no longer-range structure ✅ · C) Too much data · D) GPU not used

**Medium (3)**

6. Add-1 (Laplace) smoothing is needed to:
   - A) Speed up training · B) Prevent log(0) and assign nonzero probability to unseen pairs ✅ · C) Compress the data · D) Increase variance

7. Perplexity equals:
   - A) `mean of log probs` · B) `exp(-mean log prob)` ✅ · C) Cross-entropy times 2 · D) Vocab size

8. Memory cost of an `n`-gram count table is roughly:
   - A) O(N · V) · B) O(V^n) ✅ · C) O(1) · D) O(log N)

**Hard (2)**

9. Why use character-level rather than word-level for the baseline?
   - A) Smaller vocab + simpler tokenizer; demonstrates the math without BPE complexity ✅
   - B) It's faster · C) Words are illegal · D) It uses less RAM (N is the same)

10. The bigram with no smoothing assigns probability **0** to:
    - A) Pairs that never appeared in the corpus ✅
    - B) All pairs · C) The first character only · D) Stop tokens

### Answer Key
1.B  2.A  3.A  4.A  5.B  6.B  7.B  8.B  9.A  10.A

---

## WEEK 1 ASSIGNMENT — Track C

**Title:** *Implement & evaluate `train0.py` with n-gram extension*
**Due:** Mon Jun 22, 11:59 PM PST · GitHub repo link via the [Assignment Google Form](https://forms.gle/REPLACE_WITH_REAL_FORM)

### Instructions
1. Create a public GitHub repo `python-pathways-microgpt` (or a folder in your existing repo).
2. Implement `train0.py` end-to-end (no copy-paste from class — you re-write).
3. Add a CLI flag `--n {2,3}` to switch between bigram and trigram models.
4. Implement add-1 smoothing.
5. Compute perplexity on a held-out 10% slice of the corpus.
6. Generate a 500-character sample for both `n=2` and `n=3`.
7. Write a 1-page `README.md` reporting: vocab size, train/test perplexity for both n, and *"why does n=3 reduce perplexity but eventually plateau?"*

### Grading Criteria — $1.50 when:
- [ ] Repo public + has `train0.py`, `README.md` (0.30)
- [ ] CLI for `--n` works (0.30)
- [ ] Smoothing implemented + perplexity computed on held-out split (0.40)
- [ ] Both samples generated and pasted in README (0.30)
- [ ] Honest one-paragraph analysis (0.20)

### Stretch
Memory-profile your `n=4` and document where it breaks on your machine. (No money — just a real engineering finding.)

---

## Cumulative Mind Map (Week 1)

```
microGPT staircase:
  W1 [bigram count table]   ← YOU ARE HERE
  W2 [MLP, manual SGD + backprop]
  W3 [scalar autograd: micrograd Value class]
  W4 [token + position embeddings + 1-head attention]
  W5 [multi-head attention + LayerNorm + transformer block]
  W6 [Adam optimizer → microGPT complete]
  W7 [showcase on your dataset]

Skills picked up this week:
  Python: dataclass, type hints, comprehensions, with, Counter, random.choices
  ML: char-level tokenization, n-gram counting, add-1 smoothing, perplexity
  Insight: long-range context is what's missing.
```

Caption: *"Next week: gradients by hand. We earn every neuron."*
