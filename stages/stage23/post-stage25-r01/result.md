# Stage23 post-Stage25 R01 — positive-power backflow

STATUS=AUDITED_BACKFLOW_FROM_STAGE25_CHECKPOINT50
HISTORICAL_STAGE23_PASS_REVOKED=false
SOURCE_STAGE=Stage25
SOURCE_CHECKPOINT=50
SOURCE_PR=984
SOURCE_AUDIT=stages/stage25/25-50/audit.md

Stage25 checkpoint50 upgrades the common Stage19 numerator lower to

\[
N_2(B)\gg B^{1/4}.
\]

With the audited Stage17 law

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\]

we obtain

\[
\boxed{
\frac{N_2(B)}{N_1(B)}\gg B^{-3/4}(\log B)^{-3}.
}
\]

The audited upper remains

\[
\frac{N_2(B)}{N_1(B)}\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

Thus Stage23 remains a zero-density transition with an infinite target, now with a positive-power target lower.

## New shared-b channel

The Stage25 family canonicalizes as `(a,b,c)=(B/g,C/g,A/g)` and guarantees faces `ab` and `bc`. Therefore

\[
\boxed{N_{2,b}(B)\gg B^{1/4}},
\]

and the corresponding Stage17 raw pair-overlap channel satisfies

\[
\boxed{A_{ab,bc}(B)\gg B^{1/4}}.
\]

This is distinct from the earlier C17 shared-`c` channel lower.

## Second-order interaction

Stage22 gives

\[
M_2/M_1\asymp B^{-1}(\log B)^4.
\]

Hence the exact cross-ratio

\[
I=\frac{N_2/N_1}{M_2/M_1}
\]

obeys

\[
\boxed{I(B)\gg B^{1/4}(\log B)^{-7}\to\infty}.
\]

The previously unresolved second-order interaction sign is therefore positive/divergent.

```text
RATIO_LOWER=N2/N1>>B^(-3/4)(log B)^(-3)
RATIO_UPPER=N2/N1<<_epsilon B^(-1/2+epsilon)(log B)^(-3)
TARGET_POSITIVE_POWER_LOWER_PROVED=true
TARGET_POSITIVE_POWER_EXPONENT=1/4
N2_B_LOWER=N2,b(B)>>B^(1/4)
A_AB_BC_LOWER=A_ab,bc(B)>>B^(1/4)
SECOND_ORDER_INTERACTION_SIGN=POSITIVE_DIVERGENT
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
```
