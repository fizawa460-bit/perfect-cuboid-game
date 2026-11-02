# Stage32 32-03 multibranch — canonical folder (DRAFT / NO CREDIT)

**Only canonical location in draft PR #1846:**
`stages/stage32/32-03-multibranch/`

- `STATE.json`, `MISSION.json`, `PREFLIGHT.json`, `LIVE.json`, `fib/`: preserved historical/frozen control records.
- `MB101/`: retained normalization-profile results and original Python verifier.
- `MB102/`: retained branch/delta/genus results and original Python verifier.
- `MB103/`: retained Aut(S) orbit-quotient semantics and original Python verifier.
- `MB104/`: 104 existing verification/numeric files and runkeys; original Python source blobs preserved.
- `MB104/drive-research/`: 170 Google Drive research, audits and supporting evidence files, including SHA256SUMS.

The former `stages/stage32/final-chain/32-03-multibranch/` tree is **removed from this draft branch**, with **no symlink, alias or duplicate corpus**. Previous `stages/stage32/mb101/`, `mb102/` and `mb103/` shallow archive copies are also removed from this branch. Older commits on `main` and historical PRs still retain their immutable provenance.

**Deferred repair when execution is actually needed.** Python sources here are the exact pre-migration Git blobs, NOT adapted executable relocations. Existing Python repository-root depth, absolute file paths, runkeys, source-lock hashes, frozen `STATE.json` path lists, dispatchers and GitHub Actions still point to historical paths. They may fail if invoked from this new location or if a workflow attempts to run. No workflow wiring/CI remediation or verifier replay is included by user direction. Do not run old workflows as if this migration were a validated runtime relocation. Repair only the needed entrypoints and their locks, then test on an exact head before release.

This is solely a search/storage reorganization. No mathematical evidence is credited or excluded, no frozen audit is released, no receiver/effectivity/theorem/endpoint claim is promoted, and no merge is authorized. PR #1846 remains DRAFT; `main` is unchanged.
