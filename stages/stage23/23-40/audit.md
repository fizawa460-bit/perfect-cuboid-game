# Stage23-40 fresh re-audit

Status: **FAIL**

The Q03 repair is accepted. The previous rational-point claim `(t,w)=(0,1)` is correctly retracted in `deep-execution-q03-q06.md`, and the integral pullback is now resolved by a genuine global congruence obstruction:

\[
(t^2+1)(t^2+2t+2)\equiv 2\pmod 8
\]

for every integer `t`, hence the selected consecutive-parameter slice has no Stage19 hits. No finite scan is needed. Therefore Q03 has reached its internal boundary for this slice.

Q06 has not yet satisfied the prior repair instruction. The previous audit explicitly required deriving the available Stage14/15 `(4,4)` receiver in Stage23 variables and pushing the physical `d<=B` height/multiplicity comparison as far as the repository permits. The repair instead concludes that no concrete receiver equation/height/count package is materialized in the Stage23 interface. That identifies a missing interface, but it does not execute the selected reusable Stage14/15 weapon itself. Before Q06 can be marked internally exhausted, the source attack IDs/files behind Q06 must be opened and the actual receiver equation, variable map, physical-height relation, and multiplicity information must be imported or rejected with a precise incompatibility proof.

There is also a consistency defect: `stages/stage23/23-40/result.md` and the PR body still contain the now-retracted false statement that `(t,w)=(0,1)` is a rational point and still classify Q03 as a live elliptic-rank gate. The authoritative checkpoint result must be synchronized to the corrected mod-8 obstruction before merge.

No breakthrough is required. Repair remains narrowly scoped to Q06 source-level execution plus synchronization of the corrected Q03 result. Q04/Q11 remain deferred.

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
REPAIR_SCOPE=Q06_SOURCE_LEVEL_RECEIVER_EXECUTION_AND_Q03_RESULT_SYNC_ONLY
Q03_DEEP_EXECUTION=PASS
Q03_MOD8_OBSTRUCTION_ACCEPTED=true
Q03_REOPEN_REQUIRED=false
Q06_EXECUTION_DEPTH_INSUFFICIENT=true
Q06_SOURCE_ATTACK_IDS_MUST_BE_OPENED=true
Q06_ACTUAL_RECEIVER_MAP_REQUIRED=true
Q06_HEIGHT_MULTIPLICITY_PUSH_REQUIRED=true
STALE_Q03_FALSE_CLAIM_PRESENT_IN_RESULT=true
Q04_Q11_ACTIVATION_DEFERRED=true
ZERO_DENSITY_MATHEMATICS_REOPEN_REQUIRED=false
```
