# Stage33 — 33-07 repair-band roadmap amendment

```text
AMENDMENT_ROLE=PLANNING_ONLY
PARENT_ROADMAP=stages/stage33/ROADMAP.md
TRIGGER=STAGE33_08_REAUDIT_REOPENED_STAGE33_07
BIG_TASK_COUNT_REMAINS=11
REPAIR_CHILD_STAGES_COUNT_TOWARD_11=false
ORIGINAL_STAGE33_09_10_11_RENUMBERED_TO=33-40,33-41,33-42
```

This file defines repair numbering, child objectives, and exit interfaces. It does **not** own current progress, current child, current leaf, live counters, or live route status. The authoritative acceptance criteria remain `stages/stage33/33-00/unit-closure-contract.md`; this roadmap may refine execution but may not weaken that contract.

Use:

```text
current human state      -> stages/stage33/CURRENT.md
current machine state    -> stages/stage33/controller.json
stable Stage33 rules     -> stages/stage33/RULES.md
history/evidence index   -> stages/stage33/HISTORY.md
unit closure contract    -> stages/stage33/33-00/unit-closure-contract.md
Stage33-05 math state    -> stages/stage33/33-05/j2-representative-repair-state.json
```

## Numbering

The original downstream big-task objectives were renumbered to preserve repair address space:

```text
OLD 33-09 -> NEW 33-40  complete relevant-place and physical-local-locus certification
OLD 33-10 -> NEW 33-41  exact local evaluation production
OLD 33-11 -> NEW 33-42  physical adelic compatibility, final Brauer verdict, hostile audit
```

Repair address space is `33-09..33-39`. Repair work never increments the eleven-big-task Stage33 denominator by itself.

## Repair architecture

The contract-level repair-child chain is

```text
33-09  PICARD-EQUIVARIANT-TRANSPORT
33-10  ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER
33-11  ARITHMETIC-LOCALIZATION-CONNECTING-MAP
33-12  ARITHMETIC-HS-CLOSURE-AND-33-07-RECERTIFICATION
```

The labels `33-13`, `33-14`, and `33-15` below are retained as logical internal execution branches inside the open Stage33-12 arithmetic-HS repair. They do not independently satisfy the Stage33-12 exit gate and do not change `/11` progress.

Whether any branch is active/closed/released is read from CURRENT/controller.

## 33-09 — PICARD-EQUIVARIANT-TRANSPORT

Exit interface requires the retained Picard marking bridge and exact transport of the named integral/two-torsion actions needed downstream.

## 33-10 — ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER

Exit interface requires an exact absolute H1 receiver, all relevant kernel-Galois contribution accounted for, and a well-defined domain/codomain for the connecting-map child.

## 33-11 — ARITHMETIC-LOCALIZATION-CONNECTING-MAP

Exit interface requires the arithmetic localization connecting map with exact coverage of all 26 source directions and no unresolved connecting direction.

The exact closed interface currently available is the Stage33-11g hostile-audited `26/26` zero connecting map. Stage33-11 closure does not itself imply global-Q liftability or close Stage33-12.

## 33-12 — ARITHMETIC-HS-CLOSURE-AND-33-07-RECERTIFICATION

Stage33-12 is the contract-level final repair child for reopened Stage33-07. It assembles the closed 33-09/10/11 interfaces, the audited Stage33-05 K3 `Br[2]` arithmetic classification, the remaining finite/arithmetic HS work, the complete relevant Q-defined class inventory, and the hostile recertification of parent Stage33-07.

### K3 Br[2] subinterface

Stage33-12 consumes the **whole** Stage33-05 invariant K3 `Br[2]` block. It must not assume that a named nonzero geometric class descends.

The survivor interface follows the original Stage33-05 unit contract:

```text
K3_GEOMETRIC_BR2_DIM=2
K3_BR2_GQ_INVARIANT_BASIS_EXACT=true
K3_BR2_ARITHMETIC_HS_CLASSIFICATION_EXACT=true
DESCENT_OBSTRUCTION_ACCOUNTED=true
Q_RELEVANT_SURVIVING_DIM_EXACT=true
UNRESOLVED_K3_BR2_ARITHMETIC_UNKNOWN=0
STAGE33_05_HOSTILE_AUDIT=PASS
STAGE33_05_UNIT_CLOSED=true

if Q_RELEVANT_SURVIVING_DIM > 0:
    ALL_SURVIVING_K3_CLASSES_HAVE_EXPLICIT_ARITHMETIC_REPRESENTATIVES=true
else:
    EXACT_ZERO_SURVIVAL_CERTIFICATE=true
```

