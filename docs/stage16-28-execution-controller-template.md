# Stage16-28 Main / Audit / Codex Execution Template

Status: **common operating template for Stage16-28**.

This document generalizes the Stage15 operating pattern into a reusable research
controller. The intended human interface is deliberately small: provide the parent
stage and invoke the main batch or audit command. The controller owns checkpoint
discovery, safe batching, Codex delegation, audit routing, and advancement.

## Canonical user commands

For any parent stage `StageX`:

```text
StageX-main-batch
StageX-audit
```

These are the normal entry points. The user should not need to invent a new prompt
for each `X-10`, `X-20`, ..., `X-70` checkpoint.

A stage-specific controller may expose a repair command when necessary, but the
main/audit pair remains the canonical interface.

## Parent-stage contract

Each Stage16-28 parent must declare at least:

```text
PARENT_STAGE=StageX
PARENT_CLASS=population_state|transition|interaction_synthesis
STAGE_OBJECT=
SOURCE_POPULATION=
TARGET_POPULATION=
COMMON_POPULATION_CONTRACT=
CHECKPOINT_SEQUENCE=10,20,30,40,50,60,70
```

The common checkpoint meanings come from
`docs/stage16-28-population-roadmap.md` and must not be silently redefined by an
individual controller.

## Controller state

The controller should persist a compact machine-readable state:

```text
CURRENT_STAGE=StageX
CURRENT_CHECKPOINT=10|20|30|40|50|60|70
MAIN_STATUS=READY|IN_PROGRESS|SUBMITTED|BLOCKED|COMPLETE
AUDIT_STATUS=PENDING|PASS|FAIL|BLOCKED|NOT_REQUIRED
ADVANCE_ALLOWED=true|false
NEXT_CHECKPOINT=
NEXT_STAGE=
NEW_INPUT_REQUIRED=true|false
HUMAN_DECISION_REQUIRED=true|false
```

The controller, not the chat user, is responsible for discovering the next
checkpoint from repository state.

## `StageX-main-batch`

The main batch is the research/build lane. On each invocation it should:

1. read the parent-stage contract and current controller state;
2. discover which checkpoint outputs are already certified and which are pending;
3. run the repository-wide reuse preflight in
   `docs/stage16-28-reuse-preflight.md`, including arsenal, numerical index,
   stage/supplement/archive files, and historical PR discovery, before opening
   new work;
4. reuse verified literature, earlier stages, and compatible prior results before
   opening new work;
5. execute the current checkpoint and, when safe, continue through additional
   checkpoints in the same batch;
6. create or update the required result, verifier, manifest, data, or proof files;
7. decide whether Codex should be delegated a bounded implementation/repository
   task;
8. stop at the first boundary that requires audit, new mathematical input, human
   policy choice, incompatible population repair, or unresolved external gate;
9. emit a standardized handoff for the audit lane.

The arsenal is a curated fast index, not a complete inventory. A result's absence
from the arsenal does not justify re-proving it. In particular, checkpoints that
claim a strongest bound, best construction, absent theorem, new mechanism, or
`OPEN_GATE` must first verify that no stronger compatible audited result is lying
in a prior stage, supplement, archive, or historical PR.

### Safe multi-checkpoint batching

A single main-batch invocation may complete several checkpoints, for example
`10 -> 20 -> 30`, when each step is already supported by verified inputs and no
intermediate result needs an independent decision before the next step can be
constructed.

Batching must stop when proceeding would cause the next result to depend on an
unaudited novel claim. The goal is fast advancement through routine/known work,
not elimination of the independent audit boundary.

The main lane may mark work `SUBMITTED`; it must not self-award the final audit
PASS for a nontrivial mathematical result.

## Repository-wide reuse preflight

The normative discovery contract is
`docs/stage16-28-reuse-preflight.md`.

