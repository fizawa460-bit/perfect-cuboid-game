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
DEEPSEEK_R05_VERDICT=NOT_RECORDED

R05_INDEPENDENT_CLOSED_VERDICTS=1
R05_REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2
R05_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=2
R05_SUBSTANTIVE_REPAIR_REQUIRED=true
R06_REQUIRED=true
```

Grok's user-relayed external review is recorded at `stages/stage13/13-13fj/grok-r05-verdict.md` and is `CLOSED`.

Claude's user-relayed external review is recorded at `stages/stage13/13-13fj/claude-r05-verdict.md` and is `OPEN`.

Qwen's user-relayed zero-base external review is recorded at `stages/stage13/13-13fj/qwen-r05-verdict.md`. Qwen labels the bundle `NEAR-ACCEPTABLE / CONDITIONAL`, but explicitly recommends against freeze until a high-severity proof-completeness defect is repaired; for the repository gate this is therefore `OPEN`.

## What the independent reviews strongly validate

Claude and Qwen independently reconstructed the repaired Wiener/error arithmetic and report exact agreement with R05, including:

```text
||a||_rho <= (8/3) rho
||b||_rho <= (44/9) rho
||M||_rho <= (32/9) rho^2
||E_vartheta||_rho <= (17744/243) rho^2
||C_vartheta-1||_rho <= (3465625/6561) rho^2 < 529 rho^2
BOX_ACCUMULATION=(log B)^-62 * (log B)^27 = (log B)^-35
HARMONIC_AGGREGATION_EXPONENT=4*C_H+D_H+6
```

Qwen also confirms the repaired all-ell Riesz/Perron route, fixed-S order of limits, inert multiplier, Stage12 calibration and factor-two bridge are internally coherent at the reviewed level.

## Unresolved theorem-level objection 1 — Claude external H1/H2 boundary

Claude does not accept `CLOSED` while the exact Gaussian-Hecke primary-source boundary remains independently unverified for the proof-facing family:

```text
k=8 ell, ell>=1
required fixed residue twists
analytic continuation / functional equation
no pole at s=1 for the nonzero angular family
required fixed-strip / conductor growth
```

This external-boundary objection may in principle be closed by a primary-source audit if the cited theorems exactly imply the proof-facing contract.

## Unresolved theorem-level objection 2 — Qwen geometric normalization identity

Qwen identifies a separate high-severity proof-completeness defect:

```text
I_ab + I_ac + I_bc = pi^2/8
```

is asserted in the R05 canonical proof without an analytic derivation. The deterministic Simpson computation is only a validator and cannot prove the identity. Because this identity normalizes both the directional proportions and the total exactly-one constant, Qwen requires a symbolic derivation in the proof-facing text.

That change is substantive. R05 is immutable, so this repair cannot be made in R05 and requires a new R06 (or later) bundle.

## R06 repair ledger

Mandatory:

1. prove `sum_q I_q=pi^2/8` analytically, directly by chamber partition/symmetry or via the `J_q` bridge with an analytic proof of `sum_q J_q=pi/4`;
2. resolve Claude's H1/H2 primary-source boundary or replace it with a fully justified proof-facing external contract.

Recommended explicitness repairs to include while rebuilding the proof:

3. define the Wiener mixed term `M` explicitly before the `32/9` bound;
4. state explicitly that inert `p=3` gives `lambda_3=1`, hence contraction uses inert `p>=7`;
5. strengthen the finite-data caveat: the `100k -> 5m` data are neither a contradiction nor positive convergence evidence;
6. expand the Gelfand–Leray radial normalization leading to the dimensionless `1/(P/d)` factor;
7. expose OE/EE 2-adic face-independence branchwise;
8. identify the unbounded pole-producing channels and their character-twist pole loss;
9. decompose the `4*C_H+D_H+6` harmonic exponent ledger.

## Gate decision

The freeze condition is not met, and majority voting cannot override either unresolved theorem-level objection. Because Qwen's high-severity objection requires a proof-text change, R05 is now historical immutable review evidence and a repaired immutable R06 is required before final freeze.

```text
STAGE13_13F=BLOCKED_R05_R06_REPAIR_REQUIRED
STAGE13_13FJ=R05_FRESH_REVIEW_BLOCKED_R06_REQUIRED
R05_INDEPENDENT_CLOSED_VERDICTS=1
R05_REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2
R05_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=2
CLAUDE_H1_H2_PRIMARY_SOURCE_VERIFICATION_REQUIRED=true
QWEN_SUM_IQ_ANALYTIC_DERIVATION_REQUIRED=true
R05_SUBSTANTIVE_REPAIR_REQUIRED=true
R06_REQUIRED=true
R05_IMMUTABLE=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13fj
```
