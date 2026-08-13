# Stage14-q17 — reciprocal divisor/CRT support literature radar

## Trigger header

```text
TRIGGER_STAGE=Stage14-4gd+Stage14-4ge
EXACT_OBSTRUCTION=FixedAgreementPairRadialLinearTwoLevelDivisorCRTReciprocalSolvabilitySupport
CURRENT_BEST_BOUND=ambient_primitive_pair_support_B^(kappa+o(1))_with_fixed_pair_candidate_multiplicity_B^o(1)_but_no_uniform_lower_bound_for_nonempty_reciprocal_support
WHY_EXISTING_Q_LEDGER_DOES_NOT_ALREADY_ANSWER_IT=q16_only_resolves_ambient_rectangular_product_capacity_and_explicitly_leaves_conditional_physical_lift_unsearched
SEARCH_FAMILIES=divisor_function_in_arithmetic_progressions;factorable_or_smooth_moduli;divisor_support_in_intervals;binary_form_divisor_sums;linear_divisor_correlations
LAST_RADAR_BASELINE=Stage14-q16
PROMOTION_STANDARD=uniform_principal_cell_support_bound_sharp_at_B_power_scale_preserving_exact_reciprocal_CRT_filters_and_quantifier_order
```

Search date: 2026-08-12.

Only primary papers/preprints are used for the candidate ledger below.

## 1. Frozen Stage14 target

On a fixed-E two-sided principal primitive rectangle, merged 4gd/4ge reduce one part of the physical completion problem to the Boolean

```text
B_rec(u,v)=1{Omega_rec(u,v) nonempty},
```

where a reciprocal witness requires choices satisfying

```text
p | H0*x*u*v,
q | H0*y*u*v,
F_-*F_+ = 4*r*s*epsilon_k*p*q,
F_+ + F_- == 0 (mod 2U),
F_+ - F_- == 0 (mod 2V),
```

plus the already-frozen parity/positivity/endpoint-small divisibility conditions.

The exact target is the support

```text
T_rec={(u,v):B_rec(u,v)=1}
```

inside

```text
R_prim={(u,v):u in D,v in V,gcd(u,v)=1},
#R_prim=B^(kappa+o(1)).
```

Near threshold, a surviving heavy packet requires

```text
#T_rec=B^(kappa-o(1)).
```

The existing bound

```text
#Omega_rec(u,v)<=B^o(1)
```

is only a witness-multiplicity upper bound. It does not imply that `Omega_rec(u,v)` is nonempty on a positive-power proportion of pairs.

## 2. Candidate A — Grimmelt--Merikoski, divisor function in arithmetic progressions

Primary source:

```text
Lasse Grimmelt, Jori Merikoski,
"The divisor function along arithmetic progressions and binary cubic polynomials",
arXiv:2508.17979 (2025).
```

Their paper proves new equidistribution estimates for the divisor function in arithmetic progressions to moduli with two small factors, including an asymptotic for almost all moduli of exponent `2/3`, and applies the technology to a nonhomogeneous binary cubic polynomial.

Classification:

```text
GRIMMELT_MERIKOSKI_2025=NEAR_HIGH_PRIORITY
```

Why it is near:

- the Stage14 reciprocal selector contains divisor choices plus fixed congruence conditions;
- the modulus structure in 4gd is factorized through fixed `(U,V)` data and candidate divisor/factor-pair choices, so factorable-modulus divisor-AP technology is structurally relevant;
- the paper supplies genuine power-saving equidistribution technology rather than only a soft divisor-density statement.

Unverified / blocking points:

1. Stage14 needs an existential support lower bound on every charged principal pair cell, not merely a mean divisor-count asymptotic;
2. the selector has two divisor choices `p,q` coupled through the factor-pair equation for `F_-F_+` and two CRT congruences;
3. the paper's almost-all-moduli and binary-cubic applications do not directly match the frozen fixed-E pair family;
4. no moment-to-support transfer preserving all Stage14 masks is currently proved.

