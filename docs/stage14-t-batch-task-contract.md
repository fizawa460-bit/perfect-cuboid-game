# Stage14-t-batch — canonical task contract

## Common contract

First read [`stage14-batch-common-contract.md`](stage14-batch-common-contract.md).
That file is normative for source boundaries, 3--5 work units, integrated H,
stop rules, validation, publication, and strict-saving claims. This file states
only the t-route specialization and output fields.

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

## Batch execution specialization

Use the common one-branch batch to advance the t route. For every ordinary
internal t stage:

1. read the merged predecessor and every merged dependency it names;
2. preserve the fixed-`U` packet, physical masks, primitive and gcd conditions,
   root/orientation data, quantifier order, and charged-once accounting;
3. write a self-contained result with its own boundary tokens and exact `NEXT`;
4. make an explicit `tH` decision, even when the answer is false;
5. when `tH` is needed, state the exact requested theorem/object, immutable
   source snapshot, target file, and blocking/nonblocking status;
6. run the narrow deterministic audit needed for that internal step.

All common publication rules apply.

## Integrated tH work unit and independence

Apply the common integrated-H rule under the name `tH`. In addition to the
common frozen target, record the exact request, immutable source snapshot,
target file, and blocking status. Reusable independent tH roads may continue;
any road depending on unmerged output outside this batch remains PARKED.

## Stop-rule specialization

Apply the common stop rules to the minimal fixed-`U` receiver. Re-expression of
the same charged-once receiver is not a material receiver change.

## Publication fields

In addition to the common final-report fields, state:

```text
STAGE14_T_BATCH=COMPLETE|STOPPED_EARLY
CURRENT_T_RECEIVER=<receiver>
T_ROUTE_H_NEEDED=<true|false>
T_ROUTE_H_REQUEST=<exact object or NONE>
T_ROUTE_H_TARGET=<path or NONE>
T_ROUTE_H_BLOCKING=<true|false>
NEXT=<next concrete Stage14-t stage or exact unresolved gate>
```

A fixed-`U` saving must not be cross-promoted unless its summation over the
complete physical `U` family is proved with the required uniformity.
