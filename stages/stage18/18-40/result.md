# Stage18-40 — upper-bound ledger

Status: **SUBMITTED_FOR_FRESH_AUDIT**

The frozen Stage15 asymptotic on the exact Stage18 population is
\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]
Hence
\[
\boxed{M_2(B)\ll B(\log B)^5}.
\]
This upper bound is order-sharp at the current resolution because the same positive asymptotic supplies a matching lower bound.

No stronger polynomial upper exponent is asserted. Finite Stage18-20 data are not used as proof.

```text
UPPER_BOUND=M_2(B) << B(log B)^5
ORDER_SHARP=true
SOURCE=FROZEN_STAGE15_ASYMPTOTIC
NEW_ANALYTIC_INPUT=false
FINITE_DATA_USED_AS_PROOF=false
CODEX_REQUIRED=false
AUDIT_REQUIRED=true
```
