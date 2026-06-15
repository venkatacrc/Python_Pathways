# Track B — Week 4: "The Numbers Behind Medicine — Statistics"

**Dates:** Tue Jul 7 + Thu Jul 9, 2026 · 6:30 PM PST · Colab + numpy + scipy
**Big Picture:** *Week 4 of 7 — every chart you made last week is a story; this week, you check whether the story is real. Mean, median, std, correlation, and your first inferential test.*

---

## SESSION 1 — Tuesday, July 7, 2026

### Learning Objectives
By the end of this session, students can:
1. Compute mean, median, std, IQR, and percentiles in pandas / numpy.
2. Compute Pearson and Spearman correlation between two variables.
3. Interpret correlation values (and what they don't tell you — *"correlation ≠ causation"*).

### Active Recall (3 min)
"What does `df.describe()` give? What's a histogram showing? What's `groupby` for?"

### Big Picture (1 min)
Step 4 of 7. *"This is the math med-students get tested on. We're doing it now."*

### Block 1 — 25 min
1. **Descriptive stats:**
   ```python
   pima["glucose"].mean(), pima["glucose"].median()
   pima["glucose"].std()
   pima["glucose"].quantile([0.25, 0.5, 0.75])
   ```
2. **By group:**
   ```python
   pima.groupby("outcome")["glucose"].agg(["mean", "median", "std"])
   ```
3. **Correlation:**
   ```python
   pima[["glucose","bmi","age","bp","outcome"]].corr()  # default Pearson
   pima[["glucose","bmi","age","bp","outcome"]].corr(method="spearman")
   ```
   Interpret: 0 = none, ±0.3 weak, ±0.5 moderate, ±0.7 strong, ±1 perfect.

### 5-min Pomodoro Break
"Read my Apple Watch": 60 sec — share one health number from your watch/phone (steps, heart rate, sleep). No pressure. Just reps of *"my body produces data."*

### Block 2 — 25 min — Lab: "What predicts diabetes?"
Each student computes correlation between `outcome` and every other column, sorts results, and writes 2 sentences:
- Which variables are most correlated?
- Why doesn't correlation alone make this a "cause"?

### 2-min Diffuse Mode Reflection
*"You just measured how strongly two clinical variables move together. What's a real-world example where two things correlate but DON'T cause each other?"*

### Homework Preview
Thursday: scipy + the t-test.

---

## SESSION 2 — Thursday, July 9, 2026

### Stuck Check (3 min)
"Whose correlation matrix has weird NaN values? Whose interpretations feel uncertain?"

### Big Picture (1 min)
Step 4 still. *"Today: a real statistical test. The thing biostatisticians do all day."*

### Block 1 — 25 min — Independent t-test with scipy
```python
from scipy import stats

# Are mean BMIs different between diabetic and non-diabetic patients?
diabetic     = pima[pima["outcome"] == 1]["bmi"]
non_diabetic = pima[pima["outcome"] == 0]["bmi"]

t_stat, p_value = stats.ttest_ind(diabetic, non_diabetic)
print(f"t = {t_stat:.3f}, p = {p_value:.5f}")
```
Discuss: p < 0.05 → reject the null (the two means probably differ). p ≥ 0.05 → can't conclude they differ. Caveat: small samples, multiple-testing problem (we'll only do a few tests today).

### 5-min Pomodoro Break
"Coffee or tea, age old debate" — fun aside about caffeine + heart rate science (medical but light).

### Block 2 — 25 min — Lab: "Which features have a real difference?"
Each student runs t-tests comparing diabetic vs non-diabetic across `glucose, bmi, age, bp, insulin`. Tabulate t and p. Then write a markdown summary: *"Of these 5 features, X showed the strongest evidence of difference between groups (p = ...)."*

### 2-min Diffuse Mode Reflection
*"You just used the same test that runs in 80% of medical research papers. What does it FEEL like to have that tool?"*

