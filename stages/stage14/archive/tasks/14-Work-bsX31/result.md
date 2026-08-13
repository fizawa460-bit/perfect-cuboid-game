# Stage14-Work-bsX31 — scalar outer reciprocal-selector and endpoint-transfer audit

## Status

`COMPLETE_SCALAR_OUTER_RECIPROCAL_SELECTOR_AND_ENDPOINT_TRANSFER_NOGO`

Consumes only merged theorem sources on latest main at branch start:

- merged `Stage14-Work-brX30`;
- merged mainline `Stage14-4fh..4fj`;
- merged s-route `Stage14-s7-90..92`;
- merged fixed-U `Stage14-t129..131`;
- merged `Stage14-q14` as a literature-routing boundary;
- completed merged `Stage14-tH29` only through its already-consumed negative boundary.

Branch-start main:

```text
017f4984c27c474d353291ad9040571d549185a6
```

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. What brX30 left open

Work-brX30 proved that global/main and s use the same normalized radial reciprocal-divisor coordinate, while fixed-U shares only reciprocal-hyperbola geometry.  The remaining integrated target was

```text
ReciprocalWindowEndpointInteriorPhysicalWeightIntersectionOrNoGo.
```

The new merged descendants sharpen both sides enough to settle the coordinate-level part of that target.

## 2. Global/s: the main reciprocal divisor is exactly the primitive divisor-ratio selector

Merged s7-90..92 gives the exact primitive-ratio normal form

```text
n=E*u*v,
gcd(u,v)=1,
|Xr|=alpha*E*u^2,
|Yr|=beta*E*v^2.
```

The reciprocal divisor coordinate from merged 4fg/brX30 is therefore

```text
L=E*u^2,
L/n=u/v.
```

Conversely, on the same accepted global/s packet, the s7-90 bijection reconstructs

```text
E=n/(u*v),
L=E*u^2,
```

with the inherited squareclass, gcd, primitive, canonical, root-origin and reverse-completion masks carried by `E` and the frozen packet labels.

Thus merged mainline 4fj's physical incidence

```text
I_int=sum_n sum_L w_phys(n,L)
```

can be pulled back exactly, with only the already-charged finite labels, to

```text
I_ratio
 = sum_n sum_{gcd(u,v)=1, uv|n, u/v in R_phys(n)}
     w_ratio(n,u,v,E=n/(uv)).
```

No second support count is created by changing coordinates.

```text
GLOBAL_S_PRIMITIVE_DIVISOR_RATIO_COORDINATE_IDENTIFIED=true
GLOBAL_S_MAIN_S_RECEIVERS_UNIFIED_AT_RATIO_LEVEL=true
GLOBAL_S_L_OVER_N_EQUALS_U_OVER_V=true
GLOBAL_S_RECIPROCAL_AND_RATIO_COUNTS_MULTIPLICABLE=false
GLOBAL_S_FIXED_N_INNER_FIBER=Bo1
```

The current global/s heavy receiver may therefore be written uniformly as

```text
FixedPrimitiveRayFixedAgreementPairInteriorNormalizedRadialPrimitiveCoprimeDivisorRatioShortWindowPhysicalIncidence
WithMassExponentMuAndComplementaryPhysicalWeight.
```

## 3. Global/s radial endpoints are discharged, but the arithmetic inner weight remains

Merged 4fh identifies the exact radial product window and merged 4fi proves that, on a heavy exponent cell `n=B^(nu+o(1))`, endpoint strips of logarithmic thickness `B^-theta` are negligible whenever

```text
theta>nu-mu.
```

Hence a surviving packet retains `B^(mu-o(1))` interior outer values `n`.  Merged 4fj converts existential acceptance to a physical incidence sum because every fixed `n` has only `B^o(1)` admissible inner candidates.

This same endpoint discharge is legal for the s representation because Work-brX30 and the exact map above identify the same physical global/s packet and the same outer radial integer `n`; it is not a cross-promotion from fixed-U.

What remains is not the archimedean endpoint geometry but the arithmetic physical weight on the short primitive-ratio/divisor window:

```text
w_ratio(n,u,v,E)
```

including the complementary-`E` squareclass/canonical/reverse masks.

```text
GLOBAL_S_RADIAL_ENDPOINT_STRIPS_DISCHARGED=true
GLOBAL_S_INTERIOR_OUTER_SUPPORT_EXPONENT=mu
GLOBAL_S_ARCHIMEDEAN_WINDOW_GEOMETRY_AS_FIXED_POWER_SOURCE_EXHAUSTED=true
GLOBAL_S_COMPLEMENTARY_PHYSICAL_WEIGHT_OPENING_STILL_REQUIRED=true
```

