# Exact certification of E11 §4 / §4b (slack 0, bidegrees (2, 2), (2, 3), (3, 3)) — 2026-11-09

Provenance: computed and written by ChatGPT (two runs, 2026-11-09) at the request of the user; the files are kept
byte-identical to the delivered archives (`*/SHA256SUMS.json`, `*/COMPLETE_SHA256.json`). Re-run locally by Claude
(WSL, Python 3.12 venv with sympy 1.14.0, python-flint 0.9.0, g++ C++17): all totals and histograms identical, all
assertions PASS (about one minute). The characteristic-zero argument (w23_33/PROOF.md §1–§4) was read by Claude; no gap
found. **Not independently audited.** Zero credit.

## Contents
- `w22/`: (2, 2). All 15 degree-2 maps; all odd points in K = Q(√2, √(−1+i)) (degree 8); every possible coincidence
  decided exactly in K (`--no-sieve`). 157,824 label-matched triple occurrences; every |Ω| ≤ 4 hit has a diagonal or
  antidiagonal relative Möbius matrix, i.e. the two maps share the deck involution t ↦ −t: non-birational. Birational
  hits: 0. Also the exact enumeration of the 60 degree-3 maps (normal form F_k, H_z(k) = k(3k − 2)³ − z(2k − 1)).
- `w23_33/`: (2, 3), (3, 3). Prime p = 874009, at which all 75 covers and all their odd points split with distinct
  simple reductions (disc_k H_z = −2⁴3⁹z²(z − 1)²: étale over Z[i, 1/6]). Exhaustive three-point alignment in F_p
  (complete by j ≥ 6 from E12 Lemma 0); characteristic-zero coincidences survive reduction and |Ω| can only drop, so
  every characteristic-zero candidate appears. (2, 3): no |Ω| ≤ 4 hit. (3, 3): 8,896 hits, each satisfying
  q̄∘M̄ = Ū∘f̄ with Ū one of the 24 automorphisms of B; PROOF.md §4 lifts this identity to characteristic 0 by
  Hensel uniqueness of the normal-form parameter and of the marked simple points (this is not the invalid
  "reducible mod p ⇒ reducible" step of the R2 audit's M1). Birational hits: 0.

## Reproduction
```
cd w22 && python w22.py --no-sieve && python degree3_enumeration.py
cd w23_33/.. && sh exact_w/run_complete.sh     # run_complete.sh expects the folder name exact_w: copy w23_33 to exact_w
```
