# Stage14-4ea — canonical allocation density versus reciprocal conditional density

## Status

`COMPLETE_THREE_LEVEL_NESTED_DENSITY_TO_CANONICAL_TWO_FACTOR_RECEIVER`

Consumes merged `Stage14-4dz`, merged `Stage14-s7-65`, merged s-batch `Stage14-s7-66..68`, merged `Stage14-Work-blX24`, and latest main. Unmerged descendants are advisory only.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Supersede the three-level 4dz density chain

Merged 4dz gave the exact nested factorization

```text
mu_G = mu_bal * mu_alloc * mu_comp
```

with no independence assumption.

Merged s7-66 and s7-67 then normalize the two primitive binary-form allocation spaces:

```text
minus: divisors supported separately on coprime a and b,
plus : split-prime divisors of oddpart(a^2+b^2),
       with Gaussian conjugate orientation already fixed by a/b.
```

Thus cross-sign separation, minus cross-coordinate coprimality, odd plus-prime splitting, and Gaussian conjugate choice are not independent selectors.

Merged s7-68 absorbs all remaining allocation compatibility into one canonical balanced integer/Gaussian allocation event and proves the exact two-level chain

```text
boxed:
mu_G = mu_can * mu_recip,
```

where

```text
mu_can
 = density of primitive slopes carrying at least one canonical physical
   balanced allocation witness,

mu_recip
 = conditional density that a canonical-allocation-bearing slope admits
   reciprocal / post-column completion.
```

Therefore the earlier three-factor chain is retained only as provenance. Its current charged-once theorem form is the two-factor chain above.

```text
MERGED_4DZ_THREE_LEVEL_CHAIN_IMPORTED=true
MERGED_S7_68_TWO_LEVEL_CHAIN_IMPORTED=true
THREE_LEVEL_CHAIN_SUPERSEDED_BY_CANONICAL_TWO_FACTOR_RECEIVER=true
CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true
INDEPENDENCE_ASSUMED=false
```

## 2. Canonical allocation density is a correlated binary-form problem

On the frozen primitive-slope family

```text
gcd(a,b)=1,
0<a<b,
H=max(a,b)=B^(1/4+o(1)),
```

with fixed heavy Gaussian prime, fixed root orientation, and fixed atomic chart, define

```text
F_-(a,b)=oddpart(ab),
F_+(a,b)=oddpart(a^2+b^2).
```

Merged s7-65 proves

```text
gcd(F_+,F_-)=1.
```

Merged s7-66/67 identify the physical allocation coordinates exactly:

```text
F_- : balanced divisor choices distributed across the coprime coordinates a,b,
F_+ : balanced subset/divisor choices on split rational primes of a^2+b^2,
      with the Gaussian conjugate fixed by the primitive slope.
```

Hence `mu_can` is not a generic one-integer balanced-divisor density. It is the joint density that these two coprime binary-form values simultaneously admit all retained physical window/support/squarefree/smooth-rough allocation constraints.

Merged s7-47/s7-65 already forbid claiming a fixed-power deficit from balanced divisor-window existence alone.

```text
CANONICAL_ALLOCATION_IS_CORRELATED_COPRIME_BINARY_FORM_EVENT=true
GENERIC_BALANCED_DIVISOR_EXISTENCE_FIXED_POWER_SAVING_AVAILABLE=false
CROSS_SIGN_PRIME_SEPARATION_RECHARGE_ALLOWED=false
GAUSSIAN_ORIENTATION_RECHARGE_ALLOWED=false
```

No fixed-power upper bound for `mu_can` is presently merged.

## 3. Reciprocal completion is conditional on the same allocation background

For each primitive slope, the number of canonical allocation witnesses is `B^o(1)`. Once a canonical allocation witness is fixed, merged s7-46/s7-60 reconstruct the signed quotient data and leave reciprocal / second-reciprocal / post-column completion as a Boolean admissibility test with `B^o(1)` completion multiplicity.

Thus `mu_recip` is genuinely a conditional density on the canonical allocation-bearing family. It is not a second independent support length and may not be multiplied with witness multiplicity as an additional saving.

```text
RECIPROCAL_COMPLETION_IS_CONDITIONAL_BOOLEAN_ON_CANONICAL_ALLOCATION=true
CANONICAL_ALLOCATION_WITNESS_MULTIPLICITY=Bo1
RECIPROCAL_COMPLETION_WITNESS_MULTIPLICITY=Bo1
FINITE_WITNESS_MULTIPLICITY_RECHARGE_ALLOWED=false
BALANCED_AND_RECIPROCAL_DOUBLE_CHARGE_ALLOWED=false
```

