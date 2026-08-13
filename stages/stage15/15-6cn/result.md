# Stage15-6cn — small-range polynomial-window theorem target

Base: merged Stage15-6ck-cm with fresh audit PASS. Main-batch work unit 1.

For a fixed modulus pair `(d,e)` write `q=de`. The small-range first moment is
\[
\mathcal M_{\le D_0}(B)=\sum_{q\le D_0}\ \sum_{de=q}\varphi(d)\varphi(e)N_{d,e}(B).
\]
The exact convolution satisfies
\[
\sum_{de=q}\varphi(d)\varphi(e)\ll q^{1+o(1)}.
\]
Hence if a genuinely softer physical root-line theorem had the per-modulus form
\[
N_{d,e}(B)\ll \frac{B^{1+o(1)}}{q^2}+B^{1-\delta+o(1)}q^{\beta}
\]
uniformly for `q<=B^theta`, with fixed `delta>0`, then exact phi summation would give
\[
\mathcal M_{\le D_0}(B)
\ll B^{1+o(1)}+B^{1-\delta+o(1)}D_0^{\beta+2}.
\]
Therefore a polynomial threshold `D0=B^theta` is legal precisely in the window
\[
\theta(\beta+2)<\delta.
\]
This isolates the quantitative requirement on the small side: reducing the current level exponent alone is not enough unless the error also carries genuine `B^{-delta}` room. A boundary term of ambient size `B*q^beta` never yields a polynomial window after phi summation.

An elementary index-`q^2` lattice count was re-tested. It recovers the correct main local density, but the primitive physical region is not a fixed four-variable box after normalization; its boundary error is still of ambient `B` scale in the currently certified normal form. Thus no `delta>0` is proved by elementary geometry-of-numbers here.

```text
STAGE15_6_SUBSTAGE=6cn
STAGE15_6CN_SMALL_TARGET_PROFILE=B/q^2+B^(1-delta)*q^beta
STAGE15_6CN_POLYNOMIAL_WINDOW_CONDITION=theta*(beta+2)<delta
STAGE15_6CN_ELEMENTARY_LATTICE_DELTA_PROVED=false
STAGE15_6CN_SMALL_POLYNOMIAL_WINDOW_PROVED=false
STAGE15_6CN_EXIT=LARGE_RECIPROCAL_AVERAGE_TEST_READY
```