# Stage25-reentry r010a hostile audit

AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
ROUTE_ID=Stage25-um-r010a
PR=1008

The receiver synchronization is accepted. Stage18 receives the exact raw-pair identity and directional postfilter-to-one theorem; Stage20 receives the relative `M3/M2,j` decay without changing its absolute M3 envelope; Stage22 receives the directional `(log B)^4/B` transition constants and directional mass shares.

The fine-mechanism gate remains open. The audit accepts only the narrowing: directional averaging, the third-face nonsquare postfilter, and the common canonical/primitivity/cutoff interface are not the leading source of the four-log compensation. No decomposition into four independent local/arithmetic factors is proved.

Submission head `8e46dd81fb4806da71dc2e13dc6a82328aee6f1e` has SUCCESS for the dedicated `Stage25 reentry r010a two-face backflow` workflow and the relevant Stage25 reentry regression workflows. The recurring Stage15-8 workflow failure is unrelated to this Stage25 audit scope.

The verifier was made audit-state aware so the submission PENDING state and the audited PASS-awaiting-merge state are both valid lifecycle states. Phase50 remains blocked until PR #1008 merges.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
R010A_STATUS=AUDITED_PASS_AWAITING_MERGE
ADVANCE_ALLOWED=true
CURRENT_REENTRY_PHASE=40
NEXT_REENTRY_PHASE=50
PHASE50_ALLOWED_BEFORE_MERGE=false
MERGE_ALLOWED=true
STAGE26_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #1008; then Stage25-reentry-main-batch
```
