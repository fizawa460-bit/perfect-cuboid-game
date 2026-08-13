# Stage14-Work-ckX49 — joint filtered-tau3 / reciprocal-CRT first-moment isolation

## Status

`COMPLETE_JOINT_FILTERED_TAU3_RECIPROCAL_CRT_FIRST_MOMENT_ISOLATION`

Consumes merged Work-cjX48/q22 and merged Stage14-s7-147..149 from main `a08d4c9a21290271e5c598d1eeda74c46e5a638c`.

## 1. Consumed receiver change

Stage14-s7-147 proves the fixed-power equivalence

```text
M1_G <= J1_G <= B^o(1) M1_G,
```

where `M1_G=sum_lambda 1_G(pi(lambda))` and `J1_G` counts nonnegative q17 reciprocal-CRT witnesses over the retained filtered-tau3 witnesses.

Stage14-s7-148 then unfolds `J1_G` exactly as

```text
J1_G
 = sum_{lambda in Lambda}
     sum_{f*n=W1(lambda)} R_q17(lambda;f,n),
```

with the already-frozen first-layer filter retained in `lambda` and with the q17 congruences

```text
n+f == 0 (mod 2U),
n-f == 0 (mod 2V).
```

The residual root/canonical/post-column mask is not included in this arithmetic receiver.

```text
GOOD_INDICATOR_TO_Q17_WITNESS_EQUIVALENCE_CONSUMED=true
JOINT_FILTERED_TAU3_Q17_CRT_INCIDENCE_NORMAL_FORM_CONSUMED=true
GOOD_PACKET_SECOND_MOMENT_RECHARGE_FORBIDDEN=true
Q17_WITNESS_MULTIPLICITY_RECHARGED_AS_SAVING=false
```

## 2. Charged theorem species

Exactly two noninterchangeable theorem measures remain:

```text
UniformScalarFilteredTau3ConditionedQ17ReciprocalCRTJointIncidenceFirstMomentLowerBound

UniformPolynomialOuterPairFilteredTau3ConditionedQ17ReciprocalCRTJointIncidenceFirstMomentLowerBound
```

For the second species `(E,m)` remains the charged outer pair. No map `(E,m)->Em` is used to scalarize the theorem measure.

```text
S_JOINT_INCIDENCE_THEOREM_SPECIES_COUNT=2
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
```

## 3. Charged-once ledger

Let `sigma_mult` be the already-charged first-layer support exponent, `sigma_joint` the exponent delivered by the joint incidence first moment, and `tau_phys` the final physical support exponent after the residual post-mask. Then

```text
delta_joint := sigma_mult - sigma_joint,
delta_post  := sigma_joint - tau_phys,

tau_phys = sigma_mult - delta_joint - delta_post.
```

The following are already consumed and cannot be charged again as independent fixed-power losses or savings:

- filtered-tau3 candidate multiplicity/support conversion,
- q17 reciprocal-CRT inner-kernel identification/search,
- q17 witness multiplicity,
- pushforward occupancy,
- good-packet hit support / witness support equivalence,
- good-indicator second moment,
- fixed `(E,m)->Em` fibers.

```text
RESOLVED_SUPPORT_TO_MOMENT_ADAPTER_RECHARGE_FORBIDDEN=true
JOINT_INCIDENCE_IS_CURRENT_S_ARITHMETIC_RECEIVER=true
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
```

## 4. q23 trigger

Stage14-s7-149 freezes `Q23_THEOREM_TARGET_NOW_STABLE=true`. The active object is no longer a Boolean indicator or an unspecified measure-transfer adapter, but an exact nonnegative joint filtered-tau3 / reciprocal-CRT incidence first moment. This is a new stable literature target relative to q22.

```text
Q_COMPONENT=COMPLETE
Q_TRIGGER_STAGE=Stage14-s7-149
Q_LEDGER_BASELINE=Stage14-q22
Q23_NEEDED=true
Q23_THEOREM_TARGET_NOW_STABLE=true
```

## 5. Other route gates remain independent

The aligned main/s fixed-E gate and the fixed-U super-Kai individual-residue gate remain independently parked. Neither is identified with the new s joint-incidence receiver.

```text
MAINLINE_H_NEEDED=true
MAINLINE_H_COMPLETED=true
MAINLINE_BLOCKED_BY_H=true
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
FIXED_U_H_COMPLETED=true
FIXED_U_BLOCKED_BY_H=true
TH33_COMPLETE_CONSUMED=true
TH34_NEEDED=false
WHOLE_STAGE14_BLOCKED_BY_EXTERNAL_GATES=false
```

## 6. Exponent / adapter locks

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

## 7. Next

Primary s handoffs from q23 are expected at Stage14-s7-150+.

Normal XQ revisit: approximately `s7-152`, or earlier on a successful separability/normal-form adapter for the joint incidence, a material post-mask receiver change, resolution of either parked external gate, or an exponent change.
