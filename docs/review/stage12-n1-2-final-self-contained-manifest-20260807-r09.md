# Stage12-N1-2 final self-contained manifest R09

> **BUNDLE_ID:** `PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09`
>
> **COMPLETED_THROUGH:** `Stage12-N1-3j`
>
> **SOURCE_SNAPSHOT_COMMIT:** `d69a6e2ee352700660776f55a749eebb432552f9`
>
> **SOURCE_LEDGER_SHA256:** `800a664bf940e751cb1fafc7758a2692c6950eecb6ef94784738d276a4a0debe`
>
> **FINAL_DOCUMENT:** `docs/stage12-n1-2-final-r08-self-contained.md`
>
> **PHYSICAL_PAGE:** `review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html`
>
> **DOCUMENT_STATUS:** `SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL_FINAL_TEXT`

## Purpose

R08 removed the old Stage12-N1-2p dependency and made the proof self-contained at the stated published-theorem level. A final external recalculation then identified one remaining exposition gap in R08 §2 and one wording ambiguity in the vertical-growth ledger:

1. the implication from local weighted `l1` norms to the global Euler-product coefficient norm was stated but not proved in full;
2. the vertical-growth line could be read as if a functional equation were being attributed to `J_beta`, although the intended argument only uses a functional equation for `L(s,chi_4)`.

Stage12-N1-3j closes both points without changing any main term, local factor, exponent, radial calculation, wing estimate, shallow-sector estimate, or error budget.

## Required active closure

The R09 final text must contain explicit proofs of

\[
\|f*g\|_\delta\le\|f\|_\delta\|g\|_\delta
\]

for two-variable Dirichlet convolution, and

\[
\sum_q\|C_q-1\|_\delta<\infty
\Longrightarrow
\left\|\prod_q C_q\right\|_\delta<\infty.
\]

The finite-product argument must include both a uniform norm bound and a Cauchy estimate. The coefficientwise limit must be identified with the Euler product.

The vertical-growth ledger must state explicitly:

```text
J_beta: absolute convergence => bounded
L(s,chi_4): functional equation + Stirling + Phragmen--Lindelof => polynomial growth
H_beta=L*J_beta: product => polynomial growth
J_BETA_FUNCTIONAL_EQUATION_ASSUMED=false
```

## External theorem boundary

The only theorem-level external analytic input intentionally retained is the published finite-order Selberg--Delange theorem. Its working form and the `z=1` / `z=2` application map are already embedded in the R08 parent proof.

This project does not attempt to reprove Selberg--Delange itself.

## Mathematical scope

The only asymptotic frozen by this Stage12-N1-2 proof is

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3
\]

for the primitive oriented count defined in the embedded proof.

It does not assert perfect-cuboid existence, a canonical-count asymptotic, an exact-one-face asymptotic, or a final face ratio.

## Final state requested from the bundle

```text
WEIGHTED_L1_DIRICHLET_SUBMULTIPLICATIVITY=CLOSED
EULER_PRODUCT_TO_GLOBAL_WEIGHTED_L1=CLOSED
VERTICAL_GROWTH_ROLE_SEPARATION=CLOSED
J_BETA_FUNCTIONAL_EQUATION_ASSUMED=false
OLD_2P_ACTIVE_DEPENDENCY=NONE
SELBERG_DELANGE_THEOREM=EXTERNAL_PUBLISHED_THEOREM_LEVEL_INPUT
NEW_CENTRAL_MATHEMATICAL_GAP=NONE_IDENTIFIED
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
THEOREM_SCOPE=PRIMITIVE_ORIENTED_COUNT_ONLY
ADDITIONAL_EXTERNAL_REVIEW=NOT_REQUIRED_AS_PROJECT_GATE
```

`CONTENT_SHA256` is filled into the PR record after deterministic generation succeeds.
