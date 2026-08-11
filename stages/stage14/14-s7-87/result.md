# Stage14-s7-87 — consume merged mass-capacity supersession and normalize the exact radial coordinate

## Status

`COMPLETE_MERGED_4FD_BQX29_SUPERSESSION_AND_FIXED_DENOMINATOR_RADIAL_NORMALIZATION`

Consumes merged `Stage14-s7-86`, merged mainline `Stage14-4fb..4fd`, merged `Stage14-Work-bqX29`, and latest merged main at batch start

```text
c5c84d2727caad0afdc08dec69f6696716f21b38.
```

Only merged sources are theorem sources.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. The old mass-capacity gap is superseded

Merged s7-86 ended with the fixed-ray equation

```text
d0*J*a*b=c0*h,
gcd(c0,d0)=1,
```

and the short support bound `#h<=B^(1/24+o(1))`, but it still described the obstruction as an unknown comparison between required mass and radial capacity.

Merged 4fb..4fd now settles that comparison in the exact collision-energy ledger.  If one heavy ray survives, write

```text
M_C=B^(mu+o(1)),
rho(phi)=1/4-phi.
```

Then necessarily

```text
0<mu<=rho(phi)<=1/24
```

and for a maximizing heavy ray its exact physical radial support `H_*` satisfies

```text
B^(mu-o(1)) <= |H_*| <= B^(rho(phi)+o(1)).
```

Merged Work-bqX29 explicitly identifies this with the same s-route exact radial coordinate.  Hence the s7-86 `ShortRadialScaleMassCapacityGap` is no longer the live receiver.

```text
MERGED_4FD_CONSUMED=true
MERGED_BQX29_CONSUMED=true
S7_86_MASS_CAPACITY_GAP_SUPERSEDED=true
SURVIVING_HEAVY_RAY_MU_RANGE=0<mu<=1/4-phi
SURVIVING_HEAVY_RAY_RADIAL_SUPPORT_LOWER_BOUND=B^(mu-o(1))
SURVIVING_HEAVY_RAY_RADIAL_SUPPORT_UPPER_BOUND=B^(1/4-phi+o(1))
```

## 2. Exact divisibility forced by the fixed rational-square coefficients

Retain the s7-86 exact equation

```text
d0*J*a*b=c0*h,
gcd(c0,d0)=1.
```

Euclid's lemma gives the two exact divisibilities

```text
d0 | h,
c0 | J*a*b.
```

Therefore there is a unique positive integer `n` such that

```text
boxed:
h=d0*n,
J*a*b=c0*n.
```

This is an exact normalization, not a density assumption.

```text
FIXED_DENOMINATOR_DIVIDES_EVERY_ACCEPTED_H=true
FIXED_NUMERATOR_DIVIDES_EVERY_ACCEPTED_JAB=true
NORMALIZED_RADIAL_COORDINATE_N_DEFINED=true
NORMALIZED_RADIAL_EQUALITIES=h_equals_d0_n_AND_Jab_equals_c0_n
```

## 3. Denominator spacing gives the exact support-capacity refinement

Freeze the already-allowed dyadic exponent cell

```text
h=B^(sigma+o(1)),
0<mu<=sigma<=rho(phi).
```

Write

```text
d0=B^(lambda+o(1)),
lambda>=0.
```

Because every accepted `h` is a multiple of `d0`, the normalized coordinate has scale

```text
n=B^(sigma-lambda+o(1)).
```

The map `h -> n=h/d0` is injective, so the accepted support has the same cardinality in the two coordinates.  Consequently

```text
B^(mu-o(1))
 <= #N_*
 <= B^(sigma-lambda+o(1)).
```

A surviving heavy ray therefore forces

```text
boxed:
lambda <= sigma-mu.
```

In particular a near-capacity radial packet `mu=sigma-o(1)` forces `d0=B^o(1)`.  More generally any polynomial denominator consumes exactly the same exponent from the available radial support length.

```text
RADIAL_DENOMINATOR_EXPONENT=lambda
SURVIVAL_REQUIRES_lambda_LE_sigma_MINUS_mu=true
NEAR_CAPACITY_RADIAL_OCCUPANCY_FORCES_d0=Bo1
FIXED_DENOMINATOR_DENSITY_RECHARGE_ALLOWED=false
```

This is a support identity, not a whole-family saving: small `mu` can coexist with positive `lambda`.

## 4. Receiver and H decision

The live problem is now the arithmetic support of normalized integers `n` satisfying

```text
J*a*b=c0*n
```

with the full frozen root/range/orientation/reconstruction masks.  The next internal stage should peel the fixed numerator `c0` from `(J,a,b)` at divisor-many cost and determine the true moving multiplicative form.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_87_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_87=COMPLETE_MERGED_4FD_BQX29_SUPERSESSION_AND_FIXED_DENOMINATOR_RADIAL_NORMALIZATION
S7_86_MASS_CAPACITY_GAP_SUPERSEDED=true
FIXED_DENOMINATOR_DIVIDES_EVERY_ACCEPTED_H=true
FIXED_NUMERATOR_DIVIDES_EVERY_ACCEPTED_JAB=true
NORMALIZED_RADIAL_COORDINATE_N_DEFINED=true
SURVIVAL_REQUIRES_lambda_LE_sigma_MINUS_mu=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_87_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-88
```
