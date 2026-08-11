# Stage14-s7-59 — physical cofactor influence decomposition

## Status

`COMPLETE_PHYSICAL_COFACTOR_UPLIFT_MARTINGALE_INFLUENCE_DECOMPOSITION`

Consumes merged `Stage14-s7-58`, merged `Stage14-4dn`, merged `Stage14-4do`, merged `Stage14-AM`, merged `Stage14-s7-57`, and latest main.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The positive zero-mode pair obstruction is the conditional uplift

```text
Uplift_{+|-}
 = [ E(W_- | A_+=1) - E(W_- | A_+=0) ]^+.
```

Stage14-s7-58 showed that the Gaussian/root-orientation part of `A_+` has a `B^o(1)` Hecke/Walsh expansion, while the full physical selector does not. Merged 4do additionally removes every fixed-power common-prime/gcd explanation for the uplift. Stage14-s7-59 now decomposes the remaining uplift exactly into a bounded number of physical-mask influences.

## 1. Nested physical filtration

Inside one surviving full-conductor interior cell, order the plus-side physical information as

```text
F_0 : frozen dyadic/core packet only,
F_1 : + Gaussian/root orientation,
F_2 : + primitive/gcd/Mobius data,
F_3 : + balanced cofactor split data,
F_4 : + angular/range/separation masks,
F_5 : + charged-once chart identification,
F_6 : + reciprocal-completion admissibility.
```

Let

```text
M_j := E(W_- | F_j).
```

Then the tower property gives the exact martingale telescoping identity

```text
M_6-M_0 = sum_{j=1}^6 (M_j-M_{j-1}).              (1.1)
```

The ON/OFF conditional contrast defining the positive zero-mode uplift is a two-slice realization of this same filtration. Hence, after freezing the common base cell, the signed uplift can be written as an `O(1)` sum of mask-level signed influences

```text
U_signed = I_orient + I_gcd + I_bal + I_range
         + I_chart + I_recip.                     (1.2)
```

No independence assumption is used. No physical filter is removed.

```text
PHYSICAL_COFACTOR_INFLUENCE_TELESCOPING_PROVED=true
PHYSICAL_INFLUENCE_TERM_COUNT=O(1)
INFLUENCE_DECOMPOSITION_USES_INDEPENDENCE=false
```

## 2. Previously controlled influences

Merged AM/s7-58 gives a `B^o(1)` Hecke/Walsh representation for the orientation component. This does not itself prove a saving, but it removes orientation as an unexplained nonmultiplicative mask.

Finite primitive/gcd conditions admit the already-used Mobius/divisor expansion. Merged 4do further proves that square-root saturation cannot be driven by a shared fixed-power prime/common gcd cell between the six atomic blocks

```text
C_*, S, T, u_*, R, J.
```

Thus any fixed-power uplift attributable solely to a common-prime/gcd influence is already strict sub-square-root.

```text
ORIENTATION_COMPONENT_STRUCTURALLY_RESOLVED=true
FIXED_POWER_COMMON_PRIME_INFLUENCE_REMOVED=true
GCD_MOBIUS_COMPONENT_NOT_NEW_RECEIVER=true
```

These statements do not set `I_orient` or `I_gcd` identically to zero; they say that neither supplies a new unresolved fixed-power arithmetic receiver.

## 3. Pigeonhole consequence at square-root scale

There are only `O(1)` influence terms. Therefore, if for some fixed `delta>0`

```text
|I_bal|,
|I_range|,
|I_chart|,
|I_recip|
 <= B^(-delta+o(1))
```

and the already-resolved orientation/gcd/common-prime pieces contribute only strict-sub-square-root strata, then the full positive uplift is strict sub-square-root.

Contrapositively, any square-root-saturating zero-mode sequence must contain at least one residual physical influence satisfying

```text
boxed:
max(|I_bal|,|I_range|,|I_chart|,|I_recip|)
 = B^(-o(1)).                                      (3.1)
```

