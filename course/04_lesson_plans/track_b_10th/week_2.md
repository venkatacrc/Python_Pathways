# Track B — Week 2: "Exploring Patient Data with pandas"

**Dates:** Tue Jun 23 + Thu Jun 25, 2026 · 6:30 PM PST · Google Colab + pandas
**Big Picture:** *Week 2 of 7 — last week we LOADED data. This week we GROW with it: groupby, multi-condition cohorts, derived columns. By Friday you can build cohorts a clinical researcher would recognize.*

---

## SESSION 1 — Tuesday, June 23, 2026

### Learning Objectives
By the end of this session, students can:
1. Build complex cohorts using multi-condition boolean masks.
2. Group patients by a category and aggregate (`groupby`, `mean`, `count`).
3. Add derived columns (e.g., BMI category, hypertension flag).

### Active Recall (3 min)
"What does `df.head()` show? How do you filter for `age > 50`? What's `na_values='?'`?"

### Big Picture (1 min)
Step 2 of 7. *"You're now doing what an MD-PhD student does in week one of a research lab."*

### Block 1 — 25 min — Live notebook
1. **Multi-condition cohorts:**
   ```python
   # Add the PIMA Diabetes dataset for variety
   url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
   pcols = ["pregnancies","glucose","bp","skinfold","insulin","bmi","dpf","age","outcome"]
   pima = pd.read_csv(url, names=pcols)
   high_risk = pima[(pima["glucose"] > 140) & (pima["bmi"] > 30) & (pima["age"] > 45)]
   print("High-risk cohort:", len(high_risk))
   ```
2. **`groupby` aggregation:**
   ```python
   pima.groupby("outcome")[["glucose", "bp", "bmi"]].mean()
   pima.groupby("age")["outcome"].mean()  # diabetes rate by age
   ```
3. **Derived columns:**
   ```python
   def bmi_category(b):
       if b < 18.5:  return "underweight"
       elif b < 25:  return "normal"
       elif b < 30:  return "overweight"
       else:         return "obese"
   pima["bmi_cat"] = pima["bmi"].apply(bmi_category)
   pima["bmi_cat"].value_counts()
   ```

### 5-min Pomodoro Break
Look out a window. Talk to a person nearby for 60 seconds about anything *not* class-related.

### Block 2 — 25 min — Lab: Cohort Builder
Each student builds 3 cohorts in their notebook and prints summary stats:
- *Young diabetics:* `age < 35 & outcome == 1`
- *Old non-diabetics with high BMI:* `age > 55 & outcome == 0 & bmi > 30`
- *Their own clinical question.*

### 2-min Diffuse Mode Reflection
*"Which of your 3 cohorts surprised you most? Why?"*

### Homework Preview
Thursday: missing data + categorical encoding.

---

## SESSION 2 — Thursday, June 25, 2026

### Stuck Check Opener (3 min)
"Whose `groupby` results don't make sense? Whose `apply()` errors out?"

### Big Picture (1 min)
Step 2 still. *"Today: data is messy. We clean it like clinicians clean labs."*

### Block 1 — 25 min — Missing & Categorical Data
1. **Why PIMA's `0`s are actually missing:**
   ```python
   # In PIMA, glucose=0 or bp=0 are sensor errors / missing markers
   for col in ["glucose","bp","skinfold","insulin","bmi"]:
       pima[col] = pima[col].replace(0, pd.NA)
   pima.isna().sum()
   ```
2. **Imputation:**
   ```python
   pima["glucose"] = pima["glucose"].fillna(pima["glucose"].median())
   pima["bp"]      = pima["bp"].fillna(pima["bp"].median())
   ```
   Discuss: why median over mean? (Robust to outliers — a real clinical reason.)
3. **Categorical encoding (preview):**
   ```python
   pima["risk_flag"] = (pima["glucose"] > 140).astype(int)
   ```

### 5-min Pomodoro Break
Stretch shoulders. Take 5 deep breaths through the nose.

### Block 2 — 25 min — Lab: "Build a Risk Flag"
Each student adds a derived column to PIMA:
```python
def composite_risk(row):
    score = 0
    if row["glucose"] > 140: score += 1
    if row["bmi"]      > 30: score += 1
    if row["age"]      > 50: score += 1
    if row["bp"]       > 90: score += 1
    return score

pima["risk_score_v0"] = pima.apply(composite_risk, axis=1)
pima.groupby("risk_score_v0")["outcome"].mean()
```
Discuss: *does our flag actually correlate with diabetes outcome?* This previews Week 6 (the real risk tool).

