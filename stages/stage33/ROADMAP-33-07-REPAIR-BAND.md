# Stage33 — 33-07 repair-band roadmap amendment

```text
AMENDMENT_ROLE=PLANNING_ONLY
PARENT_ROADMAP=stages/stage33/ROADMAP.md
TRIGGER=STAGE33_08_REAUDIT_REOPENED_STAGE33_07
BIG_TASK_COUNT_REMAINS=11
REPAIR_CHILD_STAGES_COUNT_TOWARD_11=false
ORIGINAL_STAGE33_09_10_11_RENUMBERED_TO=33-40,33-41,33-42
```

This file defines repair numbering, child objectives, and exit interfaces. It does **not** own current progress, current child, current leaf, live counters, or live route status.

Use:

```text
current human state      -> stages/stage33/CURRENT.md
current machine state    -> stages/stage33/controller.json
stable Stage33 rules     -> stages/stage33/RULES.md
history/evidence index   -> stages/stage33/HISTORY.md
unit closure contract    -> stages/stage33/33-00/unit-closure-contract.md
active J2 repair plan    -> stages/stage33/ROADMAP-33-05-J2-REPRESENTATIVE-REPAIR.md
active J2 math state     -> stages/stage33/33-05/j2-representative-repair-state.json
```

## Numbering

The original downstream big-task objectives were renumbered to preserve repair address space:

```text
OLD 33-09 -> NEW 33-40  complete relevant-place and physical-local-locus certification
OLD 33-10 -> NEW 33-41  exact local evaluation production
OLD 33-11 -> NEW 33-42  physical adelic compatibility, final Brauer verdict, hostile audit
```

Repair address space is `33-09..33-39`. Repair children do not independently increment the eleven-big-task Stage33 denominator.

Do not manufacture stages merely to consume numbers. Split only when a genuinely independent exact subkernel needs its own child.

## Repair sequence

The repair architecture is:

```text
33-09  PICARD-EQUIVARIANT-TRANSPORT
33-10  ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER
33-11  ARITHMETIC-LOCALIZATION-CONNECTING-MAP
33-12  CORRECTED-J2-MARKED-KC-ARITHMETIC-CLOSURE
33-13  FINITE-V4-KUMMER-MATRIX
33-14  FINITE-HS-COSETS-AND-TWO-PRIMARY-CONSTANT-BLOCK
33-15  GLOBAL-ARITHMETIC-HS-ASSEMBLY-AND-33-07-HOSTILE-RECERTIFICATION
```

Whether a child is currently closed, blocked, released, or active is read from CURRENT/controller, not this roadmap.

## 33-09 — PICARD-EQUIVARIANT-TRANSPORT

Exit interface requires the retained Picard marking bridge and exact transport of the named integral/two-torsion actions needed downstream.

The closed historical evidence, when applicable, remains in the 33-09 result/audit/certificates and is indexed by HISTORY.

## 33-10 — ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER

Exit interface requires an exact absolute H1 receiver, all relevant kernel-Galois contribution accounted for, and a well-defined domain/codomain for the connecting-map child.

## 33-11 — ARITHMETIC-LOCALIZATION-CONNECTING-MAP

Exit interface requires the arithmetic localization connecting map with exact coverage of all 26 source directions and no unresolved connecting direction.

The roadmap prescribes the receiver/coverage, not a mandatory serial mini-map method.

## 33-12 — CORRECTED-J2-MARKED-KC-ARITHMETIC-CLOSURE

Purpose: consume the corrected named-J2 evidence and package it into the exact Stage33-12 child closure. Stage33-12 does not run a second independent derivation of the Stage33-05 J2 problem.

### Retired old checklist

The old corrected-J2-independent checklist based on

```text
infinity exceptional attachment
ptsK order/index
qPicK exceptional coordinate
old branch-Jacobian Kummer glue
```

belongs to the superseded representative route. It is historical evidence, not a mandatory checklist for the corrected finite-smooth-support route.

