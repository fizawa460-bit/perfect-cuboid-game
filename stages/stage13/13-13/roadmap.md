# Stage13-13 — final proof hardening and freeze roadmap

> STATUS: `STAGE13_13_ROADMAP_DEFINED`
>
> PURPOSE: turn the reviewed Stage13 R03 theorem candidate plus the post-review `13-12ag` explicitness supplement into one canonical, self-contained, reviewable and finally frozen Stage13 theorem package.
>
> IMPORTANT: Stage13-13 is a proof-hardening/freeze track. It does **not** change the counting convention, theorem statement, directional constants, or Stage12 R09 input unless a genuine defect is discovered.

## Numeric-only dispatch contract

After this roadmap is merged, the user may request work by stage token alone.

```text
13-13a
13-13b
13-13c
13-13d
13-13e
13-13f
13-13g
```

The token is sufficient instruction to execute the corresponding stage against the latest merged `main`, while preserving all completed earlier 13-13 stages.

If a stage discovers a theorem-level defect that invalidates an upstream lock, do **not** silently repair it inside the wrong token. Record the blocker explicitly and stop promotion to the next token until the defect has its own repair stage or revised roadmap entry.

---

## Frozen inputs

Stage13-13 begins from:

```text
Stage12 R09                    frozen upstream theorem input
Stage13-12af R03               immutable reviewed proof snapshot
Stage13-12ag                   post-R03 proof-explicitness supplement
R03 Grok verdict               CLOSED
R03 Qwen verdict               CLOSED
R03 Claude verdict             not recorded
```

Current theorem candidate:

\[
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\},
\]

and

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

