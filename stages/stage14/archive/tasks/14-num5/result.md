# Stage14-num5 — moving-window finite scaling and anomaly diagnostics

> STATUS: `STAGE14_NUM5=COMPLETE_FINITE_SCALING_ANOMALY_DIAGNOSTICS`
>
> CLASSIFICATION: finite descriptive diagnostics only. All power-law fits and anomaly thresholds are non-theorem heuristics.
>
> No asymptotic or perfect-cuboid existence/nonexistence claim is made here.

## 1. Input contract

Num5 consumes the merged Stage14-num4 canonical `B=100,000,000` source and refuses to run unless the frozen num3 object/face/edge hashes and all four num4 unified hashes match. The population remains primitive exact-two objects under the Stage14 numerical contract; the frozen triple count is `T=0`.

The diagnostic grid is every `5,000,000` in `B`. Moving half-range shells are `(B/2,B]` for `B=30m,35m,...,100m` (15 shells). Rolling power fits use five consecutive cumulative grid points.

## 2. Cumulative finite scale

| B | N2 | a | b | c | N2/sqrt(B) | max degree |
|---:|---:|---:|---:|---:|---:|---:|
| 5,000,000 | 531 | 207 | 211 | 113 | 0.237470419 | 9 |
| 10,000,000 | 720 | 293 | 286 | 141 | 0.227683992 | 9 |
| 15,000,000 | 855 | 348 | 340 | 167 | 0.220760051 | 9 |
| 20,000,000 | 977 | 392 | 388 | 197 | 0.218463841 | 9 |
| 25,000,000 | 1070 | 425 | 429 | 216 | 0.214000000 | 9 |
| 30,000,000 | 1157 | 455 | 463 | 239 | 0.211238333 | 9 |
| 35,000,000 | 1228 | 481 | 493 | 254 | 0.207569885 | 10 |
| 40,000,000 | 1309 | 512 | 524 | 273 | 0.206971073 | 10 |
| 45,000,000 | 1375 | 536 | 551 | 288 | 0.204972898 | 10 |
| 50,000,000 | 1428 | 552 | 573 | 303 | 0.201949697 | 10 |
| 55,000,000 | 1490 | 573 | 599 | 318 | 0.200911559 | 10 |
| 60,000,000 | 1547 | 600 | 620 | 327 | 0.199716841 | 11 |
| 65,000,000 | 1597 | 621 | 636 | 340 | 0.198083471 | 11 |
| 70,000,000 | 1642 | 640 | 653 | 349 | 0.196256538 | 11 |
| 75,000,000 | 1685 | 653 | 673 | 359 | 0.194567041 | 11 |
| 80,000,000 | 1726 | 664 | 696 | 366 | 0.192972666 | 11 |
| 85,000,000 | 1767 | 678 | 715 | 374 | 0.191658059 | 11 |
| 90,000,000 | 1806 | 694 | 736 | 376 | 0.190369115 | 11 |
| 95,000,000 | 1842 | 719 | 744 | 379 | 0.188985212 | 11 |
| 100,000,000 | 1875 | 729 | 758 | 388 | 0.187500000 | 11 |

`N2/sqrt(B)` falls from `0.2374704192` at `B=5m` to exactly `0.1875` at `B=100m`, a finite fractional change of about `-21.04%`. This continues the num3 warning that the early `~sqrt(B)` normalization is not stabilized.

## 3. Five-point rolling log-log fits

Each row fits `log N2 = log C + alpha log B` over five consecutive 5m grid points. `alpha` is an effective finite exponent only.

| end B | start B | alpha | R^2 |
|---:|---:|---:|---:|
| 25,000,000 | 5,000,000 | 0.436373295 | 0.999875654 |
| 30,000,000 | 10,000,000 | 0.433456755 | 0.999704213 |
| 35,000,000 | 15,000,000 | 0.426837223 | 0.999001216 |
| 40,000,000 | 20,000,000 | 0.418897526 | 0.999325177 |
| 45,000,000 | 25,000,000 | 0.426634491 | 0.999198740 |
| 50,000,000 | 30,000,000 | 0.419886286 | 0.998188178 |
| 55,000,000 | 35,000,000 | 0.421265125 | 0.997742532 |
| 60,000,000 | 40,000,000 | 0.409165640 | 0.998859024 |
| 65,000,000 | 45,000,000 | 0.412969865 | 0.998703782 |
| 70,000,000 | 50,000,000 | 0.415768617 | 0.998740115 |
| 75,000,000 | 55,000,000 | 0.395116912 | 0.999007754 |
| 80,000,000 | 60,000,000 | 0.379636095 | 0.999820860 |
| 85,000,000 | 65,000,000 | 0.376323716 | 0.999961887 |
| 90,000,000 | 70,000,000 | 0.378880668 | 0.999942893 |
| 95,000,000 | 75,000,000 | 0.378467490 | 0.999916308 |
| 100,000,000 | 80,000,000 | 0.371872866 | 0.999498481 |