A corrected named J2 Q-defined preimage is not mandatory. The current audited input is

```text
GEOMETRIC_GQ_INVARIANT_BASIS=[J2,q1]
d2(J2)|_<ct> != 0
d2(q1)|_<ct> != 0
PAIRING_SIGNATURE_MATRIX_ROWS_[CsK2,CsK5]_COLS_[J2,q1]=[[1,1],[1,0]]
RESTRICTED_D2_RANK_F2=2
GLOBAL_D2_KERNEL_DIMENSION_F2=0
Q_RELEVANT_SURVIVING_DIM=0
EXACT_ZERO_SURVIVAL_CERTIFICATE=true
STAGE33_05_HOSTILE_AUDIT=PASS
STAGE33_05_UNIT_CLOSED=true
```

Thus the former corrected-J2-specific `d2=0 -> Q-defined J2 preimage` blocker is retired. The historical `ell_J2` remains revoked.

### Stage33-12 contract exit

The authoritative unit closure contract requires all of the following before Stage33-12 can exit:

```text
ARITHMETIC_HS_D2_COMPUTED=true
GLOBAL_Q_RESIDUE_LIFT_COMPLETION=true
COMPLETE_RELEVANT_Q_DEFINED_CLASS_INVENTORY_FOR_FROZEN_STAGE33_BRAUER_SCOPE=true
STAGE33_07_HOSTILE_RECERTIFICATION=PASS
STAGE33_12_EXIT_EXACT=true
```

The exact zero K3 `Br[2]` survival result satisfies the K3 contribution to that assembly, but it does not discharge independent BR0B/BR0G/global-Q inventory obligations.

### Internal branch 33-13 — FINITE-V4-KUMMER-MATRIX

Purpose: materialize the finite-V4 Kummer restriction on the remaining full-surface proper `Br[2]` receiver needed by the Stage33-12 arithmetic-HS assembly.

Planned exact interface:

```text
P=Br(Sbar)[2]^{G_Q}
DIM_F2(P)=10
DIM_F2(H^1(V4,Pic(Sbar)/2))=75
KUMMER_MATRIX_SHAPE=75x10
```

Exit requires all 10 exact columns, an exact 75x10 matrix, and no unresolved Kummer column. Guessed zero columns are forbidden.

### Internal branch 33-14 — FINITE-HS-COSETS-AND-TWO-PRIMARY-CONSTANT-BLOCK

Purpose: consume the exact finite Kummer matrix and discharge the remaining finite HS obstruction cosets and two-primary constant block.

Exit requires:

```text
FINITE_HS_OBSTRUCTION_COSETS_ACCOUNTED=26/26
GLOBAL_Q_BR0G_TWO_PRIMARY_RESIDUE_LIFTS_COMPLETE=true
REMAINING_TWO_PRIMARY_CONSTANT_BLOCK_CLOSED_EXACT=true
NO_REMAINING_ARITHMETIC_HS_OBSTRUCTION_BLOCK=true
```

### Internal branch 33-15 — GLOBAL-ARITHMETIC-HS-ASSEMBLY-AND-33-07-HOSTILE-RECERTIFICATION

Purpose: assemble every closed repair interface, complete the relevant Q-defined class inventory, and hostile-recertify parent Stage33-07.

Exit requires:

```text
ARITHMETIC_HS_D2_COMPUTED=true
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=true
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=true
STAGE33_07_HOSTILE_REAUDIT=PASS
```

Only this full audited Stage33-12 exit may reclose parent Stage33-07 and release Stage33-08.

## Retired old J2 checklist

The old checklist based on

```text
infinity exceptional attachment
ptsK order/index
qPicK exceptional coordinate
old branch-Jacobian Kummer glue
```

belongs to superseded J2 representative routes. It is historical evidence, not a mandatory checklist for the corrected finite-smooth-support route.

## Evidence/context policy

Compact evidence, bounded startup context, Actions/storage safety, loop handling, and claim-promotion rules are Stage33/Research-OS policy rather than roadmap progress. Use `RULES.md`, `AGENTS.md`, and the Research OS policies.

## Downstream big tasks

```text
Stage33-40 = original Stage33-09 objective
Stage33-41 = original Stage33-10 objective
Stage33-42 = original Stage33-11 objective
```

Their current release state belongs in controller/CURRENT.