Current normalized directional vector:

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)
```

Stage13-13 must distinguish carefully between:

1. repository-proved statements;
2. standard external analytic inputs;
3. finite numerical validation;
4. external reviewer verdicts;
5. bookkeeping/freeze status.

---

## 13-13a — claim and dependency ledger

Status: `[>] Next`.

Purpose: inventory the exact theorem claims and every dependency before rewriting anything.

Required work:

- enumerate every theorem-level claim used by R03 + 13-12ag;
- map each claim to its source file/section;
- classify each dependency as `INTERNAL_PROOF`, `FROZEN_STAGE12_INPUT`, `STANDARD_EXTERNAL_THEOREM`, `FINITE_CHECK`, or `REVIEW_RECORD`;
- verify that no historical superseded Stage13 argument is still silently required;
- identify duplicate derivations and wording drift between R03, roadmap, result files and supplements;
- freeze the exact theorem statement and constants that 13-13c must reproduce unchanged unless a real defect is found.

Expected artifacts:

```text
stages/stage13/13-13a/claim-dependency-ledger.md
stages/stage13/13-13a/result.md
stages/stage13/data/13-13a/claim-dependency-ledger.json
```

Minimum completion lock:

```text
STAGE13_13A=COMPLETE_CLAIM_DEPENDENCY_LEDGER
THEOREM_STATEMENT_FROZEN_FOR_RESYNTHESIS=true
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
NEXT=13-13b
```

---

## 13-13b — external-theorem hypothesis audit

Status: `[ ] Pending 13-13a`.

Purpose: make the theorem boundary explicit enough that a reviewer never has to guess where Stage13 stops and imported analysis begins.

Audit at least:

- the precise finite-order Selberg--Delange/Tauberian input;
- the Gaussian-Hecke / angular harmonic zero-free input used uniformly over the retained polylogarithmic range;
- every use of standard Pythagorean parametrization/counting results inherited from Stage12;
- local character/Jacobi-sum identities and whether they are proved internally or imported;
- any dominated-convergence, Wiener-algebra, coarea/Fubini, or summation interchange whose hypotheses were previously implicit.

For every external theorem record:

```text
THEOREM_USED
SOURCE
HYPOTHESES
WHERE_VERIFIED_IN_STAGE13
WHAT_CONCLUSION_IS_IMPORTED
```

No literature item may be cited as novelty evidence merely because no collision was found.

Expected artifacts:

```text
stages/stage13/13-13b/external-theorem-crosswalk.md
stages/stage13/13-13b/result.md
```

Minimum completion lock:

```text
STAGE13_13B=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT
UNMAPPED_EXTERNAL_INPUTS=0
NEXT=13-13c
```

---

## 13-13c — canonical proof resynthesis

Status: `[ ] Pending 13-13b`.

Purpose: produce the single canonical Stage13 proof that future stages and reviewers should read instead of reconstructing the repair history.

Rules:

- mathematical content must equal the frozen theorem from 13-13a unless a recorded defect forces revision;
- incorporate the useful explicit derivations from 13-12ag directly into the proof rather than leaving them as detached supplements;
- keep R03 immutable as historical reviewed evidence;
- historical R01/R02/R03 repair narrative should move to a short provenance appendix, not interrupt the proof chain;
- all notation must be defined once and used consistently;
- all `o(...)`, uniformity ranges, fixed-set limits, and order-of-limits statements must be visible at the point of use;
- the exact-one overlap subtraction and the common-factor/direction split must be non-circular in the final text.

Expected canonical artifact:

```text
stages/stage13/13-13c/stage13-final-proof.md
```

Minimum completion lock:

```text
STAGE13_13C=COMPLETE_CANONICAL_PROOF_RESYNTHESIS
THEOREM_CHANGED=false
R03_REWRITTEN=false
NEXT=13-13d
```

If `THEOREM_CHANGED=true`, 13-13e may not be entered until the change is explicitly audited and the roadmap status updated.

---

## 13-13d — deterministic reproducibility and consistency audit

Status: `[ ] Pending 13-13c`.

Purpose: ensure every computable constant/interface appearing in the canonical proof is reproducible and internally consistent.

Required checks include, where applicable:

- chamber integrals and normalized direction vector;
- `J_q=2I_q/pi` consistency;
- exact inert-prime character-sum identities;
- local multiplier formulas including `lambda_p`;
- exact finite bridge identities imported from earlier Stage13 stages;
- theorem statement/constants agree across `stage13-final-proof.md`, Stage13 roadmap and machine-readable audit output;
- no stale R01/R02 constants or superseded formulas survive in canonical files.

This stage is a consistency audit, not evidence for the asymptotic theorem by numerical fit.

Expected artifacts:

```text
stages/stage13/scripts/13-13d/final_consistency_audit.py
stages/stage13/data/13-13d/final_consistency_audit.json
stages/stage13/13-13d/result.md
.github/workflows/stage13-13d-final-consistency.yml
```

Minimum completion lock:

```text
STAGE13_13D=COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT
CANONICAL_CONSTANTS_REPRODUCED=true
STALE_SUPERSEDED_FORMULAS_IN_CANONICAL_FILES=0
NEXT=13-13e
```

---

## 13-13e — R04 self-contained review bundle

Status: `[ ] Pending 13-13d`.

Purpose: generate a new immutable final-review snapshot. R03 must remain untouched.

The R04 bundle must contain enough context for an external reviewer to evaluate Stage13 without browsing the repository, including:

- theorem statement;
- counting convention and Stage12 interface;
- full canonical proof;
- explicit external-theorem boundary/crosswalk;
- deterministic consistency summary;
- exact scope of what is and is not claimed.

It must receive a new immutable bundle identifier and content hash.

Expected artifacts:

```text
review/STAGE13-FINAL-SELF-CONTAINED-<date>-R04.html
stages/stage13/13-13e/review-manifest.md
```

Minimum completion lock:

```text
STAGE13_13E=COMPLETE_R04_REVIEW_BUNDLE
R04_IMMUTABLE=true
R03_IMMUTABLE=true
NEXT=13-13f
```

---

## 13-13f — external-review ingestion and repair gate

Status: `[ ] Pending R04 reviewer feedback`.

Purpose: record external reviewer verdicts and repair only actionable defects.

Review policy:

- target independent review from Grok, Qwen and Claude when available;
- final freeze requires at least two independent `CLOSED` verdicts on R04;
- any received unresolved theorem-level objection blocks 13-13g even if two other reviewers say `CLOSED`;
- stylistic suggestions may be recorded without reopening mathematics;
- substantive repair creates a new immutable R05 bundle rather than mutating R04.

Possible outputs:

```text
CLOSED
REPAIRABLE
OPEN
```

If repairs are required, this stage may iterate R05/R06 with explicit immutable versioning, while remaining under token `13-13f` until the review gate closes.

Minimum completion lock:

```text
STAGE13_13F=COMPLETE_EXTERNAL_REVIEW_GATE
INDEPENDENT_CLOSED_VERDICTS>=2
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0
NEXT=13-13g
```

---

## 13-13g — final Stage13 freeze and downstream contract

Status: `[ ] Pending 13-13f`.

Purpose: close Stage13 as a stable theorem dependency for Stage14 and future work.

Required work:

- declare the canonical proof and final reviewed bundle immutable;
- record exact bundle ID, content hash, source commit and reviewer verdicts;
- update Stage13 roadmap/status from candidate/pending bookkeeping to final frozen status;
- write a compact downstream theorem contract containing only the exact facts Stage14 may import;
- retain historical R01/R02/R03 artifacts for provenance without presenting them as current proof;
- explicitly state any unresolved limitations that remain outside the theorem.

Expected artifacts:

```text
stages/stage13/13-13g/final-freeze.md
stages/stage13/13-13g/downstream-contract.md
```

Target completion state:

```text
STAGE13_13G=COMPLETE_FINAL_FREEZE
STAGE13_GLOBAL_STATUS=FROZEN
EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=THEOREM_LEVEL_REPOSITORY_LOCK
FINAL_REVIEW_BUNDLE_IMMUTABLE=true
DOWNSTREAM_STAGE14_CONTRACT_FROZEN=true
NEXT_STAGE13_ACTION=NONE_UNLESS_A_GENUINE_DEFECT_IS_REPORTED
```

---

## Scope boundary

Stage13-13 does not:

- reopen Stage12 R09 merely for cosmetic cleanup;
- alter Stage14 mathematics;
- infer perfect-cuboid existence or nonexistence;
- upgrade finite numerical agreement into an asymptotic proof;
- use external reviewer approval as a substitute for a written proof;
- silently change an immutable reviewed bundle.

The project may later run an analogous final-freeze cleanup for Stage12, but that is a separate track and must not be mixed into Stage13-13.

```text
STAGE13_13_ROADMAP=DEFINED
NUMERIC_ONLY_DISPATCH=true
NEXT=13-13a
```
