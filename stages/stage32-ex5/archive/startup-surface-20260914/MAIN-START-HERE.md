# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order:

1. `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. `stages/stage32/MAIN-STATE.json` for current Stage32 routing;
4. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. `stages/stage32-ex5/CROSS-LANE-STATE.json` whenever EX5 has current demand state;
6. `stages/stage32-ex5/README.md`;
7. this file;
8. `MAINBATCH-OPERATIONS.md`;
9. `MAIN-STATE.json`;
10. only the active EX5 working set required by the selected route.

Historical Cycle1 files remain source-locked provenance.

## Cross-lane demand priority

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`.

Before local EX5 research, inspect every OPEN demand with `producer_lane=EX5`. If a higher-priority OPEN demand exists relative to the current local route, producing the requested exact artifact becomes the next EX5 route. Do not continue lower-priority local BC2 refinement merely because it was already in progress.

If EX5 is a consumer for another OPEN demand, wait without duplicating the producer. If that demand becomes SATISFIED, re-enter on the next `stage32ex5-mainbatch` and validate the satisfying artifact path/blob/canonical and population semantics before resuming. Demand SATISFIED does not grant mathematical credit; hostile audit, claim sync, current-target adapters and MAIN promotion remain separate.

Current coordination state:

- `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` remains **SATISFIED**. Its retained handoff is `stages/stage32/proof/CUT192-EX5-E8-HANDOFF-SATISFIED.json`.
- `S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1` is **OPEN / P0_BLOCKING_DOWNSTREAM**. EX5 must therefore defer the lower-priority BC2-25/26 local route and produce the smallest exact population-preserving terminal-to-Picard64 interface covering the retained HPADJ-01 current-V22 charged population across all 178 FULL178 rows.
- The HPADJ demand ends at Picard64 population identity. It must not claim effectivity, integrality, irreducibility, normalization genus, receiver/theorem/endpoint credit, or Stage32 closure.

## Current authority

PR #1765 is merged at `98c5710dad4ca9a006e93b273ecf5259733e03aa`; it is not an active working PR. Current Stage32 routing must be read from `stages/stage32/MAIN-STATE.json`, not the old #1765 base SHA. Later unmerged EX5 research remains retained only at its exact audited boundary until separately integrated.

The retained local EX5 state/evidence remains mathematical provenance; cross-lane coordination state changes routing priority only and creates no mathematical credit.

## Retained boundary

BC2-24 remains the merged EX5 base result: 4 newly UNSAT parents, `19` retained UNKNOWN, 0 SAT; known parent-UNSAT lower bound `7145`; `172` other BC2-19 UNKNOWN identities remain uninferred. Later BC2-25/26 work may exist on an unmerged research PR, but it is deferred while the P0 HPADJ demand is OPEN.

The whole first block, whole stratum, and FULL178 remain open.

## Executable boundary

On a new `stage32ex5-mainbatch` invocation:

1. synchronize current MAIN routing;
2. inspect `CROSS-LANE-DEMANDS.json` and `CROSS-LANE-STATE.json`;
3. execute `S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1` before lower-priority local BC2 work while it remains OPEN;
4. produce only the smallest exact source-locked interface needed to preserve HPADJ population identity through terminal-to-Picard64 completion;
5. if the demand becomes SATISFIED, preserve its exact handoff receipt and stop at the audit/MAIN-consumption boundary;
6. never relabel UNKNOWN as UNSAT and do not broad/heavy scale out without its separate authorization gate.

Supplying or satisfying a cross-lane interface does not itself prove UNSAT, FULL178 closure, effectivity, receiver credit, theorem credit, endpoint credit, or Stage32 closure.

No Stage32 MAIN, N350, theorem, receiver, effectivity, endpoint, or Perfect Cuboid credit follows automatically.
