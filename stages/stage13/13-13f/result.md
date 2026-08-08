# Stage13-13f — external review gate status

> STATUS: `STAGE13_13F_BLOCKED_R04_REPAIR_REQUIRED`
>
> TARGET_BUNDLE_ID: `STAGE13-FINAL-SELF-CONTAINED-20260809-R04`
>
> TARGET_CONTENT_SHA256: `789656b5bb2190ae62cf2dcae7a3da06ece4f473780a1229ba7284b10b7f4f1b`

## Current gate

Three independent R04 reviews have been received and recorded:

```text
GROK_R04_VERDICT=CLOSED
CLAUDE_R04_VERDICT=OPEN
DEEPSEEK_R04_VERDICT=REPAIRABLE
QWEN_R04_VERDICT=NOT_RECORDED
INDEPENDENT_CLOSED_VERDICTS=1
UNRESOLVED_SUBSTANTIVE_REVIEW_OBJECTIONS=2
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=2
R04_REPAIR_REQUIRED=true
R04_IMMUTABLE=true
PROMOTE_TO_13_13G=false
```

Grok reports no fatal or major theorem-level defect. Claude raises an OPEN objection centered on the unresolved relationship between finite directional behavior and the claimed limiting vector, plus the hidden `529 p^{-5/4}` and box-error derivations. DeepSeek independently judges the central strategy plausible but the R04 proof package not sufficiently self-contained or explicit, and explicitly recommends an R05/R06 revision.

## Claude OPEN objection

The theorem candidate predicts

```text
P = (0.5347369332313988,
     0.24535917783225203,
     0.21990388893634913),
```

while the committed `B=100000` exactly-one fixture `(84146,43180,40704)` remains much closer to `2:1:1`. Finite disagreement does not refute an asymptotic theorem, but R04 does not quantitatively show that the observed discrepancy is compatible with its remainder or exclude an omitted q-dependent leading arithmetic factor.

This objection must be closed by a dedicated finite-cutoff/secondary-term audit and a retracing of q-independence of the top arithmetic coefficient.

## DeepSeek REPAIRABLE objections

DeepSeek requests explicit closure of the following proof-critical interfaces:

1. derive or fully expose `||C_{ell,p}-1||_{5/8} <= 529 p^{-5/4}`;
2. make small-height/small-coordinate/core/boundary error estimates and `O((log B)^C)` box accumulation quantitatively auditable;
3. expose the conductor/log bookkeeping for all retained nonzero harmonics `ell <= (log B)^4`;
4. copy a complete Stage12 R09 counting interface into the review proof, including the exact definition of `C_prim(B)`, orientation convention, `kappa` interface and the factor-two projection bridge;
5. state the exact imported Hecke/Dirichlet and Vaaler hypotheses actually used;
6. expand the fixed inert-prime transfer, including principal/nonprincipal character tuples and the fixed-conductor `o(B(log B)^3)` bound;
7. remove ambiguous angle notation and make `C_{ell,p}` substitutions and p-dependence explicit;
8. keep deterministic `PASS` explicitly scoped to reproducibility checks rather than proof validation.

These are classified `REPAIRABLE` rather than a direct disproof, but they are substantive enough that R04 cannot be frozen as the final proof package.

## Active repair plan

The combined Claude + DeepSeek closure plan is recorded at

```text
stages/stage13/13-13f/r05-repair-plan.md
```

It contains eight mandatory gates covering the finite-ratio/q-independence audit, Wiener derivation, box-error accumulation, harmonic uniformity, Stage12 interface, external theorem contracts, fixed-prime transfer, and notation/audit-scope cleanup.

## Gate decision

The Stage13-13f gate is **blocked**. A later `CLOSED` review cannot numerically outvote unresolved substantive objections.

R04 remains immutable. The active repair/closure audit must determine whether the theorem statement survives unchanged; if it does, the repaired canonical proof must be packaged as a new immutable R05 and freshly reviewed. If the q-independence audit discovers a genuine leading-term defect, the theorem contract itself must be reopened before any new bundle is promoted.

```text
STAGE13_13F=BLOCKED_R04_REPAIR_REQUIRED
GROK_R04_VERDICT=CLOSED
CLAUDE_R04_VERDICT=OPEN
DEEPSEEK_R04_VERDICT=REPAIRABLE
QWEN_R04_VERDICT=NOT_RECORDED
INDEPENDENT_CLOSED_VERDICTS=1
REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=2
R04_REPAIR_REQUIRED=true
R05_REQUIRED_IF_THEOREM_SURVIVES_AUDIT=true
R05_FRESH_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13f
```