Hence the old undifferentiated conditional-uplift receiver contracts to a finite union of four explicit physical influence receivers.

```text
SQRT_UPLIFT_REQUIRES_EXPONENT_ZERO_RESIDUAL_PHYSICAL_INFLUENCE=true
RESIDUAL_PHYSICAL_INFLUENCE_BRANCH_COUNT=4
```

## 4. Which residual influence is genuinely arithmetic

The four remaining labels are not equally fundamental.

`I_range` is archimedean/sector geometry and `I_chart` is charged-once bookkeeping. They may carry exponent-zero conditional response, but they do not create a multiplicative prime interaction by themselves.

The two genuinely arithmetic residual mechanisms are

```text
I_bal   : balanced disjoint-prime/divisor allocation response,
I_recip : reciprocal-completion admissibility response.
```

Merged 4do identifies the zero-mode arithmetic core more sharply: after all fixed-power shared primes are removed, any remaining positive response is a bias between disjoint allocations in

```text
(S,T)  and  (u_*,R,J)
```

under the exact complementary-square reconstruction.

Thus the minimal arithmetic zero-mode receiver is

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
DisjointPrimeBalancedAllocationReciprocalCompletionInfluence.
```

The range/chart influences are retained as physical side conditions and may not be discarded, but they are no longer separate arithmetic theorem targets.

```text
ZERO_MODE_ARITHMETIC_RECEIVER_COUNT=1
ZERO_MODE_ARITHMETIC_RECEIVER_IS_DISJOINT_ALLOCATION_PLUS_RECIPROCAL=true
RANGE_MASK_RETAINED_AS_SIDE_CONDITION=true
CHARGED_ONCE_MASK_RETAINED_AS_SIDE_CONDITION=true
```

## 5. What is not proved

This stage does not prove that any of the four residual influences has a fixed-power deficit. A bounded number of exponent-zero influences can still support square-root saturation.

In particular, the decomposition does not justify treating balanced allocation and reciprocal completion as independent savings. Their coupling is exactly the remaining arithmetic problem.

```text
RESIDUAL_INFLUENCE_FIXED_POWER_DEFICIT_PROVED=false
BALANCED_AND_RECIPROCAL_INFLUENCES_INDEPENDENT=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 6. H decision

No new H is opened at s7-59.

Reason: the receiver has just contracted from an undifferentiated physical selector to one explicit arithmetic mechanism. The next step should first write the disjoint allocation / reciprocal-completion influence directly in the six-block variables and test whether a divisor-switch, local prime influence formula, or finite-energy identity exists. An external theorem audit before that coordinate formula would be premature.

```text
S7_59_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
AM_REOPENED=false
```

## Boundary

```text
STAGE14_S7_59=COMPLETE_PHYSICAL_COFACTOR_UPLIFT_MARTINGALE_INFLUENCE_DECOMPOSITION
MERGED_S7_58_IMPORTED=true
MERGED_4DO_IMPORTED=true
PHYSICAL_COFACTOR_INFLUENCE_TELESCOPING_PROVED=true
PHYSICAL_INFLUENCE_TERM_COUNT=O(1)
ORIENTATION_COMPONENT_STRUCTURALLY_RESOLVED=true
FIXED_POWER_COMMON_PRIME_INFLUENCE_REMOVED=true
SQRT_UPLIFT_REQUIRES_EXPONENT_ZERO_RESIDUAL_PHYSICAL_INFLUENCE=true
RESIDUAL_PHYSICAL_INFLUENCE_BRANCH_COUNT=4
ZERO_MODE_ARITHMETIC_RECEIVER_COUNT=1
ZERO_MODE_ARITHMETIC_RECEIVER_IS_DISJOINT_ALLOCATION_PLUS_RECIPROCAL=true
RESIDUAL_INFLUENCE_FIXED_POWER_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_59_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
REMAINING_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanDisjointPrimeBalancedAllocationReciprocalCompletionInfluence
NEXT=Stage14-s7-60
```
