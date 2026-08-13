# Stage14-4dt — finite candidate support for one Gaussian mover prime

## Status

`COMPLETE_FINITE_DIVISOR_CANDIDATE_SUPPORT_NO_WHOLE_FAMILY_SAVING`

Consumes merged `Stage14-4ds`, merged `Stage14-s7-61`, merged `Stage14-Work-bhX20`, and latest main. Unmerged descendants are advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering mover receiver

Stage14-4ds reduces the live zero-mode arithmetic obstruction to an already-Gaussian split prime `ell` whose allocation flip crosses the two-square physical boundary. After all other cofactor data are frozen, write the two local allocation states as

```text
state + : (X,Y)=(ell*x,y),
state - : (X,Y)=(x,ell*y),
```

with `gcd(ell,2xy)=1` and all physical side masks retained.

## 2. Plus-state admissibility gives divisor-many ell candidates

If the plus state is admissible, then for integers `D,A`

```text
ell*x + y = 2D^2,
ell*x - y = 2A^2.
```

Hence

```text
y=(D-A)(D+A),
ell=(D^2+A^2)/x.
```

Thus every admissible plus-state mover prime arises from one factorization

```text
y = r*s,
r=D-A,
s=D+A,
r<s,
r == s (mod 2),
```

followed by

```text
D=(r+s)/2,
A=(s-r)/2,
ell=(D^2+A^2)/x.
```

For fixed `(x,y)`, the number of such candidate values is at most divisor-many:

```text
#Cand_+(x,y) <= tau(y)=B^o(1)
```

on the retained Stage14 size range.

## 3. Minus-state admissibility is likewise divisor/representation-many

If the minus state is admissible, then

```text
x + ell*y = 2D^2,
x - ell*y = 2A^2,
```

so

```text
x=D^2+A^2,
ell*y=D^2-A^2.
```

The number of representations of fixed `x` as a sum of two squares is bounded by `B^o(1)` via the standard divisor bound, and each representation determines at most one candidate `ell`.

Therefore

```text
#Cand_-(x,y)=B^o(1).
```

Combining both states,

```text
#Cand_mover(x,y)=B^o(1).
```

This replaces the informal picture of a positive-density continuum of eligible mover primes by a finite divisor/representation candidate list after the frozen cofactor state is fixed.

```text
FIXED_FROZEN_STATE_MOVER_PRIME_CANDIDATE_COUNT=Bo1
MOVER_PRIME_CONTINUUM_AFTER_FREEZING=false
```

## 4. Why this does not yet beat square root

The candidate-list bound is conditional on fixing the outer cofactor state `(x,y)` and all other allocation data. Those frozen states themselves carry the entire currently surviving `B^(1/2+o(1))` support.

A `B^o(1)` candidate list per state therefore gives only

```text
#states * B^o(1),
```

which remains compatible with the square-root bound. The divisor representation cannot be charged again as an independent saving because the same factorization data are already part of the physical allocation ledger.

Hence

```text
FINITE_CANDIDATE_SUPPORT_GIVES_FIXED_POWER_SAVING=false
CANDIDATE_LIST_DOUBLE_CHARGE_ALLOWED=false
```

The obstruction has moved from prime density to **weighted concentration across frozen states**: square-root saturation requires `B^(1/2-o(1))` total state mass to land on states carrying at least one physically admissible mover candidate with exponent-zero aggregate conditional influence.

## 5. New minimal receiver

The surviving object is

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FrozenCofactorStateWeightedGaussianMoverCandidateConcentration.
```

Equivalently: estimate the weighted incidence between frozen cofactor states `(x,y)` and their divisor-generated candidate mover primes, with the two-square, balanced, range, chart, primitive, and reciprocal-completion masks all retained.

A future fixed-power saving may come from a collision/energy estimate for the map

```text
(state factorization data) -> ell candidate,
```

or from proving that the candidate-bearing frozen states occupy only `B^(1/2-delta+o(1))` total mass. Neither statement is presently merged.

## 6. H decision

No new H is opened. The next step is internal: test the multiplicity/energy of the candidate map across frozen states before asking for an external theorem.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4DT=COMPLETE_FINITE_DIVISOR_CANDIDATE_SUPPORT_NO_WHOLE_FAMILY_SAVING
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
FIXED_FROZEN_STATE_MOVER_PRIME_CANDIDATE_COUNT=Bo1
MOVER_PRIME_CONTINUUM_AFTER_FREEZING=false
FINITE_CANDIDATE_SUPPORT_GIVES_FIXED_POWER_SAVING=false
CANDIDATE_LIST_DOUBLE_CHARGE_ALLOWED=false
SQRT_OBSTRUCTION_REDUCED_TO_WEIGHTED_MOVER_CANDIDATE_CONCENTRATION=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

Next: `Stage14-4du`.
