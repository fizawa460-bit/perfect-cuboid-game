# Stage14-s-batch — canonical task contract

## Common contract

First read [`stage14-batch-common-contract.md`](stage14-batch-common-contract.md).
That file is normative for source boundaries, 3--5 work units, integrated H,
stop rules, validation, publication, and strict-saving claims. This file states
only the s-route specialization and output fields.

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

## Batch execution specialization

Use the common one-branch batch to advance the s route. For every ordinary
internal s stage:

1. read the merged predecessor and every merged dependency it names;
2. preserve all physical masks, primitive and gcd conditions, orientations,
   quantifier order, and charged-once accounting;
3. write a self-contained result with its own boundary tokens and exact `NEXT`;
4. make an explicit `sH` decision, including the theorem target when H is needed;
5. run the narrow deterministic audit needed for that internal step.

All common publication rules apply.

## Integrated sH work unit

Apply the common integrated-H rule under the name `sH`. Freeze the exact theorem
target and source snapshot before the clean-room audit; the next s stage may
consume its positive result, negative result, or minimal obstruction.

## Stop-rule specialization

Apply the common stop rules to the minimal remaining s-route arithmetic
receiver. No additional s-route stop event is introduced.

## Publication fields

In addition to the common final-report fields, state:

```text
STAGE14_S_BATCH=COMPLETE|STOPPED_EARLY
CURRENT_S_RECEIVER=<receiver>
S_ROUTE_H_NEEDED=<true|false>
NEXT=<next concrete Stage14-s stage or exact unresolved gate>
```
