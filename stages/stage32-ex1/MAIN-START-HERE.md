# Stage32EX1 MAIN startup

Ordinary `stage32ex1-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex1/MAIN-START-HERE.md`;
3. `stages/stage32-ex1/MAIN-STATE.json`;
4. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This file is the fixed ordinary startup contract. Mutable frontier, current leaf, blockers, audit status, and next route live only in `MAIN-STATE.json`. The goal/dependency contract lives in `stages/stage32-ex1/stage32-ex1.md` and is opened only when the current working set or active task requires it.

Do not preload the Stage32 root, Stage32 history/controllers, other Stage32EX roadmaps, Research OS, Arsenal, or large retained payloads unless `AGENTS.md`, `MAIN-STATE.json`, or the active leaf explicitly triggers them.

## Authority split

`MAIN-STATE.json` is the mutable Stage32EX1 routing/resume projection. It is not a proof certificate and cannot create mathematical credit by assertion.

Exact claims must be grounded in source locks, leaf artifacts, verifiers, and hostile-audit records referenced by the state. Stage32 MAIN may be read as routing/source context only where the active leaf explicitly requires it; Stage32EX1 does not inherit an unaudited Stage32 candidate as theorem authority.

The final mathematical target and credit hierarchy are fixed by `stage32-ex1.md`. A compact state update may select the next route but may not weaken that final target.

## `stage32ex1-mainbatch` execution contract

A batch does the following:

1. read the startup set above and identify exactly one current mathematical unit;
2. revalidate every load-bearing input needed by that unit through exact source locators;
3. execute the bounded mathematical/diagnostic unit;
4. retain only results that have an explicit claim scope, assumptions, quantification domain, and replay path;
5. update the leaf artifact/verifier when appropriate, then update `MAIN-STATE.json` with result, credit ceiling, blocker/reopen condition, audit readiness, and next route;
6. stop at a coherent checkpoint rather than silently broadening the target.

A failed technique is not Stage32EX1 exhaustion. When a route blocks, record `LEAF_BLOCKED` or `ROUTE_BLOCKED`, use the cycle-exploration policy when its trigger is met, and move to a materially distinct legal route. A finite residual ledger or missing-data diagnosis remains an active work queue until EX1-06 closure or an explicit genuine survivor is established.

## Timeout-safe execution

For micro-diagnostics, prefer a scratch branch or isolated working branch rather than pushing every experiment to a shared audit candidate. Scratch results are non-authoritative. Consolidate only retained successful leaves into the working PR at an audit-ready checkpoint; perform freshness synchronization and broad exact-head CI at that checkpoint rather than after every micro-diagnostic.

Heavy/artifact-producing workflows require the repository heavy-workflow policy and an explicit authorization gate. This startup file does not authorize heavy compute.

## `stage32ex1-audit` handoff

`stage32ex1-audit` is a separate hostile-audit lane. It follows `stages/stage32-ex1/AUDIT-CONTRACT.md`, audits an exact candidate head independently, and does not treat the mainbatch narrative as evidence.

A hostile-audit FAIL sends the same working lineage back to `stage32ex1-mainbatch` for repair. A PASS records only the audited Stage32EX1 claim ceiling; it does not automatically merge, alter Stage32 MAIN authority, or grant endpoint credit.

## Search, write, and merge discipline

Repository discovery is search-first under `AGENTS.md`. Existing weapon/evidence lookup follows the repository asset-discovery policy only when the active leaf needs it. Do not infer repository-wide absence from a search miss.

Before writes, preserve source/proof locks and current firewalls. Do not merge without explicit user authorization.
