# Stage32 canonical command surface

This file is the single human-facing command registry for ordinary Stage32 operation. It changes no mathematical authority or credit. Current mathematical routing still comes from `stages/stage32/MAIN-STATE.json` and exact retained/audited evidence.

## ACTIVE commands

### `stage32mainbatch`

Primary Stage32 controller **and researcher**.

Responsibilities:
- coordinate the current Stage32 frontier, integration, claim/audit transitions, and handoffs;
- continue mathematics directly when `MAIN-STATE.json` explicitly routes the current leaf to MAIN;
- perform cross-lane adapters, synthesis, same-object identity work, and genuinely unowned research needed to decide the frontier;
- route dedicated vertical work to the appropriate active specialist surface instead of duplicating it;
- consume retained/audited specialist results only through the required current-target adapter/claim-sync boundary.

This command is **not coordination-only**. It may do substantial mathematics. It must not start a duplicate FULL178 mission leaf already owned by `stage32-01-178-mainbatch`, a duplicate EX5 Picard64/producer leaf already owned by `stage32ex5-mainbatch`, a direct Picard64 completion-infeasibility leaf owned by `stage32cut-mainbatch`, or the 32-03 multibranch final-chain mission owned by `stage32mb-mainbatch`, unless current `MAIN-STATE.json` explicitly reassigns that work to MAIN.

### `stage32audit`

Hostile audit for an exact retained Stage32 MAIN boundary. Do not use it as a normal research command and do not treat PASS as merge authorization.

### `stage32-01-178-mainbatch`

Dedicated FULL178 numerical Picard-census research mission. Before research it must synchronize against current `stages/stage32/MAIN-STATE.json`; historical `MISSION.json` snapshots and Generation-1 lane returns are inputs, not current Stage32 routing authority.

Execution mode is single-researcher breadth-cycle. It may rotate mathematical routes inside one chat. It must not fan out `-a/-b/...` child lanes unless the user explicitly re-enables parallel dispatch.

### `stage32-01-178-audit`

Hostile audit only when the 178 MAINBATCH freezes a new exact retained boundary.

### `stage32ex5-mainbatch`

Dedicated Stage32EX5 auxiliary producer/research surface for FULL178 Picard64/node-support obstruction and related retained producer work. It must synchronize against current Stage32 MAIN before opening a new leaf and must not self-promote to Stage32 MAIN credit.

PR #1765 / BC2-24 is already merged history. A new invocation starts from current main and considers the bounded post-merge BC2-25 continuation; it must not resume the old merge-first stop condition.

### `stage32ex5-audit`

Hostile audit only after EX5 MAINBATCH freezes a new exact retained checkpoint. PR #1765 is historical/merged and is not the current audit target.

### `stage32cut-mainbatch`

Dedicated auxiliary FULL178 **direct completion obstruction** researcher. It consumes an already retained/source-locked exact Picard64 completion interface and researches finite-ring/modular infeasibility first, followed only if necessary by exact dual/Farkas or proof-producing integer infeasibility certificates.

CUT must not build or repair the EX5 terminal-to-Picard64 adapter, work on EX5 BC2-25 node-support/UNKNOWN identity refinement, or duplicate 178 prefix/exceptional-mass/block-sum/transport/maxcut/N356 work. Its startup contract is `stages/stage32/full178-cut/MAIN-START-HERE.md` and its mission is `stages/stage32/full178-cut/MISSION.json`.

### `stage32cut-audit`

Hostile audit only after CUT freezes an exact retained obstruction/checkpoint. PASS does not grant MAIN pruning credit or merge authorization by itself.

### `stage32mb-mainbatch`

Dedicated auxiliary Stage32 **32-03 multibranch final-chain** researcher. It advances the R29-LG2-MB population/normalization, local delta/genus accounting, Aut(S) quotient, justified finite window, and later Picard/effectivity backend. The lane is explicitly independent of FULL178 execution and may run concurrently with 178, EX5, and CUT.

MB must not borrow the unibranch 176/192 caps without a new proof, rerun V6/O210/Q602 exclusions, or revive dominated EX6 O266 tensor routes. Its startup contract is `stages/stage32/final-chain/32-03-multibranch/MAIN-START-HERE.md` and its mission is `stages/stage32/final-chain/32-03-multibranch/MISSION.json`.

### `stage32mb-audit`

Hostile audit only after MB freezes an exact retained checkpoint. PASS does not grant receiver/final-milestone/theorem credit or merge authorization by itself.

## NOT ordinary active commands

The following are historical, returned, merged, superseded, or on-demand research surfaces and must not be silently reactivated by ordinary startup:

- `stage32-01-178-a` through `stage32-01-178-f` — Generation-1 returned/consumed lanes;
- `stage32ex5-a` through `stage32ex5-h` — historical additive BC2 bridge lanes;
- `stage32-01-178-smith` — audited/recovered research checkpoint, not an ordinary live command;
- EX1 through EX4 separate ordinary lane startup — integrated/closed for ordinary routing unless current Stage32 authority explicitly reopens one;
- spelling variants such as `Stage32-main-batch`, `stage32main batch`, or `stage32 mainbatch` — noncanonical aliases; documentation must use `stage32mainbatch`.

## Routing precedence

For ordinary operation:

`Stage32 MAIN-STATE explicit current routing` > `this command ownership table` > `historical mission/roadmap/controller text`.

When two active commands could plausibly attack the same mathematics, do not run both independently. MAIN chooses/records ownership; the specialist lane executes the vertical leaf; MAIN later integrates the result. Parallelism is enabled only for the explicit nonoverlapping ownership split above.

Current intended split is:

- 178: FULL178 numerical/prefix/incidence/transport pruning and census;
- EX5: Picard64/node-support interface production and refinement;
- CUT: direct infeasibility certificates consuming an exact Picard64 completion interface;
- MB: independent 32-03 multibranch final-chain research;
- MAIN: current authority, cross-lane synthesis, promotion, and genuinely unowned mathematics.

## Startup rule

All five active research commands (`stage32mainbatch`, `stage32-01-178-mainbatch`, `stage32ex5-mainbatch`, `stage32cut-mainbatch`, `stage32mb-mainbatch`) must read this registry during startup and then synchronize against current Stage32 MAIN authority before substantive new work.

Replay the command-surface guard with:

`python stages/stage32/verify_command_surface.py`
