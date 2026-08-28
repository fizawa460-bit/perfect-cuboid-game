# Stage33-00 — unit closure and downstream-release contract

```text
CONTRACT_SCHEMA=STAGE33_UNIT_CLOSURE_V4_REPAIR_RENUMBERED
BIG_TASKS=Stage33-01,Stage33-02,Stage33-03,Stage33-04,Stage33-05,Stage33-06,Stage33-07,Stage33-08,Stage33-40,Stage33-41,Stage33-42
BIG_TASK_COUNT=11
PROGRESS_DENOMINATOR=11
REPAIR_CHILDREN=Stage33-09,Stage33-10,Stage33-11,Stage33-12
REPAIR_RESERVED_RANGE=Stage33-13..Stage33-39
REPAIR_CHILDREN_COUNT_TOWARD_PROGRESS=false
REPAIR_RESERVED_RANGE_COUNTS_TOWARD_PROGRESS=false
BRAUER_SCOPE=FROZEN_STAGE29_PHYSICAL_OPEN_BRAUER_KERNEL
PARTIAL_COUNTS_AS_COMPLETE=false
BLOCKED_COUNTS_AS_COMPLETE=false
AUDIT_REQUIRED_COUNTS_AS_COMPLETE=false
DOWNSTREAM_MAY_CONSUME_PARTIAL=false
STAGE33_SCOPE_NONEMPTY_IMPLIES_FULL_BM_NONEMPTY_WITHOUT_FULL_COVERAGE_CERT=false
STAGE33_SCOPE_EMPTY_IMPLIES_NO_RATIONAL_ENDPOINT=true
```

## Purpose

Stage33 is a dependency DAG, not a strict linear chain. Independent units may run concurrently, but a downstream unit must never consume a merely partial predecessor as if that predecessor were complete.

The eleven big tasks counted in Stage33 progress are exactly `33-01..33-08,33-40..33-42`. The identifiers `33-09..33-12` are repair children of reopened parent big task Stage33-07, and `33-13..33-39` are reserved repair address space only. Neither the repair children nor the reserved range belong to the eleven-big-task denominator.

The frozen Stage29 Brauer scope carried by this contract includes the `BR0B` open-algebraic absolute-Galois contribution at all primary orders still permitted by Stage29, `BR0G` physical-boundary residue classes, and the `BR2` two-primary geometric/transcendental branch. Stage29 closed proper odd-primary transcendental Brauer, but it explicitly did **not** close possible odd-primary open-algebraic unit/character terms in `BR0B`. Any such survivor must therefore flow through Stage33-07, Stage33-08, Stage33-40, Stage33-41, and Stage33-42.

The progress counter is intentionally strict:

```text
STAGE33_PROGRESS = number of BIG_TASKS with UNIT_STATUS=CLOSED / 11
```

No fractional credit is used. A big task that is 90% complete still contributes zero to the numerator until its closure contract is satisfied and audited. Repair-child progress may be reported separately but never changes this denominator.

## Big-task universal state machine

Every big task (`33-01..08,33-40..42`) must use exactly one of:

```text
OPEN
RUNNING
AUDIT_REQUIRED
CLOSED
BLOCKED_NEW_KERNEL
BLOCKED_RESOURCE
```

Meanings:

```text
OPEN
  authorized scope exists but work has not begun.

RUNNING
  exact work is in progress; no downstream release.

AUDIT_REQUIRED
  the unit claims its own closure conditions are met, but hostile audit has not yet accepted them.
  This does not count as CLOSED and does not release dependent units.

CLOSED
  every unit-specific closure condition is met, no unresolved UNKNOWN remains inside the declared
  unit scope, source locks/artifacts are recorded, and the unit closure passed hostile audit.

BLOCKED_NEW_KERNEL
  the smallest unresolved mathematical dependency has been isolated as a new stable kernel.
  The unit is not CLOSED and dependent downstream units remain locked.

BLOCKED_RESOURCE
  a finite exact computation is specified but the current backend cannot finish it.
  The unit is not CLOSED and dependent downstream units remain locked.
```

Universal big-task release law:

```text
DOWNSTREAM_RELEASED=true  iff  UNIT_STATUS=CLOSED
```

