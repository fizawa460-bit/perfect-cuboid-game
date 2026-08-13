# Stage17-20 finite-data baseline

Status: submitted for fresh audit.

The audited Stage17-10 population is unchanged: primitive canonical triples `0<a<b<c`, exactly one integral face diagonal, common cutoff `R<=B`, and integral `R`.

`enumerate.py` follows the Stage16-20 Pythagorean-face coverage path and additionally requires `a^2+b^2+c^2` to be a square. An independent direct canonical-triple path returns the same set at B=100 and B=200.

## Frozen census

| B | N1 | ab | ac | bc |
|---:|---:|---:|---:|---:|
| 50 | 7 | 3 | 1 | 3 |
| 100 | 25 | 14 | 5 | 6 |
| 200 | 67 | 40 | 11 | 16 |
| 400 | 174 | 86 | 46 | 42 |
| 800 | 453 | 226 | 115 | 112 |
| 1200 | 764 | 373 | 208 | 183 |
| 1600 | 1077 | 535 | 266 | 276 |
| 2000 | 1434 | 698 | 369 | 367 |

CSV SHA-256: `2f066143090713c25eec2e8ecef7a31d5c5ec169dc008380577757b34674168a`.

## Matched Stage16 diagnostic

The frozen Stage16 source counts at the same cutoffs are 490, 2620, 12664, 59574, 273901, 662207, 1234822, and 1997863. The corresponding finite ratios `N1/M1` are approximately 0.014286, 0.009542, 0.005291, 0.002921, 0.001654, 0.001154, 0.000872, and 0.000718.

The face split and finite ratios are diagnostic only. No asymptotic order, limiting ratio, decay exponent, upper/lower bound, independence claim, or causal conclusion is inferred at this checkpoint.

Evidence level: COMPUTED. Population contract changed: NO. Comparison adapter required: NO. AR-039 remains parked for checkpoint 50. A fresh Stage17 audit is required before checkpoint 30.
