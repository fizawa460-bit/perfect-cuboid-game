# Stage15-6cs — quantified delta/beta/sigma recomputation

Base: Stage15-6cr. Main-batch work unit 3.

Stage15-6cq narrows the small side to a prospective profile
\[
N_{d,e}(B)
\ll B^{1+o(1)}q^{-2}+B^{1-\delta+o(1)}q^{-1},
\]
provided the physical one-sided fringe moment has exponent `delta>0`. Thus the exact ledger has the improved conditional value
\[
\beta=-1,
\]
and after exact `phi` summation the polynomial threshold condition becomes
\[
0<\theta<\delta.
\]

Stage15-6cr narrows the large side to a cross-gcd-normalized reciprocal complementary moment. If this yields
\[
\mathcal M_{>D_0}(B)\ll B^{1+o(1)}D_0^{-\sigma}
\]
with `sigma>0`, then any `D0=B^theta` with `0<theta<delta` gives a power-saving large tail `B^{1-\theta\sigma+o(1)}` while keeping the small-range boundary error harmless.

This is a meaningful quantitative improvement of the ledger: the required small-side modulus exponent is now conditionally `beta=-1`, so the overlap condition is no longer `theta<delta/(beta+2)` in an unknown `beta`; it is simply `theta<delta`.

However neither exponent is independently certified:
- `delta>0`: open physical one-sided dyadic fringe moment;
- `sigma>0`: open cross-gcd-normalized reciprocal complementary moment.

Accordingly there is still no executable overlap window and no legal split. The two theorem species remain coupled through the same primitive-normalizer geometry; a split before one side is proved would duplicate the same unresolved physical-measure input.

Candidate ledger:
- physical one-sided fringe moment with `delta>0`: LIVE;
- cross-gcd-normalized reciprocal complementary moment with `sigma>0`: LIVE;
- generic per-modulus level exponent search: DOMINATED by 6cq reduction;
- raw reciprocal/Rankin routes: BLOCKED;
- split: BLOCKED until one quantitative exponent is certified.

```text
STAGE15_6_SUBSTAGE=6cs
STAGE15_6CS_DELTA_BETA_SIGMA_LEDGER_UPDATED=true
STAGE15_6CS_CONDITIONAL_BETA=-1
STAGE15_6CS_CONDITIONAL_OVERLAP_WINDOW=0<theta<delta
STAGE15_6CS_DELTA_PROVED=false
STAGE15_6CS_SIGMA_PROVED=false
STAGE15_6CS_EXECUTABLE_OVERLAP_WINDOW=false
STAGE15_6CS_SPLIT_TRIGGER=false
STAGE15_6CS_AUDIT_REQUIRED=true
STAGE15_6CS_CODEX_REQUIRED=false
STAGE15_6CS_MERGE_ALLOWED=false
STAGE15_6CS_EXIT=FRESH_AUDIT_OF_COMMON_PRIMITIVE_NORMALIZER_MOMENT_GATE
```