No `PARTIAL`, preview, heuristic, numerical sample, timeout result, or optimistic interpretation may satisfy a prerequisite edge.

## Repair-child state and release semantics

Repair children `33-09..33-12` exist only to close reopened parent big task Stage33-07. They are governed by `stages/stage33/ROADMAP-33-07-REPAIR-BAND.md` and `stages/stage33/controller.json`.

```text
REPAIR_CHILD_COUNTS_AS_BIG_TASK=false
REPAIR_CHILD_CLOSED_IMPLIES_PARENT_33_07_CLOSED=false
REPAIR_CHILD_EXIT_CONDITION_REQUIRED_BEFORE_NEXT_REPAIR_CHILD=true
FAILED_OR_EXHAUSTED_MINIMAP_WITH_OPEN_EXIT_DOES_NOT_ADVANCE=true
SAFE_INDEPENDENT_MINIMAP_BRANCHES_MAY_RUN_CONCURRENTLY=true
FIRST_EXACT_CLOSURE_MAY_SKIP_UNUSED_FALLBACK_BRANCHES=true
```

Stage33-09 must close its marked Picard/equivariant transport exit gate before Stage33-10 is released. Stage33-10 must certify the exact absolute H1 receiver before Stage33-11 is released. Stage33-11 must certify the arithmetic localization connecting map with exact coverage of all 26 source directions before Stage33-12 is released. Stage33-12 must close the arithmetic HS/global-Q repair and hostile-recertify parent Stage33-07. Only that parent hostile recertification may change Stage33-07 to `CLOSED` and move Stage33 progress from 6/11 to 7/11.

Reserved identifiers `33-13..33-39` have no default unit semantics and do not enter either the big-task state machine or progress denominator unless an audited roadmap/controller repair explicitly activates one as a repair child.

## Dependency-release DAG

The eleven-big-task execution DAG is conservatively frozen as:

```text
33-01 -> 33-02
33-01 -> 33-05

33-02 -> 33-03
33-02 -> 33-04

33-03 + 33-04 -> 33-06

33-03 + 33-04 + 33-05 + 33-06 -> 33-07
33-07 -> 33-08
33-08 -> 33-40
33-40 -> 33-41
33-07 + 33-08 + 33-40 + 33-41 -> 33-42
```

The reopened Stage33-07 repair-child sub-DAG is:

```text
33-09 -> 33-10 -> 33-11 -> 33-12 -> hostile recertification of parent 33-07
```

That line describes coarse child release gates, not necessarily serial execution of every mini-map branch. Within an active repair child, safe independent branches may run concurrently under MAIN-batch semantics, and unused fallback branches may be skipped once the child's exact exit condition is satisfied.

Independent big-task branches may run concurrently after all their own prerequisites are CLOSED. In particular, after Stage33-01 closes, Stage33-02 and Stage33-05 may run in parallel.

A later unit may tighten these prerequisites only by an audited roadmap/controller/contract repair. It may not silently weaken them.

## Unit-specific closure gates

### Stage33-01 — BRAUER-PROSPECT-SCAN / source reconstruction

`CLOSED` requires all of:

```text
SOURCE_LOCK_MANIFEST_COMPLETE=true
DEPENDENCY_DAG_RECONSTRUCTED=true
STAGE29_BRAUER_INPUTS_RECONCILED=true
BR0B_ALL_PRIMARY_SCOPE_RECONCILED=true
K3_SURVIVAL_PREVIEW_RECORDED=true
LINE9_ENDPOINT_SURVIVAL_PREVIEW_RECORDED=true
LOCAL_EVALUATION_PREVIEW_RECORDED_OR_EXACTLY_INAPPLICABLE=true
NEXT_PRIORITY_ORDER_RECORDED=true
UNRESOLVED_SOURCE_IDENTITY_AMBIGUITY=0
HOSTILE_AUDIT=PASS
```

This is reconnaissance closure only; it does not discharge BR0A/BR0B/BR0G/BR2A/BR2B unless separately proved.

### Stage33-02 — BR0A integral Picard / saturation

`CLOSED` requires all of:

