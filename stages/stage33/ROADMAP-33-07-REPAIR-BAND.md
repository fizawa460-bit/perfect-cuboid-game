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

Stage33-08 exposed a deep Stage33-07 arithmetic Hochschild--Serre / global Gersten descent repair. PR #1430 already pushed the geometric side far forward: the intrinsic 14-dimensional A[2] module, actual coordinate-swap pair, exact S3/seven-sign relations, named cc/ct compatibility, intrinsic-to-retained A[2] transport, and mixed-order divisibility filtration were materially established. The remaining repair is not a restart of Stage33-07.

The unresolved chain is concentrated in four coarse child stages: finish the historical retained Picard marking bridge; identify the correct absolute G_Q cohomology receiver; compute the arithmetic localization connecting map for all 26 source directions; then assemble arithmetic HS and hostile-recertify Stage33-07.

Stage33-07 remains the blocked parent big task. New repair execution moves to coarse child stages beginning at 33-09 so the historical `stage33-07-*` workflow family stops growing.

## 2. Numbering policy

```text
OLD 33-09 -> NEW 33-40  complete relevant-place and physical-local-locus certification
OLD 33-10 -> NEW 33-41  exact local evaluation production
OLD 33-11 -> NEW 33-42  physical adelic compatibility, final Brauer verdict, hostile audit
```

The repair may use `33-09..33-39`, but this is only address space. There is no requirement or intention to fill it. The default plan uses 33-09..33-12 only. New stage numbers are added only if a genuinely new exact subkernel cannot be contained inside the current coarse stage.

Stage33 remains an 11-big-task roadmap. Repair children do not change the denominator; only hostile-audited closure of parent Stage33-07 changes progress from 6/11 to 7/11.

## 3. Adaptive + parallel MAIN-batch rule

The mini-maps are search DAGs, not checklists and not necessarily serial pipelines.

```text
ALL_BRANCHES_MUST_RUN=false
SAFE_INDEPENDENT_BRANCHES_MAY_RUN_IN_PARALLEL=true
MAIN_BATCH_ADVANCES_MULTIPLE_LIVE_BRANCHES_UNTIL_BLOCKED_OR_CLOSED=true
FIRST_EXACT_CLOSURE_WINS=true
SIBLING_BRANCHES_MAY_STOP_AFTER_EXACT_CLOSURE=true
FAILED_OR_BLOCKED_BRANCH_DOES_NOT_AUTHORIZE_NEXT_COARSE_STAGE=true
MINIMAP_EXHAUSTED_WITHOUT_EXIT_CONDITION_DOES_NOT_ADVANCE=true
IF_CURRENT_COARSE_STAGE_DOES_NOT_CLOSE=EXTEND_OR_SPLIT_CURRENT_STAGE
NEXT_COARSE_STAGE_ALLOWED_ONLY_AFTER_CURRENT_EXIT_CONDITION=true
```

`Stage33-main-batch` may advance several independent live branches of the current coarse stage in parallel until each branch either closes, reaches a justified block, or produces an exact stage-level closure. Branch ordering below is preference/dependency guidance, not a requirement to wait for one branch to fail before starting every other branch. A branch that logically depends on output from another branch remains gated by that dependency.

Once any branch or combination of branches proves the coarse-stage exit condition exactly, unused sibling/fallback branches need not run. Conversely, if all currently planned branches block or fail while the exit condition remains open, extend the mini-map inside the same coarse stage; do not advance merely because the written map was exhausted.

## 4. Stage33-09 — PICARD-EQUIVARIANT-TRANSPORT

### Inherited state from PR #1430

Already materially established and not to be rediscovered from zero:

```text
intrinsic A[2] dimension = 14
actual intrinsic coordinate-swap pair identified
exact S3 relations
seven coordinate-sign actions exact
named cc/ct V4 compatibility exact
intrinsic -> retained A[2] swap transport materially established
mixed-order filtration 4A[8] subset 2A[4] subset A[2] checked
```

The direct replay into the literal historical q256 common-Smith basis produced a negative route result: the locally reconstructed Picard Gram did not certify identity with the historical q256 Gram. That route remains diagnostic evidence, not a reason to repeat the whole geometric search.

