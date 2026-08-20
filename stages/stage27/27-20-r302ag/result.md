# Stage27-20-r302ag — absorb the uniform primitive Ramanujan matrix into the same singular square-fiber energy

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302af
SOURCE_STAGE=Stage20

R302af exposes the normalized uniform-unit kernel

```text
R_m(u,v)
 = c_m(u^2-v^2)/phi(m)
 = (1/phi(m))
   sum_{lambda in (Z/mZ)^x}
     e_m(lambda(u^2-v^2)).
```

This entire Ramanujan matrix, not only its `u^2=v^2` entries, has an exact positive quadratic-form representation:

```text
sum_{u,v} a_u conj(a_v) R_m(u,v)
 = (1/phi(m))
   sum_{lambda in (Z/mZ)^x}
     |sum_u a_u e_m(lambda u^2)|^2.
```

Enlarge the nonnegative unit sum to all `lambda mod m` and use finite Parseval in `lambda`:

```text
<= (m/phi(m))
   sum_{t mod m}
     |sum_{u: u^2=t mod m} a_u|^2.
```

For each square fiber, Cauchy gives

```text
|sum_{u: u^2=t} a_u|^2
 <= #(u:u^2=t)
    * sum_{u:u^2=t}|a_u|^2.
```

The square-fiber size at `u` is exactly the collision degree studied in r302z, hence

```text
#(v:v^2=u^2 mod m)
 <= B^o(1) gcd(u,m_*).
```

Also `m/phi(m)=B^o(1)` on the existing polynomial-height range. Therefore

```text
sum_{u,v} a_u conj(a_v) R_m(u,v)
 <= B^o(1)
    sum_u gcd(u,m_*) |a_u|^2.
```

Apply this with the actual admissible coefficient slice `a_u=c_{du}`. The uniform primitive unit-group contribution to the Gram quadratic form is therefore controlled by **the same singular weighted Fourier energy** already reduced in r302ab-ac to nested physical coset energy.

Consequently no independent fixed-power theorem is needed for the Ramanujan main term. If the r302ac subpower block-multiplicity adapter holds, the uniform-unit component costs only `B^o(1)` times the coefficient-specific diagonal scale and is paid by the diagonal fixed-power deficit.

The only genuinely new fixed-power analytic burden on the odd inverse-`a'` side is now the zero-mass physical discrepancy `nu_d` from r302af.

```text
FIRST_MISSING_FIXED_POWER_OFFDIAGONAL_LEMMA=
MAINWallInverseAUnitPushforwardDiscrepancyAgainstActualShearedCoefficientClass

STAGE27_20_R302AG_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
RAMANUJAN_MATRIX_POSITIVE_FORM_IDENTITY_PROVED=true
UNIT_TO_FULL_FREQUENCY_PARSEVAL_MAJORANT_PROVED=true
RAMANUJAN_MAIN_TERM_REDUCED_TO_SINGULAR_WEIGHTED_ENERGY=true
INDEPENDENT_RAMANUJAN_FIXED_POWER_REQUIRED=false
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
NEXT_DERIVED_ROUTE=27-20-r302ah
NEXT_BATCH=Stage27-20-r302-main-batch
```