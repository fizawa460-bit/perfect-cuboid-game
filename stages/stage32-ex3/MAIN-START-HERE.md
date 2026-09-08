# Stage32EX3 MAIN startup

Ordinary `stage32ex3-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex3/MAIN-START-HERE.md`;
3. `stages/stage32-ex3/MAIN-STATE.json`;
4. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This file is the fixed ordinary startup contract. Mutable frontier, current leaf, blockers, audit status, and next route live only in `MAIN-STATE.json`. The final target and dependency roadmap live in `stages/stage32-ex3/stage32-ex3.md` and are opened only when the active task requires them.

Do not preload Stage32 root history/controllers, other Stage32EX roadmaps, Research OS, Arsenal, or large retained payloads unless `AGENTS.md`, `MAIN-STATE.json`, or the active leaf explicitly triggers them.

## Authority split

`MAIN-STATE.json` is the mutable Stage32EX3 routing/resume projection. It is not a proof certificate and cannot create mathematical credit by assertion.

Exact claims must be grounded in source locks, leaf artifacts, verifiers, and hostile-audit records referenced by the state. Stage32 MAIN is read only as source/routing context where the current leaf explicitly requires it. Stage32EX3 does not inherit an unaudited Stage32 candidate or another EX lane as theorem authority.

The completion contract in `stage32-ex3.md` may not be weakened by a state update.

## `stage32ex3-mainbatch` execution contract

A batch:

1. reads the startup set and identifies exactly one current mathematical unit;
2. revalidates every load-bearing input through exact source locators;
3. executes the bounded mathematical/diagnostic unit;
4. retains only results with explicit assumptions, object types, quantification domain, and replay path;
5. updates the leaf artifact/verifier when appropriate, then updates `MAIN-STATE.json` with result, credit ceiling, blocker/reopen condition, audit readiness, and next route;
6. stops at a coherent checkpoint instead of silently broadening the target.

A failed route is not Stage32EX3 exhaustion. A finite monodromy/Nielsen ledger or missing adapter remains an active work queue until EX3-09 terminal decision or a genuine carrier-attached O210 cover configuration is established.

## Timeout-safe / parallel execution

After EX3-00, materially distinct micro-diagnostics may run on separate scratch branches. Scratch results are non-authoritative. Cross-lane use must state whether the dependency is audited, retained exact, or provisional.

Consolidate retained successful leaves at an audit-ready checkpoint. Freshness synchronization and broad exact-head CI belong at that checkpoint rather than after every micro-diagnostic.

Heavy/artifact-producing workflows require the repository heavy-workflow policy and an explicit authorization gate. This file does not authorize heavy compute.

## Claim-DAG synchronization trigger

Ordinary `stage32ex3-mainbatch` startup remains exactly the four-item startup set above and does not preload Stage32 proof-management files.

When EX3 reaches any `RETAINED_CONSOLIDATION`, `AUTHORITY_OR_AUDIT_TRANSITION`, `EX_TO_MAIN_PROMOTION`, `ACTIVE_FRONTIER_REMAP`, or `FINAL_MILESTONE_TRANSITION`, open `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and complete its on-demand synchronization procedure before treating that checkpoint or downstream credit transition as complete.

Scratch-only diagnostics do not trigger claim-DAG writes. A hostile-audit PASS/FAIL receipt does not silently promote EX3 or MAIN; downstream use waits for claim synchronization.

## `stage32ex3-audit` handoff

`stage32ex3-audit` is a separate hostile-audit lane governed by `stages/stage32-ex3/AUDIT-CONTRACT.md`. It audits an exact candidate head independently and does not continue the research while auditing.

A hostile-audit FAIL returns the same working lineage to `stage32ex3-mainbatch` for repair. A PASS records only the audited Stage32EX3 claim ceiling. It does not automatically merge, alter Stage32 MAIN authority, exclude O210/Q602, or grant endpoint credit.

## Search, write, and merge discipline

Repository discovery is search-first under `AGENTS.md`. Existing weapon/evidence lookup follows the repository asset-discovery policy only when the active leaf needs it. A search miss is not repository-wide absence.

Preserve source/proof locks and firewalls before writes. Do not merge without explicit user authorization.
