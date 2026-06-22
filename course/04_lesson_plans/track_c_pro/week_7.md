# Track C — Week 7: "SHOWCASE — Your microGPT on Custom Data"

**Dates:** Tue Jul 28 + Thu Jul 30, 2026 · 6:30 PM PST · Python 3
**Big Picture:** *Week 7 of 7 — Tuesday: train microGPT on your dataset. Thursday: SHOWCASE — outputs, design choices, the path to GPT-4.*

---

## SESSION 1 — Tuesday, July 28, 2026 — *Train on Your Data*

### Learning Objectives
1. Tokenize and ingest a custom corpus.
2. Pick reasonable hyperparameters given your dataset's size and structure.
3. Train, sample, and prepare a 5-min demo.

### Active Recall (3 min)
"State the difference between Adam and SGD updates in a sentence. What does temperature 0.5 vs 1.5 do to samples?"

### Big Picture (1 min)
Step 7 of 7 almost lit. *"Tonight you're not following Karpathy. You're applying him."*

### Block 1 — 25 min — Tokenization choices for your corpus
Discussion: char vs byte vs BPE.
- **Char-level (default):** small vocab, long sequences, simple. Karpathy ships this.
- **Byte-level:** vocab = 256, language-agnostic, handles any Unicode without preprocessing.
- **BPE / subword:** smaller sequence length, larger vocab, requires extra implementation.

For showcase, *char-level is encouraged* (we have one stdlib day). Byte is fair game. BPE is stretch (and probably out-of-scope this week).

### 5-min Pomodoro Break
Discretionary.

### Block 2 — 25 min — Train on your corpus
Each pro:
- Loads their corpus (code repo, poetry, financial filings, song lyrics, medical notes, Reddit, etc.).
- Tokenizes char-level.
- Picks `(T, D, H, n_blocks)` proportional to corpus size (rule of thumb: n_params ≤ corpus_size / 20).
- Trains as long as patience allows; saves checkpoints.
- Generates samples at multiple temperatures.

### 2-min Diffuse Mode Reflection
*"What surprised you about how YOUR corpus's text shows up at low vs high temperature?"*

### Homework Preview
Thursday: 9 min/person showcase. Bring 2 best samples and a 1-slide hyperparameter table.

---

## SESSION 2 — Thursday, July 30, 2026 — *🏆 THE SHOWCASE 🏆*

### Cold Open — 2 min
Instructor: *"Six weeks ago you couldn't have written `softmax` from scratch. Tonight you walk in with a working transformer trained on a domain of YOUR choice. Let's see what each of you cooked up."*

### Big Picture (1 min)
Step 7 of 7 LIT. The whole staircase — bigram to microGPT — glows. Caption: *"You built every step."*

### Showcase Block — ~50 min total (5 students × ~9 min each)
Each pro: 9 min total —
- 4 min — train/sample walkthrough: dataset, tokenization, hyperparams, sample outputs, attention heatmap if interesting.
- 2 min — *"Hardest engineering moment + biggest aha."*
- 3 min — Q&A from peers (instructor scores Capstone Rubric live, including the verbal attention-mechanism explanation).

### Discussion Block — 10 min
*"What would it take to scale this to GPT-4?"* Touchstones:
- Distributed training, parameter parallel, ZeRO/FSDP
- Mixed precision (bf16/fp16) — why
- Tokenizer (BPE / SentencePiece / Tiktoken)
- Curriculum, scaling laws (Chinchilla)
- Data quality > quantity (the C4, Pile lessons)
- Alignment: SFT, RLHF, DPO; safety
- Inference: KV cache, quantization, speculative decoding

### Career & Next Steps — 5 min
- Karpathy's nanoGPT → llm.c → llm.cpp progression
- fast.ai → Practical Deep Learning
- Papers with Code, arxiv-sanity, Anthropic / OpenAI / DeepMind tech reports
- "Build a transformer in CUDA" as the next stretch
- Job/role pivots: ML engineer, applied research, infra/training-platform roles

### Closing Ritual — 3 min
- Each pro writes in the course-site journal (Track C Discussion): *"On June 15 I couldn't __. Today I can __."*
- Instructor: *"Aug 3 = Certificate Day. Wallet payouts go out tomorrow. You're done."*
- Group screenshot.

### 2-min Diffuse Mode Reflection
*"What's the next thing you build?"*

---

