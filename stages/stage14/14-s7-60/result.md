# Stage14-s7-60 — single-prime allocation / reciprocal influence packet

## Status

`COMPLETE_SINGLE_PRIME_DISJOINT_ALLOCATION_RECIPROCAL_INFLUENCE_LOCALIZATION`

Consumes merged `Stage14-s7-59`, merged `Stage14-4dp`, merged `Stage14-4do`, merged `Stage14-s7-46`, and latest main.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Stage14-s7-59 contracts the positive zero-mode arithmetic branch to one coupled receiver: disjoint balanced allocation plus reciprocal completion. Stage14-s7-60 writes that coupled receiver directly in the six-block mixed-root variables and localizes any square-root-saturating influence to one split prime allocation bit.

## 1. Six-block reconstruction

On a surviving square-root mixed-root packet put

```text
Q_mix=C_*u_*,
M_+=odd(D^2+A^2)/C_*,
M_-=odd(D^2-A^2)/u_*.
```

The physical packet requires

```text
M_+=S*T,
M_-=R*J,
```

with the already merged balanced, squarefree and pairwise-coprime cell constraints.

Merged s7-46 proves that once `(Q_mix,t,D,A)` and these divisor allocations are fixed, the signed quotient pair, k-agreement split, opposite reciprocal pair and post-column completion all have only `B^o(1)` multiplicity.

Hence reciprocal completion contributes no independent fixed-power coordinate after the divisor allocations are fixed.

```text
BALANCED_ALLOCATION_AND_RECIPROCAL_COMPLETION_SHARE_ONE_COORDINATE_PACKET=true
RECIPROCAL_COMPLETION_INDEPENDENT_FIXED_POWER_SUPPORT=false
```

## 2. Prime-allocation bit model

Because the six atomic blocks are fixed-power pairwise separated on any saturation sequence, every prime divisor of `M_+M_-` belongs to exactly one physical divisor cell up to `B^o(1)` exceptional support.

For one split prime `ell` in the unfrozen cofactor support, define one allocation bit `sigma_ell` recording which admissible physical divisor cell receives `ell` inside the relevant cofactor split.

Freeze all other prime allocations, all dyadic/range/chart side conditions and the mixed-root tuple. The two values of `sigma_ell` produce at most two candidate physical completions. By merged s7-46 each candidate has `B^o(1)` reciprocal/post-column completions.

Thus the conditional response to a single prime flip is a finite-fiber arithmetic object.

```text
SINGLE_PRIME_ALLOCATION_BIT_DEFINED=true
FIXED_OTHER_BITS_SINGLE_FLIP_COMPLETION_FIBER=Bo1
```

## 3. Exact local complementary-square packet

The allocation bit is not a free Bernoulli variable. The candidate cells must still satisfy the exact complementary-square identities

```text
C_* S T = odd(D^2+A^2) * B^o(1),
u_* R J = odd(D^2-A^2) * B^o(1),
```

and

```text
D^2=(X+Y)/2,
A^2=(X-Y)/2,
X=C_*ST,
Y=u_*RJ,
```

under the fixed endpoint / 2-primary convention.

Therefore moving one split prime between admissible divisor cells changes the candidate pair `(X,Y)` only through its divisor allocation while the square reconstruction requires simultaneously

```text
(X+Y)/2 is a square,
(X-Y)/2 is a square.
```

The local prime influence is exactly the symmetric difference of physical admissibility between the two divisor allocations after these two square conditions and all retained side masks are imposed.

```text
SINGLE_PRIME_INFLUENCE_HAS_EXPLICIT_TWO_SQUARE_ADMISSIBILITY_PACKET=true
```

## 4. No fresh divisor-switch saving yet

A divisor switch merely reparametrizes the same factorization packet. Since fixed `(X,Y)` recovers `(D,A)` with `B^o(1)` ambiguity and fixed `(D,A)` recovers the physical split with divisor-many ambiguity, forward and reverse divisor-switch ledgers both remain at exponent `1/2`.

No second factor `1/ell`, no independent modulus spacing, and no extra reciprocal support may be charged from the same prime allocation bit.

```text
FRESH_DIVISOR_SWITCH_FIXED_POWER_SAVING_PROVED=false
SINGLE_PRIME_DOUBLE_CHARGE_ALLOWED=false
```

## 5. Pigeonhole consequence

Merged s7-59 gives an `O(1)` mask-level influence decomposition. Within the one arithmetic receiver, expand the residual divisor allocation through its prime-allocation bits. If every active split-prime bit had fixed-power-small conditional response, the total arithmetic uplift would be fixed-power small after the existing `B^o(1)` support convention.

Hence any square-root-saturating zero-mode arithmetic sequence must contain at least one active split prime whose conditional physical-admissibility response is exponent-zero:

```text
max_ell Influence(ell)=B^(-o(1)).
```

This is a localization statement, not a saving theorem.

```text
SQRT_ARITHMETIC_UPLIFT_REQUIRES_EXPONENT_ZERO_SINGLE_PRIME_INFLUENCE=true
```

## 6. Minimal receiver

The remaining arithmetic receiver is now

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
DisjointPrimeSingleAllocationTwoSquareReciprocalAdmissibilityInfluence.
```

The variable package is:

```text
mixed-root tuple (Q_mix,t,D,A),
cofactor products M_+,M_-,
one active split prime ell,
all other divisor allocations frozen,
all range/chart/orientation side masks retained,
physical admissibility tested by the two complementary square conditions
plus the B^o(1)-fiber reciprocal completion.
```

This is theorem-ready enough to ask whether a local prime flip has a fixed-power influence deficit or whether a finite-energy / character-sum identity controls the average influence.

## 7. H decision

No new H is opened at s7-60.

Reason: the arithmetic object has only now become a single-prime explicit two-square influence packet. The next internal step should derive the exact congruence condition for one `ell`-flip and test whether the influence is supported on a thin residue set. An external theorem audit before that local congruence calculation is premature.

```text
S7_60_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_60=COMPLETE_SINGLE_PRIME_DISJOINT_ALLOCATION_RECIPROCAL_INFLUENCE_LOCALIZATION
BALANCED_ALLOCATION_AND_RECIPROCAL_COMPLETION_SHARE_ONE_COORDINATE_PACKET=true
RECIPROCAL_COMPLETION_INDEPENDENT_FIXED_POWER_SUPPORT=false
SINGLE_PRIME_ALLOCATION_BIT_DEFINED=true
FIXED_OTHER_BITS_SINGLE_FLIP_COMPLETION_FIBER=Bo1
SINGLE_PRIME_INFLUENCE_HAS_EXPLICIT_TWO_SQUARE_ADMISSIBILITY_PACKET=true
FRESH_DIVISOR_SWITCH_FIXED_POWER_SAVING_PROVED=false
SINGLE_PRIME_DOUBLE_CHARGE_ALLOWED=false
SQRT_ARITHMETIC_UPLIFT_REQUIRES_EXPONENT_ZERO_SINGLE_PRIME_INFLUENCE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_60_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
REMAINING_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanDisjointPrimeSingleAllocationTwoSquareReciprocalAdmissibilityInfluence
NEXT=Stage14-s7-61
```
