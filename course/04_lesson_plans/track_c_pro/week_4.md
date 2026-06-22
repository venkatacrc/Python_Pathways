# Track C — Week 4: "Attention + train3.py — Embeddings & Single-Head Attention"

**Dates:** Tue Jul 7 + Thu Jul 9, 2026 · 6:30 PM PST · Python 3 (numpy or your `Value`)
**Big Picture:** *Week 4 of 7 — tonight, the magic that makes transformers work. Token + position embeddings, then the single-headed self-attention block, derived from first principles.*

---

## SESSION 1 — Tuesday, July 7, 2026

### Learning Objectives
1. Reason about token embeddings as a learnable lookup table.
2. Add position embeddings and explain why they're needed.
3. Compute scaled dot-product attention by hand for a tiny example.

### Active Recall (3 min)
"What's `Value.backward()` doing? What's `softmax(logits) - onehot(y)` give you? Why accumulate (`+=`) gradients?"

### Big Picture (1 min)
Step 4 of 7. *"The bigram saw 1 char back. The MLP saw 1 char back. Attention sees ALL the chars back, weighted."*

### Block 1 — 25 min — Embeddings + the Q/K/V intuition
1. **Token embedding:** a learned matrix `tok_emb ∈ R^{V×D}`. Forward = `tok_emb[idx]`.
2. **Position embedding:** for context length `T`, `pos_emb ∈ R^{T×D}`. Add elementwise.
3. **Why?** Without position info the attention block is permutation-invariant (a "bag of tokens"). Show this with a 2-token toy example.
4. **Scaled dot-product attention (the key derivation):**
   - `Q = X @ Wq, K = X @ Wk, V = X @ Wv` (shapes `T × D_h` each)
   - `att = softmax((Q @ K^T) / sqrt(D_h)) @ V`
   - Causal mask: `att[i,j] = 0 for j > i` so token `t` only attends to `t' ≤ t`.

Walk a 4-token example by hand on the whiteboard.

### 5-min Pomodoro Break
Discretionary.

### Block 2 — 25 min — `train3.py` skeleton in numpy
```python
import numpy as np

T, D, Dh = 8, 32, 32   # context length, embed dim, head dim
V = 65                 # vocab

tok_emb = np.random.randn(V, D) * 0.02
pos_emb = np.random.randn(T, D) * 0.02
Wq = np.random.randn(D, Dh) * 0.02
Wk = np.random.randn(D, Dh) * 0.02
Wv = np.random.randn(D, Dh) * 0.02
Wo = np.random.randn(Dh, V) * 0.02     # tied or separate; here separate

def forward(idx_seq):
    """idx_seq: array of T ints"""
    x = tok_emb[idx_seq] + pos_emb         # (T, D)
    Q = x @ Wq; K = x @ Wk; Vh = x @ Wv    # (T, Dh)
    scores = Q @ K.T / np.sqrt(Dh)         # (T, T)
    mask = np.tril(np.ones((T, T)))
    scores = np.where(mask == 1, scores, -1e9)
    att = np.exp(scores - scores.max(axis=-1, keepdims=True))
    att /= att.sum(axis=-1, keepdims=True)
    h = att @ Vh                           # (T, Dh)
    logits = h @ Wo                        # (T, V)
    return logits, att
```

### 2-min Diffuse Mode Reflection
*"Why divide by sqrt(Dh)? What blows up otherwise?"*

### Homework Preview
Thursday: backward pass through attention, full training loop.

---

## SESSION 2 — Thursday, July 9, 2026

### Stuck Check (3 min)
"Whose mask doesn't look triangular? Whose attention sums to 1? Who isn't sure why position embedding is added vs concatenated?"

### Big Picture (1 min)
Step 4 still. *"Today: train it. See it learn structure beyond bigram."*

### Block 1 — 25 min — Backward + training
For numpy + manual: derive `dQ`, `dK`, `dV` from chain rule (or use Karpathy's Python `Value` from W3 if you want full autograd — slower but pedagogically pure). Karpathy's `train3.py` uses numpy for the heavy ops with manual or vectorized backward; either approach is acceptable.

Show the loss curve dropping. Sample text. Note the *qualitative* improvement vs MLP — words start to look like words.

### 5-min Pomodoro Break
Discretionary.

### Block 2 — 25 min — Lab: Visualize the attention matrix
Each pro picks a 16-character string from the corpus, runs the model, and visualizes the (T, T) post-softmax attention matrix as a heatmap. Annotate which positions attend most strongly to which.

### 2-min Diffuse Mode Reflection
*"You looked at the actual attention pattern. What did you expect to see, and what did you see?"*

### Homework Preview
**Assignment W4 below.**

---

## WEEK 4 QUIZ — Track C (10 questions)

> **Spaced repetition:** Q9 + Q10 review Week 2 (manual gradients).

**Easy (5)**

1. The shape of `Q @ K^T` for a single head is:
   - A) `(D, D)` · B) `(T, T)` · C) `(T, D)` · D) `(V, V)`

