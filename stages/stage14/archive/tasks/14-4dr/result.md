# Stage14-4dr — single-prime two-square admissibility influence

## Status

`COMPLETE_SINGLE_PRIME_TWO_SQUARE_INFLUENCE_REDUCTION`

Consumes merged `Stage14-4dq`, merged `Stage14-s7-60`, merged `Stage14-t100`, merged `Stage14-tH27`, and latest main. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Import the coupled arithmetic receiver

Merged `4dq` shows that the only genuinely arithmetic zero-mode masks are balanced disjoint-prime allocation and reciprocal completion, acting sequentially on one six-block packet and therefore forbidden from independent double charge.

Merged `s7-60` sharpens this further: once the mixed-root packet, all side masks, and all other allocation bits are frozen, reciprocal completion has only `B^o(1)` multiplicity and the remaining arithmetic response is carried by one split-prime allocation bit `ell`.

Hence square-root saturation in this branch forces an exponent-zero single-prime physical-admissibility influence.

```text
SINGLE_PRIME_ARITHMETIC_INFLUENCE_IMPORTED=true
RECIPROCAL_COMPLETION_INDEPENDENT_FIXED_POWER_SUPPORT=false
```

## 2. Exact two-square test

Write the two product packets after the `ell` allocation choice as

```text
X = C_* S T,
Y = u_* R J.
```

Physical reconstruction requires simultaneously

```text
D^2 = (X+Y)/2,
A^2 = (X-Y)/2.
```

Thus for the two candidate states `sigma_ell=0,1`, the local influence is exactly the symmetric difference of the two-square admissibility predicate

```text
Q(X,Y) := 1_{(X+Y)/2 square} * 1_{(X-Y)/2 square}
```

with all range, chart, primitive, orientation and endpoint side conditions retained.

This converts the residual conditional influence into a finite-fiber comparison of two explicit integer pairs `(X_0,Y_0)` and `(X_1,Y_1)` differing only by the placement of `ell` in the disjoint allocation.

```text
TWO_SQUARE_ADMISSIBILITY_PREDICATE_EXPLICIT=true
SINGLE_PRIME_INFLUENCE_IS_TWO_CANDIDATE_SYMMETRIC_DIFFERENCE=true
```

## 3. No automatic thinness from one prime flip

The fact that only one split prime moves does not imply that the two-square symmetric difference is supported on a fixed-power-thin residue set.

A flip can change divisibility and residue information in both `X+Y` and `X-Y`, but the moduli inherited from the frozen cofactor packet need not be fixed or small. Likewise, `t100/tH27` only provide explicit fixed-U boundary-class information and do not legally cross-promote a uniform whole-family deficit into this global six-block receiver.

Therefore no `1/ell`, no square-root cancellation, and no independent reciprocal saving may be charged merely from the local flip representation.

```text
SINGLE_PRIME_FLIP_THIN_RESIDUE_SUPPORT_PROVED=false
FIXED_U_BOUNDARY_SAVING_CROSS_PROMOTED=false
FRESH_SINGLE_PRIME_FIXED_POWER_SAVING_PROVED=false
```

## 4. Minimal remaining arithmetic question

The whole zero-mode arithmetic obstruction is now reduced to one question:

```text
Can the average symmetric difference

Q(X_0,Y_0) XOR Q(X_1,Y_1)

for one active split prime ell be bounded by B^(-delta+o(1))
for some fixed delta>0, uniformly over the full-conductor physical packet?
```

Equivalently, one needs an exact local congruence / finite-energy identity for a single `ell`-flip that either gives a fixed-power deficit or isolates one residual principal class where both square tests remain coherent.

The receiver is

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
DisjointPrimeSingleAllocationTwoSquarePhysicalAdmissibilityInfluence.
```

This is narrower than `4dq`: reciprocal completion is now part of the `B^o(1)` completion fiber, not a separate theorem target.

## 5. H decision

No new mainline H is opened yet. The next step is internal: derive the exact congruence relation between the two candidate pairs under an `ell`-flip and classify when both square tests can change coherently. Only after that calculation exposes a standard theorem-shaped average should an H audit be triggered.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4DR=COMPLETE_SINGLE_PRIME_TWO_SQUARE_INFLUENCE_REDUCTION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
SINGLE_PRIME_ARITHMETIC_INFLUENCE_IMPORTED=true
RECIPROCAL_COMPLETION_INDEPENDENT_FIXED_POWER_SUPPORT=false
TWO_SQUARE_ADMISSIBILITY_PREDICATE_EXPLICIT=true
SINGLE_PRIME_INFLUENCE_IS_TWO_CANDIDATE_SYMMETRIC_DIFFERENCE=true
SINGLE_PRIME_FLIP_THIN_RESIDUE_SUPPORT_PROVED=false
FRESH_SINGLE_PRIME_FIXED_POWER_SAVING_PROVED=false
ZERO_MODE_SQRT_OBSTRUCTION_REDUCED_TO_SINGLE_PRIME_TWO_SQUARE_INFLUENCE=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

New receiver:

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
DisjointPrimeSingleAllocationTwoSquarePhysicalAdmissibilityInfluence
OrMaskedFullConductorInverseFractionCovariance
OrPositiveConnectedThirdCumulant
OrPrincipalOccupancy
```

Next: `Stage14-4ds`.