## WEEK 7 QUIZ — Track C (10 questions)
*Optional — completion-based. $1.00 for honest attempt.*

> **Spaced repetition:** Q9 + Q10 review Week 5 (multi-head + LN).

**Easy (5)**

1. The capstone showcase is on:
   - A) Aug 1 · B) Jul 30 · C) Aug 3 · D) Jul 28

2. A char-level tokenizer's vocabulary on a typical English corpus is approximately:
   - A) ~30 · B) ~65–100 (depending on punctuation) · C) ~256 · D) ~50000

3. KV cache speeds up inference by:
   - A) Random sampling · B) Reusing previously-computed K and V across the autoregressive decode loop · C) Compression · D) Quantization

4. BPE produces subword tokens; pros include:
   - A) Smaller sequence length, OOV-resistant · B) Always smaller vocab · C) No tokenization cost · D) Forbidden in transformers

5. Chinchilla scaling laws suggest:
   - A) More params is always better · B) Compute should be split such that data tokens ≈ 20× parameter count for compute-optimal training · C) Data doesn't matter · D) Random

**Medium (3)**

6. Mixed-precision training (`bf16`):
   - A) Lossless · B) Trades a small precision for ~2× memory & speed; bf16 has the same exponent range as fp32 · C) Slower · D) Required for transformers

7. RLHF stands for:
   - A) Real-Life Human Filtering · B) Reinforcement Learning from Human Feedback · C) RL Hyperparameter Function · D) Random Latent Hidden Forward

8. The "secret" to GPT-4 is:
   - A) New math · B) Same architecture, much more compute + data + alignment + engineering · C) Quantum · D) Forbidden knowledge

**Hard (2)**

9. *(Week 5 review)* In a transformer block, the residual connection adds the:
   - A) Input of the block to the output of attention/MLP sub-layers · B) Logits · C) Embeddings · D) None

10. *(Week 5 review)* LayerNorm differs from BatchNorm by:
    - A) Normalizing across the batch · B) Normalizing across the feature dimension per sample (no batch statistics) · C) No difference · D) Slower

### Answer Key
1.B  2.B  3.B  4.A  5.B  6.B  7.B  8.B  9.A  10.B

---

## WEEK 7 ASSIGNMENT (Capstone Submission)

**Title:** *microGPT on Custom Data — Submission*
**Due:** Wed Jul 29, 11:59 PM PST

### Instructions
Submit:
1. GitHub repo link (final, with `train0.py` … `train5.py`, your custom-data run, samples).
2. A short README section describing your dataset, tokenization, hyperparameters, and 5 best samples.
3. A 2-minute screen-recording walking through the train + sample loop.
4. Forum post in `[C] Track C Forum` with: dataset name, sample paragraph, and a one-line explanation of attention applied to YOUR data domain.

### Grading
This is the **Capstone**, scored against the rubric in Artifact 6 — up to **$12.50**.

### No stretch this week.

---

## Final Cumulative Mind Map (Week 7)

```
microGPT staircase  |  Architectural addition           |  Pure-Python tools you mastered
=====================|====================================|====================================
W1 bigram           |  count table + smoothing          |  Counter, dataclass, type hints,
                    |                                     |  random.choices, urllib
W2 MLP              |  hidden layer, manual backprop    |  numpy, manual chain rule, SGD
                    |                                     |  loop, gradient check
W3 Value autograd   |  scalar autograd engine           |  dunder methods (__add__, __mul__,
                    |                                     |  __pow__), closures, topo sort
W4 1-head attention |  embeddings + scaled dot-prod     |  reshape, np.tril mask, softmax
                    |                                     |  stability, sqrt(D_h) scaling
W5 transformer      |  multi-head + LayerNorm + MLP +   |  multi-axis reshape, residual
   block            |  pre-norm + residual              |  connection patterns
W6 microGPT (Adam)  |  Adam with bias correction +      |  optimizer state, top-k & temp
                    |  temperature/top-k sampling       |  sampling
W7 SHOWCASE         |  custom dataset, your decisions   |  hyperparam taste, evaluation taste

Insight web at the top:
  - Attention = differentiable retrieval over the past
  - LayerNorm + residuals = trainability at depth
  - Adam = adaptive per-param step
  - Pure-Python implementation IS the curriculum;
    every magic in PyTorch was something you wrote yourself this term.
```

Caption: *"You walked from a bigram count-table to a working transformer in 7 weeks, in pure Python. Save this map. Remember it when you scale up."*
