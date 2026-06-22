# Track B — Week 3: "Seeing the Data — Visualization"

**Dates:** Tue Jun 30 + Thu Jul 2, 2026 · 6:30 PM PST · Colab + matplotlib + seaborn
**Big Picture:** *Week 3 of 7 — pictures of data are how clinicians spot patterns. By Friday, you can produce a chart any med-school stats class would accept.*
**⚠️ Heads up:** Tuesday Jun 30 is normal. Thursday Jul 2 is the at-risk session before July 4th weekend (some families will travel). **Async option below.**

---

## SESSION 1 — Tuesday, June 30, 2026

### Learning Objectives
By the end of this session, students can:
1. Plot histograms, scatter plots, and bar charts from a DataFrame.
2. Use `seaborn` for clean medical-style visuals.
3. Add titles, axis labels, and clinical context to a plot.

### Active Recall (3 min)
"What's `groupby`? How do you make a derived column? Why use median over mean for imputation?"

### Big Picture (1 min)
Step 3 of 7. *"You can query data. Today: you can SHOW data. Charts are how science persuades."*

### Block 1 — 25 min
1. **matplotlib basics:**
   ```python
   import matplotlib.pyplot as plt
   plt.hist(pima["age"], bins=20)
   plt.title("Age distribution — PIMA cohort")
   plt.xlabel("Age (years)"); plt.ylabel("Count")
   plt.show()
   ```
2. **Comparing distributions overlay:**
   ```python
   plt.hist(pima[pima["outcome"]==0]["glucose"], alpha=0.5, label="No diabetes", bins=20)
   plt.hist(pima[pima["outcome"]==1]["glucose"], alpha=0.5, label="Diabetes",    bins=20)
   plt.title("Glucose levels by diabetes outcome")
   plt.xlabel("Glucose"); plt.ylabel("Count")
   plt.legend(); plt.show()
   ```
3. **Scatter plot:**
   ```python
   plt.scatter(pima["bmi"], pima["glucose"], c=pima["outcome"], alpha=0.5, cmap="coolwarm")
   plt.xlabel("BMI"); plt.ylabel("Glucose")
   plt.title("BMI vs Glucose, colored by diabetes outcome")
   plt.colorbar(label="Outcome (0=no, 1=yes)"); plt.show()
   ```

### 5-min Pomodoro Break
20-20-20 eye rule again. Stretch wrists.

### Block 2 — 25 min — Lab: 3 charts
Each student produces:
- 1 histogram of any column they pick (with title + labels)
- 1 scatter plot of any 2 columns colored by outcome
- 1 bar chart from `groupby` (e.g., diabetes rate by BMI category)

### 2-min Diffuse Mode Reflection
*"Pick the most interesting chart you made today. What does a clinician seeing it for the first time learn?"*

### Homework Preview
Thursday: **seaborn** for the clean look + box-plots + correlation heatmaps.

---

## SESSION 2 — Thursday, July 2, 2026  *(at-risk session — async option below)*

### Stuck Check (3 min)
"Whose chart looks ugly? Whose has no labels? Whose color got applied to the wrong axis?"

### Big Picture (1 min)
Step 3 still. *"matplotlib gives you control. seaborn makes it pretty for free."*

### Block 1 — 25 min — seaborn + Box Plots + Heatmap
```python
import seaborn as sns
sns.set_theme(style="whitegrid")

# Box plot — distributions of glucose by outcome
sns.boxplot(data=pima, x="outcome", y="glucose")
plt.title("Glucose by diabetes outcome"); plt.show()

# Pair plot
sns.pairplot(pima[["glucose","bmi","age","bp","outcome"]], hue="outcome", diag_kind="hist")

# Correlation heatmap
corr = pima.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation matrix — PIMA features"); plt.show()
```

### 5-min Pomodoro Break
"Best chart from Tuesday" — each student drops a screenshot in chat. Vote.

### Block 2 — 25 min — Lab: Clinical Story-Telling
Each student picks ONE finding and produces a polished chart with:
- A title that states a CLAIM (e.g., "BMI > 35 strongly predicts diabetes in this cohort")
- Properly labeled axes (with units)
- A caption (markdown below the chart) explaining what a clinician should notice

### 2-min Diffuse Mode Reflection
*"You just made a chart that could go in a medical poster. What's the next chart you wish you could make?"*

### Homework Preview
**Assignment W3.** Due Mon Jul 6, 11:59 PM PST.

---

### 🇺🇸 ASYNC ALTERNATIVE for Thursday Jul 2 (July 4 weekend make-up)

If you can't attend Thursday's live session because of the holiday weekend, here is your full make-up — **same content, ~75 min, same earning potential**:

