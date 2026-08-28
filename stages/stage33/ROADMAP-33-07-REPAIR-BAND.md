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

Stage33-08 exposed a deep Stage33-07 arithmetic Hochschild--Serre / global Gersten descent repair. PR #1430 already pushed the geometric side far forward: the intrinsic 14-dimensional A[2] module, actual coordinate-swap pair, exact S3/seven-sign relations, named cc/ct compatibility, intrinsic-to-retained A[2] transport, and mixed-order divisibility filtration were all materially established. The remaining repair is therefore not a restart of Stage33-07.

The unresolved chain is now concentrated in four coarse child stages: finish the historical retained Picard marking bridge; identify the correct absolute G_Q cohomology receiver; compute the arithmetic localization connecting map for all 26 source directions; then assemble arithmetic HS and hostile-recertify Stage33-07.

Keeping all of this inside `33-07` makes the unit too large to audit and causes the historical `stage33-07-*` workflow family to re-fire unrelated leaves. Stage33-07 remains the blocked parent big task, while repair execution moves to coarse child stages beginning at 33-09.

## 2. Numbering policy

```text
OLD 33-09 -> NEW 33-40  complete relevant-place and physical-local-locus certification
OLD 33-10 -> NEW 33-41  exact local evaluation production
OLD 33-11 -> NEW 33-42  physical adelic compatibility, final Brauer verdict, hostile audit
```

The repair may use numbers `33-09..33-39`, but this is only an address space. There is no requirement or intention to fill it. The default plan uses 33-09..33-12 only. New stage numbers are added only if a genuinely new exact subkernel cannot be contained inside the current coarse stage.

Stage33 remains an 11-big-task roadmap. Repair children do not change the denominator or progress count; only hostile-audited closure of parent Stage33-07 changes progress from 6/11 to 7/11.

## 3. Adaptive repair rule

The child roadmap is a decision tree, not a checklist.

```text
ALL_BRANCHES_MUST_RUN=false
FIRST_EXACT_CLOSURE_WINS=true
FAILED_ROUTE_DOES_NOT_AUTHORIZE_NEXT_COARSE_STAGE=true
IF_CURRENT_COARSE_STAGE_DOES_NOT_CLOSE=EXTEND_OR_SPLIT_CURRENT_STAGE
NEXT_COARSE_STAGE_ALLOWED_ONLY_AFTER_CURRENT_EXIT_CONDITION=true
```

A cheap route may close a stage immediately; unused fallback routes then remain unused. If a route fails, continue to the next planned route. If all planned routes fail but the exit condition is still open, add the next justified subroute/subkernel inside that stage rather than advancing merely because the written mini-map was exhausted.

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

The direct replay into the literal historical q256 common-Smith basis produced a negative route result: the locally reconstructed Picard Gram did not certify identity with the historical q256 Gram. That route is diagnostic evidence, not a reason to repeat the whole geometric search.

### Remaining target

Finish the source-locked marked Picard basis bridge from the pinned upstream qPic/INDLIST marking to the historical retained q256 Picard basis, and revalidate the already-known named actions through that bridge.

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

If the marked bridge exposes a genuinely new incompatibility, 33-09 remains open and its mini-map may expand. Otherwise proceed immediately to 33-10.

## 5. Stage33-10 — ABSOLUTE-H1-AND-GALOIS-DESCENT-ADAPTER

Purpose: identify the mathematically correct absolute receiver that Stage33-11 must map into. This is not merely planning for Stage33-11; it is the finite-to-absolute Galois cohomology repair itself.

Known starting point:

```text
finite H^1(V4, proper geometric Br[2]) dimension = 16
absolute H^1(G_Q, proper geometric Br[2]) NOT YET identified with finite V4 H1
```

### Mini-map / route order

#### 33-10a — finite-to-absolute shortcut test
Test whether the already-computed finite V4 receiver is exactly sufficient for the absolute G_Q receiver in this case.

```text
PASS -> jump to 33-10e
FAIL -> 33-10b
```

#### 33-10b — inflation-restriction decomposition
Compute the exact inflation-restriction / kernel-Galois contribution for the map from G_Q to the named finite V4 quotient.

```text
kernel contribution proved zero -> 33-10e
kernel contribution nonzero/undetermined -> 33-10c
```

