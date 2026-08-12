# Stage14-s7-128 — fixed-power equivalence of filtered tau3 support and first moment

## Status

`COMPLETE_FILTERED_TAU3_SUPPORT_FIRST_MOMENT_EQUIVALENCE_AND_RECEIVER_CHANGE`

Consumes batch-local `Stage14-s7-126/127`, merged `Stage14-s7-125`, and merged `Stage14-q18`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Abstract bounded-multiplicity lemma

Let `T` be either a charged scalar baseline or the charged polynomial outer-pair baseline. Let `N(t)` be the corresponding exact nonnegative filtered ternary-divisor weight from s7-126 or s7-127, and assume uniformly

```text
N(t) <= B^o(1).
```

Define

```text
Supp(N) := {t in T : N(t)>=1},
M1(N)   := sum_{t in T} N(t).
```

Pointwise on `T`,

```text
1_{N(t)>=1} <= N(t) <= B^o(1)*1_{N(t)>=1}.
```

Summing gives the exact fixed-power sandwich

```text
#Supp(N) <= M1(N) <= B^o(1)*#Supp(N).
```

Therefore support cardinality and first moment have the same fixed-power exponent.

```text
FILTERED_TAU3_SUPPORT_FIRST_MOMENT_EQUIVALENCE_PROVED=true
```

This uses only nonnegativity and the already proved subpolynomial per-candidate factorization multiplicity. It does not assert a first-moment asymptotic.

## 2. Scalar application

For the endpoint and polynomial-E fixed-product scalar branches, let

```text
M1_scalar := sum_{z in S_pre} N_mult(z).
```

Then

```text
#S_mult <= M1_scalar <= B^o(1)*#S_mult.
```

If

```text
M1_scalar = B^(rho_mult+o(1)),
```

then `rho_mult=sigma_mult` at fixed-power scale and

```text
delta_mult = sigma_pre-rho_mult.
```

Thus the first-layer support theorem species may be replaced, without exponent loss, by the exact filtered first-moment species

```text
UniformOneDimensionalFixedSquarefreeAllocationFilteredTau3FirstMoment.
```

The second reverse layer and post-mask remain separate receivers.

## 3. Polynomial outer-pair application

For the charged pair branch, keep

```text
M1_pair
 := sum_{(E,m) in S_pre_pair} N_mult_pair(E,m).
```

Then, on the pair measure itself,

```text
#S_mult_pair <= M1_pair <= B^o(1)*#S_mult_pair.
```

Hence the pair first-layer support exponent is exactly the exponent of the pair-indexed first moment. The correct theorem species becomes

```text
UniformPolynomialOuterPairFiberedFixedSquarefreeAllocationFilteredTau3FirstMoment.
```

No scalarization through `n=Em` is used or needed.

```text
POLYNOMIAL_PAIR_FILTERED_TAU3_SUPPORT_FIRST_MOMENT_EQUIVALENCE_PROVED=true
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
```

## 4. q18 handoff status

q18 reported

```text
FILTERED_TAU3_TO_SUPPORT_ADAPTER_PROVED=false
```

because its literature pass did not contain this Stage14-specific bounded-multiplicity conversion. The exact internal adapter is now proved for both charged theorem species:

```text
Q18_FILTERED_TAU3_TO_SUPPORT_ADAPTER_PROVED=true
Q18_SCALAR_FILTERED_TAU3_ENCODING_TEST=PASS
Q18_POLYNOMIAL_PAIR_FIBERED_SUPPORT_MOMENT_TEST=PASS
```

This does **not** promote any q18 literature result to a theorem. Rather, it sharpens the next external target from support to an exact restricted first moment.

The q18 next-search trigger `exact_filtered_tau3_or_binary_form_encoding_or_new_pair_level_moment_object` has therefore been reached.

```text
Q18_NEXT_SEARCH_TRIGGER_REACHED=true
```

## 5. Material receiver change

The aligned fixed-E two-sided packet remains parked at

```text
UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment.
```

The active nonaligned s receiver changes to

```text
scalar branches:
  exact filtered tau3 first moment
  -> second reverse reciprocal reconstruction deficit
  -> residual post-mask;

polynomial pair branch:
  exact pair-indexed filtered tau3 first moment
  -> second reverse reciprocal reconstruction deficit
  -> residual post-mask.
```

Equivalently,

```text
CURRENT_S_RECEIVER=FixedETwoSidedParkedUniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment_OR_OneDimensionalFixedSquarefreeAllocationFilteredTau3FirstMomentThenSecondReverseThenConditionalPostMask_OR_PolynomialOuterPairFiberedFixedSquarefreeAllocationFilteredTau3FirstMomentThenSecondReverseThenConditionalPostMask
```

```text
RECEIVER_MATERIALLY_CHANGED=true
S_ROUTE_H_NEEDED=false
WORK_CCX41_REVISIT_TRIGGER_S7_128_REACHED=true
NEXT=Stage14-s7-129
```

No new sH is opened: q18 has already performed the primary literature radar, and the newly sharpened first-moment objects should return to integrated XQ/q for any follow-up literature decision rather than duplicate that search locally.

## Boundary

```text
STAGE14_S7_128=COMPLETE_FILTERED_TAU3_SUPPORT_FIRST_MOMENT_EQUIVALENCE_AND_RECEIVER_CHANGE
FILTERED_TAU3_SUPPORT_FIRST_MOMENT_EQUIVALENCE_PROVED=true
Q18_FILTERED_TAU3_TO_SUPPORT_ADAPTER_PROVED=true
Q18_NEXT_SEARCH_TRIGGER_REACHED=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-129
```
