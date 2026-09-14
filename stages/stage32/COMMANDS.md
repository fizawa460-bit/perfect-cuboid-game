# Stage32 canonical command surface

This file is the stable human-facing registry for Stage32 operator commands. It is not mathematical authority and must not duplicate current PR numbers, exact heads, authority-version transitions, terminal totals, or lane-local retained state.

Current mathematical routing and credit authority is `stages/stage32/MAIN-STATE.json`.
Current operational cross-lane dependency authority is `stages/stage32/proof/CROSS-LANE-DEMANDS.json`.
Each lane's startup/read order belongs only in that lane's `MAIN-START-HERE.md`.

## Stable startup invariants

Before substantive work, every active `*-mainbatch` surface must:

1. resolve the live Stage32 MAIN authority surface rather than trusting a stale lane-local mirror;
2. inspect current `stages/stage32/MAIN-STATE.json`;
3. inspect current `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
4. follow the lane-local `MAIN-START-HERE.md` contract;
5. open only the exact current lane state and source/evidence required by that routing.

If the live MAIN authority identity cannot be resolved, or the lane-local mirror disagrees with it, fail closed before substantive research. Historical receipts, snapshots, roadmaps, and mission DAGs are evidence/history only unless current routing explicitly selects them.

Demand state and mathematical credit remain separate. `SATISFIED` means the requested operational artifact exists; it does not grant pruning, receiver, effectivity, theorem, endpoint, closure, or merge credit. Hostile audit, claim synchronization, current-target adapters, explicit MAIN promotion/consumption, merge-ready freshness, and merge authorization remain distinct gates.

## ACTIVE commands

### `stage32mainbatch`

Primary Stage32 controller and researcher. Owns authority integration, cross-lane synthesis, promotion, and genuinely MAIN-owned or unowned mathematics. Startup contract: `stages/stage32/MAIN-START-HERE.md`.

### `stage32audit`

Hostile audit for an exact retained Stage32 MAIN boundary. PASS is not MAIN promotion, merge-ready freshness, or merge authorization.

### `stage32-01-178-mainbatch`

Dedicated FULL178 numerical Picard-census specialist. Startup contract: `stages/stage32/32-01-178/MAIN-START-HERE.md`.

### `stage32-01-178-audit`

Hostile audit after 178 freezes a new exact retained boundary.

### `stage32ex5-mainbatch`

Dedicated Picard64/node-support producer/refinement surface. It never self-promotes to MAIN credit.

### `stage32ex5-audit`

Hostile audit after EX5 freezes a new exact retained checkpoint.

### `stage32cut-mainbatch`

Dedicated direct-completion obstruction consumer/research surface. It never self-promotes to MAIN authority.

### `stage32cut-audit`

Hostile audit for an exact retained CUT obstruction/checkpoint. PASS alone never grants MAIN credit.

### `stage32mb-mainbatch`

Dedicated 32-03 multibranch final-chain researcher. It is independent of FULL178 execution and does not own MAIN promotion.

### `stage32mb-audit`

Hostile audit after MB freezes a new exact retained checkpoint.

## On-demand and historical surfaces

`stage32certlift-mainbatch` and the 32-02 scalar experiment are on-demand surfaces, not ordinary active commands. New work on them requires explicit current MAIN assignment/routing; retained historical producer or adapter evidence is consumed only through current source-locked interfaces.

EX1 through EX6 may remain enrolled for machine routing where `LANE-ADAPTERS.json` says so, but ordinary separate EX research is inactive unless current MAIN authority or a valid cross-lane demand explicitly reopens it.

Historical child commands such as `stage32-01-178-a..f`, `stage32ex5-a..h`, and retained checkpoint-specific commands are not ordinary active startup surfaces unless current MAIN explicitly re-enables them.

## Routing precedence and ownership

Mathematical authority:

`Stage32 MAIN-STATE explicit routing` > exact retained/audited evidence > historical roadmap/snapshot text.

Operational scheduling inside that authority:

`higher-priority OPEN cross-lane demand` > current lane-local route > historical roadmap text.

The demand layer cannot change mathematical authority by itself.

Stable ownership split:

- 178: sustained FULL178 numerical census, prefix/incidence/transport/support-capacity and completeness work;
- EX5: sustained Picard64/node-support interface production and refinement;
- CUT: direct infeasibility/obstruction work consuming exact producer interfaces;
- MB: independent 32-03 multibranch final-chain research;
- MAIN: authority, demand coordination, cross-lane synthesis, promotion, and genuinely unowned mathematics.

No two surfaces should independently own the same semantic leaf without explicit current MAIN reassignment.

## Guards

Cross-lane demand guard:

`python stages/stage32/proof/verify_cross_lane_demands.py`

Command-surface guard:

`python stages/stage32/verify_command_surface.py`

This registry grants no mathematical credit and no merge authorization.
