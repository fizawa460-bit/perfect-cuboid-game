# Stage27-20-r302af — subtract the uniform primitive unit measure and isolate Ramanujan main term plus discrepancy

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ae
SOURCE_STAGE=Stage20

R302x-ad show that, on the odd primitive modulus `m=q'_odd`, the Gram phase is controlled by

```text
lambda = inverse(4a') (mod m),
phase = e_m(-lambda (u^2-v^2))
      = e_m(-lambda r s).
```

Because `(a',m)=1`, the inverse coordinate `lambda` ranges in the unit group `(Z/mZ)^x`, not in all residues. Fix the retained 2-primary local data and push the positive same-measure amplitude `|A_d(x)|^2 dH_phys^MAIN(x)` to this odd unit coordinate. Let `mu_d(lambda)` be the resulting positive pushforward and

```text
D_d = sum_{lambda in (Z/mZ)^x} mu_d(lambda).
```

Decompose it exactly against the uniform **unit-group** measure:

```text
mu_d(lambda)
 = D_d/phi(m) + nu_d(lambda),

sum_{lambda in (Z/mZ)^x} nu_d(lambda)=0.
```

For `h=u^2-v^2`, the uniform unit component contributes the Ramanujan sum

```text
D_d * c_m(h)/phi(m),

c_m(h)
 = sum_{lambda in (Z/mZ)^x} e_m(-lambda h).
```

Writing `g=(m,h)`, the classical exact formula is

```text
c_m(h)
 = mu(m/g) * phi(m) / phi(m/g),
```

with the convention that the expression is zero when the Möbius factor vanishes. Thus

```text
c_m(0)/phi(m)=1,
```

while for nonzero `h` the uniform primitive main term may already be small when `m/g` is large. It is **not** correct to replace the unit-group average by full-residue orthogonality and declare every noncollision term zero.

The remaining contribution is the zero-mass unit-group discrepancy

```text
nu_hat_d(h)
 = sum_{lambda in (Z/mZ)^x}
     nu_d(lambda)e_m(-lambda h).
```

Hence every odd Gram phase splits exactly into

```text
uniform Ramanujan main term
+
physical inverse-a unit-distribution discrepancy.
```

The `h=0` square-collision branch is still the full uniform main term and remains routed through r302y-ac. For `h!=0`, both the normalized Ramanujan factor and the discrepancy must be accounted for; neither is silently discarded.

No fixed-power discrepancy theorem and no global Ramanujan-main-term summation estimate are proved here.

```text
FIRST_MISSING_LEMMAS=
MAINWallRamanujanMainTermShearedCoefficientControl,
MAINWallInverseAUnitPushforwardDiscrepancyAgainstActualShearedCoefficientClass

STAGE27_20_R302AF_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
UNIFORM_PRIMITIVE_UNIT_SUBTRACTION_EXACT=true
FULL_RESIDUE_ORTHOGONALITY_MISUSED=false
RAMANUJAN_MAIN_TERM_EXPOSED=true
ZERO_MASS_UNIT_DISCREPANCY_EXPOSED=true
RAMANUJAN_MAIN_TERM_DEFICIT_PROVED=false
INVERSE_A_DISCREPANCY_DEFICIT_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
FINE_BLOCK_MULTIPLICITY_SUBPOWER_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302ag
NEXT_BATCH=Stage27-20-r302-main-batch
```