1. **Watch:** the Tuesday Jun 30 recording (link on this week's course-site page; skim sections you've already done).
2. **Read** the course-site page **"Seaborn Quickstart for Clinical Data"** (an annotated notebook with each chart type explained in plain English).
3. **Code:** in Colab, reproduce the box plot, pair plot, and heatmap above on the PIMA dataset.
4. **Apply:** make the same "clinical story-telling" chart described in Block 2 — pick one finding, write a claim title, polish the axes, write a 2-sentence caption in markdown.
5. **Post in `[B] Track B Forum`:** screenshot your final chart with the `#share` tag and a one-line claim.
6. **Stuck Check:** post any errors or confusion with `#stuck`. Instructor responds within 24 hrs.

You will receive full attendance + assignment credit on completion.

---

## WEEK 3 QUIZ — Track B (10 questions, 15 min)

> **Spaced repetition:** Q9 + Q10 review Week 1 (Pandas basics).

**Easy (5)**

1. To make a histogram in matplotlib:
   - A) `plt.histogram(...)` · B) `plt.hist(...)` · C) `plt.bar(...)` · D) `plt.plot(...)`

2. `plt.show()` does:
   - A) Saves the figure · B) Displays the chart in the notebook · C) Closes the chart · D) Prints the data

3. seaborn is built on top of:
   - A) numpy · B) matplotlib · C) pandas · D) scipy

4. To add a chart title in matplotlib:
   - A) `plt.label(...)` · B) `plt.title(...)` · C) `plt.heading(...)` · D) `plt.set_title(...)`

5. A correlation heatmap shows:
   - A) Heat over time · B) Pairwise correlation between numeric columns · C) The first 5 rows · D) Missing data only

**Medium (3)**

6. `sns.boxplot(data=df, x="outcome", y="glucose")` shows:
   - A) Bar chart of outcomes · B) Glucose distribution stratified by outcome (median, IQR, outliers) · C) Histogram · D) Scatter

7. To overlay two histograms with transparency:
   - A) `alpha=0.5` · B) `transparent=True` · C) `overlay=True` · D) `alpha="0.5"`

8. The `hue` argument in seaborn:
   - A) Sets the title color · B) Splits the plot by a categorical column · C) Sets the y-axis · D) Removes labels

**Hard (2)**

9. *(Week 1 review)* `df.dropna()` returns:
   - A) The DataFrame in place · B) A new DataFrame with rows containing NaN dropped · C) The list of NaN locations · D) An error

10. *(Week 1 review)* In `pd.read_csv(url, names=[...], na_values="?")`:
    - A) `names` sets column names because the file has no header    - B) `names` is the list of users who can read it
    - C) `na_values` adds NaN
    - D) Both A and: yes, A is the answer

### Answer Key
1.B  2.B  3.B  4.B  5.B  6.B  7.A  8.B  9.B  10.A

---

## WEEK 3 ASSIGNMENT — Track B

**Title:** *"Three-Chart Clinical Story"*
**Due:** Mon Jul 6, 11:59 PM PST

### Instructions
Choose either the Heart Disease or PIMA dataset. Produce **3 charts** that tell a clinical story:
1. A **distribution chart** (histogram or boxplot) for one risk factor.
2. A **comparison chart** (overlay or grouped bar) showing how the risk factor differs by outcome.
3. A **multi-variable chart** (scatter colored by outcome, OR correlation heatmap, OR seaborn pairplot).
Each chart has:
- A title that states a clinical claim, not just "Histogram of X."
- Axis labels with units.
- A 2-3 sentence markdown caption beneath, explaining what a clinician should notice.

### Grading Criteria — $1.50 when:
- [ ] All 3 chart types present (0.50)
- [ ] All charts have titles + labeled axes + units (0.30)
- [ ] Each chart has a 2-3 sentence clinical interpretation (0.40)
- [ ] Notebook runs end-to-end (0.20)
- [ ] At least 1 chart uses seaborn (0.10)

### Stretch
Add a 4th chart using `sns.violinplot` or `sns.swarmplot` and explain why you chose it.

---

## Cumulative Mind Map (Week 3)

- W1 + W2 branches stand (Python core, Pandas, Cohorts, Aggregation, Imputation).
- 🆕 ⚪ **Visualization**:
  - matplotlib: `plt.hist`, `plt.scatter`, `plt.bar`, titles + labels
  - seaborn: `sns.boxplot`, `sns.pairplot`, `sns.heatmap`, `hue=...`
  - Storytelling: claim-titles, axis units, captions

Caption: *"Next week: numbers behind the pictures. Statistics."*
