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

## 1. Current topology

Stage33-08 exposed a deep Stage33-07 arithmetic Hochschild--Serre / global Gersten descent repair. Stage33-07 remains the blocked parent big task, while repair execution proceeds through coarse child stages.

Closed exact repair children:

```text
33-09 PICARD-EQUIVARIANT-TRANSPORT = CLOSED_EXACT
33-10 ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER = CLOSED_EXACT_HOSTILE_AUDIT_PASS
33-11 ARITHMETIC-LOCALIZATION-CONNECTING-MAP = CLOSED_EXACT_HOSTILE_AUDIT_PASS
33-11 connecting columns = 26/26 exact, unresolved 0
```

Remaining children:

```text
33-12 = corrected J2 / marked-Kc / arithmetic descent closure package
33-13 = finite-V4 75x10 Kummer matrix
33-14 = 26 finite HS cosets + two-primary constant block
33-15 = global arithmetic HS assembly + Stage33-07 hostile recertification
```

Important current reopen:

```text
Stage33-05 = REOPENED at R5 arithmetic descent
current Stage33 progress = 5/11
successful Stage33-05 reclosure restores progress to 6/11
hostile-audited Stage33-07 closure later raises progress from 6/11 to 7/11
```

Repair children do not change the 11-big-task denominator.

## 2. Numbering and adaptive execution

```text
OLD 33-09 -> NEW 33-40  complete relevant-place and physical-local-locus certification
OLD 33-10 -> NEW 33-41  exact local evaluation production
OLD 33-11 -> NEW 33-42  physical adelic compatibility, final Brauer verdict, hostile audit
33-16..33-39 = UNUSED_BY_DEFAULT
```

Do not manufacture stages to consume numbers. Split only when a genuinely independent exact subkernel becomes too large for the current child.

Mini-maps are search DAGs, not mandatory serial checklists. Safe independent branches may run in parallel inside the current child. Exact partial progress is retained monotonically. A blocked branch does not authorize the next child; the next child is released only after the current exit condition.

## 3. Stage33-09..11 frozen interfaces

### 33-09 — PICARD-EQUIVARIANT-TRANSPORT
Status: `CLOSED_EXACT`.

```text
HISTORICAL_RETAINED_PICARD_MARKING_BRIDGE_CERTIFIED=true
NAMED_INTEGRAL_AND_TWO_TORSION_ACTIONS_SOURCE_LOCKED=true
PICARD_EQUIVARIANT_TRANSPORT_CLOSED=true
```

### 33-10 — ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER
Status: `CLOSED_EXACT_HOSTILE_AUDIT_PASS`.

```text
ABSOLUTE_H1_RECEIVER_EXACT=true
FINITE_V4_SHORTCUT_STATUS=PROVED_VALID_OR_EXPLICITLY_REPLACED
KERNEL_GALOIS_RELEVANT_CONTRIBUTION_ACCOUNTED=true
STAGE33_11_DOMAIN_AND_CODOMAIN_WELL_DEFINED=true
```

### 33-11 — ARITHMETIC-LOCALIZATION-CONNECTING-MAP
Status: `CLOSED_EXACT_HOSTILE_AUDIT_PASS`.

```text
ARITHMETIC_LOCALIZATION_CONNECTING_MAP_COMPUTED=true
CONNECTING_SOURCE_DIRECTIONS_COVERED=26/26
NO_UNRESOLVED_CONNECTING_DIRECTION=true
CONNECTING_MAP=COMPUTED_EXACT_ZERO_MAP
```

33-09..11 are opaque by default after closure. Do not reload their full evidence, PR diffs, workflow logs, or generated certificates unless the current proof names a missing representative/matrix, a source-lock mismatch occurs, a certificate contradiction occurs, or hostile-audit mode explicitly requires expansion.

## 4. Stage33-12 — CORRECTED-J2-MARKED-KC-ARITHMETIC-CLOSURE

