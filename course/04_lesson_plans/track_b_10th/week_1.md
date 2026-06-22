# Track B — Week 1: "Python for Science"

**Dates:** Tue Jun 16 + Thu Jun 18, 2026 · 6:30 PM PST · Google Colab
**Big Picture:** *Week 1 of 7 — today you set up your scientific Python notebook and load real patient data for the first time. By the end of the week, the data is talking back.*

---

## SESSION 1 — Tuesday, June 16, 2026

### Learning Objectives
By the end of this session, students can:
1. Open Colab, create a notebook, run a code cell, and add markdown.
2. Use Python's basic data types (`int`, `float`, `str`, `bool`, `list`) and control flow.
3. Load a CSV of patient data with `pandas` and view the first 5 rows.

### Active Recall Opener
*Skipped — first session.* Instead: 3-min round of "What's a clinical question you'd love to answer if you had a database of 1 million patients?"

### Big Picture (1 min)
Show the 7-week ladder: today = data + Python. Week 7 = a working risk-scoring tool you demo. *"Every step, you're closer to a tool a doctor might actually use."*

### Block 1 — 25 min (Instructor-led)
1. **Colab orientation (5 min):** create a new notebook in `colab.research.google.com`. Show: code cells (`Shift+Enter` to run), markdown cells, the file pane, mounting Google Drive.
2. **Python crash course (15 min):** types, list slicing, `if/else`, `for`, `def`. Single live-coded cell:
   ```python
   patient = {"name": "P001", "age": 54, "bp_sys": 142, "smoker": True, "labs": [98.2, 7.1, 188]}
   if patient["age"] > 50 and patient["bp_sys"] > 140:
       print(f"{patient['name']}: stage-2 hypertension at age {patient['age']}")
   for lab_value in patient["labs"]:
       print("Lab:", lab_value)
   ```
3. **First DataFrame (5 min):**
   ```python
   import pandas as pd
   url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
   cols = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target"]
   df = pd.read_csv(url, names=cols, na_values="?")
   df.head()
   ```
   *(UCI Cleveland Heart Disease — 303 anonymized patients.)*

### 5-min Pomodoro Break
Stand up. Stretch. Drink water. Look out a window for 30 sec (the eye doctors will thank you).

### Block 2 — 25 min (Students try)
Each student opens the same dataset and answers, in code:
1. How many patients are in the dataset? `len(df)`
2. What's the average age? `df["age"].mean()`
3. How many smokers (`fbs == 1` is fasting blood sugar > 120, *not* a smoking field — instructor clarifies; use `df["chol"].max()` instead): max cholesterol in the dataset.
4. What does `df.dtypes` tell you? Why are some columns floats?

### 2-min Diffuse Mode Reflection
Course-site journal (Track B Discussion): *"This dataset is real. 303 real (de-identified) patients. What's a question you wish you could ask all 303 of them?"*

### Homework Preview
Thursday: more pandas. Try `df.describe()` on your own before then.

---

## SESSION 2 — Thursday, June 18, 2026

### Stuck Check Opener (3 min)
"Where did Tuesday lose you? Errors, syntax, conceptual?" — capture for the live agenda.

### Big Picture (1 min)
Step 1 of 7. *"Tuesday: load data. Today: ASK QUESTIONS of it."*

### Block 1 — 25 min (Live coding, instructor + students)
1. **`describe()`, `info()`, `value_counts()`:**
   ```python
   df.describe()
   df["target"].value_counts()    # how many had heart disease
   df["sex"].value_counts()       # 1=male, 0=female
   ```
2. **Filtering with boolean masks:**
   ```python
   over_60 = df[df["age"] > 60]
   high_chol = df[df["chol"] > 280]
   over_60_high_chol = df[(df["age"] > 60) & (df["chol"] > 280)]
   print(len(over_60_high_chol), "patients over 60 with high cholesterol")
   ```
3. **Missing data:**
   ```python
   df.isna().sum()                # how many NaN per column
   df = df.dropna()               # drop rows with any missing value
   ```

### 5-min Pomodoro Break
Eye-rest exercise: focus on something 20 feet away for 20 seconds (20-20-20 rule from optometry — a real medicine break).

### Block 2 — 25 min — Lab: "Find Your Cohort"
Each student picks a clinical question and writes 2 lines of code to answer it:
- *"All male patients with chest pain type 4 and resting BP > 150."*
- *"Average heart rate of patients diagnosed with disease vs. not."*
- *"Youngest patient in the dataset who has any sign of disease."*

Each shares their question and answer in the Forum with the `#share` tag.

