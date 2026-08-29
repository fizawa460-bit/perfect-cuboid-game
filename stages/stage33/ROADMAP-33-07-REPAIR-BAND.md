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

Stage33-08 exposed a deep Stage33-07 arithmetic Hochschild--Serre / global Gersten descent repair. The repair is not a restart of Stage33-07. Stage33-07 remains the blocked parent big task, while repair execution proceeds through coarse child stages.

The first three repair children are now closed exactly:

```text
33-09 PICARD-EQUIVARIANT-TRANSPORT = CLOSED_EXACT
33-10 ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER = CLOSED_EXACT_HOSTILE_AUDIT_PASS
33-11 ARITHMETIC-LOCALIZATION-CONNECTING-MAP = CLOSED_EXACT_HOSTILE_AUDIT_PASS
33-11 connecting columns = 26/26 exact, unresolved 0
```

The former single Stage33-12 scope had become too broad to expose human-visible progress. It mixed named J2/K3 orientation, Kummer glue, a 75x10 finite-V4 Kummer matrix, 26 finite HS obstruction cosets, a two-primary constant block, global HS assembly, and hostile recertification. This amendment therefore splits that scope into four coarse repair children, 33-12 through 33-15.

## 2. Numbering policy

```text
OLD 33-09 -> NEW 33-40  complete relevant-place and physical-local-locus certification
OLD 33-10 -> NEW 33-41  exact local evaluation production
OLD 33-11 -> NEW 33-42  physical adelic compatibility, final Brauer verdict, hostile audit
```

Repair address space remains `33-09..33-39`. There is no requirement to fill it. Only genuinely useful coarse audit boundaries receive numbers.

Stage33 remains an 11-big-task roadmap. Repair children do not change the denominator. Only hostile-audited closure of parent Stage33-07 changes progress from `6/11` to `7/11`.

## 3. Adaptive + parallel MAIN-batch rule