Purpose: package the corrected named J2 bridge into an exact Stage33-12 child closure. Stage33-12 does not run an independent second J2 derivation in parallel with the Stage33-05 R5 repair.

### Anti-duplication rule

The historical Stage33-12 checklist

```text
infinity exceptional attachment
ptsK order/index
qPicK exceptional coordinate
old branch-Jacobian Kummer glue
```

belonged to the superseded representative route. For the corrected divisor `D=P_r2-P_r4`, exact work established finite smooth support on marked `CsK[22]` and eliminated the old infinity/exceptional dependency.

Therefore:

```text
OLD_INFINITY_PTSK_QPICK_CHECKLIST_FOR_CORRECTED_J2 = RETIRED
DO_NOT_RECOMPUTE_OLD_INFINITY_ROUTE = true
STAGE33_05_R5_REPAIR_STATE = AUTHORITATIVE_FOR_CURRENT_J2_ARITHMETIC_GAP
```

Historical files remain cold evidence and are not deleted.

### Corrected J2 evidence already exact

```text
corrected geometric J2=(f2,1) nonzero                     DONE
explicit CV E[2] cocycle xi(rho)=Tr                      DONE
marked Brauer coordinate J2=[1,0]                       DONE
corrected finite smooth Kc support on CsK[22]            DONE
branch Pic0[2] -> surface H^2(mu2) adapter               DONE
explicit Cech surface mu2 lift lambda_D                  DONE
generic cc/ct splitting data and ct norm module          DONE
actual compactified Pic/2 defect                          OPEN
integral Pic lifts                                        OPEN
Hochschild-Serre d2 class                                 OPEN
Q-defined corrected J2 Brauer preimage                    OPEN
```

The exact current leaf is owned by:

`stages/stage33/ROADMAP-33-05-J2-REPRESENTATIVE-REPAIR.md`.

### Stage33-12 closure contract

Stage33-12 remains blocked while Stage33-05 R5 arithmetic descent is open. After successful full R5 exit and its mandatory super-hostile audit, Stage33-12 closure is a corrected-evidence audit/package step, not a replay of the old infinity route.