Therefore this is not DIRECT.

## 3. Candidate B — Irving, divisor function to smooth moduli

Primary source:

```text
A. J. Irving,
"The divisor function in arithmetic progressions to smooth moduli",
arXiv:1403.8031 (2014).
```

The paper obtains divisor-function asymptotics in arithmetic progressions for larger moduli when the modulus has suitable factorisation, using a q-analogue of van der Corput.

Classification:

```text
IRVING_2014_SMOOTH_MODULI=NEAR_SECONDARY
```

Potential use: if Stage14-4gf rewrites the reciprocal selector as a nonnegative divisor sum in one progression whose modulus inherits the required factorisation, Irving-type distribution could become a first-moment input.

Blocking points:

- the current selector is not yet reduced to one divisor sum in one progression;
- the relevant Stage14 modulus/factorisation range has not been matched to Irving's hypotheses;
- a first-moment asymptotic still does not by itself give the required support lower bound.

## 4. Candidate C — Nguyen, generalized divisor functions in arithmetic progressions

Primary sources:

```text
David T. Nguyen,
"Generalized divisor functions in arithmetic progressions: I",
arXiv:2308.06839 (2023).

D. T. Nguyen,
"Generalized divisor functions in arithmetic progressions: II",
arXiv:2302.12815 (2023).
```

Part I gives distribution results for `k`-fold divisor functions in arithmetic progressions, including moduli beyond square-root scale under averaging and conditional GRH variants. Part II controls a second moment of modified shifted convolutions of the three-fold divisor function.

Classification:

```text
NGUYEN_DIVISOR_AP_I_II=NEAR_MOMENT_ARCHITECTURE
```

Why it matters: q17's smallest plausible analytic adapter is a first/second-moment support argument for the nonnegative witness count `N_rec(u,v)=#Omega_rec(u,v)`. Nguyen's work is relevant to the moment side of that architecture.

Blocking points:

- the Stage14 witness count is not yet encoded as the generalized divisor function family used there;
- averaging over moduli / shifted-convolution structure does not match a uniform every-principal-cell statement automatically;
- the physical primitive-pair and fixed `(U,V)` CRT restrictions must remain inside the estimate.

## 5. Candidate D — Ford, integers with a divisor in a prescribed interval

Primary source:

```text
Kevin Ford,
"The distribution of integers with a divisor in a given interval",
arXiv:math/0401223 (2004).
```

Ford determines the order of magnitude of the support of integers possessing a divisor in a prescribed interval over very broad ranges.

Classification:

```text
FORD_2004_DIVISOR_SUPPORT=BACKGROUND_SUPPORT_TEMPLATE
```

This is important conceptually because it is a genuine support theorem, unlike a divisor-function mean. However q17's obstruction is not merely "has a divisor in an interval": it requires two coupled divisor choices and the fixed factor-pair CRT conditions. No direct transfer is available.

## 6. Candidate E — Frei--Sofos, generalized divisor sums over binary forms

Primary source:

```text
Christopher Frei, Efthymios Sofos,
"Generalised divisor sums of binary forms over number fields",
arXiv:1609.04002 (2016).
```

The paper proves asymptotic estimates and lower bounds for generalized divisor sums over values of binary forms, allowing Jacobi-symbol-type weights with varying arguments.

Classification:

```text
FREI_SOFOS_2016_BINARY_FORM_DIVISOR_SUMS=NEAR_STRUCTURE
```

Potential relevance: the Stage14 frozen pair variables `(u,v)` are already a two-variable primitive rectangle, so an exact rewrite of `N_rec(u,v)` into a nonnegative divisor sum over explicit binary-form values would put this family much closer to an existing theorem architecture.

Blocking points:

- no such exact binary-form encoding is currently merged;
- q17's coupled `p,q,F_-,F_+` CRT witness is not a standard `1*chi` weight as stated;
- the residual physical post-mask must not be smuggled into the reciprocal selector.

