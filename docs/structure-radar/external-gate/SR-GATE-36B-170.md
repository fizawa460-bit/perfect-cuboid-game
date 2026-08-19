# StructureRadar parallel batch 36B — SR-STR-170 square-divisor witness multiplicity

BATCH_ID=SR-BATCH-PARALLEL-36B-170-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=B
STRUCTURE=SR-STR-170
MODE=PARALLEL_DEEP_ATTACK
BASE_MAIN=8e7dd3e8410aad9d33734de2598bae25630901ce
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 35B. There the squareclass branch was unfolded exactly to the witness-indexed first moment

```text
sum_{a in I_A} sum_k mu(Ja^2k) A(Ja^2k,a),
```

with the cofactor/canonical masks retained in the witness variable `a`.

## 1. Witness multiplicity is only subpolynomial

For fixed `M`, every contributing witness satisfies `J a^2 | M`. Hence

```text
#{a : J a^2 | M} <= #{a : a^2 | M}.
```

If `M=prod p^{v_p(M)}`, the number of square-divisor roots is exactly

```text
prod_p (floor(v_p(M)/2)+1) <= tau(M).
```

On the existing polynomial-height range, `tau(M)=B^o(1)`. Therefore for the exact Boolean-mask branch `A(M,a) in {0,1}` we have pointwise

```text
1_{exists a in I_A : Ja^2|M and A(M,a)=1}
 <= sum_{a in I_A} 1_{Ja^2|M} A(M,a)
 <= B^o(1) 1_{exists a in I_A : Ja^2|M and A(M,a)=1}.
```

Thus, when the retained witness masks are Boolean indicators, the lane35B first moment and the exact witness event differ by only `B^o(1)` multiplicity.

For a merely bounded nonnegative normalized weight `0<=A(M,a)<=1`, only the upper multiplicity statement is automatic:

```text
sum_{a in I_A} 1_{Ja^2|M} A(M,a)
 <= B^o(1) 1_{exists a in I_A : Ja^2|M and A(M,a)>0}.
```

The reverse event-to-weight inequality is not asserted without a uniform positive lower bound on active weights. Hence the weighted first moment remains the canonical target on any genuinely weighted packet.

## 2. Repaired restart point

The audit therefore records a two-form same-measure target:

```text
FIRST_MISSING_LEMMA=PhysicalSquareDivisorWitnessEventOrWeightedMassSameMeasureDeficit
```

A sufficient form is either:

1. on Boolean-mask packets, prove a fixed-power deficit for the exact event `exists a in I_A : J a^2|M and A(M,a)=1`; or
2. on genuinely weighted packets, prove the same fixed-power deficit directly for the audited witness first moment `sum_a 1_{Ja^2|M}A(M,a)`.

In both cases the actual physical window, endpoint headroom, witness-dependent cofactor/canonical masks and quantifier order must be retained. No ambient ordinary-divisor theorem is imported and no independence is assumed.

## 3. Firewalls

```text
WEIGHTED_SQUARE_DILATE_UNFOLDING_REUSED=true
SQUARE_DIVISOR_WITNESS_MULTIPLICITY_SUBPOLYNOMIAL=PROVED
BOOLEAN_WITNESS_EVENT_EQUIVALENCE_UP_TO_SUBPOLYNOMIAL=PROVED
BOUNDED_WEIGHT_EVENT_EQUIVALENCE_PROVED=false
WITNESS_MASKS_RETAINED=true
UNION_BOUND_FIXED_POWER_LOSS=false
PHYSICAL_SQUARE_DIVISOR_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=PhysicalSquareDivisorWitnessEventOrWeightedMassSameMeasureDeficit
SR_STR_170_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
NOVELTY_BY_SEARCH_ABSENCE=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
