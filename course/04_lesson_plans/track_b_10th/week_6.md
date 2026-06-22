# Track B — Week 6: "Building the Risk Scoring Tool"

**Dates:** Tue Jul 21 + Thu Jul 23, 2026 · 6:30 PM PST · Colab — full-stack notebook
**Big Picture:** *Week 6 of 7 — every skill so far, integrated. By Friday you have the prototype of the tool you'll demo at the showcase.*

---

## SESSION 1 — Tuesday, July 21, 2026

### Learning Objectives
By the end of this session, students can:
1. Take patient input via a Colab form (or `input()`).
2. Compute a multi-factor risk score with explicit, medically-justified weights.
3. Output a categorized risk level (Low/Moderate/High) with a chart.

### Active Recall (3 min)
"What's an `if/elif/else`? Where does `pima.groupby` fit? What's a t-test for? What's GC content?"

### Big Picture (1 min)
Step 6 of 7. *"All weeks integrated. Tonight you build v1 of your tool."*

### Block 1 — 25 min — Build v1 of the Risk Tool
We use the **Framingham-style cardiovascular risk** as our model — published, simple, age-appropriate. Adapted, evidence-justified weights:

```python
def heart_risk(age, bmi, sys_bp, chol, smoker):
    """
    Returns a 0-10 risk score and a risk category.
    Weights are inspired by published Framingham factors,
    simplified for educational use. NOT for clinical use.
    """
    score = 0
    score += 0 if age < 40 else 1 if age < 55 else 2 if age < 70 else 3
    score += 0 if bmi < 25 else 1 if bmi < 30 else 2
    score += 0 if sys_bp < 120 else 1 if sys_bp < 140 else 2
    score += 0 if chol < 200 else 1 if chol < 240 else 2
    score += 1 if smoker else 0
    category = "Low" if score <= 2 else "Moderate" if score <= 5 else "High"
    return score, category

print(heart_risk(58, 32, 145, 230, True))  # → (7, "High")
```

Explain each weight choice. Cite (in the markdown above the cell): *"Weights inspired by Framingham study cutoffs (NHLBI, 2008). Educational only — not for clinical decisions."*

### 5-min Pomodoro Break
"What's the BLOOD PRESSURE in the room?" — students take their pulse for 15 sec, multiply by 4. Share the number. (Fun, hands-on.)

### Block 2 — 25 min — Lab: Add Form Input + Visual Output
Each student wraps the function with:
1. Colab form widgets (the `# @param` syntax) for `age`, `bmi`, `sys_bp`, `chol`, `smoker`.
2. A horizontal bar chart showing the patient's score on a 0-10 scale colored by category.

```python
# @title Patient Risk Calculator
age    = 55       # @param {type:"slider", min:18, max:90, step:1}
bmi    = 28       # @param {type:"slider", min:15, max:50, step:0.5}
sys_bp = 130      # @param {type:"slider", min:80, max:200, step:1}
chol   = 220      # @param {type:"slider", min:120, max:400, step:1}
smoker = True     # @param {type:"boolean"}

score, cat = heart_risk(age, bmi, sys_bp, chol, smoker)
print(f"Risk score: {score}/10 → {cat}")

import matplotlib.pyplot as plt
color = {"Low":"green","Moderate":"orange","High":"red"}[cat]
plt.barh([f"Patient (age {age})"], [score], color=color)
plt.xlim(0, 10); plt.title(f"Cardiovascular Risk = {cat}"); plt.show()
```

### 2-min Diffuse Mode Reflection
*"You just built a tool a clinic could use as a screening prompt. What's the one feature you'd add next?"*

### Homework Preview
Thursday: validate against real PIMA/Heart data + add a BioPython twist for full integration.

---

## SESSION 2 — Thursday, July 23, 2026

### Stuck Check (3 min)
"Whose risk function returns weird scores? Whose Colab form is broken? Whose chart looks off?"

### Big Picture (1 min)
Step 6 still. *"Today: validate. Test on the dataset. Add the bio-data integration."*

### Block 1 — 25 min — Validation + Bio Integration
1. **Run the tool over the entire Heart dataset** and compare predicted "High risk" vs. actual `target > 0`:
   ```python
   def predict_row(row):
       smoker = False  # Heart dataset doesn't include smoking; document this
       return heart_risk(row["age"], 27, row["trestbps"], row["chol"], smoker)[1]

   df["predicted"] = df.apply(predict_row, axis=1)
   pd.crosstab(df["predicted"], df["target"] > 0)
   ```
   Discuss confusion-matrix-style results. Honest acknowledgment: this is a teaching prototype.
