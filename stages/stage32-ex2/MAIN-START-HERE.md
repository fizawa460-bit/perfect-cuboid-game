# Stage32EX2 MAIN startup

Ordinary `stage32ex2-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex2/MAIN-START-HERE.md`;
3. `stages/stage32-ex2/MAIN-STATE.json`;
4. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This file is the fixed ordinary startup contract. Mutable frontier, current leaf, blockers, audit status, and next route live only in `MAIN-STATE.json`. The mathematical target and dependency roadmap live in `stages/stage32-ex2/stage32-ex2.md` and are opened only when the active task/working set requires them.

Do not preload Stage32 history/controllers, other EX lanes, Research OS, Arsenal, or retained heavy payloads unless `AGENTS.md`, `MAIN-STATE.json`, or the active leaf explicitly triggers them.

## Authority split

`MAIN-STATE.json` is a routing/resume projection, not a proof certificate. It cannot create mathematical credit by assertion.

Exact mathematical claims must be grounded in source locks, retained leaf artifacts, verifiers, and hostile-audit records. Stage32 MAIN is source/routing context only where the active EX2 leaf explicitly needs it; an unaudited Stage32 candidate is not inherited as theorem authority.

The final EX2 target is fixed by `stage32-ex2.md`: decide whether the V6 linear system contains an actual integral irreducible geometric-genus-1 member, by either a verified positive witness or a population-wide negative linear-system proof. A missing-data diagnosis, finite search miss, one fixed-component lemma, or one reducible member may not weaken this terminal contract.

## `stage32ex2-mainbatch` execution contract

A batch:

1. identifies exactly one current mathematical unit;
2. revalidates every load-bearing input through exact source locators;
3. executes a bounded reconstruction/decomposition/verification unit;
4. records object type, field, model, population, assumptions, claim scope, and replay path;
5. updates retained artifacts/verifiers when appropriate, then updates `MAIN-STATE.json` with result, credit ceiling, blocker/reopen condition, and next route;
6. stops at a coherent checkpoint instead of silently broadening the target.

A failed reconstruction technique is `LEAF_BLOCKED`, not EX2 exhaustion. When a lane blocks, record the exact missing object and reopen condition and move to a materially distinct legal lane. Failure to find a member in one finite ansatz is never a linear-system-wide exclusion.

## Parallel / timeout-safe execution

After EX2-00 source locking, the section-coordinate, fixed-moving, symmetry, known-curve, ideal-syzygy, and negative-linear-system lanes may run in parallel on scratch branches.

Scratch results are non-authoritative. Do not push every micro-diagnostic into a shared audit candidate. Consolidate only retained successful leaves; perform freshness synchronization and broad exact-head CI at audit-ready checkpoints.

Heavy/artifact-producing workflows require the repository heavy-workflow policy and explicit authorization. This startup contract does not authorize heavy compute.

## `stage32ex2-audit` handoff

`stage32ex2-audit` is a separate hostile-audit lane governed by `stages/stage32-ex2/AUDIT-CONTRACT.md`. It audits an exact candidate head independently and does not continue or repair the research while auditing.

A hostile-audit FAIL returns the same working lineage to `stage32ex2-mainbatch` for repair. PASS records only the audited EX2 claim ceiling and does not auto-merge or auto-promote Stage32 MAIN.

## Search, write, and merge discipline

Repository discovery is search-first under `AGENTS.md`. Existing weapon/evidence lookup follows the repository asset-discovery policy only when the active leaf needs it. A search miss is not repository-wide absence.

Preserve source/proof locks and firewalls on writes. Do not merge without explicit user authorization.