Merged q14 is consistent with this boundary: Ford-type divisor-in-an-interval results are near geometry, but no direct theorem preserves the charged squareclass/physical measure.  In particular, no Ford saving is imported here.

```text
Q14_FORD_ROUTE_REMAINS_GLOBAL_S_ONLY=true
Q14_DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
Q14_FORD_TRANSFER_PREMATURE_BEFORE_PHYSICAL_WEIGHT_OPENING=true
```

## 4. fixed-U: every live branch now has one scalar-norm outer coordinate

Merged t129..131 consumes the tH29 split and proves that every surviving fixed-U mechanism can be expressed over the polynomial scalar cofactor norm

```text
n=N(gamma).
```

The three live mechanisms are:

```text
(A) endpoint corner-wedge projective-prime depletion;
(B) long-headroom real Hecke bias against W_phys(n) xi_chi(n_G);
(C) long-headroom nonreal Hecke correlation against A_chi(n),
```

with

```text
D_chi,long
 = chi([a]) sum_n A_chi(n) P_chi(X_U/n),
|A_chi(n)|<=B^o(1).
```

Real/order-two projective characters are orientation-blind, while nonreal orientation dependence is compressed into `A_chi(n)`.

```text
FIXED_U_ALL_LIVE_BRANCHES_ONE_DIMENSIONAL_SCALAR_NORM_OUTER=true
FIXED_U_REAL_BRANCH_ORIENTATION_BLIND=true
FIXED_U_NONREAL_ORIENTATION_COMPRESSED_TO_NORM_FIBER_COEFFICIENT=true
FIXED_U_PROJECTIVE_PRIME_RECIPROCAL_CUMULATIVE_ARGUMENT=X_U_over_n
```

This is a genuine receiver simplification, but it does not identify the fixed-U norm variable with the global/s normalized radial variable.

## 5. Endpoint/interior transfer no-go at the current arithmetic level

The word "endpoint" now refers to different arithmetic phenomena on the two sides.

Global/s:

```text
radial product-window endpoint in the outer integer n;
```

its thin strips can be discarded by the plain cardinality estimate of 4fi.

Fixed-U:

```text
projective-prime headroom endpoint
R(n)=N_max/n in (1,B^theta),
```

which becomes the logarithmic hyperbola wedge `0<u<=v<theta`.  Merged t129 proves that neither projection is fixed-power small from geometry alone, so this branch cannot be discarded by importing 4fi.

Therefore the common reciprocal-window language does **not** produce a common endpoint theorem.

```text
GLOBAL_S_RADIAL_ENDPOINT_DISCHARGE_CROSS_PROMOTABLE_TO_FIXED_U=false
FIXED_U_ENDPOINT_HEADROOM_BRANCH_DISCHARGED=false
COMMON_ENDPOINT_NOTION_ARITHMETICALLY_IDENTIFIED=false
COMMON_ENDPOINT_INTERIOR_TRANSFER_PROVED=false
```

The direct adapter also still fails at the inner-selector level:

```text
GLOBAL/S:
  existence of gcd(u,v)=1, uv|n, u/v in a short physical window,
  with complementary E=n/(uv) masks;

FIXED-U:
  weighted prime cumulative sums P_chi(X_U/n),
  projective character phases and physical scalar-norm weights.
```

One side is a divisor-ratio existence/incidence problem with `B^o(1)` inner candidates per fixed outer value; the other is a weighted prime/character sum with a polynomial prime interval.  No finite-fiber map preserving physical measure, prime/projective labels and quantifier order is merged.

