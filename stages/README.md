# Stage-oriented research layout

This repository uses a **stage-first** layout for stage-specific research assets.

## Active entry point

Read first:

```text
docs/00_CURRENT_RESEARCH_STATUS.md
```

## Stage directories

```text
stages/stage12/   frozen Stage12 result and provenance
stages/stage13/   active Stage13 work
```

Stage-specific mathematics, scripts, data, and archives belong under the corresponding stage directory. Repository-wide utilities and status documents may remain at top level.

## Naming rule

The stage/task context belongs in the **path**, not at the end of every filename.

Preferred:

```text
stages/stage12/archive/scripts/2k/audit_final_remainder.py
stages/stage12/archive/data/2k/final_remainder_report.json
```

Avoid for new files:

```text
scripts/audit_final_remainder_stage12_n1_2k.py
data/final_remainder_stage12_n1_2k_report.json
```

This makes GitHub directory listings readable while preserving exactly which stage/task used each asset.

## Review artifacts

A generated review page that is intentionally distributed by a direct URL may remain under top-level `review/`. Historical review pages belong inside the relevant stage archive.
