# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage20-40-REPAIR-SUBMITTED
STAGE12_STATUS=FROZEN_R09
STAGE13_STATUS=CLOSED_R07
STAGE14_STATUS=CLOSED_R06
STAGE15_STATUS=CLOSED_R02_REVIEW_FROZEN
STAGE16_STATUS=CLOSED_R01_AUDIT_PASS
STAGE16S_STATUS=CLOSED_R01_AUDIT_PASS
STAGE17_STATUS=CLOSED_R01_AUDIT_PASS
STAGE18_STATUS=CLOSED_R01_AUDIT_PASS
STAGE19_STATUS=CLOSED_R01_AUDIT_PASS
STAGE20_STATUS=OPEN_CHECKPOINT_40_REPAIR_SUBMITTED
STAGE20_CONTROLLER=stages/stage20/20-controller.json
STAGE20_CURRENT_RESULT=stages/stage20/20-40/result.md
STAGE20_PRIOR_AUDIT=stages/stage20/20-40/audit.md
STAGE20_CURRENT_DATA=stages/stage20/20-20/counts.csv
STAGE20_CURRENT_ENUMERATOR=stages/stage20/20-20/enumerate.py
STAGE20_AUDIT_PERSISTENCE=PENDING
STAGE20_NEXT_CHECKPOINT=50
NEXT_EXPECTED_COMMAND=Stage20-audit
NEXT_RESEARCH_PROGRAM=docs/stage16-28-population-roadmap.md
```

## Current operation

Checkpoint40 has been reopened because a previously audited reusable Stage14-e8 theorem was found to match the Stage20 population and cutoff exactly. Stage14-e8 counts primitive canonical Euler bricks with all three face diagonals integral and Euclidean R<=B, with no integral-space-diagonal requirement.

That theorem proves
\[
M_3(B)\ll B\log B\,\exp(O(\log B/\log\log B))=B^{1+o(1)},
\]
equivalently `M3(B)=O_epsilon(B^(1+epsilon))` for every fixed epsilon>0. This supersedes the previously recorded ambient cubic bound as the strongest certified Stage20 upper envelope.

The polynomial upper ceiling one is not a two-sided growth theorem: a matching lower bound, sharpness, and the true Stage20 growth law remain unresolved. Checkpoint50 is therefore not started until this repaired checkpoint40 receives fresh audit.

```text
STAGE_STATUS=OPEN
CHECKPOINT=40
CHECKPOINT_STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT
UPPER_BOUND_PROVENANCE=Stage14-e8
STRONGEST_CERTIFIED_PROJECT_BOUND=M3(B)=B^(1+o(1))
OPEN_GATE_30=STAGE20_POPULATION_GROWTH_LAW_UNRESOLVED
OPEN_GATE_40=SHARPNESS_AND_MATCHING_LOWER_BOUND_UNRESOLVED
STAGE18_TO_STAGE20_RATIO=DEFER_STAGE26
AUDIT_STATUS=PENDING
AUDIT_PERSISTENCE_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=50
NEXT_EXPECTED_COMMAND=Stage20-audit
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_REQUIRED=false
```
