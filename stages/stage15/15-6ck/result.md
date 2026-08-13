# Stage15-6ck — small-range polynomial-window audit

Base: merged Stage15-6ch-cj with audit PASS. Main-batch work unit 1.

The certified fixed/moderate-level profile currently contributes an error with neighbourhood/modulus complexity `(de)^(10+eps)`. Keeping exact `phi(d)phi(e)` weights does not by itself soften that level exponent: grouping by `n=de`,
\[
\sum_{de\le D_0}\varphi(d)\varphi(e)(de)^{10+\varepsilon}
=\sum_{n\le D_0}n^{10+\varepsilon}\sum_{de=n}\varphi(d)\varphi(e).
\]
The inner convolution is multiplicative and satisfies only divisor-type growth `\ll n^{1+o(1)}` from the present information, so the total is `\ll D_0^{12+o(1)}` to `D_0^{13+o(1)}` depending on the chosen safe envelope; this does not create a genuine polynomial modulus window.

A materially softer small-range route would therefore have to improve the *per-modulus physical root-line error* itself, not merely the phi-weight summation. No existing Stage14 Arsenal result supplies such a whole-family physical estimate: t76 is fixed-packet spacing, while Huang's effective toric error has the same polynomial level-complexity obstruction already certified in 6bp/6bq.

Thus the small side remains LIVE, with the exact required theorem species narrowed to a physical root-line estimate uniform for `de<=B^theta` whose error has effective level exponent small enough to keep the summed error at `B^(1+o(1))`.

```text
STAGE15_6_SUBSTAGE=6ck
STAGE15_6CK_EXACT_PHI_RESUMMATION_TESTED=true
STAGE15_6CK_PHI_RESUMMATION_ALONE_SOFTENS_LEVEL=false
STAGE15_6CK_POLYNOMIAL_WINDOW_PROVED=false
STAGE15_6CK_REQUIRED_INPUT=SOFTER_PER_MODULUS_PHYSICAL_ROOT_LINE_ERROR
STAGE15_6CK_EXIT=LARGE_COMPLEMENTARY_DECAY_TEST_READY
```