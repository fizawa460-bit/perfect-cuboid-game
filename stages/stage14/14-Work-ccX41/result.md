# Stage14-Work-ccX41 — square-class reverse theorem-species partition with integrated q18

## Status

`COMPLETE_SQUARECLASS_THEOREM_SPECIES_PARTITION_WITH_TRIGGERED_Q18`

Starts from latest merged main

```text
95ab6d5fc152357bbadf64d0067b2eb8a89162ba
```

and consumes only merged sources:

- `Stage14-Work-cbX40` plus merged CI repair #788;
- mainline external boundary `Stage14-4ghH`;
- s-route through `Stage14-s7-125`;
- fixed-U route through `Stage14-t157` with frozen `Stage14-tH33` target;
- latest merged q baseline `Stage14-q17`.

```text
STAGE14_WORK_TOOLBOX_X=RUN
STAGE14_WORK_TOOLBOX_XQ=RUN
RUN_TRIGGER=s7_122_q18_stability_plus_s7_125_refinement_plus_t157_new_tH33_target
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. X41 lemma — common host algebra does not identify charged support measure

Suppose two charged families admit the same internal witness equation

```text
g*x*y = c*z
```

and the same finite continuation architecture after fixing packet data and a squarefree allocation.  This identifies an algebraic witness kernel.  It does **not** identify the support theorem unless the charged outer measures and quantifier order are also identified.

In particular, a scalar support theorem for

```text
z -> exists (g,x,y,...)
```

cannot be substituted for a pair support theorem

```text
(E,m) -> exists (g,x,y,...),   z=E*m
```

merely because a fixed `z` has only `B^o(1)` factorizations `z=E*m`.  That fiber has already been charged and cannot be reused as evidence that pair-dependent prefilters or post-masks are constant on the fiber.

```text
COMMON_HOST_ALGEBRA_DOES_NOT_IDENTIFY_CHARGED_SUPPORT_MEASURE=true
SUBPOLYNOMIAL_HOST_FIBER_CANNOT_SCALARIZE_PAIR_SUPPORT=true
THEOREM_SPECIES_MUST_PRESERVE_OUTER_MEASURE_AND_QUANTIFIER_ORDER=true
```

This is the new X41 charged-once separation rule.

## 2. Main aligned packet remains parked at its existing external gate

Completed `Stage14-4ghH` leaves exactly

```text
UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
```

unresolved.  `Stage14-Work-cbX40` already localized that gate to the aligned main/s fixed-E two-sided realization.  Nothing in s7-123..125 or t156..157 supplies the missing every-principal-cell first-moment theorem.

Therefore

```text
MAIN_ALIGNED_EXTERNAL_GATE_UNCHANGED=true
MAIN_EXTERNAL_GATE_CROSS_PROMOTED_TO_NONALIGNED_S=false
MAIN_EXTERNAL_GATE_CROSS_PROMOTED_TO_FIXED_U=false
```

## 3. Nonaligned s branches reduce to exactly two theorem species

Merged s7-123 gives the exact first reverse normalization, after one ordered squarefree allocation `A*B=K` is fixed,

```text
F2^- = g*A*x^2,
F2^+ = g*B*y^2,
g*x*y = c_C*z.
```

Merged s7-124 transports all already-exposed first-layer parity/order/endpoint conditions to a deterministic predicate `R_mult` on this host.  Merged s7-125 then defines

```text
S_pre -> S_mult -> S_rev2 -> S_phys
```

with exact deficits

```text
delta_mult,
delta_rev2,
delta_post.
```

The two scalar realizations

```text
fixed-E endpoint: z=t,
polynomial-E fixed-product: z=E
```

share the same theorem species

```text
UniformOneDimensionalFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport.
```

The polynomial outer-pair realization instead requires

```text
UniformPolynomialOuterPairFiberedFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport,
```

because its charged baseline is `(E,m)` while `z=E*m` is internal to the reverse witness.

Hence the three active nonaligned branches produce **two**, not one and not three, bare-reverse theorem species.

```text
S_NONALIGNED_COMMON_TRIPLE_PRODUCT_REVERSE_KERNEL_PROVED=true
S_NONALIGNED_THEOREM_SPECIES_COUNT=2
S_SCALAR_BRANCHES_SHARE_THEOREM_SPECIES=true
S_POLYNOMIAL_PAIR_REQUIRES_DISTINCT_THEOREM_SPECIES=true
S_POLYNOMIAL_PAIR_SCALAR_HOST_REPLACEMENT_PROVED=false
```

The residual post-mask remains outside both q18 bare-support targets.

## 4. fixed-U has a fresh H target, not a q18 cross-promotion target

Merged t156 localizes every actual-scale Kai-inadmissible long survivor to a pseudopolynomial modulus window, with principal compatibility caps

```text
sparse: d^3 <= B^(1/2+o(1)),
area:   d^5 <= B^(1/2+o(1)).
```

Merged t157 proves that sparse and area long survivors require the same pointwise prime-side statement once one actual upper endpoint is frozen, and freezes

```text
SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
```

as immutable `Stage14-tH33` target.

This is a materially new fixed-U theorem target, but its clean-room theorem audit belongs to tH33.  The integrated q18 search therefore does not duplicate that H investigation and does not mix Gaussian-prime occupancy with the integer square-class reverse support problem.

```text
FIXED_U_H_TARGET_MATERIALLY_CHANGED=true
FIXED_U_Q18_DUPLICATE_SEARCH_FORBIDDEN=true
TH33_NEEDED=true
TH33_EXECUTED=false
```

## 5. Post-X q gate — TRIGGERED

Latest merged q baseline is q17.  q17 searched the aligned fixed-E reciprocal divisor/CRT support

```text
FixedAgreementPairRadialLinearTwoLevelDivisorCRTReciprocalSolvabilitySupport.
```

The s7-125 targets are materially different.  Their first layer is now an exact fixed-squarefree-allocation filtered triple-product host

```text
g*x*y=c_C*z
```

followed by a second reverse factor-pair reconstruction, and one branch is charged on polynomial outer pairs rather than the scalar host.

Therefore the q gate triggers `Stage14-q18` on the same branch.

```text
Q_COMPONENT=COMPLETE
Q_TRIGGER_STAGE=Stage14-s7-122+Stage14-s7-125
EXACT_Q_OBSTRUCTION=ScalarAndFiberedFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport
Q_LEDGER_BASELINE=Stage14-q17
Q_RESULT_IMPORTED_BACK_TO_X=true
```

### q18 imported verdict

The primary-literature pass finds no unconditional theorem directly proving the required uniform support statement for either frozen theorem species while preserving the second reverse layer, branch-specific filters and charged measure.

The nearest current architectures are:

```text
Nguyen 2023 generalized k-fold divisor functions in arithmetic progressions = NEAR_MOMENT_ARCHITECTURE
Wei-Xue-Zhang 2015 general divisor functions to large smooth moduli = NEAR_AP_ARCHITECTURE
Frei-Sofos 2016 generalized divisor sums of binary forms = NEAR_STRUCTURE
Ford 2004/2006 divisor-interval and multiplication-table support = BACKGROUND_SUPPORT
Grimmelt-Merikoski 2025 divisor AP / binary cubic = BACKGROUND_NEAR_STRUCTURE
DeLaBreteche-Browning 2006 arithmetic functions over binary forms = BACKGROUND_UPPER_TEMPLATE
```

None of these statements, as published, simultaneously supplies:

1. support rather than only an average weighted divisor count;
2. every-principal-cell uniformity;
3. the filtered triple-product host;
4. the second reverse reciprocal factor-pair existence;
5. pair-measure preservation on the `(E,m)` branch.

Thus

```text
Q18_DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
Q18_SCALAR_TRIPLE_PRODUCT_REVERSE_DIRECT_THEOREM_FOUND=false
Q18_POLYNOMIAL_PAIR_FIBERED_REVERSE_DIRECT_THEOREM_FOUND=false
Q18_FILTERED_TAU3_TO_SUPPORT_ADAPTER_PROVED=false
Q18_PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
```

The exact radar and falsification tests are recorded in the q18 files.

## 6. q18 handoffs

First receiving test for the scalar branches:

```text
Q18_SCALAR_FILTERED_TAU3_ENCODING_TEST -> Stage14-s7-126
```

Freeze one principal scalar cell and test whether the first-layer count can be written as a finite linear combination of restricted `tau_3(c_C*z)`-type weights with all `R_mult` conditions explicit.  Even a successful encoding is only the first layer; a support transfer through the second reverse factor pair must still be proved.

For the polynomial pair branch:

```text
Q18_POLYNOMIAL_PAIR_FIBERED_SUPPORT_MOMENT_TEST -> Stage14-s7-126+
```

Do not replace `(E,m)` by `n=Em` unless every pair-dependent prefilter and second-layer condition is proved constant or summably controllable on the `B^o(1)` factorization fiber.

## 7. Receiver / supersession ledger

Superseded or exhausted at fixed-power scale:

```text
- treating the three nonaligned s branches as one undifferentiated square-class support theorem;
- treating the endpoint and fixed-product scalar branches as separate theorem species solely because z has a different name;
- using the B^o(1) E*m=n fiber to scalarize the polynomial-pair support;
- reopening q17 for the unchanged aligned main first-moment gate;
- duplicating tH33 inside q18.
```

Retained:

```text
MAIN/S ALIGNED:
  UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment external gate;

