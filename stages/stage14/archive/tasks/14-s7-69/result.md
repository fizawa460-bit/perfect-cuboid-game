# Stage14-s7-69 — canonical-allocation substitution into the first reciprocal equation

## Status

`COMPLETE_FIRST_RECIPROCAL_SELECTOR_ELIMINATION_ON_CANONICAL_ALLOCATION_BACKGROUND`

Consumes merged `Stage14-s7-68`, merged `Stage14-s7-66/67`, merged `Stage14-s7-46`, merged `Stage14-s7-60`, merged `Stage14-Work-blX24`, and latest merged main at batch start `972b63725cc3086d7993b558d75319b858b93e8a`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering receiver

Merged s7-68 writes the global s obstruction as

```text
mu_G = mu_can * mu_recip,
```

where `mu_can` is canonical balanced integer/Gaussian allocation density and `mu_recip` is conditional reciprocal/post-column completion density on that background. Work-blX24 confirms that the `B^o(1)` witness fibers are not independent saving lengths.

Stage14-s7-69 substitutes the exact first reciprocal identities into the canonical allocation coordinates.

## 2. Primitive signed factors are already fixed

Batch-local s7-66 gives, after the frozen common-scale and 2-primary decorations,

```text
D-A = g a,
D+A = g b,
gcd(a,b)=1,
g=B^o(1).
```

The canonical minus allocation chooses the physical agreement factors inside these two coprime signed factors. In the notation of merged s7-46,

```text
D+A = a_1 U,
D-A = b_1 V,
```

with `U,V` reconstructed from the minus allocation and therefore `a_1,b_1` forced. The number of such decorated reconstructions per canonical allocation witness is `B^o(1)`.

```text
CANONICAL_MINUS_ALLOCATION_FIXES_FIRST_SIGNED_QUOTIENT_DATA=true
FIRST_SIGNED_QUOTIENT_RECONSTRUCTION_MULTIPLICITY=Bo1
```

## 3. The first reciprocal equation is an identity after allocation reconstruction

Merged s7-46 uses the exact first reciprocal equation

```text
(a_1 U)^2-(b_1 V)^2 = 4 r s epsilon_k p q.
```

But the canonical signed factors give

```text
(a_1 U)^2-(b_1 V)^2
 = (D+A)^2-(D-A)^2
 = 4DA.
```

The endpoint factorization used throughout the theta-quarter packet is

```text
D=delta*s,
A=alpha*r,
```

so identically

```text
4DA = 4rs alpha delta.
```

After the fixed sign/2-primary convention, the k-agreement product is precisely the odd physical allocation of `alpha*delta`; hence `epsilon_k p q` is reconstructed from the same canonical witness. Therefore the first reciprocal equation does not impose a new Boolean condition after the canonical allocation witness is fixed.

```text
FIRST_RECIPROCAL_EQUATION_TAUTOLOGICAL_AFTER_CANONICAL_ALLOCATION=true
FIRST_RECIPROCAL_CONDITIONAL_DENSITY_FACTOR=1_UP_TO_Bo1_DECORATION=true
FIRST_RECIPROCAL_FIXED_POWER_SELECTOR_REMAINS=false
```

This is a selector elimination, not a power saving.

## 4. No double charge from the reconstructed k split

For fixed `alpha*delta`, the ordered coprime split `(p,q)` is divisor-many. This multiplicity was already charged as a finite fiber in merged s7-46/s7-60. It cannot be turned into either an additional density loss or an additional support length.

```text
K_AGREEMENT_SPLIT_MULTIPLICITY=Bo1
K_SPLIT_RECHARGE_ALLOWED=false
```

## 5. Updated reciprocal conditional event

After removing the first reciprocal identity, `mu_recip` is unchanged as a numerical conditional density but its live arithmetic content is smaller. It consists only of:

```text
1. opposite signed quotient / second reciprocal admissibility,
2. post-column reverse reciprocal completion,
3. all retained range/chart/orientation masks already frozen at allocation level.
```

Merged s7-42/X13 already makes post-column reverse reconstruction finite-fiber once the opposite reciprocal data are fixed. Hence the only possible polynomial-density selector inside `mu_recip` must occur before that final finite-fiber reconstruction.

```text
POST_COLUMN_REVERSE_COMPLETION_INDEPENDENT_POLYNOMIAL_SELECTOR=false
LIVE_RECIPROCAL_SELECTOR_MOVED_TO_OPPOSITE_SECOND_RECIPROCAL_STAGE=true
```

## 6. Receiver and H decision

The theorem-level receiver is not yet materially changed: it remains canonical allocation density times reciprocal conditional density, but the internal reciprocal predicate has been contracted.

```text
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_S_RECEIVER=PrimitiveCoprimeBinaryFormsCanonicalBalancedIntegerGaussianAllocationDensity_x_ConditionalOppositeReciprocalCompletionDensity
S7_69_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

Next: substitute the exact opposite reciprocal/root equation and determine whether it is another reconstructed identity or the first genuine arithmetic selector.

## Boundary

```text
STAGE14_S7_69=COMPLETE_FIRST_RECIPROCAL_SELECTOR_ELIMINATION_ON_CANONICAL_ALLOCATION_BACKGROUND
CANONICAL_MINUS_ALLOCATION_FIXES_FIRST_SIGNED_QUOTIENT_DATA=true
FIRST_RECIPROCAL_EQUATION_TAUTOLOGICAL_AFTER_CANONICAL_ALLOCATION=true
FIRST_RECIPROCAL_FIXED_POWER_SELECTOR_REMAINS=false
K_AGREEMENT_SPLIT_MULTIPLICITY=Bo1
POST_COLUMN_REVERSE_COMPLETION_INDEPENDENT_POLYNOMIAL_SELECTOR=false
LIVE_RECIPROCAL_SELECTOR_MOVED_TO_OPPOSITE_SECOND_RECIPROCAL_STAGE=true
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_69_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-70
```
