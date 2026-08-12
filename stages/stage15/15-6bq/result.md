# Stage15-6bq — maximal Huang level certificate

Base: Stage15-6bp. Audit verdict: PASS (negative quantitative certificate).

Comparing main and error gives

\[
q^{12+o(1)} \ll (\log B)^{1/2},
\]

so the direct effective-equidistribution theorem certifies at most

\[
q\le (\log B)^{1/24-o(1)}.
\]

This range is logarithmic and cannot yield a causal fixed-power exponent by the 6bo low/high balance.

```text
STAGE15_6_SUBSTAGE=6bq
STAGE15_6BQ_AUDIT_VERDICT=PASS
STAGE15_6BQ_MAX_DIRECT_HUANG_LEVEL=log(B)^(1/24-o(1))
STAGE15_6BQ_FIXED_POWER_LEVEL_CERTIFIED=false
STAGE15_6BQ_EXIT=GEOMETRIC_SIEVE_LARGE_PRIME_AUDIT_READY
```
