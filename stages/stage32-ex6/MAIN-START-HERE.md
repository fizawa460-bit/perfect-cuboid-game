# Stage32EX6 MAIN startup

Ordinary `stage32ex6-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex6/MAIN-START-HERE.md`;
3. `stages/stage32-ex6/MAIN-STATE.json`;
4. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This is the fixed ordinary startup contract. Mutable routing, current blocker, re-entry conditions, audit provenance, and next route live only in `MAIN-STATE.json`. The mathematical endpoint roadmap remains `stages/stage32-ex6/stage32-ex6.md` and is opened only when the active task requires it.

Do not preload Stage32 root history/controllers, other EX roadmaps, Research OS, Arsenal, or the whole EX6 artifact set unless `AGENTS.md`, `MAIN-STATE.json`, or the active leaf explicitly triggers them.

## Authority split

`MAIN-STATE.json` is a routing/resume projection, not a proof certificate. It cannot create mathematical credit by assertion.

The merged #1697 lineage is retained as bounded EX6 evidence. Its current endpoint decision is `O266_ENDPOINT_NOT_CLOSED`: the O=266 endpoint remains open pending genuinely new input. This is not O266 exclusion, does not descend to O264, and does not move Stage32 MAIN away from its current O210/Q602/V6 frontier.

Exact mathematical use must follow the merged source locks/artifacts/verifiers. The bounded hostile re-audit PASS on #1697 does not enlarge the stated mathematical ceiling.

## `stage32ex6-mainbatch` execution contract

A batch:

1. reads the startup set and identifies one or more bounded O266 endpoint/re-entry units that belong to the same coherent investigation;
2. revalidates every load-bearing input through exact source locators;
3. executes as many bounded mathematical/diagnostic units as are useful for that investigation, continuing across successive micro-results instead of stopping merely because one unit completed;
4. retains only replayable results with explicit population, object type, assumptions, quantification domain, and claim ceiling;
5. updates the leaf artifact/verifier when appropriate, then updates `MAIN-STATE.json` with blocker/re-entry condition, audit readiness, and next route;
6. stops at a coherent mathematical/operational checkpoint, or earlier only for a genuine context, safety, dependency, or authorization boundary, instead of enforcing a one-unit cadence or guessing descent from O=266 to lower O.

A blocked endpoint route is not Stage32 exhaustion. The current state remains stopped until genuinely new endpoint input appears.

## Timeout-safe execution

Use scratch/isolated branches for micro-diagnostics. Scratch results are non-authoritative. Consolidate retained successful leaves at coherent audit-ready checkpoints; freshness synchronization and broad exact-head CI belong there rather than after every experiment.

Heavy/artifact-producing workflows require the repository heavy-workflow policy and explicit authorization. This startup file does not authorize heavy compute.

## Claim-DAG synchronization trigger

Ordinary scratch work does not preload the Stage32 claim DAG. Open `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and perform the on-demand synchronization procedure only when one of these events occurs:

- `RETAINED_CONSOLIDATION`;
- `AUTHORITY_OR_AUDIT_TRANSITION`;
- `EX_TO_MAIN_PROMOTION`;
- `ACTIVE_FRONTIER_REMAP`;
- `FINAL_MILESTONE_TRANSITION`.

Scratch-only diagnostics do not trigger claim-DAG writes. A hostile-audit FAIL or revocation immediately blocks downstream consumption even before registry synchronization; a PASS cannot upgrade authority before synchronization.

EX6 has no automatic promotion path. Any future O266 terminal result must satisfy the claim-DAG authority rules and an explicit current-target EX -> MAIN promotion adapter before affecting MAIN.

## Search, write, and merge discipline

Repository discovery is search-first under `AGENTS.md`. Existing evidence/weapon lookup follows the repository asset-discovery policy only when the active leaf needs it. A search miss never proves repository-wide absence.

Preserve source/proof locks and current firewalls before writes. Do not merge without explicit user authorization.