Before submitting a checkpoint, the main lane must emit:

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=<IDs/paths/PRs or NONE>
REUSE_MATCH_STATUS=EXACT|ADAPTER_PROVED|MIXED|NO_MATCH
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true|false
NEW_RESEARCH_JUSTIFIED=<reason or NOT_REQUIRED>
```

This is mandatory for new theorem/proof/construction work as well as for claims
that a checkpoint records the strongest currently certified project result. If a
later search discovers a stronger audited result after an earlier PASS, preserve
the older valid theorem as provenance and supersede only the strongest-known
metadata or strengthened claim that actually changed.

## Codex delegation rule

Codex participation follows the Stage15 pattern. The main controller decides when
Codex is useful and emits a complete, bounded task instead of requiring the user
to design the Codex prompt.

Required delegation fields:

```text
CODEX_REQUIRED=true|false
CODEX_REASON=
CODEX_TASK=
CODEX_SCOPE=
CODEX_MAY_EDIT=
CODEX_MUST_NOT_EDIT=
CODEX_EXPECTED_OUTPUT=
CODEX_VALIDATION=
CODEX_AUDIT_REQUIRED=true|false
```

Good Codex targets include:

- repository/controller/manifest repair;
- verifier or enumerator implementation;
- deterministic data generation and replay tooling;
- repetitive file migrations or archive/index maintenance;
- self-contained bundle assembly after the mathematical claims are frozen;
- CI/workflow support needed to validate a bounded research artifact.

Codex must not be treated as the final authority merely because it produced an
artifact. New mathematical claims, changed population contracts, theorem-transfer
steps, and causal conclusions remain subject to the normal main/audit evidence
rules.

### Returning Codex work

When Codex work is present, the next main-batch invocation records:

```text
CODEX_RESULT_PRESENT=true
CODEX_RESULT_ACCEPTED=true|false
CODEX_RESULT_USED_AS=
CODEX_FILES=
CODEX_COMMIT_OR_PR=
CODEX_DEPENDENCIES=
```

Rejected or partial Codex work must not silently become a stage premise.

## `StageX-audit`

The audit lane is independent of the main lane. It inspects the submitted
checkpoint/batch against the frozen population contract, evidence level,
dependencies, mathematical claims, verifier coverage, reuse-preflight state, and
stage-specific exit criteria.

The audit must end with standardized markers:

```text
AUDIT_VERDICT=PASS|FAIL|BLOCKED
ADVANCE_ALLOWED=true|false
NEW_INPUT_REQUIRED=true|false
HUMAN_DECISION_REQUIRED=true|false
NEXT_CHECKPOINT=
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=true|false
CODEX_REASON=
```

### Audit semantics

`PASS` means the submitted scope is certified and the controller may advance.

`FAIL` means a concrete repair is available from existing inputs. The audit should
state the smallest repair scope and route it back to the main lane. It must not
weaken a theorem or silently change the population contract merely to obtain PASS.

`BLOCKED` means the missing input is external, mathematically open, or requires a
human policy choice. It should identify the exact blocker. If the checkpoint is a
valid audited `OPEN_GATE`, the checkpoint can still count as classified under the
roadmap's closure rule, but the blocked research route must not be repeatedly
reopened without new input.

A missing repository-wide reuse preflight does not automatically falsify a theorem
proved inside the checkpoint. It does block unsupported metadata claims such as
`STRONGEST_CERTIFIED_*`, `BEST_*`, `NO_KNOWN_*`, or an `OPEN_GATE` justified by
asserting that no prior compatible project result exists.

## Automatic checkpoint advancement

After audit PASS, the controller advances to the next unresolved checkpoint.
Routine completed checkpoints may be skipped automatically.

Example:

```text
CURRENT_STAGE=Stage16
AUDITED_THROUGH=30
NEXT_CHECKPOINT=40
```

If the next main batch can certify 40 and 50 from existing literature or reusable
weapons, it may submit both in one batch, after which `Stage16-audit` audits that
submitted scope.

The user therefore normally alternates only:

```text
Stage16-main-batch
Stage16-audit
Stage16-main-batch
Stage16-audit
```

rather than manually naming every subtask.

## Automatic parent-stage advancement

A parent stage may close only when:

1. checkpoints 10-70 all have explicit roadmap statuses;
2. StageX-70 closeout has an audit PASS;
3. population-contract and comparison safety checks are complete;
4. dependency and evidence ledgers are complete;
5. required self-contained bundle work is either complete or explicitly not
   required;
6. required arsenal promotions are complete or explicitly not required;
7. no unfinished internal route is being mislabeled as an external `OPEN_GATE`.

Then the controller records:

```text
STAGE_STATUS=CLOSED
ADVANCE_ALLOWED=true
NEXT_STAGE=StageY
```

The next invocation uses the next parent controller. Stage numbering follows the
roadmap rather than assuming every mathematical relation is a linear chain.

## Repair loop

When audit returns FAIL:

```text
main-batch -> submitted result -> audit FAIL -> bounded repair -> main-batch -> audit
```

The repair should preserve the audited mathematical target. Controller/discovery
repairs may change manifests, paths, markers, or verifier discovery without
weakening the underlying mathematical verifier unless the audit explicitly found
the mathematical statement itself invalid.

## Stop conditions

Automatic advancement stops when any of the following is true:

```text
NEW_INPUT_REQUIRED=true
HUMAN_DECISION_REQUIRED=true
POPULATION_CONTRACT_CHANGED=YES
COMPARISON_ADAPTER_REQUIRED=YES   # until adapter is certified
AUDIT_VERDICT=FAIL|BLOCKED        # unless the exact roadmap closure semantics permit classification
```

The controller must prefer a clean stop over inventing a new internal route.

## Minimal main-batch handoff

Every main batch should finish with a compact machine-readable handoff similar to:

```text
MAIN_BATCH_STATUS=SUBMITTED|BLOCKED|COMPLETE
CURRENT_STAGE=StageX
CHECKPOINTS_ATTEMPTED=
CHECKPOINTS_SUBMITTED=
NEW_CLAIMS=
REUSED_WEAPONS=
REPO_REUSE_PREFLIGHT=PASS
STRONGEST_KNOWN_CHECK=PASS
CODEX_REQUIRED=true|false
CODEX_REASON=
AUDIT_REQUIRED=true|false
NEXT_EXPECTED_COMMAND=StageX-audit|StageX-main-batch|human-input
```

## Minimal stage-close handoff

At the end of StageX-70:

```text
STAGE_STATUS=CLOSED|OPEN_GATE_CLASSIFIED|BLOCKED
AUDIT_VERDICT=PASS|FAIL|BLOCKED
ADVANCE_ALLOWED=true|false
NEXT_STAGE=
SELF_CONTAINED_BUNDLE_REQUIRED=YES|NO
ARSENAL_PROMOTION_REQUIRED=YES|NO
NEW_INPUT_REQUIRED=true|false
HUMAN_DECISION_REQUIRED=true|false
```

## Design principle

The objective is not unattended autonomous research. It is a controlled research
state machine in which routine advancement is automated, Codex work is delegated
when appropriate, and independent audit remains the gate for new mathematical
claims. The human operator supplies the parent command and intervenes only when a
real research or policy boundary is reached.

### Numerical reuse preflight

Before launching a new census or finite diagnostic, the main lane must inspect `docs/stage14-num-reuse-index.md`. It must reuse a compatible frozen artifact, prove an exact population/intersection adapter, or state why no match exists. The handoff must emit:

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=<IDs or NONE>
NUM_POPULATION_MATCH=<EXACT | ADAPTER_PROVED | NO_MATCH>
NUM_EVIDENCE_LEVEL=<level or NOT_APPLICABLE>
NUM_NEW_COMPUTATION_JUSTIFIED=<reason or NOT_REQUIRED>
```

