# Stage32 MAIN startup

This file is the single ordinary startup contract for Stage32.

## Operator surface

Normal work has two user-facing commands:

- `stage32mainbatch` — continue Stage32 research.
- `stage32audit` — audit a frozen Stage32 boundary.

All former lane-specific commands are internal execution details. The operator does not need to choose EX5, MB, MB-FIB, 178, CUT, or BRIDGE before starting.

## Ordinary `stage32mainbatch` startup

Read only, in this order:

1. `AGENTS.md`;
2. this file;
3. `stages/stage32/MAIN-STATE.json`;
4. the current formal unit in `stages/stage32/ROADMAP.md`;
5. that unit's live state/startup boundary;
6. only the exact evidence required by that boundary.

Do not preload specialist history, old controller snapshots, `CROSS-LANE-DEMANDS.json`, Research OS policy files, or archived audit receipts. They are on-demand dependencies.

## Dispatch algorithm

Use `MAIN-STATE.json` to identify the current incomplete formal unit.

- `32-01` is audited complete and retained. Do not restart 178/CUT/BRIDGE work unless MAIN explicitly reopens a concrete obligation or a verified regression invalidates the retained claim.
- `32-02` is the primary active unit. Dispatch to its effectivity state and, only when required by that state, the EX5/Picard64 backend.
- `32-03` is the parallel active unit. Dispatch to the MB state when it is the selected useful work; MB may dispatch to MB-FIB only through its own explicit resume/audit handoff.
- `32-04` starts only after 32-02 and 32-03 satisfy their roadmap close criteria.
- `32-05` is external hostile audit. MAIN must stop before self-awarding Stage32 closure.

Default rule: continue 32-02. Use 32-03 when 32-02 is blocked or when already-running/resumable 32-03 work makes parallel progress preferable.

The dispatch decision belongs to MAIN. A user should not need to know which internal PR or historical lane implements the selected work.

## Internal execution isolation

Separate PRs, states, workflows, and audit boundaries may remain where they are technically useful for heavy-run authorization, checkpoint/resume, provenance, or hostile audit.

This isolation does not create additional operator entrypoints. Internal execution surfaces are subordinate to the selected formal roadmap unit and cannot independently change MAIN authority.

## Authority and credit

`MAIN-STATE.json` is the mutable routing projection. `ROADMAP.md` defines formal mathematical units and close criteria. Claim registries, exact source locks, retained certificates, adapters, and hostile-audit receipts control mathematical credit.

A specialist result changes MAIN authority only through its applicable audited handoff/promotion boundary. Never double-count overlapping restrictions or savings.

## Writeback and stop

Before stopping, update only the live state actually relied upon by the selected work and any required audited handoff. Do not refresh unrelated parked specialists merely for bookkeeping.

Stop when:

- the selected unit exposes a precise residual/tool/theorem wall;
- 32-02 and 32-03 are complete and 32-04 requires synthesis;
- 32-04 is complete and 32-05 external audit is next;
- an applicable safety/audit gate requires a hold.

Do not merge without explicit user authorization.
