# Stage32EX6 MAIN startup

Ordinary `stage32ex6-mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex6/MAIN-START-HERE.md`;
3. `stages/stage32-ex6/MAIN-STATE.json`;
4. only the local paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This file is the fixed ordinary startup contract. Mutable routing, the external research lineage, blockers, credit ceiling, and next route live only in `MAIN-STATE.json`.

EX6 is the reverse upper-endpoint attack on the fixed Stage32 V6 population at `O=266`. Its existing research lineage remains PR #1697 until separately consolidated. The management bootstrap introduced here does not copy or promote the unmerged #1697 mathematical artifacts.

If `MAIN-STATE.json.external_research_lineage.local_math_artifacts_imported` is false, the exact external PR/head listed there is source/routing context only. Read only the listed `external_current_leaf_paths` from that exact head when the active EX6 task requires them. Do not silently substitute current main or a newer branch head.

## Authority split

`MAIN-STATE.json` is a routing/resume projection, not a proof certificate. It cannot create mathematical credit by assertion.

The retained #1697 endpoint diagnostics are provisional external research lineage unless and until exact artifacts are consolidated, source-locked into a registered claim, and hostile-audited. `O266_ENDPOINT_NOT_CLOSED` is a blocker/stopping diagnosis, not endpoint exclusion and not Stage32 MAIN advancement.

EX6 never self-promotes. Any future `O266_ENDPOINT_EXCLUDED` result requires an exact retained claim, hostile-audit PASS, and an explicit current-target EX -> MAIN promotion adapter before it can affect MAIN authority.

## `stage32ex6-mainbatch` execution contract

A batch:

1. reads the startup set above and resolves the exact EX6 external lineage/head when needed;
2. revalidates every load-bearing endpoint input through exact source locators;
3. executes one bounded endpoint/re-entry unit;
4. retains only results with explicit population, field/model, assumptions, claim scope, and replay path;
5. updates local EX6 routing state only when the management projection changes, without importing mathematical credit from an external branch by narrative;
6. stops at a coherent checkpoint rather than guessing descent from `O=266` to `O=264` or lower.

A blocked endpoint route is not Stage32 exhaustion. `O266_ENDPOINT_NOT_CLOSED` remains a valid stopping state until genuinely new endpoint input appears.

## Timeout-safe execution

Use scratch/isolated work for micro-diagnostics. Scratch results are non-authoritative. Consolidate retained successful leaves at coherent audit-ready checkpoints; freshness synchronization and broad exact-head CI belong there rather than after every experiment.

Heavy/artifact-producing workflows require the repository heavy-workflow policy and explicit authorization. This startup file does not authorize heavy compute.

## Claim-DAG synchronization trigger

Ordinary scratch work does not preload the Stage32 claim DAG. Open `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and perform the on-demand synchronization procedure only when one of these events occurs:

- `RETAINED_CONSOLIDATION`;
- `AUTHORITY_OR_AUDIT_TRANSITION`;
- `EX_TO_MAIN_PROMOTION`;
- `ACTIVE_FRONTIER_REMAP`;
- `FINAL_MILESTONE_TRANSITION`.

Scratch-only diagnostics do not trigger claim-DAG writes. A hostile-audit FAIL or revocation immediately blocks downstream consumption even before registry synchronization; a PASS cannot upgrade authority before synchronization.

## Search, write, and merge discipline

Repository discovery is search-first under `AGENTS.md`. Existing evidence/weapon lookup follows the repository asset-discovery policy only when the active leaf needs it. A search miss never proves repository-wide absence.

Preserve source/proof locks and current firewalls before writes. Do not merge without explicit user authorization.
