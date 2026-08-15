# Stage24 post-Stage25 R01 — positive-power lower and interaction-sign backflow

STATUS=AUDITED_BACKFLOW_FROM_STAGE25_CHECKPOINT50
HISTORICAL_STAGE24_PASS_REVOKED=false
SOURCE_STAGE=Stage25
SOURCE_CHECKPOINT=50
SOURCE_PR=984
SOURCE_AUDIT=stages/stage25/25-50/audit.md

Stage24's historical closeout remains valid at its audit time. Stage25 checkpoint50 provides a stronger later target lower:

\[
\boxed{N_2(B)\gg B^{1/4}}.
\]

Since

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\]

we now have

\[
\boxed{
\frac{N_2(B)}{M_2(B)}\gg B^{-3/4}(\log B)^{-5}.
}
\]

Together with the existing upper,

\[
\boxed{
B^{-3/4}(\log B)^{-5}
\ll
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
}
\]

The zero-density conclusion remains unchanged.

## Ambient interaction sign resolved

The audited Stage16S ambient space-survival baseline is

\[
S_0(B)\asymp B^{-1}.
\]

Therefore

\[
J_2(B)=\frac{N_2(B)/M_2(B)}{S_0(B)}
\gg B^{1/4}(\log B)^{-5}\to\infty.
\]

Thus Stage24's previously unresolved global interaction sign is now rigorously positive/divergent.

## Second-order interaction sign resolved

Using

\[
S_1(B)=N_1(B)/M_1(B)\asymp B^{-1}(\log B)^2,
\]

we get

\[
I(B)=\frac{N_2/M_2}{N_1/M_1}
\gg B^{1/4}(\log B)^{-7}\to\infty.
\]

Thus the Stage22/23 second-order interaction sign is also positive/divergent.

```text
CURRENT_TARGET_LOWER=N2(B)>>B^(1/4)
CURRENT_SURVIVOR_RATIO_LOWER=N2/M2>>B^(-3/4)(log B)^(-5)
STAGE24_CLASS=THIN_BUT_POSITIVE_POWER_INFINITE
STAGE24_GLOBAL_INTERACTION_SIGN=POSITIVE_DIVERGENT
SECOND_ORDER_INTERACTION_SIGN=POSITIVE_DIVERGENT
ZERO_DENSITY_REMAINS_PROVED=true
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
```