Exact Stage33-12 exit requires:

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
STAGE33_05_SUPER_HOSTILE_AUDIT=PASS
STAGE33_12_CLOSED_EXACT=true
```

If the actual HS `d2` class is nonzero, do not close Stage33-12. Record the exact no-go and rebuild the affected dependency chain.

Stage33-13 is not released until `STAGE33_12_CLOSED_EXACT=true`.

## 5. Stage33-13 — FINITE-V4-KUMMER-MATRIX

Purpose: materialize the finite-V4 Kummer restriction on the full-surface proper Br[2] receiver after Stage33-12 exact closure.

```text
P=Br(Sbar)[2]^{G_Q}
DIM_F2(P)=10
DIM_F2(H^1(V4,Pic(Sbar)/2))=75
KUMMER_MATRIX_SHAPE=75x10
VISIBLE_PROGRESS=<materialized_columns>/10
```

Columns may be produced independently or in exact natural blocks. Partial exact columns are retained monotonically; guessed zero columns are forbidden.

Exit:

```text
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=10/10
FINITE_V4_KUMMER_MATRIX_EXACT=true
NO_UNRESOLVED_KUMMER_COLUMN=true
STAGE33_13_CLOSED_EXACT=true
```

## 6. Stage33-14 — FINITE-HS-COSETS-AND-TWO-PRIMARY-CONSTANT-BLOCK

Purpose: consume the exact finite Kummer matrix and discharge the two remaining arithmetic HS obstruction blocks.

```text
FINITE_HS_COSETS=<materialized_or_discharged>/26
CONSTANT_TWO_PRIMARY_BLOCK=OPEN|CLOSED_EXACT
```

The constant block is independent bookkeeping and must not be inferred closed from finite-block cancellation, odd-primary completion, boundary-function scalar cancellation, or zero localization.

Exit:

```text
FINITE_HS_OBSTRUCTION_COSETS_ACCOUNTED=26/26
GLOBAL_Q_BR0G_TWO_PRIMARY_RESIDUE_LIFTS_COMPLETE=true
REMAINING_TWO_PRIMARY_CONSTANT_BLOCK_CLOSED_EXACT=true
NO_REMAINING_ARITHMETIC_HS_OBSTRUCTION_BLOCK=true
STAGE33_14_CLOSED_EXACT=true
```

## 7. Stage33-15 — GLOBAL-ARITHMETIC-HS-ASSEMBLY-AND-33-07-HOSTILE-RECERTIFICATION

Purpose: final global arithmetic HS assembly from closed 33-09..14 interfaces, relevant Q-defined class inventory completion, and hostile recertification of parent Stage33-07.

```text
GLOBAL_HS_ASSEMBLY=NOT_STARTED|IN_PROGRESS|CLOSED_EXACT
Q_DEFINED_CLASS_INVENTORY=INCOMPLETE|COMPLETE_EXACT
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN|RUNNING|PASS|FAIL
```

If integration exposes a new mathematical gap, do not force PASS; reopen/split the relevant dependency.

Exit:

```text
ARITHMETIC_HS_D2_COMPUTED=true
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=true
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=true
STAGE33_07_HOSTILE_REAUDIT=PASS
```

Only then may Stage33-07 close and progress rise from 6/11 to 7/11. Stage33-08 remains blocked until that closure.

## 8. Compact evidence policy — mandatory for 33-12..15

The repository must not accumulate giant expanded generated JSON merely because it is convenient for replay. Exactness and reproducibility are preserved, but expanded machine evidence should normally remain runner-local.

For every new generated certificate whose canonical expanded form is large (default review threshold: about 2,000 lines or 256 KiB), prefer committing this compact interface instead:

```text
SOURCE_LOCKS = immutable input paths/SHAs needed for reconstruction
GENERATOR = deterministic repo script + invocation/version
CANONICAL_SHA256 = digest of the complete regenerated canonical output
SEMANTIC_SUMMARY = dimensions/shapes/counts/basis labels/coverage/UNKNOWN count
EXIT_RELEVANT_INVARIANTS = exact fields consumed by the next child
REGEN_COMMAND = deterministic local/CI reconstruction command
```

Required behavior:

```text
EXPANDED_GENERATED_EVIDENCE_DEFAULT_LOCATION=RUNNER_LOCAL
COMMIT_NEW_GIANT_GENERATED_JSON_BY_DEFAULT=false
COMPACT_CERTIFICATE_REQUIRED=true
REGENERATION_MUST_BE_DETERMINISTIC=true
HASH_MUST_COVER_COMPLETE_CANONICAL_OUTPUT=true
COMPACTION_MUST_NOT_DROP_NEXT_CHILD_LOAD_BEARING_DATA=true
```

Exceptions are allowed only when the expanded object itself contains irreducible load-bearing data that cannot be reconstructed from committed immutable inputs. The exception must be named in the result/handoff with the reason. Existing large Stage33-12 source-lock/certificate files are retained as cold evidence; do not rewrite or delete them merely for size reduction.

CI should regenerate large expanded objects in temporary runner storage, verify their canonical digest and exact invariants, then discard them. Do not upload them as Actions artifacts unless a specific audit/debug need requires it and the repository Actions storage policy permits it.

## 9. Bounded context / handoff policy — mandatory for MAIN

Normal MAIN startup is bounded to:

```text
1. AGENTS.md
2. stages/stage33/controller.json
3. current child roadmap section
4. immediate predecessor handoff/result summary
5. current child's explicitly named compact input certificates
```

While Stage33-05 R5 is reopened, also read:

```text
stages/stage33/ROADMAP-33-05-J2-REPRESENTATIVE-REPAIR.md
stages/stage33/33-05/j2-representative-repair-state.json
stages/stage33/33-05/j2-post-r5-hs-d2-state.json
```

Default prohibitions:

```text
READ_FULL_PR_DIFF_BY_DEFAULT=false
READ_ALL_PRIOR_STAGE_RESULTS_BY_DEFAULT=false
READ_GIANT_JSON_BODY_BY_DEFAULT=false
READ_OLD_ACTIONS_LOGS_BY_DEFAULT=false
RECONSTRUCT_AUDITED_HISTORY_BY_DEFAULT=false
```

Expansion is demand-driven only. Before opening cold/large evidence, record a named reason from this set:

```text
MISSING_LOAD_BEARING_REPRESENTATIVE_OR_MATRIX
SOURCE_LOCK_MISMATCH
CERTIFICATE_CONTRADICTION_OR_MISSING_INVARIANT
HOSTILE_AUDIT_MODE
DEBUGGING_FAILED_DETERMINISTIC_REPLAY
```

When possible, query or regenerate only the needed slice/column/block instead of loading a complete expanded certificate.

Every child closure must produce a compact handoff containing exact status, source hashes, definitions of exported objects, dimensions/counts, unresolved items, next exact leaf, firewalls, and the minimum named files the next child may read.

## 10. Chat/context budget rule

```text
HOT = controller + current roadmap section + current compact handoff + immediate scripts/certificates
WARM = predecessor compact handoff and named interface definitions
COLD = giant generated JSON, old workflow logs, full PR diffs, audited ancestor internals
```

COLD material is not loaded during routine MAIN. If a proof step requires it, load only the named portion, derive/update a compact reusable interface, and return it to COLD status. Repeated rediscovery of the same ancestor detail means the handoff is missing an exported invariant and should be repaired once.

## 11. Visible progress dashboard

During the Stage33-05 hostile reopen, use status rather than the retired Stage33-12 `x/5` counter:

```text
33-05 R5: geometric PASS; arithmetic descent OPEN at actual Cech Pic/2 -> HS d2
33-12: BLOCKED_PENDING_SUCCESSFUL_33_05_R5_EXIT_AND_SUPER_HOSTILE_AUDIT
33-13: BLOCKED_PENDING_33_12_EXACT_CLOSURE; finite-V4 columns x/10 after release
33-14: finite HS cosets x/26; constant 2-primary block OPEN/CLOSED after release
33-15: global assembly state; Q-defined inventory state; hostile recertification state after release
Stage33 progress: 5/11 while 33-05 is reopened
```

Counters are navigational only; exact certificates and audit states remain authoritative.

## 12. Workflow policy

Prefer one lightweight deterministic checkpoint workflow for the current child. Heavy or unreliable external probes are manual or narrowly armed diagnostics, never ordinary PR-synchronized merge gates.

Future 33-13/14 workflows should consume compact handoffs, generate expanded evidence runner-local, and commit only compact deterministic certificates unless a documented irreducible-data exception applies.

## 13. Downstream big tasks

```text
Stage33-40 = original Stage33-09 objective
Stage33-41 = original Stage33-10 objective
Stage33-42 = original Stage33-11 objective
```

Stage33-40 remains blocked until Stage33-08 is actually closed.

## 14. Firewalls and progress transitions

```text
REPAIR_CHILDREN_COUNT_TOWARD_STAGE33_PROGRESS=false
CURRENT_STAGE33_PROGRESS_WHILE_33_05_REOPENED=5/11
SUCCESSFUL_33_05_RECLOSURE_PROGRESS=6/11
SUCCESSFUL_33_07_HOSTILE_RECERTIFICATION_PROGRESS=7/11
STAGE33_12_CLOSE_BEFORE_33_05_R5_SUCCESS=false
STAGE33_13_RELEASE_BEFORE_33_12_CLOSED=false
STAGE33_08_RELEASE_BEFORE_33_07_CLOSED=false
THEOREM_CREDIT=false_UNLESS_SEPARATELY_AUTHORIZED
ENDPOINT_CREDIT=false_UNLESS_SEPARATELY_AUTHORIZED
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Operational PASS, CI success, a materialized Kummer column, a geometric-only J2 result, or closure of one repair child never by itself promotes parent Stage33-07 credit.
