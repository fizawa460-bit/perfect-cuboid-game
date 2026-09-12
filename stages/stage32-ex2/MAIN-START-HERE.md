# Stage32EX2 MAIN startup

Ordinary `stage32ex2-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex2/MAIN-START-HERE.md`;
3. `stages/stage32-ex2/MAIN-STATE.json`;
4. `stages/stage32/proof/CROSS-LANE-DEMANDS.json`;
5. only the paths listed in `MAIN-STATE.json.current_leaf_working_set` plus any exact demand artifact/state explicitly selected by the registry.

This file is the fixed ordinary startup contract. Mutable frontier, current leaf, blockers, audit status, and next route live only in `MAIN-STATE.json`. The mathematical target and dependency roadmap live in `stages/stage32-ex2/stage32-ex2.md` and are opened only when the active task/working set requires them.

Do not preload Stage32 history/controllers, other EX lanes, Research OS, Arsenal, or retained heavy payloads unless `AGENTS.md`, `MAIN-STATE.json`, the cross-lane registry, or the active leaf explicitly triggers them.

## Cross-lane demand routing

Shared semantics are in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`. Before substantive local work, inspect every OPEN demand involving EX2. A higher-priority OPEN demand where EX2 is producer preempts lower-priority local research. If EX2 is consumer of an OPEN demand, wait without duplicating producer mathematics; when it becomes SATISFIED, re-enter on the next mainbatch and validate satisfying artifact identity and source-population semantics before resuming. Demand SATISFIED does not grant mathematical credit; hostile audit, claim sync and MAIN promotion remain separate.

## Authority split

`MAIN-STATE.json` is a routing/resume projection, not a proof certificate. It cannot create mathematical credit by assertion.

Exact mathematical claims must be grounded in source locks, retained leaf artifacts, verifiers, and hostile-audit records. Stage32 MAIN is source/routing context only where the active EX2 leaf explicitly needs it; an unaudited Stage32 candidate is not inherited as theorem authority.

The final EX2 target is fixed by `stage32-ex2.md`: decide whether the V6 linear system contains an actual integral irreducible geometric-genus-1 member, by either a verified positive witness or a population-wide negative linear-system proof. A missing-data diagnosis, finite search miss, one fixed-component lemma, or one reducible member may not weaken this terminal contract.

## `stage32ex2-mainbatch` execution contract

A batch:

1. identifies exactly one current mathematical unit after applying any higher-priority cross-lane demand;
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

## Claim-DAG synchronization trigger

Ordinary `stage32ex2-mainbatch` startup now includes the operational cross-lane demand registry but still does not preload the mathematical claim DAG.

When EX2 reaches any `RETAINED_CONSOLIDATION`, `AUTHORITY_OR_AUDIT_TRANSITION`, `EX_TO_MAIN_PROMOTION`, `ACTIVE_FRONTIER_REMAP`, or `FINAL_MILESTONE_TRANSITION`, open `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and complete its on-demand synchronization procedure before treating that checkpoint or downstream credit transition as complete.

Scratch-only diagnostics and demand-status changes alone do not trigger claim-DAG credit writes. A hostile-audit PASS/FAIL receipt does not silently promote EX2 or MAIN; downstream use waits for claim synchronization.

## `stage32ex2-audit` handoff

`stage32ex2-audit` is a separate hostile-audit lane governed by `stages/stage32-ex2/AUDIT-CONTRACT.md`. It audits an exact candidate head independently and does not continue or repair the research while auditing.

A hostile-audit FAIL returns the same working lineage to `stage32ex2-mainbatch` for repair. PASS records only the audited EX2 claim ceiling and does not auto-merge or auto-promote Stage32 MAIN.

## Search, write, and merge discipline

Repository discovery is search-first under `AGENTS.md`. Existing weapon/evidence lookup follows the repository asset-discovery policy only when the active leaf needs it. A search miss is not repository-wide absence.

Preserve source/proof locks and firewalls on writes. Do not merge without explicit user authorization.