### 2-min Diffuse Mode Reflection
*"You just queried a real medical dataset. Could a doctor doing rounds use this? What would they need that you don't have yet?"*

### Homework Preview
**Assignment W1 below.** Due Mon Jun 22, 11:59 PM PST.

---

## WEEK 1 QUIZ — Track B (10 questions, 15 min, closed-notes)

> **Spaced repetition:** none yet (first week). All 10 are current-week.

**Easy (5)**

1. To open the first 5 rows of a DataFrame, you call:
   - A) `df.first(5)` · B) `df.head()` · C) `df.start()` · D) `df.preview()`

2. Which library is standard for tabular data in Python?
   - A) `numpy` · B) `pandas` · C) `csvio` · D) `matplotlib`

3. In `df["age"]`, the `["age"]` is:
   - A) A function call · B) Column selection by name · C) An import · D) A loop

4. To run a cell in Colab:
   - A) `Ctrl+S` · B) `Shift+Enter` · C) Right-click → Run · D) Click anywhere

5. Which is a **boolean** value in Python?
   - A) `"True"` · B) `True` · C) `1` · D) `0.0`

**Medium (3)**

6. What does `df.describe()` return?
   - A) Just the means · B) Summary stats (count, mean, std, min, quartiles, max) for numeric columns · C) The schema · D) The first 100 rows

7. To filter for patients aged 50–60 (inclusive):
   - A) `df[df.age >= 50 and df.age <= 60]` (wrong — `and` doesn't work elementwise in pandas)
   - B) `df[(df["age"] >= 50) & (df["age"] <= 60)]`   - C) `df[df.age in range(50, 60)]`
   - D) `df.filter(age=50..60)`

8. `df.isna().sum()` tells you:
   - A) The total of all numeric columns · B) The number of missing values per column · C) The dtype of each column · D) The mean of each column

**Hard (2)**

9. The Cleveland heart-disease dataset uses `?` for missing values. The right `read_csv` argument is:
   - A) `header="?"` · B) `na_values="?"` · C) `missing="?"` · D) `replace="?"`

10. After `df = df.dropna()`, the original DataFrame:
    - A) Is also modified in place · B) Is unchanged because `dropna()` returns a new DataFrame · C) Is deleted · D) Is None

### Answer Key
1.B  2.B  3.B  4.B  5.B  6.B  7.B  8.B  9.B  10.B

---

## WEEK 1 ASSIGNMENT — Track B

**Title:** *"First Patient-Data Notebook"*
**Due:** Mon Jun 22, 11:59 PM PST · 45–60 min · Submit a Colab notebook share-link via the [Assignment Google Form](https://forms.gle/REPLACE_WITH_REAL_FORM)

### Instructions
Create a Colab notebook titled `[YourName]_Week1_Heart.ipynb` containing:
1. A markdown title and a 2-sentence description of the dataset (UCI Cleveland Heart Disease).
2. Loading the CSV with `na_values="?"`.
3. Print: number of patients, columns list, `df.describe()` output.
4. Filter patients with `age >= 60` AND `chol >= 240` (clinical cutoff for high cholesterol). Print the count and the first 10 rows.
5. Compute and print: average resting BP (`trestbps`) of the filtered cohort vs. all patients.
6. A markdown cell at the bottom: 2-3 sentences describing **one observation** you find interesting.

### Starter Code (linked from this page as a Colab template)
```python
import pandas as pd
URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
cols = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target"]
df = pd.read_csv(URL, names=cols, na_values="?")
df = df.dropna()
print("Total patients:", len(df))
df.describe()
```

### Grading Criteria — full $1.50 when:
- [ ] Notebook runs from top to bottom without errors (0.40)
- [ ] Markdown title + description present (0.20)
- [ ] Filter condition correct (0.30)
- [ ] At least one comparison (filtered vs. all) computed (0.30)
- [ ] One thoughtful observation in markdown (0.30)

### Stretch (no $$)
Create a second filter: female (`sex == 0`) patients with `target > 0` (any disease). Compare their `thalach` (max heart rate achieved) distribution to males with disease. One markdown sentence on what you see.

---

## Cumulative Mind Map (Week 1)

Center: **MEDICAL PYTHON**.
- 🟢 **Python core**: types · variables · `if/else` · `for` · `def`
- 🟦 **Tools**: Colab · code cells · markdown · `pip` (preview)
- 🟡 **Pandas Step 1**: `read_csv` · `head` · `describe` · `info`
- 🔵 **Filtering**: `df[df.col > x]` · `&` and `|` · boolean masks
- 🟠 **Data hygiene**: `na_values` · `isna` · `dropna`

Caption: *"Next week: cohorts, slicing, the real shape of clinical data."*
