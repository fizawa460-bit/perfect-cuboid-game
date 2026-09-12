# Stage32 cross-lane demand startup contract

This contract governs operational dependencies between Stage32 research lanes. The machine authority is `stages/stage32/proof/CROSS-LANE-DEMANDS.json`.

Every ordinary `*-mainbatch` startup must inspect the registry before substantive local research.

- Producer rule: inspect all `OPEN` demands with `producer_lane` equal to this lane. If an OPEN demand has higher priority than the lane's current local route, supplying the exact requested artifact becomes the next route. Do not continue lower-priority local work merely because it was already in progress.
- Consumer rule: an `OPEN` demand means wait at the exact blocker and do not rebuild producer-owned mathematics. When the demand becomes `SATISFIED`, re-enter on the next mainbatch, validate the satisfying artifact path/blob/canonical and source-population semantics, then continue the consumer leaf immediately.
- `OBSOLETE` means the dependency is no longer load-bearing; record the reason rather than silently deleting history.
- Demand `SATISFIED` does not grant mathematical credit. Hostile audit, exact source locks, claim synchronization, current-target adapters, and explicit MAIN promotion remain separate requirements.
- MAIN monitors all OPEN demands for cycles, orphan producer/consumer lanes, producer diversion into lower-priority local work, missing consumer re-entry wiring, and hostile-audited results that still require MAIN consumption.

The demand DAG and mathematical claim DAG are intentionally separate. A demand-status transition alone must not mutate `CLAIM-REGISTRY.json`, `ACTIVE-FRONTIER.json`, theorem/receiver/effectivity/endpoint credit, or merge authorization.
