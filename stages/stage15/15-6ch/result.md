# Stage15-6ch — small-range exact phi-weighted physical root-line sum

Base: repaired Stage15-6cf/6cg with fresh audit PASS. Main-batch work unit 1.

For `de<=D0`, retain the exact weight `phi(d)phi(e)` and use only the already-certified fixed/moderate-level toric root-line count. Writing the certified per-modulus profile schematically as
\[
N_{d,e}(B)\ll \frac{B(\log B)^5}{(de)^2}+B(\log B)^{9/2+\varepsilon}(de)^{10+\varepsilon},
\]
the exact small-range sum satisfies
\[
\mathcal M_{\le D_0}(B)=\sum_{de\le D_0}\varphi(d)\varphi(e)N_{d,e}(B).
\]
Using `phi(n)<=n`,
\[
\sum_{de\le D_0}\frac{\varphi(d)\varphi(e)}{(de)^2}\ll (\log D_0)^2,
\]
while a deliberately crude but safe estimate gives
\[
\sum_{de\le D_0}\varphi(d)\varphi(e)(de)^{10+\varepsilon}\ll D_0^{13+\varepsilon}.
\]
Hence
\[
\boxed{\mathcal M_{\le D_0}(B)\ll B(\log B)^5(\log D_0)^2+B(\log B)^{9/2+\varepsilon}D_0^{13+\varepsilon}.}
\]
This is quantitative and preserves the exact phi weights until the certified inequalities. It only permits a polylogarithmic `D0` without losing the ambient `B^{1+o(1)}` scale; no polynomial `D0=B^theta` window is certified.

```text
STAGE15_6_SUBSTAGE=6ch
STAGE15_6CH_SMALL_RANGE_QUANTIFIED=true
STAGE15_6CH_EXACT_PHI_SUM_START=true
STAGE15_6CH_SMALL_MAIN=B*log(B)^5*log(D0)^2
STAGE15_6CH_SMALL_ERROR=B*log(B)^(9/2+eps)*D0^(13+eps)
STAGE15_6CH_POLYNOMIAL_D0_CERTIFIED=false
STAGE15_6CH_EXIT=LARGE_RANGE_QUANTITATIVE_PROFILE_READY
```