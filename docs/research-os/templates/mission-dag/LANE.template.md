# __MISSION__ parallel lane

This contract applies to short commands such as `__MISSION__-a`, `__MISSION__-b`, and `__MISSION__-c`.

## Startup

1. Read repository `AGENTS.md`.
2. Read this mission's `MISSION.json` only far enough to resolve the exact recorded dispatch assignment for the requested slot.
3. Read only the assigned node's `STATE.json` and exact referenced source/evidence paths.
4. Use the recorded `work_branch` or its exact mission-approved equivalent. Do not create a PR by default.

## Hard binding

The slot-to-node mapping is immutable for that dispatch generation.

- Do not recompute the READY frontier to choose a different node.
- Do not steal another lane's node.
- Do not continue onto a second node after finishing the assigned one.
- If the assignment is absent, cancelled, consumed, or otherwise invalid, stop and return to `__MISSION__-mainbatch` for redispatch.

## Research execution

Before work, inspect the node's `reuse_check` and prior attempts. Search before creating a new route. Do not retry a `BLOCKED` route unless its recorded reopen condition is now true.

Execute bounded materially distinct work, retain exact scope/evidence/replay information, and stop at a coherent node checkpoint. A blocked route is not mission exhaustion.

## Return to MAINBATCH

Report the assigned node outcome as one of:

- retained progress/checkpoint;
- exact blocker with reopen condition;
- equivalent/dominated existing result;
- audit-ready retained result.

MAINBATCH owns DAG mutation across nodes, redispatch, cross-lane integration, promotion, and audit handoff. The lane does not merge and does not self-grant hostile-audit credit.
