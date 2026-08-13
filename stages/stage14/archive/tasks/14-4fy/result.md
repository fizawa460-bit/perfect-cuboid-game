# Stage14-4fy — principal rectangular product capacity versus conditional physical-lift deficit

## Status

`COMPLETE_FIXED_E_PRINCIPAL_RECTANGLE_TO_DISTINCT_PRODUCT_CAPACITY_VERSUS_PHYSICAL_LIFT_BUDGET`

Consumes batch-local `Stage14-4fw/4fx`, merged `Stage14-q15`, merged `Stage14-s7-102..104`, and merged `Stage14-Work-bwX35`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Principal two-sided product rectangle

After 4fx every surviving fixed-`E` two-sided cell has fixed integer factor windows `D,V` with

```text
#D #V = B^(kappa_D+kappa_V+o(1)),
kappa_D+kappa_V >= mu-o(1).
```

Its legal ordinary upper envelope is exactly the distinct product set

```text
P(D,V)={dv:d in D,v in V}.
```

Write

```text
#P(D,V)=B^(pi+o(1)),
0<=pi<=kappa_D+kappa_V.
```

## 2. Put the physical support directly under the product support

Let

```text
S_phys := #{m : A_2s(m)=1}=B^(tau+o(1)).
```

Since merged 4fu and 4fw give pointwise

```text
A_2s(m) <= B_2s(m) <= 1_{m in P(D,V)},
```

we have

```text
0<=tau<=pi.
```

Define the total conditional physical-lift deficit from the ordinary product envelope by

```text
delta_lift := pi-tau >= 0.
```

This deficit intentionally includes every restriction removed in passing to the product envelope, notably

```text
- unitary/coprime-complement requirement,
- canonical/root-origin masks,
- reverse/post-column completion,
- any retained packet-local physical Boolean not forced by membership in P(D,V).
```

It is a nested-support exponent, not an independence assumption.

A surviving physical cell requires exactly

```text
pi-delta_lift=tau >= mu.                           (1)
```

Therefore survival forces both

```text
pi >= mu,
delta_lift <= pi-mu
```

up to `o(1)`.

```text
PRODUCT_SUPPORT_PHYSICAL_SUPPORT_NESTED=true
DISTINCT_PRODUCT_EXPONENT_PI_DEFINED=true
CONDITIONAL_PHYSICAL_LIFT_DEFICIT_DEFINED=true
FIXED_E_TWO_SIDED_SURVIVAL_BUDGET=pi_minus_delta_lift_ge_mu
```

## 3. Two noninterchangeable remaining mechanisms

The principal two-sided branch can now close in only two ways:

### P — distinct-product capacity loss

Prove for every relevant principal rectangle

```text
pi <= mu-eta
```

for some fixed `eta>0`.

### C — physical-lift loss inside a large product set

When `pi>=mu`, prove

```text
delta_lift > pi-mu
```

uniformly.

The two mechanisms are not multiplied unless a joint theorem controls the same charged cell.

```text
DISTINCT_PRODUCT_CAPACITY_MECHANISM_SEPARATED=true
CONDITIONAL_PHYSICAL_LIFT_MECHANISM_SEPARATED=true
PRODUCT_AND_LIFT_SAVINGS_INDEPENDENT_ASSUMED=false
```

## 4. q15 / Ford routing after exact straightening

Merged q15 searched the localized divisor shadow because at that time the interval

```text
U_E0(m)=sqrt(m*R_int(E0*m))
```

was still presented as moving with `m`. Stage14-4fw shows that on a fixed-`E`, fixed root/exponent chart this is exactly the fixed rectangular factor condition

```text
d in D,
m/d in V.
```

Hence the q15 moving-interval normalization problem is no longer the correct minimal formulation. The bare receiver is now a **distinct rectangular product-set capacity** problem.

Ford/Drappeau--Mounier remain useful ambient divisor architectures, but no merged result gives the branch-exact fixed-power upper bound

```text
#P(D,V) <= B^(mu-eta+o(1))
```

uniformly on all principal Stage14 rectangles. No logarithmic or `B^(-o(1))` compression is promoted to a fixed-power saving.

```text
Q15_MOVING_INTERVAL_NORMALIZATION_REMAINS=false
Q15_LOCALIZED_DIVISOR_ROUTE_SUPERSEDED_BY_RECTANGULAR_PRODUCT_CAPACITY=true
DIRECT_FIXED_POWER_RECTANGULAR_PRODUCT_CAPACITY_BOUND_MERGED=false
LITERATURE_FIXED_POWER_SAVING_IMPORTED=false
```

## 5. Whole heavy receiver and material change

The fixed-`E` part of the main heavy packet is now

```text
FixedComplementaryDilationPrimitiveEndpointOneDimensionalConditionalPhysicalCompletionSupport
OR
FixedComplementaryDilationTwoSidedPrincipalRectangularDistinctProductCapacityVersusConditionalPhysicalLiftDeficit.
```

The polynomial-`E` branches from 4fs/Work-bwX35 remain unchanged and separate:

```text
PolynomialComplementaryDilationFixedPrimitiveProductResidualELocalMaskVersusConditionalPhysicalCompletionDeficit
OR
PolynomialComplementaryDilationPolynomialPrimitiveProductBareUnitaryOuterPairShadowVersusConditionalPhysicalCompletionDeficit.
```

This is a material receiver change: the former moving ordinary-divisor interval has been fully eliminated from the minimal fixed-`E` two-sided object and replaced by an exact rectangular distinct-product support ledger.

```text
CURRENT_HEAVY_RECEIVER=FixedEEndpointConditionalCompletion_OR_FixedETwoSidedPrincipalRectangularDistinctProductCapacityVersusConditionalPhysicalLiftDeficit_OR_PolynomialEFixedProductResidualELocalMaskVersusCompletion_OR_PolynomialEPolynomialProductBareUnitaryOuterPairVersusCompletion
RECEIVER_MATERIALLY_CHANGED=true
```

## 6. H decision

No new heavy main H is opened at this boundary. The product-set object is stable, but before freezing an external theorem target the next internal step should split the principal rectangles by multiplication-map collision energy / near-injective product support and determine whether the Stage14 threshold `mu` actually demands fixed-power compression beyond elementary product capacity.

This avoids asking an H audit to prove a stronger product-set theorem than the branch exponent ledger requires.

The already-open non-heavy mainline H gates remain separate and pending.

```text
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
NEXT=Stage14-4fz
```

## Boundary

```text
STAGE14_4FY=COMPLETE_FIXED_E_PRINCIPAL_RECTANGLE_TO_DISTINCT_PRODUCT_CAPACITY_VERSUS_PHYSICAL_LIFT_BUDGET
FIXED_E_TWO_SIDED_SURVIVAL_BUDGET=pi_minus_delta_lift_ge_mu
DISTINCT_PRODUCT_CAPACITY_MECHANISM_SEPARATED=true
CONDITIONAL_PHYSICAL_LIFT_MECHANISM_SEPARATED=true
Q15_LOCALIZED_DIVISOR_ROUTE_SUPERSEDED_BY_RECTANGULAR_PRODUCT_CAPACITY=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
RECEIVER_MATERIALLY_CHANGED=true
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4fz
```
