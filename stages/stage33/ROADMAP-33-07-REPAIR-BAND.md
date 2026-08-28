# Stage33 — 33-07 repair-band roadmap amendment

```text
AMENDMENT_STATUS=AUTHORITATIVE_FOR_POST_33_08_NUMBERING
PARENT_ROADMAP=stages/stage33/ROADMAP.md
TRIGGER=STAGE33_08_REAUDIT_REOPENED_STAGE33_07
BIG_TASK_COUNT_REMAINS=11
REPAIR_CHILD_STAGES_COUNT_TOWARD_11=false
ORIGINAL_STAGE33_09_10_11_RENUMBERED_TO=33-40,33-41,33-42
PERFECT_CUBOID_PROBLEM_STATUS=OPEN
```

## 1. Why this amendment exists

Stage33-08 did not merely find a small typo in Stage33-07. It exposed a deep arithmetic Hochschild--Serre / global Gersten descent repair whose implementation has expanded into integral Picard marking, coordinate-swap recovery, intrinsic-to-retained two-torsion transport, named V4 action identification, finite/absolute H1 separation, naturality constraints and the still-unmaterialized arithmetic localization connecting map.

Continuing to add all of that under `33-07` creates two operational problems:

1. the semantic unit becomes too large to audit as one repair;
2. path-triggered `stage33-07-*` workflows repeatedly re-fire unrelated historical leaves.

Therefore Stage33-07 remains the blocked parent big task, while its repair is executed through a dedicated child-stage number band beginning at 33-09.

## 2. Numbering policy

The original big-task meanings of Stage33-09, Stage33-10 and Stage33-11 are preserved but moved far enough away that the repair chain can grow without another renumbering event:

```text
OLD 33-09 -> NEW 33-40  complete relevant-place and physical-local-locus certification
OLD 33-10 -> NEW 33-41  exact local evaluation production
OLD 33-11 -> NEW 33-42  physical adelic compatibility, final Brauer verdict, hostile audit
```

Stage33-09 through Stage33-39 are reserved for bounded repair children of the reopened Stage33-07 arithmetic-HS kernel. These child stages do not increase the denominator of Stage33 progress. Stage33 remains an 11-big-task roadmap:

```text
big task 1..8 = 33-01..33-08
big task 9    = 33-40
big task 10   = 33-41
big task 11   = 33-42
```

A repair child may close without changing `stage33_progress`. Only hostile-audited closure of the parent Stage33-07 changes progress from 6/11 to 7/11.

## 3. 33-07 repair child roadmap

The repair children are sequential by mathematical dependency but may use small independent workflows when the inputs are frozen. Each child gets a narrow path namespace and should prefer one workflow with job partitioning over a family of near-duplicate workflows.

### Stage33-09 — RETAINED-PICARD-MARKING-BRIDGE

Objective: freeze the exact bridge from the retained Stage32 integral Picard marking into the Stage33 proper-geometric Picard basis used by the arithmetic-HS repair.

Required closure data:

```text
RETAINED_STAGE32_MARKING_SOURCE_LOCKED=true
PICARD_RANK_AND_SMITH_DATA_MATCH=true
MARKING_TO_STAGE33_BASIS_INTEGRAL=true
BASIS_BRIDGE_CERTIFICATE_MATERIALIZED=true
```

This stage absorbs the current marking-recovery work and forbids assigning arithmetic-HS credit merely from a rational linear identification.

### Stage33-10 — ACTUAL-INTEGRAL-COORDINATE-SWAP-ACTIONS

Objective: compute the actual integral Picard actions of the coordinate swaps required by the arithmetic Galois model, using the frozen marking rather than a linear-envelope surrogate.

Required closure data:

```text
ACTUAL_SWAP12_INTEGRAL_ACTION_MATERIALIZED=true
ACTUAL_SWAP13_INTEGRAL_ACTION_MATERIALIZED=true
INTERSECTION_AND_LATTICE_COMPATIBILITY_CERTIFIED=true
LINEAR_ENVELOPE_ONLY=false
```

A large intertwiner space is diagnostic only and does not close this stage.

### Stage33-11 — INTRINSIC-TO-RETAINED-AT2-TRANSPORT

Objective: identify the intrinsic proper-geometric two-torsion module with the retained `A_T[2]` coordinates and transport the actual integral swap actions through that identification.

Required closure data:

```text
INTRINSIC_AT2_PRESENTATION_FROZEN=true
RETAINED_AT2_PRESENTATION_FROZEN=true
INTRINSIC_TO_RETAINED_TRANSPORT_EXACT=true
TRANSPORTED_SWAP_ACTIONS_EXACT=true
```

Filtration or divisibility signatures may be used to prove uniqueness but do not by themselves authorize a guessed basis identification.

### Stage33-12 — NAMED-V4-PROPER-BR2-ACTION

Objective: identify the transported coordinate-swap actions with the named arithmetic generators (`cc`, `ct`) and materialize the resulting action on the proper geometric `Br[2]` kernel.

Required closure data:

