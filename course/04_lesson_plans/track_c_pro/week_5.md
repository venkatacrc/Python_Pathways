# Track C — Week 5: "The Full Architecture + train4.py — Multi-Head Attention"

**Dates:** Tue Jul 14 + Thu Jul 16, 2026 · 6:30 PM PST · Python 3
**Big Picture:** *Week 5 of 7 — multiple attention heads + LayerNorm + feed-forward MLP per block, stacked. By Friday, the architecture is GPT-2 in miniature.*

---

## SESSION 1 — Tuesday, July 14, 2026

### Learning Objectives
1. Implement multi-head attention by reshape (H heads of head-dim D/H).
2. Implement LayerNorm with learnable γ, β.
3. Compose a transformer block: `x = x + Attn(LN(x)); x = x + MLP(LN(x))` (pre-norm).

### Active Recall (3 min)
"Why do we add position embeddings? What does causal mask look like? What does attention output shape look like?"

### Big Picture (1 min)
Step 5 of 7. *"You've got 1 head. We give the model 4 or 8 heads, each looking at a different relationship pattern."*

### Block 1 — 25 min — Multi-head attention
Key idea: split `D` into `H` heads of size `D/H`, run attention per head, concatenate, then project.

```python
H = 4
Dh = D // H

def multi_head_attention(x, Wq, Wk, Wv, Wo):
    """x: (T, D); Wq/Wk/Wv: (D, D); Wo: (D, D)"""
    T = x.shape[0]
    Q = (x @ Wq).reshape(T, H, Dh).transpose(1, 0, 2)   # (H, T, Dh)
    K = (x @ Wk).reshape(T, H, Dh).transpose(1, 0, 2)
    Vh = (x @ Wv).reshape(T, H, Dh).transpose(1, 0, 2)
    scores = Q @ K.transpose(0, 2, 1) / np.sqrt(Dh)     # (H, T, T)
    mask = np.tril(np.ones((T, T)))
    scores = np.where(mask == 1, scores, -1e9)
    att = np.exp(scores - scores.max(-1, keepdims=True))
    att /= att.sum(-1, keepdims=True)
    out = att @ Vh                                       # (H, T, Dh)
    out = out.transpose(1, 0, 2).reshape(T, D)           # (T, D)
    return out @ Wo
```

### 5-min Pomodoro Break
Discretionary.

### Block 2 — 25 min — LayerNorm
```python
def layer_norm(x, gamma, beta, eps=1e-5):
    """x: (T, D); gamma/beta: (D,)"""
    mu = x.mean(-1, keepdims=True)
    var = x.var(-1, keepdims=True)
    return gamma * (x - mu) / np.sqrt(var + eps) + beta
```
Walk through each component. Compare to BatchNorm and explain why LN wins for sequence models.

### 2-min Diffuse Mode Reflection
*"What does each attention head specialize in? Speculate."*

### Homework Preview
Thursday: full transformer block + stack 2-4 of them.

---

## SESSION 2 — Thursday, July 16, 2026

### Stuck Check (3 min)
"Whose multi-head reshape is wrong? Whose LayerNorm broadcasts incorrectly? Whose loss explodes when you stack blocks?"

### Big Picture (1 min)
Step 5 still. *"Stack the block. We now have a real transformer."*

### Block 1 — 25 min — The transformer block
```python
def transformer_block(x, params):
    # Pre-norm style — same as Karpathy's nanoGPT and microGPT
    a = layer_norm(x, params["g1"], params["b1"])
    x = x + multi_head_attention(a, params["Wq"], params["Wk"], params["Wv"], params["Wo"])
    a = layer_norm(x, params["g2"], params["b2"])
    h = (a @ params["W_in"]).clip(0)              # ReLU MLP
    x = x + h @ params["W_out"]
    return x
```
Discussion: residual connections, why pre-norm trains more stably than post-norm at depth.

### 5-min Pomodoro Break
Discretionary.

### Block 2 — 25 min — Lab: Stack 2 blocks
Each pro stacks 2 transformer blocks. Trains on Tiny Shakespeare. Compares loss against `train3` (single-head, no LN, no MLP, no residuals). Notes the qualitative jump: actual short words emerge.

