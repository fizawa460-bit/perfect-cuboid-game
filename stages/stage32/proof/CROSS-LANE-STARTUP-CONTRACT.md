# Stage32 cross-lane demand contract

This contract governs internal operational dependencies after Stage32 MAIN has selected an execution surface.

The machine authority is `stages/stage32/proof/CROSS-LANE-DEMANDS.json`. It is **not** part of every ordinary `stage32mainbatch` startup. MAIN reads it only when the selected unit has a concrete producer/consumer dependency, handoff, or audit transition.

For a dispatched internal surface:

- inspect only demands that involve that surface;
- an `OPEN` producer demand may preempt lower-priority local work;
- an `OPEN` consumer demand means wait rather than duplicate producer-owned mathematics;
- a `SATISFIED` demand requires exact artifact/source-population validation before consumption;
- `OBSOLETE` records why a dependency is no longer load-bearing.

Demand state never grants mathematical credit. Hostile audit, exact source locks, claim synchronization, current-target adapters where applicable, and explicit MAIN consumption remain separate gates.

The demand DAG and mathematical claim DAG are intentionally separate. A demand-status transition alone must not mutate theorem, receiver, effectivity, endpoint, closure, merge, or Perfect-Cuboid credit.
