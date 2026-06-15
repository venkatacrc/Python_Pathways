# ARTIFACT 5 — Office Hours Agendas: Track C (Professionals)

**Format:** 60 minutes weekly, Zoom, recorded.
**Suggested time slot:** Wednesday 7:30–8:30 PM PST (mid-week, between Tue/Thu sessions; lets the cohort apply Tuesday's content and arrive at Thursday primed).
**Tone:** peer-to-peer. Smart adults; move fast; reference papers and ecosystem freely.

---

## Week 1 — Wed Jun 17, 2026

**0–10 — Open Q&A (Implement & evaluate `train0.py`)**
- "What's the right held-out split?" | "Why does add-1 smoothing break perplexity comparisons across n?" | "Should I write tests this early?"

**10–30 — Top 3 Confusion Points**
1. **Smoothing mechanics.** Why add-1 perplexity isn't directly comparable to no-smoothing perplexity. Show Kneser-Ney as the next step (briefly; we won't implement).
2. **Memory of `n`-gram counts.** `O(V^n)` rapidly hits RAM; `defaultdict(Counter)` saves you because most pairs never occur.
3. **Stochasticity in sampling.** Why you should `random.seed(0)` for reproducible Forum posts.

**30–50 — "Go Further"**
Live demo: train a 4-gram, observe quality, profile memory with `tracemalloc`. Discuss why scaling up n-grams is a dead end (motivates neural).

**50–60 — Preview Week 2**
*"Next week: gradients by hand. The most under-rated 2 hours in any ML curriculum."*

---

## Week 2 — Wed Jun 24, 2026

**0–10 — Open Q&A (Implement `train1.py`)**
- "Why does my loss diverge at lr=1.0?" | "Numerical gradient check is failing on `tanh` derivative." | "How do I batch the inputs cleanly?"

**10–30 — Top 3 Confusion Points**
1. **Gradient sign errors.** Walk through the cross-entropy gradient derivation again; common bug is forgetting the chain through softmax.
2. **`tanh` derivative.** `1 - tanh(x)^2`, NOT `1 - x^2`. Easy mix-up.
3. **Initialization scale.** `0.01` works; `1.0` blows up. Why: large pre-activations saturate `tanh`, gradients ≈ 0.

**30–50 — "Go Further"**
Mini-demo of **Xavier/Glorot** initialization. Talk about why `He init` is the right default for ReLU. Connect to W5 transformer block.

**50–60 — Preview Week 3**
*"Next week: stop computing gradients by hand. Build the engine that does it for you."*

---

## Week 3 — Wed Jul 1, 2026 *(July 4 weekend; expect cohort to be split — async option active)*

**0–10 — Open Q&A (Value autograd + MLP)**
- "My `__pow__` for fractional powers crashes." | "Topological order of the graph isn't unique — does that matter?" | "Cycles in a `Value` graph: possible?"

**10–30 — Top 3 Confusion Points**
1. **Gradient accumulation `+=` vs assignment.** Common bug: a node used twice in the graph gets its grad over-written if you use `=`. Show with a simple `c = a*b + a` example.
2. **Memory leaks from circular references.** `_prev` is a set of children, not parents — by design — to avoid cycles. Note Python GC handles closures fine.
3. **Numerical gradient checks pass at scale ≈ 1, fail at extreme scales.** Show the `eps` choice and the relative-error metric.

**30–50 — "Go Further"**
Implement `Value.exp()` and `Value.log()` together. Use them to write proper cross-entropy with autograd.

**50–60 — Preview Week 4**
*"Next week: ATTENTION. The trick that beats every prior architecture for sequences."*

---

## Week 4 — Wed Jul 8, 2026

**0–10 — Open Q&A (Embeddings + 1-head attention)**
- "Why is my attention sometimes still attending across the mask?" | "Position embedding: learned vs sinusoidal — which?" | "Logits `nan` after softmax — why?"

**10–30 — Top 3 Confusion Points**
1. **Mask is applied to scores PRE-softmax with `-inf` (effectively `-1e9`), not post-softmax.** Show the difference; post-softmax masking shifts the distribution by renormalizing residuals.
2. **`sqrt(D_h)` scaling is per-head.** The right value is `D / H = D_h`, not `D`. Bug if you scale by `sqrt(D)` after splitting heads.
3. **Numerical NaN traces.** `softmax` after `-1e9` is fine; but if you mask AFTER softmax, you renormalize zeros. Show.

