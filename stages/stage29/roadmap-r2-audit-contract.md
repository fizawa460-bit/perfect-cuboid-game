# Stage29 roadmap R2 — audited contract

```text
AUDITED_PR=1307
AUDITED_SUBMISSION_HEAD=e06fbda9e3df1bab240f4f958ef7e8e144770af1
AUDIT_MODE=ADVERSARIAL_ROADMAP_DESIGN
AUDIT_VERDICT=PASS_AFTER_MATERIAL_REPAIR
```

## Why R2 survives

The original roadmap assumed that later Stage29 items still needed to discover the global endpoint and joint-cover models and would then choose one of three entrances. Audited 29-02 work made that architecture stale. The replacement multi-route roadmap is correct in direction, but the submission required several material repairs before it was safe to ratify.

## Material repairs found by audit

### R2-A — F7 was drawn too much like a universal quotient hierarchy

The submitted 29-06 chain could be read as

```text
F7 -> K3 -> Campedelli -> Beauville -> ...
```

which is false as a global organizing chain. In particular the audited Beauville morphism is a degree-two cover

```text
X_cub -> S_endpoint,
```

not a quotient `S_endpoint -> X_cub` produced by the F7 sign lattice.

Repair: 29-06 now requires an **endpoint-hub directed graph** with every arrow carrying direction, type, degree, field, and rational-point semantics. F7 organizes its certified sign quotients but is not assumed to organize Beauville, modular, F2, or cohomological routes.

```text
F7_UNIVERSAL_ORGANIZER_ASSUMED=false
ENDPOINT_HUB_GRAPH_REQUIRED=true
```

### R2-B — exact counting strata were too close to being described as nested survival steps

The submission used `population transition` language too broadly. Exact face-count strata are not automatically nested. The audited numerical ledger already certifies that `N2/M2` is literal finite survival while `M3/M2` is not objectwise survival.

Repair: 29-04 is now a **host + predicate + mask** ledger. Every comparison must state whether nested conditioning is valid. Disjoint exact strata must be represented inside a named common host before ratios receive probabilistic language.

```text
EXACT_STRATUM_IS_NOT_AUTOMATIC_NESTED_TRANSITION=true
N2_over_M2_is_literal_finite_survival=true
M3_over_M2_is_objectwise_survival=false
M3_over_N2_is_survival_probability=false
```

### R2-C — living-roadmap policy needed a hard anti-loop rule

Repair:

```text
ROADMAP_REVIEW_DOES_NOT_IMPLY_REWRITE=true
ROADMAP_REWRITE_REQUIRES_MATERIALITY_CERTIFICATE=true
COMPLETED_AUDITED_ITEMS_IMMUTABLE=true
REOPEN_COMPLETED_ITEM_ONLY_VIA_TARGETED_ADDENDUM=true
REWRITE_APPLIES_TO_UNEXECUTED_FUTURE_ITEMS_BY_DEFAULT=true
```

A materiality certificate must identify exact new mathematics and affected future items. Cosmetic changes and receiver churn do not reopen the roadmap.

### R2-D — portfolio parallelism could double-count the same mechanism

Repair: 29-05 now assigns every live receiver one canonical `ROUTE_ID` and one primary portfolio owner. Cross-reference is allowed; duplicate progress accounting is not. Exact RED/MERGED routes are retired immediately rather than waiting for 29-16.

```text
EARLY_EXACT_DEDUP_REQUIRED=true
FINAL_PORTFOLIO_COMPRESSION_AT_29_16=true
```

29-09 is local-arithmetic infrastructure; 29-12 attacks with the resulting receivers. 29-08 builds the parametrization/coverage atlas; 29-12 uses only routes that survive exact adaptation. 29-10 may identify natural slices; systematic closure/coverage is 29-14.

### R2-E — Campedelli Q arithmetic wording was too compressed

The `6+2+2` result is the orbit decomposition under the certified Q-defined `S3` action, not a theorem that there are exactly three Q-isomorphism classes.

```text
GEOMETRIC_Qi_KERNEL_ORBITS=8+2
CERTIFIED_Q_DEFINED_S3_ACTION_ORBITS=6+2+2
EXACT_Q_ISOMORPHISM_CLASS_COUNT_PROVED=false
```

### R2-F — 29-03 and GAP_SCAN_A were positioned as redundant roadmap reviews

PR #1307 itself is the roadmap ratification audit. Therefore 29-03 is now `FOUNDATION_BACKFLOW_DECISION_AND_BRIDGE_QUEUE_LOCK`, not another roadmap-ratification stage. `GAP_SCAN_A` is moved after 29-04/05, where new exact population/dependency information can actually justify a review.

### R2-G — controller state needed synchronization with merged #1306

The submitted controller delta did not explicitly repair the stale `child_02hd=PENDING_MERGE` state left in the canonical controller after #1306 merged. The audited delta and controller must record #1306 as merged with merge commit `8e6e3ba77b4ef49af9fa3bbb910a9487ce2b9b14` while preserving all prior audit metadata.

## Audited sequence

```text
29-01 GLOBAL_CERTIFIED_MAP_LOCK
29-02 NEW_FOUNDATION_SCREENING
29-03 FOUNDATION_BACKFLOW_DECISION_AND_BRIDGE_QUEUE_LOCK
29-04 POPULATION_HOST_PREDICATE_AND_CONDITION_COST_MATRIX
29-05 DEPENDENCY_EQUIVALENCE_ROUTE_OWNERSHIP_AND_DOUBLE_CHARGE_LEDGER
GAP_SCAN_A / ROADMAP_REVIEW_A
29-06 GLOBAL_FOUNDATION_SYNTHESIS
29-07 SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
29-08 PARAMETRIZATION_FIBRATION_AND_COVERAGE_ATLAS
29-09 FULL_ENDPOINT_LOCAL_ARITHMETIC
GAP_SCAN_B / ROADMAP_REVIEW_B
29-10 GLOBAL_AND_K3_ATTACK_PORTFOLIO
29-11 QUOTIENT_DESCENT_AND_MODULAR_ATTACK_PORTFOLIO
29-12 JOINT_LOCAL_PARAMETRIC_AND_INTERACTION_ATTACK_PORTFOLIO
GAP_SCAN_C / ROADMAP_REVIEW_C
29-13 A2_METHOD_TRANSFER_ACROSS_SURVIVING_ROUTES
29-14 NATURAL_SLICE_QUOTIENT_AND_COVERAGE_TEST
29-15 ENDPOINT_ARSENAL_REMATCH
29-16 RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO
GAP_SCAN_FINAL / ROADMAP_REVIEW_FINAL
29-17 PERFECT_CUBOID_ATTACK_HANDOFF
29-close
```

## Final state

```text
ROADMAP_R2_SUBMISSION=false
ROADMAP_R2_AUDIT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-03_FOUNDATION_BACKFLOW_DECISION_AND_BRIDGE_QUEUE_LOCK
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```