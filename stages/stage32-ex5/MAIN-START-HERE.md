# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order:

1. `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. `stages/stage32/MAIN-STATE.json` for current Stage32 routing;
4. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. `stages/stage32-ex5/CROSS-LANE-STATE.json` when EX5 has an OPEN producer demand;
6. `stages/stage32-ex5/README.md`;
7. this file;
8. `MAINBATCH-OPERATIONS.md`;
9. `MAIN-STATE.json`;
10. only the active EX5 working set required by the selected route.

Historical Cycle1 files remain source-locked provenance.

## Cross-lane demand priority

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`.

Before local EX5 research, inspect every OPEN demand with `producer_lane=EX5`. If an OPEN demand has higher priority than the current local route, producing the requested exact artifact becomes the next EX5 route. Do not continue lower-priority local BC2 refinement merely because it was already in progress.

If EX5 is a consumer for another OPEN demand, wait without duplicating the producer. If that demand becomes SATISFIED, re-enter on the next `stage32ex5-mainbatch` and validate the satisfying artifact path/blob/canonical and population semantics before resuming. Demand SATISFIED does not grant mathematical credit; hostile audit, claim sync, current-target adapters and MAIN promotion remain separate.

Current coordination state gives `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` priority `P0_BLOCKING_DOWNSTREAM`. It requests a source-locked exact terminal-to-Picard64 completion interface for a disjoint current-MAIN-surviving e=8 block/population with exact rank/unrank semantics. This priority demand supersedes lower-priority same-first-block BC2 residual refinement while OPEN.

## Current authority

PR #1765 is merged at `98c5710dad4ca9a006e93b273ecf5259733e03aa`; it is not an active working PR. Current Stage32 routing must be read from `stages/stage32/MAIN-STATE.json`, not the old #1765 base SHA. Later unmerged EX5 research remains retained only at its exact audited boundary until separately integrated.

The retained local EX5 state/evidence remains mathematical provenance; cross-lane coordination state changes routing priority only and creates no mathematical credit.

## Retained boundary

BC2-24 remains the merged EX5 base result: 4 newly UNSAT parents, `19` retained UNKNOWN, 0 SAT; known parent-UNSAT lower bound `7145`; `172` other BC2-19 UNKNOWN identities remain uninferred. Later BC2-25/26 work may exist on an unmerged research PR, but it does not override the P0 producer demand or current MAIN population semantics.

The whole first block, whole stratum, and FULL178 remain open.

## Executable boundary

On a new `stage32ex5-mainbatch` invocation:

1. synchronize current MAIN routing;
2. inspect `CROSS-LANE-DEMANDS.json` and `CROSS-LANE-STATE.json`;
3. if a higher-priority OPEN producer demand exists, execute the smallest exact unit that supplies that requested artifact;
4. otherwise replay/validate the retained local EX5 boundary and continue the current local route;
5. never relabel UNKNOWN as UNSAT and do not broad/heavy scale out without its separate authorization gate.

For the current CUT192 demand, EX5 must identify a disjoint current-MAIN-surviving e=8 population, freeze exact rank/unrank semantics, and retain/source-lock the exact terminal-to-Picard64 completion interface. Supplying the interface does not itself prove UNSAT, FULL178 closure, effectivity, receiver credit, theorem credit, endpoint credit, or Stage32 closure.

No Stage32 MAIN, N350, theorem, receiver, effectivity, endpoint, or Perfect Cuboid credit follows automatically.
