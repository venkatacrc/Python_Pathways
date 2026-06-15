# Track C — Week 3: "Autograd Engine + train2.py — The Value Class"

**Dates:** Tue Jun 30 + Thu Jul 2, 2026 · 6:30 PM PST · Python 3 (stdlib only)
**Big Picture:** *Week 3 of 7 — you build your own PyTorch. Scalar autograd in ~150 lines: `Value` class with operator overloading and a topological backward pass. This is **micrograd**.*
**⚠️ Heads up:** Tuesday Jun 30 is normal. Thursday Jul 2 is the at-risk session before July 4th weekend. **Async option below.**

---

## SESSION 1 — Tuesday, June 30, 2026

### Learning Objectives
1. Implement Python's data model dunder methods to overload `+`, `-`, `*`, `/`, `**`.
2. Build a scalar `Value` class that records the computation graph for backprop.
3. Implement `backward()` via topological sort of the graph.

### Active Recall (3 min)
"State chain rule. Why is `d/dx tanh(x) = 1 - tanh(x)^2`? What's the gradient shape of a (V,H)-shaped weight matrix?"

### Big Picture (1 min)
Step 3 of 7. *"Tonight we stop computing gradients by hand and build the **mechanism that does it for us, automatically**, in pure Python."*

### Block 1 — 25 min — Build the `Value` class
```python
# train2.py — micrograd-style scalar autograd
class Value:
    def __init__(self, data, _children=(), _op=""):
        self.data = float(data)
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op

    def __repr__(self): return f"Value({self.data:.4f}, grad={self.grad:.4f})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), "+")
        def _back():
            self.grad  += 1.0 * out.grad
            other.grad += 1.0 * out.grad
        out._backward = _back
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), "*")
        def _back():
            self.grad  += other.data * out.grad
            other.grad += self.data  * out.grad
        out._backward = _back
        return out

    def __pow__(self, other):
        assert isinstance(other, (int, float))
        out = Value(self.data ** other, (self,), f"**{other}")
        def _back():
            self.grad += other * self.data**(other - 1) * out.grad
        out._backward = _back
        return out

    def relu(self):
        out = Value(max(0.0, self.data), (self,), "relu")
        def _back():
            self.grad += (out.data > 0) * out.grad
        out._backward = _back
        return out

    def __neg__(self):    return self * -1
    def __sub__(self, o): return self + (-o)
    def __radd__(self, o): return self + o
    def __rmul__(self, o): return self * o
    def __rsub__(self, o): return (-self) + o
    def __truediv__(self, o): return self * (o ** -1) if isinstance(o, Value) else self * (1.0 / o)

    def backward(self):
        topo, visited = [], set()
        def build(v):
            if v in visited: return
            visited.add(v)
            for c in v._prev: build(c)
            topo.append(v)
        build(self)
        self.grad = 1.0
        for v in reversed(topo):
            v._backward()
```

Demonstrate:
```python
a = Value(2.0); b = Value(-3.0); c = Value(10.0)
e = a*b; d = e + c; f = d * Value(0.5)
f.backward()
print(a.grad, b.grad, c.grad)   # -1.5, 1.0, 0.5
```

### 5-min Pomodoro Break
Discretionary.

### Block 2 — 25 min — Lab: Two-layer net on `Value`
```python
import random
class Neuron:
    def __init__(self, nin):
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
        self.b = Value(0.0)
    def __call__(self, x):
        return sum((wi*xi for wi,xi in zip(self.w, x)), self.b).relu()

class Layer:
    def __init__(self, nin, nout): self.neurons = [Neuron(nin) for _ in range(nout)]
    def __call__(self, x): return [n(x) for n in self.neurons]

class MLP:
    def __init__(self, sizes):
        self.layers = [Layer(sizes[i], sizes[i+1]) for i in range(len(sizes)-1)]
    def __call__(self, x):
        for L in self.layers: x = L(x)
        return x[0] if len(x) == 1 else x
    def parameters(self):
        return [p for L in self.layers for n in L.neurons for p in (n.w + [n.b])]
```

Train on the moons toy dataset (linked from this page — small XOR-like). Watch loss go down. Cheers.

### 2-min Diffuse Mode Reflection
*"How does the topological sort guarantee correct backprop order?"*

### Homework Preview
Thursday: hook `Value` into our character-LM and run train2 properly. + async option for those traveling.

---

## SESSION 2 — Thursday, July 2, 2026  *(at-risk session — async option below)*

### Stuck Check (3 min)
"Whose `backward()` returns wrong grads? Whose `__pow__` was buggy? Whose RAM exploded on a long graph?"

### Big Picture (1 min)
Step 3 still. *"Connect `Value` to the language model. Convince yourself it's exactly what train1 did, by hand, but auto."*