### Homework Preview
**Assignment W4 below.** Mini risk-prediction project.

---

## WEEK 4 QUIZ — Track B (10 questions)

> **Spaced repetition:** Q9 + Q10 review Week 2 (groupby + filtering).

**Easy (5)**

1. The `mean` of `[2, 4, 6, 8]` is:
   - A) 4 · B) 5 ✅ · C) 6 · D) 8

2. `df["x"].std()` returns:
   - A) Sum · B) Standard deviation ✅ · C) Median · D) Mode

3. Correlation values lie between:
   - A) 0 and 1 · B) -1 and 1 ✅ · C) -∞ and ∞ · D) 0 and 100

4. To import scipy's stats module:
   - A) `import scipy` · B) `from scipy import stats` ✅ · C) `import stats` · D) `from scipy.stats import all`

5. A p-value of 0.001 generally indicates:
   - A) No difference · B) Strong evidence the means differ ✅ · C) Always wrong · D) Sample too large

**Medium (3)**

6. `pima[["glucose","bmi"]].corr()` returns:
   - A) A 2x2 correlation matrix ✅ · B) A scatter plot · C) A list of values · D) A boolean

7. `df["x"].quantile(0.75)` is:
   - A) The 25th percentile · B) The 75th percentile (Q3) ✅ · C) The mean · D) The mode

8. An independent t-test compares:
   - A) Two paired observations · B) Two means from independent groups ✅ · C) Variance · D) Counts

**Hard (2)**

9. *(Week 2 review)* `pima.groupby("outcome")[["glucose","bmi"]].mean()` returns:
   - A) One row per `outcome` value, columns glucose/bmi means ✅ · B) The whole DataFrame · C) Counts only · D) An error

10. *(Week 2 review)* To filter PIMA for "obese diabetics":
    - A) `pima[pima.bmi > 30 and pima.outcome == 1]` (wrong because of `and`)
    - B) `pima[(pima["bmi"] > 30) & (pima["outcome"] == 1)]` ✅
    - C) `pima.filter(bmi=30, outcome=1)`
    - D) `pima[pima.obese & pima.diabetic]`

### Answer Key
1.B  2.B  3.B  4.B  5.B  6.A  7.B  8.B  9.A  10.B

---

## WEEK 4 ASSIGNMENT — Track B

**Title:** *"What Predicts Heart Disease (or Diabetes)?"*
**Due:** Mon Jul 13, 11:59 PM PST

### Instructions
Pick one dataset (Heart or PIMA). In a Colab notebook:
1. Compute the correlation matrix for all numeric columns; visualize it as a heatmap.
2. Identify the **top 3** features most correlated with the outcome variable.
3. Run an independent t-test for each of those 3 features (`outcome=1` vs `outcome=0`); report `t` and `p`.
4. Markdown summary (~6 sentences):
   - Which feature looked strongest?
   - Were any results surprising?
   - One reason this is *not* causal proof.

### Grading Criteria — $1.50 when:
- [ ] Correlation heatmap rendered with annotations (0.30)
- [ ] Top 3 features identified correctly (0.20)
- [ ] 3 t-tests run + p-values reported (0.40)
- [ ] Markdown summary present and thoughtful (0.40)
- [ ] Notebook runs end-to-end (0.20)

### Stretch
Add a *Bonferroni correction*: divide your significance threshold (0.05) by the number of tests run. Comment which features still pass.

---

## Cumulative Mind Map (Week 4)

- All previous branches stand.
- 🆕 🟪 **Statistics**:
  - Descriptive: `mean`, `median`, `std`, `quantile`
  - Correlation: Pearson vs Spearman, `df.corr()`
  - Inferential: `scipy.stats.ttest_ind`, p-values, multiple-testing caveat
  - Caveat: correlation ≠ causation

Caption: *"Next week: a 1-week intro to bioinformatics — BioPython, real DNA sequences."*
