# Stage13-13 — final proof hardening and freeze roadmap

> STATUS: `STAGE13_13F_R05_REPAIR_GATES_A_B_COMPLETE_GATE_C_NEXT`
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
13-13fa
13-13fb
13-13fc
13-13fd
13-13fe
13-13ff
13-13fg
13-13fh
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
GENERAL_SELBERG_DELANGE_BLACK_BOX_REQUIRED=false
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

## 13-13f — external-review ingestion and R05 repair gate

Status: `[!] BLOCKED — R05 repairs in progress`.

Recorded R04 verdicts remain historical review facts:

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

The active repair plan is:

```text
stages/stage13/13-13f/r05-repair-plan.md
```

### 13-13fa — Gate A: finite discrepancy + q-independence

Status: `[x] Complete`.

The audit combines retained exact-one checkpoints from `B=1000` through `B=5000000` and retraces the non-circular common-`Theta` proof.

Endpoint diagnostic:

```text
B=100000:
  L1 distance to 2:1:1       = 0.015515086591680
  L1 distance to claimed P   = 0.067914621089948

B=5000000:
  L1 distance to 2:1:1       = 0.023705817456749
  L1 distance to claimed P   = 0.061874500485977
```

Thus the finite endpoint trajectory moves away from exact `2:1:1` and modestly toward the claimed vector; finite data are not a logical contradiction to the asymptotic theorem. No monotonicity claim is made.

The leading arithmetic chain was retraced through the primitive `j=0` local coefficient, mixed correction, OE/EE/parity factors, curved zero mode, nonzero-harmonic lower-order step, and only then Stage12 total calibration. No q-dependent leading arithmetic factor was found at the current proof level.

Crucially, the theorem still supplies only a little-`o` remainder and **no effective convergence rate** capable of numerically predicting the discrepancy at `B<=5m`. R05 must state that limitation explicitly.

```text
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
FINITE_DATA_CONTRADICTS_THEOREM=false
LEADING_Q_DEPENDENT_ARITHMETIC_FACTOR_FOUND=false
COMMON_THETA_AUDIT=PASS_AT_CURRENT_PROOF_LEVEL
PROVED_EFFECTIVE_CONVERGENCE_RATE=false
FINITE_DISCREPANCY_QUANTITATIVELY_EXPLAINED_BY_PROVED_REMAINDER=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
```

This internal repair audit does not rewrite the historical Claude/DeepSeek R04 verdicts. Fresh review will be required on R05.

### 13-13fb — Gate B: explicit Wiener bound

Status: `[x] Complete`.

The split-prime mixed correction is now expanded coefficient by coefficient. For `rho=p^-5/8` and `p>=13`,

```text
||a||       <= (8/3) rho
||b||       <= (44/9) rho
||M||       <= (32/9) rho^2
||A^-1||    <= 5/3
||B^-1||    <= 25/12
```

and pure-axis cancellation gives

```text
||E|| <= (17744/243) rho^2.
```

Therefore

```text
(17744/243)*(5/3)*(25/12)^2
 = 3465625/6561
 = 528.2159731748209...
 < 529,
```

so

```text
||C_{ell,p}-1||_{5/8} <= 529 p^(-5/4), p>=13.
```

The formerly implicit exceptional split prime is now explicit as well:

```text
||C_{ell,5}-1||_{5/8}
 <= 10799919009/25000000
 = 431.99676036
 < 432.
```

The bounds are uniform in the local angular phase and therefore throughout the retained harmonic range. The exact constants are regenerated by dedicated CI.

```text
STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND
WIENER_E_BOUND=17744/243
WIENER_EXACT_CONSTANT=3465625/6561
WIENER_ROUNDED_CONSTANT=529
WIENER_EXPONENT=5/4
P5_EXPLICIT_FINITE_BOUND_LT=432
PHASE_UNIFORM=true
RETAINED_HARMONIC_UNIFORM=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
```

### Remaining R05 gates

```text
13-13fc  [>] curved-region / box error accumulation
13-13fd  [ ] retained-harmonic conductor/log bookkeeping
13-13fe  [ ] complete Stage12 R09 counting and factor-two interface
13-13ff  [ ] precise external Hecke/Dirichlet/Vaaler contracts
13-13fg  [ ] expanded fixed inert-prime transfer
13-13fh  [ ] notation cleanup + deterministic-audit scope + R05 synthesis readiness
```

If a later repair uncovers a genuine theorem-level defect, reopen the theorem contract. Otherwise, after all gates, produce a new immutable R05 bundle and obtain fresh independent reviews on R05. R04 verdicts do not automatically count toward the R05 freeze.

13-13f can close only when the final reviewed bundle satisfies:

```text
INDEPENDENT_CLOSED_VERDICTS>=2
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0
```

Until then:

```text
STAGE13_13F=BLOCKED_R05_REPAIR_IN_PROGRESS
R04_IMMUTABLE=true
R05_REQUIRED=true
R05_FRESH_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fc
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
STAGE13_13_ROADMAP=ACTIVE_BLOCKED_R05_REPAIR
NUMERIC_ONLY_DISPATCH=true
STAGE13_13A=COMPLETE_CLAIM_DEPENDENCY_LEDGER
STAGE13_13B=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT
STAGE13_13C=COMPLETE_CANONICAL_PROOF_RESYNTHESIS
STAGE13_13D=COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT
STAGE13_13E=COMPLETE_R04_REVIEW_BUNDLE
STAGE13_13F=BLOCKED_R05_REPAIR_IN_PROGRESS
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fc
```