### Remaining target

Finish the source-locked marked Picard basis bridge from the pinned upstream qPic/INDLIST marking to the historical retained q256 Picard basis, then revalidate the already-known named actions through that bridge.

```text
primary missing adapter = pinned qPic/INDLIST -> historical retained q256 marking
marked bridge must be source locked
actual swaps / cc / ct / sign actions must transport exactly through it
no guessed-basis or linear-envelope ambiguity may remain
```

Exit condition:

```text
HISTORICAL_RETAINED_PICARD_MARKING_BRIDGE_CERTIFIED=true
NAMED_INTEGRAL_AND_TWO_TORSION_ACTIONS_SOURCE_LOCKED=true
PICARD_EQUIVARIANT_TRANSPORT_CLOSED=true
```

33-09 is therefore near-exit by current evidence, but if the marked bridge exposes a genuinely new incompatibility its mini-map may expand. Only its exact exit releases 33-10.

## 5. Stage33-10 — ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER

Purpose: identify the mathematically correct absolute receiver that Stage33-11 must map into. This is the finite-to-absolute Galois cohomology repair itself, not merely planning for Stage33-11.

Known starting point:

```text
finite H^1(V4, proper geometric Br[2]) dimension = 16
absolute H^1(G_Q, proper geometric Br[2]) NOT YET identified with finite V4 H1
```

### Mini-map

#### 33-10a — finite-to-absolute shortcut test
Test whether the existing finite V4 receiver already equals the required absolute receiver. This is cheap and should start immediately.

#### 33-10b — inflation-restriction decomposition
Compute the exact inflation-restriction / kernel-Galois decomposition. This may run in parallel with 10a to the extent its inputs are already available. If it proves the kernel contribution zero, it may itself supply the closure route.

#### 33-10c — relevant kernel-Galois contribution
If nonzero kernel contribution is established or strongly exposed, materialize only the part that can reach the Stage33 arithmetic receiver. This branch depends on enough 10b information to define the contribution correctly.

#### 33-10d — direct absolute H1 construction fallback
Independent/direct construction route for the required absolute H1 receiver. It may be started in parallel when cost is justified rather than waiting for every shortcut route to fail, but it must obey the same source-lock and exactness requirements.

#### 33-10e — absolute receiver certification
Common convergence/exit node. It consumes whichever successful branch or combination of branches suffices.

Possible closures include:

```text
10a alone proves finite shortcut exact -> 10e -> close
10b proves kernel contribution zero -> 10e -> close
10b + 10c account for nonzero contribution -> 10e -> close
10d directly constructs receiver -> 10e -> close
multiple partial branches combine -> 10e -> close
```

Exit condition:

```text
ABSOLUTE_H1_RECEIVER_EXACT=true
FINITE_V4_SHORTCUT_STATUS=PROVED_VALID_OR_EXPLICITLY_REPLACED
KERNEL_GALOIS_RELEVANT_CONTRIBUTION_ACCOUNTED=true
STAGE33_11_DOMAIN_AND_CODOMAIN_WELL_DEFINED=true
```

Not all 10a..10d must finish. MAIN-batch may push multiple viable branches concurrently. Once 10e certifies the exit, unfinished siblings stop. If none closes the receiver, add 10f/10g or split a genuinely independent new subkernel; Stage33-11 remains blocked.

## 6. Stage33-11 — ARITHMETIC-LOCALIZATION-CONNECTING-MAP

Purpose: compute the genuine arithmetic localization connecting map / middle Gersten extension data for all 26 mixed-order source directions using the exact receiver certified by Stage33-10.

Starting state inherited from Stage33-07/#1430:

```text
source directions = 26
connecting-map columns explicitly materialized = 0/26
middle Gersten module action not yet materialized
```

The exit condition is complete exact coverage, not a prescribed method. All 26 directions must be determined, but they need not be solved one-by-one.

### Parallel mini-map

#### 33-11a — global/all-at-once closure
Search for exact module structure, naturality, symmetry, tensor structure, or an equivalent formula determining all 26 columns simultaneously.

