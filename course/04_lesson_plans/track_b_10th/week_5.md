# Track B — Week 5: "Introduction to BioPython"

**Dates:** Tue Jul 14 + Thu Jul 16, 2026 · 6:30 PM PST · Colab + BioPython
**Big Picture:** *Week 5 of 7 — you've worked with patient-level data. Now: molecular-level data. Real human DNA, parsed in Colab.*

---

## SESSION 1 — Tuesday, July 14, 2026

### Learning Objectives
By the end of this session, students can:
1. Install BioPython in Colab and import `Bio.Seq` and `Bio.SeqIO`.
2. Read a FASTA file of a human gene (e.g., `BRCA1` exon).
3. Compute GC content and identify start codons.

### Active Recall (3 min)
"What's a t-test for? What's a p-value? What's the strongest correlation we found last week?"

### Big Picture (1 min)
Step 5 of 7. *"From people-level data to molecule-level data. Same Python."*

### Block 1 — 25 min
1. **Install + import:**
   ```python
   !pip install biopython -q
   from Bio.Seq import Seq
   from Bio import SeqIO
   ```
2. **Sequence basics:**
   ```python
   dna = Seq("ATGCGTACGTAGCTAGCTAACGTACGAT")
   print(len(dna))
   print(dna.complement())
   print(dna.reverse_complement())
   print(dna.translate())   # to amino acids
   ```
3. **GC content:**
   ```python
   from Bio.SeqUtils import gc_fraction
   print(f"GC = {gc_fraction(dna):.2%}")
   ```
4. **Loading a real FASTA from NCBI** (instructor links a small `BRCA1_exon11.fasta` from this page):
   ```python
   record = next(SeqIO.parse("BRCA1_exon11.fasta", "fasta"))
   print(record.id, record.description)
   print(f"Length: {len(record.seq)} bp")
   print(f"GC: {gc_fraction(record.seq):.2%}")
   ```

### 5-min Pomodoro Break
"Take a deep breath. Imagine 3 billion of these letters in every cell of your body." Pause for awe. Sip water.

### Block 2 — 25 min — Lab: "Read Your First Gene"
Each student loads the BRCA1 exon FASTA and:
- Computes its length, GC content, and translated protein sequence.
- Counts how often each base (A, C, G, T) appears using `record.seq.count("A")` etc.
- Plots base counts as a bar chart (calling back to Week 3 viz skills).

### 2-min Diffuse Mode Reflection
*"You just read a piece of an actual cancer-suppressor gene with code you wrote yourself. What's something you wish you could ask the gene?"*

### Homework Preview
Thursday: motif search + simple sequence-stat comparisons.

---

## SESSION 2 — Thursday, July 16, 2026

### Stuck Check (3 min)
"Whose `pip install` failed? Whose FASTA didn't open?"

### Big Picture (1 min)
Step 5 still. *"Today: search a sequence for clinically meaningful patterns."*

### Block 1 — 25 min — Motifs + Comparisons
1. **Motif search:**
   ```python
   gene_seq = str(record.seq)
   start_codons = [i for i in range(len(gene_seq)-2) if gene_seq[i:i+3] == "ATG"]
   stop_codons  = [i for i in range(len(gene_seq)-2) if gene_seq[i:i+3] in ("TAA","TAG","TGA")]
   print(f"Start codons: {len(start_codons)}; Stops: {len(stop_codons)}")
   ```
2. **Compare two genes:**
   ```python
   # instructor provides BRCA2_partial.fasta too
   r1 = next(SeqIO.parse("BRCA1_exon11.fasta", "fasta"))
   r2 = next(SeqIO.parse("BRCA2_partial.fasta", "fasta"))
   print("BRCA1 GC:", gc_fraction(r1.seq))
   print("BRCA2 GC:", gc_fraction(r2.seq))
   ```
3. **Translation length sanity check:**
   ```python
   protein = r1.seq.translate(to_stop=True)
   print("Protein:", protein[:60], "...")
   ```

### 5-min Pomodoro Break
"5-minute biology snack" — instructor shares a 60-second story about Marie Maynard Daly (first Black woman to earn a chemistry PhD in the US). Students share one figure they admire.