2. **BioPython tie-in:** add a "genetic risk flag" to the tool — if a user uploads a tiny FASTA, count occurrences of a known SNP-related motif (e.g., a synthetic example) and add 1 to the risk score:
   ```python
   def genetic_modifier(fasta_path):
       record = next(SeqIO.parse(fasta_path, "fasta"))
       motif_count = str(record.seq).count("CAGCTG")  # E-box, common regulatory motif
       return 1 if motif_count > 5 else 0
   ```

### 5-min Pomodoro Break
"Stand up + 10 squats." (We just spent a long time talking about cardiovascular risk; let's earn some Z's.)

### Block 2 — 25 min — Lab: Tool v2
Each student integrates the validation + BioPython modifier into their notebook. Documents in markdown: limitations, what they'd improve, who would use this, and what would be needed before it could be clinically deployed (regulatory, validation, ethics).

### 2-min Diffuse Mode Reflection
*"You wrote a *limitations* section for your own work. What did writing it teach you about science?"*

### Homework Preview
**Assignment W6 below.** Lock for the showcase next week.

---

## WEEK 6 QUIZ — Track B (10 questions)

> **Spaced repetition:** Q9 reviews W4 (statistics). Q10 reviews W4 (correlation).

**Easy (5)**

1. A function that returns multiple values uses:
   - A) `return a, b` (a tuple) · B) `return [a]; return [b]` · C) `return a or b` · D) Two `return` statements run at once

2. Colab `# @param` lines create:
   - A) Documentation only · B) Interactive form widgets · C) Errors · D) Code cells

3. To convert a smoker boolean to 0/1:
   - A) `int(smoker)` · B) `smoker.toInt()` · C) `(smoker)` · D) `bool(smoker)`

4. `pd.crosstab(a, b)` produces:
   - A) A correlation · B) A contingency table of `a` vs `b` · C) A scatter · D) A heatmap

5. A "limitations" section in a tool document is:
   - A) Optional fluff · B) An honest description of what your tool can't do, mandatory for clinical work · C) Code · D) The bibliography

**Medium (3)**

6. Which line is a defensive default for a missing field?
   - A) `smoker = smoker or False` · B) `smoker == False` · C) `smoker := False` · D) `default smoker`

7. A confusion-matrix-style 2x2 table shows:
   - A) Predicted vs actual class counts · B) Just true positives · C) The mean of predictions · D) Random samples

8. Risk weights "inspired by Framingham" must:
   - A) Be perfect for clinical use · B) Be cited and labeled as educational, not clinical · C) Be hidden · D) Use machine learning

**Hard (2)**

9. *(Week 4 review)* If a t-test returns `p = 0.0001`, the correct interpretation is:
   - A) The means are exactly equal · B) Strong statistical evidence the means differ · C) Sample is too small · D) Always reject

10. *(Week 4 review)* `df.corr()` defaults to which correlation?
    - A) Spearman · B) Pearson · C) Kendall · D) Pointbiserial

### Answer Key
1.A  2.B  3.A  4.B  5.B  6.A  7.A  8.B  9.B  10.B

---

## WEEK 6 ASSIGNMENT — Track B

**Title:** *"Patient Risk Tool — Working Prototype"*
**Due:** Mon Jul 27, 11:59 PM PST

### Instructions
Build a single Colab notebook that:
1. Loads either the Heart or PIMA dataset.
2. Defines a `risk(...)` function with at least **5 inputs** and **clear weights** (cite your reasoning in markdown).
3. Provides interactive Colab form widgets for input.
4. Returns a numeric score AND a category (Low/Moderate/High or comparable).
5. Displays a horizontal bar chart of the patient's score, color-coded by category.
6. Validates on the dataset (predict label, compare to actual outcome via crosstab).
7. Includes a `## Limitations` section in markdown — at least 4 honest bullets.

### Grading Criteria — $1.50 when:
- [ ] Risk function with 5+ inputs and explained weights (0.40)
- [ ] Form input + chart output present (0.30)
- [ ] Validation against real dataset (0.30)
- [ ] Limitations section honest + thoughtful (0.30)
- [ ] Notebook runs end-to-end (0.20)

### Stretch
Add a BioPython "genetic modifier" hook (uses a FASTA upload to bump the score by 1). Add a 2nd chart comparing the patient to dataset distribution.

---

## Cumulative Mind Map (Week 6)

All branches integrated:
- Python core · Pandas · Filtering · Aggregation · Imputation
- Visualization (matplotlib + seaborn)
- Statistics (descriptive, correlation, t-test)
- BioPython (Seq, SeqIO, GC, motifs)
- 🆕 🧰 **Risk Tool**: combine all above with a function + form + chart + validation + honest limitations

Caption: *"Next week: SHOWCASE. You demo the tool to the cohort."*
