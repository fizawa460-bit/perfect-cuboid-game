# Stage27-20-r302x — expose the exact squared-frequency phase-difference Gram kernel

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302w
SOURCE_STAGE=Stage20
STRUCTURE_RADAR_SOURCE=SR-GATE-33A-169,SR-GATE-34-169,SR-GATE-36A-169

R302v gives, on a fixed packet and gcd stratum,

```text
K_d(x,b)=1_{b in Adm_d} A_d(x) psi_d(x,b),
|psi_d(x,b)|=1.
```

Therefore

```text
G_d(b,b')
 = 1_{b,b' in Adm_d}
   integral |A_d(x)|^2
     psi_d(x,b) conj(psi_d(x,b'))
   dH_phys^MAIN(x).
```

The odd primitive Gauss factor makes the phase difference explicit. Write

```text
q'=q/d,
m=q'_odd,
u=b/d,
v=b'/d.
```

Then the odd component of the primitive phase ratio is exactly

```text
e_m(-inverse(4a') * (u^2-v^2)).
```

The primitive 2-primary factor is kept as its exact bounded unit phase ratio on the admissible parity class; no parity-free simplification is imposed.

Thus, after pushing the positive weight `|A_d(x)|^2 dH_phys^MAIN(x)` through the inverse-`a'` coordinate on the odd part, every off-diagonal Gram entry is a same-measure Fourier coefficient at the **squared-frequency difference**

```text
h = u^2-v^2 (mod m),
```

with the exact 2-primary local multiplier retained.

Schematically, but without changing the measure,

```text
G_d(b,b')
 = 1_{b,b' in Adm_d}
   integral Xi_{2,d}(x;b,b')
     e_m(-inverse(4a'(x)) * h)
   dmu_d(x),

dmu_d(x)=|A_d(x)|^2 dH_phys^MAIN(x).
```

This is a stricter description than the generic phrase “Kloosterman/spectral off-diagonal correlation”: the only odd-part frequency presented to the inverse-`a'` physical measure is `u^2-v^2`. Any future theorem must control this exact pushforward with the existing common-parent weights and masks, rather than an unrelated complete Kloosterman matrix.

No decay of these Fourier coefficients is proved here.

```text
FIRST_MISSING_LEMMA=
MAINWallPrimitiveInverseASquaredFrequencyPushforwardCorrelationDeficit

STAGE27_20_R302X_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
SQUARED_FREQUENCY_PHASE_DIFFERENCE_EXPOSED=true
SAME_H_PHYS_MAIN_PUSHFORWARD_PRESERVED=true
TWO_PRIMARY_LOCAL_PHASE_RETAINED=true
PUSHFORWARD_FOURIER_DECAY_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302y
NEXT_BATCH=Stage27-20-r302-main-batch
```