# Stage32 CUT startup

Ordinary `stage32cut-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. `stages/stage32/full178-cut/MAIN-START-HERE.md`;
4. `stages/stage32/full178-cut/MISSION.json`;
5. current `stages/stage32/MAIN-STATE.json`;
6. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
7. `stages/stage32/full178-cut/CROSS-LANE-STATE.json` when CUT is waiting on a demand;
8. only the exact source/interface assets required by the current CUT node.

The current Stage32 mathematical routing authority remains `stages/stage32/MAIN-STATE.json`. Cross-lane demand state governs operational wait/re-entry only. This lane cannot promote itself to MAIN credit.

## Cross-lane demand routing

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`.

Before local CUT research, inspect OPEN demands. If CUT is producer for a higher-priority OPEN demand, supply that artifact before lower-priority local work. If CUT is consumer for an OPEN demand, wait at the exact blocker and do not rebuild producer-owned mathematics. When that demand becomes SATISFIED, the next `stage32cut-mainbatch` must immediately validate the satisfying artifact path/blob/canonical, source locks, and current population semantics, then re-enter the blocked CUT node.

Demand SATISFIED does not grant mathematical credit. Hostile audit, claim sync, current-target adapter and explicit MAIN consumption remain required.

Current CUT192 coordination state waits on `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1`, produced by EX5. CUT191 is independent of that wait and its hostile-audited 113-terminal result is already consumed into MAIN V12 authority.

## Ownership

CUT owns direct infeasibility research on an already source-locked exact Picard64 completion system: finite-ring/modular obstruction first, then exact dual/Farkas or proof-producing integer infeasibility only if needed.

CUT does **not** own:

- construction or repair of the EX5 indexed-terminal -> Picard64 completion adapter;
- EX5 BC2 node-support/UNKNOWN identity refinement;
- the 178 lane's prefix, exceptional-mass, block-sum, transport, maxcut, N356/N357, or equivalent numerical cut work;
- MAIN authority promotion, claim-DAG mutation, final milestone integration, or merge.

If a required exact completion interface is absent, stale, or insufficiently source-locked for the chosen bounded case, stop with a precise blocker and retain/update the cross-lane demand. Do not rebuild EX5 mathematics inside CUT.

## Exact-population rule

Always begin from the current **authoritative** survivor population in `MAIN-STATE.json`. An unaudited candidate on another branch is not input authority merely because it exists.

Any obstruction must identify the exact terminal/block/stratum it certifies and an exact population-preserving preimage. Do not extrapolate a bounded certificate to other strata.

## Route order

1. inspect demand registry and resolve any consumer wait/re-entry;
2. replay/freeze the exact completion interface and target scope;
3. try bounded finite-ring completion infeasibility;
4. certify exact scope and preimage;
5. only if needed, try exact rational dual/Farkas infeasibility, then proof-producing integer-specific infeasibility;
6. freeze a retained checkpoint, blocker, or audit handoff.

The historical N105 route discovery is a seed, not current routing authority. Its direct-Picard modular and dual candidates may be reopened only through the current exact interface and current MAIN population.

## Handoff and audit

A useful retained CUT result receives zero Stage32 MAIN pruning credit until its exact boundary is hostile-audited and MAIN explicitly consumes it through the required current-target/claim-sync procedure. `stage32cut-audit` is audit-only and does not merge or self-promote.

Do not merge without explicit user authorization.
