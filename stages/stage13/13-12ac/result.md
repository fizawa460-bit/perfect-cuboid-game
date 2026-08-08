# Stage13-12ac — R02 re-synthesis and external re-review package

> **STATUS:** `STAGE13_12AC_COMPLETE_R02_REVIEW_RESYNTHESIS`
>
> **MATHEMATICS_CHANGED:** `false`
>
> **REPAIR_INPUTS:** Stage13-12aa + Stage13-12ab
>
> **EXTERNAL_STATUS:** `PENDING_EXTERNAL_R02`

## Purpose

Stage13-12ac does not add a new mathematical theorem. It consolidates the two
repairs triggered by the R01 `OPEN` review into a new authoritative R02 review
entrypoint and a new physical Stage13-only HTML bundle.

R01 is not overwritten. The R02 artifacts have a distinct identity:

```text
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260808-R02
review/STAGE13-FINAL-SELF-CONTAINED-20260808-R02.html
stages/stage13/data/13-12ac/review_bundle_manifest.json
```

## Current proof precedence

For R02 review, use this order:

```text
1. stages/stage13/13-12ac/current-proof.md
2. stages/stage13/13-12aa/result.md
3. stages/stage13/13-12ab/result.md
4. historical stages/stage13/main.md and the underlying scripts/reports
```

The old 7jb categorywise constant check and old 7jf fixed-modulus transfer are
historical provenance only where superseded by 13-12aa/13-12ab.

## Review-neutrality change from R01

R01 received a structural criticism that its protocol could psychologically
encourage a `CLOSED` verdict. R02 therefore states explicitly:

```text
PREVIOUS_R01_VERDICT_BINDING=false
INTERNAL_PASS_FLAGS_ARE_EVIDENCE=false
INTERNAL_COMPLETE_FLAGS_ARE_EVIDENCE=false
GIT_HASHES_ARE_MATHEMATICAL_EVIDENCE=false
CI_SUCCESS_IS_MATHEMATICAL_EVIDENCE=false
NEGATIVE_VERDICT_REQUIRES_EXTRA_BURDEN=false
```

Hashes and CI are retained only for source identity and deterministic
reproducibility.

## R02 required focus

The external reviewer should re-audit Stage13 from the declared Stage12 R09
input boundary, with special attention to:

- non-circular direction-neutrality in the raw `j=0` channel;
- the mixed-correction weighted-`l1` and harmonic uniformity claims in 13-12aa;
- the fixed-prime local-state/Euler-factor replacement lemma in 13-12ab;
- the inert-prime acceptance and positive-valuation tail;
- the order of limits `fixed k -> B->infinity -> k->infinity`;
- pair/triple lower order and exactly-one transfer.

The allowed top-level verdicts remain

```text
CLOSED
REPAIRABLE
OPEN
UNREADABLE_SOURCE
```

with no preference among them.

## Scope

The physical bundle contains Stage13 sources only. Stage12 R09 remains a
frozen declared prior theorem; its proof is not physically embedded and is not
re-audited in R02.

The bundle must not claim publication-grade peer review, perfect-cuboid
existence/nonexistence, an effective convergence rate, monotonicity, or a
certified enclosure for `kappa`.

## Decision

```text
STAGE13_12AC=COMPLETE_R02_REVIEW_RESYNTHESIS
STAGE13_12AC_MATHEMATICAL_THEOREM=false
R01_MUTATED=false
R02_PHYSICAL_SINGLE_HTML=true
R02_STAGE13_ONLY=true
R02_REVIEW_NEUTRALITY_EXPLICIT=true
STAGE13_REPAIR_CHAIN=COMPLETE
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02
NEXT=EXTERNAL_STAGE13_R02_REVIEW
```
