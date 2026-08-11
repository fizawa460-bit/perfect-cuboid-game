# Stage14-s7-83 — polynomial physical-factor mobility splits into squarefree-kernel diffusion or fixed-kernel square-part mobility

## Status

`COMPLETE_POLYNOMIAL_FACTOR_MOBILITY_TO_KERNEL_DIFFUSION_OR_SQUARE_PART_MOBILITY_SPLIT`

Consumes batch-local `Stage14-s7-81/82`, merged `Stage14-4ex`, and merged `Stage14-Work-boX27`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. The selected polynomial factor

Stage14-s7-82 freezes one factor label

```text
F_* in { |Xr|, |Yr|, |U|, |V| }
```

whose value support on a saturating radial packet satisfies

```text
|S_*| >= B^(delta-o(1))
```

for some fixed `delta>0` (one may take `delta=mu/4` from the radial-support exponent `mu`).

Every positive factor value has the unique decomposition

```text
F_* = kappa * a^2,
```

where

```text
kappa=sqf(F_*)
```

is squarefree and `a>=1`.

```text
POLYNOMIAL_FACTOR_VALUE_SUPPORT_FIXED=true
FACTOR_SQUAREFREE_KERNEL_SQUAREPART_DECOMPOSITION_UNIQUE=true
```

## 2. Quantitative support dichotomy

Let

```text
K_* := {kappa : exists a with kappa*a^2 in S_*}
```

be the squarefree-kernel support, and for each `kappa` let

```text
A_kappa := {a : kappa*a^2 in S_*}.
```

Then exactly

```text
|S_*| = sum_{kappa in K_*} |A_kappa|
      <= |K_*| * max_kappa |A_kappa|.
```

Since `|S_*|>=B^(delta-o(1))`, at least one of the following holds:

```text
A. |K_*| >= B^(delta/2-o(1)),
```

or

```text
B. max_kappa |A_kappa| >= B^(delta/2-o(1)).
```

Thus polynomial factor mobility cannot disappear inside a subpolynomial kernel dictionary and a subpolynomial square-part dictionary simultaneously.

```text
POLYNOMIAL_FACTOR_MOBILITY_SPLIT_QUANTITATIVE=true
KERNEL_OR_SQUAREPART_MOBILITY_EXPONENT_AT_LEAST=delta/2
```

## 3. Branch A — diffuse squarefree-kernel mobility

In branch A, polynomially many squarefree kernels of the selected physical factor occur. The exact s7-81 squareclass relation remains

```text
sqf(F1*F2*F3*F4)=K,
```

so the moving kernel of `F_*` is correlated with the other three factor kernels:

```text
sqf(F_*)
 = K * product_{j!=*} sqf(F_j)
```

in the squareclass group.

The live object is therefore not generic squarefree-kernel density but a factor-kernel correlation under the full canonical physical background.

Call this branch

```text
FixedPrimitiveRayDiffusePhysicalFactorSquarefreeKernelCorrelation.
```

```text
DIFFUSE_FACTOR_KERNEL_BRANCH_DEFINED=true
GENERIC_SQUAREFREE_KERNEL_DENSITY_RECHARGE_ALLOWED=false
```

## 4. Branch B — fixed-kernel polynomial square-part mobility

In branch B, freeze one squarefree kernel

```text
kappa_*
```

at a polynomial-support fiber. This is an exponent-level pigeonhole supplied by the quantitative dichotomy, not an assumption that the total kernel dictionary is subpolynomial.

Then the selected factor varies through

```text
F_* = kappa_* a^2
```

for polynomially many exact square-part values `a`.

The global fixed-ray squareclass condition no longer imposes any new density on this factor's moving square part: multiplying by `a^2` leaves its squareclass unchanged. Any saving on this branch must come from how the physical range/allocation/reciprocal masks correlate with the polynomial square-part coordinate `a`, not from squareclass parity itself.

Call this branch

```text
FixedPrimitiveRayFixedFactorKernelPolynomialSquarePartPhysicalIncidence.
```

```text
FIXED_FACTOR_KERNEL_SQUAREPART_BRANCH_DEFINED=true
SQUARECLASS_SELECTOR_IS_CONSTANT_ON_SQUAREPART_MOBILITY=true
SQUARECLASS_RECHARGE_ON_FIXED_KERNEL_BRANCH_ALLOWED=false
```

## 5. Material receiver change

The merged mainline receiver

```text
FixedPrimitiveRayCanonicalReciprocalProductFixedKernelSquareValueIncidence
```

has now been reduced to a factor-level dichotomy:

```text
FixedPrimitiveRayDiffusePhysicalFactorSquarefreeKernelCorrelation
OR
FixedPrimitiveRayFixedFactorKernelPolynomialSquarePartPhysicalIncidence.
```

This is a material change: the polynomial outer mobility has been localized from the four-factor product to either a moving squarefree kernel of one physical factor or a moving square part inside one fixed factor squareclass.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayDiffusePhysicalFactorSquarefreeKernelCorrelation_OR_FixedPrimitiveRayFixedFactorKernelPolynomialSquarePartPhysicalIncidence
RECEIVER_MATERIALLY_CHANGED=true
```

## 6. H decision

No new `sH` is opened at this boundary. Neither branch is theorem-ready yet:

- the diffuse-kernel branch first needs the actual factor label (`Xr`, `Yr`, `U`, or `V`) and retained gcd/squarefree/allocation masks projected onto its kernel coefficient;
- the fixed-kernel square-part branch first needs the physical equations written in the moving square-part coordinate `a`.

The existing global mover/diffuse H gates concern different receivers and cannot be cross-promoted.

```text
S7_83_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_83=COMPLETE_POLYNOMIAL_FACTOR_MOBILITY_TO_KERNEL_DIFFUSION_OR_SQUARE_PART_MOBILITY_SPLIT
POLYNOMIAL_FACTOR_MOBILITY_SPLIT_QUANTITATIVE=true
DIFFUSE_FACTOR_KERNEL_BRANCH_DEFINED=true
FIXED_FACTOR_KERNEL_SQUAREPART_BRANCH_DEFINED=true
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayDiffusePhysicalFactorSquarefreeKernelCorrelation_OR_FixedPrimitiveRayFixedFactorKernelPolynomialSquarePartPhysicalIncidence
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_83_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-84
```
