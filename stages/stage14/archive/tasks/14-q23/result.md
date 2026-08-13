# Stage14-q23 — joint filtered-tau3 / reciprocal-CRT incidence first-moment literature radar

## Status

`COMPLETE_JOINT_FILTERED_TAU3_RECIPROCAL_CRT_FIRST_MOMENT_LITERATURE_RADAR`

Triggered by merged Stage14-s7-149 after the q22 handoffs both passed:

```text
Q22_GOOD_INDICATOR_EXACT_WITNESS_EXPANSION_TEST=PASS_NONNEGATIVE_Q17_WITNESS_COUNT
Q22_POSITIVE_FIRST_MOMENT_NORMAL_FORM_TEST=PASS_JOINT_NONNEGATIVE_DIVISOR_CRT_INCIDENCE
Q23_THEOREM_TARGET_NOW_STABLE=true
```

## 1. Exact target

The active nonnegative arithmetic object is

```text
J1_G
 = sum_{lambda in Lambda}
     sum_{f*n=W1(lambda)} R_q17(lambda;f,n),
```

where `lambda` is a retained filtered-tau3 first-layer witness and `R_q17` includes the already-frozen reciprocal-CRT divisor conditions, including

```text
f*n = W1(lambda),
n+f == 0 (mod 2U),
n-f == 0 (mod 2V),
```

plus the frozen q17 kernel-side labels and filters. The residual root/canonical/post-column post-mask is excluded.

The target is a uniform positive lower bound in every surviving principal cell, separately for the scalar charged measure and polynomial outer-pair `(E,m)` charged measure.

## 2. Literature radar

### Topacogullari — shifted convolution of divisor functions

Berke Topacogullari, *The Shifted Convolution of Divisor Functions*, arXiv:1506.02608, proves asymptotics with power-saving error for shifted convolutions involving `d_3(n)` and `d(n+h)`, uniformly in a shift range.

This is structurally close to a filtered-tau3 witness coupled to a second divisor condition, but the Stage14 `W1(lambda)` and the congruence/divisor packet predicates depend on the first-layer witness. No exact reduction to a fixed or uniformly admissible additive shift has been proved.

```text
TOPACOGULLARI_D3_D_NEAR=true
TOPACOGULLARI_DIRECT_TRANSFER_PROVED=false
```

### Nguyen — generalized divisor functions in arithmetic progressions

David T. Nguyen, *Generalized divisor functions in arithmetic progressions: I*, arXiv:2308.06839, gives distribution results for `d_k` in arithmetic progressions, including moduli beyond the square-root range under averaging/structural hypotheses.

This is relevant to the reciprocal-CRT congruence aspect, but the theorem does not directly preserve the witness-dependent `W1(lambda)`, all frozen q17 filters, and the charged scalar / `(E,m)` principal-cell quantifiers simultaneously.

```text
NGUYEN_GENERALIZED_DIVISOR_AP_NEAR=true
NGUYEN_DIRECT_TRANSFER_PROVED=false
```

Nguyen, *Generalized divisor functions in arithmetic progressions: II*, arXiv:2302.12815, develops modified shifted `d_3` second-moment machinery. The current Stage14 gate is a positive first moment, and the already-proved Stage14 occupancy envelope has superseded the need for another generic second-moment step.

```text
NGUYEN_MODIFIED_SHIFTED_D3_NEAR=true
NGUYEN_SECOND_MOMENT_RECHARGE_ALLOWED=false
```

### Frei--Sofos — generalized divisor sums over binary forms

Christopher Frei and Efthymios Sofos, *Generalised divisor sums of binary forms over number fields*, arXiv:1609.04002, proves asymptotics/lower bounds for broad divisor sums over values of binary forms.

A transfer would require an exact bounded-complexity binary-form representation of `W1(lambda)` together with the retained filtered-tau3 and reciprocal-CRT predicates. Such an adapter is not currently proved.

```text
FREI_SOFOS_BINARY_FORM_NEAR=true
BINARY_FORM_JOINT_INCIDENCE_ADAPTER_PROVED=false
```

## 3. Direct-theorem verdict

No located primary-source theorem directly proves the full Stage14 q23 target with all physical prefilters and charged-measure quantifiers retained.

```text
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
JOINT_FILTERED_TAU3_RECIPROCAL_CRT_FIRST_MOMENT_DIRECT_THEOREM_FOUND=false
FIXED_SHIFT_JOINT_INCIDENCE_ADAPTER_PROVED=false
DIVISOR_AP_JOINT_INCIDENCE_ADAPTER_PROVED=false
BINARY_FORM_JOINT_INCIDENCE_ADAPTER_PROVED=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
```

## 4. Falsifiable handoffs

Before another broad literature pass, expose whether the witness dependence can be separated without losing the charged measure.

```text
Q23_W1_WITNESS_DEPENDENCE_SEPARABILITY_TEST=Stage14-s7-150
Q23_FIXED_SHIFT_OR_AP_OR_BINARY_FORM_JOINT_NORMAL_FORM_TEST=Stage14-s7-151+
```

The first test should cell-decompose the frozen labels and ask whether `W1(lambda)` and `R_q17(lambda;f,n)` can be rewritten as one of:

- a fixed/uniformly controlled shifted-divisor correlation,
- a divisor function in a fixed/factorable arithmetic progression,
- a bounded-complexity binary-form divisor sum,
- or another exact standard correlation form.

Failure should freeze the current joint incidence itself as the external theorem target rather than erasing witness dependence.

```text
Q24_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```
