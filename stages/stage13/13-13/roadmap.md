# Stage13-13 — final proof hardening and freeze roadmap

> STATUS: `STAGE13_13C_COMPLETE_CANONICAL_PROOF_RESYNTHESIS_13_13D_NEXT`
>
> PURPOSE: turn the reviewed Stage13 R03 theorem candidate plus the post-review explicitness work into one canonical, self-contained, reproducible, externally reviewed and finally frozen Stage13 theorem package.
>
> IMPORTANT: Stage13-13 is a proof-hardening/freeze track. It does **not** change the counting convention, theorem statement, directional constants, or Stage12 R09 input unless a genuine defect is discovered.

## Numeric-only dispatch contract

The following tokens are sufficient instructions against the latest merged `main`:

```text
13-13a
13-13b
13-13c
13-13d
13-13e
13-13f
13-13g
```

If a stage discovers a theorem-level defect that invalidates an upstream lock, do not silently repair it inside the wrong token. Record the blocker explicitly and stop promotion until the defect is separately resolved.

---

## Frozen inputs

```text
Stage12 R09                    frozen upstream theorem input
Stage13-12af R03               immutable reviewed proof snapshot
Stage13-12ag                   post-R03 proof-explicitness supplement
R03 Grok verdict               CLOSED
R03 Qwen verdict               CLOSED
R03 Claude verdict             not recorded
```

Frozen theorem contract:

\[
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\},
\]

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3,
\]

\[
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8},
\qquad
J_q=\frac{2I_q}{\pi},
\]

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad
T(B)=o(B(\log B)^3),
\]

\[
\lambda_p=\frac{p+5}{2(p+1)}
\qquad(p\equiv3\pmod4).
\]

