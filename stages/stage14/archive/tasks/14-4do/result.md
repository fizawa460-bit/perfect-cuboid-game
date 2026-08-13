# Stage14-4do — disjoint-prime allocation source of conditional uplift

## Status

`COMPLETE_ZERO_MODE_UPLIFT_DISJOINT_PRIME_ALLOCATION_REDUCTION`

Consumes merged `Stage14-4dn`, `Stage14-s7-57`, `Stage14-Work-bfX18`, `Stage14-4df`, `Stage14-4de`, `Stage14-s7-47`, and `Stage14-X15` on latest main.

The whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering conditional-response identity

For the representative zero-mode pair put

```text
A=A_+,
B=W_-,
nu_1=E[B|A=1],
nu_0=E[B|A=0].
```

Merged 4dn gives exactly

```text
Cov(A,B)=mu_A(1-mu_A)(nu_1-nu_0).
```

Hence only the positive uplift

```text
Uplift:=(nu_1-nu_0)^+
```

is an upper-bound obstruction. Fixed-power small uplift is already strict sub-square-root.

Merged s7-57 proves that exponent-zero positive correlation does not imply near-deterministic Bernoulli coupling. Thus there is no legal probabilistic shortcut from `Uplift=B^(-o(1))` to selector equality.

## 2. Return to the six atomic arithmetic blocks

At square-root saturation, merged 4df/s7-47 give the six-block representation

```text
C_*, S, T, u_*, R, J
```

with fixed-power pairwise separation.  In particular all pairwise gcds among these six blocks are `B^o(1)` after the frozen endpoint-small decoration is removed.

The two physical product packets are

```text
X_+ = C_* S T,
X_- = u_* R J,
```

and

```text
D^2=(X_+ + X_-)/2,
A^2=(X_+ - X_-)/2.
```

Thus, once the six blocks and the frozen `B^o(1)` decoration are fixed, `(D,A)` and the reciprocal completion have `B^o(1)` multiplicity.

## 3. Conditional uplift cannot come from a common fixed-power prime

The plus zero-mode cofactor selector toggles admissibility of the `(S,T)` allocation while the minus selector is reconstructed from the complementary `(u_*,R,J)` packet together with the same physical square identities.

Because the six atomic blocks are fixed-power pairwise separated, no prime `p=B^(epsilon+o(1))` can simultaneously divide a plus-side cofactor block and a minus-side atomic block on a square-root-saturating sequence.  Therefore a positive conditional uplift cannot be attributed to a shared fixed-power prime factor or a shared fixed-power gcd cell.

Equivalently, every fixed-power common-prime explanation of

```text
nu_1 > nu_0
```

has already been peeled by the merged six-block separation stages.

## 4. Remaining arithmetic source: disjoint-prime allocation bias

After fixing the common core, root label, archimedean box, endpoint-small decoration, and all `B^o(1)` gcd data, the only remaining arithmetic distinction between the `A=1` and `A=0` slices is the divisor/prime allocation pattern inside the disjoint packets

```text
plus packet : (S,T),
minus packet: (u_*,R,J).
```

Hence the zero-mode conditional response is reduced to a **disjoint-prime allocation bias**:

```text
Resp_zero
 = E[ W_- | plus allocation admissible ]
 - E[ W_- | plus allocation inadmissible ],
```

with no fixed-power common prime allowed to mediate the correlation.

This is a contraction of the receiver, not a proof that the bias is small.  A multiplicative/Hecke phase factorization of this disjoint-allocation sensitivity is not yet available, and merged Stage14-AM does not apply directly because the physical primitive reconstruction and fixed-product conditioning destroy the free multiplicative averaging parameter.

## 5. Consequence

Every fixed-power common-prime or common-gcd uplift stratum is removed.  Square-root saturation in the zero-mode branch can only occur through

```text
Uplift=B^(-o(1))
```

caused by correlation between **disjoint prime allocations** under the exact complementary-square reconstruction.

No new external theorem family is exposed beyond the already-audited multiplicative/dispersion shelves, so a new H is premature.

## Boundary

```text
STAGE14_4DO=COMPLETE_ZERO_MODE_UPLIFT_DISJOINT_PRIME_ALLOCATION_REDUCTION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
ZERO_MODE_CONDITIONAL_UPLIFT_IMPORTED=true
BERNOULLI_NEAR_DETERMINISM_SHORTCUT_FORBIDDEN=true
SIX_ATOMIC_BLOCK_PAIRWISE_SEPARATION_IMPORTED=true
FIXED_POWER_COMMON_PRIME_UPLIFT_REMOVED=true
FIXED_POWER_COMMON_GCD_UPLIFT_REMOVED=true
ZERO_MODE_SQRT_OBSTRUCTION_REDUCED_TO_DISJOINT_PRIME_ALLOCATION_BIAS=true
DISJOINT_PRIME_ALLOCATION_BIAS_FIXED_POWER_DEFICIT_PROVED=false
STAGE14_AM_DIRECT_TRANSFER_APPLICABLE=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

New receiver:

```text
FullConductorNearMaximalInteriorDensePrimitiveQuarterPythagorean
PositiveZeroModeDisjointPrimeAllocationConditionalUplift
OrMaskedFullConductorInverseFractionCovariance
OrPositiveConnectedThirdCumulant
OrPrincipalOccupancy
```

Next: `Stage14-4dp`.