### 2-min Diffuse Mode Reflection
*"You just stacked transformer blocks. Why does ResNet-style residual work as well here as in vision?"*

### Homework Preview
**Assignment W5 below.**

---

## WEEK 5 QUIZ — Track C (10 questions)

> **Spaced repetition:** Q9 + Q10 review Week 3 (autograd `Value`).

**Easy (5)**

1. With `D=64` and `H=4`, the per-head dim is:
   - A) 4 · B) 16 · C) 32 · D) 64

2. LayerNorm normalizes over:
   - A) Batch · B) The feature dim of each token, per-token · C) Heads · D) Time

3. Pre-norm means LayerNorm is applied:
   - A) After the residual sum · B) Inside the residual branch, before the operation · C) Never · D) Only at the end

4. Residual connections:
   - A) Slow training · B) Help gradient flow + identity shortcut · C) Are decorative · D) Required only for vision

5. The MLP inside a transformer block typically uses:
   - A) Sigmoid · B) ReLU or GELU · C) tanh always · D) Linear only

**Medium (3)**

6. Multiple heads exist because:
   - A) They look at different subspaces / relationships in parallel · B) Required by Python · C) Decorative · D) Faster only

7. `np.tril` returns:
   - A) An upper-triangular ones matrix · B) A lower-triangular ones matrix · C) Random · D) A vector

8. Stacking 2 blocks vs 1 typically yields:
   - A) No change · B) Better loss but more compute · C) Worse loss · D) Errors

**Hard (2)**

9. *(Week 3 review)* The `Value._backward` closure of `c = a + b` updates:
   - A) `c.data` · B) `a.grad += c.grad; b.grad += c.grad` · C) Errors · D) `a.grad = c.grad`

10. *(Week 3 review)* Why does `__pow__(self, n)` only support `n: float|int`, not `Value`?
    - A) For simplicity in the educational engine; `Value`-power requires the full `exp(n*log(x))` chain    - B) PyTorch limitation · C) Always works · D) Forbidden by Python

### Answer Key
1.B  2.B  3.B  4.B  5.B  6.A  7.B  8.B  9.B  10.A

---

## WEEK 5 ASSIGNMENT — Track C

**Title:** *Implement `train4.py` — multi-head attention + LayerNorm + 2-block transformer*
**Due:** Mon Jul 20, 11:59 PM PST · GitHub link

### Instructions
1. Implement `train4.py`:
   - Multi-head causal self-attention (H=4 by default).
   - Pre-norm LayerNorm.
   - MLP block with ReLU (or GELU).
   - 2 stacked transformer blocks.
   - Standard cross-entropy training loop with SGD (we'll add Adam next week).
2. Train on Tiny Shakespeare for at least 10,000 iterations.
3. Generate a 500-character sample.
4. Update README:
   - PPL chain: bigram → MLP → 1-head attn → multi-head + 2 blocks
   - Sample comparison from each milestone
   - 1 paragraph: which architectural change gave the biggest jump?

### Grading Criteria — $1.50 when:
- [ ] Multi-head attention implemented with correct reshape (0.40)
- [ ] LayerNorm + residuals + MLP block in pre-norm style (0.40)
- [ ] 2 blocks stacked, training stable (0.20)
- [ ] PPL comparison + sample chain in README (0.30)
- [ ] Code organized, documented (0.20)

### Stretch
Use GELU instead of ReLU. Try `H=8`. Try `T=64`, `D=128`. Note compute scaling: attention is O(T²·D), MLP is O(T·D²). Plot loss curve.

---

## Cumulative Mind Map (Week 5)

```
microGPT staircase:
  W1 bigram · W2 MLP · W3 Value autograd · W4 1-head attention
  W5 [multi-head + LN + transformer block stack] ← YOU ARE HERE
  W6 [Adam → microGPT complete]
  W7 [showcase]

New skills:
  Architecture: multi-head reshape, LayerNorm, residual + pre-norm pattern, transformer block,
                  stacking depth
  Insight: GPT-2 = this block, repeated N times, with Adam.
```

Caption: *"Next week: better optimizer (Adam) → microGPT is COMPLETE."*
