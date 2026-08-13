# Stage15-6cr — primitive-normalized reciprocal complementary-product audit

Base: Stage15-6cq. Main-batch work unit 2.

The repaired large-range receiver carries weight
\[
\frac{\sqrt{A_SB_SA_OB_O}}{\sqrt{a_Sb_Sa_Ob_O}},
\qquad
A_SB_SA_OB_O=|m^4-n^4|\,|r^4-s^4|.
\]
Stage15-6co already rules out raw-height pointwise domination. Reinsert the exact primitive normalization from 6aj:
\[
R=\frac{2}{\gamma}kN(z)N(w),\qquad \gamma\in\{2,4\},
\]
with raw gcd normalizer
\[
G=\gamma h_\alpha h_\beta.
\]
The unbalanced growth in the four-form numerator can therefore only be neutralized statistically through the same cross-gcd normalizer package; it is not a free pointwise consequence of `R<=B`.

A Rankin-type attempt was tested. For any `eta>0`,
\[
\mathbf 1_{de>D_0}\le (de/D_0)^\eta
\]
turns the exact weight into a higher positive moment `(de)^{1+eta}`, so without a pre-existing gcd moment it worsens the receiver and is BLOCKED. The complementary-product truncation is also one-sided: small `a_Sb_Sa_Ob_O` makes the reciprocal weight larger.

Thus a genuine `sigma>0` would follow from a normalized reciprocal moment of the form
\[
\sum_{P\in A(B)}
\sum_{\mathrm{comp}}
\left(
\frac{\sqrt{|m^4-n^4|\,|r^4-s^4|}}{G\sqrt{a_Sb_Sa_Ob_O}}
\right)^{1+\eta}
\ll B^{1+o(1)}
\]
for some fixed `eta>0`, together with the exact relation between the switched divisor product and the primitive normalizer. No such moment is currently certified.

The large-side theorem species is therefore narrowed to a **cross-gcd-normalized reciprocal complementary moment**. This is strictly stronger and more physical than the raw reciprocal average of 6cl, but `sigma>0` remains unproved.

```text
STAGE15_6_SUBSTAGE=6cr
STAGE15_6CR_PRIMITIVE_NORMALIZER_REINSERTED=true
STAGE15_6CR_RAW_GCD_NORMALIZER=gamma*h_alpha*h_beta
STAGE15_6CR_RANKIN_WITHOUT_MOMENT=BLOCKED
STAGE15_6CR_RECIPROCAL_TRUNCATION_ALONE_DECAYS=false
STAGE15_6CR_SIGMA_PROVED=false
STAGE15_6CR_LARGE_GATE=CROSS_GCD_NORMALIZED_RECIPROCAL_COMPLEMENTARY_MOMENT
STAGE15_6CR_EXIT=DELTA_SIGMA_LEDGER_RECOMPUTE_READY
```