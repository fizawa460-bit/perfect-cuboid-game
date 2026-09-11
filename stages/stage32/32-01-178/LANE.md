# stage32-01-178 parallel lane

This contract applies to `stage32-01-178-a`, `-b`, `-c`, etc.

## Startup

1. Read `AGENTS.md`.
2. Read `stages/stage32/32-01-178/MISSION.json` only far enough to resolve the exact dispatch assignment for the requested slot.
3. Read only the assigned node's `STATE.json` and exact referenced source/evidence paths.
4. Use the dispatch-recorded `work_branch`. Do not create a PR by default.

## Hard binding

The slot-to-node mapping is immutable within its dispatch generation. Do not recompute the frontier, steal another lane, or continue to a second node after finishing the assigned node.

If the assigned node is itself too large, it may instantiate a nested Mission DAG under its node directory or an explicitly named child area. The parent lane then acts as that nested mission's integrator and returns only a coherent child checkpoint to the parent `stage32-01-178-mainbatch`.

## Anti-duplication / anti-loop

Before research, inspect `reuse_check` and prior attempts. Search before creating a new route. Do not retry a BLOCKED `route_id` unless its recorded reopen condition is now true. If broadening/parking/exhaustion is load-bearing, invoke the Cycle Exploration Safety Protocol on demand.

## Scope

Do only the assigned obligation. Preserve exact population/model/quantifier scope and replay evidence. Scratch is non-authoritative. Heavy compute requires separate authorization.

EX5 is an external producer. Do not duplicate its active BC2-02 work unless the assigned node explicitly proves a materially distinct non-overlapping obligation.

## Return

Return one of: retained checkpoint, exact blocker + reopen condition, explicit equivalent/dominated result, or audit-ready result. MAINBATCH owns cross-node reconciliation and promotion. No merge and no self-granted hostile-audit credit.
