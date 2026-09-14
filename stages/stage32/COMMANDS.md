# Stage32 canonical command surface

This file is the stable human-facing registry for Stage32 operator commands. It is not mathematical authority and must not duplicate current PR numbers, exact heads, authority-version transitions, terminal totals, lane-local retained state, or a lane's startup sequence.

Current mathematical routing/credit authority is `stages/stage32/MAIN-STATE.json`; current operational dependency authority is `stages/stage32/proof/CROSS-LANE-DEMANDS.json`. Lane startup entrypoints are resolved by `stages/stage32/proof/LANE-ADAPTERS.json`. Most active lanes point to a `MAIN-START-HERE.md`; Stage32EX5 is intentionally collapsed to `stages/stage32-ex5/MAIN-STATE.json` so retired readme/startup/roadmap mirrors cannot compete with live state. This registry resolves commands to those entrypoints and is not a second startup contract.

If the live MAIN authority identity cannot be resolved, or a lane-local mirror conflicts with the authority being consumed, fail closed before substantive research. Historical receipts, snapshots, roadmaps, and mission DAGs remain evidence/history unless current routing explicitly selects them. Demand status and mathematical credit remain separate.

## ACTIVE commands

- `stage32mainbatch` — primary Stage32 controller/researcher for authority integration, demand coordination, cross-lane synthesis, promotion, and genuinely MAIN-owned/unowned mathematics. Startup: `stages/stage32/MAIN-START-HERE.md`.
- `stage32audit` — hostile audit for an exact retained MAIN boundary. PASS is not promotion, merge-ready freshness, or merge authorization.
- `stage32-01-178-mainbatch` — sustained FULL178 numerical-census specialist. Startup: `stages/stage32/32-01-178/MAIN-START-HERE.md`.
- `stage32-01-178-audit` — hostile audit after a new exact retained 178 boundary is frozen.
- `stage32ex5-mainbatch` — Picard64/node-support producer/refinement specialist; never self-promotes to MAIN credit. Startup: `stages/stage32-ex5/MAIN-STATE.json`.
- `stage32ex5-audit` — hostile audit after a new exact retained EX5 checkpoint is frozen.
- `stage32cut-mainbatch` — direct completion infeasibility/obstruction consumer/research specialist; never self-promotes to MAIN authority.
- `stage32cut-audit` — hostile audit for an exact retained CUT checkpoint; PASS alone grants no MAIN credit.
- `stage32mb-mainbatch` — independent 32-03 multibranch final-chain specialist; does not own MAIN promotion.
- `stage32mb-audit` — hostile audit after a new exact retained MB checkpoint is frozen.

## On-demand and historical surfaces

`stage32certlift-mainbatch` and the 32-02 scalar experiment are on-demand, not ordinary active commands; new work requires explicit current MAIN assignment. EX1-EX4 and EX6 may remain machine-enrolled in `LANE-ADAPTERS.json`, but ordinary separate EX research is inactive unless current authority or a valid demand reopens it. EX5 is the active specialist listed above. Historical child commands such as `stage32-01-178-a..f`, `stage32ex5-a..h`, and checkpoint-specific commands are not ordinary startup surfaces unless MAIN explicitly re-enables them.

## Routing precedence and ownership

Mathematical authority: `MAIN-STATE explicit routing` > exact retained/audited evidence > historical roadmap/snapshot text.

Operational scheduling inside that authority: `higher-priority applicable OPEN demand` > current lane route > historical roadmap text. The demand layer cannot change mathematical authority by itself.

Stable ownership split: 178 = sustained FULL178 census/incidence/transport/completeness; EX5 = Picard64/node-support interface production/refinement; CUT = direct infeasibility/obstruction consuming exact producer interfaces; MB = 32-03 multibranch research; MAIN = authority, coordination, cross-lane synthesis, promotion, and genuinely unowned mathematics. No two surfaces independently own the same semantic leaf without explicit MAIN reassignment.

## Guards

Cross-lane demand guard: `python stages/stage32/proof/verify_cross_lane_demands.py`

Command/startup-surface guard: `python stages/stage32/verify_command_surface.py`

This registry grants no mathematical credit and no merge authorization.
