# Stage18 post-Stage25-r010a receiver synchronization

STATUS=AUDITED_PASS_SYNCED_BY_STAGE25_REENTRY_70
HISTORICAL_STAGE18_PASS_REVOKED=false
SOURCE_ROUTE=Stage25-um-r010a
PARENT_TASK=Stage25-u22-r004a
PARENT_PR=1007
PARENT_MERGE_COMMIT=eebe4cd59caef804be76508f3773f2af6c7d47f2
BACKFLOW_PR=1008
BACKFLOW_MERGE_COMMIT=9d2e767697a33195e756af6b366cb6f0548494d3

Stage18's frozen global theorem remains unchanged:

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]

For each canonical shared-edge chamber `j=a,b,c`, let `P_j` be the raw two-successful-face chamber before excluding the third face. The audited phase40/r010a receiver gives

\[
P_j=M_{2,j}+M_3
\]

exactly and

\[
M_{2,j}(B)\sim C_jB(\log B)^5,\qquad C_j>0.
\]

The Stage20 log-saving upper makes the triple-face term lower order in every chamber:

\[
M_3/M_{2,j}\ll_{j,\eta}(\log B)^{-\eta}\to0
\quad(\eta<1/46).
\]

Hence

\[
P_j(B)\sim C_jB(\log B)^5,
\qquad
M_{2,j}(B)/P_j(B)\to1.
\]

Thus the exactly-two third-face nonsquare postfilter does not change the directional leading constant.

The r010a-era `G22_LOG4_FINE_MECHANISM` gate was subsequently superseded by audited r011a: it is now closed at the geometric Manin-invariant level only; independent local-factor / Dirichlet-pole factorization remains open.

```text
FROZEN_GLOBAL_M2_THEOREM_CHANGED=false
DIRECTIONAL_RAW_PAIR_ASYMPTOTIC_SYNCED=true
DIRECTIONAL_THIRD_FACE_POSTFILTER_TO_ONE=true
THIRD_FACE_EXCLUSION_LEADING_CAUSE=false
G22_LOG4_FINE_MECHANISM=CLOSED_AT_GEOMETRIC_INVARIANT_LEVEL
FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false
COMMON_DIRICHLET_POLE_SLOT_LEDGER_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
BACKFLOW_ROUTE=Stage25-um-r010a
BACKFLOW_AUDIT_STATUS=PASS
BACKFLOW_SYNCHRONIZED=true
```
