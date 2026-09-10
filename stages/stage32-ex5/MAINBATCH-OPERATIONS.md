# Stage32EX5 MAINBATCH operations

This file is an operational contract only. It grants no mathematical, FULL178, Stage32 MAIN, N350, receiver, theorem, endpoint, or Perfect Cuboid credit.

## Single active MAINBATCH authority

- The only active Stage32EX5 MAINBATCH working PR is PR #1765 on branch `impl/stage32ex5-bc2-12-outer-rank3`.
- PR #1764 (`stage32ex5-mainbatch-bc2-12`) is superseded and must remain closed/unmerged.
- While PR #1765 remains open, ordinary `stage32ex5-mainbatch` must continue on that PR/branch. Do not create a second Stage32EX5 MAINBATCH PR unless the user explicitly requests a replacement or split.
- Merge remains unauthorized unless the user explicitly authorizes it.

## Workflow lifecycle / anti-refire rule

The repository-level `AGENTS.md` heavy-workflow rerun authorization remains mandatory: a heavy job may run only when its dedicated run key is freshly and semantically advanced in the triggering commit range; otherwise it must fail closed and skip heavy compute.

In addition, Stage32EX5 bounded-unit workflows are not permanent PR-wide checks. Once a bounded unit has completed and a later unit becomes the active frontier, its old `.github/workflows/...` pull-request workflow must be retired from the current working head before further ordinary synchronization. Retain the solver/checkpoint/run-key/provenance and Git history/run id needed for audit; do not keep obsolete bounded-unit PR triggers active merely for provenance.

At this operational cleanup boundary, BC2-12 through BC2-23 bounded-unit workflow definitions are retired from the current PR head. BC2-24 is the only live Stage32EX5 bounded-unit heavy workflow retained. This prevents GitHub's PR-wide path matching from materializing old BC2 workflow runs on every later synchronization.

## Audit boundary

Audit this cleanup for: (1) PR #1764 closed and unmerged; (2) PR #1765 remains the sole open Stage32EX5 MAINBATCH authority; (3) retired BC2-12..23 workflow definitions are absent from the current `.github/workflows` head; (4) BC2-24 remains available; (5) no mathematical claim or credit was promoted by this operational change.
