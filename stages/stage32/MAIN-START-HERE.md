# Stage32 MAIN startup

This is the single ordinary operator entrypoint for Stage32.

The guiding rule is now simple: **follow the formal Stage32 roadmap, select the current incomplete unit, and open only the state needed for that unit.** Do not perform a repository-wide specialist sweep on every invocation.

## Ordinary `stage32mainbatch` startup

Read only, in this order:

1. `AGENTS.md`;
2. this file;
3. `stages/stage32/ROADMAP.md`;
4. current `stages/stage32/MAIN-STATE.json`;
5. the state/startup boundary for the roadmap unit actually selected below;
6. exact source/evidence files referenced by that selected boundary.

`CROSS-LANE-DEMANDS.json`, specialist history, old controller snapshots, Research OS policy files, and archived audit receipts are **on-demand**. Open them only when the selected unit has an actual dependency, handoff, audit transition, or policy trigger.

## Current roadmap position

The audited numerical-census obligation `32-01` is complete.

- **32-01 — COMPLETE / RETAINED.** `S32.FULL178.NUMERICAL_CENSUS.V2` is audited. Ordinary MAIN startup must not restart FULL178 numerical pruning merely because historical 178/CUT/BRIDGE surfaces exist.
- **32-02 — ACTIVE PRIMARY.** Effectivity/carrier disposal is the default MAIN target.
- **32-03 — ACTIVE PARALLEL.** Multibranch work may proceed independently when useful.
- **32-04 — BLOCKED.** Start only after 32-02 and 32-03 are complete.
- **32-05 — EXTERNAL AUDIT.** MAIN must not self-award final closure.

Default selection rule: work 32-02; if its exact next step is blocked or an already-running 32-03 job makes parallel progress useful, work 32-03. Do not reopen 32-01 without an explicit current MAIN reassignment or a demonstrated regression in the audited numerical claim.

## Internal execution surfaces

The user-facing operating command is `stage32mainbatch`. Specialist commands remain available as internal/on-demand execution surfaces, not as competing Stage32 controllers.

- 32-02 may dispatch to the EX5 affine/Picard backend when its exact certificate is needed.
- 32-03 may dispatch to MB; MB may consume MB-FIB only through its explicit retained/audited handoff rules.
- 178, CUT, and BRIDGE are parked/retained after 32-01 completion unless MAIN explicitly reopens a concrete obligation.

Keeping separate execution PRs is intentional: heavy-run authorization, resume state, and hostile-audit boundaries should not be collapsed into one giant PR. The **operator entrypoint is unified; execution surfaces are isolated only where technically useful.**

## Authority and credit

`MAIN-STATE.json` is the mutable ordinary-startup projection. Exact mathematical credit still comes from retained certificates, exact source locks, claim synchronization, and hostile audits.

A specialist result does not change MAIN authority merely because it exists. MAIN consumes a handoff only through the applicable adapter/audit/promotion boundary. No additive double counting is allowed.

## Status writeback

Before stopping, update `MAIN-STATE.json` only for information actually relied upon during this run: current roadmap unit, selected live execution surface, audit/handoff status, and blocking reason. There is no requirement to refresh unrelated parked specialists.

Do not merge without explicit user authorization.
