# Stage27-20-r302q — isolate the diagonal normalization ratio before spectral work

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302p
SOURCE_STAGE=Stage20

R302p shows that the mandatory all-`c` Gram diagonal cannot obtain a saving from inverse-frequency phase cancellation. The next exact diagnostic is the dimensionless ratio

```text
theta_diag(packet,d)
 = sup_{b:d|b} G_d(b,b) / E_packet.
```

Because `G_d` is positive semidefinite,

```text
||G_d||op >= sup_b G_d(b,b),
```

so the r302m all-`c` operator receiver can hold with a fixed power only if

```text
sup_{packet,d} theta_diag(packet,d)
 <= B^{-2delta_diag+o(1)}
```

for some fixed `delta_diag>0`.

This gives a strict ordering rule for the continuation: no off-diagonal spectral theorem can close the strengthened all-`c` receiver until the single-frequency normalization ratio is shown power-small. If `theta_diag` is instead of order `B^{o(1)}` on some retained packets, the all-`c` operator-norm strengthening is too strong for those packets, even though the original Stage27 physical correlation could still conceivably be small for its special Fourier coefficient vector.

Accordingly there are two legal branches:

1. **Uniform-operator branch.** Prove the r302p single-frequency physical energy deficit and then attack `||G_d-diag(G_d)||op`.
2. **Coefficient-specific branch.** If uniform diagonal saving is unavailable, return to the exact original coefficient vector `c_b=W_hat(b)/q` and prove that its Fourier energy avoids the large-diagonal modes strongly enough to recover a fixed power. This requires a new adapter; merely subtracting a baseline inside the all-`c` theorem is still invalid.

The exact Parseval and weak-`L2` statements from StructureRadar batch34 control the size distribution of `c_b`, but by themselves do not correlate large `|c_b|` with small `G_d(b,b)`. Therefore they do not yet discharge branch 2.

FIRST_MISSING_LEMMA=MAINWallPrimitiveInverseFrequencyDiagonalNormalizationOrActualCoefficientAvoidance

STAGE27_20_R302Q_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
DIAGONAL_NORMALIZATION_RATIO_DEFINED=true
ALL_C_OPERATOR_DEFICIT_REQUIRES_UNIFORM_DIAGONAL_POWER=true
OFFDIAGONAL_SPECTRAL_THEOREM_CAN_RESCUE_FULL_DIAGONAL=false
ACTUAL_COEFFICIENT_FALLBACK_LOGICALLY_AVAILABLE=true
ACTUAL_COEFFICIENT_AVOIDS_BAD_DIAGONAL_MODES_PROVED=false
UNIFORM_DIAGONAL_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302r
NEXT_BATCH=Stage27-20-r302-main-batch
