# Stage15-6cv — large-side transversality test and coupled recomputation

Base: Stage15-6cu. Main-batch work unit 3.

For the large switched receiver, `q=de` divides the channel-gcd majorant `G_SG_O`, whereas Stage15-6ct proves `gcd(q,H)=1`. Therefore the primitive normalizer `G=gamma H` cannot itself absorb any unbounded odd part of `q`. A `D0^{-sigma}` gain cannot be manufactured by assigning large switched modulus to a large common normalizer.

The independence is concrete already at the channel-gcd level. For
\[
(m,n,r,s)=(77,36,71,65)
\]
all four cross gcds are one, so `H=1`, while
\[
G_S=\gcd(77^2+36^2,71^2-65^2)=17,
\]
\[
G_O=\gcd(77^2-36^2,71^2+65^2)=4633,
\]
and `G_SG_O=78761`. This example is used only to refute a pointwise control of the channel-gcd majorant by `H`; it is **not** asserted to be a Stage15 exact survivor or to have actual core `q=78761`.

Thus:
- `sigma>0` from primitive-normalizer size/correlation alone: **DISPROVED as a mechanism**;
- `sigma>0` for the exact large survivor receiver: still **LIVE**, requiring arithmetic distribution of the complementary residual channel forms under `HMNUV<=B` and `gcd(q,H)=1`.

The two open exponents have therefore not split into independent analytic worlds. Both now require the same refined object: S/O residual channel arithmetic on the cross-gcd-cell product-height hyperbola, with modulus transverse to `H`.

Ledger recomputation:
- conditional `beta=-1` is preserved;
- certified `delta>0`: no;
- certified `sigma>0`: no;
- executable `theta` window: none;
- split remains disabled.

The next main task should formulate/count the residual channel forms after substituting
\[
m=abM,\ n=cdN,\ r=acU,\ s=bdV,
\]
with pairwise-coprime `a,b,c,d`, `HMNUV<=B`, and `(q,H)=1`, rather than continue searching for savings from `H` itself.

```text
STAGE15_6_SUBSTAGE=6cv
STAGE15_6CV_NORMALIZER_ONLY_SIGMA=false
STAGE15_6CV_FULL_SURVIVOR_SIGMA_PROVED=false
STAGE15_6CV_CONDITIONAL_BETA=-1
STAGE15_6CV_DELTA_PROVED=false
STAGE15_6CV_SIGMA_PROVED=false
STAGE15_6CV_EXECUTABLE_OVERLAP_WINDOW=false
STAGE15_6CV_SPLIT_TRIGGER=false
STAGE15_6CV_AUDIT_REQUIRED=true
STAGE15_6CV_CODEX_REQUIRED=false
STAGE15_6CV_MERGE_ALLOWED=false
STAGE15_6CV_EXIT=FRESH_AUDIT_OF_RESIDUAL_CHANNEL_ARITHMETIC_GATE
```