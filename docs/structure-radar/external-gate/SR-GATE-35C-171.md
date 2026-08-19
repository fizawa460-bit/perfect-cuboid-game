# StructureRadar parallel batch 35C — SR-STR-171 weighted divisor-dilate unfolding

BATCH_ID=SR-BATCH-PARALLEL-35C-171-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=C
STRUCTURE=SR-STR-171
MODE=PARALLEL_DEEP_ATTACK
BASE_MAIN=4d87d7f5461ee019229b31cd5f8c0947e13dbc0c
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 33C. The unitary restriction was already removed one-sidedly for upper bounds by `u || m => u | m`. The remaining restart point asked for a published ordinary-divisor-window theorem on the exact physical measure and window.

## 1. Exact weighted divisor-incidence unfolding

Let `w(m)>=0` be the exact charged packet weight and let `I` be the localized divisor window. Pointwise,

```text
1_{exists d|m, d in I}
 <= sum_{d in I} 1_{d|m}.
```

Hence

```text
sum_m w(m) 1_{exists d|m, d in I}
 <= sum_{d in I} sum_{k>=1} w(dk).
```

Combining with the merged unitary-to-ordinary inclusion gives

```text
sum_m w(m) 1_{exists u||m, u in I}
 <= sum_{d in I} sum_k w(dk).
```

This is an exact same-measure first-moment reduction. It does not require any density equivalence between unitary and ordinary divisors and does not discard the physical conditioning: all remaining masks may stay inside `w(dk)`.

## 2. Smaller theorem target

The previous restart point `PhysicalLocalizedOrdinaryDivisorWindowMeasureAndWidthCompatibility` is again sufficient but stronger than necessary. The live requirement can be stated directly as

```text
FIRST_MISSING_LEMMA=PhysicalLocalizedDivisorDilationMassDeficit
```

A sufficient form is:

> On every retained physical packet, with the actual localized interval `I`, prove
> `sum_{d in I} sum_k w(dk) <= B^{-delta+o(1)} sum_m w(m)`
> for one fixed `delta>0`, uniformly in the frozen radial/cofactor variables and with at most `B^o(1)` loss after packet summation.

A Ford/Drappeau--Mounier-type support theorem may imply this if its measure matches, but the proof target is now the concrete weighted dilation mass rather than a full theorem about the ambient ordinary-divisor support distribution.

## 3. Relation to SR-STR-170

The 35B squareclass lane has the stricter right-hand side `sum_a sum_k w(J a^2 k)`. This lane has `sum_d sum_k w(dk)`. They are two upper shadows of the same charged support and cannot be multiplied as independent savings. If one common weighted dilation theorem controls both, only one fixed-power charge is available.

## 4. Firewalls

```text
UNITARY_TO_ORDINARY_UPPER_SHADOW_REUSED=true
WEIGHTED_DIVISOR_DILATION_UNFOLDING=PROVED
FULL_ORDINARY_DIVISOR_SUPPORT_THEOREM_REQUIRED=false
PHYSICAL_LOCALIZED_DILATION_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=PhysicalLocalizedDivisorDilationMassDeficit
SR_STR_171_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
