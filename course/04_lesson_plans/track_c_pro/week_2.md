# Track C — Week 2: "Neural Networks from Scratch + train1.py"

**Dates:** Tue Jun 23 + Thu Jun 25, 2026 · 6:30 PM PST · Python 3 (standard library only — `math`, `random`)
**Big Picture:** *Week 2 of 7 — manually-computed gradients, hand-rolled SGD, MLP language model. The "why does gradient descent work" intuition before the formalism. This is the floor of every modern net.*

---

## SESSION 1 — Tuesday, June 23, 2026

### Learning Objectives
1. Express the cross-entropy loss for a tiny neural net analytically and code it.
2. Hand-derive gradients for a 1-hidden-layer MLP.
3. Implement SGD updates with explicit `param -= lr * grad` lines.

### Active Recall (3 min)
"State the bigram model in one sentence. Why does perplexity collapse with n=3 vs n=2 vs n=4? What's add-1 smoothing for?"

### Big Picture (1 min)
Step 2 of 7. *"Tonight: you replace the count-table with a *learned* table — it can interpolate between bigrams it never saw."*

### Block 1 — 25 min — MLP math, by hand
1. **Setup:** input one-hot of size V (V≈65), hidden size H=64, output size V. Two weight matrices `W1` (V×H), `W2` (H×V), biases optional.
2. **Forward:**
   - `h = tanh(x @ W1 + b1)`
   - `logits = h @ W2 + b2`
   - `loss = -log(softmax(logits)[y])`
3. **Manual backward (the part most engineers have never done):** derive `dL/dlogits = softmax(logits) - onehot(y)`, then `dL/dW2 = h^T · dL/dlogits`, etc. Do this on a whiteboard / iPad live.

### 5-min Pomodoro Break
Get up. Drink water. Whatever.

### Block 2 — 25 min — `train1.py` (numpy-free or numpy-light)
Karpathy's microGPT uses pure-Python lists for `train1`. Live build:
```python
# train1.py — MLP language model, manual gradients, pure Python
import math, random, urllib.request

URL = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
text = urllib.request.urlopen(URL).read().decode("utf-8")
vocab = sorted(set(text))
stoi = {c: i for i, c in enumerate(vocab)}
itos = {i: c for c, i in stoi.items()}
V = len(vocab)
H = 16  # tiny for live build

def matmul(A, B):
    n, m = len(A), len(B[0]); k = len(B)
    return [[sum(A[i][p]*B[p][j] for p in range(k)) for j in range(m)] for i in range(n)]

def init(rows, cols, scale=0.01):
    return [[random.uniform(-1, 1)*scale for _ in range(cols)] for _ in range(rows)]

W1 = init(V, H); W2 = init(H, V)

def softmax(z):
    m = max(z); ez = [math.exp(x-m) for x in z]; s = sum(ez); return [e/s for e in ez]

def forward(idx):
    x = [0.0]*V; x[idx] = 1.0
    h = [math.tanh(sum(x[i]*W1[i][j] for i in range(V))) for j in range(H)]
    logits = [sum(h[j]*W2[j][k] for j in range(H)) for k in range(V)]
    return h, logits

def loss_and_grads(idx, target):
    h, logits = forward(idx)
    p = softmax(logits)
    loss = -math.log(p[target] + 1e-12)
    dlogits = p[:]; dlogits[target] -= 1.0
    dW2 = [[h[j]*dlogits[k] for k in range(V)] for j in range(H)]
    dh  = [sum(dlogits[k]*W2[j][k] for k in range(V)) for j in range(H)]
    dh_pre = [(1 - h[j]*h[j]) * dh[j] for j in range(H)]
    dW1 = [[(1.0 if i == idx else 0.0)*dh_pre[j] for j in range(H)] for i in range(V)]
    return loss, dW1, dW2

lr = 0.5
for step in range(2000):
    i = random.randrange(len(text)-1)
    src, tgt = stoi[text[i]], stoi[text[i+1]]
    loss, dW1, dW2 = loss_and_grads(src, tgt)
    for r in range(V):
        for c in range(H): W1[r][c] -= lr * dW1[r][c]
    for r in range(H):
        for c in range(V): W2[r][c] -= lr * dW2[r][c]
    if step % 200 == 0: print(f"step {step}  loss {loss:.4f}")
```

### Block 2 (continued) — Lab: Hand-Trace
Each pro picks ONE step and prints every intermediate (`x`, `h`, `logits`, `p`, `loss`, `dlogits`, `dW1`, `dW2`) for that step. Posts a screenshot in Forum. **The point:** to *feel* the chain rule.

### 2-min Diffuse Mode Reflection
*"What's the intuition for why subtracting `onehot(y)` from `softmax(logits)` is the gradient of cross-entropy?"*

### Homework Preview
Thursday: vectorize the MLP with numpy, train longer, sample text, compare perplexity to bigram.

---

## SESSION 2 — Thursday, June 25, 2026

### Stuck Check (3 min)
"Whose gradients exploded? Whose loss went UP? Whose pure-Python is too slow to train past 5k steps?"

### Big Picture (1 min)
Step 2 still. *"Today: numpy. Same math, 100× faster. Then sample."*

