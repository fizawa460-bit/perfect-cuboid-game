# Stage27-20-r302al — joint odd/2-primary primitive unit pushforward removes slice-count loss

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ak
SOURCE_STAGE=Stage20
STRUCTURE_RADAR_SOURCE=SR-GATE-34-169

R302ak shows that the odd inverse-`a'` coordinate needs only subpower nonconcentration on a fixed 2-primary slice, but does not charge a potentially polynomial number of slices. The exact primitive 2-primary completion from StructureRadar allows the two local coordinates to be treated jointly instead.

Write the descended primitive modulus as

```text
q'=q/d=2^nu m,
m odd,
(a',q')=1.
```

## 1. Exact primitive phase labels

On the odd local factor put

```text
y_odd = b' * inverse(2) (mod m),
b'=b/d,
```

so the completed odd phase is

```text
e_m(-a'_odd^{-1} y_odd^2).
```

For `nu>=2`, primitive 2-adic completion forces `b'` even. Put

```text
y_2=b'/2 (mod 2^{nu-1}),
```

and the 2-primary phase is exactly

```text
e_{2^nu}(-a'_2^{-1} y_2^2).
```

For `nu=1`, the admissible class is `b'` odd and the primitive mod-2 factor is a fixed nonzero local factor with no nontrivial unit coordinate. For `nu=0` there is no 2-primary coordinate.

Thus for `nu>=2` the admissible frequencies are in bijection with

```text
(y_2 mod 2^{nu-1}, y_odd mod m),
```

while for `nu<=1` only the odd coordinate is nontrivial after the exact parity restriction.

## 2. Joint positive primitive-unit pushforward

Push the same positive physical amplitude `|A_d(x)|^2 dH_phys^MAIN(x)` through the joint inverse-unit coordinate

```text
(lambda_2,lambda_odd)
 = (a'_2^{-1},a'_odd^{-1})
```

when `nu>=2`, and through `lambda_odd` alone when `nu<=1`. Denote the resulting positive mass by `mu_d` and its total mass by `D_d`.

A sufficient zero-fixed-power-loss hypothesis is the joint pointwise nonconcentration

```text
max mu_d
 <= B^{o(1)} D_d / |U_d|,
```

where

```text
|U_d| = phi(m)                         if nu<=1,
|U_d| = phi(2^nu) phi(m)              if nu>=2.
```

No factor equal to the number of 2-primary slices is introduced.

## 3. Joint additive Parseval

For `nu>=2`, with `a_y` the exact admissible coefficient vector in the `(y_2,y_odd)` coordinates, define

```text
F(lambda_2,lambda_odd)
 = sum_y a_y
   e_{2^nu}(lambda_2 y_2^2)
   e_m(lambda_odd y_odd^2).
```

Enlarging the nonnegative unit sum to all additive coordinates and applying two-dimensional finite Parseval gives

```text
sum_{lambda_2 mod 2^nu}
 sum_{lambda_odd mod m} |F|^2
 = 2^nu m
   sum_{t_2,t_odd}
     |sum_{y:y_2^2=t_2 mod 2^nu,
             y_odd^2=t_odd mod m} a_y|^2.
```

For `nu<=1` the same formula holds with the trivial 2-coordinate omitted.

The odd square-fiber degree is bounded by r302z. For `nu>=2` the elementary 2-adic square-fiber bound is

```text
#{z mod 2^{nu-1}: z^2=y^2 (mod 2^nu)}
 <= 2 gcd(y,2_*),

2_* = 2^{floor(nu/2)}.
```

Hence the joint square-label fiber degree is

```text
<= B^{o(1)}
   gcd(y_odd,m_*) gcd(y_2,2_*)
```

for `nu>=2`, and reduces to the odd weight for `nu<=1`.

Also

```text
(2^nu m)/(phi(2^nu)phi(m))=B^{o(1)}
```

for `nu>=2`, and `m/phi(m)=B^{o(1)}` otherwise.

Therefore joint primitive-unit nonconcentration plus a subpower bound for the corresponding joint singular weighted Fourier energy yields

```text
Q_primitive(c)
 <= B^{o(1)} D_d
    * sum_{b in Adm_d}|c_b|^2.
```

This is the exact zero-loss form needed to let the r302w diagonal product supply the sole fixed power.

No joint unit-fiber nonconcentration and no joint singular-energy adapter is proved here.

```text
FIRST_MISSING_LEMMAS=
MAINWallJointPrimitiveUnitFiberSubpowerNonconcentration,
MAINWallJointPrimitiveSquareFiberWeightedEnergySubpowerAdapter

STAGE27_20_R302AL_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
JOINT_ODD_TWO_PRIMARY_PHASE_NORMAL_FORM_PROVED=true
TWO_PRIMARY_SLICE_COUNT_CHARGED=false
JOINT_ADDITIVE_PARSEVAL_REDUCTION_PROVED=true
TWO_ADIC_SQUARE_FIBER_BOUND_PROVED=true
SEPARATE_OFFDIAGONAL_FIXED_POWER_REQUIRED=false
JOINT_UNIT_FIBER_NONCONCENTRATION_PROVED=false
JOINT_SINGULAR_WEIGHTED_ENERGY_SUBPOWER_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302am
NEXT_BATCH=Stage27-20-r302-main-batch
```