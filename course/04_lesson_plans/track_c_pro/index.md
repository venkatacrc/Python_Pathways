---
title: Track C — Overview
---

# Track C · Professionals — microGPT from Scratch

<span class="track-badge c">TRACK C</span> Experienced engineers · Python 3 stdlib (numpy ok) · zero PyTorch

> By Thursday **July 30, 2026**, you'll have implemented Karpathy's **microGPT** progression end-to-end (`train0.py` → `train5.py`) and run it on a custom dataset of your choice.

## The 7-week staircase

```
train0  →  train1  →  train2  →  train3  →  train4  →  train5  →  SHOWCASE
bigram     MLP       Value      embed +    multi-     Adam →
            +SGD     autograd   1-head     head + LN  microGPT
                                attention  + block
```

## Weekly modules

- [Week 1 — `train0.py`: Bigram baseline](week_1.md)
- [Week 2 — `train1.py`: MLP + manual backprop](week_2.md)
- [Week 3 — `train2.py`: Value autograd engine](week_3.md) *(includes async option for July 4 weekend)*
- [Week 4 — `train3.py`: Embeddings + 1-head attention](week_4.md)
- [Week 5 — `train4.py`: Multi-head + LayerNorm](week_5.md)
- [Week 6 — `train5.py`: Adam → microGPT complete](week_6.md)
- [Week 7 — Showcase](week_7.md)

## Office hours

[Wednesday 7:30 PM PST · all 7 weeks of agendas](../../05_office_hours/track_c.md)

## Capstone rubric

[Track C microGPT Rubric ($12.50 max)](../../06_capstone_rubrics.md#track-c-rubric)

## Reference

- Karpathy, *microGPT* — `https://karpathy.github.io/2026/02/12/microgpt/`
- *Attention Is All You Need* (Vaswani et al.) — `https://arxiv.org/abs/1706.03762`
- Karpathy's *Zero to Hero* YouTube playlist (linked in [Resources](../../08_resources.md#track-c-resources))

## Tech setup

- Python 3.x locally **or** Google Colab.
- A GitHub account (you'll push `train0` … `train5` to your own repo).
- Clone the starter scaffolding once Week 1 unlocks.
