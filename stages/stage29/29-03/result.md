# Stage29-03 — foundation backflow decision and bridge queue lock

```text
TASK_ID=Stage29-03
ROLE=FOUNDATION_BACKFLOW_DECISION_AND_BRIDGE_QUEUE_LOCK
ROADMAP_REVISION=R2_POST_29_02_FOUNDATION_SCREEN_AUDITED
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Decision

No Stage16–28 stage is reopened at this checkpoint.

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
STAGE16_28_SEQUENTIAL_RERUN=false
OLD_FROZEN_GATE_REPLAY=false
BACKFLOW_QUEUE_SIZE=0
```

This is not a claim that the Stage16–20 population program has already been identified with successive levels of the degree-64 sign/Kummer cover. That bridge remains unproved. The decision is only about **execution location**: the new receivers can be tested more cleanly inside Stage29 against the already-audited earlier-stage outputs, without changing those earlier certified results.

The audited Stage29-02b joint-V4 result already states `OLD_STAGE_REENTRY_REQUIRED=false` and `KEEP_STAGE29_NATIVE=true`; Stage29-02ha created the sign-tower bridge receivers but did not prove population transfer. R2 then explicitly assigned the population-host work to 29-04, the sign-tower/joint-V4 bridge to 29-07, and parametrization crosswalks to 29-08.

## 2. Priority receiver decisions

### R29-KUM3A

```text
RECEIVER=R29-KUM3A
MEANING=TwoFaceSignSubcoverToStage28ToricYBirationalAdapter
DECISION=STAGE29_INTERNAL_ADAPTER_ONLY
EXECUTION_OWNER=29-07_SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
SOURCE_STAGE=Stage28
OLD_STAGE_ADDENDUM_REQUIRED=false
```

Reason: Stage28 already supplies the audited common toric host `Y=Bl_4(P1xP1)` and the two marginal K3 covers. The missing statement is an exact comparison from the F7 sign-subcover language to that existing host. Proving that comparison does not require reopening Stage28 unless it later exposes an actual error or missing certified statement in Stage28 itself.

### R29-KUM3B

```text
RECEIVER=R29-KUM3B
MEANING=JointV4AsResidualTwoSquareRootsOfFullSignTower
DECISION=STAGE29_INTERNAL_ADAPTER_ONLY
EXECUTION_OWNER=29-07_SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
DEPENDENCY=R29-KUM3A
OLD_STAGE_ADDENDUM_REQUIRED=false
```

Reason: the joint V4 endpoint model is already audited as an exact dense-open/function-field endpoint model over the Stage28 two-face host. What remains is the exact embedding/quotient relationship with F7. This is a Stage29-to-Stage29 bridge.

### R29-KUM4

```text
RECEIVER=R29-KUM4
MEANING=Stage16To20PopulationMaskAsSignSubcoverLattice
DECISION=STAGE29_INTERNAL_ADAPTER_ONLY
PRECONDITION_OWNER=29-04_POPULATION_HOST_PREDICATE_AND_CONDITION_COST_MATRIX
GEOMETRIC_OWNER=29-07_SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
OLD_STAGE_ADDENDUM_REQUIRED=false_NOW
```

Reason: R2 audit explicitly forbids treating exact strata as automatically nested survival steps. Before any sign-tower interpretation, Stage29 must rebuild the counting comparisons using a named common host, exact predicate masks, physical height, primitive normalization, canonical ordering, and multiplicity. That is new synthesis work, not repair of the old population theorems.

Allowed later escalation:

```text
IF_29_04_OR_29_07_FINDS_OLD_CERTIFIED_STATEMENT_NEEDS_CHANGE=true
THEN_TARGETED_ADDENDUM_MAY_BE_CREATED=true
GLOBAL_REOPEN=false
```

### R29-PESCH1

```text
RECEIVER=R29-PESCH1
MEANING=EuclidPairToStage28TwoFaceHostAndJointV4ExactCrosswalk
DECISION=STAGE29_INTERNAL_ADAPTER_ONLY
EXECUTION_OWNER=29-08_PARAMETRIZATION_FIBRATION_AND_COVERAGE_ATLAS
PESCHMANN_PROVEN_F2_ADAPTER=false
PESCHMANN_INDEPENDENCE_RESOLVED=false
OLD_STAGE_ADDENDUM_REQUIRED=false
```

