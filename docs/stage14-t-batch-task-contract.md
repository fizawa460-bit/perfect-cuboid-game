# Stage14-t-batch — canonical task contract

## Canonical invocation

The permanent task name is:

```text
Stage14-t-batch
```

When this exact name is requested, read this contract before choosing a concrete
stage number or creating a branch. Start from latest merged `main`, locate the
latest merged `Stage14-t*` result, and follow its unique `NEXT`. The permanent
name is only an entry point: concrete results retain the ordinary sequence, such
as `Stage14-t106`, `Stage14-t107`, and so on.

## Source boundary

Only merged commits on latest `main` are theorem sources. Open, draft,
closed-unmerged, local-only, or concurrently produced results are advisory and
must not determine a theorem boundary. At the start and immediately before
publication, record the main SHA and recheck whether a newly merged predecessor
or consumer changes the batch.

## Batch execution

Use one branch to advance 3--5 substantive `t` stages. For every internal stage:

1. read the merged predecessor and every merged dependency it names;
2. preserve the fixed-`U` packet, physical masks, primitive and gcd conditions,
   root/orientation data, quantifier order, and charged-once accounting;
3. write a self-contained result with its own boundary tokens and exact `NEXT`;
4. make an explicit `tH` decision, even when the answer is false;
5. when `tH` is needed, state the exact requested theorem/object, immutable
   source snapshot, target file, and blocking/nonblocking status;
6. run the narrow deterministic audit needed for that internal step.

Do not publish a separate branch or PR for each internal stage. Checkpoint commits
are allowed, but the batch has one final branch, one consolidated validation pass,
and one Draft PR.

## Integrated tH work unit and independence

A newly exposed `tH` target does not by itself end the batch. Freeze the exact
request, immutable source snapshot, target file, and blocking status, then
perform the independent `tH` audit as the next work unit on the same branch. The
H artifact must be clean-room with respect to later internal `t` stages: it may
read the frozen target, but must not use a later `t` conclusion to prove that
target. After the audit is complete, the following `t` stage may consume its
positive result, negative result, or minimal obstruction and continue within
the same Draft PR.

An integrated `tH` audit counts as one of the batch's 3--5 substantive work
units. For example, `tN`, `tHk`, `t(N+1)` is a three-unit batch. It is not a
separate PR and it does not count as an extra stage outside the cap. Existing
merged or concurrently running tH work remains read-only/advisory, is never
rewritten to chase the batch, and retains its frozen-snapshot independence.
Reusable tH roads may continue independently, while any road that depends on
unmerged output outside this batch remains frozen and PARKED.

## Stop rules

End the batch at the first of these events:

- **receiver change**: the minimal fixed-`U` arithmetic receiver changes in a
  mathematically material way;
- **unresolved external gate**: after carrying out the integrated tH audit,
  further progress still depends on an unavailable source, an unfrozen theorem
  statement, outside coordination, or another result that cannot be decided in
  the current batch;
- **rigorous counterexample**: an explicit verified witness rules out the active
  adapter, saving mechanism, or proposed reduction;
- **five completed work units**: the hard cap, even if the receiver has not changed.

The normal target is at least three completed work units, counting integrated
H. Early stopping before three is permitted only for one of the first three
mathematical events above, and the result must identify the exact trigger. A
mere renaming, restatement, dependency refresh, or re-expression of the same
charged-once receiver is not substantive and does not count toward the 3--5
target.

## Publication boundary

The single Draft PR must contain only batch-owned results, scripts/data, the
path-scoped workflow, and any genuinely reusable lemma produced by the batch.
Run all internal audits once more at the end plus the relevant predecessor
regressions. Existing merged stages remain read-only.

The final batch report must state:

```text
STAGE14_T_BATCH=COMPLETE|STOPPED_EARLY
BATCH_START_MAIN_SHA=<sha>
BATCH_PUBLICATION_MAIN_SHA=<sha>
BATCH_FIRST_STAGE=<stage>
BATCH_LAST_STAGE=<stage>
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=<3..5, or justified early count; includes integrated tH>
BATCH_SUBSTANTIVE_STAGE_COUNT=<same value; compatibility alias including integrated tH>
BATCH_INTEGRATED_H_UNITS=<comma-separated tH stages or NONE>
BATCH_STOP_REASON=receiver_change|unresolved_external_gate|rigorous_counterexample|five_stage_cap
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=<value>
STRICT_SUBSQRT_POWER_SAVING_PROVED=<true|false>
CURRENT_T_RECEIVER=<receiver>
T_ROUTE_H_NEEDED=<true|false>
T_ROUTE_H_REQUEST=<exact object or NONE>
T_ROUTE_H_TARGET=<path or NONE>
T_ROUTE_H_BLOCKING=<true|false>
NEXT=<next concrete Stage14-t stage or exact unresolved gate>
```

No strict sub-square-root saving may be declared unless the batch proves

```text
V(B) << B^(1/2-delta+o(1))
```

for some fixed `delta>0` on the full physical packet. A fixed-`U` saving must
not be cross-promoted unless its summation over the complete physical `U` family
is proved with the required uniformity.