### 2-min Diffuse Mode Reflection
*"You just built the FIRST DRAFT of a clinical risk score. What's missing to make it useful for a real doctor?"*

### Homework Preview
**Assignment W2 below.** Due Mon Jun 29, 11:59 PM PST.

---

## WEEK 2 QUIZ — Track B (10 questions, 15 min)

> **Spaced repetition:** Q9 + Q10 review Week 1 (DataFrame basics).

**Easy (5)**

1. `df.groupby("outcome")["bmi"].mean()` returns:
   - A) Each row's mean · B) Mean BMI for each value of `outcome` ✅ · C) Total BMI · D) Error

2. `df["age"].apply(lambda x: x * 12)` does what?
   - A) Multiplies the column by 12 elementwise ✅ · B) Adds 12 · C) Filters · D) Errors

3. To replace zeros with NaN:
   - A) `df["bp"].drop(0)` · B) `df["bp"].replace(0, pd.NA)` ✅ · C) `df["bp"] = None if 0` · D) `df.fillna(0)`

4. Median is preferred over mean for imputation when:
   - A) The data are perfectly normal · B) There are outliers ✅ · C) Always · D) Never

5. To add a derived column:
   - A) `df["new"] = df["a"] + df["b"]` ✅ · B) `df.add("new", df.a + df.b)` · C) `df.append(...)` · D) `df.col("new")`

**Medium (3)**

6. `pima[(pima["age"] > 50) & (pima["bmi"] > 30)]` — the `&` instead of `and` is required because:
   - A) Pandas syntax · B) `and` doesn't work elementwise on Series ✅ · C) `&` is faster · D) `and` errors silently

7. `df.apply(fn, axis=1)` applies `fn` to:
   - A) Each column · B) Each row ✅ · C) Each cell · D) Random samples

8. Why might a 0 in PIMA's `bp` column be wrong?
   - A) Resting blood pressure of 0 is impossible (the patient would be dead) ✅
   - B) `bp` shouldn't be in the dataset · C) Encoding artifact only · D) Both A and: yes, but A is the medical reason — go with A

**Hard (2)**

9. *(Week 1 review)* What does `df["age"].mean()` return?
   - A) The DataFrame · B) A single number — the average age ✅ · C) A list · D) A new column

10. *(Week 1 review)* `df["target"].value_counts()` returns:
    - A) The number of unique values for each entry of `target` ✅ · B) The mean of `target` · C) Each row's count · D) Errors

### Answer Key
1.B  2.A  3.B  4.B  5.A  6.B  7.B  8.A  9.B  10.A

---

## WEEK 2 ASSIGNMENT — Track B

**Title:** *"Cohort Comparison Notebook"*
**Due:** Mon Jun 29, 11:59 PM PST

### Instructions
In a new Colab notebook:
1. Load the PIMA Diabetes dataset.
2. Treat `0` in `glucose, bp, bmi, insulin, skinfold` as missing → replace with NaN → impute with column median.
3. Add a derived column `bmi_cat` ("underweight"/"normal"/"overweight"/"obese").
4. Build **3 cohorts** of your choice (e.g., obese diabetics, lean non-diabetics over 50, etc.) and print their `.describe()` for at least 2 numeric columns.
5. Use `groupby("bmi_cat")["outcome"].mean()` to show the diabetes rate per BMI category.
6. Markdown summary at the end: 3-4 sentences on what you found.

### Grading Criteria — $1.50 when:
- [ ] Notebook runs end-to-end (0.30)
- [ ] Missing data correctly handled with median imputation (0.30)
- [ ] `bmi_cat` derived column present (0.20)
- [ ] 3 cohorts defined with multi-condition filters (0.40)
- [ ] `groupby` aggregation included (0.20)
- [ ] Markdown summary makes a real observation (0.10)

### Stretch
Plot diabetes rate by `bmi_cat` as a bar chart (preview of Week 3).

---

## Cumulative Mind Map (Week 2)

- 🟢 Python core (W1) · 🟦 Tools/Colab (W1) · 🟡 Pandas Step 1 (W1) · 🔵 Filtering (W1) · 🟠 Data hygiene (W1)
- 🆕 🟣 **Cohorts**: multi-condition masks, `&` vs `|`
- 🆕 🔴 **Aggregation**: `groupby` → `mean`, `count`, `value_counts`
- 🆕 🟤 **Derived columns**: `apply`, `lambda`, custom functions
- 🆕 ⚫ **Imputation**: medical-grade missing-value handling

Caption: *"Next week: this data needs PICTURES. Welcome to matplotlib."*