### Block 2 — 25 min — Lab: "Mini Sequence Lab"
Each student picks one of:
- Find every "ATG" in the BRCA1 exon and visualize their positions on a number line.
- Compute GC content in 50 bp windows across the gene; plot it.
- Translate to protein, count occurrences of each amino acid, bar-chart it.

### 2-min Diffuse Mode Reflection
*"You're 30 lines of code away from doing something a lab tech does. What WOULD a clinical genetics lab do next that you couldn't yet?"*

### Homework Preview
**Assignment W5 below.**

---

## WEEK 5 QUIZ — Track B (10 questions)

> **Spaced repetition:** Q9 + Q10 review Week 3 (visualization).

**Easy (5)**

1. To install BioPython in Colab:
   - A) `!pip install biopython` ✅ · B) `pip biopython install` · C) `apt-get biopython` · D) `import biopython`

2. `Seq("ATCG").complement()` returns:
   - A) `"TAGC"` ✅ · B) `"CGAT"` · C) `"GCTA"` · D) `"ATCG"`

3. GC content is:
   - A) The number of G + C bases divided by total bases ✅ · B) Total length · C) Position of the first G · D) None

4. To translate DNA to protein:
   - A) `seq.complement()` · B) `seq.translate()` ✅ · C) `seq.protein()` · D) `seq.amino()`

5. FASTA files are:
   - A) Spreadsheets · B) Plain-text files with sequences and headers ✅ · C) Image files · D) Compressed archives

**Medium (3)**

6. `Seq("ATCG").reverse_complement()` returns:
   - A) `"GCTA"` · B) `"CGAT"` ✅ · C) `"ATCG"` · D) `"TAGC"`

7. To translate up to the first stop codon:
   - A) `seq.translate(to_stop=True)` ✅ · B) `seq.translate(stop=True)` · C) `seq.until_stop()` · D) `seq[:stop]`

8. `gene_seq.count("ATG")` counts:
   - A) Non-overlapping occurrences of `"ATG"` ✅ · B) All overlapping copies · C) Random count · D) Always 1

**Hard (2)**

9. *(Week 3 review)* `plt.scatter(x, y, c=labels)` colors points by:
   - A) The order of x · B) The values in `labels` ✅ · C) Random · D) Always blue

10. *(Week 3 review)* In `sns.heatmap(corr, annot=True)`, `annot=True` does:
    - A) Annotates the matrix cells with their numeric values ✅ · B) Adds a title · C) Hides the colorbar · D) Logs the matrix

### Answer Key
1.A  2.A  3.A  4.B  5.B  6.B  7.A  8.A  9.B  10.A

---

## WEEK 5 ASSIGNMENT — Track B

**Title:** *"BRCA1 Mini Sequence Report"*
**Due:** Mon Jul 20, 11:59 PM PST

### Instructions
In a Colab notebook:
1. Install BioPython, import `Seq` and `SeqIO`.
2. Load the provided `BRCA1_exon11.fasta` (link on this week's course-site page).
3. Print: sequence length, GC content (with %), reverse complement first 60 bp, translated protein (to first stop).
4. Plot:
   - Bar chart of A/C/G/T counts.
   - Line plot of GC content in 50 bp windows across the sequence.
5. Markdown summary: 4 sentences on what these numbers tell you about this region.

### Grading Criteria — $1.50 when:
- [ ] BioPython installed and imports run (0.20)
- [ ] FASTA loaded and basic stats printed (0.30)
- [ ] Both plots rendered with titles + labels (0.40)
- [ ] Markdown summary present (0.30)
- [ ] Notebook runs end-to-end (0.30)

### Stretch
Compare BRCA1 and BRCA2 (provided) on GC content + length + protein length. One markdown sentence per comparison.

---

## Cumulative Mind Map (Week 5)

- All previous branches stand.
- 🆕 🧬 **Bioinformatics**:
  - `Bio.Seq`, `Bio.SeqIO`
  - DNA ops: `complement`, `reverse_complement`, `translate`
  - GC content, motif search (`count`, slicing)
  - FASTA: parse → record (id, description, seq)

Caption: *"Next week: bring it all together — the patient risk-scoring tool."*
