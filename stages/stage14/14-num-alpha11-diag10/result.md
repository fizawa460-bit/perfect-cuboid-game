# Stage14-num-alpha11-diag10 — finite-count shell heterogeneity test

## Result

Diag9 isolated large shell-to-shell movement in the conditional second-face-survival factor while the Stage13-style raw source proportions stayed almost fixed. Diag10 asks whether that movement is already larger than finite-count noise at the current `B<=1,000,000` panel.

Frozen shell exactly-two counts:

```text
89, 27, 22, 29, 21, 40, 27
```

Total exactly-two objects: `255`; pooled pair counts `(a,b,c)=(98,101,56)`.

### 1. Conditional permutation test

Null: one common pair-direction law across all seven shells, conditional on the observed row totals and pooled direction totals. `50,000` deterministic permutations, seed `14010`.

Observed statistics and Monte Carlo p-values:

```text
Pearson chi-square                 12.11419   p=0.43899
G statistic                        13.82070   p=0.33827
max shell pair-L1                   0.46710   p=0.14200
N2-weighted survival-shape RMS      0.06435   p=0.49387
```

No statistic rejects the finite-count common-law null at 5%.

### 2. Source-adjusted common-survival calibration

Use the frozen `B=1m` empirical relative survival profile

```text
S_ab:S_ac:S_bc = 0.604399:0.908758:1
```

and each shell's actual raw-source composition to construct shell-specific expected pair probabilities. `50,000` deterministic parametric draws, seed `14011`.

```text
source-adjusted Pearson            11.86304   p=0.62471
source-adjusted G                  13.60455   p=0.51151
N2-weighted survival-shape RMS      0.06435   p=0.49441
```

This second p-value set is a plug-in calibration, not an exact nuisance-free test, because the global survival profile is estimated from the same B<=1m panel. It nevertheless agrees with the conditional test.

## Interpretation

The diag9 statement remains algebraically correct: the visible shell volatility enters through the second-face-survival factor rather than through movement of the raw Stage13-style source population. But at `N2=255` total and only `21..89` objects per shell, the *magnitude* of that survival-side volatility is entirely compatible with ordinary finite-count sampling noise.

Therefore current data do **not** detect arithmetic shell heterogeneity. This also does not prove shell homogeneity asymptotically; more data could still reveal a real arithmetic effect.

```text
STAGE14_NUM_ALPHA11_DIAG10=FINITE_COUNT_SHELL_HETEROGENEITY_TEST_COMPLETE
SHELL_COUNT=7
B_MAX=1000000
TOTAL_N2=255
CONDITIONAL_MC_TRIALS=50000
CONDITIONAL_PEARSON_P=0.4389912201755965
CONDITIONAL_G_P=0.3382732345353093
CONDITIONAL_MAX_PAIR_L1_P=0.14199716005679885
CONDITIONAL_SURVIVAL_RMS_P=0.49387012259754803
SOURCE_ADJUSTED_PLUGIN_SURVIVAL_RMS_P=0.49441011179776406
COMMON_PAIR_DIRECTION_NULL_REJECTED_AT_5PCT=false
FINITE_COUNT_SAMPLING_NOISE_SUFFICIENT_EXPLANATION_AT_CURRENT_B1M_PANEL=true
ARITHMETIC_SHELL_HETEROGENEITY_DETECTED=false
ARITHMETIC_SHELL_HETEROGENEITY_RULED_OUT_ASYMPTOTICALLY=false
ASYMPTOTIC_SECOND_FACE_SURVIVAL_PROFILE_CLAIM=false
ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM=false
NEXT=Stage14-num-alpha11-diag11 cumulative survival-rate drift and uncertainty bands / stopping decision
```
