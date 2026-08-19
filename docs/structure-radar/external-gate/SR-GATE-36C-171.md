# StructureRadar parallel batch 36C — SR-STR-171 localized divisor witness multiplicity

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

For fixed `m`, every contributing witness is an ordinary divisor of `m`, so

```text
#{d in I : d|m and A(m,d)>0} <= tau(m).
```

On the current polynomial-height range, `tau(m)=B^o(1)`. For the Boolean-mask branch `A(m,d) in {0,1}` this gives pointwise

```text
1_{exists d in I : d|m and A(m,d)=1}
 <= sum_{d in I} 1_{d|m} A(m,d)
 <= B^o(1) 1_{exists d in I : d|m and A(m,d)=1}.
```

Thus the ordinary witness first moment and ordinary witness event are `B^o(1)`-equivalent on Boolean-mask packets.

For merely bounded normalized weights `0<=A(m,d)<=1`, only

```text
sum_{d in I} 1_{d|m} A(m,d)
 <= B^o(1) 1_{exists d in I : d|m and A(m,d)>0}
```

is automatic. The reverse event-to-weight inequality is not claimed without a positive lower bound on active weights. Therefore a genuinely weighted packet must retain the audited weighted first moment as the theorem target.

The already-audited implication `u||m => u|m` remains one-sided. Nothing here supplies a lower equivalence between unitary and ordinary support.

## 2. Repaired restart point

```text
FIRST_MISSING_LEMMA=PhysicalLocalizedDivisorWitnessEventOrWeightedMassSameMeasureDeficit
```

A sufficient form is either:

1. on Boolean-mask packets, prove a fixed-power deficit for the exact localized ordinary-divisor witness event with all masks retained; or
2. on genuinely weighted packets, prove the corresponding fixed-power deficit directly for `sum_{d in I}1_{d|m}A(m,d)`.

The actual interval, endpoint headroom, frozen radial/cofactor variables, witness-dependent masks and quantifier order must be preserved. No independent saving may be multiplied with the SR-STR-170 squareclass lane.

## 3. Firewalls

```text
UNITARY_TO_ORDINARY_UPPER_SHADOW_REUSED=true
WEIGHTED_DIVISOR_DILATION_UNFOLDING_REUSED=true
DIVISOR_WITNESS_MULTIPLICITY_SUBPOLYNOMIAL=PROVED
BOOLEAN_WITNESS_EVENT_EQUIVALENCE_UP_TO_SUBPOLYNOMIAL=PROVED
BOUNDED_WEIGHT_EVENT_EQUIVALENCE_PROVED=false
WITNESS_DEPENDENT_MASKS_RETAINED=true
UNITARY_TO_ORDINARY_LOWER_EQUIVALENCE_PROVED=false
PHYSICAL_LOCALIZED_DIVISOR_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=PhysicalLocalizedDivisorWitnessEventOrWeightedMassSameMeasureDeficit
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