Reason: the 29-02hd audit specifically rejected the earlier informal inference that the matching condition pattern alone proves an F2 adapter. The exact rational map remains open. Until that map is constructed, no Stage16–20 population, height, primitivity, or coverage statement transfers.

## 3. Locked immediate queue

```text
NEXT=29-04_POPULATION_HOST_PREDICATE_AND_CONDITION_COST_MATRIX
THEN=29-05_DEPENDENCY_EQUIVALENCE_ROUTE_OWNERSHIP_AND_DOUBLE_CHARGE_LEDGER
THEN=GAP_SCAN_A_ROADMAP_REVIEW_A
THEN=29-06_GLOBAL_FOUNDATION_SYNTHESIS
THEN=29-07_SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
THEN=29-08_PARAMETRIZATION_FIBRATION_AND_COVERAGE_ATLAS
```

The ordering matters:

1. 29-04 first decides what the population predicates actually mean on common hosts;
2. 29-05 deduplicates mechanisms and assigns canonical route ownership;
3. only then may GAP_SCAN_A decide whether a real targeted backflow has become necessary;
4. 29-07 attempts KUM3A/B and the geometric part of KUM4;
5. 29-08 attempts the exact Peschmann crosswalk.

## 4. Backflow trigger contract

A future Stage16–28 addendum may be created only if all of the following are present:

```text
NEW_EXACT_RECEIVER=true
AFFECTED_OLD_STAGE_NAMED=true
OLD_CERTIFIED_STATEMENT_OR_REQUIRED_ADAPTER_NAMED=true
WHY_STAGE29_INTERNAL_RECORD_IS_INSUFFICIENT=true
REIMPORT_CONTRACT_DEFINED=true
GLOBAL_STAGE_REOPEN=false
```

Merely proving that an old population predicate has a new geometric interpretation is not enough to reopen the old stage. A targeted addendum is justified only if the old stage's certified contract itself must be extended or corrected for downstream use.

## 5. Population/sign-tower firewall retained

```text
FULL_ENDPOINT_IS_DEGREE64_SIGN_KUMMER_COVER=true
STAGE16_20_AS_LITERAL_SIGN_TOWER_LEVELS_PROVED=false
POPULATION_TRANSFER_TO_SIGN_TOWER_AUTOMATIC=false
HEIGHT_TRANSFER_AUTOMATIC=false
PRIMITIVITY_TRANSFER_AUTOMATIC=false
CANONICAL_ORDER_TRANSFER_AUTOMATIC=false
MULTIPLICITY_TRANSFER_AUTOMATIC=false
ASYMPTOTIC_TRANSFER_AUTOMATIC=false
N2_over_M2_is_literal_finite_survival=true
M3_over_M2_is_objectwise_survival=false
M3_over_N2_is_survival_probability=false
```

Thus the intuitive picture "all candidates split by successive square predicates and the perfect endpoint is the all-YES branch" remains a useful logical picture, but Stage29 has not yet proved that the audited Stage16–20 counting strata coincide one-for-one with literal floors of the F7 degree-64 cover.

## 6. No route pruning here

29-03 is not an attack stage and does not rank endpoint routes. Campedelli, Beauville, modular, Brauer, K3, local, and full-surface routes remain live subject to later 29-05 ownership/deduplication and 29-10/11/12 attack portfolios.

```text
PREMATURE_SINGLE_ROUTE_SELECTION=false
MULTI_ROUTE_ATTACK_ALLOWED=true
ROUTE_PRUNING_AT_29_03=false
```

## 7. Submission state

```text
CHECKPOINT29_03_SUBMISSION=READY_FOR_FRESH_AUDIT
AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
PROPOSED_NEXT_ITEM_AFTER_PASS=29-04_POPULATION_HOST_PREDICATE_AND_CONDITION_COST_MATRIX
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