The rolling exponent moves from `0.436373295` (ending 25m) to `0.371872866` (ending 100m), a change of `-0.064500429`. Under the declared descriptive threshold `|delta alpha| >= 0.05`, this is a material finite scaling drift. `SCALING_STABILIZED=false`.

## 4. Moving-shell direction drift

The final cumulative `B=100m` shares are `a=0.3888`, `b=0.4042666667`, `c=0.2069333333`. Comparing each `(B/2,B]` shell against those final shares gives the largest finite deviations:

| direction | largest abs deviation | shell end B | shell share | final cumulative share |
|:--|--:|---:|--:|--:|
| a | 0.044800000 | 55,000,000 | 0.344000000 | 0.388800000 |
| b | 0.024967672 | 90,000,000 | 0.429234339 | 0.404266667 |
| c | 0.043733333 | 55,000,000 | 0.250666667 | 0.206933333 |

With the declared `0.04` descriptive threshold, the `a` and `c` shell proportions show material finite drift; `b` does not. This is not evidence for or against any limiting directional ratio.

## 5. e9 six-state local fingerprint stability

For each prime `p in {2,3,5,7,11,13}`, num5 recomputes the exact e9 six-state fingerprint on every object and compares adjacent half-range-shell distributions by total variation distance (TVD).

| p | maximum adjacent-shell TVD | at shell end B |
|---:|---:|---:|
| 2 | 0.039457381 | 35,000,000 |
| 3 | 0.037068729 | 45,000,000 |
| 5 | 0.030625729 | 40,000,000 |
| 7 | 0.025120589 | 65,000,000 |
| 11 | 0.027769088 | 55,000,000 |
| 13 | 0.025996276 | 55,000,000 |

All maxima stay below the declared `0.05` descriptive threshold. Thus `LOCAL_FINGERPRINT_MATERIAL_INSTABILITY_DETECTED=false` on the completed finite range. This is a stability observation, not an independence theorem.

## 6. Graph anomalies

The finer 5m grid resolves two max-degree jumps that were hidden between the coarser frozen num3 milestones:

- at `B=35,000,000`: max degree `9 -> 10`;
- at `B=60,000,000`: max degree `10 -> 11`;

Num3 only stated the first *listed frozen milestone* with degree 10 (`50m`) and 11 (`100m`); num5 does not contradict that statement. It locates the transitions more tightly on the 5m grid.

## 7. Anomaly policy and handoff

The thresholds are intentionally simple and frozen for reproducibility, not statistical significance claims:

```text
rolling alpha total drift        0.05
direction shell share deviation  0.04
local adjacent-shell TVD         0.05
graph max-degree jump            1
```

Observed flags:

- `direction_shell_drift=true`
- `graph_degree_jump=true`
- `local_fingerprint_instability=false`
- `perfect_cuboid_emergency=false`
- `scaling_alpha_drift=true`

The main handoff is therefore: scaling remains visibly non-stationary at `B<=100m`; direction shells still move at the few-percent level; the e9 local fingerprint distributions are comparatively stable; graph hubs continue to acquire partners. The numerical track should append larger exact cutoffs rather than promote a finite fit to a law.

## 8. Frozen boundary

```text
STAGE14_NUM5=COMPLETE_FINITE_SCALING_ANOMALY_DIAGNOSTICS
MOVING_WINDOWS_FROZEN=true
ROLLING_FITS_NON_THEOREM=true
SCALING_STABILIZED=false
LOCAL_FINGERPRINT_MATERIAL_INSTABILITY_DETECTED=false
MATERIAL_FINITE_CHANGE_HANDOFF=true
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
NEXT=Stage14-num6 rolling observatory / larger exact cutoff append
```

Canonical artifacts:

```text
stages/stage14/14-num5/result.md
stages/stage14/scripts/14-num5/scaling_anomaly_diagnostics.py
stages/stage14/data/14-num5/scaling_anomaly_manifest.json
.github/workflows/stage14-num5-scaling-anomaly.yml
```
