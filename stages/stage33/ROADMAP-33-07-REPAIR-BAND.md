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

Stage33-08 exposed a deep Stage33-07 arithmetic Hochschild--Serre / global Gersten descent repair. Stage33-07 remains the blocked parent big task, while repair execution proceeds through coarse child stages.

Closed exact repair children:

```text
33-09 PICARD-EQUIVARIANT-TRANSPORT = CLOSED_EXACT
33-10 ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER = CLOSED_EXACT_HOSTILE_AUDIT_PASS
33-11 ARITHMETIC-LOCALIZATION-CONNECTING-MAP = CLOSED_EXACT_HOSTILE_AUDIT_PASS
33-11 connecting columns = 26/26 exact, unresolved 0
```

The former single Stage33-12 mixed too many independent kernels. The remaining repair is split into four human-trackable children:

```text
33-12 = J2 / marked-Kc / Kummer glue
33-13 = finite-V4 75x10 Kummer matrix
33-14 = 26 finite HS cosets + two-primary constant block
33-15 = global arithmetic HS assembly + Stage33-07 hostile recertification
```

Repair children do not change the 11-big-task denominator. Only hostile-audited closure of parent Stage33-07 changes progress from 6/11 to 7/11.

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

## 4. Stage33-12 — J2-MARKED-KC-KUMMER-GLUE

Purpose: finish the named J2 bridge from the branch-normalization half-divisor through the pinned marked Stoll Kc resolution into the exact Kc Picard discriminant/Brauer 2-torsion coordinate. This child stops before the full 75x10 finite-V4 Kummer matrix.

Current checkpoint:

```text
1/5 named J2 half-divisor and CV support adapter                 DONE
2/5 pinned Stoll branch/support identification                  DONE
3/5 infinity exceptional geometric attachment                  DONE
4/5 ptsK index + qPicK exceptional coordinate                  OPEN
5/5 branch-Jacobian 2-torsion -> Kc discriminant Kummer glue   OPEN
VISIBLE_PROGRESS=3/5
```

Exit:

```text
J2_INFINITY_STOLL_PTSK_ORDER_INDEX_MATERIALIZED=true
J2_INFINITY_QPICK_EXCEPTIONAL_COORDINATE_MATERIALIZED=true
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=true
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=true
J2_KC_KERNEL_LINE_FIXED=true
STAGE33_12_CLOSED_EXACT=true
```

Remote Magma may be used as a manual diagnostic, but unreliable remote execution is not a PR merge gate. Exact closure requires a deterministic retained certificate.

## 5. Stage33-13 — FINITE-V4-KUMMER-MATRIX

Purpose: materialize the finite-V4 Kummer restriction on the full-surface proper Br[2] receiver.

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

Only then may Stage33-07 close, progress become 7/11, and Stage33-08 be released.

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

The mathematical breadth of Stage33 does not require every MAIN batch to reread the breadth. Each closed child must expose a small interface sufficient for the next child.

Normal MAIN startup is bounded to:

```text
1. AGENTS.md
2. stages/stage33/controller.json
3. current child roadmap section
4. immediate predecessor handoff/result summary
5. current child's explicitly named compact input certificates
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

Every child closure must produce a compact handoff containing: exact status, source hashes, definitions of exported objects, dimensions/counts, unresolved items, next exact leaf, firewalls, and the minimum named files the next child may read. Target handoff size is small enough for a fresh chat to understand the current mathematical interface without reconstructing the branch history.

## 10. Chat/context budget rule

Context size is an engineering constraint, not a reason to weaken mathematics. Stage33 MAIN should optimize for a bounded working set:

```text
HOT = controller + current roadmap section + current compact handoff + immediate scripts/certificates
WARM = predecessor compact handoff and named interface definitions
COLD = giant generated JSON, old workflow logs, full PR diffs, audited ancestor internals
```

COLD material is not loaded during routine MAIN. If a proof step requires it, load only the named portion, derive/update a compact reusable interface, and return it to COLD status. Repeatedly rediscovering the same ancestor detail is a signal that the handoff is missing an exported invariant and should be repaired once.

This rule applies equally when the mathematics spans K3 surfaces, Picard lattices, Galois cohomology, Gersten localization, Kummer theory, and Brauer groups: cross-field dependencies should be represented by explicit small adapters/interfaces rather than by keeping all source derivations in the active context.

## 11. Visible progress dashboard

Every MAIN checkpoint exposes one compact line:

```text
33-12: J2/Kummer glue milestones x/5
33-13: finite-V4 Kummer matrix columns x/10
33-14: finite HS cosets x/26; constant 2-primary block OPEN/CLOSED
33-15: global assembly state; Q-defined inventory state; hostile recertification state
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

## 14. Firewalls

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