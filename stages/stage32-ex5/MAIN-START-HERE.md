# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex5/MAIN-START-HERE.md`;
3. `stages/stage32-ex5/MAIN-STATE.json`;
4. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This file is the fixed ordinary startup contract. Mutable frontier, route-cycle version, current leaf, blockers, audit status, and next route live only in `MAIN-STATE.json`. The final route-decision contract lives in `stages/stage32-ex5/stage32-ex5.md`.

Do not preload Stage32 history/controllers, other Stage32EX roadmaps, Research OS, Arsenal, or large retained payloads unless `AGENTS.md`, `MAIN-STATE.json`, or the active leaf explicitly triggers them.

## Authority split

`MAIN-STATE.json` is a routing/resume projection, not a proof certificate. Receiver rows, route status, and mathematical effects require exact source locks, retained leaf artifacts, verifiers, and hostile-audit records.

Stage32 MAIN is read as routing/source context only where the current leaf requires it. Stage32EX5 does not inherit unaudited Stage32 or other-stage candidates as theorem authority.

The EX5 completion state is `EX5_ROUTE_DECISION_CLOSURE`, not Stage32 `FULL_TARGET_CLOSURE`.

## `stage32ex5-mainbatch` execution contract

A batch:

1. identifies exactly one current mathematical/route-qualification unit;
2. revalidates every load-bearing receiver/source input needed by that unit;
3. executes one bounded unit;
4. retains only results with explicit receiver scope, field/model, quantifier, assumptions, and replay path;
5. updates the leaf artifact/verifier when appropriate, then updates `MAIN-STATE.json` with route status, credit ceiling, blocker/re-entry condition, and next route;
6. stops at a coherent checkpoint instead of silently widening the frozen breadth package.

A failed route is not EX5 exhaustion. Record its stable route identity and blocker, then move to a materially distinct route. Exhaustion is only the bounded outcome defined by the frozen package in the roadmap.

## Receiver/asset discovery discipline

During EX5-00..02, global finite-target/receiver semantics may open only the on-demand authority paths explicitly referenced by current Stage32 state or the active source-lock contract.

During EX5-04, existing weapon lookup must follow:

`docs/research-os/policies/repository-asset-discovery.md`
`-> docs/arsenal/index.json`
`-> relevant generated card`.

Do not use repository-wide search misses as proof of absence. Do not recursively enumerate the repository.

## Timeout-safe execution

Use scratch branches for route-family microdiagnostics. Scratch results are non-authoritative. Consolidate retained successful leaves only at coherent checkpoints; freshness synchronization and broad exact-head CI belong at consolidation/audit-ready checkpoints rather than after every diagnostic.

Heavy/artifact-producing workflows require the repository heavy-workflow policy and an explicit authorization gate. This startup file does not authorize heavy compute.

## `stage32ex5-audit` handoff

`stage32ex5-audit` is a separate hostile-audit lane and follows `stages/stage32-ex5/AUDIT-CONTRACT.md`. It audits an exact candidate head independently and does not continue research or repair the branch.

Audit PASS establishes only the audited EX5 route-decision ceiling. It does not merge, does not alter Stage32 MAIN, and does not automatically promote a selected route.

## Search, write, and merge discipline

Repository discovery is search-first under `AGENTS.md`. Preserve source/proof locks and current firewalls before writes. Do not merge without explicit user authorization.
