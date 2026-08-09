# Stage14-numα11-diag5 — family / cluster dependence diagnostic

## Result

This stage reuses the merged exact `B=500,000,000` exactly-two census (`3495` objects) and asks whether the shell-local direction movement found in diag1–diag3 is an artifact of dependent arithmetic families.

Two cluster notions were fixed before reading the diag5 output:

1. **same space diagonal `d`**;
2. **connected component of the primitive oriented-face graph** already frozen by Stage14-num (`3495` edges, `5082` vertices, maximum degree `13`).

The answer is negative for both tested notions: clustering exists, especially in the face graph, but it does not attenuate the `300m–400m -> 400m–500m` directional shift when groups are equal-weighted.

## 1. Same-space-diagonal clusters are sparse

The `3495` objects occupy `3325` distinct space diagonals.

```text
multiplicity 1: 3159 diagonals
multiplicity 2:  162 diagonals
multiplicity 3:    4 diagonals
maximum multiplicity: 3
```

Thus `90.3863%` of objects are on singleton diagonals and only `9.6137%` belong to repeated-`d` clusters.

Within the `174` same-`d` object pairs, `56` have the same direction. Under the fixed-global-label shuffle moment calibration the expectation is `61.6479`; the standardized deviation is only

```text
z = -0.8958
normal two-sided calibration p = 0.37035
```

so there is no evidence here that direction labels are unusually concentrated inside equal-`d` clusters. This is a calibration statement only; the arithmetic objects are not claimed IID.

Most importantly, equalizing the weight of each represented `d` does **not** reduce the late-shell jump:

```text
object-weighted late shift L2 = 0.1223201
equal-d late shift L2         = 0.1239583
ratio                           = 1.01339
```

The simple same-`d` multiplicity-bin mixture explains essentially none of the shift (`explained_fraction_L2 = -0.00468`).

## 2. Primitive-face graph families are real but also do not explain the jump

The frozen exactly-two graph decomposes into `1703` connected components. There are large historical families: the largest component contains `95` exactly-two objects, and `65.92%` of all objects lie in non-singleton components.

However the repeated components are usually **direction-mixed**, not single-direction bursts:

```text
repeated components                         = 512
repeated components with >=2 directions    = 452
fraction                                    = 88.28125%
```

Across the `18,915` within-component object pairs, the same-direction fraction is `0.35934` versus fixed-label-shuffle expectation `0.35430`:

```text
z = 0.79899
normal two-sided calibration p = 0.42430
```

Again there is no material directional over-clustering under this calibration.

The late shells are also not dominated by one large component. In `(300m,400m]`, the largest represented component contributes only `5/328 = 1.52%`; in `(400m,500m]` the maximum is `6/301 = 1.99%`. The top five components contribute only about `6.10%` and `5.65%`, respectively.

Equal-component weighting actually makes the late directional shift slightly larger:

```text
object-weighted late shift L2 = 0.1223201
equal-component late shift L2 = 0.1336350
ratio                           = 1.09250
```

Component-size mixture likewise explains essentially none of the jump (`explained_fraction_L2 = -0.00384`). Therefore the previously observed shell movement is not plausibly a simple consequence of a few high-multiplicity graph families changing their shell weights.

## 3. The diag4 p=7 signature survives cluster controls

Diag4 found that `7 | shared edge` is associated with direction. Diag5 checks whether that was merely a repeated-diagonal / large-component artifact.

Raw object-weighted `7 | shared` rates are

```text
a: 0.55167
b: 0.64114
c: 0.63467
```

Equal-`d` rates remain

```text
a: 0.55070
b: 0.63916
c: 0.63405
```

and equal face-component rates remain

```text
a: 0.52033
b: 0.61388
c: 0.63295
```

so the same `a`-low versus `b/c`-high ordering survives both reweightings.

The same-data subset calibrations also show the signal in the `3159` singleton-`d` objects (`p=1.65e-5`) and separately in both isolated face components (`p=9.73e-4`) and nontrivial face components (`p=2.68e-4`). The repeated-`d` subset alone has only `336` rows and gives `p=0.0722`; it is not an independent confirmation or contradiction.

Thus cluster concentration does not account for the p=7 signature found in diag4.

## Interpretation

The natural dependence explanations tested so far have now been weakened in sequence:

- diag3: ordinary multinomial finite fluctuation remains possible at 50m resolution;
- diag4: simple parity / inert-prime class mixtures do not explain the late shift;
- diag5: same-`d` multiplicity and connected primitive-face families do not explain it either.

This still does **not** prove a changing asymptotic direction law. The late contrast was identified from the same finite `B500m` dataset, and all statistical tails here are calibration devices rather than probability models for deterministic arithmetic objects.

The useful next move is not a noisier `25m` partition. `diag6` should settle which finite observable is most stable (object-weighted cumulative, shell-local, equal-family, or conditioned) and then compare Stage13 exactly-one and Stage14 exactly-two under **matched cutoff and shell conventions**.

```text
STAGE14_NUM_ALPHA11_DIAG5=FAMILY_CLUSTER_DEPENDENCE_DIAGNOSTIC_COMPLETE
SOURCE_B500M_ROWS=3495
SAME_DIAGONAL_GROUPS=3325
SAME_DIAGONAL_MAX_MULTIPLICITY=3
SAME_DIAGONAL_REPEATED_OBJECT_FRACTION=0.096137339055794
SAME_DIAGONAL_DIRECTION_CLUSTER_Z=-0.8958133367908503
SAME_DIAGONAL_EQUAL_WEIGHT_LATE_SHIFT_RATIO=1.0133921901483236
FACE_GRAPH_COMPONENTS=1703
FACE_GRAPH_MAX_COMPONENT_OBJECTS=95
FACE_GRAPH_REPEATED_COMPONENT_MULTI_DIRECTION_FRACTION=0.8828125
FACE_GRAPH_DIRECTION_CLUSTER_Z=0.7989898907161457
FACE_GRAPH_EQUAL_WEIGHT_LATE_SHIFT_RATIO=1.09250237451836
LATE_SHIFT_ATTENUATED_BY_TESTED_CLUSTER_REWEIGHTING=false
P7_SHARED_DIVISIBILITY_PATTERN_SURVIVES_EQUAL_D_WEIGHTING=true
P7_SHARED_DIVISIBILITY_PATTERN_SURVIVES_EQUAL_COMPONENT_WEIGHTING=true
FINER_25M_SHELLS_RECOMMENDED_NEXT=false
IID_ARITHMETIC_OBJECTS_CLAIM=false
ASYMPTOTIC_CLAIM=false
NEXT=Stage14-num-alpha11-diag6 matched Stage13 exactly-one vs Stage14 exactly-two observable comparison
```