```text
NAMED_CC_ACTION_MATERIALIZED=true
NAMED_CT_ACTION_MATERIALIZED=true
V4_RELATIONS_CERTIFIED=true
PROPER_GEOMETRIC_BR2_ACTION_MATERIALIZED=true
```

The existing finite candidate/naturality envelopes remain constraints only until the actual named action is fixed.

### Stage33-13 — FINITE-TO-ABSOLUTE-H1-ADAPTER

Objective: repair the gap between finite `H^1(V4, Br(Sbar)[2])` and the absolute `H^1(G_Q, Br(Sbar)[2])` term required by arithmetic Hochschild--Serre descent.

Required closure data:

```text
INFLATION_RESTRICTION_ADAPTER_MATERIALIZED=true
KERNEL_GALOIS_ACTION_ACCOUNTED=true
ABSOLUTE_H1_RECEIVER_IDENTIFIED=true
FINITE_H1_EQUALS_ABSOLUTE_H1_CLAIM_JUSTIFIED_OR_REJECTED=true
```

No finite-V4 dimension count alone may be promoted to an absolute-Galois conclusion.

### Stage33-14 — ARITHMETIC-LOCALIZATION-CONNECTING-MAP

Objective: materialize the genuine arithmetic localization connecting map / middle Gersten extension class for the 26 mixed-order boundary source directions.

Required closure data:

```text
SOURCE_DIRECTIONS=26
CONNECTING_MATRIX_COLUMNS_MATERIALIZED=26/26
MIDDLE_GERSTEN_MODULE_ACTION_MATERIALIZED=true
NATURALITY_CERTIFIED_FOR_NAMED_CC_CT=true
PROJECT_14x26_L_SQUARECLASS_TENSOR_COMPUTED=true|PROVED_UNNECESSARY_BY_EXACT_ADAPTER
```

This is the first child that may directly close the currently named `R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT` kernel.

### Stage33-15 — ARITHMETIC-HS-DESCENT-CLOSURE-AND-33-07-RECERTIFICATION

Objective: compute the remaining Hochschild--Serre obstruction data, reassemble the complete relevant Q-defined class inventory, and hostile-audit the repaired Stage33-07 parent.

Required closure data:

```text
ARITHMETIC_LOCALIZATION_CONNECTING_MAP_COMPUTED=true
ARITHMETIC_HS_D2_COMPUTED=true
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=true
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=true
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
STAGE33_07_HOSTILE_REAUDIT=PASS
```

Only after this child passes may the parent be changed to:

```text
Stage33-07 UNIT_STATUS=CLOSED
Stage33 progress=7/11
Stage33-08 release allowed=true
```

## 4. Reserved repair expansion band

```text
33-16..33-39=RESERVED_FOR_33_07_REPAIR_CHILDREN_IF_NEW_EXACT_SUBKERNELS_APPEAR
```

Use the next free child number only when an already-defined repair child exposes a genuinely new exact subkernel. Do not renumber the original downstream big tasks again.

## 5. Workflow policy for the repair band

New repair work should use stage-local paths such as:

```text
stages/stage33/33-09/**
stages/stage33/33-10/**
...
```

and normally one workflow per repair child:

```text
.github/workflows/stage33-09-main.yml
.github/workflows/stage33-10-main.yml
...
```

Prefer job matrices/job splitting inside that workflow. Heavy or unreliable remote Magma probes should be separate `workflow_dispatch` diagnostics and should not synchronize on every pull-request file change.

The existing historical `stage33-07-*` workflows are retained as evidence but are not the namespace for new repair growth.

## 6. Downstream big tasks after repair

### Stage33-40 — complete relevant-place and physical-local-locus certification

This is exactly the original Stage33-09 objective and acceptance contract from `ROADMAP.md`; only the unit number changes.

Prerequisite:

```text
Stage33-08=CLOSED
```

### Stage33-41 — exact local evaluation production

This is exactly the original Stage33-10 objective and acceptance contract from `ROADMAP.md`; only the unit number changes.

Prerequisite:

```text
Stage33-40=CLOSED
```

### Stage33-42 — physical adelic compatibility, final Brauer verdict, and hostile audit

This is exactly the original Stage33-11 objective and acceptance contract from `ROADMAP.md`; only the unit number changes.

Prerequisites:

```text
Stage33-07=CLOSED
Stage33-08=CLOSED
Stage33-40=CLOSED
Stage33-41=CLOSED
```

## 7. Anti-overclaim and migration firewall

```text
REPAIR_CHILD_CLOSED_IMPLIES_PARENT_33_07_CLOSED=false
REPAIR_CHILD_COUNT_CHANGES_BIG_TASK_COUNT=false
RENUMBERING_GRANTS_THEOREM_CREDIT=false
RENUMBERING_GRANTS_ENDPOINT_CREDIT=false
OLD_33_09_10_11_SEMANTICS_DROPPED=false
OLD_33_09_10_11_SEMANTICS_MOVED_TO_33_40_41_42=true
STAGE33_08_CAN_RELEASE_BEFORE_33_07_CLOSES=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