## 7. Candidate F — Bettin, linear correlations of the divisor function

Primary source:

```text
Sandro Bettin,
"Linear correlations of the divisor function",
arXiv:1701.06608 (2017).
```

The paper studies products of divisor functions constrained by a nontrivial linear relation and obtains analytic continuation and a power-saving point-counting application.

Classification:

```text
BETTIN_2017_LINEAR_DIVISOR_CORRELATIONS=BACKGROUND_NEAR_STRUCTURE
```

This is relevant only if 4gf/4gg converts the reciprocal/factor-pair constraints to a finite combination of linear divisor correlations. The present relation is still multiplicative through `F_-F_+=C*p*q`, so no direct import is justified.

## 8. q17 verdict

No searched primary source proves the frozen Stage14 obstruction unchanged.

```text
STAGE14_Q17=COMPLETE_RECIPROCAL_CRT_SUPPORT_LITERATURE_RADAR
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
RECIPROCAL_CRT_SUPPORT_DIRECT_THEOREM_FOUND=false
DIVISOR_AP_MOMENT_TO_EXISTENTIAL_SUPPORT_ADAPTER_PROVED=false
BINARY_FORM_ENCODING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_FROM_LITERATURE_PROVED=false
```

The strongest current interpretation is:

```text
Grimmelt--Merikoski / Irving / Nguyen
  = plausible analytic moment inputs after an exact Stage14 encoding;

Ford
  = support-theorem template but missing the CRT coupling;

Frei--Sofos / Bettin
  = structural encodings to test if the internal algebra opens in the right form.
```

## 9. Falsifiable receiving-stage handoffs

### Handoff 1 — direct construction first

```text
Q17_EXPLICIT_RECIPROCAL_SELECTOR_CONSTRUCTION_TEST
RECEIVER=Stage14-4gf
```

On one principal fixed-E cell, attempt an explicit deterministic choice of `p,q,F_-,F_+` satisfying all frozen divisibility/CRT/parity conditions on `B^(kappa-o(1))` primitive pairs. If successful, the reciprocal support deficit is exhausted without an external theorem.

### Handoff 2 — moment-to-support adapter

```text
Q17_DIVISOR_AP_FIRST_SECOND_MOMENT_SUPPORT_TRANSFER_TEST
RECEIVER=Stage14-4gf_or_successor
```

Define

```text
N_rec(u,v)=#Omega_rec(u,v)>=0.
```

A sufficient exponent-scale support route would be to prove on every principal cell

```text
sum N_rec >= B^(kappa-o(1)),
sum N_rec^2 <= B^(kappa+o(1)),
```

with the same charged measure and all frozen reciprocal filters. Cauchy--Schwarz would then give

```text
#T_rec >= B^(kappa-o(1)).
```

The first falsification test is whether `N_rec` can be exactly rewritten into divisor-AP pieces compatible with Grimmelt--Merikoski, Irving or Nguyen without dropping the coupled factor-pair CRT condition.

### Handoff 3 — binary-form encoding

```text
Q17_BINARY_FORM_DIVISOR_SUM_ENCODING_TEST
RECEIVER=Stage14-4gf_or_successor
```

Try to express the reciprocal witness count as a finite nonnegative divisor-sum weight on explicit binary-form values in `(u,v)`. Only after an exact identity is proved should Frei--Sofos-type lower bounds be tested.

## 10. Scope locks

q17 does not search the residual root-origin/canonical/post-column mask, because 4ge keeps it as a separate conditional support. It also does not cross-promote fixed-U Gaussian-prime results.

```text
Q17_POST_MASK_SEARCHED=false
Q17_FIXED_U_SEARCHED=false
Q17_GLOBAL_TO_FIXED_U_CROSS_PROMOTION=false
Q17_NEW_HEAVY_H_NEEDED=false
Q17_NEXT_SEARCH_TRIGGER=4gf_or_successor_proves_exact_divisor_AP_or_binary_form_encoding_or_exposes_a_different_stable_obstruction
```
