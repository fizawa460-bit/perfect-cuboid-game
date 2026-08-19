# StructureRadar parallel batch 33C — SR-STR-171 unitary-to-ordinary shadow contraction

BATCH_ID=SR-BATCH-PARALLEL-33C-171-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=C
STRUCTURE=SR-STR-171
MODE=PARALLEL_DEEP_ATTACK
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from merged Stage14 q15, where the heavy obstruction was split into bare localized unitary-divisor shadow sparsity plus a separate conditional canonical/reverse physical-completion deficit.

The q15 handoff asked whether the unitary restriction could be imposed/removed with only `B^o(1)` distortion before using ordinary-divisor interval theorems. For the upper-sparsity direction actually needed by this gate, that transfer question is stronger than necessary.

## 1. Exact one-sided transfer

By definition

```text
u || m
  iff
u | m and gcd(u,m/u)=1.
```

Therefore every unitary divisor is an ordinary divisor. For any interval/window `I`, pointwise in `m`,

```text
1_{exists u || m, u in I}
 <=
1_{exists d | m, d in I}.
```

This is an exact domination with constant 1. No average argument, Möbius expansion, or bounded-distortion estimate is needed to pass from unitary support to ordinary support when proving an upper bound for the exceptional set.

The same statement remains true after multiplying both sides by any nonnegative physical packet weight. Hence the coprime-complement condition cannot make the unitary exceptional set larger than the ordinary-divisor shadow on the identical underlying measure.

## 2. What this does and does not prove

This proves the transfer needed only for an upper-support/sparsity theorem. It does **not** prove:

- a lower-density equivalence between unitary and ordinary divisors;
- an asymptotic with the same constant;
- that the Stage14 physical integer distribution satisfies the hypotheses of Ford/Drappeau--Mounier-type ordinary-divisor theorems;
- that the actual window has the required exponent width;
- that the separate canonical/reverse completion factor supplies any saving.

Thus the unitary-to-ordinary part of the old gate is discharged, but theorem/measure/window compatibility remains.

## 3. Smaller missing lemma

The surviving bridge is

```text
FIRST_MISSING_LEMMA=PhysicalLocalizedOrdinaryDivisorWindowMeasureAndWidthCompatibility
```

A sufficient form is:

> For the exact nonnegative Stage14 packet measure feeding the live Stage27-19 boundary/outer-support receiver, prove that the ordinary-divisor shadow window produced by the merged reciprocal normalization lies in a published localized-divisor upper-support regime with one fixed positive power. Verify the actual multiplicative/exponent width, all endpoint headroom, and all conditioning on the radial/cofactor variables. Sum the packetized bounds with at most `B^o(1)` loss.

Once this lemma is available, the same fixed-power upper bound immediately applies to the localized unitary-divisor support by the exact pointwise inclusion above. No separate `UNITARY_TO_ORDINARY_LOCALIZED_SHADOW_BOUNDED_DISTORTION` theorem is needed for this upper lane.

## 4. Relation to SR-STR-170

SR-STR-170 concerns the additional squareclass/square-divisor restriction in the reciprocal divisor coordinate. SR-STR-171 concerns unitary support. Their one-sided ordinary-divisor shadows can be compared on a common physical packet, but they are alternative restrictions of the same charged arithmetic support and may not be multiplied as independent savings.

## 5. Verdict / firewalls

```text
UNITARY_DIVISOR_SUPPORT_SUBSET_OF_ORDINARY_DIVISOR_SUPPORT=PROVED
UNITARY_TO_ORDINARY_UPPER_SHADOW_DISTORTION=1
UNITARY_TO_ORDINARY_LOWER_EQUIVALENCE_PROVED=false
PHYSICAL_ORDINARY_DIVISOR_MEASURE_COMPATIBILITY_PROVED=false
PHYSICAL_WINDOW_WIDTH_COMPATIBILITY_PROVED=false
CANONICAL_REVERSE_COMPLETION_SAVING_PROVED=false
FIRST_MISSING_LEMMA=PhysicalLocalizedOrdinaryDivisorWindowMeasureAndWidthCompatibility
SR_STR_171_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
