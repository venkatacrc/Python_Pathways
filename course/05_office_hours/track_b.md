# ARTIFACT 5 — Office Hours Agendas: Track B (10th Graders)

**Format:** 60 minutes weekly, on Zoom, recorded.
**Suggested time slot:** Saturday 11:30 AM – 12:30 PM PST (post-Track A; lets students sleep in but still hit lunch).
**Tone:** rigorous-but-warm. Treat them as young scientists. Connect to medicine wherever possible.

---

## Week 1 — Sat Jun 20, 2026

**0–10 — Open Q&A (Assignment: First Patient-Data Notebook)**
- "Colab keeps disconnecting." | "What's a `na_values`?" | "How do I share my notebook?"

**10–30 — Top 3 Confusion Points**
1. **Colab session timeouts** — code state lost after ~90 min idle. Show how to "Run all" to rebuild quickly; mounting Drive for persistent files.
2. **`df["x"]` vs `df[["x"]]`** — single brackets return a Series, double brackets a DataFrame. Demo the type difference.
3. **Sharing notebook permissions** — must set "Anyone with link can view" before pasting into the assignment Google Form.

**30–50 — "Go Further" Demo**
Compute prevalence of heart disease in the Cleveland dataset, both overall and by sex. Compare to the published 1988 prevalence numbers (instructor projects the original UCI paper's table).

**50–60 — Preview Week 2 + Motivational**
*"Next week: cohorts and groupby — the same lens a clinical research lab uses on day one."* End: *"You ran your first medical-data analysis tonight. That's a step a 1st-year MD-PhD student takes."*

---

## Week 2 — Sat Jun 27, 2026

**0–10 — Open Q&A (Cohort Comparison Notebook)**
- "Why doesn't `and` work in pandas?" | "Imputed columns broke my charts." | "groupby returns a weird object."

**10–30 — Top 3 Confusion Points**
1. **`&` vs `and`** — pandas operates elementwise on Series; bitwise `&` is required + parentheses around each comparison.
2. **`SettingWithCopyWarning`** — `df[df.x>0]["y"] = ...` warning. Show the `.loc[...]` fix.
3. **Median imputation can hide signal.** Briefly discuss "missingness as a feature" — sometimes a 0 is informative; conservative approach: impute + add a binary `was_missing` flag column.

**30–50 — "Go Further"**
Build a `BMI vs glucose` lattice plot using `sns.FacetGrid` split by age decade.

**50–60 — Preview Week 3 + Motivational**
*"Next week: VISUALIZATION. Charts are how science persuades. Your first publication-style plot."* End: *"Today you built cohorts. Real epidemiologists do this exact step every week."*

---

## Week 3 — Sat Jul 5, 2026 *(post-July-4 weekend; expect attendance dip; async students prioritized)*

**0–10 — Open Q&A (Three-Chart Clinical Story)**
- "Why is my axis label tiny?" | "How do I save a figure?" | "Async catch-up — show me what I missed."

**10–30 — Top 3 Confusion Points**
1. **Forgot `plt.show()` (or it's called twice and overlaps charts).** Live demo, fix.
2. **Color/legend mismatches.** When using `c=column` in `plt.scatter`, the colorbar shows continuous; use seaborn `hue=` for categorical.
3. **Axis labels missing units.** Real-clinical-quality charts ALWAYS state units. Show the `xlabel="Glucose (mg/dL)"` polish.

**30–50 — "Go Further"**
Save a chart at 300 dpi as PNG with `plt.savefig("fig.png", dpi=300, bbox_inches="tight")` — demo "publication-ready."

**50–60 — Preview Week 4 + Motivational**
*"Next week: STATISTICS. The math behind every medical paper. We'll run our first t-test."* End: *"Your chart this week could go in a med-school poster."*

---

## Week 4 — Sat Jul 11, 2026

**0–10 — Open Q&A ("What Predicts Heart Disease?")**
- "What's a p-value REALLY?" | "Pearson vs Spearman vs Kendall?" | "Why is my correlation 0.0001 — that can't be right?"

**10–30 — Top 3 Confusion Points**
1. **What p-value means (and doesn't).** It is *not* P(null is true). It is P(data this extreme | null is true). Walk this carefully.
2. **Multiple testing.** Run 20 tests with α=0.05 → expect ≈1 false positive. Show Bonferroni.
3. **Correlation ≠ causation.** Chocolate consumption vs Nobel laureates per capita (the famous spurious example).

**30–50 — "Go Further"**
Demo logistic regression with `sklearn.linear_model.LogisticRegression` (just to *show* what's coming, no need to grade) — predict outcome, get coefficients, compare to correlation rankings.

**50–60 — Preview Week 5 + Motivational**
*"Next week: DNA. We meet BioPython."* End: *"Today's t-test is the same one in 80% of medical papers. You're now able to read those papers' Methods sections critically."*

---

## Week 5 — Sat Jul 18, 2026

**0–10 — Open Q&A (BRCA1 Mini Sequence Report)**
- "Where do I find FASTA files?" | "GC content felt arbitrary — what's biological about it?" | "Translate threw a `Bio.Data.CodonTable` warning."

**10–30 — Top 3 Confusion Points**
1. **FASTA format basics.** First line `>id description` then sequence wrapped at 60-80 chars per line. Show how `SeqIO.parse` lazily yields records.
2. **GC content's biological meaning.** GC bonds = 3 H-bonds (vs AT's 2) → higher GC ⇒ more thermally stable DNA → reflects evolutionary pressure. Brief 2-min explainer.
3. **Stop codons + translate('to_stop=True').** Why `to_stop` matters when the sequence isn't a complete ORF.

**30–50 — "Go Further"**
Show NCBI's BLAST web tool — paste a 60-bp piece of BRCA1 → see the top hits across species. Real bioinformatics in 60 seconds.

**50–60 — Preview Week 6 + Motivational**
*"Next week: bring it ALL together — patient risk tool, real prototype."* End: *"Today you read actual genes from actual humans. That's not a metaphor."*

---

## Week 6 — Sat Jul 25, 2026

**0–10 — Open Q&A (Patient Risk Tool — Working Prototype)**
- "Are these weights medically right?" | "How do I justify thresholds?" | "Colab forms aren't showing widgets."

**10–30 — Top 3 Confusion Points**
1. **Medical justification of thresholds.** Show the **JNC 8** hypertension guidelines page; show **NCEP/ATP III** cholesterol cutoffs. Tell them: *"This is what evidence-based medicine LOOKS LIKE."*
2. **Colab `# @param` syntax must be exactly right.** Live walkthrough; show the cell behavior toggling.
3. **Validation honesty.** Their tool will not perform like a real model — that's fine. Lean into "this is a teaching prototype" framing.

**30–50 — "Go Further"**
Quick demo of `sklearn.metrics.roc_auc_score` and `confusion_matrix` to show how real model evaluation works (they don't need to use it, just see it).

**50–60 — Preview Week 7 + Motivational**
*"Showcase week. You'll demo to the class. Bring your tool, your dataset, your honest limitations slide."* End: *"You built a clinical decision-support prototype. That's a real engineering artifact."*

---

## Week 7 — Sat Aug 1, 2026 — *Capstone reflection + futures*

**0–10 — Open Q&A**
*"Final demo nerves? Last-minute polish? Show me your title slide."*

**10–30 — Top 3 Confusion Points**
1. **Demoing a notebook live without crashes.** Use `Runtime → Restart and run all` once before showcasing.
2. **Verbal explanation of design choices.** Practice: "I picked these 5 features because they appear in the Framingham score; weights are ordinal because…"
3. **Sharing without exposing identifiers.** All datasets used are public/anonymized — confirm this in their submission.

**30–50 — "Go Further"**
Show the **MIMIC-IV** publicly-available ICU dataset (PhysioNet) → with proper data-use agreement, this is a path forward in college research.

**50–60 — Wrap + Motivational**
- Read each Track-B student's name, dataset, and one-sentence finding.
- Aug 3 disbursement reminder.
- *"You're a 10th-grader. Most med students don't touch a real dataset until 2nd or 3rd year. You're three years ahead. Carry that with you."*