Do not recompute it merely to satisfy an obsolete roadmap generation.

### 33-12 exit interface

Exact Stage33-12 closure requires corrected evidence sufficient to certify:

```text
CORRECTED_J2_GEOMETRIC_REPRESENTATIVE_NONZERO=true
CORRECTED_J2_MARKED_BRAUER_COORDINATE=[1,0]
CORRECTED_J2_SURFACE_MU2_LIFT_EXACT=true
CORRECTED_J2_ACTUAL_PIC_MOD2_DEFECT_EXACT=true
CORRECTED_J2_HS_D2_CLASS_ZERO=true
CORRECTED_J2_Q_DEFINED_BRAUER_PREIMAGE=true
CORRECTED_J2_ARITHMETIC_UNRAMIFIEDNESS=true
CORRECTED_J2_RESTRICTION_BACK_TO_F2_1=true
STAGE33_05_R5_FULL_REPAIR_EXIT=true
required hostile/super-hostile audit = PASS
STAGE33_12_CLOSED_EXACT=true
```

The current production of those J2 arithmetic facts belongs to the Stage33-05 R5 repair state/roadmap. Stage33-12 consumes and audits/packages them after the required release gate.

If the exact HS `d2` class is nonzero, do not close Stage33-12; record the exact no-go and rebuild affected dependencies.

## 33-13 — FINITE-V4-KUMMER-MATRIX

Purpose: materialize the finite-V4 Kummer restriction on the full-surface proper Br[2] receiver after 33-12 exact release.

Planned interface:

```text
P=Br(Sbar)[2]^{G_Q}
DIM_F2(P)=10
DIM_F2(H^1(V4,Pic(Sbar)/2))=75
KUMMER_MATRIX_SHAPE=75x10
```

Exit requires all 10 exact columns, an exact 75x10 matrix, and no unresolved Kummer column. Guessed zero columns are forbidden.

## 33-14 — FINITE-HS-COSETS-AND-TWO-PRIMARY-CONSTANT-BLOCK

Purpose: consume the exact finite Kummer matrix and discharge the remaining finite HS obstruction cosets and two-primary constant block.

Exit requires:

```text
FINITE_HS_OBSTRUCTION_COSETS_ACCOUNTED=26/26
GLOBAL_Q_BR0G_TWO_PRIMARY_RESIDUE_LIFTS_COMPLETE=true
REMAINING_TWO_PRIMARY_CONSTANT_BLOCK_CLOSED_EXACT=true
NO_REMAINING_ARITHMETIC_HS_OBSTRUCTION_BLOCK=true
STAGE33_14_CLOSED_EXACT=true
```

The constant block is independent bookkeeping and is not inferred closed from unrelated cancellation.

## 33-15 — GLOBAL-ARITHMETIC-HS-ASSEMBLY-AND-33-07-HOSTILE-RECERTIFICATION

Purpose: assemble the closed repair interfaces, complete the relevant Q-defined class inventory, and hostile-recertify parent Stage33-07.

Exit requires:

```text
ARITHMETIC_HS_D2_COMPUTED=true
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=true
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=true
STAGE33_07_HOSTILE_REAUDIT=PASS
```

Only the audited parent closure changes the Stage33 big-task numerator and releases the downstream parent dependency.

## Evidence/context policy

Compact evidence, bounded startup context, Actions/storage safety, loop handling, and claim-promotion rules are Stage33/Research-OS policy rather than roadmap progress. Use `RULES.md`, `AGENTS.md`, and the Research OS policies.

Per-child result/audit/certificate files and Git history remain the historical evidence. `HISTORY.md` is the navigation index.

## Downstream big tasks

```text
Stage33-40 = original Stage33-09 objective
Stage33-41 = original Stage33-10 objective
Stage33-42 = original Stage33-11 objective
```

Their current release state belongs in controller/CURRENT.
