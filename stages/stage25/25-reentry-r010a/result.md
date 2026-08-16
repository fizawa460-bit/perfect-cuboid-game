# Stage25-reentry r010a — directional two-face / Stage20 receiver backflow

STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ROUTE_ID=Stage25-um-r010a
PARENT_TASK=Stage25-u22-r004a
PARENT_PR=1007
PARENT_MERGE_COMMIT=eebe4cd59caef804be76508f3773f2af6c7d47f2
AFFECTED_STAGES=18,20,22

## Accepted parent theorem

In the primitive canonical no-space host, let `P_j(B)` be the raw pair chamber with the two faces sharing canonical edge `j` integral, before the third-face mask is imposed. Phase40 hostile audit accepted, for `j=a,b,c`,

\[
P_j=M_{2,j}+M_3
\]

exactly. The frozen directional Stage18 theorem and Stage20 upper give

\[
M_{2,j}(B)\sim C_j B(\log B)^5,\qquad C_j>0,
\]

and, for every fixed `eta<1/46`,

\[
M_3(B)\ll_\eta B(\log B)^{5-\eta}.
\]

Therefore

\[
\frac{M_3(B)}{M_{2,j}(B)}\ll_{j,\eta}(\log B)^{-\eta}\to0,
\]

\[
P_j(B)\sim C_jB(\log B)^5,
\]

and the literal third-face nonsquare postfilter has

\[
\frac{M_{2,j}(B)}{P_j(B)}=1-O_{j,\eta}((\log B)^{-\eta})\to1.
\]

Using

\[
M_1(B)\sim\frac{3}{4\pi^2}B^2\log B,
\]

one also has the directional Stage22 transition

\[
\frac{M_{2,j}(B)}{M_1(B)}\sim
\frac{4\pi^2C_j}{3}\frac{(\log B)^4}{B}\to0.
\]

The exactly-two directional chambers partition `M2`, hence

\[
C_{M_2}=C_a+C_b+C_c,
\qquad
\frac{M_{2,j}(B)}{M_2(B)}\to\frac{C_j}{C_{M_2}}.
\]

## Fine-mechanism boundary retained

This synchronization narrows, but does not close, `G22_LOG4_FINE_MECHANISM`.

It proves the four-log compensation is:

- present in every canonical shared-edge chamber;
- not created by summing the three directional chambers;
- not created by the third-face nonsquare postfilter;
- not attributable to the common canonical/primitivity/cutoff interface.

The unresolved source is internal to the one-face versus shared-edge double-Pythagorean counting architecture (equivalently the rank-6 toric/shared-edge mechanism). No canonical decomposition into four independent arithmetic, valuation, squareclass, divisor, or local-probability factors is proved.

```text
THEOREM_REPROVED=false
THEOREM_CHANGING_RECEIVER_SYNC=true
EXACT_COMMON_M3_DECOMPOSITION_SYNCED=true
DIRECTIONAL_POSTFILTER_TO_ONE_SYNCED=true
DIRECTIONAL_STAGE22_CONSTANTS_SYNCED=true
LOG4_DIRECTIONAL_ROBUSTNESS_SYNCED=true
G22_LOG4_FINE_MECHANISM=OPEN_NARROWED_TO_SHARED_EDGE_TORIC_INTERNAL_MECHANISM
FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
GLOBAL_M2_THEOREM_UPGRADED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_REENTRY_PHASE=50
STAGE26_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-reentry-audit
```
