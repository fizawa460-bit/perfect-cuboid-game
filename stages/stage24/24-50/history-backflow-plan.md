# Stage24-50 history supersession backflow plan

STATUS=PENDING_FRESH_AUDIT
EXECUTE_ONLY_IF_CHECKPOINT50_AUDIT_PASS=true

Checkpoint50 proposes two results that are stronger than the historical Stage19 checkpoint50/final status:

```text
historical: STAGE19_UNBOUNDEDNESS_PROVED=false
proposed:   STAGE19_UNBOUNDEDNESS_PROVED=true

historical: INFINITE_PRIMITIVE_CONSTRUCTION_CERTIFIED=false
proposed:   INFINITE_PRIMITIVE_STAGE19_CONSTRUCTION_PROVED=true
```

The historical files were correct at the time they were audited. They must not be silently rewritten while the new theorem is still pending fresh audit.

If and only if Stage24 checkpoint50 receives `AUDIT_VERDICT=PASS`, the next history backflow must:

1. add an explicit post-Stage24 supersession note to the current Stage19 handoff/final-facing status surface rather than pretending Stage19 originally proved the theorem;
2. preserve provenance to Stage24 checkpoint50 and its audit commit/PR;
3. change current consumer-facing lower status from constant floor only to
   `N2(B)>>sqrt(log B)`;
4. change current consumer-facing unboundedness/infinite-construction flags to true;
5. retain `POSITIVE_POWER_LOWER_BOUND_PROVED=false` and `MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false`;
6. narrow Stage23 R60-01 from broad-formula death to `odd/odd specialization dead; mixed-parity C17 variant revived`;
7. leave every perfect-cuboid nonexistence/existence flag unchanged.

Before PASS:

```text
HISTORY_BACKFLOW_EXECUTED=false
HISTORICAL_STAGE19_FILES_MUTATED=false
```

After PASS the fresh auditor/main controller may execute the backflow on the audited branch or require one narrow follow-up, but advancement to checkpoint60 must not leave stale current-facing status claiming unboundedness is still unknown.
