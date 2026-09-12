# Stage32 32-01-178 MAIN startup

Ordinary `stage32-01-178-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. current `stages/stage32/MAIN-STATE.json`;
4. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. this file;
6. `stages/stage32/32-01-178/MISSION.json`;
7. only the exact current node/state/assets selected by current MAIN routing and the mission.

The parent Stage32 `MAIN-STATE.json` remains the current mathematical routing authority. Historical mission snapshots and Generation-1 returns are inputs, not current routing authority.

## Cross-lane demand routing

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`.

Before sustained FULL178 research, inspect every OPEN demand involving lane `32-01-178`. If this lane is producer for a higher-priority OPEN demand, the requested exact artifact preempts lower-priority local work until SATISFIED, OBSOLETE, or explicitly reprioritized by MAIN. If this lane is consumer of an OPEN demand, wait at the exact blocker rather than duplicating producer work. When it becomes SATISFIED, re-enter on the next `stage32-01-178-mainbatch`, validate satisfying artifact identity/source-population semantics, then continue immediately.

Demand SATISFIED does not grant mathematical credit. Hostile audit, claim synchronization, current-target adapters, explicit MAIN consumption, and merge authorization remain separate.

## Ownership

This lane owns sustained FULL178 numerical Picard-census, prefix/incidence/transport/support-capacity pruning, completeness execution, and related exact population work currently routed to 32-01-178. It does not duplicate EX5 Picard64 producer/refinement, CUT direct completion-infeasibility, or MB multibranch final-chain research unless MAIN explicitly reassigns ownership.

N357 and successor FULL178 work remain zero MAIN credit until the required independent audit and MAIN consumption boundary.

## Execution discipline

Use one researcher breadth-cycle by default; historical `-a..-f` child lanes are not ordinary active fanout. Revalidate current MAIN authority before each retained leaf, preserve exact source/population semantics, and stop at a coherent retained checkpoint or precise blocker.

Heavy/artifact-producing work requires its separate authorization gate. This startup contract does not authorize heavy compute.

The cross-lane demand DAG is operational and separate from the mathematical claim DAG. A demand status change alone must not mutate claim authority.

Do not merge without explicit user authorization.