```text
EXACT_DIVISOR_LATTICE_CERTIFIED=true
INTEGRAL_SATURATION_CERTIFIED=true
INTERSECTION_MAPS_CERTIFIED=true
RESTRICTION_MAPS_REQUIRED_DOWNSTREAM_CERTIFIED=true
REPRODUCIBLE_CAS_MANIFEST=true
BR0A=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

### Stage33-03 — BR0B absolute-Galois UPic / Gersten

`CLOSED` requires all of:

```text
EXPLICIT_GALOIS_ACTION_CERTIFIED=true
UPIC_GERSTEN_MAPS_CERTIFIED=true
KERNELS_COKERNELS_TORSION_EXACT=true
UNIT_KERNEL_ABSOLUTE_GALOIS_INFLATION_CHARACTER_TERMS_EXACT=true
NO_UNJUSTIFIED_TWO_PRIMARY_RESTRICTION=true
QBAR_TO_Q_DESCENT_ADAPTER_CERTIFIED=true
OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE=true
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
BR0B=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

If a smaller new theorem dependency appears, status is `BLOCKED_NEW_KERNEL`, not CLOSED. A proof that no odd-primary open-algebraic class survives is acceptable; silently assuming that conclusion is not.

### Stage33-04 — BR0G physical 72-boundary residue adapter

`CLOSED` requires all of:

```text
PHYSICAL_BOUNDARY_72_INVENTORY_COMPLETE=true
BOUNDARY_STABLE_IDS_COMPLETE=true
RESIDUE_INCIDENCE_MATRIX_EXACT=true
MULTIQUADRATIC_PULLBACK_RESIDUES_EXACT=true
EXCEPTIONAL_DIVISOR_RESIDUES_EXACT=true
PHYSICAL_BOUNDARY_OMISSIONS=0
UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=true
BR0G=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

### Stage33-05 — K3 Br[2] Q(i)/Q action and descent

`CLOSED` requires all of:

```text
K3_GEOMETRIC_BR2_DIM=2
QI_OVER_Q_ACTION_MATRIX_EXACT=true
INVARIANT_DESCENDED_SUBSPACE_EXACT=true
DESCENT_OBSTRUCTION_ACCOUNTED=true
Q_RELEVANT_SURVIVING_DIM_EXACT=true
ALL_SURVIVING_K3_CLASSES_HAVE_EXPLICIT_ARITHMETIC_REPRESENTATIVES=true
  OR EXACT_ZERO_SURVIVAL_CERTIFICATE=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

Zero surviving classes is a valid exact closure of this branch; it is not a reason to skip unfinished independent Stage33 branches.

### Stage33-06 — seven-line endpoint / multiquadratic survival

`CLOSED` requires all of:

```text
LINE9_SOURCE_BASIS_RELATIONS_EXACT=true
ENDPOINT_MULTIQUADRATIC_PULLBACK_EXACT=true
PHYSICAL_BOUNDARY_SURVIVAL_EXACT=true
Q_GALOIS_SURVIVAL_EXACT=true
TRIVIAL_DUPLICATE_SYMBOL_QUOTIENT_EXACT=true
ENDPOINT_RELEVANT_SURVIVING_SUBSPACE_EXACT=true
  OR EXACT_ZERO_SURVIVAL_CERTIFICATE=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

### Stage33-07 — BR2A relation/symbol integration and complete Stage33 class inventory

`CLOSED` requires all of:

```text
BR0B_ALL_PRIMARY_CLASSES_IMPORTED=true
BR0G_RELEVANT_CLASSES_IMPORTED=true
RELATION_MATRIX_EXACT_FOR_TWO_PRIMARY_BRANCH=true
SYMBOL_MATRIX_EXACT_FOR_TWO_PRIMARY_BRANCH=true
THEOREM_HYPOTHESES_SOURCE_LOCKED=true
VARIABLE_DICTIONARY_COMPLETE=true
TRIVIAL_ALGEBRAIC_DUPLICATE_QUOTIENT_EXACT=true
NF_PHYS2_CAMP4_INVOCATIONS_HYPOTHESIS_GATED=true
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=true
EVERY_CLASS_HAS_PRIMARY_ORDER_AND_PROVENANCE=true
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
BR2A=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

