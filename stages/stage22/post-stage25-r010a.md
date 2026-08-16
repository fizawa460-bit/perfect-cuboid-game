# Stage22 post-Stage25-r010a — directional transition receiver

STATUS=AUDITED_PASS_SYNCED_BY_STAGE25_REENTRY_70
HISTORICAL_STAGE22_PASS_REVOKED=false
SOURCE_ROUTE=Stage25-um-r010a
PARENT_TASK=Stage25-u22-r004a
PARENT_PR=1007
PARENT_MERGE_COMMIT=eebe4cd59caef804be76508f3773f2af6c7d47f2
BACKFLOW_PR=1008
BACKFLOW_MERGE_COMMIT=9d2e767697a33195e756af6b366cb6f0548494d3

Stage22's frozen global transition remains

\[
\frac{M_2(B)}{M_1(B)}\sim
\frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B}.
\]

The audited phase40/r010a receiver strengthens this directionally. For every shared edge `j=a,b,c`,

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

## Current fine-mechanism status

At r010a this mechanism was still open. Audited r011a subsequently closes it at the geometric Manin-invariant level:

\[
M_1:(a,b)=(2,2),\qquad N_1:(a,b)=(1,4),\qquad M_2:(a,b)=(1,6),
\]

so the Stage22 logarithmic enhancement is the rational `b`-invariant jump `6-2=4`, with additive geometric decomposition `(4-2)+(6-4)=2+2`.

The finer arithmetic factorization remains open: no four independent probabilities, named Dirichlet pole slots, valuation factors, or squareclass factors are proved.

```text
FROZEN_GLOBAL_STAGE22_THEOREM_CHANGED=false
DIRECTIONAL_STAGE22_CONSTANTS_SYNCED=true
G22_LOG4_FINE_MECHANISM=CLOSED_AT_GEOMETRIC_INVARIANT_LEVEL
FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false
COMMON_DIRICHLET_POLE_SLOT_LEDGER_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
BACKFLOW_ROUTE=Stage25-um-r010a
BACKFLOW_AUDIT_STATUS=PASS
BACKFLOW_SYNCHRONIZED=true
```
