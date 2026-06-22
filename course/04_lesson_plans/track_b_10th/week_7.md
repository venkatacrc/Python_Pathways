# Track B — Week 7: "SHOWCASE — Patient Risk Scoring Tool"

**Dates:** Tue Jul 28 + Thu Jul 30, 2026 · 6:30 PM PST · Colab
**Big Picture:** *Week 7 of 7 — Tuesday is dress-rehearsal. Thursday is THE SHOWCASE — you demo your tool, defend its design, and discuss its limits like a clinician-scientist would.*

---

## SESSION 1 — Tuesday, July 28, 2026 — *Dress Rehearsal*

### Learning Objectives
1. Demo the risk tool from form input → output → validation → limitations.
2. Defend at least one design decision with a rationale.
3. Help one peer improve one part of their tool.

### Active Recall (3 min)
"What's the difference between a `Low` and `High` category in your tool? Why those thresholds?"

### Big Picture (1 min)
Step 7 of 7 almost lit. *"Tonight: practice. Thursday: do."*

### Block 1 — 25 min — Demo Practice
Each student gets ~5 min:
- Show the tool from form to chart, in a clean run.
- 90 sec design defense: "Why these 5 inputs, why these weights, what's the limitation."
- 90 sec Q&A from peers.

Instructor + peers give 1 specific compliment + 1 actionable suggestion each.

### 5-min Pomodoro Break
"Walk a lap" — stand, walk for 60 seconds, come back. Cardiologist-approved.

### Block 2 — 25 min — Pair Polish
Pairs swap notebooks. Each tries to break the partner's tool with edge inputs (age = 18, BMI = 50, etc.). Report bugs. Help fix one.

### 2-min Diffuse Mode Reflection
*"What's the part of YOUR tool that you'd put your name behind in front of a doctor? What's the part you'd hide?"*

### Homework Preview
Lock the notebook by Wed 11:59 PM PST. Bring polish + 1 chart you're proud of.

---

## SESSION 2 — Thursday, July 30, 2026 — *🏆 THE SHOWCASE 🏆*

### Cold Open — 2 min
Instructor: *"Six weeks ago you'd never heard of pandas. Tonight you walk in with a clinical decision-support prototype. That's what real biomedical informatics looks like."*

### Big Picture (1 min)
Step 7 of 7 LIT. Whole 7-step ladder glows. *"You're at the top."*

### Showcase Block — ~50 min (5 students × ~9 min each)
Each student: 9 min total —
- 4 min — live demo (load → input → score → chart → validation snippet)
- 2 min — *"My tool, my dataset, what I found, what I'd change."*
- 3 min — Q&A from peers + instructor (instructor scores Capstone Rubric live).

### Discussion Block — 10 min
Group conversation: *"How could a tool like this actually help a doctor or nurse? What guardrails would it need before deployment?"* Touchstones: regulatory (FDA SaMD), bias, validation cohorts, patient consent, EHR integration.

### Closing Ritual — 5 min
- Each student writes in the course-site journal (Track B Discussion): *"On June 15 I couldn't __. Today I can __."*
- Instructor reveals: *"Aug 3 = Certificate Day. Wallet payouts go out tomorrow morning."*
- Group screenshot. End on: *"You're builders, and the medicine that comes is going to need exactly this skill."*

### 2-min Diffuse Mode Reflection
*"Where does this skill plug into your future?"*

---

## WEEK 7 QUIZ — Track B (10 questions)
*Optional — completion-based, $1.00 earned for any honest attempt.*

> **Spaced repetition:** Q9 + Q10 review Week 5 (BioPython).

**Easy (5)**

1. The capstone showcase is on:
   - A) Aug 1 · B) Jul 30 · C) Aug 3 · D) Aug 4

2. A clinical decision-support tool needs:
   - A) Pretty colors only · B) Validation, transparency about limitations, regulatory awareness · C) Marketing · D) None of these

3. To re-render an updated chart in Colab, you need to:
   - A) Restart Colab · B) Re-run the cell that calls `plt.show()` · C) Refresh browser · D) Print again

4. The Framingham study is:
   - A) A pizza chain · B) A foundational longitudinal cardiovascular study · C) A coding competition · D) A novel

5. To export a Colab notebook for sharing:
   - A) Print → PDF · B) `File → Download → .ipynb` · C) Email screenshot · D) Tweet

**Medium (3)**

6. To document why you used certain weights:
   - A) Hide them in code · B) Add a markdown cell citing the source · C) Comment in Spanish · D) Skip it

7. Which is **NOT** a typical limitation of a tool like yours?
   - A) Small / non-representative training data · B) Data leakage · C) Demographic bias · D) `df.head()` default of 5
8. Demoing in a showcase, the most persuasive narrative is:
   - A) "It's perfect" · B) "Here's what it does, here's why these choices, here's what would break it" · C) "I'm not sure how it works" · D) "Trust me"

**Hard (2)**

9. *(Week 5 review)* `Seq("ATG").translate()` returns:
   - A) `Seq("M")` (the methionine amino acid; ATG is the start codon)   - B) `Seq("ATG")` · C) An error · D) Empty

10. *(Week 5 review)* GC content of `"ACGTACGT"` is:
    - A) 25% · B) 50% · C) 75% · D) 100%

### Answer Key
1.B  2.B  3.B  4.B  5.B  6.B  7.D  8.B  9.A  10.B

---

## WEEK 7 ASSIGNMENT (Capstone Submission)

**Title:** *"Submit your Patient Risk Tool for Showcase"*
**Due:** Wed Jul 29, 11:59 PM PST

### Instructions
Submit:
1. A finalized, runnable Colab notebook (link with view/comment access).
2. A 2-minute screen-recording walking through the tool.
3. A short Forum post in `[B] Track B Forum`:
   - Tool name
   - Dataset used
   - One thing you're proud of
   - One thing you'd improve

### Grading
This is the **Capstone**, scored against the rubric in Artifact 6 — up to **$12.50**.

### No stretch this week.

---

## Final Cumulative Mind Map (Week 7)

```
              MEDICAL PYTHON
        /        |          |          \
   Python     Pandas    Visualization   Statistics
    core      types     matplotlib +    descriptive +
              filtering seaborn          inferential
              groupby    titles/units    Pearson, Spearman,
              imputation                 t-test, p-values
                            \            /
                             Cohorts ↔ Charts ↔ p-values
                                         |
                                    BioPython
                                     Seq · SeqIO · GC · motifs
                                         |
                                 The Risk Tool
                              form → score → category
                              chart → validation → LIMITATIONS
```

Caption: *"On June 15 you'd never opened a Colab notebook. Tonight you've built a clinical-style tool from scratch. Take this map. Save it."*