Because Stage33-07 has been reopened by Stage33-08 re-audit, its current closure additionally requires successful completion of the repair-child chain defined in `ROADMAP-33-07-REPAIR-BAND.md`, including arithmetic HS/global-Q closure and hostile recertification. Completion of any repair child by itself is insufficient.

The complete class list may be empty. It must include every surviving open-algebraic `BR0B` class even when its primary order is odd; Creutz--Viray/two-primary machinery is not a license to discard those classes.

### Stage33-08 — BR2B explicit endpoint representatives

`CLOSED` requires all of:

```text
EVERY_STAGE33_07_RELEVANT_CLASS_ACCOUNTED=true
EVERY_SURVIVING_CLASS_HAS_PRIMARY_ORDER_AND_PROVENANCE=true
EVERY_SURVIVING_CLASS_HAS_EXACT_EVALUABLE_REPRESENTATIVE=true
RAMIFICATION_SUPPORT_COMPLETE=true
DENOMINATOR_SUPPORT_COMPLETE=true
EQUIVALENCE_INDEPENDENCE_CERTIFICATES_COMPLETE=true
PHYSICAL_OPEN_DOMAIN_CERTIFIED=true
BR2B=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

If the Stage33-07 complete class list is empty, an exact empty-representative inventory satisfies this unit only after audit verifies the inheritance.

### Stage33-40 — relevant places and physical local loci

This is the original Stage33-09 big-task objective, renumbered without changing its mathematical acceptance criteria.

`CLOSED` requires all of:

```text
RELEVANT_PLACE_SET_COMPLETE=true
PLACE_SET_DERIVED_FROM_REPRESENTATIVES_AND_BAD_DATA=true
ODD_PRIMARY_PLACES_FROM_BR0B_SURVIVORS_ACCOUNTED=true
CONSTANCY_OUTSIDE_RELEVANT_PLACE_SET_PROVED_WHEN_USED=true
PHYSICAL_LOCAL_LOCUS_COVERAGE_COMPLETE=true
EVERY_RELEVANT_PLACE_HAS_EXACT_LOCAL_DESCRIPTION_OR_CERTIFICATE=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

### Stage33-41 — exact local evaluations

This is the original Stage33-10 big-task objective, renumbered without changing its mathematical acceptance criteria.

`CLOSED` requires all of:

```text
EVERY_RELEVANT_CLASS_PLACE_PAIR_ACCOUNTED=true
ALL_PRIMARY_ORDERS_IN_STAGE33_CLASS_LIST_EVALUATED=true
LOCAL_EVALUATION_IMAGES_EXACT=true
PHYSICAL_LOCAL_COMPONENT_OR_CELL_COVERAGE_COMPLETE=true
CONSTANCY_NONCONSTANCY_CERTIFICATES_COMPLETE=true
NUMERICAL_SAMPLING_USED_AS_PROOF=false
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

### Stage33-42 — adelic compatibility / final Brauer verdict

This is the original Stage33-11 big-task objective, renumbered without changing its mathematical acceptance criteria.

`CLOSED` requires all prerequisite units CLOSED and all of:

```text
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=true
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
RELEVANT_PLACE_SET_COMPLETE=true
PHYSICAL_LOCAL_LOCUS_COVERAGE_COMPLETE=true
LOCAL_EVALUATION_IMAGES_EXACT=true
RECIPROCITY_ASSEMBLY_EXACT=true
FINAL_BRAUER_DISPOSITION_EXACTLY_ONE_OF=
  PHYSICAL_STAGE33_BRAUER_SCOPE_SET_EMPTY_CERTIFIED |
  PHYSICAL_STAGE33_BRAUER_SCOPE_SET_NONEMPTY_CERTIFIED |
  RELEVANT_STAGE33_BRAUER_SCOPE_TRIVIAL_OR_EVALUATIONS_VACUOUS_CERTIFIED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
