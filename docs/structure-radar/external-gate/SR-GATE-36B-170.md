# StructureRadar parallel batch 36B — SR-STR-170 square-divisor witness-event reduction

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

On the physical packet the masks are indicators (or bounded nonnegative weights after the existing normalization), so take `0<=A(M,a)<=1`. For fixed `M`, any contributing witness satisfies `J a^2 | M`. Hence

```text
#{a : J a^2 | M} <= #{a : a^2 | M}.
```

If `M=prod p^{v_p(M)}`, the number of square-divisor roots is exactly

```text
prod_p (floor(v_p(M)/2)+1) <= tau(M).
```

On the existing polynomial-height range, `tau(M)=B^o(1)`. Therefore pointwise

```text
1_{physical square-divisor witness exists}
 <= sum_{a in I_A} 1_{Ja^2|M} A(M,a)
 <= B^o(1) 1_{physical square-divisor witness exists}
```

for Boolean physical masks, with the same upper multiplicity statement for bounded nonnegative weights.

Thus the lane35B witness first moment does not introduce a hidden polynomial union-bound loss. Up to `B^o(1)`, the unresolved mass is the exact same-measure physical square-divisor witness event itself.

## 2. New restart point

The remaining target can therefore be narrowed from a dilation first moment to

```text
FIRST_MISSING_LEMMA=PhysicalSquareDivisorWitnessEventSameMeasureDeficit
```

A sufficient form is:

> Uniformly on every retained packet, prove that the exact physical event
> `exists a in I_A : J a^2 | M` together with its witness-dependent cofactor/canonical masks carries at most `B^{-delta+o(1)}` of the original charged packet mass, for some fixed `delta>0`, with the actual physical window, endpoint headroom and quantifier order retained.

The first-moment formulation and the event formulation differ only by `B^o(1)` witness multiplicity on the current height range. No ambient ordinary-divisor theorem is imported and no independence is assumed.

## 3. Firewalls

```text
WEIGHTED_SQUARE_DILATE_UNFOLDING_REUSED=true
SQUARE_DIVISOR_WITNESS_MULTIPLICITY_SUBPOLYNOMIAL=PROVED
WITNESS_MASKS_RETAINED=true
UNION_BOUND_FIXED_POWER_LOSS=false
PHYSICAL_SQUARE_DIVISOR_EVENT_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=PhysicalSquareDivisorWitnessEventSameMeasureDeficit
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
