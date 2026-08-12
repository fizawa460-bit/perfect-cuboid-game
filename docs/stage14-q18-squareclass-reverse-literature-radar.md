# Stage14-q18 — filtered triple-product / two-level reverse support literature radar

## Trigger header

```text
TRIGGER_STAGE=Stage14-s7-122+Stage14-s7-125
EXACT_OBSTRUCTION=ScalarAndFiberedFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport
CURRENT_BEST_BOUND=exact_gxy_eq_cz_normal_form_plus_Bo1_allocation_and_witness_multiplicity_but_no_uniform_nonempty_support_bound_through_second_reverse_layer
WHY_EXISTING_Q_LEDGER_DOES_NOT_ALREADY_ANSWER_IT=q17_covers_the_aligned_Kfree_two_divisor_quadratic_CRT_first_moment_not_the_nonaligned_fixed_squarefree_allocation_triple_product_host_or_pair_measure
SEARCH_FAMILIES=generalized_tau3_AP;general_divisor_functions_smooth_moduli;binary_form_divisor_sums;divisor_interval_and_multiplication_table_support;binary_cubic_divisor_sums
LAST_RADAR_BASELINE=Stage14-q17
PROMOTION_STANDARD=uniform_every_principal_cell_support_estimate_preserving_fixed_squarefree_allocation_Rmult_second_reverse_layer_and_charged_scalar_or_pair_measure
```

## Frozen Stage14 targets

After one ordered squarefree allocation `A*B=K` is frozen, the first reverse layer is exactly

```text
F2^- = g*A*x^2,
F2^+ = g*B*y^2,
g*x*y=c_C*z,
R_mult(z;g,x,y)=1.
```

A surviving first-layer triple must then extend through the reconstructed `cp,dq`, their ordered factorizations, and the second reverse factor-pair system before the residual root/canonical/post-column mask is charged.

There are two charged theorem species.

### Scalar species

```text
UniformOneDimensionalFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport
```

for the scalar outer variables `z=t` and `z=E`.

### Pair species

```text
UniformPolynomialOuterPairFiberedFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport
```

for the charged outer pair `(E,m)` with internal host `z=E*m`.

The `B^o(1)` factorization fiber of a fixed host does not permit replacement of pair support by scalar support.

## Verdict

```text
STAGE14_Q18=COMPLETE_FILTERED_TRIPLE_PRODUCT_REVERSE_SUPPORT_LITERATURE_RADAR
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
SCALAR_TRIPLE_PRODUCT_REVERSE_DIRECT_THEOREM_FOUND=false
POLYNOMIAL_PAIR_FIBERED_REVERSE_DIRECT_THEOREM_FOUND=false
FILTERED_TAU3_TO_SUPPORT_ADAPTER_PROVED=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_FROM_LITERATURE_PROVED=false
```

No source below is promoted merely because it contains a `tau_3`, divisor-sum, binary-form or multiplication-table vocabulary.  The Stage14 target is support of a nested filtered witness, not the average order of an unrestricted divisor function.

## 1. Nguyen — generalized divisor functions in arithmetic progressions

Primary sources:

- David T. Nguyen, *Generalized divisor functions in arithmetic progressions: I*, arXiv:2308.06839.
- David T. Nguyen, *Generalized divisor functions in arithmetic progressions: II*, arXiv:2302.12815.

Classification:

```text
NGUYEN_TAU3_AP=NEAR_MOMENT_ARCHITECTURE
```

Why it is relevant:

- the first reverse equation has an exact triple-product structure;
- `tau_3` technology is the natural comparison family once `R_mult` is encoded as arithmetic weights;
- Nguyen supplies distribution/moment machinery for generalized divisor functions in progressions.

Why it is not DIRECT:

- the published distribution statements use modulus averaging or hypotheses that do not match every Stage14 principal scalar cell;
- the Stage14 count is not unrestricted `tau_3(c_C z)` but a fixed-allocation filtered triple factorization;
- the second reverse factor-pair existence is another coupled arithmetic layer;
- the polynomial `(E,m)` branch is charged on pairs and cannot be replaced by the scalar host without a new adapter.

Minimal transfer test:

```text
Q18_SCALAR_FILTERED_TAU3_ENCODING_TEST
```

Derive an exact finite expansion of the first-layer Stage14 witness count into restricted `tau_3`-type weights and list every modulus/local filter before invoking any AP theorem.

## 2. Wei--Xue--Zhang — general divisor functions to large smooth moduli

Primary source:

- Fei Wei, Boqing Xue, Yitang Zhang, *General divisor functions in arithmetic progressions to large moduli*, arXiv:1512.01470.

Classification:

```text
WEI_XUE_ZHANG_GENERAL_DIVISOR_AP=NEAR_AP_ARCHITECTURE
```

This is potentially useful only after an exact AP encoding of the filtered triple-product layer.  Its smooth/factorable-modulus framework does not itself manufacture the Stage14 support theorem, and it does not preserve the second reverse reciprocal existence or the polynomial pair baseline as stated.

## 3. Frei--Sofos — generalized divisor sums over binary forms

