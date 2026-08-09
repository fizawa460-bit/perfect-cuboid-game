# DeepSeek R05 adversarial review verdict

> REVIEW_TARGET: `STAGE13-FINAL-SELF-CONTAINED-20260809-R05`
>
> REPOSITORY_GATE_VERDICT: `OPEN`
>
> REVIEWER_LABEL: `REPAIR_REQUIRED_CONDITIONAL_ACCEPT`

DeepSeek's user-relayed fresh adversarial review judges R05 substantially improved over R04 but not yet freeze-ready. The review explicitly requests revision before acceptance, so the repository freeze gate records it as `OPEN`, not `CLOSED`.

## High-severity objections

1. **Principal pole sector / auxiliary-character aliasing (§14).** The proof-facing definition remains too intensional. R06 should characterize the principal pole sector explicitly enough to show that its full contribution reproduces the local average `product_{p in S} lambda_p`, including algebraic relations among auxiliary coordinates. The tagged factor `2` used for the overlap upper bound must also be shown to cover every evaluated overlap state and never undercount.

2. **Nonprincipal pole loss (§14).** R06 should define the unbounded pole-producing channels explicitly and show that every tuple outside the principal pole sector leaves at least one such induced channel genuinely nonprincipal after all possible character aliasing/cancellation. This is the proof-facing justification for the `o_S(B(log B)^3)` remainder.

3. **Gaussian-Hecke functional-equation normalization (§7 / H1-H2).** DeepSeek independently flags the exact normalization of `Xi_k` and the completed functional equation. R06 must match the primary source's definition and gamma factor exactly, and explain why the chosen normalization yields the only properties subsequently used: entire/holomorphic nonzero angular family, no pole at `s=1`, and fixed-strip polynomial growth in the angular/conductor parameter.

4. **Box count explicitness (§8).** The stated `O((log B)^27)` bound is accepted as a safe coarse upper bound, but R06 should display the calculation: with `Lambda=log B`, `eta=Lambda^-8`, each of `h,r,s` has at most `O(log(2B)/eta)=O(Lambda^9)` multiplicative mesh intervals, hence at most `O(Lambda^27)` product boxes before imposing the curved constraint.

## Medium / low explicitness requests

- state endpoint convention or measure-zero handling for Vaaler interval majorants/minorants;
- expose the `p=5` Wiener bound `<432` calculation, since `rho=5^-5/8>1/4` and the `p>=13` shortcut is not literally reusable;
- state explicitly that `ell>=1` in `C_{ell,p}` is the nonzero Gaussian angular mode;
- strengthen the finite-data caveat: finite data are neither proof of convergence nor a refutation of the asymptotic theorem absent an effective remainder;
- retain the `theta` / `vartheta` notation separation and audit it mechanically;
- optionally show the elementary `1+O(p^-2)` expansion proving absolute convergence of the explicit `kappa` Euler product.

## Positive findings

DeepSeek acknowledges the R05 improvements: exact external-contract section, explicit `529 p^-5/4` derivation, non-circular common-Theta ordering, and deterministic-audit scope limitation. The review does not claim the central theorem is false; it requires proof-facing clarification/repair before freeze.

## Gate consequence

This review reinforces the already-required R06. It adds no route for majority voting around the open objections.

```text
DEEPSEEK_R05_VERDICT=OPEN
DEEPSEEK_R05_REVIEWER_LABEL=REPAIR_REQUIRED_CONDITIONAL_ACCEPT
R05_PROMOTION_ALLOWED=false
R06_REQUIRED=true
```
