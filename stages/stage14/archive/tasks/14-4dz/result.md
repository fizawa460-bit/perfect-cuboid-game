# Stage14-4dz — nested physical-acceptance density factorization

## Status

`COMPLETE_PRIMITIVE_SLOPE_ACCEPTANCE_TO_NESTED_CONDITIONAL_DENSITIES`

Consumes merged `Stage14-4dy`, merged `Stage14-s7-64`, merged `Stage14-Work-bkX23`, and latest main at branch creation (`51a0228d727103abb7f73bcc1cf5be244e60cbb2`). Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering principal-density receiver

Merged `4dy` reduces the range-stable global arithmetic obstruction to one fixed Boolean selector

```text
A_phys(a,b) in {0,1}
```

on the frozen primitive-slope background family `Omega_G(B)`, where all of

```text
ell_* = B^o(1) fixed,
Gaussian root orientation fixed,
atomic mover chart fixed,
gcd(a,b)=1,
0<a<b,
a == epsilon_* i_* b (mod ell_*),
positive-width transported slope/height windows
```

have already been localized.

The ambient family has

```text
|Omega_G(B)| = B^(1/2+o(1)),
```

and on every square-root-saturating arithmetic subsequence

```text
mu_G := E_{Omega_G} A_phys = B^(-o(1))
```

in the lower-bound exponent-zero sense.

Merged `s7-64` leaves exactly one internal witness decomposition to perform:

```text
(a) balanced divisor-in-window existence,
(b) disjoint smooth/rough allocation compatibility,
(c) reciprocal/post-column completion.
```

The point of `4dz` is to make this decomposition exact without assuming probabilistic independence.

## 2. Three nested Boolean events

For one slope `omega=(a,b) in Omega_G(B)`, let `W_0(omega)` be the divisor-many candidate allocation witnesses obtained from the reconstructed complementary cofactors after the already-frozen `B^o(1)` endpoint / 2-primary / common-scale decorations.

Define three Boolean events.

### Level 1: balanced divisor-window existence

```text
E_bal(omega)=1
```

iff at least one candidate witness in `W_0(omega)` realizes the required balanced plus/minus divisor splits in the transported dyadic windows, including the squarefree/coprime conditions already belonging to the physical xi-cell split.

### Level 2: physical prime-allocation compatibility

```text
E_alloc(omega)=1
```

iff at least one `E_bal` witness also satisfies the frozen-chart disjoint smooth/rough prime-allocation compatibility and all allocation-side primitive/gcd decorations.

By definition,

```text
E_alloc <= E_bal.
```

### Level 3: full reciprocal completion

```text
E_comp(omega)=A_phys(omega)
```

iff at least one `E_alloc` witness admits the full signed reciprocal / opposite reciprocal / post-column completion retained by merged `s7-64`.

Therefore pointwise

```text
A_phys = E_comp <= E_alloc <= E_bal <= 1.
```

No independence statement is made or needed.

```text
NESTED_ACCEPTANCE_EVENTS_DEFINED=true
FULL_ACCEPTANCE_SUBSET_ALLOCATION_SUBSET_BALANCED=true
INDEPENDENCE_ASSUMED=false
```

## 3. Exact conditional-density factorization

Use normalized counting measure on `Omega_G(B)` and define

```text
mu_bal   := P(E_bal=1),
mu_alloc := P(E_alloc=1 | E_bal=1),
mu_comp  := P(E_comp=1  | E_alloc=1).
```

Whenever `mu_G>0`, the nesting gives the exact chain-rule identity

```text
boxed:
mu_G = mu_bal * mu_alloc * mu_comp.
```

This is not a heuristic product of unrelated local densities. `mu_alloc` and `mu_comp` are conditional densities on the actual surviving witness-bearing slope families.

Equivalently, writing

```text
Omega_bal   = {omega : E_bal(omega)=1},
Omega_alloc = {omega : E_alloc(omega)=1},
Omega_comp  = {omega : A_phys(omega)=1},
```

one has exactly

```text
mu_bal   = |Omega_bal|/|Omega_G|,
mu_alloc = |Omega_alloc|/|Omega_bal|,
mu_comp  = |Omega_comp|/|Omega_alloc|,
```

and telescoping of cardinality ratios gives the product above.

```text
GLOBAL_ACCEPTANCE_DENSITY_CHAIN_RULE_EXACT=true
BALANCED_ALLOCATION_COMPLETION_DENSITIES_NOT_DOUBLE_CHARGED=true
```

## 4. Saturation forces every conditional factor to exponent zero

On a square-root-saturating arithmetic sequence merged `4dy` gives

```text
mu_G = B^(-o(1)).
```

Every factor in

```text
mu_G = mu_bal * mu_alloc * mu_comp
```

lies in `[0,1]`. Hence no factor may have a fixed positive power deficit on such a sequence.

More precisely, if for some fixed `delta>0` any one factor satisfied

```text
mu_bal   <= B^(-delta+o(1)),
```

or

```text
mu_alloc <= B^(-delta+o(1)),
```

or

```text
mu_comp  <= B^(-delta+o(1)),
```

then automatically

```text
mu_G <= B^(-delta+o(1)),
```

contradicting square-root saturation and yielding the desired strict sub-square-root saving on this arithmetic branch.

Therefore every saturating sequence necessarily has

```text
mu_bal   = B^(-o(1)),
mu_alloc = B^(-o(1)),
mu_comp  = B^(-o(1))
```

