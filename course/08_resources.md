# ARTIFACT 8 — Open Source Resources List

*Curated by Venkata Chintapalli for Python Pathways: From Zero to Builder.*

> **Rule of thumb:** every link below is **free** at the time of writing. If a paywall appears, alert the instructor and we'll find the open mirror.

---

## Track A — 5th Graders { #track-a-resources }

### Books (free)
- **"Invent Your Own Computer Games with Python"** by Al Sweigart — `https://inventwithpython.com/invent4thed/` — the gold standard intro for kids; matches our Pygame curriculum exactly.
- **"Making Games with Python & Pygame"** by Al Sweigart — `https://inventwithpython.com/pygame/` — perfect after Week 4; expands beyond what we cover.

### Documentation
- **Pygame docs** — `https://www.pygame.org/docs/` — the reference. We use `pygame.draw`, `pygame.event`, `pygame.font`, `pygame.mixer`, `pygame.Rect`.
- **Python `turtle` module** — `https://docs.python.org/3/library/turtle.html` — for Weeks 1–2.

### Free courses
- **CS50P (Harvard's Intro to Programming with Python)** — `https://cs50.harvard.edu/python/2022/` — recommended INTRO modules only (Week 0 "Functions, Variables", Week 1 "Conditionals", Week 2 "Loops"). Skip beyond that for now — it gets faster than a 5th grader needs.
- **Replit's Python beginner tutorials** — `https://replit.com/learn` — short, browser-based, great for between-class warmups.

### YouTube channels (age-appropriate, parent-vetted)
- **Tech With Tim** — `https://www.youtube.com/c/TechWithTim` — pygame tutorials, calm pace; recommended for after Week 4.
- **Code Palace** — `https://www.youtube.com/@CodePalace` — beginner Python with games and animations.
- **Coding Train** by Daniel Shiffman — `https://www.youtube.com/@TheCodingTrain` — energetic, creative coding; a few Python videos and lots of inspirational stuff.
- **DrCodie** — `https://www.youtube.com/@DrCodie` — short, fun, kid-targeted Python clips.

### Game asset sources (free, kid-friendly)
- **OpenGameArt.org** — sprites and tiles, mostly CC-licensed.
- **Kenney.nl** — free game-art packs, public-domain.
- **Freesound.org** — sound effects (parent should help vet specific files).

---

## Track B — 10th Graders { #track-b-resources }

### Free datasets
- **UCI ML Repository — Heart Disease (Cleveland)** — `https://archive.ics.uci.edu/ml/datasets/heart+disease` — 303 patients, the classic teaching dataset.
- **PIMA Indians Diabetes (Kaggle mirror)** — `https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database` — 768 records, classic.
- **Breast Cancer Wisconsin (Diagnostic)** — `https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)` — 569 samples, great for binary-classification challenges.
- **PhysioNet** (advanced, requires data-use agreement) — `https://physionet.org/` — when you're ready for real ICU data (MIMIC-IV).

### Documentation
- **pandas** — `https://pandas.pydata.org/docs/`
- **matplotlib** — `https://matplotlib.org/stable/users/index.html`
- **seaborn** — `https://seaborn.pydata.org/tutorial.html`
- **scipy.stats** — `https://docs.scipy.org/doc/scipy/reference/stats.html`
- **BioPython tutorial** — `https://biopython.org/wiki/Documentation` and the Cookbook — `https://biopython.org/DIST/docs/tutorial/Tutorial.html`

### Free books
- **"Python for Data Analysis" (3rd ed.)** by Wes McKinney — `https://wesmckinney.com/book/` — the official free online edition by the author of pandas.
- **"Python Data Science Handbook"** by Jake VanderPlas — `https://jakevdp.github.io/PythonDataScienceHandbook/` — free online; great chapters on numpy + pandas + matplotlib.

### Free courses
- **Khan Academy — Statistics and Probability** — `https://www.khanacademy.org/math/statistics-probability` — perfect prep for Week 4. Run units: Analyzing categorical data, Modeling data distributions, Probability, Random variables, Inference.
- **Google Colab beginner guide** — `https://colab.research.google.com/notebooks/welcome.ipynb` — get the platform under your fingers.
- **DataCamp's free pandas tutorial** — `https://www.datacamp.com/tutorial/pandas` — bookmarkable.

### Medical-informatics references (real-world)
- **PhysioNet's WFDB Python package** — `https://github.com/MIT-LCP/wfdb-python` — for reading actual ECG signals (advanced, post-course).
- **GitHub: `MIT-LCP/mimic-code`** — `https://github.com/MIT-LCP/mimic-code` — open-source notebooks built on the MIMIC-IV ICU dataset; great real-world reference.
- **JAMA's "Statistical Primer for Cardiovascular Research"** series — search PubMed (open-access summary articles), explains the biostat concepts you used in Week 4.

### YouTube
- **Corey Schafer's pandas series** — `https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS`
- **Aladdin Persson** — `https://www.youtube.com/@AladdinPersson` — clean coding walkthroughs.

---

## Track C — Professionals { #track-c-resources }

### The microGPT spine
- **Andrej Karpathy — microGPT post** — `https://karpathy.github.io/2026/02/12/microgpt/` — our reference. Every weekly milestone maps to a `trainN.py` here.
- **Karpathy `nanoGPT` GitHub** — `https://github.com/karpathy/nanoGPT` — the next step (with PyTorch). Read for taste.
- **Karpathy `micrograd` GitHub** — `https://github.com/karpathy/micrograd` — the autograd engine we rebuild in Week 3.

### Karpathy's Zero-to-Hero YouTube series (free, complete)
- **Full playlist** — `https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ`
  - Lesson 1 — micrograd (~2.5 hr) → Week 3 spine
  - Lesson 2 — bigrams + makemore → Week 1 spine
  - Lesson 3 — MLP for makemore → Week 2 spine
  - Lessons 4–6 — backprop ninja, batch norm, WaveNet → optional but recommended
  - Lesson 7 — let's build GPT (~1.5 hr) → consolidates Weeks 4–6
  - Lesson 8 — GPT tokenizer (BPE) → optional bonus

### Foundational papers (open-access)
- **"Attention Is All You Need" (Vaswani et al., 2017)** — `https://arxiv.org/abs/1706.03762` — the transformer paper.
- **"Language Models are Unsupervised Multitask Learners" (Radford et al., 2019, GPT-2)** — `https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf`
- **"GPT-3: Language Models are Few-Shot Learners" (Brown et al., 2020)** — `https://arxiv.org/abs/2005.14165`
- **"Training Compute-Optimal Large Language Models" (Hoffmann et al., 2022, Chinchilla)** — `https://arxiv.org/abs/2203.15556`
- **"FlashAttention" (Dao et al., 2022)** — `https://arxiv.org/abs/2205.14135` — the IO-aware attention algorithm.
- **"Adam" (Kingma & Ba, 2014)** — `https://arxiv.org/abs/1412.6980` — read for clarity on bias correction.
- **"AdamW / Decoupled Weight Decay Regularization" (Loshchilov & Hutter, 2017)** — `https://arxiv.org/abs/1711.05101`

### Visual / tutorial
- **The Illustrated Transformer** — Jay Alammar — `https://jalammar.github.io/illustrated-transformer/` — best diagrammatic explanation of the architecture in existence.
- **The Annotated Transformer** — Sasha Rush et al. — `https://nlp.seas.harvard.edu/annotated-transformer/` — paper-with-code annotation.
- **3Blue1Brown's "Neural Networks" series** — `https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi` — for visual intuition.

### Free advanced courses
- **fast.ai — Practical Deep Learning for Coders** — `https://course.fast.ai/` — Lessons 1–4 are most relevant for what we cover; lessons 5+ go further.
- **MIT 6.S191 — Intro to Deep Learning** — `http://introtodeeplearning.com/`
- **Stanford CS224N (NLP w/ Deep Learning)** — public lectures: `https://web.stanford.edu/class/cs224n/`
- **HuggingFace NLP Course** — `https://huggingface.co/learn/nlp-course/chapter1/1` — once you graduate from from-scratch land.

### Documentation
- **PyTorch official docs** — `https://pytorch.org/docs/stable/index.html` — your next stop after this course.
- **NumPy docs** — `https://numpy.org/doc/stable/`
- **Hugging Face `transformers`** — `https://huggingface.co/docs/transformers/index`

### Communities & ongoing reading
- **arxiv-sanity** — `https://arxiv-sanity.com` — Karpathy's research feed.
- **Papers with Code** — `https://paperswithcode.com/`
- **EleutherAI Discord + GitHub** — open-source LLM research community.
- **Anthropic Interpretability papers** — `https://transformer-circuits.pub/` — for understanding *what* attention is doing inside trained models.

### Career resources for the pivot
- **Chip Huyen's "Designing Machine Learning Systems"** book — paid, but her free blog is excellent: `https://huyenchip.com/`
- **Lilian Weng's blog** — `https://lilianweng.github.io/` — clear deep dives on RLHF, attention variants, agents.
- **The Gradient (publication)** — `https://thegradient.pub/` — accessible long-form ML writing.
