# Stage33-00 — unit closure and downstream-release contract

```text
CONTRACT_SCHEMA=STAGE33_UNIT_CLOSURE_V1
APPLIES_TO=Stage33-01..Stage33-11
BIG_TASK_COUNT=11
PROGRESS_DENOMINATOR=11
PARTIAL_COUNTS_AS_COMPLETE=false
BLOCKED_COUNTS_AS_COMPLETE=false
AUDIT_REQUIRED_COUNTS_AS_COMPLETE=false
DOWNSTREAM_MAY_CONSUME_PARTIAL=false
```

## Purpose

Stage33 is a dependency DAG, not a strict linear chain. Independent units may run concurrently, but a downstream unit must never consume a merely partial predecessor as if that predecessor were complete.

The progress counter is intentionally strict:

```text
STAGE33_PROGRESS = number of units with UNIT_STATUS=CLOSED / 11
```

No fractional credit is used. A unit that is 90% complete still contributes zero to the numerator until its closure contract is satisfied and audited.

## Universal unit state machine

Every big unit must use exactly one of:

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

Universal release law:

```text
DOWNSTREAM_RELEASED=true  iff  UNIT_STATUS=CLOSED
```

No `PARTIAL`, preview, heuristic, numerical sample, timeout result, or optimistic interpretation may satisfy a prerequisite edge.

## Dependency-release DAG

The execution DAG is conservatively frozen as:

```text
33-01 -> 33-02
33-01 -> 33-05

33-02 -> 33-03
33-02 -> 33-04

33-03 + 33-04 -> 33-06

33-03 + 33-04 + 33-05 + 33-06 -> 33-07
33-07 -> 33-08
33-08 -> 33-09
33-09 -> 33-10
33-07 + 33-08 + 33-09 + 33-10 -> 33-11
```

Independent branches may run concurrently after all their own prerequisites are CLOSED. In particular, after Stage33-01 closes, Stage33-02 and Stage33-05 may run in parallel.

A later unit may tighten these prerequisites only by an audited roadmap/controller repair. It may not silently weaken them.

## Unit-specific closure gates

### Stage33-01 — BRAUER-PROSPECT-SCAN / source reconstruction

`CLOSED` requires all of:

```text
SOURCE_LOCK_MANIFEST_COMPLETE=true
DEPENDENCY_DAG_RECONSTRUCTED=true
STAGE29_BRAUER_INPUTS_RECONCILED=true
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
QBAR_TO_Q_DESCENT_ADAPTER_CERTIFIED=true
BR0B=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

If a smaller new theorem dependency appears, status is `BLOCKED_NEW_KERNEL`, not CLOSED.

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

### Stage33-07 — BR2A Creutz--Viray relation/symbol integration

`CLOSED` requires all of:

```text
RELATION_MATRIX_EXACT=true
SYMBOL_MATRIX_EXACT=true
THEOREM_HYPOTHESES_SOURCE_LOCKED=true
VARIABLE_DICTIONARY_COMPLETE=true
TRIVIAL_ALGEBRAIC_DUPLICATE_QUOTIENT_EXACT=true
NF_PHYS2_CAMP4_INVOCATIONS_HYPOTHESIS_GATED=true
Q_DEFINED_RELEVANT_TWO_PRIMARY_CLASS_LIST_COMPLETE=true
BR2A=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

The complete class list may be empty.

### Stage33-08 — BR2B explicit endpoint representatives

`CLOSED` requires all of:

```text
EVERY_STAGE33_07_RELEVANT_CLASS_ACCOUNTED=true
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

### Stage33-09 — relevant places and physical local loci

`CLOSED` requires all of:

```text
RELEVANT_PLACE_SET_COMPLETE=true
PLACE_SET_DERIVED_FROM_REPRESENTATIVES_AND_BAD_DATA=true
CONSTANCY_OUTSIDE_RELEVANT_PLACE_SET_PROVED_WHEN_USED=true
PHYSICAL_LOCAL_LOCUS_COVERAGE_COMPLETE=true
EVERY_RELEVANT_PLACE_HAS_EXACT_LOCAL_DESCRIPTION_OR_CERTIFICATE=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

### Stage33-10 — exact local evaluations

`CLOSED` requires all of:

```text
EVERY_RELEVANT_CLASS_PLACE_PAIR_ACCOUNTED=true
LOCAL_EVALUATION_IMAGES_EXACT=true
PHYSICAL_LOCAL_COMPONENT_OR_CELL_COVERAGE_COMPLETE=true
CONSTANCY_NONCONSTANCY_CERTIFICATES_COMPLETE=true
NUMERICAL_SAMPLING_USED_AS_PROOF=false
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```

### Stage33-11 — adelic compatibility / final Brauer verdict

`CLOSED` requires all prerequisite units CLOSED and all of:

```text
RELEVANT_Q_DEFINED_CLASS_LIST_COMPLETE=true
RELEVANT_PLACE_SET_COMPLETE=true
PHYSICAL_LOCAL_LOCUS_COVERAGE_COMPLETE=true
LOCAL_EVALUATION_IMAGES_EXACT=true
RECIPROCITY_ASSEMBLY_EXACT=true
FINAL_BRAUER_DISPOSITION_EXACTLY_ONE_OF=
  PHYSICAL_BM_SET_EMPTY_CERTIFIED |
  PHYSICAL_BM_SET_NONEMPTY_CERTIFIED |
  RELEVANT_BRAUER_GROUP_TRIVIAL_OR_EVALUATIONS_VACUOUS_CERTIFIED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
FINAL_HOSTILE_AUDIT=PASS
```

`NEW_KERNEL_EXPOSED` is not a CLOSED final disposition; it leaves Stage33 progress below 11/11 and freezes the exact residual instead.

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

Invariant checker:

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

## Progress reporting

Human-readable progress must always use only audited CLOSED units:

```text
STAGE33_PROGRESS=<CLOSED_COUNT>/11
```

Examples:

```text
33-02 CLOSED, 33-03 RUNNING, 33-05 CLOSED  -> 2/11
33-06 AUDIT_REQUIRED                       -> still not counted
33-07 BLOCKED_NEW_KERNEL                   -> not counted
```

This contract deliberately prefers undercounting to accidental downstream theorem credit.
