# Stage25 checkpoint60 continuation policy

STATUS=NORMATIVE_FOR_STAGE25_60_DEEP_ROUNDS

Checkpoint60 is an iterative deep-research checkpoint. A fresh audit PASS for one checkpoint60 round certifies that round; it does **not** by itself close checkpoint60 or authorize Stage70 synthesis while high-value live routes remain.

## Operating rule

After each audited checkpoint60 round:

1. merge the audited PR if allowed;
2. re-open checkpoint60 on a new continuation branch/PR when a live high-value route remains;
3. preserve every prior checkpoint60 audit record as historical provenance;
4. do not overwrite or weaken an earlier audited theorem merely because a later sublane fails;
5. move to checkpoint70 only after the stop rule below is satisfied.

Suggested round naming:

- `25-60-r01` — causal cross-ratio / r501 rigidity / first R503-R506 triage (PR #985);
- `25-60-r02` — highest-value remaining lane(s), expected first target R503 Yoshida uniform-height receiver;
- subsequent rounds `r03`, `r04`, ... as justified.

## Audit placement rule

Fresh audit is required whenever a round does one of the following:

- proves a stronger global lower or upper exponent;
- proves a new infinite family or moving-family theorem;
- changes an interaction sign/classification;
- closes a previously named OPEN_GATE;
- makes a strongest-certified / no-known-route claim;
- introduces a new external theorem species as load-bearing input.

A negative exploratory round may be merged after audit if it materially certifies a route boundary, but negative results do not erase still-live unrelated lanes.

## Stop rule for checkpoint60

`CHECKPOINT60_DEEP_STOP_RULE=SATISFIED` only when all of the following hold:

- every currently named high-value lane R502-R506 is either `CLOSED_PROVED`, `CLOSED_NO_UPGRADE_WITH_CERTIFICATE`, or `EXTERNAL_THEOREM_GATE`;
- no repo-native attack compatible with the Stage14/15 deep-review reopen conditions remains live;
- any new theorem-class-changing result has received fresh audit;
- current global envelope and interaction classification are synchronized across Stage23/24/25 backflow artifacts;
- remaining open items require genuinely new external mathematics, not another unexecuted algebraic/computational mutation already available in-repo.

Only then may checkpoint60 set `NEXT_CHECKPOINT=70`.

## Current post-r01 state

```text
ROUND=25-60-r01
PR=985
AUDIT_STATUS=PENDING
CHECKPOINT60_CLOSED=false
STAGE70_ALLOWED=false
LIVE_HIGH_VALUE_LANES=R503_YOSHIDA_UNIFORM_HEIGHT,R504_SYMMETRIC_K_AGGREGATION,R505_COMMON_CORE,R506_COMMON_LEG_SPACE
R502_STATUS=SAME_EXPONENT_FALLBACK
NEXT_AFTER_R01_PASS=MERGE_AND_CONTINUE_CHECKPOINT60
```
