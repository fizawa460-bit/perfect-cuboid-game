# Stage15-6ce — pointwise structural domination audit

Base: merged Stage15-6cd with fresh audit PASS. Main-batch work unit 1.

We test the preserved UNTESTED route: dominate `G_S G_O` pointwise by an already charged physical variable strongly enough to make the first moment automatic.

With
\[
G_S=\gcd(m^2+n^2,r^2-s^2),\qquad G_O=\gcd(m^2-n^2,r^2+s^2),
\]
the elementary bounds
\[
G_SG_O\le (m^2+n^2)(r^2+s^2)
\]
and the symmetric alternatives are valid but too large relative to primitive physical height after the moving gcd normalizer. No identity discovered in the current normal form gives `G_S G_O <= B^o(1)` or a domination by a once-charged variable whose first moment is already certified.

Hence the preserved pointwise route is now tested and BLOCKED for the current normal form; this closes the UNTESTED ledger entry rather than silently dropping it.

```text
STAGE15_6_SUBSTAGE=6ce
STAGE15_6CE_POINTWISE_STRUCTURAL_DOMINATION_TESTED=true
STAGE15_6CE_POINTWISE_STRUCTURAL_DOMINATION_PROVED=false
STAGE15_6CE_POINTWISE_ROUTE_CLASS=BLOCKED_CURRENT_NORMAL_FORM
STAGE15_6CE_EXIT=PHYSICAL_DIVISOR_SWITCH_READY
```