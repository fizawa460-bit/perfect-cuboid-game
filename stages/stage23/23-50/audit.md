# Stage23-50 fresh re-audit

Status: **FAIL**

The previous fresh-surgeon depth failure is repaired. `fresh-surgeon-candidate-ledger.md` now materializes four genuinely new Stage19 candidate mechanisms (F50-S1 through F50-S4), tests the literal Stage19 contract, and records distinct failure/survival gates. Q04/Q11 remain accepted and need not be reopened.

Two narrow defects remain.

First, the checkpoint50 result does not explicitly state the strongest currently certified Stage19 lower bound. The canonical Stage19 final interface proves the exact finite floor

\[
\boxed{N_2(B)\ge 3495\qquad(B\ge 500{,}000{,}000),}
\]

by monotonicity from `N_2(500,000,000)=3495`. This is a constant lower floor only. Stage19 still has no proof that `N_2(B)->infinity`, no infinite primitive construction, no positive-power lower bound `N_2(B)>>B^delta`, and no matching half-power lower bound. Checkpoint50 currently says only that no positive-power lower bound was found; for closeout-quality provenance it must distinguish the known constant floor from the unresolved unbounded/positive-power gate.

Second, F50-S4 overstates what an infinite survivor sequence would imply. From `d~v^4`, an infinite but arbitrarily sparse sequence of admissible `v` does **not** by itself imply a `B^(1/4)` lower bound. A `B^(1/4)`-scale lower bound would require quantitative density/counting information in the parameter `v` (for example, a positive proportion or another proved counting law). The candidate remains valuable because its height law identifies the scale available under a sufficiently dense survivor set, but the unconditional implication from mere infinitude must be removed.

No other checkpoint50 mathematics is reopened. In particular, the fresh candidate-generation ledger is accepted as satisfying the surgeon-depth repair, and Q04/Q11 remain accepted.

```text
AUDIT_VERDICT=FAIL
AUDIT_PERSISTENCE_STATUS=COMMITTED
UNSYNCED_AUDIT_STATE=NONE
ADVANCE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=50
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=false
REPAIR_SCOPE=EXPLICIT_STAGE19_CURRENT_LOWER_BOUND_STATUS_AND_F50_S4_RATE_CLAIM_CORRECTION_ONLY
FRESH_STAGE19_SURGEON_DEPTH_ACCEPTED=true
FRESH_CANDIDATE_GENERATION_ACCEPTED=true
Q04_ANALYSIS_ACCEPTED=true
Q11_ANALYSIS_ACCEPTED=true
STAGE19_CERTIFIED_CONSTANT_LOWER_FLOOR=N2(B)>=3495_FOR_B>=500000000
STAGE19_UNBOUNDEDNESS_PROVED=false
STAGE19_POSITIVE_POWER_LOWER_BOUND_PROVED=false
STAGE19_MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
F50_S4_INFINITE_SEQUENCE_IMPLIES_B_QUARTER=false
F50_S4_DENSE_SURVIVOR_COUNT_COULD_YIELD_B_QUARTER_SCALE=true
Q04_Q11_REOPEN_REQUIRED=false
SURGEON_REOPEN_REQUIRED=false
```
