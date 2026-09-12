# Stage32 canonical command surface

This file is the single human-facing command registry for ordinary Stage32 operation. It changes no mathematical authority or credit. Current mathematical routing comes from `stages/stage32/MAIN-STATE.json`; current operational cross-lane dependencies come from `stages/stage32/proof/CROSS-LANE-DEMANDS.json`.

## Cross-lane demand routing

All active `*-mainbatch` surfaces must inspect `stages/stage32/proof/CROSS-LANE-DEMANDS.json` before substantive local work. Higher-priority OPEN producer demands preempt lower-priority local work; consumers wait rather than duplicate producer work. Demand SATISFIED never grants mathematical credit.

Historical demand `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1` remains **SATISFIED**. CUT193 subsequently re-entered and is now part of the V22 batch composition below. CUT191 is already consumed.

## Current MAIN transition

Hostile-audited V21 exact head `62768270a39b23c358f11b3a75bccae5d7cea0f6` has PASS review `5188129691`.

V22 batch-composes three previously audited but unconsumed CUT results against that exact current authority in one fail-closed replay:

- CUT193: exact head `5b2ebb3f67805eddefef835878ba4b9744bfdbd9`, review `5180126251`, **25,651** terminals, survivor offsets `1..255`.
- CUT197: exact head `adce53dc9004c24bffb3ba9f88e9d5d6e51cf6a5`, review `5186601376`, **28,250** terminals, survivor offsets `1021..1275`.
- CUT198: exact head `16e439bc65e723c9f2658c274d53fb839738dcd2`, review `5188018895`, **28,024** terminals, survivor offsets `1276..1530`.

The single composition verifier reconstructs the exact `g1-d008/e8` 7,596-block N357 survivor sequence, proves the three new waves mutually disjoint, proves disjointness from already-consumed CUT191/CUT194/CUT195/CUT196 waves, proves zero N357 overlap, and source-locks the N358 proof that its incremental domain is empty on `g1-d008/e8`. Total incremental rejection is **81,925 terminals**.

Candidate V22 authority is therefore **17,128 strata / 47,589,703,313,957,134,804,198 terminals**. N372 remains a current-authority witness because survivor offset `797` is outside all three newly consumed waves. FULL178 remains incomplete. No effectivity-final, receiver, theorem, endpoint, Stage32 closure, Perfect-Cuboid, or merge credit is granted. V22 requires `stage32audit` before any further MAIN authority promotion.

## ACTIVE commands

### `stage32mainbatch`
Primary Stage32 controller and researcher. Owns authority integration, cross-lane synthesis, promotion, and genuinely unowned mathematics.

### `stage32audit`
Hostile audit for an exact retained Stage32 MAIN boundary. PASS is not merge authorization.

### `stage32-01-178-mainbatch`
Dedicated FULL178 numerical Picard-census specialist. Startup contract: `stages/stage32/32-01-178/MAIN-START-HERE.md`.

### `stage32-01-178-audit`
Hostile audit after 178 freezes a new exact retained boundary.

### `stage32ex5-mainbatch`
Dedicated Picard64/node-support producer/refinement surface. EX5 never self-promotes to MAIN credit.

### `stage32ex5-audit`
Hostile audit after EX5 freezes a new exact retained checkpoint.

### `stage32cut-mainbatch`
Dedicated direct-completion obstruction consumer. CUT never self-promotes to MAIN authority.

### `stage32cut-audit`
Hostile audit for exact retained CUT obstruction/checkpoints. PASS alone never grants MAIN credit.

### `stage32mb-mainbatch`
Dedicated 32-03 multibranch final-chain researcher. Independent of FULL178 execution and does not own MAIN promotion.

### `stage32mb-audit`
Hostile audit after MB freezes a new exact retained checkpoint.

## Routable EX lanes

EX1 through EX6 remain enrolled in `LANE-ADAPTERS.json`. Ordinary separate EX1-EX4/EX6 research stays inactive unless current authority or a valid demand reopens it.

## Routing precedence

Mathematical authority: `Stage32 MAIN-STATE explicit routing` > exact retained/audited evidence.

Operational scheduling: `higher-priority OPEN cross-lane demand` > local specialist route > historical roadmap text.

The demand layer cannot change mathematical authority by itself. Current ownership split: 178 = FULL178 numerical census; EX5 = Picard64/node-support producer; CUT = direct infeasibility certificates; MB = multibranch final chain; MAIN = authority, coordination, synthesis, and promotion.

## Startup rule

All active mainbatch commands and routable EX startup contracts read `stages/stage32/proof/CROSS-LANE-DEMANDS.json` before substantive work.

`python stages/stage32/proof/verify_cross_lane_demands.py`

`python stages/stage32/verify_command_surface.py`
