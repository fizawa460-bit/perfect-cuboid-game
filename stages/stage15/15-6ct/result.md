# Stage15-6ct — exact cross-gcd cell factorization

Base: merged Stage15-6cs with fresh audit PASS. Main-batch work unit 1.

Put
\[
a=\gcd(m,r),\quad b=\gcd(m,s),\quad c=\gcd(n,r),\quad d=\gcd(n,s).
\]
Because `(m,n)=(r,s)=1`, the four cells `a,b,c,d` are pairwise coprime. There are unique positive residuals `M,N,U,V` with
\[
m=abM,\quad n=cdN,\quad r=acU,\quad s=bdV,
\]
and all four residual cross-gcds are one. Thus
\[
h_\alpha=bc,\qquad h_\beta=ad,\qquad H:=h_\alpha h_\beta=abcd.
\]
Stage15-6aj gives `G=gamma H`, `gamma in {2,4}`. The physical shared edge therefore has the exact form
\[
E_{phys}=\frac{4mnrs}{\gamma H}=\frac4\gamma H MNUV.
\]
Since `E_phys<=R<=B`,
\[
\boxed{H M N U V\le B.}
\]
(up to the harmless exact factor `gamma/4<=1`). This is a second exact physical product-height bridge, now in the common normalizer cells.

The channel gcds are arithmetically transverse to the normalizer. If `p|H`, then `p` divides exactly one of `m,n` and exactly one of `r,s`; hence neither `m^2+n^2` nor `m^2-n^2` is `0 mod p`. Therefore
\[
\boxed{\gcd(H,G_SG_O)=1.}
\]
Consequently every switched modulus `q=de` with `d|G_S`, `e|G_O` satisfies
\[
\boxed{\gcd(q,H)=1.}
\]
(up to the already isolated bounded 2-adic convention). Thus the moving primitive normalizer changes the physical measure but cannot share the odd channel modulus.

This exact transversality is the common geometry needed by both live receivers.

```text
STAGE15_6_SUBSTAGE=6ct
STAGE15_6CT_CROSS_GCD_CELLS_EXACT=true
STAGE15_6CT_H=abcd
STAGE15_6CT_PHYSICAL_CELL_PRODUCT_HEIGHT=H*M*N*U*V<=B
STAGE15_6CT_CHANNEL_GCD_COPRIME_TO_H=true
STAGE15_6CT_SWITCHED_MODULUS_COPRIME_TO_H=true
STAGE15_6CT_EXIT=NORMALIZER_ONLY_EXPONENT_TEST_READY
```