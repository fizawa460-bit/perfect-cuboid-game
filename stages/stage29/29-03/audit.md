# Stage29-03 — adversarial audit

```text
AUDITED_PR=1308
AUDITED_SUBMISSION_HEAD=6615f33acdaffe9297c8efd68dd944e9ebb3bc1c
AUDIT_MODE=ADVERSARIAL_EXECUTION_LOCATION_AND_BACKFLOW_ROUTING
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
```

## Executive verdict

The main execution-location decision survives: **no Stage16–28 addendum is required now**. The four bridge receivers can be tested inside Stage29 against already-audited old-stage outputs before any old certified contract is modified.

One routing-semantic defect was found. The submission used

```text
BACKFLOW_QUEUE_SIZE=0
DECISION=STAGE29_INTERNAL_ADAPTER_ONLY
```

while the audited 29-02ha route contract had already recorded

```text
R29-KUM4=NEW_TARGETED_BACKFLOW_RECEIVER_NOT_EXECUTED.
```

Those statements are compatible only if `queue=0` means **active backflow executions now**, not that no conditional backflow candidate exists, and if `INTERNAL_ADAPTER_ONLY` is read as an initial execution location rather than a permanent prohibition on a later targeted addendum. The audit repairs this explicitly.

## Attack 1 — false no-backflow / history erasure

### R29-KUM3A

`R29-KUM3A` compares the new F7 sign-subcover language with the already-audited Stage28 common host. Stage28's certified results need not be changed merely to prove a new comparison map. Therefore:

```text
R29-KUM3A_DECISION=STAGE29_INTERNAL_FIRST
ACTIVE_BACKFLOW_REQUIRED_NOW=false
EXECUTION_OWNER=29-07
```

If the comparison later proves that a Stage28 certified contract itself must be extended or corrected, a narrow Stage28 addendum is still allowed under the R2 policy.

### R29-KUM3B

The audited 29-02b joint V4 model is already Stage29-native and exact at the stated dense-open/function-field scope. The missing statement is its exact relation to F7. The 29-02ha contract also marks KUM3B as formal conditional on KUM3A. Thus:

```text
R29-KUM3B_DECISION=STAGE29_INTERNAL_FIRST
DEPENDENCY=R29-KUM3A
ACTIVE_BACKFLOW_REQUIRED_NOW=false
```

No conclusion is inferred merely from matching `(Z/2)^2` ranks or from counting square roots.

### R29-KUM4 — bounded repair

This receiver spans Stage16–20 and was explicitly introduced in 29-02ha as a targeted-backflow receiver not yet executed. R2 subsequently established the stricter rule that an old stage is reopened only when its certified contract must actually be extended/corrected.

Therefore the exact audited state is:

```text
R29-KUM4_EXECUTION_DECISION=STAGE29_INTERNAL_FIRST_WITH_CONDITIONAL_BACKFLOW_WATCH
ACTIVE_BACKFLOW_REQUIRED_NOW=false
CONDITIONAL_BACKFLOW_CANDIDATE=true
CONDITIONAL_BACKFLOW_TRIGGER=29-04_OR_29-07_PROVES_OLD_CERTIFIED_CONTRACT_REQUIRES_EXTENSION_OR_CORRECTION
```

This preserves both pieces of audited history instead of silently overwriting one with the other.

## Attack 2 — KUM4 population overreach

No literal sign-tower population identification is proved at 29-03. The following remain independent obligations for 29-04/07:

```text
COMMON_HOST_AND_EXACT_MASKS
PHYSICAL_HEIGHT_COMPATIBILITY
PRIMITIVE_NORMALIZATION_COMPATIBILITY
CANONICAL_ORDER_COMPATIBILITY
MULTIPLICITY_COMPATIBILITY
```

The roadmap-R2 firewalls remain unchanged:

```text
STAGE16_20_AS_LITERAL_SIGN_TOWER_LEVELS_PROVED=false
POPULATION_TRANSFER_TO_SIGN_TOWER_AUTOMATIC=false
N2_over_M2_is_literal_finite_survival=true
M3_over_M2_is_objectwise_survival=false
M3_over_N2_is_survival_probability=false
```

Hence no old population theorem is reinterpreted by analogy at this checkpoint.

## Attack 3 — Peschmann premature collapse / premature rejection

The 29-02hd audit left both of these false:

```text
PESCHMANN_PROVEN_F2_ADAPTER=false
PESCHMANN_INDEPENDENCE_RESOLVED=false
```

29-08 is a reasonable primary owner for the exact crosswalk because it is the parametrization/fibration/coverage stage. However, **failure** to construct the F2 crosswalk must not automatically mark the route RED or redundant. A failed exact crosswalk may instead be evidence that the route is genuinely independent.

The repaired routing adds:

```text
PESCH1_CROSSWALK_SUCCESS => ADAPTER_CLASSIFICATION
PESCH1_CROSSWALK_FAILURE => INDEPENDENCE_REASSESSMENT_REQUIRED
AUTO_RED_ON_CROSSWALK_FAILURE=false
29_02H_NAMESPACE_REOPENABLE_IF_NEW_INDEPENDENT_FOUNDATION_CERTIFIED=true
```

## Attack 4 — anti-loop and old-stage immutability

The proposed backflow trigger contract is consistent with roadmap R2. A targeted addendum requires a named old stage, a named certified statement/adapter that must change, an exact new receiver, and a reimport contract. A new geometric interpretation alone does not reopen an audited stage.

```text
SEQUENTIAL_STAGE16_28_RERUN=false
OLD_FROZEN_GATE_REPLAY=false
GLOBAL_STAGE_REOPEN=false
COMPLETED_AUDITED_ITEMS_IMMUTABLE=true
TARGETED_ADDENDUM_IF_CONTRACT_CHANGE_ONLY=true
```

## Attack 5 — queue order / route pruning

The immediate order survives audit:

```text
29-04 population host/predicate matrix
29-05 dependency + route ownership
GAP_SCAN_A / roadmap review
29-06 global synthesis
29-07 KUM3A/B + geometric KUM4 bridge
29-08 Peschmann exact crosswalk / parametrization atlas
```

29-04 must precede KUM4 population interpretation. 29-05 must deduplicate routes before the attack portfolios. No Campedelli, Beauville, modular, Brauer, K3, local, or full-surface route is pruned at 29-03.

## Audited backflow state

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[R29-KUM4]
BACKFLOW_CANDIDATES_PROVED_EMPTY=false
```

The last line is load-bearing: a zero active queue is an execution decision, not a theorem that no future targeted backflow can become necessary.

## Final state

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_03_AUDIT=PASS
BOUNDED_REPAIR=ACTIVE_VS_CONDITIONAL_BACKFLOW_SEMANTICS_PLUS_INTERNAL_FIRST_WORDING_PLUS_PESCHMANN_FAILURE_REASSESSMENT
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[R29-KUM4]
NEXT_ITEM=29-04_POPULATION_HOST_PREDICATE_AND_CONDITION_COST_MATRIX
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```