# Stage-oriented research layout

This repository uses a **stage-first** layout for stage-specific research assets.

## Active entry point

Read first:

```text
docs/00_CURRENT_RESEARCH_STATUS.md
```

## Stage directories

Stage directory numbers are zero-padded to two digits so GitHub's lexical ordering matches the research order.

```text
stages/stage02/   two-face geometry / Kummer classification
stages/stage03/   Mordell--Weil analysis
stages/stage04/   all observed-fiber rank analysis
stages/stage05/   rank / canonical-height audit
stages/stage06/   height theory
stages/stage07/   inverse-height analysis
stages/stage08/   local sieve
stages/stage09/   divisor-chain analysis
stages/stage10/   explicit one-face family / lower bound
stages/stage11/   shared-face-diagonal convolution
stages/stage12/   frozen Stage12 R09 result and provenance
stages/stage13/   frozen Stage13 R07 result and provenance
stages/stage14/   frozen Stage14 R05 result, arsenal, and provenance
stages/stage15/   active Stage15 comparison work
```

Stage-specific mathematics, scripts, derived reports, and frozen workflows belong under the corresponding stage directory. Repository-wide/shared source data and status documents may remain at top level.

## Naming rule

The stage/task context belongs in the **path**, not at the end of every filename. Stage directories always use two decimal digits (`stage02`, ..., `stage09`, `stage10`, ...).

Preferred:

```text
stages/stage10/scripts/audit_one_face_lower_bound.py
stages/stage10/data/lower_bound_report.json
stages/stage12/archive/scripts/2k/audit_final_remainder.py
```

Avoid for new files:

```text
scripts/audit_one_face_lower_bound_stage10.py
data/final_remainder_stage12_n1_2k_report.json
```

This makes GitHub directory listings readable while preserving exactly which stage used each asset.

## Completed-stage workflows

Workflows that existed only to reproduce a completed research stage are stored inside that stage's `workflows/` directory rather than `.github/workflows/`. They are provenance and do not run automatically. If a completed stage is deliberately reopened, restore only the required workflow to `.github/workflows/` and update paths intentionally.

## Shared assets

`docs/face-ratio-geometry-research.md` remains a cross-stage research memo. Canonical/raw datasets used by multiple stages may remain under top-level `data/`; stage-specific derived JSON reports belong inside the stage that produced them.

## Completed Stage13/14 rule

Completed Stage13 and Stage14 mathematics use one final file each:

```text
stages/stage13/final.md
stages/stage14/final.md
```

Historical task directories and completed workflows are archive-only. Stage14's
arsenal indexes under `docs/` remain protected interfaces for Stage15.

## Review artifacts

A generated review page intentionally distributed by a direct URL may remain under top-level `review/`. Historical review pages belong inside the relevant stage archive.