S NONALIGNED SCALAR:
  UniformOneDimensionalFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport;

S NONALIGNED PAIR:
  UniformPolynomialOuterPairFiberedFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport;

FIXED-U:
  endpoint residue occupancy plus SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio on Kai-inadmissible long packets.
```

## 8. H decisions

```text
MAINLINE_H_NEEDED=true
MAINLINE_H_TARGET=UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
MAINLINE_H_COMPLETED=true
MAINLINE_BLOCKED_BY_H=true
NEW_HEAVY_MAIN_H_NEEDED=false

S_ROUTE_H_NEEDED=false
S_ROUTE_H_TARGET=NONE
S_ROUTE_H_REASON=q18_is_the_current_external_radar_and_s7_126_internal_encoding_test_precedes_any_sH

FIXED_U_H_NEEDED=true
FIXED_U_H_TARGET=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
FIXED_U_H_REASON=t157_froze_new_immutable_clean_room_target
TH33_NEEDED=true
TH33_EXECUTED=false
WHOLE_STAGE14_BLOCKED_BY_MAIN_EXTERNAL_GATE=false
```

The main external gate blocks only its aligned packet.  tH33 is nonblocking for the rest of Stage14.

## 9. Required locks

```text
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
Q_COMPONENT=COMPLETE
Q_TRIGGER_STAGE=Stage14-s7-122+Stage14-s7-125
EXACT_Q_OBSTRUCTION=ScalarAndFiberedFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport
Q_LEDGER_BASELINE=Stage14-q17
Q_RESULT_IMPORTED_BACK_TO_X=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_GLOBAL_RECEIVER=AlignedFixedETwoSidedParkedNestedKFreeQuadraticDivisorRootFirstMoment_OR_NonalignedScalarOrFiberedSquarefreeAllocationTripleProductTwoLevelReverseSupportThenPostMask
CURRENT_FIXED_U_RECEIVER=EndpointDoubleResidueOccupancy_OR_SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
MAINLINE_H_NEEDED=true
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=true
TH33_NEEDED=true
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT_REVISIT_CONDITION=main_external_gate_resolution_OR_merged_tH33_plus_s7_128_OR_earlier_q18_handoff_adapter_receiver_or_exponent_change
```

## 10. Next integrated target

```text
FilteredTripleProductReverseSupportVersusSuperKaiGaussianPrimeOccupancyOrNoGo
```

No strict sub-square-root power saving is claimed.