### Block 1 — 25 min — `train2.py` proper
Replace the manual gradients in `train1.py` with `Value`-graph training. The key is the loss is just:
```python
loss = sum(((logit_v - onehot_v)**2 for logit_v, onehot_v in zip(logits, onehot)), Value(0))
loss.backward()
```
(Or use a Value-based softmax + log; either is fine for educational purposes — Karpathy's Zero-to-Hero uses MSE first then NLL.)

### 5-min Pomodoro Break
Discretionary.

### Block 2 — 25 min — Lab: Convergence Check
Each pro confirms `train2.py` converges to a similar loss as `train1.py` and matches gradient direction. Bonus: write a *unit test* that asserts numerical agreement between `train1`'s analytical gradient and `train2`'s autograd gradient on the same weight.

### 2-min Diffuse Mode Reflection
*"You built the equivalent of `torch.Tensor` with autograd. What does PyTorch add on top of this that we won't, and why?"*

### Homework Preview
**Assignment W3 below.**

---

### 🇺🇸 ASYNC ALTERNATIVE for Thursday Jul 2

If you can't attend live for July 4th weekend:
1. **Watch:** Karpathy's "The spelled-out intro to neural networks and backpropagation: building micrograd" video (Zero-to-Hero, lesson 1, ~2.5 hr — but you can 1.5×).
2. **Read:** the Tuesday Jun 30 transcript on this week's course-site page + the `train2.py` walkthrough page.
3. **Code:** complete the `Value` class + `MLP` and run on the moons toy dataset.
4. **Hook to LM:** swap the manual gradients in your `train1.py` for `Value`-based autograd, train, sample.
5. **Post:** in `[C] Track C Forum`, share a screenshot showing `train1.py` and `train2.py` reach similar loss + a sentence comparing wallclock time.

Full credit on completion.

---

## WEEK 3 QUIZ — Track C (10 questions, 15 min)

> **Spaced repetition:** Q9 + Q10 review Week 1 (bigram baseline / vocab).

**Easy (5)**

1. To overload `+` for a class, you implement:
   - A) `add(self, other)` · B) `__add__(self, other)` ✅ · C) `__plus__` · D) `+=`

2. After `out.backward()`, the gradient of every leaf `Value` is:
   - A) Always 0 · B) Computed via reversed topo sort with chain rule ✅ · C) Random · D) Equal to data

3. Topological sort visits each node:
   - A) Twice · B) Once, after all its children ✅ · C) Never · D) In random order

4. `Value(3) ** 2` should produce a Value with `data=`:
   - A) 6 · B) 9 ✅ · C) 5 · D) 1

5. The `_backward` closure on each Value is responsible for:
   - A) Forward computation · B) Adding the *local* gradient contributions to its parents ✅ · C) Garbage collection · D) Topo sort

**Medium (3)**

6. Why must we *accumulate* gradients (`+=`) rather than assign?
   - A) For style · B) Because a parameter may participate in multiple paths in the graph and contributions must sum ✅ · C) For speed · D) Required by Python

7. The graph stored in `_prev` enables:
   - A) Forward pass only · B) Topological backward pass ✅ · C) Repeated forward · D) Pickling

8. Calling `backward()` twice on the same loss without zeroing:
   - A) Doubles all grads ✅ (gradients accumulate) · B) Errors · C) Resets · D) Has no effect

**Hard (2)**

9. *(Week 1 review)* On Tiny Shakespeare, vocab includes:
   - A) Just lowercase letters · B) Letters (both cases), digits, punctuation, whitespace ✅ · C) Words · D) Bytes

10. *(Week 1 review)* Why does the bigram model never produce coherent words?
    - A) Wrong dataset · B) It can only condition on the immediately previous character ✅ · C) Smoothing too high · D) Vocab too small

### Answer Key
1.B  2.B  3.B  4.B  5.B  6.B  7.B  8.A  9.B  10.B

---

## WEEK 3 ASSIGNMENT — Track C

**Title:** *Implement `train2.py` (Value autograd + MLP)*
**Due:** Mon Jul 6, 11:59 PM PST · GitHub link

### Instructions
1. Implement the `Value` class with `+ - * / ** -unary tanh relu` ops, all with correct `_backward` closures.
2. Build `Neuron`, `Layer`, `MLP` classes on top.
3. Use it to train a 2-layer MLP on the **moons** dataset (provided as a function linked from this page, ~100 points).
4. Plot the decision boundary (matplotlib OK *for plotting only* — no PyTorch).
5. Write a `tests/test_grads.py` that asserts numerical gradients match analytical `Value` grads to 1e-5 on at least 5 different operations.
6. Update README with:
   - Train/test loss curves
   - Decision boundary screenshot
   - 1-paragraph comparison: hand-rolled gradients (W2) vs `Value` autograd (W3) — which was easier? Faster? Less error-prone?

### Grading Criteria — $1.50 when:
- [ ] `Value` class implemented + tests pass (0.50)
- [ ] MLP trains and learns the moons (0.30)
- [ ] Decision boundary plot included (0.20)
- [ ] Numerical-gradient tests pass (0.30)
- [ ] README comparison paragraph (0.20)

### Stretch
Add `Value.exp()` and `Value.log()`, then implement true cross-entropy loss with `Value`. Train your character-LM on it.

---

## Cumulative Mind Map (Week 3)

```
microGPT staircase:
  W1 [bigram count table]
  W2 [MLP, manual SGD + backprop]
  W3 [scalar autograd: micrograd Value class] ← YOU ARE HERE
  W4 [embeddings + 1-head attention]
  W5 [multi-head + LN]
  W6 [Adam → microGPT complete]
  W7 [showcase]

New skills:
  Python: dunder methods (`__add__`, `__mul__`, `__pow__`), closures, topological sort
  ML: forward graph, reverse-mode autodiff, gradient accumulation
  Engineering: numerical grad checks, unit tests around math
  Insight: PyTorch is this pattern, scaled to tensors + GPU.
```

Caption: *"Next week: tokens become VECTORS. Embeddings + the dot-product attention head."*
