# Stage27-20-r302aa — charge regular odd square collisions to the same diagonal energy

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302z
SOURCE_STAGE=Stage20

For admissible frequencies r302v gives

```text
G_d(du,du)=D_d.
```

Because `G_d` is a Gram matrix, Cauchy-Schwarz gives the exact pointwise envelope

```text
|G_d(du,dv)|
 <= sqrt(G_d(du,du) G_d(dv,dv))
 = D_d
```

whenever both frequencies are admissible.

Let `u~v` denote the odd square-collision relation `u^2=v^2 (mod m)`. By symmetry and `2|xy|<=|x|^2+|y|^2`,

```text
|sum_{u!=v, u~v} c_{du} conj(c_{dv}) G_d(du,dv)|
 <= D_d * sum_u deg_m(u) |c_{du}|^2,
```

where `deg_m(u)` is the number of square-collision partners of `u` (including or excluding the diagonal changes only an absolute term already accounted for separately).

R302z proves

```text
deg_m(u) <= B^o(1) gcd(u,m_*).
```

Therefore

```text
|C_coll|
 <= B^o(1) D_d
    * sum_u gcd(u,m_*) |c_{du}|^2.
```

In particular, on the unit-frequency part `(u,m)=1`,

```text
|C_coll,unit|
 <= B^o(1) D_d * sum_{(u,m)=1}|c_{du}|^2.
```

Thus regular/unit odd square collisions require **no second fixed-power theorem** beyond the coefficient-specific diagonal product deficit: once `D_d` times the relevant admissible Fourier energy is power-small, the unit-collision contribution is paid at only `B^o(1)` extra cost.

The only collision residue not automatically absorbed this way is the singular weighted moment

```text
sum_u gcd(u,m_*) |c_{du}|^2.
```

No bound strong enough for that singular moment is proved here.

```text
FIRST_MISSING_LEMMA=
MAINWallPrimitiveSingularSquareCollisionWeightedFourierEnergyControl

STAGE27_20_R302AA_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
GRAM_CAUCHY_COLLISION_ENVELOPE_PROVED=true
UNIT_COLLISION_PAID_BY_DIAGONAL_UP_TO_SUBPOWER=true
INDEPENDENT_UNIT_COLLISION_SAVING_REQUIRED=false
SINGULAR_COLLISION_WEIGHTED_ENERGY_CONTROL_PROVED=false
NONZERO_SQUARED_FREQUENCY_DEFICIT_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302ab
NEXT_BATCH=Stage27-20-r302-main-batch
```