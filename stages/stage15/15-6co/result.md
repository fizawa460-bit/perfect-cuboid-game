# Stage15-6co — large complementary reciprocal-product audit

Base: Stage15-6cn. Main-batch work unit 2.

The four channel forms factor exactly as
\[
A_SA_O=(m^2+n^2)|m^2-n^2|=|m^4-n^4|,
\]
\[
B_SB_O=|r^2-s^2|(r^2+s^2)=|r^4-s^4|.
\]
Thus the numerator in the switched large-range weight is
\[
\sqrt{A_SB_SA_OB_O}
=
\sqrt{|m^4-n^4|\,|r^4-s^4|}.
\]
A direct pointwise domination by the raw physical diagonal height was tested and fails. Indeed with `n=s=1` and `m=r=T`,
\[
\sqrt{A_SB_SA_OB_O}\asymp T^4,
\]
whereas the exact raw diagonal identity gives
\[
R_{\rm raw}^2=4(m^2r^2+n^2s^2)(m^2s^2+n^2r^2)\asymp 8T^6,
\]
so `R_raw\asymp T^3` and the ratio grows like `T`. Therefore the needed inverse-`D0` gain cannot be obtained from a universal pointwise inequality comparing the four-form numerator to raw height.

This negative certificate does not rule out a primitive-normalized average: the moving gcd normalizer may correlate with precisely the unbalanced configurations above. But such correlation must be proved statistically in the physical `R<=B` measure; it cannot be inserted pointwise.

Consequently the minimal large-side theorem species remains an averaged reciprocal complementary-product estimate. A useful target is
\[
\mathcal M_{>D_0}(B)\ll B^{1+o(1)}D_0^{-\sigma}
\]
for some fixed `sigma>0`, derived only after primitive normalization.

```text
STAGE15_6_SUBSTAGE=6co
STAGE15_6CO_FORM_PRODUCT_FACTORIZATION=true
STAGE15_6CO_RAW_HEIGHT_POINTWISE_DOMINATION=false
STAGE15_6CO_COUNTERSCALING=n=s=1,m=r=T
STAGE15_6CO_PRIMITIVE_AVERAGE_STILL_LIVE=true
STAGE15_6CO_INVERSE_D0_DECAY_PROVED=false
STAGE15_6CO_EXIT=COUPLED_OVERLAP_RECOMPUTE_READY
```