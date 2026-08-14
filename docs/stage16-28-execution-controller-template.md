# Stage16-28 Main / Audit / Codex Execution Template

Status: **common operating template for Stage16-28**.

This document generalizes the Stage15 operating pattern into a reusable research controller. The intended human interface is deliberately small: provide the parent stage and invoke the main batch or audit command. The controller owns checkpoint discovery, safe batching, Codex delegation, audit routing, artifact materialization, and advancement.

## Canonical user commands

```text
StageX-main-batch
StageX-audit
```

## Parent-stage contract

Each parent stage declares population/source/target/common cutoff and checkpoint sequence `10,20,30,40,50,60,70`. Checkpoint meanings are fixed by `docs/stage16-28-population-roadmap.md`.

## Main-batch core rule

Each `StageX-main-batch` reads controller state, performs repository-wide reuse preflight, reuses compatible audited results before new work, executes the current checkpoint, persists artifacts, decides Codex delegation, and stops at audit or a genuine research boundary. The main lane may submit work but never self-awards mathematical audit PASS.

## Repository-wide reuse preflight

Before a new theorem/proof/construction or strongest-known claim, search arsenal, numerical index, stages, supplements, archives, and historical PRs. Absence from the curated arsenal never proves absence from the repository.

Required markers include:

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true|false
NEW_RESEARCH_JUSTIFIED=
```

## Audit lane

`StageX-audit` independently checks population/cutoff/multiplicity contracts, evidence levels, mathematics, verifier coverage, reuse state, and closeout artifacts. It returns `PASS|FAIL|BLOCKED` with explicit advancement markers. A concrete bounded repair returns to `StageX-main-batch`.

## Automatic checkpoint advancement

After a non-70 checkpoint audit PASS, the controller advances to the next unresolved checkpoint. Routine certified checkpoints may be batched when no unaudited premise would be consumed.

## Stage70 artifact materialization gate

Stage70's declarations are **obligations, not classifications only**.

If Stage70 says

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
```

then the required bundle must be created and persisted before Stage70 can receive final closeout PASS.

If Stage70 says

```text
ARSENAL_PROMOTION_REQUIRED=YES
```

then every declared candidate must be materialized as a portable contract in the repository before Stage70 can receive final closeout PASS. A `YES` flag plus candidate names is not completion.

Required state:

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES|NO
SELF_CONTAINED_BUNDLE_PRESENT=true|false|NOT_REQUIRED
SELF_CONTAINED_BUNDLE_PATH=
ARSENAL_PROMOTION_REQUIRED=YES|NO
ARSENAL_PROMOTION_PRESENT=true|false|NOT_REQUIRED
ARSENAL_PROMOTION_PATHS=
ARSENAL_PROMOTION_IDS=
MANIFEST_PRESENT=true|false
POST_AUDIT_PROMOTION_PENDING=true|false
```

Preferred ordering is to assemble candidate bundle/promotions during Stage70 main-batch and then audit the complete closeout surface once. If an audit determines that a promotion must be changed, the repair stays at checkpoint70 until the materialized artifact is re-audited.

A controller must never emit `NEXT_STAGE=StageY` as actionable advancement while a required bundle, manifest, or arsenal promotion is absent.

## Automatic parent-stage advancement

A parent stage may close only when all of the following are true:

1. checkpoints 10-70 have explicit statuses;
2. Stage70 mathematical synthesis has audit PASS;
3. population/comparison safety checks are complete;
4. dependency/evidence ledgers are complete;
5. required self-contained bundle is physically present and audited, or explicitly not required;
6. required arsenal promotions are physically present and audited, or explicitly not required;
7. manifest/current-status/controller closeout surfaces agree;
8. no unfinished internal route is mislabeled as an external OPEN_GATE.

Only then may the controller record:

```text
STAGE_STATUS=CLOSED
ADVANCE_ALLOWED=true
NEXT_STAGE=StageY
POST_AUDIT_PROMOTION_PENDING=false
```

If required artifact materialization is missing, the state must instead be:

```text
STAGE_STATUS=OPEN
CURRENT_CHECKPOINT=70
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_STAGE=
NEXT_EXPECTED_COMMAND=StageX-main-batch
```

## Historical promotion debt check

Because earlier Stage16-28 runs may predate this enforcement, repository maintenance should periodically scan closed stages for

```text
ARSENAL_PROMOTION_REQUIRED=YES
```

without a corresponding materialized promotion artifact. Such cases are `PROMOTION_DEBT`, not reasons to invalidate already-audited mathematics. They should be repaired as bounded bookkeeping/toolbox work.

## Repair loop

```text
main-batch -> submitted -> audit FAIL -> bounded repair -> main-batch -> audit
```

Repairs preserve the audited mathematical target unless the audit found the theorem itself invalid.

## Numerical reuse preflight

Before launching a new census, inspect `docs/stage14-num-reuse-index.md`; reuse a compatible frozen artifact or certify why a new computation is necessary. Finite evidence never upgrades itself to theorem status.

## Stage21-28 exploration gate

For Stage21-28, formulas are starting points rather than default stops. Required discovery layers and sublane decisions follow `docs/stage21-28-exploration-policy.md`. Incomplete exploration evidence blocks advancement even when the first formula is correct.

## Minimal closeout handoff

```text
STAGE_STATUS=CLOSED|OPEN|BLOCKED
AUDIT_VERDICT=PASS|FAIL|BLOCKED|PENDING
ADVANCE_ALLOWED=true|false
NEXT_STAGE=
SELF_CONTAINED_BUNDLE_REQUIRED=YES|NO
SELF_CONTAINED_BUNDLE_PRESENT=true|false|NOT_REQUIRED
ARSENAL_PROMOTION_REQUIRED=YES|NO
ARSENAL_PROMOTION_PRESENT=true|false|NOT_REQUIRED
POST_AUDIT_PROMOTION_PENDING=true|false
NEW_INPUT_REQUIRED=true|false
HUMAN_DECISION_REQUIRED=true|false
```

## Design principle

The controller is a research state machine, not merely a status classifier. When it decides that an artifact is required, it must ensure that artifact is actually materialized before allowing parent-stage advancement.
