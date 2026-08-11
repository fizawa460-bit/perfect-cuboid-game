# Stage14-s7-68 — canonical allocation background and reciprocal conditional-density receiver

## Status

`COMPLETE_CANONICAL_INTEGER_GAUSSIAN_ALLOCATION_BACKGROUND_AND_RECIPROCAL_CONDITIONAL_DENSITY_REDUCTION`

Consumes merged batch-start sources, merged `Stage14-4dz`, and batch-local `Stage14-s7-66/67`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Canonical allocation incidence space

For a primitive slope `(a,b)`, define a canonical allocation witness by the data

```text
minus side:
  divisors supported separately on a and b,
plus side:
  a balanced divisor split of the normalized odd core of a^2+b^2,
  whose rational primes are all 1 mod 4 and whose Gaussian conjugates are fixed by a/b,
plus the frozen B^o(1) endpoint/common-scale decorations.
```

Retain all physical balanced windows, squarefree/coprime masks, smooth/rough labels, chart and orientation locks. By merged s7-46 and s7-65, the number of physical candidate allocation witnesses per primitive slope is `B^o(1)`.

```text
CANONICAL_INTEGER_GAUSSIAN_ALLOCATION_SPACE_DEFINED=true
CANONICAL_ALLOCATION_WITNESS_MULTIPLICITY_PER_SLOPE=Bo1
```

## 2. Redundant allocation conditions are discharged

Batch-local s7-66/67 show that the following are already forced by primitive coordinates and therefore are not independent density selectors:

```text
cross-sign prime separation,
minus cross-coordinate coprimality,
odd plus-prime Gaussian splitting,
Gaussian conjugate orientation at each plus prime.
```

Thus the allocation-compatible event of merged 4dz can be rewritten on the canonical witness space without these redundant tests. What remains genuinely selective at allocation level is the correlated existence of divisors in the required physical windows/support classes for the two binary-form values.

```text
REDUNDANT_CROSS_SIGN_AND_GAUSSIAN_ORIENTATION_TESTS_DISCHARGED=true
CANONICAL_BALANCED_ALLOCATION_EVENT_EXPLICIT=true
```

## 3. Exact two-level density chain

Merged 4dz gives the exact nested chain

```text
A_phys <= E_alloc <= E_bal.
```

After absorbing the now-explicit allocation compatibility into the canonical balanced-allocation incidence space, define

```text
mu_can := density of primitive slopes admitting at least one canonical physical allocation witness,
mu_recip := conditional density that such a witness-bearing slope admits reciprocal/post-column completion.
```

The charged-once finite-fiber change from Boolean slopes to allocation incidences costs only `B^o(1)`. Therefore, on the exponent scale, the full acceptance density satisfies the exact cardinality-ratio chain

```text
mu_G = mu_can * mu_recip
```

when the two factors are defined on the nested Boolean slope families, and equivalently up to `B^o(1)` distortion on the witness incidence space.

No independence is assumed.

```text
CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true
INDEPENDENCE_ASSUMED=false
```

## 4. Saturation consequence

On any square-root-saturating arithmetic subsequence, merged 4dy/4dz give

```text
mu_G=B^(-o(1)).
```

Since `0<=mu_can,mu_recip<=1`, saturation forces both conditional factors to exponent zero. Conversely, any fixed-power deficit in either factor closes the arithmetic branch.

```text
SATURATION_FORCES_CANONICAL_ALLOCATION_DENSITY_EXPONENT_ZERO=true
SATURATION_FORCES_RECIPROCAL_CONDITIONAL_DENSITY_EXPONENT_ZERO=true
ANY_FIXED_POWER_DEFICIT_IN_EITHER_FACTOR_CLOSES_BRANCH=true
```

## 5. Material receiver change

The s7-65 opaque joint selector

```text
CoprimeBinaryFormsBalancedDivisorAllocationReciprocalAcceptancePrincipalDensity
```

has now split into two theorem-shaped nested targets with all elementary allocation redundancies removed:

```text
Target A:
PrimitiveCoprimeBinaryFormsCanonicalBalancedIntegerGaussianAllocationDensity

Target B:
ConditionalReciprocalPostColumnCompletionDensityOnCanonicalAllocationBackground.
```

This is a material receiver change: the next stage no longer needs to manipulate the six-block allocation masks abstractly. It must choose which of these two explicit conditional factors admits the next internal arithmetic reduction.

```text
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_S_RECEIVER=PrimitiveCoprimeBinaryFormsCanonicalBalancedIntegerGaussianAllocationDensity_x_ConditionalReciprocalPostColumnCompletionDensity
```

No fixed-power deficit is proved for either factor.

## 6. H decision

No new sH is opened at this boundary. The receiver has just changed, so the batch stops here by contract. A future s7-69 should first substitute the exact reciprocal equations into the canonical allocation coordinates; if that leaves a genuine averaged correlated-divisor theorem, it should then freeze an sH target.

```text
S7_68_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_68=COMPLETE_CANONICAL_INTEGER_GAUSSIAN_ALLOCATION_BACKGROUND_AND_RECIPROCAL_CONDITIONAL_DENSITY_REDUCTION
CANONICAL_INTEGER_GAUSSIAN_ALLOCATION_SPACE_DEFINED=true
REDUNDANT_CROSS_SIGN_AND_GAUSSIAN_ORIENTATION_TESTS_DISCHARGED=true
CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true
SATURATION_FORCES_CANONICAL_ALLOCATION_DENSITY_EXPONENT_ZERO=true
SATURATION_FORCES_RECIPROCAL_CONDITIONAL_DENSITY_EXPONENT_ZERO=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_68_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-69
```