FINAL_HOSTILE_AUDIT=PASS
```

Scope semantics are asymmetric and mandatory. Emptiness of the physical adelic set orthogonal to the complete Stage33 class inventory is enough to exclude rational endpoint points. Nonemptiness for the Stage33 scope closes this frozen mechanism negatively but does **not** certify nonemptiness of the full Brauer--Manin set unless `FULL_RELEVANT_BRAUER_GROUP_COVERAGE_CERTIFIED=true` has itself been independently proved and audited.

`NEW_KERNEL_EXPOSED` is not a CLOSED final disposition; it leaves Stage33 progress below 11/11 and freezes the exact residual instead.

## Repair-child exit gates

These are not big-task closure gates and do not contribute to `STAGE33_PROGRESS`.

### Stage33-09 — PICARD-EQUIVARIANT-TRANSPORT repair child

Exit requires the source-locked historical retained Picard marking bridge and exact transport of the already-established named actions, as defined in `ROADMAP-33-07-REPAIR-BAND.md`.

### Stage33-10 — ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER repair child

Exit requires an exact absolute H1 receiver with all relevant kernel-Galois contribution accounted for and Stage33-11 domain/codomain well-defined. Mini-map branches may run concurrently when independent; not every fallback branch must execute.

### Stage33-11 — ARITHMETIC-LOCALIZATION-CONNECTING-MAP repair child

Exit requires `ARITHMETIC_LOCALIZATION_CONNECTING_MAP_COMPUTED=true` and exact coverage of all 26 source directions. Global, orbit/block, and individual fallback routes may run concurrently when safe; the prescribed result is 26/26 coverage, not a prescribed method.

### Stage33-12 — ARITHMETIC-HS-CLOSURE-AND-33-07-RECERTIFICATION repair child

Exit requires arithmetic HS d2, global-Q residue-lift completion, complete relevant Q-defined class inventory for the frozen Stage33 Brauer scope, and hostile recertification of parent Stage33-07. Failure to satisfy that exit gate does not release Stage33-08.

## Machine handoff requirement

Every big-task handoff must contain:

```text
STAGE33_UNIT=
UNIT_STATUS=OPEN|RUNNING|AUDIT_REQUIRED|CLOSED|BLOCKED_NEW_KERNEL|BLOCKED_RESOURCE
UNIT_CLOSED=true|false
DOWNSTREAM_RELEASED=true|false
PREREQUISITE_UNITS=[]
PREREQUISITES_ALL_CLOSED=true|false
CLOSURE_CRITERIA_TOTAL=
CLOSURE_CRITERIA_SATISFIED=
UNRESOLVED_UNKNOWN_IN_SCOPE=
RECEIVERS_DISCHARGED=[]
RECEIVERS_OPEN=[]
NEW_KERNEL_ID=NONE|<stable-id>
THEOREM_CREDIT=true|false
ENDPOINT_CREDIT=true|false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=true|false
SOURCE_LOCKS=[]
ARTIFACT_HASHES=[]
AUDIT_VERDICT=
NEXT_RELEASED_UNITS=[]
```

Invariant checker for big tasks:

```text
if UNIT_STATUS != CLOSED:
    UNIT_CLOSED=false
    DOWNSTREAM_RELEASED=false

if UNIT_STATUS == CLOSED:
    assert UNRESOLVED_UNKNOWN_IN_SCOPE == 0
    assert AUDIT_VERDICT == PASS
    UNIT_CLOSED=true
    DOWNSTREAM_RELEASED=true
```

Repair-child handoffs must instead report their child exit condition, unresolved exact subkernel, and any active/closed mini-map branches; they must not claim `UNIT_STATUS=CLOSED` credit in the eleven-big-task denominator merely because a child exit gate is satisfied.

## Progress reporting

Human-readable Stage33 progress must always use only audited CLOSED big tasks:

```text
STAGE33_PROGRESS=<CLOSED_BIG_TASK_COUNT>/11
BIG_TASK_IDS=33-01,33-02,33-03,33-04,33-05,33-06,33-07,33-08,33-40,33-41,33-42
REPAIR_CHILD_IDS=33-09,33-10,33-11,33-12
```

Examples:

```text
33-02 CLOSED, 33-03 RUNNING, 33-05 CLOSED  -> 2/11
33-06 AUDIT_REQUIRED                       -> still not counted
33-07 BLOCKED_NEW_KERNEL                   -> not counted
33-09 repair child exit PASS               -> does not change /11 progress
```

This contract deliberately prefers undercounting to accidental downstream theorem credit.
