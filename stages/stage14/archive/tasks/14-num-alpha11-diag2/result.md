# Stage14-numα11-diag2 — 50m shell distribution diagnostic

## Result

The merged α11 exact B500m census was split into ten non-overlapping 50m shells. Every adjacent pair of 50m shells recomposes the merged diag1 100m parent shell exactly.

| shell d | N2 | a | b | c | Ra | Rb | Rc |
|---|---:|---:|---:|---:|---:|---:|---:|
| (0,50m] | 1428 | 552 | 573 | 303 | 0.3866 | 0.4013 | 0.2122 |
| (50m,100m] | 447 | 177 | 185 | 85 | 0.3960 | 0.4139 | 0.1902 |
| (100m,150m] | 338 | 130 | 134 | 74 | 0.3846 | 0.3964 | 0.2189 |
| (150m,200m] | 244 | 98 | 75 | 71 | 0.4016 | 0.3074 | 0.2910 |
| (200m,250m] | 200 | 75 | 82 | 43 | 0.3750 | 0.4100 | 0.2150 |
| (250m,300m] | 209 | 85 | 82 | 42 | 0.4067 | 0.3923 | 0.2010 |
| (300m,350m] | 178 | 72 | 62 | 44 | 0.4045 | 0.3483 | 0.2472 |
| (350m,400m] | 150 | 51 | 59 | 40 | 0.3400 | 0.3933 | 0.2667 |
| (400m,450m] | 160 | 72 | 64 | 24 | 0.4500 | 0.4000 | 0.1500 |
| (450m,500m] | 141 | 62 | 55 | 24 | 0.4397 | 0.3901 | 0.1702 |

## What changed relative to diag1

The large 300–400m versus 400–500m contrast does not disappear at 50m resolution.

- `Rc` is high in both halves of 300–400m: `0.2472`, `0.2667`.
- `Rc` is low in both halves of 400–500m: `0.1500`, `0.1702`.
- `Ra` is high in both halves of 400–500m: `0.4500`, `0.4397`.

Therefore the diag1 400–500m anomaly is not caused by a single narrow 50m burst. Both halves carry the same qualitative direction bias.

The largest adjacent 50m movement is exactly at the boundary 350–400m -> 400–450m: `Rc` changes by `0.1166667` (11.67 percentage points), while `Ra` changes by 11.00 points.

Other parent shells are less uniform. In particular 100–200m is strongly internally split: `Rb` moves from `0.39645` in 100–150m to `0.30738` in 150–200m, a change of 8.91 points. Thus the shell process is not well described by one smooth monotone drift with d.

These are finite descriptive facts only. Counts in the later 50m shells are around 141–209, so the next task should calibrate how much of the observed shell heterogeneity is compatible with multinomial sampling fluctuation under a common direction distribution. The previous cumulative 2% operational gate is not a statistical significance threshold.

```text
STAGE14_NUM_ALPHA11_DIAG2=B500M_50M_SHELL_DIAGNOSTIC_COMPLETE
SOURCE_B500M_ROWS=3495
DIAG1_100M_PARENT_RECOMPOSITION_EXACT=true
MAX_ADJACENT_50M_ABSOLUTE_RATIO_SHIFT=0.11666666666666667
MAX_ADJACENT_50M_SHIFT_DIRECTION=c
MAX_ADJACENT_50M_SHIFT_BOUNDARY=350m_400m_to_400m_450m
B400M_TO_B500M_DIRECTION_PATTERN_PERSISTS_IN_BOTH_50M_HALVES=true
SIMPLE_SMOOTH_DIRECTION_DRIFT_SUPPORTED=false
CUMULATIVE_2PCT_GATE_REUSED_AS_SIGNIFICANCE=false
STATISTICAL_SIGNIFICANCE_CLAIM=false
ASYMPTOTIC_CLAIM=false
NEXT=Stage14-num-alpha11-diag3
```
