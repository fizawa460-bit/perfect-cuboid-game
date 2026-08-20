# Stage27-20-r302ak — odd inverse-a needs only subpower unit-fiber nonconcentration once the diagonal supplies the fixed power

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302aj
SOURCE_STAGE=Stage20

R302ah records a strong sufficient theorem with a fixed-power relative error for the odd inverse-`a'` unit pushforward. That strength is unnecessary once the diagonal product itself is the source of the fixed power.

Fix one primitive 2-primary local coordinate and retain it as part of the coefficient/physical data. On the odd primitive unit group let

```text
mu_{d,tau}(lambda)>=0,
D_{d,tau}=sum_{lambda in (Z/mZ)^x} mu_{d,tau}(lambda).
```

For the corresponding actual odd-coordinate coefficient slice `a_{tau,u}`, put

```text
F_{tau}(lambda)=sum_u a_{tau,u} e_m(lambda u^2).
```

The odd inverse-`a'` contribution on this fixed local slice is

```text
Q_{mu,tau}
 = sum_{lambda in (Z/mZ)^x}
     mu_{d,tau}(lambda)|F_tau(lambda)|^2.
```

Assume only the relative pointwise subpower nonconcentration

```text
max_lambda mu_{d,tau}(lambda)
 <= B^{o(1)} D_{d,tau}/phi(m).
```

Then additive Parseval plus the odd square-fiber bound gives

```text
Q_{mu,tau}
 <= B^{o(1)} D_{d,tau}
    * sum_u gcd(u,m_*)|a_{tau,u}|^2.
```

Thus, on every fixed 2-primary local slice, a fixed-power relative discrepancy is unnecessary: odd inverse-`a'` only needs a zero-fixed-power-loss density bound, provided the corresponding singular square-fiber energy is also controlled at subpower cost.

This card deliberately does **not** infer the full primitive quadratic form by summing over 2-primary slices with an unproved zero-loss recombination. The exact 2-primary phase can couple many local coefficient coordinates, and a naive slice count may be polynomial. The next route globalizes the argument on the joint primitive unit group instead of charging the number of 2-primary slices.

```text
FIRST_MISSING_ODD_LOCAL_LEMMA=
MAINWallOddInverseAUnitFiberSubpowerNonconcentration

STAGE27_20_R302AK_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
FIXED_POWER_ODD_INVERSE_A_EQUIDISTRIBUTION_REQUIRED=false
ODD_SUBPOWER_UNIT_FIBER_NONCONCENTRATION_SUFFICIENT_SLICEWISE=true
FULL_TWO_PRIMARY_RECOMBINATION_PROVED=false
SEPARATE_OFFDIAGONAL_FIXED_POWER_REQUIRED_ON_ODD_SLICE=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
PROJECTED_FINE_BLOCK_MULTIPLICITY_SUBPOWER_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302al
NEXT_TARGET=GLOBALIZE_TO_JOINT_ODD_AND_TWO_PRIMARY_PRIMITIVE_UNIT_PUSHFORWARD
NEXT_BATCH=Stage27-20-r302-main-batch
```