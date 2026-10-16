# Stage32 FIXED-DIRECTION-CERTIFICATES — exact Hodge bound and fixed-direction certificates on compressed terminals

Status: `RESEARCH_RESULT__HOSTILE_AUDIT_PENDING__MAIN_AUTHORITY_UNCHANGED`.

This is a necessary-condition research result. It does not change MAIN authority (V51, 5369214401). It grants no MAIN, effectivity, receiver, theorem, endpoint, Stage32-closure, Perfect-Cuboid or merge credit.

## Setting

- `S` is the cuboid surface (minimal resolution) and `G` the Gram matrix of `Pic(S) ≅ Z^64`, from the retained basis.
- `P` (140 × 64) holds the pairings of the 140 known curves with that basis.
- A compressed terminal is `t = (x0..x10, d, e)`:
  - `x_i = C.Gamma_{l_i}` for the assignment order `l = [95,99,103,102,49,97,94,101,93,98,96]`, so `x4` is the normal curve 49 and the other ten coordinates are exceptional;
  - `d = K.C` and `e = sum_j C.E_j`.
- `A` (13 × 64) is the integral map with `A x = t`. Its rows are those 11 curve rows, the degree row `(sum normal + 5 sum exceptional)/19`, and the exceptional-sum row.
- The population is the **UNIBRANCH-NODE-HURWITZ census**, the same as V50 and V51:
  - N220 canonical terminals: `x0 <= x1`; if `x0 = x1` then `(x5,x6) <=lex (x8,x9)`; `x1+x8+x9+x10` is even; `sum_{i≠4} x_i <= e`; and `x4 <= 19d-5e`;
  - with `S10 + min(38, e - M10) >= max(K, ceil((d+e)/2) - 2g + 2)`;
  - over the 530 strata `(g,d,e)`.

## Proposition (fibre emptiness certificates)

Let `L = 2g - 2 - d`. Every integral curve in the population satisfies `C^2 >= L` (adjunction, `p_a >= g`). It also satisfies `C.Gamma_k >= 0` for all 140 known curves, since it is none of them.

Define:

- `Q = (A G^-1 A^T)^-1`;
- `h0(t) = t^T Q t`;
- `LIN = P G^-1 A^T Q`;
- for a fixed rational `lambda >= 0` in `Q^140`, `lin_D(t) = lambda^T LIN t`;
- `c_D = lambda^T P N M^-1 N^T P^T lambda`, where `N` is an integral basis of `ker A` and `M = -N^T G N`.

If `h0(t) < L`, or if `lin_D(t) < 0` and `lin_D(t)^2 > (h0(t) - L) c_D`, then no class `x` in `Pic(S)` with `A x = t` satisfies all of the necessary conditions. In particular, the terminal's fibre contains no curve of the population.

**Proof.**

1. `M` is positive definite. This is checked exactly by LDL; it is Hodge index on `ker A ⊂ K⊥`.
2. Over the reals, write `x = x* + y` with `x* = G^-1 A^T Q t` and `y ∈ ker A`.
3. Then `x*.y = t^T Q A y = 0`. Hence `x^2 = h0 + y^2` with `y^2 <= 0`, and `x^2 <= h0`. If `h0 < L`, the first case is done.
4. Let `D = sum_k lambda_k Gamma_k` and `s >= 0`. Then `x.D = lin_D + y.D >= 0`.
5. So `x^2 <= x^2 + 2s x.D = h0 + 2s lin_D + (y^2 + 2s y.D)`.
6. Write `y = N z`. Then `y^2 + 2s y.D = -z^T M z + 2s lambda^T P N z <= s^2 c_D`.
7. So `x^2 <= h0 + 2s lin_D + s^2 c_D` for every `s >= 0`.
8. If `lin_D < 0`, take `s = -lin_D/c_D`. This gives `x^2 <= h0 - lin_D^2/c_D < L`, which contradicts `x^2 >= L`. ∎

Any `lambda >= 0` gives a valid certificate. The 24 directions in `DIRECTIONS.json` were selected by sampling (research cycle 32R-11). They need not be optimal, and their choice does not affect validity.

## Count

The C counter `count_fixed_direction_certificates.c` works as follows:

- It enumerates every canonical exceptional prefix of every stratum, using a monotone pruning that is checked against exact prefix counts.
- It tests every `x4` in `0..19d-5e` with exact `__int128` integer arithmetic. Every product in the certificate test is overflow-checked.
- The forms are integer-scaled from the exact rationals; `Q` has denominator 456.

| | count |
|---|---|
| census prefixes (= N220 × unibranch) | 3,736,306,749 (530 strata, each equal to the symbolic count) |
| census terminals (= V50) | 511,353,002,049 |
| + exact Hodge bound | 7,601,355,235 |
| **+ 24 fixed-direction certificates** | **727,865,116** |
| per-row MIN with V51 (HPADJ22-UNIBRANCH) | **726,240,487** (≈ V51 / 7.4) |

- V51 is smaller in 13 high-d rows (`g0-d034…d044`, `g1-d036…d048`), and the per-row MIN takes those values.
- Counts are **compressed terminals**, not Picard classes or curves.

## Checks (`verify_fixed_direction_certificates.py`)

1. The exact forms are rebuilt from the retained Picard data. The kernel's negative definiteness is checked exactly, and every `lambda >= 0`. The forms' sha256 must match `RESULT.json`.
2. The 530 strata and their exact prefix counts are rebuilt with the N220 symbolic counter.
3. **Independent reference.** A separate Python enumeration with exact integer arithmetic reproduces `(prefixes, Hodge survivors, final survivors)` on the 40 smallest strata.
4. The C counter is compiled and run. Every stratum's prefix count must equal step 2, and all per-stratum data must equal `RESULT.json`.
5. The per-row MIN with V51 and all totals are recomputed.

`--skip-full` runs steps 1–3 only, in about 1 minute. The full run takes about 14 minutes on 12 threads and needs `gcc` with OpenMP.

## Promotion

Before any MAIN use, three things are required:

1. a hostile audit;
2. a separate MAIN V52 authority sync;
3. owner merge permission.
