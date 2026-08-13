# Stage18-30 — ratio / thinning law

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage18 counts the audited primitive canonical exactly-two-face population `M_2(B)` under `R<=B`, with no integral-space-diagonal requirement.

Frozen Stage15 gives
\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]
Frozen Stage16 gives the matched ambient primitive/canonical population
\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2).
\]
The population, cutoff, multiplicity and physical counting measure match literally. Therefore
\[
\boxed{\frac{M_2(B)}{U(B)}\sim \frac{36\zeta(3)C_{M_2}}{\pi}\frac{(\log B)^5}{B^2}\to0}.
\]
Thus the Stage18 population is polynomially sparse of ambient order `B^-2` with a `(log B)^5` factor.

This is an ambient-density statement only. The conditional Stage16 -> Stage18 survival ratio `M_2(B)/M_1(B)` belongs to Stage22 and is not claimed here.

```text
RATIO_SOURCE=ambient U(B)
RATIO_TARGET=M_2(B)
RATIO_ASYMPTOTIC=(36*zeta(3)*C_M2/pi)*(log B)^5/B^2
RATIO_LIMIT=0
POLYNOMIAL_THINNING_POWER=2
LOG_POWER=5
LEADING_CONSTANT=36*zeta(3)*C_M2/pi
EVIDENCE_LEVEL=PROVED_FROM_FROZEN_STAGE15_AND_STAGE16
FINITE_DATA_USED_AS_PROOF=false
STAGE16_TO_18_CONDITIONAL_RATIO=DEFER_TO_STAGE22
CODEX_REQUIRED=false
AUDIT_REQUIRED=true
```
