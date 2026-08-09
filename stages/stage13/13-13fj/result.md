# Stage13-13fj — fresh R05 external-review ledger

> STATUS: `STAGE13_13F_R05_FRESH_REVIEW_BLOCKED_R06_REQUIRED`

## Immutable review target

```text
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260809-R05
SOURCE_SNAPSHOT_COMMIT=79f03341b67dd49a8c128cfbeba3f756c91de6f6
CONTENT_SHA256=4214a6e3621b52ce39373799b48fc8325351f650514e732d6e2244d28d475458
BUNDLE_PATH=review/STAGE13-FINAL-SELF-CONTAINED-20260809-R05.html
R05_IMMUTABLE=true
R04_VERDICTS_CARRY_FORWARD_TO_R05=false
```

## Fresh reviewer ledger

```text
GROK_R05_VERDICT=CLOSED
CLAUDE_R05_VERDICT=OPEN
QWEN_R05_VERDICT=OPEN
QWEN_R05_REVIEWER_LABEL=NEAR_ACCEPTABLE_CONDITIONAL
DEEPSEEK_R05_VERDICT=OPEN
DEEPSEEK_R05_REVIEWER_LABEL=REPAIR_REQUIRED_CONDITIONAL_ACCEPT

R05_INDEPENDENT_CLOSED_VERDICTS=1
R05_REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2
R05_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=3
R05_SUBSTANTIVE_REPAIR_REQUIRED=true
R06_REQUIRED=true
```

Grok's user-relayed external review is recorded at `grok-r05-verdict.md` and is `CLOSED`. Claude's review is `OPEN`. Qwen's zero-base review is `OPEN`. DeepSeek's fresh adversarial review is recorded at `deepseek-r05-verdict.md`; its final label is conditional repair required, therefore the repository freeze gate records it as `OPEN`.

## What the independent reviews strongly validate

Claude and Qwen independently reconstructed the repaired Wiener/error arithmetic and report exact agreement with R05, including `17744/243`, `3465625/6561 < 529`, the `(log B)^27` box ledger and the all-box `(log B)^-35` remainder. DeepSeek also recognizes the explicit Wiener derivation, non-circular common-Theta ordering, external-contract exposure and deterministic-audit scope as substantial improvements.

## Unresolved theorem-level objection 1 — Gaussian-Hecke primary-source contract / normalization

Claude requires primary-source verification of the exact proof-facing Gaussian-Hecke family. DeepSeek independently strengthens this objection by requiring the definition of `Xi_k` and its completed functional equation/gamma factor to match the cited source normalization exactly. R06 must verify analytic continuation, functional equation, holomorphy/no pole at `s=1` for nonzero angular modes, fixed finite twists, and sufficient fixed-strip polynomial growth.

## Unresolved theorem-level objection 2 — analytic chamber normalization

Qwen identifies the missing symbolic proof of

```text
I_ab + I_ac + I_bc = pi^2/8.
```

Numerical quadrature is validation only. Because this identity normalizes the directional proportions and total exactly-one constant, R06 must contain an analytic derivation.

## Unresolved theorem-level objection 3 — fixed-S principal pole sector / pole-loss closure

DeepSeek requires §14 to be made proof-facing rather than intensional: explicitly characterize the unbounded pole-producing channels, include auxiliary-character aliasing/algebraic relations, show that the full principal pole sector reproduces `product_{p in S} lambda_p`, prove the tagged factor `2` never undercounts the true overlap states, and show every tuple outside that sector leaves at least one induced unbounded channel genuinely nonprincipal, hence loses at least one pole and contributes `o_S(B(log B)^3)`.

## R06 repair plan

Mandatory:

1. analytic proof of `sum_q I_q=pi^2/8`;
2. exact Gaussian-Hecke primary-source contract and normalization closure;
3. explicit principal-pole-sector / channel / aliasing / tagged-upper-bound proof for fixed-S transfer.

Proof-facing hardening to include while rebuilding R06:

- define Wiener `M` explicitly;
- expose the `p=5` `<432` calculation and state `ell>=1` in `C_{ell,p}`;
- state `lambda_3=1`, hence inert contraction starts at `p>=7`;
- strengthen the finite-data nonclaim;
- expand Gelfand–Leray radial normalization;
- expose OE/EE 2-adic face-independence;
- display `O((log B)^27)` as `(O((log B)^9))^3`;
- decompose the harmonic `4*C_H+D_H+6` exponent;
- state Vaaler endpoint convention / measure-zero handling;
- retain `theta`/`vartheta` separation and optionally expose the elementary `kappa` Euler-product convergence expansion.

## Gate decision

No majority vote overrides an unresolved theorem-level objection. R05 remains immutable historical review evidence. R06 is mandatory and must restart external review from zero.

```text
STAGE13_13F=BLOCKED_R05_R06_REPAIR_REQUIRED
STAGE13_13FJ=R05_FRESH_REVIEW_BLOCKED_R06_REQUIRED
R05_INDEPENDENT_CLOSED_VERDICTS=1
R05_REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2
R05_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=3
CLAUDE_H1_H2_PRIMARY_SOURCE_VERIFICATION_REQUIRED=true
QWEN_SUM_IQ_ANALYTIC_DERIVATION_REQUIRED=true
DEEPSEEK_PRINCIPAL_POLE_SECTOR_CLOSURE_REQUIRED=true
R05_SUBSTANTIVE_REPAIR_REQUIRED=true
R06_REQUIRED=true
R06_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R05_IMMUTABLE=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fj
```
