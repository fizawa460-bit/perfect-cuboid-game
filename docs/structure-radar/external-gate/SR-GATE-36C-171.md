# StructureRadar parallel batch 36C — SR-STR-171 localized divisor witness-event reduction

BATCH_ID=SR-BATCH-PARALLEL-36C-171-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=C
STRUCTURE=SR-STR-171
MODE=PARALLEL_DEEP_ATTACK
BASE_MAIN=8e7dd3e8410aad9d33734de2598bae25630901ce
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 35C. There the physical unitary-shadow upper lane was reduced to the exact witness-weighted divisor first moment

```text
sum_{d in I} sum_k mu(dk) A(dk,d),
```

with every divisor-witness-dependent mask retained.

## 1. Divisor-witness multiplicity has no fixed-power cost

For the retained Boolean/bounded physical masks take `0<=A(m,d)<=1`. For fixed `m`, every contributing witness is an ordinary divisor of `m`, so

```text
#{d in I : d|m and A(m,d)>0} <= tau(m).
```

On the current polynomial-height range, `tau(m)=B^o(1)`. Therefore, pointwise for Boolean masks,

```text
1_{physical localized divisor witness exists}
 <= sum_{d in I} 1_{d|m} A(m,d)
 <= B^o(1) 1_{physical localized divisor witness exists}.
```

Combining with the already-audited one-sided implication `u||m => u|m`, the lane35C first-moment normalization carries no hidden polynomial witness-overcount. Its fixed-power content is exactly the scarcity, on the same charged physical measure, of the localized divisor witness event with all masks retained.

This does not identify unitary and ordinary support from below; it only says the ordinary witness first moment and ordinary witness event are `B^o(1)`-equivalent for the upper lane.

## 2. New restart point

```text
FIRST_MISSING_LEMMA=PhysicalLocalizedDivisorWitnessEventSameMeasureDeficit
```

A sufficient form is:

> Uniformly on each retained packet, prove that the exact physical event
> `exists d in I : d|m` together with its divisor-witness-dependent physical masks has mass at most `B^{-delta+o(1)}` times the original packet mass, for one fixed `delta>0`, preserving the actual interval, endpoint headroom, frozen radial/cofactor variables and quantifier order.

Any localized divisor theorem may be used only after matching this exact same-measure event. No independent saving may be multiplied with the SR-STR-170 squareclass lane.

## 3. Firewalls

```text
UNITARY_TO_ORDINARY_UPPER_SHADOW_REUSED=true
WEIGHTED_DIVISOR_DILATION_UNFOLDING_REUSED=true
DIVISOR_WITNESS_MULTIPLICITY_SUBPOLYNOMIAL=PROVED
WITNESS_DEPENDENT_MASKS_RETAINED=true
UNITARY_TO_ORDINARY_LOWER_EQUIVALENCE_PROVED=false
PHYSICAL_LOCALIZED_DIVISOR_EVENT_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=PhysicalLocalizedDivisorWitnessEventSameMeasureDeficit
SR_STR_171_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
NOVELTY_BY_SEARCH_ABSENCE=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
