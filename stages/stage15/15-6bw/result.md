# Stage15-6bw — channel-gcd majorant reduction

Audit verdict: PASS.

Let

\[
G_S=\gcd(m^2+n^2,r^2-s^2),\qquad
G_O=\gcd(m^2-n^2,r^2+s^2).
\]

From Stage15-6aa, `k_S|G_S`, `k_O|G_O`, `(k_S,k_O)=1`, and the actual odd core is `q=k_S k_O`. Therefore

\[
\boxed{q\mid G_SG_O.}
\]

Thus every survivor with `q>Q` lies in the tail `G_SG_O>Q`, and Markov gives the exact upper-bound interface

\[
N_{q>Q}(B)\le Q^{-1}\sum_{P\in\mathcal A(B)}G_S(P)G_O(P),
\]

where `A(B)` is the ambient physical shared-edge population. No actual-core multiplicity or orientation sum is needed in this inequality.

This replaces the moving-squarefree-core sieve by a first-moment problem for two explicit channel gcds.

```text
STAGE15_6_SUBSTAGE=6bw
STAGE15_6BW_AUDIT_VERDICT=PASS
STAGE15_6BW_CHANNEL_GCD_MAJORANT=q|G_S*G_O
STAGE15_6BW_MARKOV_HIGH_CORE_REDUCTION=true
STAGE15_6BW_GCD_PRODUCT_FIRST_MOMENT_PROVED=false
STAGE15_6BW_EXIT=CHANNEL_GCD_PRODUCT_FIRST_MOMENT_AUDIT_READY
```
