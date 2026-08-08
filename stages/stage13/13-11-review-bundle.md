# Stage13-11 — self-contained external review bundle

> **STATUS:** `STAGE13_11_COMPLETE_SELF_CONTAINED_REVIEW_BUNDLE`
>
> **MATHEMATICS_CHANGED:** `false`
>
> **CANONICAL_MATHEMATICAL_SOURCE:** `stages/stage13/main.md`

## Purpose

Stage13-11 does not introduce a new mathematical theorem. It packages the completed Stage13 proof chain into one physical HTML file that an external AI or human reviewer can audit from a single URL.

The review bundle is

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260808-R01.html
```

with bundle identity

```text
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260808-R01
```

Its machine-readable integrity ledger is

```text
stages/stage13/data/13-11/review_bundle_manifest.json
```

## Review boundary

The bundle is self-contained at the **frozen Stage12 R09 input boundary**.

It physically embeds:

- the frozen Stage12 canonical final theorem and R09 manifest;
- the Stage13 canonical mathematical source `main.md`;
- Stage13 policy, roadmap, README and initial definition/decomposition documents;
- every active Stage13 audit/reproducibility script predating 13-11;
- every active Stage13 JSON/text audit report predating 13-11;
- this Stage13-11 packaging note;
- the deterministic Stage13-11 bundle builder itself.

It deliberately does not embed the entire Stage12 historical archive. Stage12 R09 is treated as the already-frozen prior-stage theorem-level input. The reviewer must verify that Stage13 states and uses that input correctly, but is not asked to re-prove all of Stage12 inside the Stage13 review.

## Physical self-containment

The generated HTML contains all review payload inside `<main>` and uses no JavaScript, iframe, external stylesheet, runtime repository fetch or external include.

The page records:

```text
SOURCE_SNAPSHOT_COMMIT
SOURCE_LEDGER_SHA256
CONTENT_SHA256
CHECKPOINT=START_OF_MAIN
CHECKPOINT=BEFORE_EMBEDDED_SOURCES
CHECKPOINT=AFTER_EMBEDDED_SOURCES
CHECKPOINT=END_OF_MAIN
END_OF_BUNDLE
```

The builder is deterministic with respect to the source snapshot and source ledger. Output-only commits are excluded from `SOURCE_SNAPSHOT_COMMIT`, preventing the generated bundle from recursively changing its own source identity.

## Review protocol

The external reviewer is asked to return one top-level verdict:

```text
CLOSED
REPAIRABLE
OPEN
UNREADABLE_SOURCE
```

For `REPAIRABLE` or `OPEN`, findings should be classified as `FATAL`, `MAJOR` or `MINOR` and tied to an embedded source path and section/function.

The central checks are the canonical definition, chamber density, direction-neutral arithmetic factors, Stage12-to-Stage13 factor-2 projection, lower-order overlap theorem, main vector asymptotic, normalized limit, and scope/non-claims.

## R01 defaults

No additional user decision was required for R01. Stage13-11 fixes:

```text
REVIEW_MODE=FULL_ZERO_BASE_STAGE13
STAGE12_BOUNDARY=FROZEN_R09_INPUT
PHYSICAL_SINGLE_HTML=true
INCLUDE_ALL_ACTIVE_STAGE13_SCRIPTS_AND_REPORTS=true
INCLUDE_STAGE12_FULL_ARCHIVE=false
VERDICT_PROTOCOL=CLOSED_REPAIRABLE_OPEN_UNREADABLE_SOURCE
```

If an external review later returns a repairable finding, a subsequent `R02` bundle should be generated from the repaired source snapshot rather than mutating R01 in place.

## Completion

The physical HTML and JSON manifest are generated and committed by

```text
.github/workflows/stage13-11-self-contained-review.yml
```

using

```text
stages/stage13/scripts/13-11/build_self_contained_review.py
```

The workflow verifies the bundle markers, source count, physical size floor, and no-runtime-dependency status before committing the generated outputs.

```text
STAGE13_11=COMPLETE_SELF_CONTAINED_REVIEW_BUNDLE
STAGE13_11_MATHEMATICAL_THEOREM=false
STAGE13_11_REVIEW_PACKAGING=true
STAGE13_MATHEMATICS_CHANGED=false
STAGE13_INDEPENDENT_REVIEW_COMPLETED=false
NEXT=EXTERNAL_STAGE13_R01_REVIEW
```
