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
- `stages/stage25/25-reentry-controller.json` so phase10 is READY;
- the existing reentry verifier so it accepts both the historical blocked state and the post-closeout READY state, and cross-checks the checkpoint70 audit/merge evidence.

## Fresh audit failure and bounded repair

The first fresh audit of PR #1001 is intentionally preserved as FAIL:

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

The failure was not mathematical. `Stage25 reentry roadmap contract` succeeded, but `Stage25-70 closeout audit` failed because `stages/stage25/25-70/closeout_audit.py` still required `stage25_reentry_unlocked=false` after the audited closeout had already been merged and the synchronization correctly set it to `true`.

The bounded repair makes the closeout verifier lifecycle-aware. It now validates all three legitimate states:

1. closeout submission: `PENDING`, unmerged, reentry blocked;
2. hostile-audit PASS awaiting merge: `PASS`, unmerged, reentry blocked;
3. post-merge synchronization: `PASS`, merged, canonical Stage25 `CLOSED`, phase10 `READY`, Stage26 still blocked.

No theorem, route boundary, population contract, or reentry ordering changed.

No reentry research phase is executed here. Per `docs/stage25-reentry-operations.md`, phase10 itself is executed only by:

`Stage25-reentry-main-batch`

Fresh re-audit of this synchronization is required before merge.

```text
AUDIT_STATUS=PENDING_REAUDIT
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
```
