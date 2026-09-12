# Stage32 canonical command surface

This file is the single human-facing command registry for ordinary Stage32 operation. It changes no mathematical authority or credit. Current mathematical routing comes from `stages/stage32/MAIN-STATE.json`; current operational cross-lane dependencies come from `stages/stage32/proof/CROSS-LANE-DEMANDS.json`.

## Cross-lane demand routing

All active `*-mainbatch` surfaces must inspect `stages/stage32/proof/CROSS-LANE-DEMANDS.json` before substantive local work.

- Producer: a higher-priority OPEN demand preempts lower-priority local research until SATISFIED, OBSOLETE, or explicitly reprioritized by MAIN.
- Consumer: an OPEN demand means wait rather than duplicate producer work.
- Demand SATISFIED does not grant mathematical credit; hostile audit, claim synchronization, MAIN promotion, replacement-head re-audit, and merge authorization remain separate.
- MAIN monitors cycles, orphan demands, producer diversion, consumer re-entry wiring, and audited results awaiting promotion.

Current transition: MAIN V19 exact head `56c52a64dc402126431a6de6d023007052f4112c` has hostile-audit PASS review `5186730520`. N358 remains consumed with exact incremental rejection **9,274,971,107,798,843,958 terminals**, and the authoritative numerical residual remains **17,128 strata / 47,589,703,313,957,134,886,123 terminals**. V20 consumes that replacement-head audit with zero numerical change. N372 PR #1797 had hostile-audit FAIL review `5186762166` on superseded head `eafc5e4a18b30e25330eb01d3817020fa59a207c` for incomplete transitive source-lock closure; repaired exact head `9fb78a0e0c7b52baca84058dea69b8b083e33774` now has exact-head CI `34700502007` SUCCESS and is selected only as the next FULL178 witness candidate. N372 remains `current_v15_witness_candidate_only`, carries zero MAIN/effectivity/FULL178 credit, and must pass `stage32-01-178-audit` re-audit plus later current-authority rebase before any promotion. V20 itself must pass `stage32audit`. CUT197 remains deferred with zero MAIN credit.

Historical demand `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` remains **SATISFIED**; CUT193 is retained only as historical re-entry provenance. CUT191 is already consumed. CUT194, N357, CUT195, CUT196, and N358 are separately accounted under current `MAIN-STATE.json`. CUT193, CUT197, and N372 retain zero MAIN pruning credit.

## ACTIVE commands

### `stage32mainbatch`
Primary Stage32 controller and researcher. It owns authority integration, cross-lane synthesis, promotion, and genuinely unowned mathematics. It must not duplicate specialist-owned sustained leaves.

### `stage32audit`
Hostile audit for an exact retained Stage32 MAIN boundary. PASS is not merge authorization.

### `stage32-01-178-mainbatch`
Dedicated FULL178 numerical Picard-census specialist. Startup contract: `stages/stage32/32-01-178/MAIN-START-HERE.md`.

### `stage32-01-178-audit`
Hostile audit only after 178 freezes a new exact retained boundary. N372 is currently at this gate.

### `stage32ex5-mainbatch`
Dedicated Picard64/node-support producer/refinement surface. EX5 never self-promotes to MAIN credit.

### `stage32ex5-audit`
Hostile audit only after EX5 freezes a new exact retained checkpoint.

### `stage32cut-mainbatch`
Dedicated direct-completion obstruction consumer. CUT197 wave5 remains deferred and receives no MAIN credit until retained exact-head CI, hostile audit, and current-authority composition are complete.

### `stage32cut-audit`
Hostile audit only after CUT freezes an exact retained obstruction/checkpoint. PASS alone never grants MAIN credit.

### `stage32mb-mainbatch`
Dedicated 32-03 multibranch final-chain researcher. It remains independent of FULL178 execution and does not own MAIN promotion.

### `stage32mb-audit`
Hostile audit only after MB freezes an exact retained checkpoint.

## Routable EX lanes

EX1 through EX6 remain enrolled in `LANE-ADAPTERS.json` for machine routing. Ordinary separate EX1-EX4/EX6 research stays inactive unless current Stage32 authority or a valid demand explicitly reopens it.

## NOT ordinary active commands

- `stage32-01-178-a` through `stage32-01-178-f` — historical Generation-1 lanes.
- `stage32ex5-a` through `stage32ex5-h` — historical additive lanes.
- `stage32-01-178-smith` — audited/recovered checkpoint.
- spelling variants such as `Stage32-main-batch`, `stage32main batch`, or `stage32 mainbatch` — noncanonical.

## Routing precedence

Mathematical authority: `Stage32 MAIN-STATE explicit routing` > exact retained/audited evidence.

Operational scheduling: `higher-priority OPEN cross-lane demand` > local specialist route > historical roadmap text.

The demand layer cannot change mathematical authority by itself.

Current ownership split: 178 = FULL178 numerical census; EX5 = Picard64/node-support producer; CUT = direct infeasibility certificates; MB = multibranch final chain; MAIN = authority, coordination, synthesis, and promotion.

## Startup rule

All active mainbatch commands and routable EX startup contracts read `stages/stage32/proof/CROSS-LANE-DEMANDS.json` before substantive work.

`python stages/stage32/proof/verify_cross_lane_demands.py`

`python stages/stage32/verify_command_surface.py`
