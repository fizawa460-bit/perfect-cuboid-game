# Stage27-20-r302y — split odd squared-frequency collisions from genuine inverse-a oscillation

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302x
SOURCE_STAGE=Stage20

R302x exposes the odd primitive phase difference

```text
h=u^2-v^2 (mod m),
m=q'_odd.
```

This forces a structural split inside the off-diagonal form. Define

```text
Coll_d
 = {(u,v): u!=v, u^2=v^2 (mod m)},
Osc_d
 = {(u,v): u!=v, u^2!=v^2 (mod m)}.
```

For `(u,v) in Coll_d`, the odd inverse-`a'` phase is identically `1` for every retained physical point. Therefore **odd-part** Kloosterman/Kuznetsov/inverse-frequency cancellation cannot control this branch. The exact primitive 2-primary phase ratio remains present and may still oscillate; it is not discarded or declared harmless.

For `(u,v) in Osc_d`, the odd part has a genuinely nonzero squared-frequency label and remains a legitimate target for same-measure inverse-`a'` Fourier decay.

Thus the coefficient-specific off-diagonal receiver separates into

```text
C_coll
 = sum_{(u,v) in Coll_d} c_{du} conj(c_{dv}) G_d(du,dv),

C_osc
 = sum_{(u,v) in Osc_d} c_{du} conj(c_{dv}) G_d(du,dv).
```

A theorem controlling only nonzero odd inverse-frequency modes is insufficient unless `C_coll` is also bounded. Conversely, any collision estimate must not be multiplied as a second independent saving if it is already paid by the same diagonal physical-energy deficit.

This split is exact and changes no charged measure.

```text
FIRST_MISSING_LEMMAS=
MAINWallPrimitiveSquaredFrequencyCollisionContributionControl,
MAINWallPrimitiveNonzeroSquaredFrequencySameMeasureCorrelationDeficit

STAGE27_20_R302Y_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
ODD_SQUARED_FREQUENCY_COLLISION_SPLIT_PROVED=true
ODD_PHASE_CANCELLATION_AVAILABLE_ON_COLLISIONS=false
TWO_PRIMARY_COLLISION_PHASE_DISCARDED=false
COLLISION_CONTRIBUTION_DEFICIT_PROVED=false
NONZERO_SQUARED_FREQUENCY_DEFICIT_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302z
NEXT_BATCH=Stage27-20-r302-main-batch
```