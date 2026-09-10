# Stage32EX5 MAINBATCH operations

This file is an operational contract only. It grants no mathematical, FULL178, Stage32 MAIN, N350, receiver, theorem, endpoint, or Perfect Cuboid credit.

## Single active MAINBATCH authority

- The only active Stage32EX5 MAINBATCH working PR is PR #1765 on branch `impl/stage32ex5-bc2-12-outer-rank3`.
- PR #1764 (`stage32ex5-mainbatch-bc2-12`) is superseded and must remain closed/unmerged.
- While PR #1765 remains open, ordinary `stage32ex5-mainbatch` must continue on that PR/branch. Do not create a second Stage32EX5 MAINBATCH PR unless the user explicitly requests a replacement or split.
- Merge remains unauthorized unless the user explicitly authorizes it.

## Workflow lifecycle / anti-refire rule

The repository-level `AGENTS.md` heavy-workflow rerun authorization remains mandatory: a heavy job may run only when its dedicated run key is freshly and semantically advanced in the triggering commit range; otherwise it must fail closed and skip heavy compute.

Stage32EX5 bounded-unit workflows are not permanent PR-wide checks. Once a bounded unit has completed and a later unit becomes the active frontier, its old `.github/workflows/...` pull-request workflow must be retired from the current working head before further ordinary synchronization. Retain solver/checkpoint/run-key/provenance and Git history/run ids for audit; do not keep obsolete bounded-unit PR triggers active merely for provenance.

At this cleanup boundary, BC2-12 through BC2-23 bounded-unit workflow definitions are retired from the current PR head. BC2-24 is the only live Stage32EX5 bounded-unit heavy workflow retained. A non-key synchronize may still create BC2-24's cheap authorize run because the active workflow remains in the PR diff, but the heavy job must skip unless the BC2-24 run key generation advances in the exact commit range.

## Stale-state guard

The branch's compact `MAIN-STATE.json` can lag a just-completed heavy run. Do not execute a state leaf that predates the newest operational boundary recorded by `MAIN-START-HERE.md` and `CURRENT-ROADMAP.md`. At this boundary, BC2-24 workflow `34486703108` has completed successfully but its compact mathematical result has not yet been retained in the repository; therefore the only permitted next leaf is `BC2_24_RESULT_RETENTION_AND_STATE_SYNC`. Do not rerun BC2-20..23 and do not launch BC2-25 before that retention/state sync.

## Audit boundary

Audit this cleanup for: (1) PR #1764 closed and unmerged; (2) PR #1765 sole active MAINBATCH authority; (3) retired BC2-12..23 workflow definitions absent from the current `.github/workflows` head; (4) BC2-24 available with non-key heavy skip; (5) startup stale-state guard active; (6) no mathematical claim or credit promoted by this operational change.
