# Stage14-numα11-diag4 — arithmetic-class / inert-congruence decomposition

## Result

This stage reuses the merged exact `B=500,000,000` two-face census (`3495` objects, `(a,b,c)=(1374,1371,750)`) and asks whether the shell-local direction movement seen in diag1/diag2 is concentrated in simple arithmetic classes.

No new census is performed. The panel was fixed before reading the diag4 output: parity/geometry classes plus Stage13-motivated inert-prime classes for `p=7,11,19,23`. Pearson direction-by-class tests use only partitions whose minimum expected cell is at least 5, followed by one Holm correction across the 19 eligible partitions.

As in diag3, these p-values are **finite calibration only**. The arithmetic objects are deterministic and are not asserted to be IID samples.

## 1. A real p=7 divisibility/direction association appears

The strongest predeclared partition is whether the **shared edge of the two integral faces is divisible by 7**.

Class-by-direction counts `(a,b,c)` are

```text
7 ∤ shared edge : (616,492,274), total 1382
7 | shared edge : (758,879,476), total 2113
```

The corresponding within-class direction ratios are approximately

```text
7 ∤ shared edge : (0.44573,0.35601,0.19826)
7 | shared edge : (0.35873,0.41600,0.22527)
```

Calibration statistics:

```text
Pearson p          = 1.68143055755694e-06
Holm-adjusted p    = 3.194718059358186e-05
Cramer's V         = 0.0872267549763834
```

Thus the simple common-direction law is rejected for this partition even after the predeclared multiple-comparison correction. The effect is not huge, but it is clearly larger than the other tested congruence classes.

A second `p=7` partition also survives Holm correction: the number of nonshared edges divisible by 7.

```text
zero-count 0 : (210,215,168)
zero-count 1 : (1046,1062,520)
zero-count 2 : (118,94,62)

raw p   = 7.818805862508911e-05
Holm p  = 0.001407385055251604
V       = 0.05865229336839496
```

So there is a genuine finite `p=7` divisibility signature in the two-face directional population.

## 2. But this does not explain the 300–400m -> 400–500m shell jump

For each of the 22 predeclared partitions, diag4 pooled the class-specific direction laws over `300m<d<=500m`, changed only the class mixture between the two 100m shells, and asked how much of the observed direction shift that mixture alone reconstructs.

Observed late-shell shift:

```text
Ra : +0.0701827243
Rb : +0.0264463982
Rc : -0.0966291224
L2 :  0.1223201294
```

The best tested mixture explanation is only `p19_nonshared_zero_count`:

```text
mixture explained fraction (L2) = 0.0342814300
shift cosine alignment           = 0.8680136356
```

So even the best tested arithmetic-class mixture accounts for only about **3.4%** of the late-shell movement in this descriptive decomposition. The strong global `p=7` direction association is therefore not the cause of the observed 300–500m shell swing.

```text
LATE_SHELL_SHIFT_FULLY_EXPLAINED_BY_TESTED_CLASS_MIXTURE=false
```

This is the main routing result of diag4: finer 25m shells are still not the useful next move, but the unexplained movement should now be tested for **family/cluster dependence**, especially repeated space diagonals / representation multiplicity.

## 3. p=7 is locally special for the *remaining third face*

For each exactly-two object, the missing face sum was tested for membership in `QR_0(F_p)`.

Observed B500m pass rates are

```text
p=3   3495/3495 = 1.000000
p=7   3495/3495 = 1.000000
p=11  2699/3495 = 0.772246
p=19  1609/3495 = 0.460372
p=23  2232/3495 = 0.638627
```

The `p=7` all-pass result is not merely a B500m accident. An exhaustive finite-field audit over the physical two-face local universe

```text
x^2+y^2 in QR_0
x^2+z^2 in QR_0
x^2+y^2+z^2 in QR \ {0}
```

finds:

```text
p=3   missing-face QR_0: 6/6     = 1
p=7   missing-face QR_0: 54/54   = 1
p=11  missing-face QR_0: 150/190 = 15/19
p=19  missing-face QR_0: 486/918 = 9/17
p=23  missing-face QR_0: 1078/1606 = 49/73
```

Therefore, at `p=7`, once the two displayed faces and a unit square space diagonal exist modulo 7, the third face is automatically a quadratic residue modulo 7. This is an exact **finite-field local fact**, not a claim of global third-face integrality.

It also means two different `p=7` facts must not be conflated:

1. the missing-third-face `QR_0` test is locally vacuous at `p=7` after conditioning on the two-face state;
2. the **divisibility state of the shared/nonshared edges mod 7** still carries a measurable direction association in the B500m exact population.

The Stage13 value `lambda_7=3/4` belongs to a different conditioning problem (one-face -> additional face) and is not used as a null expectation here.

## Interpretation

Diag4 finds arithmetic structure, but not the structure that generated the late shell jump.

- `p=7` divisibility classes are direction-associated after Holm correction.
- ordinary diagonal residue / parity partitions do not dominate the signal.
- the remaining-third-face `QR_0` test is forced at `p=3,7` in the finite-field two-face local universe.
- none of the tested class-mixture shifts materially reconstructs the 300–400m -> 400–500m direction jump.

The next diagnostic should therefore move one level above single-object congruence and test **dependence/clustering by common space diagonal and representation family**.

```text
STAGE14_NUM_ALPHA11_DIAG4=ARITHMETIC_CLASS_AND_LOCAL_CONGRUENCE_DECOMPOSITION_COMPLETE
SOURCE_B500M_ROWS=3495
PREDECLARED_PARTITIONS=22
INFERENTIAL_ELIGIBLE_PARTITIONS=19
HOLM_CORRECTED_DIRECTION_ASSOCIATION_FOUND=true
STRONGEST_PARTITION=p7_shared_divisible
STRONGEST_PARTITION_HOLM_P=3.194718059358186e-05
STRONGEST_PARTITION_CRAMERS_V=0.0872267549763834
P7_MISSING_THIRD_FACE_QR0_FORCED_IN_FINITE_FIELD_TWO_FACE_LOCAL_UNIVERSE=true
LATE_SHELL_SHIFT_BEST_TESTED_MIXTURE_EXPLAINED_FRACTION_L2=0.0342814300399743
LATE_SHELL_SHIFT_FULLY_EXPLAINED_BY_TESTED_CLASS_MIXTURE=false
FINER_25M_SHELLS_RECOMMENDED_NEXT=false
IID_ARITHMETIC_OBJECTS_CLAIM=false
ASYMPTOTIC_CLAIM=false
NEXT=Stage14-num-alpha11-diag5 family/cluster dependence and same-diagonal multiplicity diagnostics
```
