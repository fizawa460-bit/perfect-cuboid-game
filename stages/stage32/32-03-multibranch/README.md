# Stage32 32-03 multibranch — canonical folder (NO CREDIT)

**Only canonical location (moved by PR #1846, merged 2026-11-02):**
`stages/stage32/32-03-multibranch/`

Claude sessions: start with `MB104/CLAUDE-START-HERE.md` (navigation only; not an authority).

- `STATE.json`, `MISSION.json`, `PREFLIGHT.json`, `LIVE.json`, `fib/`: historical/frozen control records; current location references updated, frozen audit/credit statuses unchanged.
- `MB101/`: retained normalization-profile results and original Python verifier.
- `MB102/`: retained branch/delta/genus results and original Python verifier.
- `MB103/`: retained Aut(S) orbit-quotient semantics and original Python verifier.
- `MB104/`: 107 retained verification/numeric files, historical Genus7 sources and runkeys; original Python source blobs preserved (3 Genus7 files restored byte-exact from `d13afbb1a693a5547bebd31ec6fbcc04a7648f05`).
- `MB104/drive-research/`: 170 Google Drive research, audits and supporting evidence files, including SHA256SUMS. Google Drive is frozen as of 2026-11-02; this copy is the final read-only reference and GitHub is the sole authority.

The former `stages/stage32/final-chain/32-03-multibranch/` tree is **removed**, with **no symlink, alias or duplicate corpus**. Previous `stages/stage32/mb101/`, `mb102/` and `mb103/` shallow archive copies are also removed. Older commits on `main` and historical PRs still retain their immutable provenance.

**Deferred repair when execution is actually needed.** Python sources here are the exact pre-migration Git blobs, NOT adapted executable relocations. MB101–MB104 Python source blobs and historical source locks are unchanged. Stage32 current routing pointers and relocated STATE path metadata now point to the canonical directory; Python repository-root depth, some source-locked historical execution assumptions, and GitHub Actions have not been fully runtime-migrated. They may fail if invoked from this new location or if a workflow attempts to run. No workflow wiring/CI remediation or verifier replay is included by user direction (`stage32-main-startup-authority.yml` was disabled in repository settings on 2026-11-02; `stage32-claim-frontier-integrity.yml` remains active). Do not run old workflows as if this migration were a validated runtime relocation. Repair only the needed entrypoints and their locks, then test on an exact head before release.

This is solely a search/storage reorganization. No mathematical evidence is credited or excluded, no frozen audit is released, no receiver/effectivity/theorem/endpoint claim is promoted, and no merge is authorized by this README.
