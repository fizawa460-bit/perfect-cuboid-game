# Stage14-4ec — second-reciprocal difference-of-squares divisor predicate

## Status

`COMPLETE_SECOND_RECIPROCAL_REVERSE_DIVISOR_PAIR_LOCALIZATION`

Consumes batch-local `Stage14-4eb` and merged `Stage14-X13`, `Stage14-s7-46`, `Stage14-s7-68`, `Stage14-4ea`. The theorem boundary remains merged main at batch start; batch-local predecessors are used only inside this batch.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Entering reciprocal survivor

Stage14-4eb discharges the first reciprocal equation as reconstruction after canonical allocation. Retain one primitive slope and one canonical allocation incidence, including one allowed `B^o(1)` common-scale / endpoint decoration.

Merged s7-46/X13 show that the outer data entering the opposite reciprocal packet are then fixed up to `B^o(1)` ambiguity. In X13 notation the exact second reciprocal equation is

```text
(c p)^2-(d q)^2
 = 4 X Y epsilon_x U V.
```

For one fixed outer decoration put

```text
W_2 := 4 X Y epsilon_x U V > 0.
```

## 2. Reverse difference-of-squares factorization

Every physical completion satisfies

```text
(c p-d q)(c p+d q)=W_2.
```

Hence define

```text
F_2^- := c p-d q,
F_2^+ := c p+d q,
```

so

```text
F_2^- F_2^+ = W_2,
0<F_2^-<F_2^+.
```

Conversely one positive factor pair of `W_2` with the required parity gives

```text
c p=(F_2^++F_2^-)/2,
d q=(F_2^+-F_2^-)/2.
```

Each resulting positive product has divisor-many ordered splittings into `(c,p)` and `(d,q)`. Therefore

```text
fixed canonical allocation incidence + fixed allowed decoration
=> # second-reciprocal candidate tuples = B^o(1).
```

This is exactly the X13 reverse-reciprocal mechanism, now placed after the canonical allocation localization of 4ea/4eb.

```text
SECOND_RECIPROCAL_DIFFERENCE_OF_SQUARES_FACTORING_EXACT=true
SECOND_RECIPROCAL_CANDIDATE_MULTIPLICITY=Bo1
SECOND_RECIPROCAL_POLYNOMIAL_SUPPORT_AFTER_OUTER_FIXING=false
```

## 3. Existence remains a Boolean arithmetic selector

The divisor bound controls candidate multiplicity only. A candidate factor pair must still satisfy all transported physical conditions, including

```text
parity and positivity,
required divisibility into p,q,c,d,
dyadic / balanced windows,
squarefree and coprimality masks,
common-core / Cayley row congruence filters,
post-column reconstruction masks.
```

Define

```text
R_2(w)=1
```

for a canonical allocation incidence `w` iff at least one divisor pair `F_2^-F_2^+=W_2(w)` passes every surviving physical filter.

Then the reciprocal conditional density is the density of this Boolean divisor-pair event on the canonical allocation background, up to the already-charged `B^o(1)` incidence/decoration fibers.

```text
SECOND_RECIPROCAL_ACCEPTANCE_IS_BOOLEAN_DIVISOR_PAIR_EVENT=true
DIVISOR_MULTIPLICITY_IMPLIES_DENSITY_SAVING=false
```

## 4. Next

Stage14-4ed should consume X13's row/post-column quantifier order and determine whether the remaining Cayley/post-column conditions produce a second polynomial selector or are only filters on the same divisor-pair candidates.

## Boundary

```text
STAGE14_4EC=COMPLETE_SECOND_RECIPROCAL_REVERSE_DIVISOR_PAIR_LOCALIZATION
SECOND_RECIPROCAL_DIFFERENCE_OF_SQUARES_FACTORING_EXACT=true
SECOND_RECIPROCAL_CANDIDATE_MULTIPLICITY=Bo1
SECOND_RECIPROCAL_POLYNOMIAL_SUPPORT_AFTER_OUTER_FIXING=false
SECOND_RECIPROCAL_ACCEPTANCE_IS_BOOLEAN_DIVISOR_PAIR_EVENT=true
DIVISOR_MULTIPLICITY_IMPLIES_DENSITY_SAVING=false
RECIPROCAL_CONDITIONAL_FIXED_POWER_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ed
```
