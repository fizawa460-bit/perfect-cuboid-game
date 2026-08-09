# Stage13-13 — final proof hardening and freeze roadmap

> STATUS: `STAGE13_13F_R05_REPAIR_GATES_A_B_C_D_COMPLETE_GATE_E_NEXT`
>
> PURPOSE: turn the reviewed Stage13 theorem candidate into one canonical, reproducible, externally reviewed and finally frozen theorem package.
>
> IMPORTANT: the theorem/counting contract is unchanged unless a genuine defect is explicitly recorded.

## Numeric-only dispatch

```text
13-13a 13-13b 13-13c 13-13d 13-13e 13-13f
13-13fa 13-13fb 13-13fc 13-13fd 13-13fe 13-13ff 13-13fg 13-13fh
13-13g
```

A theorem-level defect blocks promotion.

## Frozen theorem candidate

```text
Stage12 input: C_prim(B) ~ kappa/(12*pi) B(log B)^3
N_q(B)       ~ kappa*I_q/(3*pi^3) B(log B)^3
N1(B)        ~ kappa/(24*pi) B(log B)^3
sum I_q      = pi^2/8
J_q          = 2 I_q/pi
P_q          = 8 I_q/pi^2
O_qr(B)      = o(B(log B)^3)
T(B)         = o(B(log B)^3)
lambda_p     = (p+5)/(2(p+1))
```

Directional validator `(ab,ac,bc)`:

```text
(0.5347369332313988, 0.24535917783225203, 0.21990388893634913)
```

## Completed hardening before R04

```text
STAGE13_13A=COMPLETE_CLAIM_DEPENDENCY_LEDGER
CLAIM_COUNT=30
THEOREM_STATEMENT_FROZEN_FOR_RESYNTHESIS=true
THEOREM_LEVEL_DEFECT_FOUND=false
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false

STAGE13_13B=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT
UNMAPPED_EXTERNAL_INPUTS=0
FAILED_EXTERNAL_HYPOTHESES=0
MINIMAL_EXTERNAL_BOUNDARY_LOCKED=true
GENERAL_SELBERG_DELANGE_BLACK_BOX_REQUIRED=false
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED_FOR_FINAL_PROOF=false
GROWING_MODULUS_INPUT_USED=false

STAGE13_13C=COMPLETE_CANONICAL_PROOF_RESYNTHESIS
MINIMAL_EXTERNAL_BOUNDARY_PRESERVED=true

STAGE13_13D=COMPLETE_DETERMINISTIC_FINAL_CONSISTENCY_AUDIT
AUDIT_STATUS=PASS
CANONICAL_CONSTANTS_REPRODUCED=true
STALE_SUPERSEDED_FORMULAS_IN_CANONICAL_FILES=0

STAGE13_13E=COMPLETE_R04_REVIEW_BUNDLE
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260809-R04
SOURCE_SNAPSHOT_COMMIT=f652833d194bade57794e4c03c184928a54a31b9
CONTENT_SHA256=789656b5bb2190ae62cf2dcae7a3da06ece4f473780a1229ba7284b10b7f4f1b
R04_IMMUTABLE=true
R03_IMMUTABLE=true
```

The deterministic audit is reproducibility/consistency evidence only, not proof validation.

## 13-13f — R04 review ingestion / R05 repair gate

Status: `[!] BLOCKED — repairs in progress`.

Historical R04 verdicts:

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

Active plan: `stages/stage13/13-13f/r05-repair-plan.md`.

### 13-13fa — Gate A complete

Finite exact-one data through `B=5,000,000` do not contradict the claimed limit, no hidden leading q-dependent arithmetic factor was found, and no effective convergence rate is claimed.

```text
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
FINITE_DATA_CONTRADICTS_THEOREM=false
LEADING_Q_DEPENDENT_ARITHMETIC_FACTOR_FOUND=false
COMMON_THETA_AUDIT=PASS_AT_CURRENT_PROOF_LEVEL
PROVED_EFFECTIVE_CONVERGENCE_RATE=false
FINITE_DISCREPANCY_QUANTITATIVELY_EXPLAINED_BY_PROVED_REMAINDER=false
```

### 13-13fb — Gate B complete

The split-prime Wiener estimate is coefficientwise explicit:

