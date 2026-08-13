# Stage14-numα11-diag3 — multinomial shell homogeneity calibration

## Result

This stage calibrates the visible 50m-shell direction swings from diag2 against a simple null model: conditional on each shell's exact `N2`, directions `(a,b,c)` are multinomial with one common pooled direction probability across shells.

This is a **calibration model only**. The arithmetic objects are deterministic and may have family dependence, so the test is not a proof that the objects are IID random samples.

## 1. Global 50m-shell homogeneity

For the full `10 x 3` shell-by-direction table:

- Pearson `chi^2 = 25.4664730`, `df=18`, `p=0.1125972`
- likelihood-ratio `G = 25.4899214`, `p=0.1120055`
- Cramer's `V = 0.06036`

Thus the common-direction multinomial null is **not rejected at 5%** at 50m resolution.

This is important: the 11-point-looking local jumps in diag2 are visually large, but once all 10 shells and their sample sizes are calibrated together, the finite dataset does not yet force a non-homogeneous direction law.

## 2. Re-aggregated 100m parents

For the five exact diag1 100m parents:

- Pearson `chi^2 = 16.0397435`, `df=8`, `p=0.0418148`
- `G = 16.1201016`, `p=0.0406930`
- Cramer's `V = 0.04790`

This crosses the conventional 5% line, but only narrowly. The effect size is small and this analysis was motivated by the already-observed shell pattern, so it is treated as **exploratory evidence**, not a theorem-level structural detection.

## 3. The 300–400m versus 400–500m contrast

Combining each of those 100m regions gives:

- Pearson `chi^2 = 9.1635677`, `df=2`, `p=0.0102366`
- `G = 9.2719565`, `p=0.0096966`
- Cramer's `V = 0.12070`

So the particular late contrast highlighted by diag1/diag2 is stronger than ordinary one-pair fluctuation under the simple multinomial model. However it was selected after inspecting the same B500m data, so it is explicitly marked **same-data exploratory**, not independent confirmation.

## 4. Multiple-comparison check

Nine adjacent 50m pair tests were calibrated with Holm correction.

- smallest raw adjacent-pair `p = 0.0238277` (350–400m vs 400–450m)
- smallest Holm-adjusted `p = 0.2144492`
- no adjacent 50m pair survives 5% Holm correction

The five within-parent half-vs-half tests behave similarly:

- smallest raw `p = 0.0453182`
- smallest Holm-adjusted `p = 0.2265911`
- no within-parent split survives 5% Holm correction

## Interpretation

The practical conclusion changes from diag2.

The shell swings are **real exact finite counts**, but the present B500m sample does not yet distinguish cleanly between:

1. genuine arithmetic-class/family structure, and
2. multinomial-scale finite fluctuation amplified by looking across many shell boundaries.

Therefore going immediately to 25m shells would mostly reduce per-shell sample size and increase noise. The more informative next move is to condition on arithmetic classes/congruence or existing local states and ask whether the direction imbalance concentrates in specific classes.

```text
STAGE14_NUM_ALPHA11_DIAG3=MULTINOMIAL_SHELL_CALIBRATION_COMPLETE
GLOBAL_50M_HOMOGENEITY_REJECTED_AT_5PCT=false
GLOBAL_50M_PEARSON_P=0.11259722940263282
GLOBAL_100M_PARENT_HOMOGENEITY_REJECTED_AT_5PCT=true
GLOBAL_100M_PARENT_PEARSON_P=0.04181477967658976
LATE_300M_400M_VS_400M_500M_EXPLORATORY_P=0.01023661942850661
ADJACENT_50M_HOLM_ANY_REJECTED_AT_5PCT=false
WITHIN_100M_HOLM_ANY_REJECTED_AT_5PCT=false
OLD_CUMULATIVE_2PCT_GATE_USED=false
IID_ARITHMETIC_OBJECTS_CLAIM=false
STATISTICAL_MODEL_IS_CALIBRATION_ONLY=true
ASYMPTOTIC_CLAIM=false
NEXT=Stage14-num-alpha11-diag4 arithmetic-class/congruence decomposition before finer 25m shells
```
