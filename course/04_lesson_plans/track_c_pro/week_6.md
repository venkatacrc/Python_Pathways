# Track C — Week 6: "Adam Optimizer + train5.py — Complete microGPT"

**Dates:** Tue Jul 21 + Thu Jul 23, 2026 · 6:30 PM PST · Python 3
**Big Picture:** *Week 6 of 7 — replace SGD with Adam → `train5.py` is **microGPT**, complete in ~200 lines of standard-library Python. Run on Shakespeare → it generates believable text. Celebrate.*

---

## SESSION 1 — Tuesday, July 21, 2026

### Learning Objectives
1. Derive Adam from intuition: per-parameter learning rates with momentum + RMS scaling.
2. Implement Adam (with bias correction) in numpy.
3. Verify it converges faster than SGD on the same architecture.

### Active Recall (3 min)
"Why does SGD oscillate near a minimum? What does momentum buy you? Why does RMSProp normalize by gradient magnitude?"

### Big Picture (1 min)
Step 6 of 7. *"This is the last piece. After tonight: microGPT generates text."*

### Block 1 — 25 min — Adam, derived & implemented
The intuition:
- **Momentum** (`m`): exponential moving average of gradients → smooths SGD updates.
- **RMSProp** (`v`): exponential moving average of *squared* gradients → adaptive per-parameter step size.
- **Adam** = combine both, with bias correction since `m` and `v` start at 0.

```python
class Adam:
    def __init__(self, params, lr=3e-4, betas=(0.9, 0.999), eps=1e-8):
        self.params = params      # list of numpy arrays
        self.lr = lr
        self.b1, self.b2 = betas
        self.eps = eps
        self.t = 0
        self.m = [np.zeros_like(p) for p in params]
        self.v = [np.zeros_like(p) for p in params]

    def step(self, grads):
        self.t += 1
        for i, (p, g) in enumerate(zip(self.params, grads)):
            self.m[i] = self.b1 * self.m[i] + (1 - self.b1) * g
            self.v[i] = self.b2 * self.v[i] + (1 - self.b2) * g * g
            m_hat = self.m[i] / (1 - self.b1 ** self.t)
            v_hat = self.v[i] / (1 - self.b2 ** self.t)
            p -= self.lr * m_hat / (np.sqrt(v_hat) + self.eps)
```

### 5-min Pomodoro Break
Discretionary.

### Block 2 — 25 min — Drop into `train4.py` → `train5.py`
1. Wire Adam into the training loop.
2. Train side-by-side: Adam vs SGD with `lr=3e-4`. Plot losses.
3. See Adam crush SGD on the same architecture in fewer steps.

### 2-min Diffuse Mode Reflection
*"Bias correction matters most when t is small. Why?"*

### Homework Preview
Thursday: real microGPT run on Shakespeare → generate.

---

## SESSION 2 — Thursday, July 23, 2026

### Stuck Check (3 min)
"Whose Adam diverged at lr=1e-3? Whose loss is NaN? Whose generation looks great?"

### Big Picture (1 min)
Step 6 still. *"You built microGPT. Tonight we run it long enough to make it speak."*

### Block 1 — 25 min — Train + sample
A 2-block, 4-head, D=128, T=128 model. Train ~30k iterations (maybe ~10 min on a laptop CPU; faster on Colab GPU but Karpathy's microGPT philosophy is CPU/standard-lib-friendly). Watch the loss curve flatten ~2.0 (typical for char-LM Tiny Shakespeare).

Sample with **temperature** and **top-k**:
```python
def sample(seed, n=500, T=128, temperature=1.0, top_k=None):
    idxs = [stoi[c] for c in seed[-T:]]
    out = list(seed)
    for _ in range(n):
        ctx = idxs[-T:]
        logits, _ = forward(ctx)
        logits = logits[-1] / temperature
        if top_k:
            kth = np.partition(logits, -top_k)[-top_k]
            logits = np.where(logits < kth, -1e9, logits)
        probs = np.exp(logits - logits.max()); probs /= probs.sum()
        nxt = np.random.choice(len(probs), p=probs)
        idxs.append(int(nxt)); out.append(itos[int(nxt)])
    return "".join(out)

print(sample("To be, or not to be", n=500, temperature=0.8, top_k=10))
```

### 5-min Pomodoro Break
Discretionary. **Optional** group celebration: Karpathy's classic "we built a GPT" moment.

### Block 2 — 25 min — Lab: Hyperparameter taste
Each pro tries 3 (T, D, H, n_blocks) configurations + temperatures, ranks samples by aesthetic quality, and posts the best one in the Forum with the hyperparameters used.

### 2-min Diffuse Mode Reflection
*"You built a GPT in 200 lines. What does that tell you about what GPT-4 is — and isn't?"*

### Homework Preview
**Assignment W6 below.** Pick your custom dataset for Week 7 showcase.

---

## WEEK 6 QUIZ — Track C (10 questions)

> **Spaced repetition:** Q9 + Q10 review Week 4 (attention).

**Easy (5)**

1. Adam combines:
   - A) Just momentum · B) Momentum + RMSProp · C) SGD only · D) Adagrad only