```text
WIENER_E_BOUND=17744/243
WIENER_EXACT_CONSTANT=3465625/6561
WIENER_ROUNDED_CONSTANT=529
WIENER_EXPONENT=5/4
P5_EXPLICIT_FINITE_BOUND_LT=432
PHASE_UNIFORM=true
RETAINED_HARMONIC_UNIFORM=true
STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND
```

### 13-13fc — Gate C complete

The curved-region accumulation now has explicit global exponents:

```text
STAGE13_13FC=COMPLETE_CURVED_REGION_ERROR_ACCUMULATION
BOX_COUNT=O((log B)^27)
FINITE_REMAINDER_N=64
FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)
POWER_TAIL_SAVING=exp(-(3/16)(log B)^(1/4))
CURVED_BOUNDARY=O(B(log B)^-5)+lower-order-ledger
MESH_ERROR=O(B(log B)^-5)
```

### 13-13fd — Gate D complete

The retained nonzero harmonic family no longer relies on the unexplained `A=48` ledger. On the fixed strip `Re s>=3/4`, use the proof-facing family interface

```text
S_ell(X) << X^(1-delta_H) (1+ell)^C_H (log(2X))^D_H
```

uniformly for every `X>=2`, `ell>=1`. The retained restriction `ell<=floor((log B)^4)` is imposed only when modes are summed, avoiding the local-`X` mismatch near `H0`.

Partial summation on `h>=H0=exp((log B)^(1/4))`, two base logarithms, and all retained modes give

```text
HARMONIC_POLYLOG_EXPONENT=4*C_H+D_H+6
HARMONIC_STRETCHED_SAVING=exp(-delta_H*(log B)^(1/4))
HARMONIC_CORE=o_A(B(log B)^(-A))_for_every_fixed_A
VAALER_ZERO_MODE_EXCESS=O(B(log B)^-1)
```

The wings are removed by the positive Gate C majorant before Fourier expansion, so no factor `(log B)^4` multiplies their errors.

```text
STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING
HECKE_STRIP_LEFT=3/4
HECKE_FAMILY_BOUND=S_ell(X)<<X^(1-delta_H)(1+ell)^C_H(log(2X))^D_H_for_all_ell>=1
RETAINED_HARMONICS=ell<=floor((log B)^4)
FIXED_A48_REQUIRED=false
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false
WINGS_EXPANDED_HARMONIC_BY_HARMONIC=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
```

## Remaining R05 gates

```text
13-13fe  [>] complete Stage12 R09 counting and factor-two interface
13-13ff  [ ] precise external Hecke/Dirichlet/Vaaler contracts
13-13fg  [ ] expanded fixed inert-prime transfer
13-13fh  [ ] notation cleanup + deterministic-audit scope + R05 synthesis readiness
```

Gate E must copy the exact Stage12 `C_prim` definition, orientation convention, kappa interface, projection and factor-two proof into the repaired proof. Gate F must expose the exact external hypotheses/conclusions used by the Gate D family interface and Vaaler approximation. Gate G expands fixed inert-prime transfer. Gate H performs notation/audit cleanup and determines R05 synthesis readiness.

After A–H, if the theorem survives unchanged, create immutable R05 and obtain fresh independent reviews. R04 verdicts do not automatically count for R05.

13-13f closes only when:

```text
INDEPENDENT_CLOSED_VERDICTS>=2
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0
```

Until then:

```text
STAGE13_13F=BLOCKED_R05_REPAIR_IN_PROGRESS
R05_FRESH_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fe
```

## 13-13g — final freeze

Status: `[ ] BLOCKED by 13-13f`.

Target only after the review gate closes:

```text
STAGE13_13G=COMPLETE_FINAL_FREEZE
STAGE13_GLOBAL_STATUS=FROZEN
EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=THEOREM_LEVEL_REPOSITORY_LOCK
FINAL_REVIEW_BUNDLE_IMMUTABLE=true
DOWNSTREAM_STAGE14_CONTRACT_FROZEN=true
NEXT_STAGE13_ACTION=NONE_UNLESS_A_GENUINE_DEFECT_IS_REPORTED
```

## Global lock

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
STAGE13_13FC=COMPLETE_CURVED_REGION_ERROR_ACCUMULATION
STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fe
```
