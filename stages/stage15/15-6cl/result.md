# Stage15-6cl — large complementary-cofactor decay audit

Base: Stage15-6ck. Main-batch work unit 2.

Start from the repaired exact switched receiver. For every large-range term `de>D0`,
\[
de=\sqrt{\frac{A_SB_SA_OB_O}{a_Sb_Sa_Ob_O}},
\]
so equivalently
\[
a_Sb_Sa_Ob_O<\frac{A_SB_SA_OB_O}{D_0^2}.
\]
This gives a genuine `D0^{-2}` shrinkage of the *allowed complementary product volume*, but not yet of the weighted state count. The exact weight satisfies only
\[
\varphi(d)\varphi(e)\le de,
\]
and after substitution this reintroduces the square root of the four-form product. Therefore a statewise bound of size `D0^{-sigma}` does not follow without averaging the reciprocal complementary product against the physical `R<=B` measure.

Two candidate estimates were tested:

1. Markov on `de>D0` using `1_{de>D0}<=de/D0` raises the weight to `(de)^2/D0` and is worse; BLOCKED.
2. Complementary-volume truncation using the inequality above is promising only if one proves a physical average of divisor quadruples with weight `(a_Sb_Sa_Ob_O)^(-1/2)` or stronger. No such average is presently certified.

Hence no inverse-`D0` decay is proved. The exact minimal large-side target is now:
\[
\sum_{P\in A(B)}\sum_{\mathrm{comp}}\frac{\sqrt{A_SB_SA_OB_O}}{\sqrt{a_Sb_Sa_Ob_O}}
\mathbf 1_{a_Sb_Sa_Ob_O< A_SB_SA_OB_O/D_0^2}
\ll B^{1+o(1)}D_0^{-\sigma}
\]
for some `sigma>0`.

```text
STAGE15_6_SUBSTAGE=6cl
STAGE15_6CL_COMPLEMENTARY_VOLUME_SHRINK=D0^-2
STAGE15_6CL_WEIGHTED_COUNT_DECAY_PROVED=false
STAGE15_6CL_MARKOV_ROUTE=BLOCKED
STAGE15_6CL_REQUIRED_INPUT=PHYSICAL_RECIPROCAL_COMPLEMENTARY_PRODUCT_AVERAGE
STAGE15_6CL_EXIT=COUPLED_OPTIMIZATION_RECOMPUTE_READY
```