# F-02 addendum — structure of the low-mismatch slack-0 pairs (measured, 2026-11-13)

Status: **measurement with exact (mpmath, dps 50) recounts. Not a theorem.** Zero credit.

## 1. What was done

1. `f02_spectrum.py` (resume version v4) saves every T with ω ≤ cut, together with its frame points, in
   `low{a}x{b}.json`.
   - Cuts: (3,3) at 11; (4,4) at 14.
2. `analyze_extremal.py a b [ω]` rebuilds each saved T in mpmath and counts coincidences exactly.
   - A pair counts as coincident when its cross value is below 10⁻³⁰.
   - The run fails unless every other pair has a cross value above 10⁻¹².
   - Birationality is recomputed.
   - The birational configurations at the chosen ω are written to `extremal{a}x{b}[_om{ω}].json`.
3. `extremal_struct.py n [suffix]` puts each configuration (p₁, q, T), with p₂ = q∘T, into the first class that
   applies:
   1. **shared left factor**: n is even, and p₁ and q have a degree-2 left factor r with the same critical values.
      - For n = 4, p = r∘u with deg r = deg u = 2 exactly when Aut(p) contains an involution; u is the quotient by it.
      - Aut sizes agree with the Hurwitz centralizer counts.
   2. **symmetry, label-preserving**: q = g∘p₁∘S for a Möbius S and some g in the symmetry group of B. That group
      has 24 Möbius maps, each with or without complex conjugation. Here g maps each label class {±i}, {±1}, {0,∞}
      to itself.
   3. **symmetry, label-changing only**: as in class 2, but every such g permutes the label classes.
   4. **none**.

   Comparisons are exact, via `build_maps.key_maps_equal`.
4. Reproducibility check: `extremal_struct.py 4` reproduces the separate scripts `extremal_crosstab.py`,
   `extremal_symcheck.py` and `extremal_symcheck2.py`. The split is 8,832 / 1,728 / 576.

## 2. Exact results

All counts are of distinct T over birational slack-0 pairs. M = 2j + h.

| (n,n) | ω | M | exact count | (j,h) | class 1 shared factor | class 2 sym., labels kept | class 3 sym., labels permuted | class 4 none |
|---|---|---|---|---|---|---|---|---|
| (3,3) | 10 (min) | 10 | 384 | (4,2) | — (n odd) | 0 | 192 | 0 |
| (3,3) | 10 (min) | 10 | | (5,0) | — | 0 | 0 | **192** |
| (4,4) | 12 (min) | 12 | 11,136 | (6,0) | 8,832 | 1,728 | 576 | **0** |
| (4,4) | 14 | 10 | 27,840 | (4,2) | 12,288 | 0 | 1,728 | **3,072** |
| (4,4) | 14 | 10 | | (5,0) | 768 | 0 | 768 | **9,216** |

Sources: `extremal3x3.out`, `struct3x3.out`, `extremal4x4.out`, `struct4x4.out`, `extremal4x4_om14.out` and
`struct4x4_om14.out`.

Exact recount:
- (3,3): 1,824 records, none changed.
- (4,4): 79,229 records. The 5,885 that changed were all false coincidences in floating point, so every change
  raised ω.
- Smallest exact non-coincidence: 5.6·10⁻¹¹ for (4,4) and 3.0·10⁻³ for (3,3).

Other facts:
- (4,4), ω = 12:
  - Aut sizes of (p₁, q): (4,4) in 9,216 configurations, (2,2) in 768, (1,1) in 1,152.
  - 1,584 configurations have q = p₁ as maps.
- (4,4), ω = 14: Aut pairs (1,1) 576, (2,2) 11,904, (2,4) 3,072, (4,4) 12,288.

## 3. Reading [pattern only]

1. **The growth of M on the diagonal comes only from structured pairs.**
   - At (4,4), every configuration with M = 12 is in class 1, 2 or 3.
   - Unstructured pairs (class 4) first appear at M = 10, both at (3,3) and at (4,4).
2. **Unstructured maximum so far: M = 10 at (3,3) and (4,4).**
   - Off the diagonal the maximum is M = 8. Its structure has not been classified, because classes 2 and 3 need
     equal degrees.
   - If the unstructured maximum stays at 10, then for unstructured pairs ω ≥ 2(a+b) − 2, so |Ω| ≤ 4 forces
     a + b ≤ 3.
3. **The structured classes reduce to smaller problems.**
   - Class 1: p₁ = r∘u₁ and p₂ = r∘u₂. This is a problem of degree n/2 over r⁻¹(B).
   - Classes 2 and 3: p₂ = g∘p₁∘(S∘T). This is a correspondence between p₁ and a symmetric image of itself.
   - These need a separate treatment, not a uniform coincidence bound.
4. **Multiples of 96 continue in every class.** That is consistent with the action of the 48-element symmetry group.

## 4. Not done

- The off-diagonal extremals ((2,4), (3,4), (2,3), (1,b)) have not been classified.
- (5,5) has not been measured, because the degree-5 maps have not been built. This is where a shared left factor is
  impossible again.
- The class-4 configurations at (3,3) (5,0) and (4,4) ω = 14 have not been examined for other structure, such as a
  common sub-cover on the right after composing with g, or a larger symmetric set than B.
