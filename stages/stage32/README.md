# Stage32

Ordinary entry point:

1. `MAIN-START-HERE.md`
2. `MAIN-STATE.json`
3. only the current leaf working set named there.

Current mathematical route is the Stage32 final chain:

`32-01 FULL178 -> 32-02 effectivity -> 32-03 multibranch -> 32-04 synthesis -> 32-05 hostile audit`.

## Current layout

- `integrated-ex/` — user-facing integrated view of former EX1-EX4 subresearch.
- `residual-32-01-production/` — historical/current FULL178 production machinery.
- `proof/` — claim registry, active frontier, adapters, FINAL-CHECK support.
- `management/` — current non-mathematical routing/checkpoint records.
- `archive/` — historical root documents and cleanup manifests.
- `scratch/`, `scouts/`, `runkeys/`, `audits/` — bounded operational support.

EX5 remains outside this integrated view while its FULL178 route is still active.

## Why many `32-*` directories remain at root

The old numbered Stage32 directories are historical exact-path evidence. Many retained verifiers and source locks use those paths. They are not ordinary startup authority, but they are deliberately not moved in the current cleanup because cosmetic relocation would create proof-path/versioning churn.

New Stage32 work should not add new loose root files unless they are true startup/authority interfaces. Put new management records under `management/`, proof machinery under `proof/`, and historical material under `archive/`.
