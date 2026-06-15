---
title: Progress Wallets
search:
  exclude: true
---

# Progress Wallets

Each student has a private **Progress Wallet** page on this site, reachable only via a unique URL.

The instructor (Venkata) shares your wallet URL personally:
- Tracks A & B: emailed to your parent.
- Track C: emailed to you directly.

If you've lost your URL, email **`venkata@densesparse.com`** with subject `[WALLET]` and your name. Replacement takes ~5 minutes.

---

## How wallets are updated

Every Sunday night, Venkata runs:

```bash
python scripts/update_wallet.py
git add course/wallets && git commit -m "Wallet update — week N" && git push
```

Within ~2 minutes the GitHub Actions deploy finishes and your wallet shows the new totals.

## Sample wallet

For demonstration, a sample (placeholder data) wallet renders below — your private one looks just like this with your real numbers.

<div class="wallet">
  <h2>Sample Student's Wallet</h2>
  <p>Track: <strong>Track B</strong> &middot; Last updated: <strong>Sample data</strong></p>
  <table>
    <tr><th>Item</th><th class="amt">Earned</th><th class="amt">Max</th></tr>
    <tr><td>Quizzes (W1–W7)</td><td class="amt">$3.50</td><td class="amt">$7.00</td></tr>
    <tr><td>Assignments (W1–W7)</td><td class="amt">$4.50</td><td class="amt">$10.50</td></tr>
    <tr><td>Capstone</td><td class="amt">$0.00</td><td class="amt">$12.50</td></tr>
    <tr class="total"><td>TOTAL</td><td class="amt">$8.00</td><td class="amt">$30.00</td></tr>
  </table>
  <div class="bar"><div style="width: 26.7%;"></div></div>
  <p class="pct">26.7% of $30 earned</p>
</div>

## Privacy note

Wallet URLs use a 12-character random slug. They are not searchable, not indexed (`search.exclude: true`), and not linked from anywhere on this public site. Only you and the instructor know your URL. The actual grading data lives in a private Google Sheet only the instructor can see.
