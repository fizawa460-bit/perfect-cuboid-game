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

Stage33-08 exposed a deep Stage33-07 arithmetic Hochschild--Serre / global Gersten descent repair. The repair has already expanded into integral Picard marking, coordinate-swap recovery, intrinsic-to-retained two-torsion transport, named V4 action identification, finite/absolute H1 separation, naturality constraints and the still-unmaterialized arithmetic localization connecting map.

Keeping all of that inside `33-07` makes the unit too large to audit and causes the growing `stage33-07-*` workflow family to re-fire unrelated historical leaves. Stage33-07 therefore remains the blocked parent big task, while the repair is moved into a small number of coarse child stages starting at 33-09.

## 2. Numbering policy

The original downstream meanings are preserved and moved far away so the repair can expand only if it genuinely needs to:

```text
OLD 33-09 -> NEW 33-40  complete relevant-place and physical-local-locus certification
OLD 33-10 -> NEW 33-41  exact local evaluation production
OLD 33-11 -> NEW 33-42  physical adelic compatibility, final Brauer verdict, hostile audit
```

The repair may use numbers `33-09..33-39`, but this is only an address space. There is no requirement or intention to fill it. The default repair plan below uses only four coarse stages. New numbers are added only when one of those stages exposes a genuinely new exact subkernel that cannot be kept inside its current scope.

Stage33 remains an 11-big-task roadmap. Repair children do not change the denominator or progress count; only hostile-audited closure of parent Stage33-07 changes progress from 6/11 to 7/11.

## 3. Coarse Stage33-07 repair roadmap

### Stage33-09 — PICARD-EQUIVARIANT-TRANSPORT

Purpose: finish the geometric/integral identification layer needed before arithmetic Hochschild--Serre can be trusted.

Scope includes, without forcing separate stage numbers:

```text
Stage32 retained Picard marking -> Stage33 Picard basis bridge
actual integral coordinate swap actions
intrinsic A_T[2] <-> retained A_T[2] transport
identification of transported swaps with named cc/ct generators
proper geometric Br[2] named V4 action
exact naturality checks needed by the next phase
```

Exit condition: the actual named integral/two-torsion action is fixed exactly; no linear-envelope or guessed-basis ambiguity remains.

### Stage33-10 — ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER

Purpose: repair the finite-to-absolute cohomology gap exposed by the Stage33-08 re-audit.

Scope includes:

```text
H^1(V4, Br(Sbar)[2]) versus H^1(G_Q, Br(Sbar)[2])
inflation-restriction / kernel-Galois contribution
absolute receiver identification
all assumptions needed to pass from the named finite V4 action to the arithmetic G_Q term
```

Exit condition: the absolute H1 receiver is exact and the previous finite-V4 shortcut is either proved valid in this case or explicitly replaced.

### Stage33-11 — ARITHMETIC-LOCALIZATION-CONNECTING-MAP

Purpose: materialize the genuine arithmetic localization connecting map / middle Gersten extension data for the 26 mixed-order source directions.

Scope includes:

```text
middle Gersten module action
26 connecting-map columns or an exact equivalent representation
cc/ct naturality
project 14x26 L-squareclass tensor when genuinely required
arithmetic localization data sufficient to evaluate the HS obstruction
```

Exit condition: `ARITHMETIC_LOCALIZATION_CONNECTING_MAP_COMPUTED=true` with source-locked exact evidence.

### Stage33-12 — ARITHMETIC-HS-CLOSURE-AND-33-07-RECERTIFICATION

Purpose: assemble the repaired arithmetic Hochschild--Serre descent and decide the parent Stage33-07 unit.

Scope includes:

```text
arithmetic HS d2 / remaining obstruction data
global Q residue-lift completion
complete relevant Q-defined class inventory for the frozen Stage33 scope
BR0B all-primary completeness check
hostile re-audit of repaired Stage33-07
```

Exit condition for success:

```text
ARITHMETIC_HS_D2_COMPUTED=true
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=true
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=true
STAGE33_07_HOSTILE_REAUDIT=PASS
```

Only then may Stage33-07 become `CLOSED`, progress become `7/11`, and Stage33-08 be released.

## 4. Expansion rule

```text
33-13..33-39=UNUSED_BY_DEFAULT
```

Do not manufacture stages to consume the reserved range. Keep work inside 33-09..33-12 unless a coarse phase becomes independently too large or exposes a new exact subkernel with a clean audit boundary. If that happens, use only the next number actually needed.

## 5. Workflow policy

New repair work should stop growing the historical `stage33-07-*` workflow family. Prefer one stage-local workflow per coarse repair phase, with jobs or matrices inside it:

```text
.github/workflows/stage33-09-main.yml
.github/workflows/stage33-10-main.yml
.github/workflows/stage33-11-main.yml
.github/workflows/stage33-12-main.yml
```

Heavy/unreliable remote Magma probes should be manual diagnostic workflows instead of PR-synchronized triggers. Historical Stage33-07 workflows remain evidence and need not be renamed or rerun merely because the roadmap changes.

## 6. Downstream big tasks after repair

```text
Stage33-40 = original Stage33-09 objective
Stage33-41 = original Stage33-10 objective
Stage33-42 = original Stage33-11 objective
```

Their mathematical acceptance contracts remain exactly those in the original `ROADMAP.md`; only their unit numbers move. Stage33-40 remains blocked until Stage33-08 is actually closed.

## 7. Firewalls

```text
REPAIR_CHILD_CLOSED_IMPLIES_PARENT_33_07_CLOSED=false
REPAIR_CHILD_COUNT_CHANGES_BIG_TASK_COUNT=false
OLD_33_09_10_11_SEMANTICS_DROPPED=false
OLD_33_09_10_11_SEMANTICS_MOVED_TO_33_40_41_42=true
STAGE33_08_CAN_RELEASE_BEFORE_33_07_CLOSES=false
RENUMBERING_GRANTS_THEOREM_CREDIT=false
RENUMBERING_GRANTS_ENDPOINT_CREDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