No fixed-power upper bound for `mu_recip` is presently merged.

## 4. Saturation forces both factors to exponent zero

Merged 4dy/4dz give on every square-root-saturating global arithmetic subsequence

```text
mu_G=B^(-o(1)).
```

Since

```text
0 <= mu_can, mu_recip <= 1
```

and

```text
mu_G=mu_can*mu_recip,
```

square-root saturation forces

```text
mu_can   = B^(-o(1)),
mu_recip = B^(-o(1))
```

in the lower-bound exponent-zero sense.

Conversely either estimate

```text
mu_can   <= B^(-delta+o(1))
```

or

```text
mu_recip <= B^(-delta+o(1))
```

for any fixed `delta>0` closes this range-stable arithmetic branch.

```text
SATURATION_FORCES_CANONICAL_ALLOCATION_DENSITY_EXPONENT_ZERO=true
SATURATION_FORCES_RECIPROCAL_CONDITIONAL_DENSITY_EXPONENT_ZERO=true
ANY_FIXED_POWER_DEFICIT_IN_EITHER_FACTOR_CLOSES_BRANCH=true
```

## 5. Work-blX24 no-go consumed

Merged Work-blX24 proves that the global primitive-slope polynomial background cannot be directly identified with the subpolynomial fixed-Q Gaussian background fiber from the fixed-U route. Therefore no fixed-U local-fiber density theorem may be cross-promoted here.

The legal mainline saving levels are exactly the two global polynomial conditional factors above.

```text
DIRECT_GLOBAL_TO_FIXED_Q_FIBER_DENSITY_ADAPTER_NOGO=true
FIXED_U_LOCAL_FIBER_SAVING_CROSS_PROMOTED=false
GLOBAL_PRINCIPAL_POLYNOMIAL_SCALE_REMAINS_PRIMITIVE_SLOPE_BACKGROUND=true
```

## 6. Canonical mainline receiver

The 4dz receiver

```text
NestedPrimitiveSlopeBalancedAllocationCompletionDensities
```

contracts to

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
PrimitiveCoprimeBinaryForms
CanonicalBalancedIntegerGaussianAllocationDensity
x
ConditionalReciprocalPostColumnCompletionDensity.
```

The two factors are theorem-shaped but neither has yet been arithmetically reduced to a known external theorem class.

The next mainline step should follow the s7-68 recommendation and substitute the exact signed reciprocal equations into the canonical `(a,b)` allocation coordinates. This tests whether `mu_recip` collapses to an explicit low-degree divisibility/congruence condition. If not, the alternative is to attack `mu_can` as a correlated balanced-divisor problem for `ab` and `a^2+b^2`.

```text
SQRT_OBSTRUCTION_REDUCED_TO_CANONICAL_ALLOCATION_OR_RECIPROCAL_CONDITIONAL_DENSITY=true
CANONICAL_ALLOCATION_FIXED_POWER_DEFICIT_PROVED=false
RECIPROCAL_CONDITIONAL_FIXED_POWER_DEFICIT_PROVED=false
```

## 7. H decision

No new H is opened at 4ea. The reciprocal equations have not yet been substituted into the now-canonical allocation coordinates, so the exact external theorem shape is still premature.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4EA=COMPLETE_THREE_LEVEL_NESTED_DENSITY_TO_CANONICAL_TWO_FACTOR_RECEIVER
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
THREE_LEVEL_CHAIN_SUPERSEDED_BY_CANONICAL_TWO_FACTOR_RECEIVER=true
CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true
CANONICAL_ALLOCATION_IS_CORRELATED_COPRIME_BINARY_FORM_EVENT=true
RECIPROCAL_COMPLETION_IS_CONDITIONAL_BOOLEAN_ON_CANONICAL_ALLOCATION=true
SATURATION_FORCES_CANONICAL_ALLOCATION_DENSITY_EXPONENT_ZERO=true
SATURATION_FORCES_RECIPROCAL_CONDITIONAL_DENSITY_EXPONENT_ZERO=true
SQRT_OBSTRUCTION_REDUCED_TO_CANONICAL_ALLOCATION_OR_RECIPROCAL_CONDITIONAL_DENSITY=true
CANONICAL_ALLOCATION_FIXED_POWER_DEFICIT_PROVED=false
RECIPROCAL_CONDITIONAL_FIXED_POWER_DEFICIT_PROVED=false
DIRECT_GLOBAL_TO_FIXED_Q_FIBER_DENSITY_ADAPTER_NOGO=true
MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
```

Next: `Stage14-4eb`.