This numerical preflight is a specialized subset of the repository-wide reuse
preflight. It prevents duplicate computation but never upgrades finite evidence
into a theorem. Missing the numerical preflight blocks a newly proposed
computation; it does not reopen already audited mathematics.

## Stage21–28 exploration-evidence controller gate

For Stage21–28, checkpoint discovery is cumulative. Before submitting checkpoint `X`, the controller must verify every discovery ledger scheduled at or before `X`. Checkpoints30–60 also require the sublane decision ledger defined in `docs/stage21-28-exploration-policy.md`.

The main handoff must include:

```text
EXPLORATION_EVIDENCE_COMPLETE=true|false
DISCOVERY_CHECKPOINTS_COMPLETE=<list>
MANDATORY_LAYERS_CLASSIFIED=true|false
LIVE_ROUTE_CANDIDATES=<list or NONE>
SUBLANES_OPENED=<list or NONE>
SUBLANES_REJECTED_WITH_REASON=<route: reason or NONE_WITH_REASON>
DISCOVERY_AUDIT_REQUIRED=true|false
DISCOVERY_AUDIT_REASON=<reason>
DISCOVERY_AUDIT_VERDICT=PASS|FAIL|BLOCKED|NOT_REQUIRED
```

The audit lane must sample the recorded paths, structural signatures, dependency neighbors, accepted candidates, and rejection reasons. It must not accept bare `PASS` markers without a persisted discovery ledger.

If evidence is incomplete, a required discovery audit is absent, or its verdict is not PASS:

```text
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StageX-main-batch
```

This enforcement applies even if the checkpoint's mathematical formula is correct. It protects the Stage21–28 requirement that the first visible formula is a starting point rather than the default stopping point.

### Sublane identifier validation

Before opening or auditing a Stage21–28 research sublane, the controller must validate its identifier against `docs/stage21-28-exploration-policy.md`:

```text
SUBLANE_NAMING_CHECK=PASS|FAIL
TASK_ID=Stage<owner>[-u<source>]-r<PSS><branch>
OWNER_STAGE_MATCH=true|false
TRIGGER_CHECKPOINT_MATCH=true|false
ROUTE_SERIAL_UNIQUE=true|false
UPSTREAM_TARGET_RECORDED=true|false|NOT_APPLICABLE
```

A failed naming check blocks creation of the sublane artifact but does not block unrelated parent-checkpoint work. Renaming never changes mathematical provenance: the old identifier must remain recorded as an alias if it was already cited or audited.
