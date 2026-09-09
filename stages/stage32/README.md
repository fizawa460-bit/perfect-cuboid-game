# Stage32

Ordinary entry point:

1. `MAIN-START-HERE.md`
2. `MAIN-STATE.json`
3. only the current leaf working set named there.

Current mathematical route is the Stage32 final chain:

`32-01 FULL178 -> 32-02 effectivity -> 32-03 multibranch -> 32-04 synthesis -> 32-05 hostile audit`.

## Current layout

- `32-01-178/` — active Mission-DAG orchestration for the 178 open numerical FULL178 targets; user commands are `stage32-01-178-mainbatch` and the currently dispatched short lane commands recorded in its `MISSION.json`.
- `integrated-ex/` — user-facing integrated view of former EX1-EX4 subresearch.
- `residual-32-01-production/` — historical/current FULL178 production machinery consumed by `32-01-178/`; it remains the exact production evidence/code surface rather than being renamed.
- `proof/` — claim registry, active frontier, adapters, FINAL-CHECK support.
- `management/` — current non-mathematical routing/checkpoint records.
- `archive/` — historical root documents and cleanup manifests.
- `scratch/`, `scouts/`, `runkeys/`, `audits/` — bounded operational support.

EX5 remains outside the integrated EX1-EX4 view while its FULL178 route is still active. `32-01-178/MISSION.json` treats EX5 as an external producer and prevents duplicate work; a future audited EX5 result is consumed only through an explicit current-target adapter.

## Why many `32-*` directories remain at root

The old numbered Stage32 directories are historical exact-path evidence. Many retained verifiers and source locks use those paths. They are not ordinary startup authority, but they are deliberately not moved in the current cleanup because cosmetic relocation would create proof-path/versioning churn.

New Stage32 work should not add new loose root files unless they are true startup/authority interfaces. Put new Mission-DAG orchestration under a named subdirectory such as `32-01-178/`, management records under `management/`, proof machinery under `proof/`, and historical material under `archive/`.
