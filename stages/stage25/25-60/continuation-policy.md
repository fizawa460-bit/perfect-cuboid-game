# Stage25 checkpoint60 continuation policy

STATUS=NORMATIVE_FOR_STAGE25_60_CONTINUATION

Checkpoint60 is iterative. A fresh audit PASS certifies the submitted checkpoint60 claims, but does **not** by itself close checkpoint60 while assigned high-value research routes remain live.

## Naming invariant — preserve the assigned route IDs

Research-route IDs are persistent identities, not audit-round numbers and not checkpoint-local counters.

The existing allocation is:

- `R501` — Meskhishvili first parametrization / audited positive-power family;
- `R502` — Meskhishvili third parametrization fallback;
- `R503` — Yoshida varying-fiber / uniform-height route;
- `R504` — symmetric-k aggregation / moving elliptic section route;
- `R505` — common squarefree-core route;
- `R506` — common-leg + space receiver;
- `R507` — primitive-height rigidity of R501, opened at checkpoint60.

These IDs MUST NOT be renamed merely because work continues at checkpoint60 or because another audit/PR is opened.

```text
ROUTE_ID_IS_PERSISTENT=true
AUDIT_ROUND_IS_NOT_ROUTE_ID=true
CHECKPOINT_NUMBER_DOES_NOT_RENUMBER_EXISTING_ROUTE=true
R501_R507_ALLOCATIONS_FROZEN=true
```

If a genuinely new mathematically distinct route is created after R507, allocate the next unused route ID (`R508`, then `R509`, ...). A refinement of an existing route keeps its existing ID.

Do **not** create names such as `25-60-r01`, `25-60-r02`, etc. to represent audit rounds. PR numbers and audit-history entries already distinguish successive submissions.

## Operating rule

After each audited checkpoint60 submission:

1. merge the audited PR if allowed;
2. continue checkpoint60 when any assigned high-value route remains actionable;
3. preserve prior checkpoint60 audit records as historical provenance;
4. continue work under the original route ID (`R503`, `R504`, etc.);
5. do not overwrite or weaken an earlier audited theorem merely because a later route fails;
6. move to checkpoint70 only after the stop rule below is satisfied.

## Audit placement rule

Fresh audit is required whenever a checkpoint60 submission does one of the following:

- proves a stronger global lower or upper exponent;
- proves a new infinite family or moving-family theorem;
- changes an interaction sign/classification;
- closes a previously named OPEN_GATE;
- makes a strongest-certified / no-known-route claim;
- introduces a new external theorem species as load-bearing input.

A negative exploratory submission may be audited and merged if it materially certifies a route boundary, but it does not close unrelated live routes.

## Stop rule for checkpoint60

`CHECKPOINT60_DEEP_STOP_RULE=SATISFIED` only when all of the following hold:

- each assigned high-value route R502-R506 and any later allocated route is `CLOSED_PROVED`, `CLOSED_NO_UPGRADE_WITH_CERTIFICATE`, or `EXTERNAL_THEOREM_GATE`;
- no repo-native attack compatible with the Stage14/15 deep-review reopen conditions remains live;
- any theorem-class-changing result has received fresh audit;
- current global envelope and interaction classification are synchronized across Stage23/24/25 backflow artifacts;
- remaining open items require genuinely new external mathematics, not another unexecuted repo-native mutation.

Only then may checkpoint60 set `NEXT_CHECKPOINT=70`.

## Current state at PR #985

```text
PR=985
AUDIT_STATUS=PENDING
CHECKPOINT60_CLOSED=false
STAGE70_ALLOWED=false
R501=PROVED_B1_4_FAMILY
R502=SAME_EXPONENT_FALLBACK
R503=LIVE_HIGH_VALUE_UNIFORM_HEIGHT_GATE
R504=LIVE_GENERIC_NONTORSION_SECTION_NO_EXPONENT_UPGRADE_YET
R505=LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT
R506=LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT
R507=SUBMITTED_PRIMITIVE_HEIGHT_RIGIDITY
NEXT_AFTER_PR985_PASS=MERGE_AND_CONTINUE_CHECKPOINT60_UNDER_EXISTING_ROUTE_IDS
```