Primary source:

- Christopher Frei, Efthymios Sofos, *Generalised divisor sums of binary forms over number fields*, arXiv:1609.04002.

Classification:

```text
FREI_SOFOS_BINARY_FORM_DIVISOR_SUM=NEAR_STRUCTURE
```

The paper gives asymptotic estimates and lower bounds for generalized divisor sums over binary-form values.  This becomes actionable only if one Stage14 scalar/pair support count can be encoded as a covered nonnegative divisor sum over a binary form with uniform coefficient control.  No such encoding is currently merged, and the nested second reverse layer is not a published special case of that theorem.

Minimal transfer test:

```text
Q18_BINARY_FORM_ENCODING_TEST
```

Attempt to eliminate one host factor so that the remaining first/second reverse conditions become a divisor convolution over one explicit binary form; reject the route if pair-dependent masks or moving coefficients violate the theorem hypotheses.

## 4. Ford — divisor support and multiplication-table architecture

Primary sources:

- Kevin Ford, *The distribution of integers with a divisor in a given interval*, arXiv:math/0401223.
- Kevin Ford, *Integers with a divisor in (y,2y]*, arXiv:math/0607473.

Classification:

```text
FORD_DIVISOR_SUPPORT_MULTIPLICATION_TABLE=BACKGROUND_SUPPORT
```

These are genuine support theorems and are valuable as a reminder that average divisor multiplicity and nonempty support are different questions.  They do not impose the fixed squarefree allocation, filtered triple-product relation, second reciprocal reconstruction, or charged pair measure required here.

## 5. Grimmelt--Merikoski — divisor AP and binary cubic polynomial

Primary source:

- Lasse Grimmelt, Jori Merikoski, *The divisor function along arithmetic progressions and binary cubic polynomials*, arXiv:2508.17979.

Classification:

```text
GRIMMELT_MERIKOSKI_2025=BACKGROUND_NEAR_STRUCTURE
```

Their divisor-AP estimate and binary-cubic application show modern factorable-modulus/binary-polynomial technology, but the counted function is still an ordinary divisor function and the application is an average asymptotic.  The Stage14 nested support and every-principal-cell quantifier remain unverified.

## 6. de la Breteche--Browning — arithmetic functions over binary-form values

Primary source:

- R. de la Breteche, T. D. Browning, *Sums of arithmetic functions over values of binary forms*, arXiv:math/0604119.

Classification:

```text
DE_LA_BRETECHE_BROWNING_BINARY_FORM_UPPER=BACKGROUND_UPPER_TEMPLATE
```

The explicit-coefficient upper-bound framework may be useful if the Stage14 witness is first encoded as an arithmetic function of a binary form.  It does not give the required nonempty support lower bound or the second reverse extension.

## 7. Tempting shortcuts that remain blocked

```text
UNRESTRICTED_TAU3_POSITIVITY_IMPLIES_STAGE14_SUPPORT=false
AVERAGE_DIVISOR_COUNT_IMPLIES_EVERY_CELL_NONEMPTY_SUPPORT=false
BO1_HOST_FACTORIZATION_FIBER_IMPLIES_PAIR_SUPPORT_SCALARIZATION=false
FIRST_LAYER_ASYMPTOTIC_IMPLIES_SECOND_REVERSE_SUPPORT=false
Q18_POST_MASK_SEARCHED=false
Q18_FIXED_U_SEARCHED=false
```

The first statement is especially important: the equation `g*x*y=c_C*z` alone has trivial factorizations, but the Stage14 obstruction is the support after `R_mult` and the second reverse reconstruction are retained.

## Handoff

### Primary scalar receiving test

```text
Q18_SCALAR_FILTERED_TAU3_ENCODING_TEST
RECEIVER=Stage14-s7-126
```

For one principal scalar cell, define the nonnegative first-layer multiplicity

```text
N_mult(z)=#{(g,x,y): g*x*y=c_C*z, R_mult(z;g,x,y)=1}.
```

Determine whether `N_mult` is an exact finite combination of generalized divisor weights with fixed/factorable congruence data.  If yes, test whether the cited AP/moment machinery gives either a full-exponent first-layer support lower bound or a fixed-power deficit.  Do not infer the second reverse layer from this step.

### Pair receiving test

```text
Q18_POLYNOMIAL_PAIR_FIBERED_SUPPORT_MOMENT_TEST
RECEIVER=Stage14-s7-126+
```

Define the witness multiplicity on charged pairs `(E,m)` directly.  Any reduction through `n=Em` must prove that pair-dependent prefilters and second-layer weights can be controlled uniformly on the factorization fiber.  A `B^o(1)` fiber cardinality alone is insufficient.

### Reopen rule

Open another q search only if s derives one of:

- an exact restricted `tau_3`/generalized-divisor AP encoding with verified modulus family;
- an explicit binary-form divisor-sum encoding;
- a pair-level moment/correlation object not covered by this radar;
- a materially new post-mask theorem species.

The fixed-U `SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio` is deliberately excluded from q18 because it already has the frozen clean-room `Stage14-tH33` audit target.