The mini-maps are search DAGs, not mandatory serial checklists.

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
CROSS_COARSE_STAGE_SPECULATION_MAY_BE_RECORDED_BUT_NOT_PROMOTED_AS_CERTIFIED_PROGRESS=true
```

Parallelism is primarily inside the current coarse repair child. Later-child diagnostics may be recorded, but certified progress moves forward only when the current child's exact exit condition is satisfied.

## 4. Stage33-09 — PICARD-EQUIVARIANT-TRANSPORT

Status: `CLOSED_EXACT`.

Purpose: source-lock the marked Picard basis bridge and transport the named integral/two-torsion actions exactly.

Exit condition, already satisfied:

```text
HISTORICAL_RETAINED_PICARD_MARKING_BRIDGE_CERTIFIED=true
NAMED_INTEGRAL_AND_TWO_TORSION_ACTIONS_SOURCE_LOCKED=true
PICARD_EQUIVARIANT_TRANSPORT_CLOSED=true
```

## 5. Stage33-10 — ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER

Status: `CLOSED_EXACT_HOSTILE_AUDIT_PASS`.

Purpose: identify the mathematically correct absolute receiver consumed by the arithmetic localization computation. The finite V4 shortcut was explicitly replaced by the exact absolute receiver, including the relevant kernel-Galois contribution.

Exit condition, already satisfied:

```text
ABSOLUTE_H1_RECEIVER_EXACT=true
FINITE_V4_SHORTCUT_STATUS=PROVED_VALID_OR_EXPLICITLY_REPLACED
KERNEL_GALOIS_RELEVANT_CONTRIBUTION_ACCOUNTED=true
STAGE33_11_DOMAIN_AND_CODOMAIN_WELL_DEFINED=true
```

## 6. Stage33-11 — ARITHMETIC-LOCALIZATION-CONNECTING-MAP

Status: `CLOSED_EXACT_HOSTILE_AUDIT_PASS`.

Purpose: compute the genuine arithmetic localization connecting map / middle Gersten extension data for all 26 mixed-order source directions using the exact receiver certified by Stage33-10.

Exact exit already achieved:

```text
ARITHMETIC_LOCALIZATION_CONNECTING_MAP_COMPUTED=true
CONNECTING_SOURCE_DIRECTIONS_COVERED=26/26
NO_UNRESOLVED_CONNECTING_DIRECTION=true
CONNECTING_MAP=COMPUTED_EXACT_ZERO_MAP
```

Stage33-11 is historical input from this point onward and is opaque by default outside hostile-audit or specifically named missing-interface needs.

## 7. Stage33-12 — J2-MARKED-KC-KUMMER-GLUE

Purpose: finish the named J2 bridge from the branch-normalization half-divisor through the pinned marked Stoll Kc resolution into the exact Kc Picard discriminant/Brauer 2-torsion coordinate.

This child deliberately stops before materializing the full 75x10 finite-V4 Kummer matrix. It exists to isolate the named orientation/glue problem as a clean auditable interface.

Current exact checkpoint inherited from PR #1460:

```text
J2_NAMED_HALF_DIVISOR_MATERIALIZED=true
J2_CV_TO_RULED_SUPPORT_ADAPTER_MATERIALIZED=true
J2_BRANCH_IDENTIFIED_WITH_STOLL_CSK22=true
J2_THREE_STOLL_KC_SUPPORT_IMAGES_MATERIALIZED=true
J2_INFINITY_EXCEPTIONAL_GEOMETRIC_ATTACHMENT_MATERIALIZED=true
J2_INFINITY_STOLL_PTSK_ORDER_INDEX_MATERIALIZED=false
J2_INFINITY_QPICK_EXCEPTIONAL_COORDINATE_MATERIALIZED=false
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
```

Human-visible progress counter:

```text
33-12 milestone 1/5 = named J2 half-divisor and CV support adapter [DONE]
33-12 milestone 2/5 = pinned Stoll branch/support identification [DONE]
33-12 milestone 3/5 = infinity exceptional geometric attachment [DONE]
33-12 milestone 4/5 = ptsK index + qPicK exceptional coordinate [OPEN]
33-12 milestone 5/5 = branch-Jacobian 2-torsion -> Kc Picard discriminant Kummer glue and named J2 coordinate [OPEN]
VISIBLE_PROGRESS=3/5
```

The algorithmic `ptsK`/`qPicK` extraction may use an explicit/manual remote Magma diagnostic, but unreliable remote execution is not a PR merge gate. A deterministic committed certificate must be retained before exact closure credit.

Exit condition:

```text
J2_INFINITY_STOLL_PTSK_ORDER_INDEX_MATERIALIZED=true
J2_INFINITY_QPICK_EXCEPTIONAL_COORDINATE_MATERIALIZED=true
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=true
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=true
J2_KC_KERNEL_LINE_FIXED=true
STAGE33_12_CLOSED_EXACT=true
```

Closing 33-12 releases 33-13 only. It does not close parent Stage33-07 and does not change Stage33 progress from 6/11.

## 8. Stage33-13 — FINITE-V4-KUMMER-MATRIX

Purpose: materialize the finite-V4 Kummer restriction on the full-surface proper Br[2] receiver as the literal `75 x 10` matrix already defined by Stage33-12 checkpoint data.

Starting interface:

```text
P=Br(Sbar)[2]^{G_Q}
DIM_F2(P)=10
DIM_F2(H^1(V4,Pic(Sbar)/2))=75
KUMMER_MATRIX_SHAPE=75x10
MATERIALIZED_COLUMNS=0/10
```

Human-visible progress is the exact number of independently materialized and verified columns:

```text
VISIBLE_PROGRESS=<materialized_columns>/10
```

Columns may be produced independently or in blocks when exact naturality/symmetry permits. Partial exact columns are retained monotonically. No guessed zero column is allowed.

Exit condition:

```text
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=10/10
FINITE_V4_KUMMER_MATRIX_EXACT=true
NO_UNRESOLVED_KUMMER_COLUMN=true
STAGE33_13_CLOSED_EXACT=true
```

Closing 33-13 releases 33-14 only. It does not close parent Stage33-07.

## 9. Stage33-14 — FINITE-HS-COSETS-AND-TWO-PRIMARY-CONSTANT-BLOCK

Purpose: consume the exact finite Kummer matrix and discharge the two remaining arithmetic HS obstruction blocks:

```text
A = finite 26-direction HS obstruction cosets after U44
B = two-primary constant-character cokernel / global residue-lift block
```

Human-visible progress is two-dimensional:

```text
FINITE_HS_COSETS=<materialized_or_discharged>/26
CONSTANT_TWO_PRIMARY_BLOCK=OPEN|CLOSED_EXACT
```

The finite side should preserve monotone exact progress `0/26 -> ... -> 26/26` when individual/block computation is the route. A global exact argument may close multiple or all cosets at once.

The constant block remains a separate line item and must not be inferred closed from the finite block, boundary-function scalar cancellation, odd-primary completion, or zero localization alone.

Exit condition:

```text
FINITE_HS_OBSTRUCTION_COSETS_ACCOUNTED=26/26
GLOBAL_Q_BR0G_TWO_PRIMARY_RESIDUE_LIFTS_COMPLETE=true
REMAINING_TWO_PRIMARY_CONSTANT_BLOCK_CLOSED_EXACT=true
NO_REMAINING_ARITHMETIC_HS_OBSTRUCTION_BLOCK=true
STAGE33_14_CLOSED_EXACT=true
```

Closing 33-14 releases 33-15 only. It does not yet close parent Stage33-07.

## 10. Stage33-15 — GLOBAL-ARITHMETIC-HS-ASSEMBLY-AND-33-07-HOSTILE-RECERTIFICATION

Purpose: perform the final global arithmetic Hochschild--Serre assembly from closed 33-09..33-14 interfaces, complete the relevant Q-defined class inventory, and hostile-recertify the parent Stage33-07 unit.

This child is intentionally integration/audit heavy rather than a home for another large exploratory kernel. If assembly exposes a genuinely new mathematical gap, do not force PASS; reopen/split the relevant dependency and keep Stage33-07 blocked.

Human-visible progress:

```text
GLOBAL_HS_ASSEMBLY=NOT_STARTED|IN_PROGRESS|CLOSED_EXACT
Q_DEFINED_CLASS_INVENTORY=INCOMPLETE|COMPLETE_EXACT
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN|RUNNING|PASS|FAIL
```

Exit condition for success:

```text
ARITHMETIC_HS_D2_COMPUTED=true
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=true
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=true
STAGE33_07_HOSTILE_REAUDIT=PASS
```

Only then may:

```text
STAGE33_07=CLOSED
STAGE33_PROGRESS=7/11
STAGE33_08_RELEASED=true
```

No earlier repair-child closure grants those promotions.

## 11. Visible progress dashboard contract

Every future Stage33 MAIN checkpoint from 33-12 through 33-15 should expose a compact human-readable progress line in the controller/result handoff:

```text
33-12: J2/Kummer glue milestones x/5
33-13: finite-V4 Kummer matrix columns x/10
33-14: finite HS cosets x/26; constant 2-primary block OPEN/CLOSED
33-15: global assembly state; Q-defined inventory state; hostile recertification state
```

These counters are navigational only. They do not replace exact certificates, audit states, or exit conditions.

## 12. Expansion rule

```text
33-16..33-39=UNUSED_BY_DEFAULT
```

Do not manufacture stages merely to consume the reserved range. If 33-12, 33-13, or 33-14 exposes a genuinely independent new exact subkernel that is too large for the current coarse child, use the next number and amend dependencies explicitly.

Labels such as `33-13a` or `33-14b` are branches inside a coarse child; they do not count toward the 11-task denominator.

## 13. Workflow / MAIN-batch policy

Prefer one lightweight stage-local deterministic checkpoint workflow for the current repair child. Heavy or unreliable external probes must not be ordinary PR-synchronized merge gates.

```text
.github/workflows/stage33-12-main.yml  = deterministic 33-12 checkpoint replay
remote Magma / external extraction     = manual or narrowly armed diagnostic
future 33-13/14 workflows              = created only when those children are released
```

`Stage33-main-batch` means: read the current repair-child interface, advance authorized live branches, preserve exact partial progress, and stop once the current child closes or exposes a justified blocker. Do not reconstruct audited 33-09..33-11 history by default.

## 14. Downstream big tasks after repair

```text
Stage33-40 = original Stage33-09 objective
Stage33-41 = original Stage33-10 objective
Stage33-42 = original Stage33-11 objective
```

Their mathematical acceptance contracts remain those of the original `ROADMAP.md`; only their unit numbers moved. Stage33-40 remains blocked until Stage33-08 is actually closed.

## 15. Firewalls

```text
REPAIR_CHILDREN_COUNT_TOWARD_STAGE33_PROGRESS=false
STAGE33_PROGRESS_REMAINS=6/11_UNTIL_33_07_HOSTILE_RECERTIFICATION_PASS
STAGE33_08_RELEASE_BEFORE_33_07_CLOSED=false
THEOREM_CREDIT=false_UNLESS_SEPARATELY_AUTHORIZED
ENDPOINT_CREDIT=false_UNLESS_SEPARATELY_AUTHORIZED
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Operational PASS, CI success, a materialized Kummer column, or closure of one repair child never by itself promotes parent Stage33-07 credit.