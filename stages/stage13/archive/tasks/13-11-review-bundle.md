# Stage13-11 — self-contained external review bundle

> **STATUS:** `STAGE13_11_COMPLETE_SELF_CONTAINED_REVIEW_BUNDLE`
>
> **MATHEMATICS_CHANGED:** `false`
>
> **CANONICAL_MATHEMATICAL_SOURCE:** `stages/stage13/main.md`

## Purpose

Stage13-11 does not introduce a new mathematical theorem. It packages the completed **Stage13 proof chain only** into one physical HTML file that an external AI or human reviewer can audit from a single URL.

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

The physical bundle contains **Stage13 material only**.

It embeds:

- the Stage13 canonical mathematical source `main.md`;
- Stage13 policy, roadmap, README and initial definition/decomposition documents;
- every active Stage13 audit/reproducibility script predating 13-11;
- every active Stage13 JSON/text audit report predating 13-11;
- this Stage13-11 packaging note;
- the deterministic Stage13-11 bundle builder itself.

It does **not** embed any Stage12 source file, Stage12 manifest, Stage12 archive asset, Stage12 script or Stage12 audit report.

Stage13 does use the already-frozen Stage12 R09 theorem as a prior-stage theorem-level input. For this review, that theorem is treated as a declared external prerequisite. The reviewer should check that Stage13 states and uses the prerequisite correctly, but Stage12 itself is outside the review scope.

```text
REVIEW_SCOPE=STAGE13_ONLY
STAGE12_SOURCE_EMBEDDED=false
STAGE12_REVIEW_IN_SCOPE=false
STAGE12_R09_DECLARED_PRIOR_INPUT=true
```

## Physical self-containment

The generated HTML contains all **Stage13 review payload** inside `<main>` and uses no JavaScript, iframe, external stylesheet, runtime repository fetch or external include.

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

The builder is deterministic with respect to the Stage13 source snapshot and source ledger. Output-only commits are excluded from `SOURCE_SNAPSHOT_COMMIT`, preventing the generated bundle from recursively changing its own source identity.

## Review protocol

The external reviewer is asked to return one top-level verdict:

```text
CLOSED
REPAIRABLE
OPEN
UNREADABLE_SOURCE
```

For `REPAIRABLE` or `OPEN`, findings should be classified as `FATAL`, `MAJOR` or `MINOR` and tied to an embedded Stage13 source path and section/function.

The central checks are the canonical definition, chamber density, direction-neutral arithmetic factors, the use of the declared Stage12 input in the factor-2 projection, lower-order overlap theorem, main vector asymptotic, normalized limit, and scope/non-claims.

The reviewer must not return a negative verdict merely because the Stage12 proof is absent: that exclusion is deliberate and is part of the review boundary.

## R01 defaults

```text
REVIEW_MODE=FULL_ZERO_BASE_STAGE13
REVIEW_SCOPE=STAGE13_ONLY
PHYSICAL_SINGLE_HTML=true
INCLUDE_ALL_ACTIVE_STAGE13_SCRIPTS_AND_REPORTS=true
INCLUDE_STAGE12_SOURCES=false
STAGE12_R09_DECLARED_PRIOR_INPUT=true
VERDICT_PROTOCOL=CLOSED_REPAIRABLE_OPEN_UNREADABLE_SOURCE
```

If an external review later returns a repairable finding, a subsequent `R02` bundle should be generated from the repaired Stage13 source snapshot rather than mutating R01 in place.

## Completion

The physical HTML and JSON manifest are generated and committed by

```text
.github/workflows/stage13-11-self-contained-review.yml
```

using

```text
stages/stage13/scripts/13-11/build_self_contained_review.py
```

The workflow verifies the bundle markers, Stage13-only scope, source count, physical size floor, and no-runtime-dependency status before committing the generated outputs.

```text
STAGE13_11=COMPLETE_SELF_CONTAINED_REVIEW_BUNDLE
STAGE13_11_MATHEMATICAL_THEOREM=false
STAGE13_11_REVIEW_PACKAGING=true
STAGE13_MATHEMATICS_CHANGED=false
STAGE13_ONLY_BUNDLE=true
STAGE12_SOURCE_EMBEDDED=false
STAGE13_INDEPENDENT_REVIEW_COMPLETED=false
NEXT=EXTERNAL_STAGE13_R01_REVIEW
```
