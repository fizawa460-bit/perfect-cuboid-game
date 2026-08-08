# Stage13-13 — final proof hardening and freeze roadmap

> STATUS: `STAGE13_13F_BLOCKED_R04_REPAIR_REQUIRED`
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

## Frozen theorem contract entering R04

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

Symbolic formulas remain the theorem candidate; Stage13 is not globally frozen until 13-13f and 13-13g close.

---

## 13-13a — claim and dependency ledger

Status: `[x] Complete`.

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

---

## 13-13c — canonical proof resynthesis

Status: `[x] Complete`.

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

```text
STAGE13_13D=COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT
AUDIT_STATUS=PASS
CANONICAL_CONSTANTS_REPRODUCED=true
STALE_SUPERSEDED_FORMULAS_IN_CANONICAL_FILES=0
THEOREM_CHANGED=false
```

The audit is reproducibility/consistency evidence only; finite data do not prove the asymptotic theorem.

---

## 13-13e — R04 self-contained review bundle

Status: `[x] Complete`.

```text
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260809-R04
SOURCE_SNAPSHOT_COMMIT=f652833d194bade57794e4c03c184928a54a31b9
CONTENT_SHA256=789656b5bb2190ae62cf2dcae7a3da06ece4f473780a1229ba7284b10b7f4f1b
BUNDLE_PATH=review/STAGE13-FINAL-SELF-CONTAINED-20260809-R04.html
R04_IMMUTABLE=true
R03_IMMUTABLE=true
THEOREM_CHANGED=false
DETERMINISTIC_AUDIT_STATUS=PASS
```

Any substantive review repair must create R05/R06 rather than mutate R04.

---

## 13-13f — external-review ingestion and repair gate

Status: `[!] BLOCKED — R04 repair required`.

Recorded R04 verdicts:

```text
GROK_R04_VERDICT=CLOSED
CLAUDE_R04_VERDICT=OPEN
DEEPSEEK_R04_VERDICT=REPAIRABLE
QWEN_R04_VERDICT=NOT_RECORDED
INDEPENDENT_CLOSED_VERDICTS=1
UNRESOLVED_SUBSTANTIVE_REVIEW_OBJECTIONS=2
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=2
R04_REPAIR_REQUIRED=true
PROMOTE_TO_13_13G=false
```

Claude's primary objection is the unresolved relationship between the finite directional data, which remain close to `2:1:1`, and the theorem candidate's non-`2:1:1` limiting vector. R04 does not quantitatively show that the observed discrepancy is compatible with its remainder or independently exclude a missing q-dependent leading arithmetic factor. Claude also requests explicit closure of the `529 p^{-5/4}` Wiener bound and the accumulation of curved-region box errors.

DeepSeek independently judges the main strategy plausible but R04 insufficiently self-contained and proof-explicit. It requires repair of the same Wiener and box-error steps plus retained-harmonic uniformity, the complete Stage12 counting/factor-two interface, exact imported Hecke/Vaaler contracts, the fixed-prime transfer, notation/local-factor definitions, and the scope wording of the deterministic audit.

The active repair plan is:

```text
stages/stage13/13-13f/r05-repair-plan.md
```

Its mandatory gates are:

1. finite directional discrepancy + q-independence audit;
2. explicit Wiener bound derivation;
3. explicit curved-region/box error accumulation;
4. explicit retained-harmonic conductor/log bookkeeping;
5. complete Stage12 R09 counting and factor-two interface;
6. precise external Hecke/Dirichlet/Vaaler contracts;
7. expanded fixed inert-prime transfer;
8. notation cleanup and deterministic-audit scope clarification.

If the q-independence audit finds a genuine leading-factor defect, reopen the theorem contract. If the theorem survives unchanged, produce a new immutable R05 bundle containing the repairs and obtain fresh external reviews on R05. R04 verdicts do not automatically count toward the R05 freeze.

13-13f can close only when the final reviewed bundle satisfies:

```text
INDEPENDENT_CLOSED_VERDICTS>=2
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0
```

Until then:

```text
STAGE13_13F=BLOCKED_R04_REPAIR_REQUIRED
R04_IMMUTABLE=true
R05_REQUIRED_IF_THEOREM_SURVIVES_AUDIT=true
R05_FRESH_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13f
```

---

## 13-13g — final Stage13 freeze and downstream contract

Status: `[ ] BLOCKED by 13-13f`.

Target lock after the review gate actually closes:

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
STAGE13_13_ROADMAP=ACTIVE_BLOCKED_REVIEW_GATE
NUMERIC_ONLY_DISPATCH=true
STAGE13_13A=COMPLETE_CLAIM_DEPENDENCY_LEDGER
STAGE13_13B=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT
STAGE13_13C=COMPLETE_CANONICAL_PROOF_RESYNTHESIS
STAGE13_13D=COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT
STAGE13_13E=COMPLETE_R04_REVIEW_BUNDLE
STAGE13_13F=BLOCKED_R04_REPAIR_REQUIRED
GROK_R04_VERDICT=CLOSED
CLAUDE_R04_VERDICT=OPEN
DEEPSEEK_R04_VERDICT=REPAIRABLE
QWEN_R04_VERDICT=NOT_RECORDED
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=2
R04_REPAIR_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13f
```
