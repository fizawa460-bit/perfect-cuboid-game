# Stage14-numα11-diag1 — 100m shell distribution diagnostic

## Result

The merged α11 exact B500m census was split into five non-overlapping 100m shells. This changes the view from cumulative ratios to shell-local ratios without performing a new census.

| shell d | N2 | a | b | c | Ra | Rb | Rc |
|---|---:|---:|---:|---:|---:|---:|---:|
| (0,100m] | 1875 | 729 | 758 | 388 | 0.3888 | 0.4043 | 0.2069 |
| (100m,200m] | 582 | 228 | 209 | 145 | 0.3918 | 0.3591 | 0.2491 |
| (200m,300m] | 409 | 160 | 164 | 85 | 0.3912 | 0.4010 | 0.2078 |
| (300m,400m] | 328 | 123 | 121 | 84 | 0.3750 | 0.3689 | 0.2561 |
| (400m,500m] | 301 | 134 | 119 | 48 | 0.4452 | 0.3953 | 0.1595 |

B500m cumulative ratios are `(Ra,Rb,Rc)=(0.39313,0.39227,0.21459)`.

The shell view is materially less smooth than the cumulative view. Most notably, `Rc` moves from `0.25610` in 300–400m to `0.15947` in 400–500m, an absolute adjacent-shell shift of `0.09663` (9.66 percentage points). Over the same transition `Ra` moves by `0.07018` (7.02 points). Earlier adjacent shells also show roughly 4–5 point movement in `Rb/Rc`.

The 400–500m `Rc` deviation from the B500m cumulative ratio is about `-2.61` marginal binomial standard errors. This is only a descriptive scale: the cumulative reference contains the shell itself, the three categories are multinomial, and no independence/significance claim is made here.

Therefore the concern that cumulative ratios may be hiding shell-local structure is supported strongly enough to justify finer resolution. diag2 should split to 50m shells before α12 simply extends the upper bound.

```text
STAGE14_NUM_ALPHA11_DIAG1=B500M_100M_SHELL_DIAGNOSTIC_COMPLETE
SOURCE_B500M_ROWS=3495
SHELL_LOCAL_MOVEMENT_MATERIAL=true
MAX_ADJACENT_ABSOLUTE_RATIO_SHIFT=0.09662912243740379
MAX_SHIFT_DIRECTION=c
MAX_SHIFT_TRANSITION=300m_to_400m_shell__to__400m_to_500m_shell
CUMULATIVE_VIEW_CAN_HIDE_SHELL_LOCAL_MOVEMENT=true
CUMULATIVE_2PCT_GATE_REUSED_AS_SIGNIFICANCE=false
STATISTICAL_SIGNIFICANCE_CLAIM=false
ASYMPTOTIC_CLAIM=false
NEXT=Stage14-num-alpha11-diag2
```
