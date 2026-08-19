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

## 1. Exact weighted divisor-incidence unfolding with witness-dependent masks retained

Let `mu(m)>=0` be the nonnegative base packet mass after data independent of the divisor witness are frozen. Let `A(m,d)` be the exact remaining nonnegative witness-admissibility/physical-mask factor for divisor candidate `d`, and let `I` be the localized divisor window.

Pointwise, the physical ordinary-shadow event is bounded by the witness first moment

```text
physical_ordinary_shadow(m)
 <= sum_{d in I} 1_{d|m} A(m,d).
```

Thus

```text
sum_m mu(m) physical_ordinary_shadow(m)
 <= sum_{d in I} sum_{k>=1} mu(dk) A(dk,d).
```

Combining with the merged unitary-to-ordinary inclusion gives the same upper bound for the physical unitary-shadow event. Define

```text
w_d(k) = mu(dk) A(dk,d).
```

Then the live right-hand side is `sum_d sum_k w_d(k)`. This is an exact same-measure first-moment reduction and keeps any divisor-witness-dependent physical conditioning attached to that witness. In the bare q15 shadow where no such extra witness mask is present, `A=1` and this reduces to the simpler `sum_d sum_k w(dk)` formula.

## 2. Smaller theorem target

The previous restart point `PhysicalLocalizedOrdinaryDivisorWindowMeasureAndWidthCompatibility` is sufficient but stronger than necessary. The live requirement can be stated directly as

```text
FIRST_MISSING_LEMMA=PhysicalLocalizedDivisorDilationWitnessWeightedMassDeficit
```

A sufficient form is:

> On every retained physical packet, with the actual localized interval `I`, prove
> `sum_{d in I} sum_k w_d(k) <= B^{-delta+o(1)} H_packet`
> for one fixed `delta>0`, uniformly in the frozen radial/cofactor variables, retaining any divisor-witness-dependent masks, and with at most `B^o(1)` loss after packet summation.

A Ford/Drappeau--Mounier-type support theorem may imply this if its measure matches, but the proof target is now the concrete witness-weighted dilation mass rather than a full theorem about the ambient ordinary-divisor support distribution.

## 3. Relation to SR-STR-170

The 35B squareclass lane has the stricter square-dilate right-hand side. This lane has the general divisor-dilate right-hand side. They are two upper shadows of the same charged support and cannot be multiplied as independent savings. If one common weighted dilation theorem controls both, only one fixed-power charge is available.

## 4. Firewalls

```text
UNITARY_TO_ORDINARY_UPPER_SHADOW_REUSED=true
WEIGHTED_DIVISOR_DILATION_UNFOLDING=PROVED
WITNESS_DEPENDENT_MASKS_RETAINED=true
FULL_ORDINARY_DIVISOR_SUPPORT_THEOREM_REQUIRED=false
PHYSICAL_LOCALIZED_DILATION_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=PhysicalLocalizedDivisorDilationWitnessWeightedMassDeficit
SR_STR_171_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