#### 33-11b — symmetry/orbit/block closure
In parallel where possible, search for exact decompositions in which representative columns determine entire blocks/orbits.

#### 33-11c — individual/smallest-block fallback
Once Stage33-10 fixes the receiver and a source direction is independently computable, individual or small-block production may proceed without waiting for the global route to fail. Exact columns produced here are retained even if a later global formula is found.

MAIN-batch may therefore make monotone progress such as:

```text
0/26 -> 2/26 -> 7/26 -> 19/26 -> 26/26
```

while global and block-level routes continue in parallel. A later global theorem/formula may close all remaining columns at once. Conversely, if no global closure exists, the individual route is a valid final fallback.

Further routes may be added if new exact structure appears. Unsuccessful global/block branches do not block already-certified individual columns, but Stage33-12 remains blocked until complete coverage.

Scope may include when genuinely required:

```text
middle Gersten module action
26 connecting-map columns or exact equivalent representation
cc/ct naturality
project 14x26 L-squareclass tensor
source-locked arithmetic localization evidence
```

Exit condition:

```text
ARITHMETIC_LOCALIZATION_CONNECTING_MAP_COMPUTED=true
CONNECTING_SOURCE_DIRECTIONS_COVERED=26/26
NO_UNRESOLVED_CONNECTING_DIRECTION=true
```

## 7. Stage33-12 — ARITHMETIC-HS-CLOSURE-AND-33-07-RECERTIFICATION

Purpose: assemble the repaired arithmetic Hochschild--Serre descent using exact outputs of 33-09/10/11 and decide the parent Stage33-07 unit.

Scope:

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

Only then may Stage33-07 become `CLOSED`, progress become `7/11`, and Stage33-08 be released. If assembly exposes a new gap, remain in 33-12 (or split a genuinely independent new subkernel) rather than releasing Stage33-08 prematurely.

## 8. Expansion rule

```text
33-13..33-39=UNUSED_BY_DEFAULT
```

Do not manufacture stages to consume the reserved range. Keep work inside 33-09..33-12 unless a coarse phase becomes independently too large or exposes a genuinely new exact subkernel with a clean audit boundary. Use only the next number actually needed.

Labels such as `33-10a` or `33-11b` are branches inside the coarse stage; they do not consume new Stage33 unit numbers and do not count toward the 11-task denominator.

## 9. Workflow / MAIN-batch policy

New repair work should stop growing the historical `stage33-07-*` workflow family. Prefer one stage-local workflow per coarse phase with multiple jobs/matrices for parallel branches:

```text
.github/workflows/stage33-09-main.yml
.github/workflows/stage33-10-main.yml
.github/workflows/stage33-11-main.yml
.github/workflows/stage33-12-main.yml
```

`Stage33-main-batch` means: inspect all currently authorized live branches of the current coarse stage, advance multiple independent branches when useful, preserve exact partial progress, stop branches that hit justified blockers, and terminate sibling work once a stage-level exact closure makes it unnecessary.

Heavy/unreliable remote Magma probes should remain manual diagnostics instead of PR-synchronized triggers. Historical Stage33-07 workflows remain evidence and need not be renamed or rerun merely because the roadmap changes.

## 10. Downstream big tasks after repair

```text
Stage33-40 = original Stage33-09 objective
Stage33-41 = original Stage33-10 objective
Stage33-42 = original Stage33-11 objective
```

Their mathematical acceptance contracts remain exactly those in the original `ROADMAP.md`; only their unit numbers move. Stage33-40 remains blocked until Stage33-08 is actually closed.

## 11. Firewalls

```text
REPAIR_MINIMAP_IS_CHECKLIST=false
SAFE_PARALLEL_BRANCH_EXECUTION_ALLOWED=true
MAIN_BATCH_IS_SINGLE_BRANCH_ONLY=false
UNUSED_FALLBACK_BRANCHES_MUST_RUN=false
MINIMAP_EXHAUSTED_WITHOUT_EXIT_CONDITION_DOES_NOT_ADVANCE=true
PARTIAL_PROGRESS_IS_RETAINED=true
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
