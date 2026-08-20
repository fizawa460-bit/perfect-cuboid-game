# Stage27-20-r302ad — shear the odd squared-frequency phase to a bilinear product

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ac
SOURCE_STAGE=Stage20

The genuinely oscillatory branch from r302y has odd phase

```text
e_m(-inverse(4a') * (u^2-v^2)),
m=q'_odd.
```

Because `m` is odd, `2` is invertible modulo `m`. On the odd residue coordinates make the exact linear change

```text
r = u-v,
s = u+v,

u = (s+r)/2,
v = (s-r)/2.
```

This is a bijection on `(Z/mZ)^2`, and

```text
u^2-v^2 = r s.
```

Hence the odd primitive phase becomes

```text
e_m(-inverse(4a') * r s).
```

The 2-primary coordinates and their exact primitive phase ratio remain attached as separate local data; no claim is made that they can be discarded or summed at zero cost.

The actual coefficient pair is transported to the sheared matrix

```text
C_d(r,s)
 = c_{d(s+r)/2} conj(c_{d(s-r)/2})
```

on the odd coordinates, together with the exact admissibility and 2-primary masks. Thus the noncollision branch is not merely a generic quadratic phase: it is an **inverse-`a'` bilinear-product phase** with a very specific sheared rank-one-origin coefficient matrix.

This is the closest exact normal form reached so far to the Kloosterman-fraction/trilinear engines catalogued by StructureRadar. It still does not establish applicability of those theorems, because their separated-coefficient/range hypotheses are not automatically satisfied by the sheared matrix `C_d(r,s)` and the same `H_phys^MAIN` common-parent weights remain attached.

The restart point is therefore sharpened to

```text
FIRST_MISSING_LEMMA=
MAINWallInverseABilinearProductShearedCoefficientSameMeasureDeficit
```

No fixed-power estimate is proved here.

```text
STAGE27_20_R302AD_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
ODD_LINEAR_SHEAR_BIJECTION_PROVED=true
SQUARED_DIFFERENCE_TO_PRODUCT_PHASE_PROVED=true
SHEARED_ACTUAL_COEFFICIENT_MATRIX_EXACT=true
TWO_PRIMARY_DATA_RETAINED=true
EXTERNAL_KLOOSTERMAN_THEOREM_APPLICABILITY_PROVED=false
SHEARED_COEFFICIENT_SAME_MEASURE_DEFICIT_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
FINE_BLOCK_MULTIPLICITY_SUBPOWER_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302ae
NEXT_BATCH=Stage27-20-r302-main-batch
```