# Stage25 reentry operating contract

## Main command

`Stage25-reentry-main-batch` reads `stages/stage25/25-reentry-controller.json` and performs exactly one current phase.

Before phase10 it must verify that canonical Stage25 is audited closed at checkpoint70 and that no unresolved Stage25 repair PR is being bypassed. If not, it returns:

```text
REENTRY_BLOCKED=true
BLOCKER=STAGE25_NOT_AUDITED_CLOSED
NEXT_EXPECTED_COMMAND=Stage25-main-batch
```

For an open phase it must create a dedicated branch and Draft PR, materialize the required phase artifacts, run its verifier, and stop for fresh audit.

## Audit command

`Stage25-reentry-audit` reviews only the submitted current phase and its declared backflow proposals. Audit PASS may advance one phase, but may not merge the PR or auto-execute the next phase.

Required output:

```text
AUDIT_VERDICT=PASS|FAIL
ADVANCE_ALLOWED=true|false
CURRENT_REENTRY_PHASE=
NEXT_REENTRY_PHASE=
LIVE_DERIVED_ROUTES=
QUEUED_PROPAGATION_PROPOSALS=
STAGE26_ALLOWED=true|false
MERGE_ALLOWED=true|false
```

## Discovery-depth rule

The worker must distinguish:

- theorem-interface verification;
- mechanism refinement;
- new construction or bound;
- negative route certification;
- propagation to another stage.

Formula substitution or restating a final bundle is not a completed reentry phase. Conversely, a phase need not force a stronger theorem when every compatible repo-native route has been executed or certified and the remaining gate is genuinely external.
