# Stage14-4dp — charged-once cofactor influence decomposition

## Status

`COMPLETE_ORIENTATION_VS_NONMULTIPLICATIVE_PHYSICAL_MASK_INFLUENCE_DECOMPOSITION`

Consumes merged `Stage14-4do`, merged `Stage14-s7-58`, merged `Stage14-AM`, and merged `Stage14-Work-bfX18` on latest main.

The entering theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Positive zero-mode receiver from 4do

Merged 4do reduces the positive zero-mode conditional response to a bias between fixed-power-disjoint six-block allocations.  Shared large-prime/gcd explanations have already been removed.

Let `Y` denote the minus-side physical acceptance selector and let the plus conditioning mask be decomposed as

```text
A_+ = O * P,
```

where

```text
O = Gaussian/root-orientation plus the finite Mobius-expandable gcd/primitivity part,
P = remaining physical cofactor mask.
```

The split is a charged-once decomposition of the same selector.  It is not a product of independent counts.

## 2. What merged s7-58 / AM factorize

Merged s7-58 and AM give for the orientation component a Walsh/Gaussian-Hecke expansion with

```text
# phases = 2^omega(C_*) = B^o(1),
coefficient l1 cost = 1.
```

The finite gcd/primitivity part has a Mobius expansion with `B^o(1)` divisor complexity on the fixed packet.  Therefore the `O` dependence is a subpolynomial-complexity linear combination of multiplicative/Hecke phases.

This proves

```text
ORIENTATION_HECKE_FACTORIZATION_AVAILABLE=true
ORIENTATION_PHASE_COMPLEXITY=Bo1
ORIENTATION_COEFFICIENT_L1_COST=1
```

but it does not factorize `P`.

## 3. Exact influence telescoping

Order the retained nonmultiplicative physical masks in `P` as

```text
P_1, ..., P_r,
r=B^o(1),
```

where the list contains only masks already charged in the physical packet, e.g. dyadic/angular window membership, balanced divisor split admissibility, coupled block-separation state, chart identification, and reciprocal-completion admissibility.  Define partial selectors

```text
F_0 := O,
F_j := O * P_1 * ... * P_j,
F_r = A_+.
```

For any two conditioning states `a=1,0`, the conditional response of `Y` obeys the exact telescoping identity

```text
E[Y|F_r=1]-E[Y|F_r=0]
 = Delta_orient + sum_{j=1}^r Delta_j,
```

where `Delta_orient` is the response attributable to the orientation/Mobius-expandable sigma-algebra and each `Delta_j` is the incremental response created when adding the `j`-th physical mask, after conditioning on all earlier masks.  Equivalently one may formulate the same identity with a Doob martingale of conditional expectations.  No absolute value is taken before telescoping.

Hence by the triangle inequality only after the exact decomposition,

```text
Uplift <= Delta_orient^+ + sum_j |Delta_j|.
```

Since `r=B^o(1)`, if the total uplift is `B^(-o(1))`, then at least one component has exponent-zero size:

```text
Delta_orient^+ = B^(-o(1))
```

or for some physical mask

```text
|Delta_j| = B^(-o(1)).
```

This is a localization theorem, not yet a power saving.

## 4. Orientation branch versus physical-mask branch

The orientation branch is now theorem-compatible in form: it is a `B^o(1)`-complexity multiplicative/Hecke phase response.  However merged 4diH/sH50 already show that existing off-the-shelf oscillatory theorems do not by themselves control the whole positive physical count or its principal density.  Therefore no new H is triggered merely by exposing the same orientation phase family.

The complementary branch is genuinely nonmultiplicative.  At least one of the retained physical masks must have exponent-zero conditional influence on `Y`.  Because shared fixed-power prime support was removed in 4do, this influence cannot be explained by a common large gcd/prime between plus and minus blocks.

Thus the minimal new internal receiver is

```text
DisjointPrimeSixBlockExponentZeroSinglePhysicalMaskConditionalInfluence
```

with the masked full-conductor inverse-fraction covariance and connected third cumulant kept as separate branches.

## 5. No illegal cross-promotion

The following are alternative descriptions of the same charged-once pairwise mass and may not be multiplied:

```text
4dn conditional uplift,
4dm zero/centered covariance split,
s7-58 orientation factorization,
4dp influence telescoping.
```

Likewise fixed-U orientation influence from t96/t97 is not imported: merged bfX18 already provides an explicit witness showing large edge influence does not imply a first-order global conditional response.

## 6. Whole-family boundary

```text
STAGE14_4DP=COMPLETE_ORIENTATION_VS_NONMULTIPLICATIVE_PHYSICAL_MASK_INFLUENCE_DECOMPOSITION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
ORIENTATION_HECKE_FACTORIZATION_AVAILABLE=true
FULL_PHYSICAL_SELECTOR_HECKE_FACTORIZATION_AVAILABLE=false
COFACTOR_INFLUENCE_TELESCOPING_PROVED=true
SQRT_ZERO_MODE_REQUIRES_EXPONENT_ZERO_ORIENTATION_OR_SINGLE_MASK_INFLUENCE=true
FIXED_POWER_COMMON_PRIME_EXPLANATION_REMAINS=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

New receiver:

```text
DisjointPrimeSixBlockExponentZeroSinglePhysicalMaskConditionalInfluence
```

Next: `Stage14-4dq`.
