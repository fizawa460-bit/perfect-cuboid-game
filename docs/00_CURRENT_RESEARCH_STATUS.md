# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage20-40-AUDIT-PASS
STAGE12_STATUS=FROZEN_R09
STAGE13_STATUS=CLOSED_R07
STAGE14_STATUS=CLOSED_R06
STAGE15_STATUS=CLOSED_R02_REVIEW_FROZEN
STAGE16_STATUS=CLOSED_R01_AUDIT_PASS
STAGE16S_STATUS=CLOSED_R01_AUDIT_PASS
STAGE17_STATUS=CLOSED_R01_AUDIT_PASS
STAGE18_STATUS=CLOSED_R01_AUDIT_PASS
STAGE19_STATUS=CLOSED_R01_AUDIT_PASS
STAGE20_STATUS=OPEN_CHECKPOINT_40_AUDIT_PASS
STAGE20_CONTROLLER=stages/stage20/20-controller.json
STAGE20_CURRENT_RESULT=stages/stage20/20-40/result.md
STAGE20_CURRENT_AUDIT=stages/stage20/20-40/audit.md
STAGE20_CURRENT_DATA=stages/stage20/20-20/counts.csv
STAGE20_CURRENT_ENUMERATOR=stages/stage20/20-20/enumerate.py
STAGE20_UPPER_BOUND_PROVENANCE=Stage14-e8
STAGE20_STRONGEST_CERTIFIED_UPPER=M3(B)=B^(1+o(1))
STAGE20_AUDIT_PERSISTENCE=COMMITTED
STAGE20_NEXT_CHECKPOINT=50
NEXT_EXPECTED_COMMAND=Stage20-main-batch
NEXT_RESEARCH_PROGRAM=docs/stage16-28-population-roadmap.md
```

## Current operation

Stage20 checkpoints10 and20 are audited PASS. Checkpoint30 remains `OPEN_GATE_AUDITED_PASS` for the unresolved population growth law. Checkpoint40 has now been repaired and fresh-audited after discovery of the already-audited Stage14-e8 Euler-brick upper theorem.

The prior checkpoint40 audit from PR #935 correctly proved the ambient inclusion `M_3(B)=O(B^3)`, but incorrectly described it as the strongest certified project upper bound. Stage14-e8 counts the same primitive/canonical all-three-face population under the same Euclidean cutoff `R<=B` and proves
\[
M_3(B)\ll B\log B\exp\!\left(O\!\left(\frac{\log B}{\log\log B}\right)\right)=B^{1+o(1)},
\]
equivalently `M_3(B)=O_epsilon(B^(1+epsilon))` for every fixed epsilon>0.

This is the corrected strongest certified upper envelope. It is not a two-sided growth law. Matching lower bounds, sharpness, and the true Stage20 growth law remain unresolved and move to the appropriate later ledgers. Stage18-to-Stage20 conditional thinning remains reserved for Stage26. No space-diagonal condition or perfect-cuboid conclusion is introduced.

```text
STAGE_STATUS=OPEN
CHECKPOINT=40
CHECKPOINT_STATUS=PROVED_AUDITED_PASS
PRIOR_AUDIT_SUPERSEDED=true
UPPER_BOUND_PROVENANCE=Stage14-e8
STRONGEST_CERTIFIED_PROJECT_BOUND=M3(B)=B^(1+o(1))
OPEN_GATE_30=STAGE20_POPULATION_GROWTH_LAW_UNRESOLVED
OPEN_GATE_40=SHARPNESS_AND_MATCHING_LOWER_BOUND_UNRESOLVED
STAGE18_TO_STAGE20_RATIO=DEFER_STAGE26
AUDIT_STATUS=PASS
AUDIT_PERSISTENCE_STATUS=COMMITTED
UNSYNCED_AUDIT_STATE=NONE
ADVANCE_ALLOWED=true
MERGE_ALLOWED=true
NEXT_CHECKPOINT=50
NEXT_STAGE=
NEXT_EXPECTED_COMMAND=Stage20-main-batch
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_REQUIRED=false
```
