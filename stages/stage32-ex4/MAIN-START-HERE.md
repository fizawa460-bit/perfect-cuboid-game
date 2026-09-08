# Stage32EX4 MAIN startup

Ordinary `stage32ex4-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex4/MAIN-START-HERE.md`;
3. `stages/stage32-ex4/MAIN-STATE.json`;
4. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This file is the fixed ordinary startup contract. Mutable frontier, current leaf, blockers, audit status, and next route live only in `MAIN-STATE.json`. The final target and dependency roadmap live in `stages/stage32-ex4/stage32-ex4.md` and are opened when the active working set/task requires them.

Do not preload Stage32 history/controllers, other EX roadmaps, Research OS, Arsenal, or large retained payloads unless `AGENTS.md`, `MAIN-STATE.json`, or the active leaf explicitly triggers them.

## Authority split

`MAIN-STATE.json` is a compact routing/resume projection, not a proof certificate. It cannot create mathematical credit by assertion.

Exact claims require source locks, leaf artifacts/verifiers, and hostile-audit records. Stage32 MAIN may be used as source/routing context only where the active leaf explicitly requires it. An unaudited Stage32 candidate or another EX scratch result is not inherited as theorem authority.

The roadmap completion contract cannot be weakened by a state edit. In particular, a convenient gauge representative, one literal conjugator, a source-gap diagnosis, or a partial `3 -> 1` calculation cannot be promoted to terminal EX4 closure without the adapters required by `stage32-ex4.md`.

## `stage32ex4-mainbatch` execution contract

A batch:

1. reads the startup set and identifies exactly one current mathematical unit;
2. revalidates every load-bearing source/authority status needed by that unit;
3. executes one bounded marking/conjugator/source diagnostic or proof step;
4. records exact object types, assumptions, source locators, admissible coordinate changes, and the residual ambiguity group/orbit;
5. retains only replayable results with an explicit claim ceiling;
6. updates the leaf artifact/verifier when appropriate, then updates `MAIN-STATE.json` with result, blocker/reopen condition, audit readiness, and next route;
7. stops at a coherent checkpoint instead of silently changing populations or models.

A failed source or nonunique conjugator is not EX4 exhaustion. Record `LEAF_BLOCKED` or the exact residual line orbit and move to a materially distinct legal lane. If a source package is claimed exhausted, the ambiguity/exhaustiveness certificate required by EX4-08/10 must exist.

## Timeout-safe execution

Micro-diagnostics should use scratch/isolated branches rather than pushing every experiment into a shared audit candidate. Scratch results are non-authoritative. Consolidate retained successful leaves at a coherent audit checkpoint; perform freshness synchronization and broad exact-head CI there rather than after every experiment.

Heavy/artifact-producing workflows require the repository heavy-workflow policy and an explicit authorization gate. This startup file authorizes no heavy compute.

## Claim-DAG synchronization trigger

Ordinary `stage32ex4-mainbatch` startup remains exactly the four-item startup set above and does not preload Stage32 proof-management files.

When EX4 reaches any `RETAINED_CONSOLIDATION`, `AUTHORITY_OR_AUDIT_TRANSITION`, `EX_TO_MAIN_PROMOTION`, `ACTIVE_FRONTIER_REMAP`, or `FINAL_MILESTONE_TRANSITION`, open `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and complete its on-demand synchronization procedure before treating that checkpoint or downstream credit transition as complete.

Scratch-only diagnostics do not trigger claim-DAG writes. A hostile-audit PASS/FAIL receipt does not silently promote EX4 or MAIN; downstream use waits for claim synchronization.

## `stage32ex4-audit` handoff

`stage32ex4-audit` is a separate hostile-audit lane governed by `stages/stage32-ex4/AUDIT-CONTRACT.md`. It audits the exact candidate as written and does not repair or continue research while auditing.

A FAIL returns the same working lineage to `stage32ex4-mainbatch` for repair. A PASS records only the audited EX4 claim ceiling. It does not automatically merge, alter Stage32 MAIN authority, contract `[73,97,235]`, or exclude Q602/O210.

## Search, write, and merge discipline

Repository discovery is search-first under `AGENTS.md`. Existing evidence/weapon lookup follows the repository asset-discovery policy only when the active leaf needs it. A search miss never proves repository-wide or literature-wide absence.

Preserve source/proof locks and current firewalls before writes. Do not merge without explicit user authorization.
