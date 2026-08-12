# Stage15-6bx — channel-gcd product first-moment theorem gate

Audit verdict: NEW_GATE.

By 6bw it is enough for the desired high-core estimate to prove

\[
\boxed{\sum_{P\in\mathcal A(B)}G_S(P)G_O(P)\ll B^{1+o(1)}}.
\]

Indeed this would imply `N_{q>Q}(B) << B^{1+o(1)}/Q`, exactly the high-core interface required by Stage15-6bo.

The receiver is materially narrower than a generic dimension-two sieve: it is a first moment of the explicit gcd product

\[
\gcd(m^2+n^2,r^2-s^2)\gcd(m^2-n^2,r^2+s^2)
\]

over the physical toric height measure.

A divisor expansion suggests logarithmic expected cost because each divisor imposes codimension-two congruences, but the required polynomial-level uniform summation under the moving primitive-height normalizer has not been proved. This is now the unique gate.

```text
STAGE15_6_SUBSTAGE=6bx
STAGE15_6BX_AUDIT_VERDICT=NEW_GATE
STAGE15_6BX_REQUIRED_OBJECT=PHYSICAL_CHANNEL_GCD_PRODUCT_FIRST_MOMENT
STAGE15_6BX_TARGET=SUM_GS_GO<=B^(1+o(1))
STAGE15_6BX_IMPLICATION=HIGH_CORE_B_OVER_Q
STAGE15_6BX_CAUSAL_THREE_QUARTERS_PROVED=false
STAGE15_6BX_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6BX_EXIT=PHYSICAL_CHANNEL_GCD_PRODUCT_FIRST_MOMENT_THEOREM_GATE
```
