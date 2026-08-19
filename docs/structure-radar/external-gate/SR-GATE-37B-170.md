# StructureRadar parallel batch 37B — SR-STR-170 dyadic threshold reduction

BATCH_ID=SR-BATCH-PARALLEL-37B-170-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=B
STRUCTURE=SR-STR-170
MODE=ONE_PR_FOUR_LANES_DEEP_ATTACK
BASE_MAIN=9f70ff9c37c12981e197f0c213795fc7a906fc35
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 36B. The square-divisor witness count is already `B^o(1)` pointwise, but the audit correctly retained the genuinely weighted first moment when `0<=A(M,a)<=1` is not Boolean.

## 1. Bounded witness weights reduce to finitely many Boolean threshold masks

Fix a retained packet and normalize the witness weight so `0<=A(M,a)<=1`. For any integer `J>=1`, the elementary dyadic majorization

```text
A(M,a)
 <= sum_{j=0}^{J-1} 2^{-j} 1_{A(M,a)>2^{-j-1}} + 2^{-J}
```

holds pointwise. Applying this inside the audited square-divisor first moment gives

```text
sum_M mu(M) sum_a 1_{Ja^2|M} A(M,a)
 <= sum_{j=0}^{J-1} 2^{-j}
      sum_M mu(M) N_j(M)
    + 2^{-J} sum_M mu(M) N_all(M),
```

where `N_j(M)` counts square-divisor witnesses in the exact physical `a`-window satisfying the Boolean threshold mask `A(M,a)>2^{-j-1}`.

By 36B,

```text
N_j(M), N_all(M) <= tau(M)=B^o(1).
```

Choose `J=ceil(C log_2 B)` for any fixed large `C`. The tail is then

```text
<= B^{-C+o(1)} H_packet,
```

where `H_packet=sum_M mu(M)` is the original nonnegative packet mass. The number of threshold levels is `O(log B)=B^o(1)`, and `sum_j 2^{-j}<2`.

Thus a uniform fixed-power deficit for the Boolean threshold events is sufficient for the full bounded weighted first moment, with only `B^o(1)` bookkeeping loss and an arbitrarily small power tail.

## 2. Smaller restart point

The two-form event/weighted target from 36B can therefore be replaced by the single finite-threshold receiver

```text
FIRST_MISSING_LEMMA=PhysicalSquareDivisorDyadicThresholdEventSameMeasureDeficit
```

A sufficient form is: uniformly over every retained packet and every dyadic threshold `t=2^{-j-1}` with `0<=j<J`, prove a fixed-power deficit for the exact event

```text
exists a in I_A : J a^2 | M and A(M,a)>t,
```

on the same physical `M`-measure, retaining the actual `a`-window, endpoint headroom, cofactor/canonical masks, and quantifier order. The 36B witness multiplicity then converts threshold-event mass to threshold witness-count mass at only `B^o(1)` cost.

No ordinary-divisor theorem or independence assumption is introduced.

## 3. Firewalls

```text
SQUARE_DIVISOR_WITNESS_MULTIPLICITY_SUBPOLYNOMIAL_REUSED=true
BOUNDED_WEIGHT_DYADIC_THRESHOLD_REDUCTION=PROVED
THRESHOLD_LEVEL_COUNT_SUBPOLYNOMIAL=true
WEIGHT_TAIL_FIXED_POWER_NEGLIGIBLE=true
WITNESS_DEPENDENT_MASKS_RETAINED=true
PHYSICAL_THRESHOLD_EVENT_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=PhysicalSquareDivisorDyadicThresholdEventSameMeasureDeficit
SR_STR_170_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
NOVELTY_BY_SEARCH_ABSENCE=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