Normalized directional validator:

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)
```

The symbolic formulas are authoritative; decimals are deterministic validators only.

---

## 13-13a — claim and dependency ledger

Status: `[x] Complete`.

Artifacts:

```text
stages/stage13/13-13a/claim-dependency-ledger.md
stages/stage13/13-13a/result.md
stages/stage13/data/13-13a/claim-dependency-ledger.json
```

Locks:

```text
STAGE13_13A=COMPLETE_CLAIM_DEPENDENCY_LEDGER
CLAIM_COUNT=30
THEOREM_STATEMENT_FROZEN_FOR_RESYNTHESIS=true
THEOREM_LEVEL_DEFECT_FOUND=false
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
```

The active theorem chain was separated from provenance, finite checks and review records. Old Stage13-7jb/7jf proof routes are not required.

---

## 13-13b — external-theorem hypothesis audit

Status: `[x] Complete`.

Artifacts:

```text
stages/stage13/13-13b/external-theorem-crosswalk.md
stages/stage13/13-13b/result.md
```

Locks:

```text
STAGE13_13B=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT
UNMAPPED_EXTERNAL_INPUTS=0
FAILED_EXTERNAL_HYPOTHESES=0
MINIMAL_EXTERNAL_BOUNDARY_LOCKED=true
GENERAL_SELBURG_DELANGE_BLACK_BOX_REQUIRED=false
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED_FOR_FINAL_PROOF=false
GROWING_MODULUS_INPUT_USED=false
THEOREM_CHANGED=false
```

Minimal external boundary for the canonical proof:

```text
Stage12 R09 primitive-oriented total theorem
standard Dirichlet/Hecke analytic continuation + functional equation + polynomial strip/conductor growth
Vaaler periodic interval majorant/minorant
```

The special integer-pole-order Perron/residue argument is internalized in 13-13c.

---

## 13-13c — canonical proof resynthesis

Status: `[x] Complete`.

Purpose: replace the repair-history reading order by one canonical proof while preserving the 13-13a theorem contract exactly.

Canonical artifacts:

```text
stages/stage13/13-13c/stage13-final-proof.md
stages/stage13/13-13c/result.md
```

Canonical proof order:

```text
definitions + exact inclusion-exclusion
-> exact Stage12 factor-two projection bridge
-> chamber/Gelfand--Leray geometry
-> exact J_q = 2 I_q / pi bridge
-> primitive j=0 local coefficient system
-> weighted-Wiener correction
-> special Perron/residue pole-order lemma
-> curved zero-mode main + Vaaler/nonzero-harmonic error
-> q-independent raw constant Theta
-> Stage12 total calibration
-> exact inert-prime states + character sum
-> lambda_p exact formula
-> fixed-S overlap squeeze
-> exactly-one theorem
```

The required non-circular order is explicit: commonness of `Theta` is proved before Stage12 total mass is used to determine it.

Completion lock:

```text
STAGE13_13C=COMPLETE_CANONICAL_PROOF_RESYNTHESIS
THEOREM_CHANGED=false
R03_REWRITTEN=false
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
MINIMAL_EXTERNAL_BOUNDARY_PRESERVED=true
NEXT=13-13d
```

---

## 13-13d — deterministic reproducibility and consistency audit

Status: `[>] Next`.

Purpose: independently verify every computable constant/interface appearing in the canonical proof and detect stale or superseded formulas before review packaging.

Required checks include:

- chamber integrals and normalized direction vector;
- `J_q=2I_q/pi` and `sum I_q=pi^2/8`;
- exact inert-prime character-sum identities;
- `alpha_p` and `lambda_p=(p+5)/(2(p+1))`;
- exact Stage12 factor-two bridge checks available from earlier finite audits;
- theorem statement/constants agree between `stage13-final-proof.md`, the roadmap and machine-readable audit output;
- the canonical proof contains no stale R01/R02 constants or superseded `7jb/7jf` proof dependencies;
- the raw analytic error ledger is arithmetically consistent with the frozen parameter choices.

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

This stage is a consistency/reproducibility audit, not numerical evidence for the asymptotic theorem.

---

## 13-13e — R04 self-contained review bundle

Status: `[ ] Pending 13-13d`.

Purpose: generate a new immutable final-review snapshot. R03 remains untouched.

The R04 bundle must contain enough context for a reviewer to evaluate Stage13 without repository browsing:

- theorem statement and counting convention;
- frozen Stage12 interface;
- full canonical proof;
- external-theorem crosswalk/minimal boundary;
- deterministic consistency summary;
- exact scope and limitations.

Expected artifacts:

```text
review/STAGE13-FINAL-SELF-CONTAINED-<date>-R04.html
stages/stage13/13-13e/review-manifest.md
```

Minimum lock:

```text
STAGE13_13E=COMPLETE_R04_REVIEW_BUNDLE
R04_IMMUTABLE=true
R03_IMMUTABLE=true
NEXT=13-13f
```

---

## 13-13f — external-review ingestion and repair gate

Status: `[ ] Pending R04 reviewer feedback`.

Review policy:

- target independent review from Grok, Qwen and Claude when available;
- final freeze requires at least two independent `CLOSED` verdicts on the final bundle;
- any received unresolved theorem-level objection blocks 13-13g;
- stylistic suggestions may be recorded without reopening mathematics;
- any substantive repair creates a new immutable R05/R06 bundle rather than mutating an old bundle.

Possible states:

```text
CLOSED
REPAIRABLE
OPEN
```

Minimum lock:

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

Required outputs:

```text
stages/stage13/13-13g/final-freeze.md
stages/stage13/13-13g/downstream-contract.md
```

Required work:

- freeze the canonical proof and final reviewed bundle;
- record bundle ID, content hash, source commit and reviewer verdicts;
- update global Stage13 status from candidate/bookkeeping to frozen;
- write the exact compact theorem contract that downstream work may import;
- retain R01/R02/R03 provenance without presenting superseded artifacts as current proof;
- record limitations outside the theorem.

Target lock:

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

- reopen Stage12 R09 for cosmetic cleanup;
- alter Stage14 mathematics;
- infer perfect-cuboid existence or nonexistence;
- upgrade finite numerical agreement into an asymptotic proof;
- use reviewer approval as a substitute for a written proof;
- silently mutate an immutable review bundle.

A later Stage12 cleanup/final-proof resynthesis, if desired, is a separate track.

```text
STAGE13_13_ROADMAP=ACTIVE
NUMERIC_ONLY_DISPATCH=true
STAGE13_13A=COMPLETE_CLAIM_DEPENDENCY_LEDGER
STAGE13_13B=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT
STAGE13_13C=COMPLETE_CANONICAL_PROOF_RESYNTHESIS
NEXT=13-13d
```
