# Stage13-13 — final proof hardening and freeze roadmap

> STATUS: `STAGE13_13D_COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT_13_13E_NEXT`
>
> PURPOSE: turn the reviewed Stage13 theorem candidate into one canonical, reproducible, externally reviewed and finally frozen theorem package.
>
> IMPORTANT: this track does not change the counting convention, theorem statement, directional constants, or frozen Stage12 R09 input unless a genuine defect is explicitly recorded.

## Numeric-only dispatch contract

The user may dispatch by token alone:

```text
13-13a
13-13b
13-13c
13-13d
13-13e
13-13f
13-13g
```

A theorem-level defect blocks promotion; it must not be silently repaired inside an unrelated token.

---

## Frozen theorem contract

```text
Stage12 input: C_prim(B) ~ kappa/(12*pi) B(log B)^3
N_q(B)       ~ kappa*I_q/(3*pi^3) B(log B)^3
N1(B)        ~ kappa/(24*pi) B(log B)^3
sum I_q       = pi^2/8
J_q           = 2 I_q/pi
P_q           = 8 I_q/pi^2
O_qr(B)       = o(B(log B)^3)
T(B)          = o(B(log B)^3)
lambda_p      = (p+5)/(2(p+1)) for inert p
```

Normalized directional validator `(ab,ac,bc)`:

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)
```

Symbolic formulas are authoritative; decimals are deterministic validators only.

Frozen provenance inputs:

```text
Stage12 R09                    frozen upstream theorem input
Stage13-12af R03               immutable reviewed proof snapshot
Stage13-12ag                   post-R03 proof-explicitness supplement
R03 Grok verdict               CLOSED
R03 Qwen verdict               CLOSED
R03 Claude verdict             not recorded
```

---

## 13-13a — claim and dependency ledger

Status: `[x] Complete`.

Artifacts:

```text
stages/stage13/13-13a/claim-dependency-ledger.md
stages/stage13/13-13a/result.md
stages/stage13/data/13-13a/claim-dependency-ledger.json
```

Lock:

```text
STAGE13_13A=COMPLETE_CLAIM_DEPENDENCY_LEDGER
CLAIM_COUNT=30
THEOREM_STATEMENT_FROZEN_FOR_RESYNTHESIS=true
THEOREM_LEVEL_DEFECT_FOUND=false
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
```

---

## 13-13b — external-theorem hypothesis audit

Status: `[x] Complete`.

Artifacts:

```text
stages/stage13/13-13b/external-theorem-crosswalk.md
stages/stage13/13-13b/result.md
```

Lock:

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

Minimal external boundary:

```text
Stage12 R09 primitive-oriented total theorem
standard Dirichlet/Hecke analytic continuation + functional equation + polynomial strip/conductor growth
Vaaler periodic interval majorant/minorant
```

---

## 13-13c — canonical proof resynthesis

Status: `[x] Complete`.

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

Lock:

```text
STAGE13_13C=COMPLETE_CANONICAL_PROOF_RESYNTHESIS
THEOREM_CHANGED=false
R03_REWRITTEN=false
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
MINIMAL_EXTERNAL_BOUNDARY_PRESERVED=true
```

---

## 13-13d — deterministic reproducibility and consistency audit

Status: `[x] Complete`.

Artifacts:

```text
stages/stage13/scripts/13-13d/final_consistency_audit.py
stages/stage13/data/13-13d/final_consistency_audit.json
stages/stage13/13-13d/result.md
.github/workflows/stage13-13d-final-consistency.yml
```

The deterministic audit reproduces the chamber integrals and normalized direction vector, verifies `J_q=2I_q/pi`, checks the exact B=100000 Stage12 factor-two/inclusion-exclusion fixture, directly enumerates inert unit states at p=7,11,19,23, verifies the exact local multiplier, requires all canonical theorem-lock tokens, and scans the mathematical core for superseded `7jb/7jf` routes or stale soft local formulas.

Lock:

```text
STAGE13_13D=COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT
AUDIT_STATUS=PASS
CANONICAL_CONSTANTS_REPRODUCED=true
CHAMBER_SUM_REPRODUCED=true
DIRECTION_VECTOR_REPRODUCED=true
JQ_BRIDGE_REPRODUCED=true
FINITE_FACTOR_TWO_BRIDGE_REPRODUCED=true
INERT_UNIT_ACCEPTANCE_REPRODUCED=true
INERT_LOCAL_MULTIPLIER_REPRODUCED=true
STALE_SUPERSEDED_FORMULAS_IN_CANONICAL_FILES=0
THEOREM_CHANGED=false
NEXT=13-13e
```

This stage is reproducibility/consistency evidence only, not numerical evidence for the asymptotic theorem.

---

## 13-13e — R04 self-contained review bundle

Status: `[>] Next`.

Purpose: generate a new immutable final-review snapshot without mutating R03.

The R04 bundle must be reviewable without repository browsing and must include:

- theorem statement and counting convention;
- frozen Stage12 interface;
- full canonical proof;
- external-theorem crosswalk/minimal boundary;
- deterministic 13-13d consistency summary;
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

Policy:

- target independent Grok, Qwen and Claude review when available;
- final freeze requires at least two independent `CLOSED` verdicts on the final bundle;
- any received unresolved theorem-level objection blocks 13-13g;
- substantive repair creates a new immutable R05/R06 bundle rather than mutating an old bundle.

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

Expected artifacts:

```text
stages/stage13/13-13g/final-freeze.md
stages/stage13/13-13g/downstream-contract.md
```

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

A later Stage12 cleanup/final-proof resynthesis is a separate track.

```text
STAGE13_13_ROADMAP=ACTIVE
NUMERIC_ONLY_DISPATCH=true
STAGE13_13A=COMPLETE_CLAIM_DEPENDENCY_LEDGER
STAGE13_13B=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT
STAGE13_13C=COMPLETE_CANONICAL_PROOF_RESYNTHESIS
STAGE13_13D=COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT
CANONICAL_CONSTANTS_REPRODUCED=true
STALE_SUPERSEDED_FORMULAS_IN_CANONICAL_FILES=0
NEXT=13-13e
```
