# Stage22 post-Stage25-r010a — directional transition receiver

STATUS=SUBMITTED_BACKFLOW_R010A_PENDING_FRESH_AUDIT
HISTORICAL_STAGE22_PASS_REVOKED=false
SOURCE_ROUTE=Stage25-um-r010a
PARENT_TASK=Stage25-u22-r004a
PARENT_PR=1007
PARENT_MERGE_COMMIT=eebe4cd59caef804be76508f3773f2af6c7d47f2

Stage22's frozen global transition remains

\[
\frac{M_2(B)}{M_1(B)}\sim
\frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B}.
\]

The phase40 receiver strengthens this directionally. For every shared edge `j=a,b,c`,

\[
\boxed{\frac{M_{2,j}(B)}{M_1(B)}\sim
\frac{4\pi^2C_j}{3}\frac{(\log B)^4}{B}\to0},
\qquad C_j>0.
\]

Also

\[
C_{M_2}=C_a+C_b+C_c,
\qquad
\frac{M_{2,j}}{M_2}\to\frac{C_j}{C_{M_2}}.
\]

Thus the four-log compensation is present independently of directional aggregation. Combining the exact raw-pair decomposition with the Stage20 log-saving upper also shows the third-face nonsquare postfilter is lower order in every directional chamber.

## Current fine-mechanism gate

`G22_LOG4_FINE_MECHANISM` remains open, but its live locus is narrowed:

```text
LOG4_DIRECTIONAL_ROBUSTNESS=true
LOG4_IS_DIRECTIONAL_AVERAGING_ARTIFACT=false
THIRD_FACE_EXCLUSION_IS_LOG4_CAUSE=false
COMMON_CANONICAL_PRIMITIVE_CUTOFF_INTERFACE_IS_NEW_LOG4_CAUSE=false
LIVE_FINE_MECHANISM_LOCUS=ONE_FACE_VS_SHARED_EDGE_DOUBLE_PYTHAGOREAN_RANK6_TORIC_INTERNAL_COUNTING
FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false
LOCAL_PROBABILITY_PRODUCT_PROVED=false
VALUATION_FACTORIZATION_PROVED=false
SQUARECLASS_FACTORIZATION_PROVED=false
G22_LOG4_FINE_MECHANISM=OPEN_NARROWED_TO_SHARED_EDGE_TORIC_INTERNAL_MECHANISM
```

This is the correct receiver for any later attempt to explain the four logarithms without double charging or fake independence.

```text
FROZEN_GLOBAL_STAGE22_THEOREM_CHANGED=false
DIRECTIONAL_STAGE22_CONSTANTS_SYNCED=true
FINE_MECHANISM_CLOSED=false
PERFECT_CUBOID_CONCLUSION=NONE
BACKFLOW_ROUTE=Stage25-um-r010a
BACKFLOW_AUDIT_STATUS=PENDING
```