```text
COMMON_ONE_DIMENSIONAL_OUTER_RECIPROCAL_SELECTOR_LANGUAGE_PROVED=true
COMMON_ARITHMETIC_SCALAR_OUTER_COORDINATE_IDENTIFICATION_PROVED=false
COMMON_INNER_SELECTOR_TYPE_IDENTIFIED=false
COMMON_PHYSICAL_WEIGHT_ADAPTER_PROVED=false
DIRECT_PRIMITIVE_RATIO_TO_PROJECTIVE_CHARACTER_ADAPTER_NOGO_AT_CURRENT_LEVEL=true
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

This is a current-level no-go only.  A later exact physical map may reopen the adapter question.

## 6. Charged-once / supersession locks

The following may not be recharged as independent savings:

- main reciprocal-divisor coordinates and s primitive-ratio coordinates are exact representations of the same global/s packet;
- radial endpoint strips already removed by 4fi;
- pure reciprocal-window geometry from 4fh/s7-92;
- t129 endpoint wedge geometry;
- real-character orientation elimination from t130;
- tH29 negative theorem boundary.

```text
GLOBAL_S_COORDINATE_CHANGE_RECHARGE_ALLOWED=false
GLOBAL_S_RADIAL_ENDPOINT_SAVING_RECHARGE_ALLOWED=false
RECIPROCAL_WINDOW_GEOMETRY_RECHARGE_ALLOWED=false
FIXED_U_ENDPOINT_GEOMETRY_RECHARGE_ALLOWED=false
TH29_NEGATIVE_BOUNDARY_RECHARGE_ALLOWED=false
```

## 7. Current receivers

```text
CURRENT_GLOBAL_RECEIVER=FixedPrimitiveRayFixedAgreementPairInteriorNormalizedRadialPrimitiveCoprimeDivisorRatioShortWindowPhysicalIncidenceWithMassExponentMuAndComplementaryPhysicalWeight_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation

CURRENT_S_RECEIVER=FixedPrimitiveRayFixedAgreementPairInteriorNormalizedRadialPrimitiveCoprimeDivisorRatioShortWindowPhysicalIncidenceWithMassExponentMuAndComplementaryPhysicalWeight_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation

CURRENT_FIXED_U_RECEIVER=SharedUScalarNormOuterEndpointCornerWedgeProjectivePrimeDepletionOrLongRealHeckeBiasAgainstPhysicalNormWeightOrLongNonrealHeckeCorrelationAgainstNormFiberOrientationCoefficient
```

## 8. H decisions

No new heavy/global H is opened at this integrated boundary.  The global/s heavy branch must first expose `w_ratio`/the complementary-`E` physical weight.  q14 already says Ford transfer is premature before that opening.

The previously existing non-heavy mainline three-divisor / mover / diffuse H targets remain pending in the integrated ledger, so the broad mainline H flag remains true, while the whole mainline is not H-blocked.

Fixed-U likewise needs internal decomposition of the endpoint principal mass and the real/nonreal scalar coefficients before a materially new theorem request exists.  Completed tH29 remains the negative theorem boundary.

```text
MAINLINE_H_NEEDED=true
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH29_COMPLETE_CONSUMED=true
TH30_NEEDED=false
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

## 9. Next integrated target

The next cross-route question is no longer raw reciprocal geometry.  It is whether opening the actual arithmetic weights produces a common analyzable kernel or a stronger no-go:

```text
NEXT_INTEGRATED_TARGET=ReciprocalInnerPhysicalWeightArithmeticAdapterOrNoGo
```

Normal revisit condition:

```text
NEXT_REVISIT_CONDITION=4fm+s7-95+t134
```

Earlier revisit is justified by any of:

- a theorem-ready opening of global/s `w_ratio` or complementary-`E` weight;
- a fixed-power deficit for primitive divisor-ratio occupancy;
- deterministic closure of the fixed-U endpoint branch;
- a new real/nonreal fixed-U theorem target (`tH30` or successor);
- an exact physical arithmetic adapter between the global/s inner ratio selector and the fixed-U scalar-norm/prime-character kernel;
- any new strict sub-square-root whole-family exponent.

## Boundary locks

```text
STAGE14_WORK_BSX31=COMPLETE
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
GLOBAL_S_PRIMITIVE_DIVISOR_RATIO_COORDINATE_IDENTIFIED=true
GLOBAL_S_MAIN_S_RECEIVERS_UNIFIED_AT_RATIO_LEVEL=true
GLOBAL_S_RADIAL_ENDPOINT_STRIPS_DISCHARGED=true
FIXED_U_ALL_LIVE_BRANCHES_ONE_DIMENSIONAL_SCALAR_NORM_OUTER=true
COMMON_ONE_DIMENSIONAL_OUTER_RECIPROCAL_SELECTOR_LANGUAGE_PROVED=true
COMMON_ENDPOINT_INTERIOR_TRANSFER_PROVED=false
COMMON_PHYSICAL_WEIGHT_ADAPTER_PROVED=false
DIRECT_PRIMITIVE_RATIO_TO_PROJECTIVE_CHARACTER_ADAPTER_NOGO_AT_CURRENT_LEVEL=true
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
MAINLINE_H_NEEDED=true
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH30_NEEDED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT_INTEGRATED_TARGET=ReciprocalInnerPhysicalWeightArithmeticAdapterOrNoGo
NEXT_REVISIT_CONDITION=4fm+s7-95+t134
```
