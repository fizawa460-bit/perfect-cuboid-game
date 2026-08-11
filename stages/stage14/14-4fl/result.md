# Stage14-4fl — split primitive-ratio endpoint and genuinely polynomial branches

## Status

`COMPLETE_PRIMITIVE_RATIO_EXPONENT_CELL_AND_PROJECTIVE_ENDPOINT_BALANCED_SPLIT`

Consumes batch-local `Stage14-4fk` and merged `Stage14-s7-90..92` on the same heavy packet.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Exponent localization

On a heavy interior radial cell write

```text
n=B^(nu+o(1)),
I_int>=B^(mu-o(1)),
0<mu<=nu.
```

For every incidence in 4fk,

```text
n=E*u*v,
gcd(u,v)=1.
```

After the standard `B^o(1)` exponent/dyadic localization, write along a fixed saturating subsequence

```text
u = epsilon + alpha + beta,
E=B^(epsilon+o(1)),
u=B^(alpha+o(1)),
v=B^(beta+o(1)),
alpha,beta,epsilon>=0.                             (1)
```

The localization is bookkeeping only; no density is charged.

## 2. Three exact projective alternatives

Equation (1) gives the finite alternative

```text
(U-endpoint) alpha=0,
(V-endpoint) beta=0,
(Balanced)   alpha>0 and beta>0.
```

If both `alpha=beta=0`, that packet is included in either endpoint label after a finite tie convention. Since the heavy incidence is split among only finitely many alternatives, a surviving `B^(mu-o(1))` mass has one alternative carrying the same exponent.

```text
HEAVY_MASS_CAN_BE_FROZEN_TO_ONE_RATIO_EXPONENT_ALTERNATIVE=true
FINITE_RATIO_BRANCH_SPLIT_COST=Bo1
```

## 3. Endpoint small factor can be frozen, but the branch does not close

On the U-endpoint branch,

```text
u=B^o(1),
```

so the exact integer `u` ranges over only `B^o(1)` values and can be frozen without changing the fixed-power exponent. The V-endpoint branch is symmetric.

However, after freezing small `u`, the remaining equation is still

```text
n=(E*u)*v,
```

with `E` and `v` allowed polynomial mobility and with the full weight

```text
m_E(E) m_cpl(n,u,v,E)
```

retained. Therefore endpoint projective rays are not closed by the small-factor freeze.

The bare algebra itself shows why no geometry-only endpoint saving is available: before the residual physical weight is imposed, the family

```text
u=1,
E=1,
v=n
```

satisfies

```text
n=E*u*v,
gcd(u,v)=1
```

for every `n`. Whether the physical ratio window and completion Boolean accept such a packet is exactly part of the remaining weight problem; it cannot be decided by the factorization identity alone.

```text
ENDPOINT_SMALL_PRIMITIVE_FACTOR_FREEZABLE_AT_BO1_COST=true
ENDPOINT_RATIO_BRANCH_CLOSED=false
ENDPOINT_GEOMETRY_FIXED_POWER_SAVING_PROVED=false
```

## 4. Balanced branch

On the balanced branch both primitive factors have fixed positive exponents:

```text
alpha>0,
beta>0,
```

and hence

```text
u*v=B^(alpha+beta+o(1))
```

is polynomial. The complementary dilation has exponent

```text
epsilon=nu-alpha-beta>=0.
```

Thus the only remaining coarse split needed before the physical weight is theorem-shaped is

```text
E=B^o(1)
versus
E polynomial.
```

This split is meaningful on all three projective alternatives and is the next stage.

## 5. No double charge and H decision

Radial endpoint discharge from merged 4fi does not imply projective-ratio endpoint discharge; they are different endpoints. Work-bsX31 already forbids transferring fixed-U endpoint geometry here as well.

```text
RADIAL_ENDPOINT_AND_RATIO_ENDPOINT_IDENTIFIED=false
RADIAL_ENDPOINT_SAVING_RECHARGED=false
FIXED_U_ENDPOINT_TRANSFER_USED=false
```

No new H is opened: the complementary dilation exponent must be frozen first.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fm
```

## Boundary

```text
STAGE14_4FL=COMPLETE_PRIMITIVE_RATIO_EXPONENT_CELL_AND_PROJECTIVE_ENDPOINT_BALANCED_SPLIT
HEAVY_MASS_CAN_BE_FROZEN_TO_ONE_RATIO_EXPONENT_ALTERNATIVE=true
ENDPOINT_SMALL_PRIMITIVE_FACTOR_FREEZABLE_AT_BO1_COST=true
ENDPOINT_RATIO_BRANCH_CLOSED=false
ENDPOINT_GEOMETRY_FIXED_POWER_SAVING_PROVED=false
BALANCED_RATIO_BRANCH_EXPLICIT=true
COMPLEMENTARY_E_SCALE_SPLIT_NEXT=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4fm
```