2. Causal masking sets attention scores at `j > i` to:
   - A) 0 · B) `-inf` (so softmax → 0) · C) 1 · D) Mean

3. Position embeddings exist because:
   - A) They're decorative · B) Self-attention is permutation-invariant without positional information · C) For RAM · D) Required by Python

4. `softmax` along axis -1 normalizes:
   - A) Across batch · B) Each row of attention scores to sum to 1 · C) The values · D) Both axes

5. Scaling by `sqrt(D_h)` keeps:
   - A) Numerical precision · B) The variance of dot products bounded so softmax doesn't saturate · C) Memory low · D) None

**Medium (3)**

6. The attention output shape (single head, no batch) is:
   - A) `(T, D)` (after Wo back to embed dim) · B) `(T, D_h)` (right after attention, before any output proj) · C) `(V, T)` · D) `(D, V)`

7. Token embeddings are learnable:
   - A) Matrices indexed by token id · B) Random and frozen · C) One-hot · D) Computed from tf-idf

8. Self-attention is *self*-attention because:
   - A) Q, K, V come from the same input sequence · B) It calls itself recursively · C) It re-attends to outputs · D) It's reflexive

**Hard (2)**

9. *(Week 2 review)* The gradient `dL/dlogits` for cross-entropy is:
   - A) `softmax(logits) - onehot(y)` · B) `logits` · C) `onehot(y)` · D) `1`

10. *(Week 2 review)* Why subtract `logits.max()` before `exp` in softmax?
    - A) Make the max =0 · B) Numerical stability — avoid `exp(big number)` overflow · C) Required by transformer · D) Speed

### Answer Key
1.B  2.B  3.B  4.B  5.B  6.B  7.A  8.A  9.A  10.B

---

## WEEK 4 ASSIGNMENT — Track C

**Title:** *Implement `train3.py` — embeddings + single-head causal self-attention*
**Due:** Mon Jul 13, 11:59 PM PST · GitHub link

### Instructions
1. Build `train3.py`:
   - Char-level tokenizer (reuse from W1).
   - Token embedding (V×D), position embedding (T×D).
   - Single-head causal self-attention with `Wq, Wk, Wv` and an output projection `Wo`.
   - Cross-entropy loss with stable softmax.
   - Either pure numpy with manual backward, OR pure-Python with your W3 `Value` class.
2. Train on Tiny Shakespeare for at least 5,000 iterations.
3. Compute test perplexity and generate a 500-character sample.
4. Render a heatmap of the attention matrix on a 16-token slice. Save as PNG in repo.
5. Update README: ppl chain so far (bigram → MLP → attention), the heatmap, and a paragraph on what attention is qualitatively learning.

### Grading Criteria — $1.50 when:
- [ ] `train3.py` runs end-to-end (0.30)
- [ ] Embeddings + attention correctly shaped (verify via shape asserts) (0.40)
- [ ] Training reduces loss substantially (0.20)
- [ ] Sample + attention heatmap in README (0.40)
- [ ] Code clean, single-file (0.20)

### Stretch
Increase `T` to 32 and embed dim to 64. Try without position embeddings — confirm the model fails to learn ordering. Document.

---

## Cumulative Mind Map (Week 4)

```
microGPT staircase:
  W1 [bigram] · W2 [MLP] · W3 [Value autograd]
  W4 [embeddings + 1-head attention] ← YOU ARE HERE
  W5 [multi-head + LN]
  W6 [Adam → microGPT complete]
  W7 [showcase]

New skills:
  ML: token & position embeddings, scaled dot-product attention, causal mask, attention as
       differentiable retrieval over the past
  Numerics: stability in softmax, sqrt(D_h) scaling
  Insight: ALL the structure that beats bigram comes from this one trick.
```

Caption: *"Next week: stack heads, normalize layers, full transformer block."*
