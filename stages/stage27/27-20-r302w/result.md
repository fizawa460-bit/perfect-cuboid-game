# Stage27-20-r302w — collapse the diagonal bad-mode receiver to one admissible-class product

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302v
SOURCE_STAGE=Stage20

R302v proves that on one fixed packet and gcd stratum

```text
G_d(b,b)=1_{b in Adm_d} D_d.
```

Therefore the exact coefficient-specific diagonal contribution is

```text
sum_b |c_b|^2 G_d(b,b)
 = D_d * sum_{b in Adm_d} |c_b|^2.
```

Define the admissible Fourier-energy fraction

```text
theta_d
 = (sum_{b in Adm_d}|c_b|^2)
   /(sum_{b:d|b}|c_b|^2),
```

with `theta_d=0` when the denominator vanishes. Then the diagonal receiver is exactly

```text
(D_d/E_packet) * theta_d
 <= B^{-2 delta_diag+o(1)}.
```

This is the minimal coefficient-specific diagonal target after primitive completion. It has two possible sources of a fixed power:

1. the scalar physical/normalization factor `D_d/E_packet` is power-small; or
2. the exact Fourier vector has power-small energy on the locally admissible class.

The second possibility is not obtained merely from the size of `Adm_d`. On the odd primitive factor all frequencies are locally admissible; on the 2-primary factor the admissibility condition is only a bounded local parity restriction. Such a bounded local exclusion yields at most a constant-factor reduction by cardinality and cannot by itself create a `B^{-eta}` saving. A fixed-power saving in `theta_d` would therefore require genuine structure of the actual physical coefficient `W`, not generic local counting.

Accordingly the arbitrary threshold set `Bad_d(gamma)` from r302s is no longer the canonical diagonal restart point for the exact primitive kernel. The sharper receiver is

```text
FIRST_MISSING_LEMMA=
MAINWallPrimitiveInverseFrequencyAdmissibleClassDiagonalEnergyProductDeficit
```

namely prove, uniformly over retained packets and gcd strata, one fixed `delta_diag>0` such that

```text
(D_d/E_packet) * theta_d
 <= B^{-2 delta_diag+o(1)}.
```

No such power is proved here.

```text
STAGE27_20_R302W_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
BAD_MODE_THRESHOLD_RECEIVER_SUPERSEDED_AS_CANONICAL_DIAGONAL_TARGET=true
ADMISSIBLE_CLASS_DIAGONAL_PRODUCT_IDENTITY_PROVED=true
LOCAL_ADMISSIBILITY_CARDINALITY_ALONE_GIVES_FIXED_POWER=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
ACTUAL_COEFFICIENT_OFFDIAGONAL_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302x
NEXT_BATCH=Stage27-20-r302-main-batch
```