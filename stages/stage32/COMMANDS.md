# Stage32 canonical command surface

This file is the single human-facing command registry for ordinary Stage32 operation. It changes no mathematical authority or credit. Current mathematical routing comes from `stages/stage32/MAIN-STATE.json`; current operational cross-lane dependencies come from `stages/stage32/proof/CROSS-LANE-DEMANDS.json`.

## Cross-lane demand routing

All active `*-mainbatch` surfaces must inspect `stages/stage32/proof/CROSS-LANE-DEMANDS.json` before substantive local work.

- Producer: a higher-priority OPEN demand preempts lower-priority local research until the requested artifact is SATISFIED, OBSOLETE, or explicitly reprioritized by MAIN.
- Consumer: an OPEN demand means wait rather than duplicate producer work; SATISFIED means immediate next-mainbatch re-entry after validating artifact identity and source-population semantics.
- Demand SATISFIED does not grant mathematical credit. The claim DAG, hostile audit, claim synchronization, current-target adapters, explicit MAIN promotion, and merge authorization remain separate.
- MAIN monitors cycles, orphan demands, producer diversion, consumer re-entry wiring, and hostile-audited results awaiting required MAIN consumption.

Current highest-priority demand is `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1`: EX5 must supply CUT with a source-locked exact terminal-to-Picard64 completion interface for a disjoint current-MAIN-surviving e=8 population, with exact rank/unrank semantics. CUT waits and must not rebuild it.

CUT191 is separate: its hostile-audited 113-terminal result is already consumed in Stage32 V12 authority. CUT192's EX5 wait must not block or revoke that consumed credit.

## ACTIVE commands

### `stage32mainbatch`

Primary Stage32 controller **and researcher**. It coordinates authority/integration/claim transitions, monitors the cross-lane demand DAG, performs cross-lane adapters and genuinely unowned mathematics, and consumes audited specialist results only through existing promotion rules. It must not duplicate specialist-owned sustained leaves unless current authority explicitly reassigns them.

### `stage32audit`

Hostile audit for an exact retained Stage32 MAIN boundary. PASS is not merge authorization.

### `stage32-01-178-mainbatch`

Dedicated FULL178 numerical Picard-census specialist. Startup contract: `stages/stage32/32-01-178/MAIN-START-HERE.md`. Before research it synchronizes current MAIN authority and cross-lane demands. Historical mission snapshots/Generation-1 returns do not override current routing. Default execution is one researcher breadth-cycle; historical `-a..-f` child fanout stays inactive unless explicitly re-enabled.

### `stage32-01-178-audit`

Hostile audit only after 178 freezes a new exact retained boundary.

### `stage32ex5-mainbatch`

Dedicated Picard64/node-support producer/refinement surface. It must synchronize current MAIN plus cross-lane demands. An OPEN producer demand with higher priority than local BC2 refinement takes precedence. EX5 never self-promotes to MAIN credit.

### `stage32ex5-audit`

Hostile audit only after EX5 freezes a new exact retained checkpoint.

### `stage32cut-mainbatch`

Dedicated direct-completion obstruction consumer. It consumes an already source-locked exact Picard64 completion interface and researches modular/finite-ring infeasibility first, then exact dual/Farkas or proof-producing integer infeasibility if required. Missing producer interface becomes an OPEN demand; CUT must not rebuild EX5 adapter mathematics. When that demand is SATISFIED, CUT re-enters immediately on its next mainbatch.

### `stage32cut-audit`

Hostile audit only after CUT freezes an exact retained obstruction/checkpoint. PASS does not itself grant MAIN pruning credit.

### `stage32mb-mainbatch`

Dedicated 32-03 multibranch final-chain researcher. It is independent of FULL178 execution but still participates in demand routing. It owns multibranch population/normalization, local delta/genus accounting, Aut(S) quotient, justified finite windows, and later Picard/effectivity work; it does not own MAIN promotion.

### `stage32mb-audit`

Hostile audit only after MB freezes an exact retained checkpoint.

## Routable EX lanes

EX1 through EX6 remain enrolled in `LANE-ADAPTERS.json` for machine routing even when some are completed, dominated, or stopped. Their `MAIN-START-HERE.md` contracts read the demand registry, so an explicit future OPEN demand/re-entry can be represented without inventing an out-of-band dependency.

Ordinary separate EX1-EX4/EX6 research remains inactive unless current Stage32 authority or a valid demand explicitly reopens it.

## NOT ordinary active commands

- `stage32-01-178-a` through `stage32-01-178-f` — historical Generation-1 returned/consumed lanes;
- `stage32ex5-a` through `stage32ex5-h` — historical additive lanes;
- `stage32-01-178-smith` — audited/recovered checkpoint, not ordinary live command;
- spelling variants such as `Stage32-main-batch`, `stage32main batch`, or `stage32 mainbatch` — noncanonical.

## Routing precedence

For mathematical authority:

`Stage32 MAIN-STATE explicit routing` > exact retained/audited evidence.

For operational scheduling within that mathematical authority:

`higher-priority OPEN cross-lane demand` > local specialist route > historical roadmap text.

The demand layer cannot change mathematical authority by itself.

Current ownership split:

- 178: FULL178 numerical/prefix/incidence/transport/support-capacity pruning and census;
- EX5: Picard64/node-support interface production and refinement;
- CUT: direct infeasibility certificates consuming exact Picard64 interfaces;
- MB: independent 32-03 multibranch final-chain research;
- MAIN: authority, demand coordination, cross-lane synthesis, promotion, and genuinely unowned mathematics.

## Startup rule

All active mainbatch commands and all routable EX startup contracts read `stages/stage32/proof/CROSS-LANE-DEMANDS.json` before substantive work. The machine guard is:

`python stages/stage32/proof/verify_cross_lane_demands.py`

The command-surface guard remains:

`python stages/stage32/verify_command_surface.py`
