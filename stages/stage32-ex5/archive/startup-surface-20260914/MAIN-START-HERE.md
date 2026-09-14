# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order: `AGENTS.md`; `stages/stage32/COMMANDS.md`; current `stages/stage32/MAIN-STATE.json`; `stages/stage32/proof/CROSS-LANE-DEMANDS.json`; `stages/stage32-ex5/CROSS-LANE-STATE.json` when present; `README.md`; this file; `MAINBATCH-OPERATIONS.md`; `MAIN-STATE.json`; then only the active EX5 working set.

PR #1776 remains active/open/draft/unmerged. Merge is not authorized.

## Cross-lane demand priority

Before local work, inspect every OPEN demand with `producer_lane=EX5`. A higher-priority OPEN producer demand preempts lower-priority local work. A SATISFIED demand is only an operational handoff and **does not grant mathematical credit**.

The live synchronization retained by EX5 records zero OPEN EX5 producer demands. Both retained producer obligations are SATISFIED:

- `S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1`;
- `S32.DEMAND.HPADJ.EX5.FULL178_PICARD64.V1`.

These handoffs grant no Stage32 MAIN pruning, FULL178, theorem, endpoint, receiver, effectivity, or merge credit. EX5 remains a separate local producer/refinement surface and never self-promotes to MAIN authority.

## Current synchronized MAIN authority

EX5's retained live coordination snapshot is `LIVE-MAIN-COORDINATION-SYNC-20260914.json`, blob `c9a3a878413df5afc634f99b94707534412b5d84`, canonical `fd5c7c6d025286a5677b7dcab5113f066dff83574c4647d772d89c7799b8be6c`, from MAIN coordination PR #1800 at head `9d4a24ef479d031e9c4b85001fe8f7a10198b17d`.

The synchronized Stage32 MAIN schema is `STAGE32_MAIN_COMPACT_STATE_V24_HPADJ07_AUDIT_SYNCED`; authoritative remaining strata are `17128`; certified remaining-terminal upper bound is `26876434389242951089388`; FULL178 remains incomplete. EX5 does not mutate or auto-promote into that authority.

## Current EX5 authority — V33

BC2-39 hostile audit is PASS and consumed locally:

- hostile-audit exact head `4b974550d9ad030973fec99e19a090f6785f8aa8`;
- review `5193423203`;
- retained result `7 UNSAT / 23 UNKNOWN / 0 SAT`;
- audited known-parent UNSAT lower bound `7313`;
- remaining 23 UNKNOWN hash `29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02`.

The active EX5 schema is `STAGE32EX5_MAIN_COMPACT_STATE_V33_BC2_39_AUDIT_CONSUMED_BC2_40_PREFLIGHT`. Its fail-closed migration is covered by the shared Stage32 command/startup verifiers and the retained BC2 compatibility chain.

## BC2-40 preflight gate

BC2-40 is staged only for the exact 23 hostile-audited UNKNOWN parents. The retained producer is `breadth-cycle-2/bc2_40_replay_explicit_fresh_unknown23.py`; the preflight is `breadth-cycle-2/bc2-40-fresh-unknown23-replay-preflight.json`. Planned bounded execution is `180000 ms` per parent with at most one heavy runner and no scaleout.

No BC2-40 runkey is armed. Live execution remains `dedicated_runkey=null`, `effective_heavy_concurrency=0`, `runkey_armed=false`, and `heavy_scaleout_authorized=false`. The next exact gate is `BC2_40_FRESH_RUNKEY_AUTHORIZATION`; a fresh semantic runkey and fail-closed workflow authorization are required before any BC2-40 heavy execution. The V33 migration itself does not authorize compute.

UNKNOWN remains UNKNOWN. Any future SAT is Picard64-feasibility evidence only and cannot be promoted to an actual effective/irreducible curve.

No whole-first-block/whole-stratum/FULL178 closure, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, heavy scaleout, or merge is authorized.

Next ordinary command: `stage32ex5-mainbatch` at the BC2-40 fresh-runkey authorization gate. `stage32ex5-audit` is not active until a new exact BC2-40 result boundary is actually executed and frozen.
