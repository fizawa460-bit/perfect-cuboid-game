# Stage23 post-Stage25-r009a — exact mask and directional adjacent-stratum receiver

STATUS=SUBMITTED_BACKFLOW_R009A_PENDING_FRESH_AUDIT
HISTORICAL_STAGE23_PASS_REVOKED=false
SOURCE_ROUTE=Stage25-um-r009a
PARENT_TASK=Stage25-u23-r003a
PARENT_PR=1005
PARENT_MERGE_COMMIT=daf84757c185df6973936d2970a6307ab0bff62b

For canonical `0<a<b<c`, define directional exactly-two counts by shared edge. The accepted phase30 truth table gives

\[
\boxed{N_{2,a}=A_{ab,ac}-A_3},\qquad
\boxed{N_{2,b}=A_{ab,bc}-A_3},\qquad
\boxed{N_{2,c}=A_{ac,bc}-A_3}.
\]

Therefore

\[
\boxed{N_2=A_{ab,ac}+A_{ab,bc}+A_{ac,bc}-3A_3}.
\]

The common contamination cancels in every pairwise contrast, e.g.

\[
A_{ab,ac}-A_{ab,bc}=N_{2,a}-N_{2,b},
\]

and cyclically. No assumption on whether `A3` eventually vanishes or is nonzero is needed.

The audited all-direction lower bound and Stage19 whole-family upper imply, using Stage17 `N1(B)~kappa/(24*pi) B(log B)^3`, for every `j=a,b,c`,

\[
\boxed{B^{-3/4}(\log B)^{-3}\ll_j N_{2,j}(B)/N_1(B)}
\]

and

\[
\boxed{N_{2,j}(B)/N_1(B)\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}\to0}.
\]

The numerator and denominator are adjacent disjoint strata: exactly two faces versus exactly one face. This is a matched population-size comparison, not a literal survival probability and not a density inside `N1`.

```text
EXACT_DIRECTIONAL_MASK_IDENTITIES=true
COMMON_A3_CONTAMINATION_ISOLATED=true
PAIR_CONTRASTS_A3_FREE=true
DIRECTIONAL_ADJACENT_STRATUM_RATIO_TO_ZERO=true
LITERAL_SURVIVAL_INTERPRETATION=false
A3_QUARTER_POWER_CONTROL=false
GLOBAL_N2_EXPONENT_UPGRADED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
BACKFLOW_ROUTE=Stage25-um-r009a
BACKFLOW_AUDIT_STATUS=PENDING
```
