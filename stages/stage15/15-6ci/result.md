# Stage15-6ci — large-range complementary-cofactor quantitative profile

Base: Stage15-6ch. Main-batch work unit 2.

For `de>D0`, repaired 6cf gives the exact complementary switch
\[
M_{>D_0}(P)=\sum_{\text{complementary quadruples}\atop de>D_0}\varphi(d)\varphi(e),
\]
with multiplicity one and
\[
de=\sqrt{\frac{A_SB_SA_OB_O}{a_Sb_Sa_Ob_O}}.
\]
Using `phi(d)phi(e)<=de`, one obtains the exact certified receiver
\[
\mathcal M_{>D_0}(B)\le \sum_{P\in A(B)}\sum_{\text{switched quadruples}\atop de>D_0}\sqrt{\frac{A_SB_SA_OB_O}{a_Sb_Sa_Ob_O}}.
\]
No stronger physical-height average is currently proved. To complement 6ch at a polynomial threshold `D0=B^theta`, the large range would need at least an inverse-power profile of the form
\[
\mathcal M_{>D_0}(B)\ll B^{1+o(1)}D_0^{-\sigma}
\]
for some fixed `sigma>0`; the previously targeted high-core profile corresponds morally to `sigma=1`.

The exact complementary switch by itself does **not** supply such a decay: `de>D0` only implies the complementary product `a_Sb_Sa_Ob_O` is small relative to the four-form product, and a physical-height-aware average connecting that form product to `R<=B` is still missing.

Thus the large-range quantitative output is a sharp requirement, not an invented bound.

```text
STAGE15_6_SUBSTAGE=6ci
STAGE15_6CI_LARGE_RANGE_EXACT_RECEIVER=true
STAGE15_6CI_MULTIPLICITY_ONE=true
STAGE15_6CI_INVERSE_D0_DECAY_PROVED=false
STAGE15_6CI_REQUIRED_DECAY=B^(1+o(1))*D0^(-sigma),sigma>0
STAGE15_6CI_EXIT=COUPLED_D0_OPTIMIZATION_AUDIT_READY
```