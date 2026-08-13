# Stage15-6cp — coupled polynomial overlap recomputation

Base: Stage15-6co. Main-batch work unit 3.

The coupled receiver remains
\[
\mathcal M(B)=\mathcal M_{\le D_0}(B)+\mathcal M_{>D_0}(B).
\]
Stage15-6cn shows that a prospective softer small-range theorem
\[
N_{d,e}(B)\ll B^{1+o(1)}q^{-2}+B^{1-\delta+o(1)}q^\beta,
\qquad q=de,
\]
would yield, after exact phi summation,
\[
\mathcal M_{\le D_0}(B)
\ll B^{1+o(1)}+B^{1-\delta+o(1)}D_0^{\beta+2}.
\]
Stage15-6co keeps the prospective large profile
\[
\mathcal M_{>D_0}(B)\ll B^{1+o(1)}D_0^{-\sigma}
\]
with `sigma>0`, but proves that it cannot come from a raw-height pointwise domination.

For a polynomial threshold `D0=B^theta`, the small error is harmless exactly when
\[
0<\theta<\frac{\delta}{\beta+2},
\]
and any such positive `theta` would make the large profile power-saving if `sigma>0`. Thus the two theorem species do have a mathematically nonempty overlap window **conditional on both quantitative improvements**, but neither improvement is presently proved.

This clarifies the controller status: the receivers remain coupled through `theta`; split eligibility is not yet triggered because neither side has an independently certified quantitative theorem to execute. The next useful work must improve one of the two exact profiles rather than reparameterize the same obstruction.

Candidate ledger update:
- physical root-line theorem with `delta>0`: LIVE;
- primitive-normalized reciprocal complementary average with `sigma>0`: LIVE;
- elementary lattice error at ambient-B scale: BLOCKED for polynomial window;
- raw-height pointwise domination of four-form numerator: BLOCKED by explicit scaling family;
- immediate split: BLOCKED until one quantitative side is certified.

```text
STAGE15_6_SUBSTAGE=6cp
STAGE15_6CP_COUPLED_OPTIMIZATION_RECOMPUTED=true
STAGE15_6CP_CONDITIONAL_OVERLAP_WINDOW=0<theta<delta/(beta+2)
STAGE15_6CP_SMALL_IMPROVEMENT_PROVED=false
STAGE15_6CP_LARGE_IMPROVEMENT_PROVED=false
STAGE15_6CP_POLYNOMIAL_OVERLAP_WINDOW_CERTIFIED=false
STAGE15_6CP_SPLIT_TRIGGER=false
STAGE15_6CP_AUDIT_REQUIRED=true
STAGE15_6CP_CODEX_REQUIRED=false
STAGE15_6CP_MERGE_ALLOWED=false
STAGE15_6CP_EXIT=FRESH_AUDIT_OF_QUANTIFIED_DELTA_SIGMA_GATE
```