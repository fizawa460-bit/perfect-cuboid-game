# Stage27-20-r302ah — a pointwise inverse-a unit equidistribution theorem is sufficient

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ag
SOURCE_STAGE=Stage20

After r302ag, the remaining odd inverse-`a'` fixed-power burden is the zero-mass discrepancy

```text
nu_d(lambda)
 = mu_d(lambda)-D_d/phi(m),

lambda in (Z/mZ)^x.
```

There is a concrete sufficient route that uses the same square-fiber energy already isolated for the Ramanujan term.

For one admissible coefficient slice `a_u=c_{du}`, put

```text
F_a(lambda)=sum_u a_u e_m(lambda u^2).
```

The discrepancy contribution is exactly

```text
Q_nu(a)
 = sum_{lambda in (Z/mZ)^x}
     nu_d(lambda) |F_a(lambda)|^2.
```

Hence

```text
|Q_nu(a)|
 <= ||nu_d||_infinity
    * sum_{lambda in (Z/mZ)^x}|F_a(lambda)|^2
 <= ||nu_d||_infinity
    * sum_{lambda mod m}|F_a(lambda)|^2.
```

Full additive Parseval in `lambda` gives

```text
sum_{lambda mod m}|F_a(lambda)|^2
 = m * sum_t |sum_{u:u^2=t} a_u|^2
 <= B^o(1) m
    * sum_u gcd(u,m_*)|a_u|^2,
```

using the r302z square-fiber multiplicity bound.

Therefore, if one proves the pointwise same-measure unit-fiber equidistribution estimate

```text
max_{lambda in (Z/mZ)^x}
 |mu_d(lambda)-D_d/phi(m)|
 <= B^{-eta+o(1)} D_d/phi(m)
```

for one fixed `eta>0`, then because `m/phi(m)=B^o(1)`, r302ac's subpower singular-energy adapter yields

```text
|Q_nu(a)|
 <= B^{-eta+o(1)} D_d * sum_u |a_u|^2.
```

Thus the inverse-`a'` discrepancy is closed with a fixed power and no additional coefficient norm loss.

This pointwise equidistribution theorem is sufficient, not claimed minimal. It is nevertheless much more concrete than the previous generic Kloosterman/spectral wording: it asks for relative equidistribution of the exact positive `H_phys^MAIN` inverse-`a'` pushforward among primitive odd unit classes.

No such theorem is proved here.

```text
SUFFICIENT_FIXED_POWER_LEMMA=
MAINWallInverseAUnitFiberPointwiseRelativeEquidistribution

STAGE27_20_R302AH_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
DISCREPANCY_QUADRATIC_FORM_EXACT=true
FULL_LAMBDA_PARSEVAL_MAJORANT_PROVED=true
POINTWISE_UNIT_EQUIDISTRIBUTION_SUFFICIENT=true
POINTWISE_UNIT_EQUIDISTRIBUTION_PROVED=false
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
NEXT_DERIVED_ROUTE=27-20-r302ai
NEXT_BATCH=Stage27-20-r302-main-batch
```