#### 33-10c — relevant kernel-Galois contribution
Materialize only the kernel contribution that can reach the Stage33 arithmetic receiver; avoid computing irrelevant absolute cohomology.

```text
relevant contribution completely determined -> 33-10e
still insufficient -> 33-10d
```

#### 33-10d — direct absolute H1 construction fallback
Abandon the finite shortcut if necessary and construct the required absolute H1 receiver directly, to the exact extent required for arithmetic localization.

```text
complete -> 33-10e
```

#### 33-10e — absolute receiver certification
Produce the common exit certificate independent of which route succeeded.

Exit condition:

```text
ABSOLUTE_H1_RECEIVER_EXACT=true
FINITE_V4_SHORTCUT_STATUS=PROVED_VALID_OR_EXPLICITLY_REPLACED
KERNEL_GALOIS_RELEVANT_CONTRIBUTION_ACCOUNTED=true
STAGE33_11_DOMAIN_AND_CODOMAIN_WELL_DEFINED=true
```

Not all 10a..10d must run. If a route closes the receiver exactly, unused deeper fallbacks are skipped. Conversely, exhausting 10a..10d without satisfying the exit condition does NOT permit Stage33-11; extend the 33-10 mini-map (10f, 10g, or a new child only if genuinely necessary) until the receiver is exact.

## 6. Stage33-11 — ARITHMETIC-LOCALIZATION-CONNECTING-MAP

Purpose: compute the genuine arithmetic localization connecting map / middle Gersten extension data for all 26 mixed-order source directions, now using the exact receiver certified by Stage33-10.

Starting state inherited from Stage33-07/#1430:

```text
source directions = 26
connecting-map columns explicitly materialized = 0/26
middle Gersten module action not yet materialized
```

The exit condition is coverage, not a prescribed method: all 26 directions must be exact, but they need not be solved one-by-one.

### Mini-map / preferred escalation

#### 33-11a — global/all-at-once closure
Try exact module structure, naturality, symmetry, tensor structure, or an equivalent formula that determines all 26 columns simultaneously.

```text
26/26 exact -> Stage33-11 closes
otherwise -> 33-11b
```

#### 33-11b — orbit/block closure
Exploit cc/ct, sign, symmetry, invariant-factor, or other exact decomposition so representative columns determine whole blocks/orbits.

```text
26/26 exact after block propagation -> Stage33-11 closes
remaining directions -> 33-11c
```

#### 33-11c — individual fallback
Compute remaining unresolved source directions individually or in the smallest exact blocks required.

```text
progress may be 1/26, 3/26, ...
Stage33-11 closes only at exact 26/26 coverage
```

Further routes may be added if a new exact structure appears. The mini-map is adaptive; it does not force all routes to execute and it never authorizes Stage33-12 before complete coverage.

Scope may include, when genuinely required:

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

Purpose: assemble the repaired arithmetic Hochschild--Serre descent using the exact outputs of 33-09/10/11 and decide the parent Stage33-07 unit.

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

Do not manufacture stages to consume the reserved range. Keep work inside 33-09..33-12 unless a coarse phase becomes independently too large or exposes a genuinely new exact subkernel with a clean audit boundary. If that happens, use only the next number actually needed.

Subtask labels such as `33-10a` or `33-11b` are roadmap branches inside the coarse stage; they do not consume new Stage33 unit numbers and do not count toward the 11-task progress denominator.

## 9. Workflow policy

New repair work should stop growing the historical `stage33-07-*` workflow family. Prefer one stage-local workflow per coarse phase, with jobs/matrices or explicitly named subjobs inside it:

```text
.github/workflows/stage33-09-main.yml
.github/workflows/stage33-10-main.yml
.github/workflows/stage33-11-main.yml
.github/workflows/stage33-12-main.yml
```

Heavy/unreliable remote Magma probes should be manual diagnostics instead of PR-synchronized triggers. Historical Stage33-07 workflows remain evidence and need not be renamed or rerun merely because the roadmap changes.

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
UNUSED_FALLBACK_BRANCHES_MUST_RUN=false
MINIMAP_EXHAUSTED_WITHOUT_EXIT_CONDITION_DOES_NOT_ADVANCE=true
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
