# Stage32 32-01-178 MAIN startup

This file is the single authoritative startup/read-order contract for ordinary `stage32-01-178-mainbatch` operation. `MAINBATCH.md`, `MISSION.json`, historical Generation-1 lane files, roadmaps, and audit receipts must not define a competing startup order.

## Ordinary startup

Read only, in this order:

1. `AGENTS.md`;
2. this file;
3. current `stages/stage32/MAIN-STATE.json` from the live Stage32 MAIN authority surface;
4. current `stages/stage32/proof/CROSS-LANE-DEMANDS.json` from that same live authority surface;
5. only the exact current 178 node/state selected by those authorities;
6. only exact source/evidence paths referenced by that current node/state.

`stages/stage32/COMMANDS.md` is the command registry used to resolve this command to this entrypoint; once resolved, it is not a second 178 startup contract and need not be re-read as part of the lane payload.

`stages/stage32/32-01-178/MISSION.json` is retained mission-DAG/history. It is **on-demand only** during ordinary startup. Read it only when the current selected node explicitly depends on mission history, duplicate-route/reopen analysis, or a historical retained result. Its snapshots and old node statuses never override current MAIN routing.

Historical Generation-1 `a..f` states are also on-demand evidence only. Do not sweep them on every startup and do not reactivate them merely because they remain present.

## Authority and drift rule

Current MAIN routing wins over lane-local mirrors and historical mission text. Before substantive research, resolve the live Stage32 MAIN authority identity. If the branch-local `MAIN-STATE.json` or `CROSS-LANE-DEMANDS.json` is stale relative to that live authority, use the live authority surface and record the mismatch; if the live identity cannot be resolved safely, fail closed rather than research from an uncertain boundary.

The authoritative remaining-terminal quantity may be an upper bound rather than an exact residual identity set; preserve the semantics recorded by current `MAIN-STATE.json` and do not silently strengthen them.

## Cross-lane routing

`stages/stage32/proof/CROSS-LANE-DEMANDS.json` is the machine authority for operational dependencies. Inspect demands applicable to lane `178` before local work. A higher-priority OPEN demand or explicit MAIN reassignment preempts ordinary local research. Do not duplicate producer-owned work while waiting for another lane.

Shared explanatory demand semantics live in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`, but that prose file is on-demand reference and is not another mandatory startup read.

Demand status never grants mathematical credit. Lane-local retained work carries zero MAIN credit until the required independent audit, source/claim synchronization, current-target adapter where applicable, and explicit MAIN consumption/promotion are complete.

## Ownership

This command owns sustained concrete FULL178 numerical-census research: exact census/compression, prefix/incidence/transport/support-capacity attacks, completeness/replay architecture, and bounded successor work selected by the current 178 frontier.

It does not own Stage32 global authority/promotion, EX5 Picard64/node-support production, CUT direct obstruction work, MB multibranch research, or another lane's currently assigned semantic leaf. MAIN remains the controller/integrator and may research MAIN-owned, cross-lane, or genuinely unowned mathematics.

## Execution mode

Ordinary `stage32-01-178-mainbatch` is one single-researcher breadth cycle. Search retained current-node evidence before inventing a new route. Freeze failed routes with an exact blocker and reopen condition; do not rerun equivalent blocked work under a new name. Rotate to a materially distinct route only after recording that boundary.

Heavy or artifact-producing compute requires the repository heavy-workflow authorization gate. Ordinary startup does not arm heavy compute.

Use `stage32-01-178-audit` only after a new exact retained 178 audit boundary is frozen. Do not self-grant audit or MAIN credit. Do not merge without explicit user authorization.
