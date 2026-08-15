# Stage25 audited closeout → reentry synchronization

STATUS=REPAIRED_AFTER_FRESH_AUDIT_FAIL_PENDING_REAUDIT

PR #1000 received hostile checkpoint70 audit PASS and was merged as `12e1cb027e3123328702393ebdb3e3687ca0a169`.

This synchronization performs no new mathematics. It only materializes the already-authorized state transition:

```text
STAGE25_MAIN_STATUS=CLOSED
CHECKPOINT70_STATUS=PROVED_AUDITED_PASS
STAGE25_CLASS=THIN_BUT_POSITIVE_POWER_INFINITE
STAGE25_REENTRY_UNLOCK_CONDITION=SATISFIED
CURRENT_REENTRY_PHASE=10
REENTRY_PHASE10_STATUS=READY_PENDING_SYNC_AUDIT
STAGE26_ALLOWED=false
```

Canonical theorem state remains unchanged:

- `M1(B) ~ 3/(4*pi^2) B^2 log B`;
- `B^(1/4) << N2(B) <<_epsilon B^(1/2+epsilon)`;
- `N2/M1 -> 0` and `N2(B) -> infinity`;
- `I >> B^(1/4)(log B)^(-7) -> infinity`;
- exponent `1/4` is not claimed optimal;
- no perfect-cuboid existence/nonexistence conclusion.

The synchronization updates:

- `stages/stage25/25-controller.json` to checkpoint70 audited CLOSED while preserving all prior checkpoint history;
- `stages/stage25/25-70/controller.json` to record the actual closeout merge and satisfied reentry condition;
- `stages/stage25/25-reentry-controller.json` so phase10 is READY pending sync re-audit;
- the reentry verifier and checkpoint70 closeout verifier so both understand the post-merge synchronization lifecycle.

## Fresh audit failure and bounded repair

The first fresh audit of PR #1001 is preserved as FAIL:

```text
AUDIT_VERDICT=FAIL
FAIL_REASON=STAGE25_70_CLOSEOUT_CI_REGRESSION
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
STAGE25_STATUS=CLOSED
CHECKPOINT70_STATUS=PROVED_AUDITED_PASS
REENTRY_PHASE10_STATUS=READY_PENDING_SYNC_AUDIT
STAGE26_ALLOWED=false
```

The failure was not mathematical. `Stage25 reentry roadmap contract` succeeded, but `Stage25-70 closeout audit` failed at the stale assertion

`assert c70["stage25_reentry_unlocked"] is False`.

That assertion was correct for submission and pre-merge states but wrong after PR #1000 had been audited PASS and merged.

The bounded repair makes the checkpoint70 verifier lifecycle-aware. It now validates all three legitimate states:

1. closeout submission: `PENDING`, unmerged, reentry blocked;
2. hostile-audit PASS awaiting merge: `PASS`, unmerged, reentry blocked;
3. post-merge synchronization: `PASS`, merged, canonical Stage25 `CLOSED`, phase10 `READY_PENDING_SYNC_AUDIT` or `READY`, Stage26 still blocked.

The reentry verifier is likewise state-aware for the intermediate `READY_PENDING_SYNC_AUDIT` state so the recorded FAIL cannot be bypassed merely because the closeout merge condition is satisfied.

No theorem, route boundary, population contract, reentry ordering, or Stage26 gate changed.

No reentry research phase is executed here. Per `docs/stage25-reentry-operations.md`, phase10 itself is executed only by:

`Stage25-reentry-main-batch`

after this synchronization receives fresh audit PASS and is merged.

```text
AUDIT_STATUS=PENDING_REAUDIT
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
```
