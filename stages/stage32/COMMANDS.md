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

This command is **not coordination-only**. It may do substantial mathematics. It must not start a duplicate FULL178 mission leaf already owned by `stage32-01-178-mainbatch`, or a duplicate EX5 Picard64/producer leaf already owned by `stage32ex5-mainbatch`, unless current `MAIN-STATE.json` explicitly reassigns that work to MAIN.

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

When two active commands could plausibly attack the same mathematics, do not run both independently. MAIN chooses/records ownership; the specialist lane executes the vertical leaf; MAIN later integrates the result. Parallelism is re-enabled only when the decomposition is explicit and nonoverlapping.

## Startup rule

All three active research commands (`stage32mainbatch`, `stage32-01-178-mainbatch`, `stage32ex5-mainbatch`) must read this registry during startup and then synchronize against current Stage32 MAIN authority before substantive new work.

Replay the command-surface guard with:

`python stages/stage32/verify_command_surface.py`