### Block 1 — 25 min — Vectorize with numpy
Refactor the inner loop to numpy arrays — single matmul forward + closed-form backward:
```python
import numpy as np
W1 = np.random.randn(V, H) * 0.01
W2 = np.random.randn(H, V) * 0.01
def step(src, tgt, lr=0.5):
    x = np.zeros(V); x[src] = 1.0
    h = np.tanh(x @ W1)
    logits = h @ W2
    p = np.exp(logits - logits.max()); p /= p.sum()
    loss = -np.log(p[tgt] + 1e-12)
    dlogits = p.copy(); dlogits[tgt] -= 1
    dW2 = np.outer(h, dlogits)
    dh  = W2 @ dlogits
    dW1 = np.outer(x, (1 - h*h) * dh)
    return loss, dW1, dW2
```
Train 50,000 steps in seconds. Sample text. Show that the MLP captures things bigram cannot (e.g., whitespace patterns, simple word fragments).

### 5-min Pomodoro Break
Discretionary.

### Block 2 — 25 min — Lab: Compare baselines
Each pro:
- Trains the MLP for 30k+ steps.
- Computes test-set perplexity.
- Generates a 500-char sample.
- Posts a one-line comparison: bigram ppl vs MLP ppl, with one observation.

### 2-min Diffuse Mode Reflection
*"You wrote backprop by hand. What changes about the way you'll think about PyTorch's `loss.backward()` from now on?"*

### Homework Preview
**Assignment W2 below.** Next week: an autograd engine (Karpathy's `Value` class).

---

## WEEK 2 QUIZ — Track C (10 questions, 15 min)

> **Spaced repetition:** none yet from earlier weeks (we count W1 → W2 as "current"); Q9–Q10 are extra current-week.

**Easy (5)**

1. The gradient of cross-entropy w.r.t. logits is:
   - A) softmax(logits) minus onehot(y)
     · B) onehot(y) - softmax(logits)
     · C) sigmoid(logits) - y
     · D) the logits themselves
   *(canonical answer: A — `softmax(logits) - onehot(y)`)*

2. `np.outer(a, b)` produces:
   - A) Element-wise product · B) Outer product, shape (len a, len b) · C) Inner product · D) Cross product

3. `tanh` derivative is:
   - A) `1 - tanh(x)` · B) `1 - tanh(x)**2` · C) `tanh(x)*(1-tanh(x))` · D) `0`

4. SGD with learning rate `lr` updates parameters as:
   - A) `p += lr * grad` · B) `p -= lr * grad` · C) `p *= grad` · D) `p = grad`

5. Subtracting the max from logits before `exp` is to:
   - A) Speed up training · B) Improve numerical stability · C) Make output sum to 1 · D) None

**Medium (3)**

6. The shape of `dW2` (gradient of W2) is:
   - A) (V, H) · B) (H, V) · C) Scalar · D) (V,)

7. Why is pure-Python training 100× slower than numpy?
   - A) numpy is GPU only · B) numpy uses contiguous arrays + BLAS for matmul · C) Python is single-threaded · D) Disk I/O

8. The sum of all softmax probabilities equals:
   - A) 0 · B) 1 · C) V · D) The temperature

**Hard (2)**

9. Numerical check of gradient correctness uses:
   - A) Random weights · B) Finite differences `(L(p+ε) - L(p-ε))/(2ε)` ≈ analytical grad · C) `assert grad > 0` · D) Plotting

10. Why is the dataset re-tokenized as character indices (not raw bytes)?
    - A) Because Python forbids bytes · B) To match the V-dimensional one-hot model and remove byte-encoding artifacts · C) For speed · D) For Unicode

### Answer Key
1.A  2.B  3.B  4.B  5.B  6.B  7.B  8.B  9.B  10.B

---

## WEEK 2 ASSIGNMENT — Track C

**Title:** *Implement `train1.py` (numpy MLP) + grad-check*
**Due:** Mon Jun 29, 11:59 PM PST · GitHub link

### Instructions
1. Implement `train1.py` end-to-end:
   - Pure-numpy 1-hidden-layer MLP, manual forward + backward.
   - Cross-entropy loss with logit-max stabilization.
   - SGD training loop, 50k+ steps.
2. Add a **gradient check function** that compares analytical to finite-difference gradients on a randomly-chosen weight in `W1` and `W2` (max relative error < 1e-5).
3. Compute test-set perplexity (held-out 10%).
4. Generate a 500-character sample.
5. Update your README with: bigram ppl, MLP ppl, both samples, and a comparison paragraph.

### Grading Criteria — $1.50 when:
- [ ] `train1.py` runs and converges (0.30)
- [ ] Manual gradients pass numerical check (0.40)
- [ ] Perplexity reported on held-out (0.30)
- [ ] Sample produced + analyzed in README (0.30)
- [ ] Code clean, single-file, no PyTorch/TensorFlow (0.20)

### Stretch
Try `H=128` and `H=4`. Compare ppl. Plot loss curves with `matplotlib`. Note where the bias-variance tradeoff kicks in.

---

## Cumulative Mind Map (Week 2)

```
microGPT staircase:
  W1 [bigram count table]
  W2 [MLP, manual SGD + backprop] ← YOU ARE HERE
  W3 [scalar autograd: micrograd Value class]
  W4 [embeddings + 1-head attention]
  W5 [multi-head + LN]
  W6 [Adam → microGPT complete]
  W7 [showcase]

New skills:
  ML: cross-entropy, softmax stability, manual chain rule, SGD update rule, gradient check
  Python: numpy basics (outer, exp, log, broadcasting), seed control
  Insight: every modern training loop is this pattern, just bigger.
```

Caption: *"Next week: stop computing gradients by hand. Build the engine that does it for you."*
