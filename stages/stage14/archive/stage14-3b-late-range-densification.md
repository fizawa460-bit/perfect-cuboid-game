# Stage14-3b — late-range finite cutoff densification

## Purpose

Stage14-3b densifies the Stage14 finite directional census before the current stop line. It does not fit an asymptotic law and uses no Stage13 analytic statement.

The production Stage14 generation route was run once through `B=2,000,000`; exactly-two objects were then accumulated by their exact integer space diagonal `d`. The dense grid is

```text
B = 100,000, 150,000, ..., 2,000,000
step = 50,000
39 cumulative rows
```

The frozen anchor rows at `100k, 200k, 500k, 1m, 2m` reproduce exactly.

Machine-readable result:

```text
stages/stage14/data/14-3/late_range_densification.json
```

Reproduction script:

```text
stages/stage14/scripts/14-3/late_range_densification.py
```

## Main result 1 — the apparent `a/c = 7/4` plateau is not stable on a dense grid

Stage14-3a observed

```text
a/c = 7/4
```

at the three coarse sampled cutoffs `200k`, `500k`, and `1m`.

The 50k grid shows substantial motion between those samples. Examples:

```text
150k  a/c = 1.625000
200k  a/c = 1.750000
250k  a/c = 1.920000
300k  a/c = 1.785714
350k  a/c = 1.866667
400k  a/c = 1.694444
...
500k  a/c = 1.750000
550k  a/c = 1.553191
...
1m    a/c = 1.750000
```

Therefore the repeated coarse equality at `200k/500k/1m` does not support a constant finite trajectory, invariant, or limiting value.

Because cumulative counts are step functions, exact `7/4` equality persists on some integer cutoff intervals. In the audited range `100k <= B <= 2m`, those intervals are

```text
172057..207280
364285..365548
499525..501684
984113..1006560
1123357..1127184
1212625..1218028
1384837..1421728
```

This pattern is intermittent rather than one sustained plateau.

## Main result 2 — the `a/b` reversal is localized exactly in the finite event stream

At `B=1m`,

```text
(N_a,N_b,N_c)=(98,101,56)
a-b=-3.
```

Following every exactly-two object in increasing exact space diagonal gives four relevant tie/crossing events:

```text
d=1,083,121:  a-b  -1 ->  0, counts=(105,105,59)
d=1,096,685:  a-b   0 -> -1, counts=(105,106,59)
d=1,127,185:  a-b  -1 ->  0, counts=(106,106,60)
d=1,148,545:  a-b   0 -> +1, counts=(107,106,60)
```

After `d=1,148,545`, the cumulative finite census has `a>b` at every subsequent exactly-two event state through the verified ceiling `B=2,000,000`.

This is a finite statement only. It does not imply eventual asymptotic dominance of `a`.

## Selected dense rows

| B | `(N_a,N_b,N_c)` | a/c | b/c | a/b | a-b | leader |
|---:|---:|---:|---:|---:|---:|---|
| 100,000 | (33,33,23) | 1.434783 | 1.434783 | 1.000000 | +0 | tie |
| 150,000 | (39,37,24) | 1.625000 | 1.541667 | 1.054054 | +2 | a |
| 200,000 | (42,50,24) | 1.750000 | 2.083333 | 0.840000 | -8 | b |
| 250,000 | (48,57,25) | 1.920000 | 2.280000 | 0.842105 | -9 | b |
| 300,000 | (50,60,28) | 1.785714 | 2.142857 | 0.833333 | -10 | b |
| 400,000 | (61,70,36) | 1.694444 | 1.944444 | 0.871429 | -9 | b |
| 500,000 | (70,78,40) | 1.750000 | 1.950000 | 0.897436 | -8 | b |
| 600,000 | (77,87,47) | 1.638298 | 1.851064 | 0.885057 | -10 | b |
| 700,000 | (81,92,49) | 1.653061 | 1.877551 | 0.880435 | -11 | b |
| 800,000 | (87,96,51) | 1.705882 | 1.882353 | 0.906250 | -9 | b |
| 900,000 | (95,99,54) | 1.759259 | 1.833333 | 0.959596 | -4 | b |
| 950,000 | (96,99,55) | 1.745455 | 1.800000 | 0.969697 | -3 | b |
| 1,000,000 | (98,101,56) | 1.750000 | 1.803571 | 0.970297 | -3 | b |
| 1,050,000 | (100,104,59) | 1.694915 | 1.762712 | 0.961538 | -4 | b |
| 1,100,000 | (105,106,59) | 1.779661 | 1.796610 | 0.990566 | -1 | b |
| 1,150,000 | (107,106,60) | 1.783333 | 1.766667 | 1.009434 | +1 | a |
| 1,200,000 | (110,108,63) | 1.746032 | 1.714286 | 1.018519 | +2 | a |
| 1,300,000 | (115,111,65) | 1.769231 | 1.707692 | 1.036036 | +4 | a |
| 1,400,000 | (119,116,68) | 1.750000 | 1.705882 | 1.025862 | +3 | a |
| 1,500,000 | (123,120,70) | 1.757143 | 1.714286 | 1.025000 | +3 | a |
| 1,600,000 | (127,124,72) | 1.763889 | 1.722222 | 1.024194 | +3 | a |
| 1,700,000 | (131,126,73) | 1.794521 | 1.726027 | 1.039683 | +5 | a |
| 1,800,000 | (135,129,75) | 1.800000 | 1.720000 | 1.046512 | +6 | a |
| 1,900,000 | (139,134,77) | 1.805195 | 1.740260 | 1.037313 | +5 | a |
| 2,000,000 | (142,134,80) | 1.775000 | 1.675000 | 1.059701 | +8 | a |

The full 39-row table is in the JSON artifact.

## Interpretation boundary

The dense grid changes the Stage14-3a interpretation in one useful way:

```text
coarse a/c plateau       -> rejected as a stable finite law
b-to-a leader reversal   -> localized to exact finite d-events
```

What remains unknown:

```text
limiting directional ratio
eventual leader
growth exponent
logarithmic power
relation to Euler-side two-face direction law
```

No fit is performed in Stage14-3b.

## Triple status

No three-face object occurs through `B=2,000,000` in the production event ledger. This is the same finite search range already audited in Stage14-2 and is not a perfect-cuboid nonexistence result.

## Decision

```text
STAGE14_3A=COMPLETE
STAGE14_3B=COMPLETE
DENSE_FINITE_GRID_STEP=50000
A_OVER_C_7_4_LIMIT_SUPPORTED=false
A_B_CROSSING_LOCALIZED=true
FINAL_A_OVER_B_CROSSING_D_WITHIN_VERIFIED_RANGE=1148545
ASYMPTOTIC_FIT_PERFORMED=false
STAGE13_ASYMPTOTIC_RESULT_USED=false
NEXT=Stage14-3c finite diagnostic synthesis / stop-line preparation
```

Stage14-4 and Stage14-5 remain paused.
