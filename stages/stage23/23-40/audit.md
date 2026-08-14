# Stage23-40 fresh audit

Status: **FAIL**

The priority selection is correct, but the selected P1 weapons have not yet been executed deeply enough to satisfy Stage23's aggressive-search contract.

Q06 currently restates the conditions that a successful Kummer upper attack would need: a literal Stage19 map with controlled multiplicity, a physical-height transfer, and a point-count theorem strong enough to improve `B^(1/2+epsilon)`. That is a useful attack specification, but no concrete receiver map/height inequality is derived or tested at checkpoint40. Therefore `Q06_EXECUTED=YES` is too strong.

Q03 similarly observes that the quartic `w^2=(t^2+1)(t^2+2t+2)` has rational point `(0,1)` and hence an elliptic model over Q, but it does not actually compute a Weierstrass model, rank/torsion information, generators, or the integral/congruence pullback. Since Q03 was selected specifically as the genus-one arithmetic weapon, existence of an elliptic model is the entrance to the attack, not completion of the attack.

This audit does not require a breakthrough. It requires actual execution artifacts: for Q06, derive the available Stage14/15 `(4,4)` receiver in Stage23 variables and push the physical `d<=B` height/multiplicity comparison as far as the repository permits, recording the exact first unproved inequality/theorem. For Q03, compute an explicit elliptic model and whatever rank/torsion/integral-point information can be obtained internally; then test the `t=1 mod14` pullback. If an internal computation cannot resolve a gate, record the exact external theorem/computation required.

Q04/Q11 should not be activated merely because Q06/Q03 were described. They become reserves after these two selected attacks have genuinely reached their internal boundary.

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
REPAIR_SCOPE=DEEP_EXECUTION_OF_SELECTED_Q06_AND_Q03_ATTACKS_ONLY
Q06_SELECTION_ACCEPTED=true
Q03_SELECTION_ACCEPTED=true
Q06_EXECUTION_DEPTH_INSUFFICIENT=true
Q03_EXECUTION_DEPTH_INSUFFICIENT=true
Q04_Q11_ACTIVATION_DEFERRED=true
ZERO_DENSITY_MATHEMATICS_REOPEN_REQUIRED=false
```
