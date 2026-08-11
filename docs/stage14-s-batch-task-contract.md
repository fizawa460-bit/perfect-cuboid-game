# Stage14-s-batch — canonical task contract

## Canonical invocation

The permanent task name is:

```text
Stage14-s-batch
```

When this exact name is requested, read this contract before choosing a concrete
stage number or creating a branch.  Start from latest merged `main`, locate the
latest merged `Stage14-s*` result, and follow its unique `NEXT`.  The permanent
name is only an entry point: concrete results retain the ordinary sequence, such
as `Stage14-s7-65`, `Stage14-s7-66`, and so on.

## Source boundary

Only merged commits on latest `main` are theorem sources.  Open, draft,
closed-unmerged, local-only, or concurrently produced results are advisory and
must not determine a theorem boundary.  At the start and immediately before
publication, record the main SHA and recheck whether a newly merged predecessor
or consumer changes the batch.

## Batch execution

Use one branch to advance 3--5 substantive `s` stages.  For every internal stage:

1. read the merged predecessor and every merged dependency it names;
2. preserve all physical masks, primitive and gcd conditions, orientations,
   quantifier order, and charged-once accounting;
3. write a self-contained result with its own boundary tokens and exact `NEXT`;
4. make an explicit `sH` decision, including the theorem target when H is needed;
5. run the narrow deterministic audit needed for that internal step.

Do not publish a separate branch or PR for each internal stage.  Checkpoint
commits are allowed, but the batch has one final branch, one consolidated
validation pass, and one Draft PR.

## Stop rules

End the batch at the first of these events:

- **receiver change**: the minimal remaining arithmetic receiver changes in a
  mathematically material way;
- **external lemma gate**: further progress requires a new external theorem or
  independent H audit; freeze the exact theorem contract and H request;
- **rigorous counterexample**: an explicit verified witness rules out the active
  adapter, saving mechanism, or proposed reduction;
- **five completed stages**: the hard cap, even if the receiver has not changed.

The normal target is at least three completed stages.  Early stopping before
three is permitted only for one of the first three mathematical events above,
and the result must identify the exact trigger.  A mere renaming, restatement,
or dependency refresh is not a substantive stage and does not count toward the
3--5 target.

## Publication boundary

The single Draft PR must contain only batch-owned results, scripts/data, the
path-scoped workflow, and any genuinely reusable lemma produced by the batch.
Run all internal audits once more at the end plus the relevant predecessor
regressions.  Existing merged stages remain read-only.

The final batch report must state:

```text
STAGE14_S_BATCH=COMPLETE|STOPPED_EARLY
BATCH_START_MAIN_SHA=<sha>
BATCH_PUBLICATION_MAIN_SHA=<sha>
BATCH_FIRST_STAGE=<stage>
BATCH_LAST_STAGE=<stage>
BATCH_SUBSTANTIVE_STAGE_COUNT=<3..5, or justified early count>
BATCH_STOP_REASON=receiver_change|new_external_lemma_needed|rigorous_counterexample|five_stage_cap
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=<value>
STRICT_SUBSQRT_POWER_SAVING_PROVED=<true|false>
CURRENT_S_RECEIVER=<receiver>
S_ROUTE_H_NEEDED=<true|false>
NEXT=<next concrete Stage14-s stage or exact H gate>
```

No strict sub-square-root saving may be declared unless the batch proves

```text
V(B) << B^(1/2-delta+o(1))
```

for some fixed `delta>0` on the full physical packet.
