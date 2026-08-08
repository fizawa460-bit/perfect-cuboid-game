# E-1b — first exactly-one population profile

> **STATUS:** `E_1B_COMPLETE_FINITE_ENUMERATION`
>
> **COUNTING:** primitive canonical `0<a<b<c`
>
> **CUTOFF:** `a^2+b^2+c^2 <= B^2`
>
> **SPACE-DIAGONAL INTEGRALITY:** not required

E-1b enumerates all three exactly-one populations under the E-1a convention:

```text
N_ab(B), N_ac(B), N_bc(B).
```

The implementation generates Pythagorean face incidences rather than scanning all integer triples, counts primitive third-edge choices exactly, and removes two-face / three-face overlaps by inclusion-exclusion.

## Finite population table

| B | N_ab | N_ac | N_bc | N_1 | ab/bc | ac/bc |
|---:|---:|---:|---:|---:|---:|---:|
| 100 | 1,240 | 545 | 835 | 2,620 | 1.485030 | 0.652695 |
| 200 | 6,166 | 2,690 | 3,808 | 12,664 | 1.619223 | 0.706408 |
| 500 | 48,141 | 21,585 | 27,979 | 97,705 | 1.720612 | 0.771471 |
| 1,000 | 221,249 | 99,887 | 123,839 | 444,975 | 1.786586 | 0.806588 |
| 2,000 | 999,707 | 453,195 | 544,961 | 1,997,863 | 1.834456 | 0.831610 |
| 5,000 | 7,188,977 | 3,267,168 | 3,798,731 | 14,254,876 | 1.892468 | 0.860068 |
| 10,000 | 31,593,274 | 14,373,282 | 16,389,285 | 62,355,841 | 1.927679 | 0.876993 |

At the largest audited cutoff,

```text
N_ab : N_ac : N_bc
= 31,593,274 : 14,373,282 : 16,389,285
≈ 1.927679 : 0.876993 : 1.
```

The normalized population vector is

```text
(ab, ac, bc)
≈ (0.5066610, 0.2305042, 0.2628348).
```

## Overlap ledger at B=10,000

Raw face incidences are

```text
A_ab = 31,623,954
A_ac = 14,396,768
A_bc = 16,418,505
```

with pair overlaps

```text
O_ab_ac = 12,482
O_ab_bc = 18,216
O_ac_bc = 11,022
```

and triple overlap

```text
T = 18.
```

The exactly-one populations therefore satisfy exactly

```text
N_ab = A_ab - O_ab_ac - O_ab_bc + T
N_ac = A_ac - O_ab_ac - O_ac_bc + T
N_bc = A_bc - O_ab_bc - O_ac_bc + T.
```

## Validation

The optimized Pythagorean-incidence enumeration was compared against a literal canonical triple scan at

```text
B = 20, 30, 50, 80.
```

All three directional counts agree exactly at every validation cutoff.

## First observation

Across the audited range, `ab/bc` rises from about `1.49` to `1.93`, while `ac/bc` rises from about `0.65` to `0.88`. Thus the finite profile is moving toward a shape resembling `2:1:1` over this range.

This is only a finite observation. E-1b does **not** assert that `2:1:1` is the limiting ratio or that either ratio is monotone for all larger cutoffs.

## Assets

```text
stages/euler-cuboid/scripts/E-1b/population_enumeration.py
stages/euler-cuboid/data/E-1b/population_report.json
```

## Next

`E-1c`: study the cutoff scaling of the three populations and determine whether the apparent movement toward `2:1:1` persists, stabilizes elsewhere, or requires a different normalization.
