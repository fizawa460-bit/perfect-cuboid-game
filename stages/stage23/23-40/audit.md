# Stage23-40 fresh re-audit

Status: **FAIL**

The Q03 repair is mathematically accepted. The false claim `(t,w)=(0,1)` was introduced only at checkpoint40; it is not present in the audited checkpoint30 source. Checkpoint30 correctly stated only that the quartic is genus one, that a finite scan found no hits, and that the arithmetic remained open.

However, the later mod-8 argument reveals that checkpoint30 stopped too early: the same displayed equation already implies the global integer obstruction

\[
(t^2+1)(t^2+2t+2)\equiv2\pmod8
\]

for every integer `t`. Therefore checkpoint30 was not mathematically false, but its attack ledger is retrospectively superseded from `FINITE_ZERO_HIT_DIAGNOSTIC` to `GLOBAL_INTEGER_SLICE_EXCLUSION`. Before checkpoint40 can pass, this stronger conclusion must be propagated backward as an explicit Stage23-30 addendum/supersession record so future agents do not treat the genus-one slice as an unresolved elliptic-rank gate.

The checkpoint40 authoritative result and PR body must also remove the stale `(0,1)` rational-point statement and the stale `LIVE_ARITHMETIC_GATE` classification.

Q06 independently remains incomplete. The prior audit required opening the actual Stage14/15 sources behind Q06, importing the `(4,4)` receiver into Stage23 variables, and pushing the physical `d<=B` height and multiplicity relation to the first genuinely unavailable theorem/inequality. Saying only that the receiver package is not materialized in the Stage23 interface is insufficient because the selected weapon lives upstream in Stage14/15 and must actually be opened before it can be declared blocked.

No Stage30 PASS revocation is required: its stated theorem and finite-scan claims were valid. What is required is retrospective strengthening/provenance synchronization plus the remaining Q06 source-level execution.

```text
AUDIT_VERDICT=FAIL
AUDIT_PERSISTENCE_STATUS=COMMITTED
UNSYNCED_AUDIT_STATE=NONE
ADVANCE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=40
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=false
REPAIR_SCOPE=Q06_SOURCE_LEVEL_EXECUTION_PLUS_Q03_RETROSPECTIVE_PROPAGATION
Q03_FALSE_CLAIM_ORIGIN=CHECKPOINT40_ONLY
STAGE30_MATHEMATICS_FALSE=false
STAGE30_ATTACK_DEPTH_RETROSPECTIVELY_INCOMPLETE=true
STAGE30_SUPERSESSION_ADDENDUM_REQUIRED=true
STAGE30_NEW_STATUS_FOR_SLICE=GLOBAL_INTEGER_EXCLUSION_BY_MOD8
Q03_RESULT_AND_PR_BODY_SYNC_REQUIRED=true
Q06_SOURCE_ATTACK_IDS_MUST_BE_OPENED=true
Q06_ACTUAL_RECEIVER_MAP_REQUIRED=true
Q06_HEIGHT_MULTIPLICITY_PUSH_REQUIRED=true
Q04_Q11_ACTIVATION_DEFERRED=true
ZERO_DENSITY_MATHEMATICS_REOPEN_REQUIRED=false
```
