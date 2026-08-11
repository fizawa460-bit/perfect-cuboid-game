# Stage14-main-batch — route-specific contract

## Canonical invocation

```text
Stage14-main-batch
```

When invoked, first read
[`stage14-batch-common-contract.md`](stage14-batch-common-contract.md), then this
file. Start from latest merged `main`, locate the latest merged `Stage14-4*`
result, and follow its unique `NEXT`. Concrete results retain the `Stage14-4*`
sequence and may be grouped under `stages/stage14/14-4-batch/`.

## Main-line specialization

The common 3--5 work-unit rule applies. Preserve the complete global physical
packet and all imported s/t interfaces, but do not treat an unmerged s/t result
as a theorem source. Because the main line has the widest dependency surface,
recheck merged s, t, toolbox/X, q, and prior main-line H inputs named by the
active receiver at every internal boundary.

Every ordinary main-line unit records whether an independent main-line H audit
is needed. A new H audit is integrated under the common frozen-target clean-room
rule and counts as one work unit. It must not use later internal main-line
conclusions. If it leaves an unresolved external gate, stop; otherwise consume
its positive result, negative result, or minimal obstruction and continue.

The final report adds:

```text
STAGE14_MAIN_BATCH=COMPLETE|STOPPED_EARLY
CURRENT_MAIN_RECEIVER=<receiver>
MAIN_ROUTE_H_NEEDED=<true|false>
MAIN_ROUTE_H_REQUEST=<exact object or NONE>
MAIN_ROUTE_H_TARGET=<path or NONE>
MAIN_ROUTE_H_BLOCKING=<true|false>
```
