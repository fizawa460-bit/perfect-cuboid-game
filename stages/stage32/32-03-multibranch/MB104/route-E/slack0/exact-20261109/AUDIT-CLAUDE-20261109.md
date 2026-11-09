# Audit of the exact E11 certificates (slack 0, (2, 2), (2, 3), (3, 3)) — Claude, reading + executing, 2026-11-09

Verdict: **PASS**. No must-fix. Two remarks (no change needed).

Scope: all code in `w22/` and `w23_33/` read line by line against `w22/README.md` and `w23_33/PROOF.md`; both
certificates re-run locally (WSL, Python 3.12, sympy 1.14.0, python-flint 0.9.0, g++ C++17) with identical totals,
histograms and assertions. The auditor did not write the certificates (ChatGPT did); the auditor prepared the PR.

| # | claim | checked against the code | result |
|---|---|---|---|
| 1 | 15 degree-2 maps | `(u₀ + v₀t²)/(u₁ + v₁t²)` for all 15 pairs of values (modular_search.py; w22.py via the 24 automorphisms and two shapes) | ✔ |
| 2 | 60 degree-3 maps, normal form F_k | P0 = t²(At + C), Q0 = t − k, A = 2k − 1, C = 2 − 3k; H coefficients [z, −8 − 2z, 36, −54, 27] = k(3k − 2)³ − z(2k − 1); frame orientation sends critical points 0, ∞, 1 to values 0, ∞, 1 (Cramer identity det(z,y)x + det(x,z)y = det(x,y)z) | ✔ |
| 3 | good reduction at p = 874009 | every fibre over B splits completely, multiplicities 1 or 2 (also at ∞, validate_lifting.py), 2n + 4 distinct odd points, gcd(P, Q) = 1, squarefree Wronskian with 2n − 2 double points | ✔ |
| 4 | completeness of the alignment | `first = nA − jmin + 3` (5 for (2, 3), 7 for (3, 3)); at most nA − j unmatched points, j ≥ max(nA, nB) − 4 by O_i \ Ω ⊆ J | ✔ |
| 5 | Ω | nA + nB − 2·(label-matched coincidences) − (label-mismatched), over all point pairs | ✔ |
| 6 | composite test | f_D∘M and U∘f_A composed as binary forms, cross-multiplied; U runs over the 24 automorphisms of B, built in Q(i) and nonsingular mod p | ✔ |
| 7 | lifting to characteristic 0 (PROOF.md §4) | normal-form parameter = simple root of H_z, marked points simple: Hensel uniqueness; z, z − 1 ∈ {±1, ±i, ±1 ± i} are units away from 2 | ✔ |
| 8 | (2, 2) non-birationality | for degree-2 maps: non-birational ⇔ f₂ = U∘f₁ ⇔ same deck involution t ↦ −t ⇔ relative matrix diagonal or antidiagonal; all coincidences decided in K | ✔ |

Cross-check: the (3, 3) alignment total 3,287,808 equals the E11 search size recounted by DeepSeek in round 1 (§8).

Remarks:
1. `modular_search.py::make` does not itself reject a triple root at ∞; `validate_lifting.py` asserts n − deg ∈ {0, 1, 2}
   for every fibre, so no invalid cover can pass.
2. `run_complete.sh` expects the folder name `exact_w` (stated in README).
