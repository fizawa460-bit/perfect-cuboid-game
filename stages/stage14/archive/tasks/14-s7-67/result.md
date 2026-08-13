# Stage14-s7-67 — primitive Gaussian norm support and plus-allocation normalization

## Status

`COMPLETE_PRIMITIVE_GAUSSIAN_NORM_SPLIT_PRIME_ALLOCATION_NORMALIZATION`

Consumes merged batch-start sources plus batch-local `Stage14-s7-66`. The theorem boundary remains latest merged main at batch start; batch-local predecessors are used only inside this one batch branch.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Odd prime support of a primitive sum of two squares

Let

```text
gcd(a,b)=1,
F_+(a,b)=oddpart(a^2+b^2).
```

If an odd prime `p|a^2+b^2`, then `p` cannot divide `a` or `b`. Hence `b` is invertible modulo `p` and

```text
(a b^{-1})^2 == -1 (mod p).
```

Therefore

```text
p == 1 (mod 4).
```

So every odd rational prime in the primitive plus core is Gaussian-split.

```text
PRIMITIVE_PLUS_CORE_ODD_PRIMES_ALL_SPLIT_MOD4=true
PRIMITIVE_PLUS_CORE_HAS_NO_3MOD4_ODD_PRIME=true
```

## 2. Canonical Gaussian orientation per rational prime

For each `p|F_+`, the primitive residue ratio selects one of the two roots of `-1 mod p`. Equivalently, exactly one conjugate Gaussian prime above `p` divides `a+ib` under a fixed unit convention, while its conjugate divides `a-ib`.

Thus after freezing the global unit/root convention already present in the Stage14 packet, no new polynomial orientation coordinate remains at a plus-core prime.

```text
PRIMITIVE_SLOPE_SELECTS_GAUSSIAN_CONJUGATE_PER_PLUS_PRIME=true
PLUS_PRIME_GAUSSIAN_ORIENTATION_IS_LOCALIZED=true
```

## 3. Physical plus allocation is a divisor/subset problem on split-prime support

The physical plus cells satisfy, after the merged endpoint and fixed mover-prime peel,

```text
M_+ = S*T
```

with balanced window, squarefree and coprime cell masks. On the squarefree physical support, choosing `(S,T)` is exactly choosing a subset of the eligible rational split-prime factors of the normalized plus core, subject to the physical size windows and the frozen decorations.

The Gaussian conjugate associated to each rational prime is already determined by `(a,b)`; the remaining plus allocation bit only decides which physical cell receives the rational norm prime.

```text
PLUS_ALLOCATION_IS_SPLIT_PRIME_SUBSET_DIVISOR_PROBLEM=true
PLUS_GAUSSIAN_CONJUGATE_CHOICE_NOT_SECOND_ALLOCATION_BIT=true
```

Merged s7-46 gives only divisor-many physical balanced witnesses for fixed outer data, so this normalization introduces no new support length.

## 4. No growing modulus follows from local splitting alone

The congruence `p==1 mod 4` and its selected root are exactly the existing Gaussian splitting data. They do not place `p` in a residue class modulo any growing external modulus and therefore cannot be charged as a fresh fixed-power density loss.

```text
PLUS_LOCAL_SPLITTING_GIVES_GROWING_MODULUS=false
PLUS_LOCAL_SPLITTING_NEW_FIXED_POWER_SAVING=false
```

## 5. Receiver

Both binary-form allocations now have canonical primitive coordinates:

```text
minus: divisors distributed across coprime a and b,
plus : split-prime divisors of a^2+b^2 with conjugate fixed by a/b.
```

Balanced windows and reciprocal/post-column acceptance remain coupled. This is still a normalization of the s7-65 receiver rather than a material receiver change.

```text
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_S_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanFixedSubpolynomialGaussianPrimeFixedRootFixedAtomicChartCoprimeBinaryFormsBalancedDivisorAllocationReciprocalAcceptancePrincipalDensity
```

## 6. H decision

No new sH is needed. The next internal stage should combine these canonical allocation coordinates with the exact nested densities of merged 4dz and determine what remains after allocation compatibility is expressed without redundant cross-sign or Gaussian-orientation conditions.

```text
S7_67_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_67=COMPLETE_PRIMITIVE_GAUSSIAN_NORM_SPLIT_PRIME_ALLOCATION_NORMALIZATION
PRIMITIVE_PLUS_CORE_ODD_PRIMES_ALL_SPLIT_MOD4=true
PRIMITIVE_SLOPE_SELECTS_GAUSSIAN_CONJUGATE_PER_PLUS_PRIME=true
PLUS_ALLOCATION_IS_SPLIT_PRIME_SUBSET_DIVISOR_PROBLEM=true
PLUS_GAUSSIAN_CONJUGATE_CHOICE_NOT_SECOND_ALLOCATION_BIT=true
PLUS_LOCAL_SPLITTING_GIVES_GROWING_MODULUS=false
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_67_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-68
```