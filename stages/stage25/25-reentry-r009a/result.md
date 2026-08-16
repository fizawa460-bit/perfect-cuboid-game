# Stage25-reentry r009a — exact mask / adjacent-stratum backflow

STATUS=AUDITED_PASS_AWAITING_MERGE
ROUTE_ID=Stage25-um-r009a
PARENT_TASK=Stage25-u23-r003a
PARENT_PR=1005
PARENT_MERGE_COMMIT=daf84757c185df6973936d2970a6307ab0bff62b
AFFECTED_STAGES=17,23

Phase30 hostile audit accepted, in the common primitive canonical integral-space host,

\[
N_{2,a}=A_{ab,ac}-A_3,\qquad N_{2,b}=A_{ab,bc}-A_3,\qquad N_{2,c}=A_{ac,bc}-A_3,
\]

hence `N2=A_ab,ac+A_ab,bc+A_ac,bc-3*A3`; every pairwise raw-overlap contrast cancels the common `A3` term exactly.

Using the audited directional quarter-power lower bounds, Stage19 whole-family upper, and Stage17 `N1(B)~kappa/(24*pi)B(log B)^3`, for each `j=a,b,c`,

\[
B^{-3/4}(\log B)^{-3}\ll_j N_{2,j}(B)/N_1(B)\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}\to0.
\]

This is an adjacent-stratum population-size ratio. `N1` and `N2,j` are disjoint exactly-one/exactly-two strata; it is not literal subset survival or density inside `N1`.

Stage17 receives the exact mask bridge only as an auxiliary interface; its frozen `N1` theorem is unchanged. Stage23 receives the exact directional mask identities and adjacent-stratum ratio bounds. No quarter-power bound on `A3` and no perfect-cuboid conclusion is inferred.

```text
THEOREM_REPROVED=false
THEOREM_CHANGING_RECEIVER_SYNC=true
EXACT_MASK_RECEIVER_SYNCED=true
DIRECTIONAL_ADJACENT_STRATUM_RATIO_SYNCED=true
LITERAL_SURVIVAL_INTERPRETATION=false
A3_QUARTER_POWER_CONTROL=false
GLOBAL_N2_EXPONENT_UPGRADED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PASS
ADVANCE_ALLOWED=true
MERGE_ALLOWED=true
NEXT_REENTRY_PHASE=40
PHASE40_ALLOWED_BEFORE_MERGE=false
STAGE26_ALLOWED=false
NEXT_EXPECTED_COMMAND=merge PR #1006; then Stage25-reentry-main-batch
```
