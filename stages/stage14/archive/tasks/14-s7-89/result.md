# Stage14-s7-89 — coefficient-peeled radial support to shared squarefree dilation times square-ratio incidence

## Status

`COMPLETE_NORMALIZED_TRIPLE_PRODUCT_TO_SHARED_SQUAREFREE_DILATION_AND_FIXED_COEFFICIENT_SQUARE_RATIO_RECEIVER`

Consumes batch-local `Stage14-s7-87/88`, merged `Stage14-s7-85/86`, merged mainline `Stage14-4fd`, and merged `Stage14-Work-bqX29`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Fixed coefficient packet after the c0 peel

Stage14-s7-88 freezes

```text
c0=c_J*c_a*c_b,
J=c_J*J1,
a=c_a*a1,
b=c_b*b1,
```

and proves

```text
n=J1*a1*b1,
h=d0*n.
```

The pre-peel root normal form was

```text
|Xr|=J*A*a^2,
|Yr|=J*B*b^2,
A*B=K_Z.
```

Define the fixed positive coefficients

```text
alpha:=c_J*A*c_a^2,
beta :=c_J*B*c_b^2.
```

Then every accepted normalized point satisfies exactly

```text
boxed:
|Xr|=alpha*J1*a1^2,
|Yr|=beta *J1*b1^2,
h=d0*J1*a1*b1.
```

All coefficients depend only on the already-frozen heavy-ray/agreement/coefficient-allocation packet.

```text
FIXED_PEELED_ROOT_COEFFICIENTS_ALPHA_BETA_DEFINED=true
PEELED_ROOT_PAIR_NORMAL_FORM=true
PEELED_RADIAL_PRODUCT_NORMAL_FORM=true
```

## 2. Product and projective ratio separate exactly

The common squarefree factor `J1` acts as a simultaneous dilation of both root factors.  It cancels from their projective ratio:

```text
boxed:
|Xr|/|Yr|=(alpha/beta)*(a1/b1)^2.
```

Thus the root-side geometry decomposes into two exact coordinates:

```text
shared radial dilation: J1,
fixed-coefficient square ratio: a1/b1.
```

At the same time the normalized radial coordinate is

```text
n=J1*a1*b1.
```

So `J1` is not an independent extra support beyond `n`; rather it is the common dilation component in a factorization of each accepted radial value, while `(a1,b1)` supplies the square-ratio component.

```text
SHARED_SQUAREFREE_FACTOR_CANCELS_FROM_ROOT_RATIO=true
ROOT_PROJECTIVE_RATIO_IS_FIXED_COEFFICIENT_RATIONAL_SQUARE=true
NORMALIZED_RADIAL_VALUE_FACTORS_AS_SHARED_DILATION_TIMES_SQUAREPART_PRODUCT=true
```

## 3. Exact normalized physical incidence

After all once-charged labels are frozen, define the normalized heavy-ray incidence family by triples

```text
(J1,a1,b1)
```

satisfying simultaneously:

```text
J1 squarefree,
J1*a1*b1=n,
|Xr|=alpha*J1*a1^2,
|Yr|=beta*J1*b1^2,
h=d0*n,
```

plus every inherited physical range, gcd, primitive, orientation, root-origin, allocation, and reverse-completion mask.

For fixed `n`, merged s7-88 gives only `B^o(1)` such triples.  Merged 4fd/bqX29 gives on every surviving heavy ray

```text
B^(mu-o(1)) <= #N_* <= B^(sigma-lambda+o(1)),
0<mu<=1/4-phi.
```

Therefore the remaining heavy-ray obstruction is exactly a polynomial set of normalized radial values admitting at least one such shared-squarefree / square-ratio physical factorization.

Call the new receiver

```text
FixedPrimitiveRayFixedAgreementPairSharedSquarefreeDilationFixedCoefficientSquareRatioRadialPhysicalOccupancy.
```

This is materially sharper than the unstructured `PolynomialRadialOccupancy` receiver: the moving root pair is now an explicit fixed-coefficient multiplicative form and the common-dilation versus projective-square coordinates are separated without changing quantifier order.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairSharedSquarefreeDilationFixedCoefficientSquareRatioRadialPhysicalOccupancy
RECEIVER_MATERIALLY_CHANGED=true
```

## 4. What is and is not a fresh saving

No generic square density, squarefree density, multiplication-table sparsity, or divisor density is charged here.

The identities

```text
n=J1*a1*b1,
|Xr|/|Yr|=(alpha/beta)*(a1/b1)^2
```

are deterministic normal forms for already-accepted physical points.  A fixed-power gain would require showing that the retained physical masks make polynomial occupancy of this normalized family sparse, or exposing a further exact relation that reduces one of the three moving coordinates.

```text
GENERIC_SQUARE_DENSITY_RECHARGED=false
GENERIC_SQUAREFREE_DENSITY_RECHARGED=false
GENERIC_MULTIPLICATION_TABLE_SAVING_CLAIMED=false
FIXED_N_DIVISOR_FIBER_RECHARGED=false
```

## 5. H decision

No new `sH` is opened at this boundary.  The coefficient system is now explicit, but the live acceptance predicate still contains the canonical root-origin/range/reverse-completion masks rather than a frozen analytic coefficient sequence suitable for a theorem audit.

The next internal stage should project those masks onto the normalized `(J1,a1,b1)` family and determine whether the common dilation `J1` or the square ratio `a1/b1` remains a genuine polynomial outer selector.

```text
S7_89_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_89=COMPLETE_NORMALIZED_TRIPLE_PRODUCT_TO_SHARED_SQUAREFREE_DILATION_AND_FIXED_COEFFICIENT_SQUARE_RATIO_RECEIVER
FIXED_PEELED_ROOT_COEFFICIENTS_ALPHA_BETA_DEFINED=true
PEELED_ROOT_PAIR_NORMAL_FORM=true
SHARED_SQUAREFREE_FACTOR_CANCELS_FROM_ROOT_RATIO=true
ROOT_PROJECTIVE_RATIO_IS_FIXED_COEFFICIENT_RATIONAL_SQUARE=true
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairSharedSquarefreeDilationFixedCoefficientSquareRatioRadialPhysicalOccupancy
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_89_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-90
```