in the exponent-zero lower-bound sense.

```text
SATURATION_FORCES_BALANCED_DENSITY_EXPONENT_ZERO=true
SATURATION_FORCES_CONDITIONAL_ALLOCATION_DENSITY_EXPONENT_ZERO=true
SATURATION_FORCES_CONDITIONAL_COMPLETION_DENSITY_EXPONENT_ZERO=true
ANY_ONE_FIXED_POWER_FACTOR_DEFICIT_CLOSES_ARITHMETIC_BRANCH=true
```

This is a structural reduction, not itself a saving.

## 5. Witness multiplicity does not alter the exponent ledger

Merged `s7-64` gives

```text
PHYSICAL_ACCEPTANCE_WITNESS_MULTIPLICITY_PER_DIRECTION=B^o(1).
```

The balanced allocation witness set and completion fibers are likewise divisor/subpolynomial size after the primitive slope and frozen labels are fixed.

Consequently replacing direction counts by charged-once witness-incidence counts changes all three levels by at most `B^o(1)` factors. Thus the same exponent-zero conclusion holds if one works on the balanced-witness incidence space instead of the Boolean slope space.

However, this finite-fiber equivalence does **not** provide another density factor to multiply into the chain rule. It is only a change of measure up to subpolynomial distortion.

```text
BOOLEAN_TO_WITNESS_INCIDENCE_EXPONENT_PRESERVED=true
FINITE_WITNESS_MULTIPLICITY_RECHARGE_ALLOWED=false
```

## 6. What earlier balanced-split results imply

Merged `s7-47` already showed that bare balanced squarefree divisor-split existence is not generically fixed-power sparse in the ambient reconstructed cofactor ranges. That result does not prove that the present correlated primitive-slope factor `mu_bal` is exponent zero unconditionally, but it prevents treating a naive generic divisor-density heuristic as a proven saving.

Accordingly the current legal theorem targets are sharper:

```text
Target A:
fixed-prime/fixed-root primitive-slope dual-balanced-divisor density;

Target B:
conditional disjoint smooth/rough allocation density inside balanced slopes;

Target C:
conditional reciprocal/post-column completion density inside allocation-compatible slopes.
```

A power saving in any one target is sufficient; none is currently merged.

```text
GENERIC_BALANCED_SPLIT_HEURISTIC_CROSS_PROMOTED_AS_SAVING=false
FIXED_POWER_BALANCED_DENSITY_DEFICIT_PROVED=false
FIXED_POWER_CONDITIONAL_ALLOCATION_DEFICIT_PROVED=false
FIXED_POWER_CONDITIONAL_COMPLETION_DEFICIT_PROVED=false
```

## 7. New minimal receiver

The opaque principal density of `4dy` is now replaced by a charged-once nested density trichotomy:

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FixedSubpolynomialGaussianPrimeFixedRootFixedAtomicChart
PrimitiveRationalSlope
[
  DualBalancedDivisorWindowDensity
  x ConditionalDisjointPrimeAllocationDensity
  x ConditionalReciprocalCompletionDensity
].
```

The brackets denote the exact chain rule on nested events, not an independence factorization.

The next mainline task should identify which of the three conditional factors can be written as the most rigid explicit arithmetic predicate after all frozen labels are substituted. The natural first check is whether `E_alloc | E_bal` collapses to a canonical prime-allocation condition already present elsewhere in Stage14; if not, `E_comp | E_alloc` becomes the next irreducible receiver.

## 8. H decision

No new H is opened at `4dz`.

Reason: the principal density has only now been split into theorem-shaped conditional factors. One more internal substitution is needed to expose the exact arithmetic coefficients and quantifier order of `mu_alloc` or `mu_comp`; opening a broad sieve/dispersion H before that would risk theorem-shape mismatch.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4DZ=COMPLETE_PRIMITIVE_SLOPE_ACCEPTANCE_TO_NESTED_CONDITIONAL_DENSITIES
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NESTED_ACCEPTANCE_EVENTS_DEFINED=true
FULL_ACCEPTANCE_SUBSET_ALLOCATION_SUBSET_BALANCED=true
INDEPENDENCE_ASSUMED=false
GLOBAL_ACCEPTANCE_DENSITY_CHAIN_RULE_EXACT=true
SATURATION_FORCES_BALANCED_DENSITY_EXPONENT_ZERO=true
SATURATION_FORCES_CONDITIONAL_ALLOCATION_DENSITY_EXPONENT_ZERO=true
SATURATION_FORCES_CONDITIONAL_COMPLETION_DENSITY_EXPONENT_ZERO=true
ANY_ONE_FIXED_POWER_FACTOR_DEFICIT_CLOSES_ARITHMETIC_BRANCH=true
BOOLEAN_TO_WITNESS_INCIDENCE_EXPONENT_PRESERVED=true
FINITE_WITNESS_MULTIPLICITY_RECHARGE_ALLOWED=false
FIXED_POWER_BALANCED_DENSITY_DEFICIT_PROVED=false
FIXED_POWER_CONDITIONAL_ALLOCATION_DEFICIT_PROVED=false
FIXED_POWER_CONDITIONAL_COMPLETION_DEFICIT_PROVED=false
SQRT_OBSTRUCTION_REDUCED_TO_NESTED_PRIMITIVE_SLOPE_ACCEPTANCE_DENSITIES=true
MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
```

Next: `Stage14-4ea`.