**30–50 — "Go Further"**
Visualize attention weights at multiple depths/heads on a 16-token Shakespeare snippet. Discuss interpretability (Voita et al. — heads specialize).

**50–60 — Preview Week 5**
*"Next week: MULTI-HEAD + LAYERNORM + STACK. Your transformer."*

---

## Week 5 — Wed Jul 15, 2026

**0–10 — Open Q&A (Multi-head + LayerNorm + 2 blocks)**
- "Pre-norm vs post-norm — which is correct?" | "My multi-head reshape gives wrong shapes." | "GELU vs ReLU?"

**10–30 — Top 3 Confusion Points**
1. **Multi-head reshape mistakes.** The right ordering: `(T, D)` → `(T, H, D_h)` → transpose to `(H, T, D_h)`. Sketch shapes carefully on the board.
2. **Pre-norm is what you want.** GPT-2/3, LLaMA, microGPT all use pre-norm. Original "Attention Is All You Need" used post-norm and required learning-rate warmup; pre-norm is more stable.
3. **`np.var` defaults to ddof=0 (biased estimator).** That's fine for LayerNorm; clarify so they don't second-guess it.

**30–50 — "Go Further"**
Discuss **RMSNorm** (LLaMA's variant): drops mean centering, just scales by RMS. Faster, comparable quality. Implement in 5 lines.

**50–60 — Preview Week 6**
*"Next week: Adam → microGPT complete. We celebrate."*

---

## Week 6 — Wed Jul 22, 2026

**0–10 — Open Q&A (`train5.py` Adam + sampling)**
- "AdamW vs Adam?" | "Best lr for transformer of this size?" | "Why does temperature 0.5 still produce gibberish at 5k steps but coherent at 30k?"

**10–30 — Top 3 Confusion Points**
1. **Bias correction matters most early.** Show the `1 - β^t` term; at t=10 it's still meaningful, at t=10000 it's ≈1.
2. **AdamW's decoupled weight decay.** Vanilla Adam mixes WD with the gradient; AdamW applies WD as a separate term. Karpathy's nanoGPT uses AdamW.
3. **Temperature interactions with top-k.** Low temperature concentrates probability on the argmax; top-k prevents super-low probability outliers from sneaking in.

**30–50 — "Go Further"**
Profile training step — show that `Q @ K.T` is the dominant cost. This is the doorway to FlashAttention. Briefly cite Dao et al.

**50–60 — Preview Week 7**
*"Showcase. Your dataset, your hyperparameters, your samples. Lock in your Tuesday training run."*

---

## Week 7 — Wed Jul 29, 2026 — *Final pre-showcase polish*

**0–10 — Open Q&A**
- "My training stalled at loss 4.2." | "Tokenization for code corpora — char vs byte?" | "What's the cleanest 9-min talk structure?"

**10–30 — Top 3 Confusion Points**
1. **Stalled loss = lr too high or warmup needed.** Lower lr to 1e-4; add 500-step linear warmup.
2. **Tokenization for code.** Tabs and indentation matter — char-level handles fine; byte-level does too. BPE breaks identifiers in non-obvious ways.
3. **Showcase narrative.** Pattern: "Why this dataset → how I tokenized → what hyperparameters and why → samples + interesting failure mode → what I'd build next." 9 minutes is generous if you cut prefix-justification.

**30–50 — "Go Further"**
Demo of attention-head ablation: zero out one head's attention output, see how generation quality drops. (Diagnostic experiment from Voita et al. 2019.)

**50–60 — Wrap + Career Talk**
- Recommended next reads: Karpathy's `llm.c`, FlashAttention paper, "Mixture of Experts" (GShard, Switch), the Anthropic interpretability papers.
- Career: ML engineer (training infra), applied research (small but doable transition with this skill), technical writing (this curriculum is also a portfolio).
- Aug 3: final wallet payouts + certificate. *"You built a transformer in pure Python. That's the deepest mental model you'll ever have of this stack. Carry it forward."*