2. Bias correction in Adam matters most when:
   - A) `t` is large · B) `t` is small (early training, when m, v are biased toward 0) · C) Never · D) Always equally

3. A typical Adam learning rate for transformers is around:
   - A) `1e-1` · B) `3e-4` · C) `1` · D) `1e-9`

4. `top_k` sampling:
   - A) Always picks the argmax · B) Restricts sampling to the top-k probability candidates · C) Random · D) Beam search

5. `temperature < 1.0` makes sampling:
   - A) More random · B) More deterministic / sharper · C) Identical · D) Slower

**Medium (3)**

6. Why divide by `sqrt(v_hat)` in Adam?
   - A) Numerical hack · B) Adapts the step size per parameter to its recent gradient magnitude · C) Decorative · D) For variance

7. SGD with the same lr typically:
   - A) Converges faster than Adam · B) Slower than Adam on transformers, because of nonuniform gradient scales · C) Equal · D) Errors

8. The full microGPT (train5) can run:
   - A) Only on a GPU cluster · B) On a laptop CPU in pure Python with standard library only · C) Only on Colab Pro · D) Requires PyTorch

**Hard (2)**

9. *(Week 4 review)* The shape of the attention matrix in 1-head, single-batch is:
   - A) `(D, D)` · B) `(T, T)` · C) `(V, V)` · D) `(D_h, D_h)`

10. *(Week 4 review)* Why scale by `sqrt(D_h)` before softmax?
    - A) Decorative · B) Keep variance of dot products O(1) so softmax doesn't saturate · C) Speed · D) Required by Python

### Answer Key
1.B  2.B  3.B  4.B  5.B  6.B  7.B  8.B  9.B  10.B

---

## WEEK 6 ASSIGNMENT — Track C

**Title:** *Complete `train5.py` — microGPT with Adam + sampling*
**Due:** Mon Jul 27, 11:59 PM PST · GitHub link

### Instructions
1. Implement `train5.py`:
   - Inherits architecture from `train4.py` (multi-head attention, LayerNorm, residual MLP block, ≥2 blocks).
   - Adds an Adam optimizer (your own implementation, ≤30 lines).
   - Includes `sample(seed, n, temperature, top_k)`.
2. Train on Tiny Shakespeare for ≥20,000 iterations.
3. Save the trained weights (any format — pickle, JSON arrays).
4. Sample 5 outputs at temperatures `[0.5, 0.8, 1.0, 1.2]` and top-k `10`. Save samples to `samples.md`.
5. Update README:
   - The full microGPT staircase: ppl from bigram → microGPT.
   - Best sample, with hyperparams used.
   - Choose the dataset you'll use for the Week 7 capstone (post in Forum too).

### Grading Criteria — $1.50 when:
- [ ] Adam implemented with bias correction (0.40)
- [ ] microGPT trains stably and produces coherent text (0.40)
- [ ] Sample function with temperature + top-k (0.20)
- [ ] Saved weights + samples.md present (0.20)
- [ ] README ppl chain documented (0.30)

### Stretch
Add **AdamW** (decoupled weight decay). Try a learning-rate warmup over the first 1000 steps. Note any quality differences.

---

## Cumulative Mind Map (Week 6)

```
microGPT staircase:
  W1 bigram · W2 MLP · W3 Value autograd · W4 1-head attention · W5 multi-head+LN
  W6 [Adam → microGPT complete] ← YOU ARE HERE
  W7 [showcase]

New skills:
  Optimizer: momentum, adaptive per-param scaling, bias correction, lr practice
  Sampling: temperature, top-k, greedy/argmax
  Engineering: weight checkpointing, sample saving
  Insight: you built a GPT. In 200 lines. Pure Python. No magic.
```

Caption: *"Next week: bring your own dataset and showcase what you built."*
