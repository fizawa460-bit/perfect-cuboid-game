# Stage14-q20 — conditioned divisor-correlation literature radar

## Trigger

Merged `Stage14-s7-131` passes q19's two internal handoffs and freezes the exact stable object

```text
J_rev2
 = sum_{lambda in Lambda_mult}
     sum_{f|W1(lambda)} R_rev2(lambda;f),
```

with two charged measure variants (scalar and polynomial `(E,m)` pair). The residual post-mask is excluded.

```text
STAGE14_Q20=COMPLETE_CONDITIONED_DIVISOR_CORRELATION_LITERATURE_RADAR
Q_TRIGGER_STAGE=Stage14-s7-131
Q_LEDGER_BASELINE=Stage14-q19
```

## Exact target contract

A DIRECT theorem must preserve all of the following simultaneously:

1. `lambda` is a retained first-layer filtered ternary-product witness, not an unrestricted integer;
2. `W1(lambda)` depends on those witness labels;
3. `R_rev2(lambda;f)` contains the exact second-layer positivity/parity/order/divisibility/reciprocal reconstruction conditions;
4. scalar and polynomial `(E,m)` charged measures remain distinct;
5. the estimate is uniform on every principal cell at fixed-power precision;
6. no residual root/canonical/post-column post-mask is silently inserted or removed.

## Primary-source audit

### 1. Topacogullari — shifted convolution of `d_3` and `d`

Primary source: https://arxiv.org/abs/1506.02608

The paper proves an asymptotic formula with power-saving error for shifted convolutions of `d_3(n)` and `d(n+h)`, uniform in the shift in its theorem range.

Verdict:

```text
TOPACOGULLARI_SHIFTED_D3_D=NEAR_HIGH_PRIORITY_IF_FIXED_SHIFT_NORMAL_FORM_EXISTS
DIRECT=false
```

Reason: Stage14 has no proved reduction of `W1(lambda)` and `R_rev2(lambda;f)` to a single fixed additive shift `n+h` with an admissible smooth/arithmetic weight while retaining the charged witness conditioning.

### 2. Nguyen — generalized divisor functions in arithmetic progressions II

Primary source: https://arxiv.org/abs/2302.12815

This work obtains a second-moment bound for modified shifted convolutions of the generalized 3-fold divisor function.

Verdict:

```text
NGUYEN_AP_II_MODIFIED_SHIFTED_D3=NEAR_CONDITIONAL
DIRECT=false
```

Reason: the Stage14 inner divisor extension is witness-dependent and not yet encoded as Nguyen's modified shifted convolution object. In addition, the charged support measure and exact filters must survive the transformation.

### 3. Nguyen — generalized divisor functions in arithmetic progressions I

Primary source: https://arxiv.org/abs/2308.06839

This paper proves distribution estimates for generalized divisor functions in arithmetic progressions, including ranges beyond the square-root barrier under averaging hypotheses.

Verdict:

```text
NGUYEN_AP_I_GENERALIZED_DIVISOR_AP=NEAR_CONDITIONAL
DIRECT=false
```

Reason: no exact arithmetic-progression modulus/residue representation of the witness-conditioned `J_rev2` has been proved. An AP mean-value theorem cannot be substituted for support on every charged principal cell.

### 4. Frei–Sofos — generalized divisor sums of binary forms

Primary source: https://arxiv.org/abs/1609.04002

This work gives asymptotic estimates and lower bounds for generalized divisor sums over values of binary forms over number fields.

Verdict:

```text
FREI_SOFOS_BINARY_FORM_DIVISOR_SUMS=NEAR_STRUCTURE
DIRECT=false
```

Reason: Stage14 has not proved that `W1(lambda)` is a fixed finite-complexity binary form in the charged outer variables after retaining the first-layer witness labels and exact reverse filters.

### 5. Bettin / Matthiesen — linear divisor correlations

Primary sources:
- https://arxiv.org/abs/1701.06608
- https://arxiv.org/abs/1011.0019

These works treat divisor correlations constrained by fixed linear relations / systems of linear forms.

Verdict:

```text
BETTIN_LINEAR_DIVISOR_CORRELATION=NEAR_STRUCTURE
MATTHIESEN_LINEAR_DIVISOR_CORRELATION=NEAR_STRUCTURE
DIRECT=false
```

Reason: the current `lambda -> W1(lambda)` dependence is not proved to become one fixed finite-complexity linear system without losing conditioning or changing the charged measure.

## Literature verdict

```text
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
CONDITIONED_SECOND_REVERSE_CORRELATION_DIRECT_THEOREM_FOUND=false
SHIFTED_D3_D_DIRECT_TRANSFER_PROVED=false
MODIFIED_SHIFTED_D3_DIRECT_TRANSFER_PROVED=false
GENERALIZED_DIVISOR_AP_DIRECT_TRANSFER_PROVED=false
BINARY_FORM_DIVISOR_SUM_DIRECT_TRANSFER_PROVED=false
LINEAR_DIVISOR_CORRELATION_DIRECT_TRANSFER_PROVED=false
```

No searched theorem directly controls the exact Stage14 receiver. This is an applicability result, not a universal nonexistence claim.

## Why q20 is not q19 repeated

q19 asked whether the opaque second reverse layer could first be encoded into a theorem-shaped object. Merged `s7-129..131` answers that internal question: yes, and the exact stable object is the conditioned joint divisor-extension moment `J_rev2`.

q20 instead asks whether any existing theorem directly estimates this now-frozen correlation while preserving its conditioning and charged measure. Therefore the query is materially new.

## Handoffs

### Q20-A — witness-dependence separability test

```text
Q20_WITNESS_DEPENDENCE_SEPARABILITY_TEST
```

Test whether, on one frozen principal cell, the first-layer witness labels can be partitioned at `B^o(1)` cost so that

```text
W1(lambda) = F(outer(lambda)) + h
```

or another fixed-shift / fixed-form relation holds with the remaining filter represented by a theorem-admissible weight.

Target: `Stage14-s7-132`.

### Q20-B — fixed-shift or binary-form normal-form test

```text
Q20_FIXED_SHIFT_OR_BINARY_FORM_NORMAL_FORM_TEST
```

If Q20-A succeeds, identify exactly one of:

- shifted `d_3*d`;
- modified shifted `d_3` second moment;
- generalized divisor AP;
- binary-form divisor sum;
- fixed linear divisor correlation.

If no such exact normalization exists, freeze the conditioned correlation itself as the external theorem target rather than repeatedly searching looser analogues.

Target: `Stage14-s7-133+`.

## Boundary

```text
Q20_COMPONENT_COMPLETE=true
Q20_SEARCHED_PRIMARY_ARCHITECTURES=SHIFTED_D3_D+MODIFIED_SHIFTED_D3+GENERALIZED_DIVISOR_AP+BINARY_FORM_DIVISOR_SUM+LINEAR_DIVISOR_CORRELATION
Q20_DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
Q20_CONDITIONED_CORRELATION_DIRECT_THEOREM_FOUND=false
Q20_WITNESS_DEPENDENCE_SEPARABILITY_TEST_REQUIRED=true
Q20_FIXED_SHIFT_OR_BINARY_FORM_NORMAL_FORM_TEST_REQUIRED=true
Q20_POST_MASK_SEARCHED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_FROM_LITERATURE_PROVED=false
```
