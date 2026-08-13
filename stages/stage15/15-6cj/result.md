# Stage15-6cj — coupled D0 optimization audit

Base: Stage15-6ci. Main-batch work unit 3.

The repaired receiver is one coupled optimization problem:
\[
\mathcal M(B)=\mathcal M_{\le D_0}(B)+\mathcal M_{>D_0}(B).
\]
Stage15-6ch certifies the small-range profile
\[
\mathcal M_{\le D_0}(B)\ll B(\log B)^5(\log D_0)^2+B(\log B)^{9/2+\varepsilon}D_0^{13+\varepsilon}.
\]
Stage15-6ci leaves the large-range inverse-`D0` decay open.

Consequently no polynomial optimization `D0=B^theta` is currently legal: the certified small-range error would already be polynomially larger than `B`. Restricting `D0` to the certified polylogarithmic window keeps the small range at `B^{1+o(1)}`, but then even a hypothetical `D0^{-sigma}` gain in the large range produces only logarithmic saving, not a new fixed-power exponent.

Therefore the two receivers should **not** be split yet. The bottleneck is coupled: before optimization can generate a polynomial saving, the small-range physical root-line estimate itself must acquire a polynomial modulus window (or a substantially softer level dependence), and the large complementary average must acquire inverse-`D0` decay. These are coupled by the same threshold.

Candidate ledger update:
- small-range polynomial modulus window: LIVE;
- large-range inverse-`D0` complementary average: LIVE;
- immediate split: BLOCKED pending a legal polynomial overlap window;
- current Huang/polylog window: DOMINATED for fixed-power optimization but retained as a valid local estimate.

```text
STAGE15_6_SUBSTAGE=6cj
STAGE15_6CJ_COUPLED_OPTIMIZATION_AUDITED=true
STAGE15_6CJ_POLYNOMIAL_D0_OPTIMIZATION_LEGAL=false
STAGE15_6CJ_SPLIT_TRIGGER=false
STAGE15_6CJ_SMALL_POLYNOMIAL_WINDOW_NEEDED=true
STAGE15_6CJ_LARGE_INVERSE_D0_DECAY_NEEDED=true
STAGE15_6CJ_AUDIT_REQUIRED=true
STAGE15_6CJ_CODEX_REQUIRED=false
STAGE15_6CJ_MERGE_ALLOWED=false
STAGE15_6CJ_EXIT=FRESH_AUDIT_OF_COUPLED_POLYNOMIAL_WINDOW_GATE
```