# Stage15-6bp — Huang polynomial-window audit

Base: merged PR #853. Audit verdict: BLOCK.

For the Stage15 split toric surface, Picard rank r=6 and dim X=2. Huang v3 Theorem 1.4 gives an effective adelic-neighbourhood error of shape

\[
O_\epsilon(\mathcal L(\mathcal F_f)^{10+\epsilon} B(\log B)^{9/2+\epsilon}).
\]

The Stage15 fixed-q two-coordinate rootline neighbourhood has main mass q^{-2+o(1)}, hence main term B(log B)^5/q^2. With covering exponent L comparable to q, main dominance requires q^{12+o(1)} << (log B)^{1/2}. Therefore q=B^{1/4} is not in the certified window.

```text
STAGE15_6_SUBSTAGE=6bp
STAGE15_6BP_AUDIT_VERDICT=BLOCK
STAGE15_6BP_HUANG_R=6
STAGE15_6BP_HUANG_DIM=2
STAGE15_6BP_NEIGHBOURHOOD_EXPONENT=10
STAGE15_6BP_POLYNOMIAL_q_WINDOW=false
STAGE15_6BP_B14_WINDOW=false
STAGE15_6BP_EXIT=LOGARITHMIC_LEVEL_CERTIFICATE_READY
```
