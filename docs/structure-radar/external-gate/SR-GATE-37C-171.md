# StructureRadar parallel batch 37C — SR-STR-171 dyadic threshold reduction

BATCH_ID=SR-BATCH-PARALLEL-37C-171-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=C
STRUCTURE=SR-STR-171
MODE=ONE_PR_FOUR_LANES_DEEP_ATTACK
BASE_MAIN=9f70ff9c37c12981e197f0c213795fc7a906fc35
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 36C. The localized ordinary-divisor witness multiplicity is already `B^o(1)` pointwise, while genuinely bounded witness weights `0<=A(m,d)<=1` remain canonical.

## 1. Exact bounded-weight reduction to dyadic Boolean threshold masks

Let `K>=1` denote the dyadic threshold depth. Pointwise,

```text
A(m,d)
 <= sum_{j=0}^{K-1} 2^{-j} 1_{A(m,d)>2^{-j-1}} + 2^{-K}.
```

Insert this into the audited localized divisor first moment:

```text
sum_m mu(m) sum_{d in I} 1_{d|m} A(m,d)
 <= sum_{j=0}^{K-1} 2^{-j}
      sum_m mu(m) N_j(m)
    + 2^{-K} sum_m mu(m) N_all(m),
```

where `N_j(m)` counts divisors `d in I` satisfying both `d|m` and the Boolean threshold mask `A(m,d)>2^{-j-1}`.

By 36C,

```text
N_j(m), N_all(m) <= tau(m)=B^o(1).
```

Choose `K=ceil(C log_2 B)` for fixed large `C`. Then the residual tail is

```text
<= B^{-C+o(1)} H_packet,
```

with `H_packet=sum_m mu(m)`, while the number of threshold levels is only `O(log B)=B^o(1)` and their geometric coefficients have bounded total mass.

Therefore a uniform same-measure fixed-power theorem for these Boolean threshold events is sufficient for the full bounded weighted first moment. The previous lack of a reverse inequality for arbitrary positive weights is no longer a separate obstruction.

## 2. Smaller restart point

```text
FIRST_MISSING_LEMMA=PhysicalLocalizedDivisorDyadicThresholdEventSameMeasureDeficit
```

A sufficient form is: uniformly over every retained packet and every dyadic threshold `t=2^{-j-1}` with `0<=j<K`, prove a fixed-power deficit for

```text
exists d in I : d|m and A(m,d)>t,
```

on the exact physical `m`-measure, preserving the actual localized interval, endpoint headroom, frozen radial/cofactor variables, witness masks and quantifier order. The already-audited one-sided transfer `u||m => u|m` remains one-sided only.

This lane and SR-STR-170 remain two upper shadows of charged support and may not be multiplied as independent savings.

## 3. Firewalls

```text
UNITARY_TO_ORDINARY_UPPER_SHADOW_REUSED=true
DIVISOR_WITNESS_MULTIPLICITY_SUBPOLYNOMIAL_REUSED=true
BOUNDED_WEIGHT_DYADIC_THRESHOLD_REDUCTION=PROVED
DYADIC_DEPTH_SYMBOL_SEPARATED=true
THRESHOLD_LEVEL_COUNT_SUBPOLYNOMIAL=true
WEIGHT_TAIL_FIXED_POWER_NEGLIGIBLE=true
UNITARY_TO_ORDINARY_LOWER_EQUIVALENCE_PROVED=false
NO_DOUBLE_CHARGE_WITH_SR_STR_170=true
PHYSICAL_THRESHOLD_EVENT_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=PhysicalLocalizedDivisorDyadicThresholdEventSameMeasureDeficit
SR_STR_171_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
NOVELTY_BY_SEARCH_ABSENCE=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
