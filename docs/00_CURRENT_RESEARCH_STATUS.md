# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage25-reentry-30-AUDITED-PASS-AWAITING-MERGE-AND-BACKFLOW
STAGE12_STATUS=FROZEN_R09
STAGE13_STATUS=CLOSED_R07
STAGE14_STATUS=CLOSED_R06
STAGE15_STATUS=CLOSED_R02_REVIEW_FROZEN
STAGE16_STATUS=CLOSED_R01_AUDIT_PASS
STAGE16S_STATUS=CLOSED_R01_AUDIT_PASS
STAGE17_STATUS=CLOSED_R01_AUDIT_PASS
STAGE18_STATUS=CLOSED_R01_AUDIT_PASS
STAGE19_STATUS=CLOSED_R01_AUDIT_PASS_WITH_POST_STAGE25_DIRECTIONAL_SUPERSESSION
STAGE20_STATUS=CLOSED_R01_AUDIT_PASS
STAGE21_STATUS=CLOSED_AUDIT_PASS_MERGED_PR950
STAGE22_STATUS=CLOSED_AUDIT_PASS_MERGED_PR957
STAGE23_STATUS=CLOSED_AUDIT_PASS_MERGED_PR966_WITH_DIRECTIONAL_BACKFLOW
STAGE24_STATUS=CLOSED_AUDIT_PASS_MERGED_PR979_WITH_DIRECTIONAL_BACKFLOW
STAGE25_STATUS=CLOSED_R01_AUDIT_PASS
STAGE25_REENTRY_PHASE10_STATUS=AUDITED_PASS_MERGED
STAGE25_REENTRY_PHASE20_STATUS=AUDITED_PASS_MERGED
STAGE25_REENTRY_R008A_STATUS=AUDITED_PASS_MERGED_PR1004
STAGE25_REENTRY_CURRENT_PHASE=30
STAGE25_REENTRY_PHASE30_TASK=Stage25-u23-r003a
STAGE25_REENTRY_PHASE30_STATUS=AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW
STAGE25_REENTRY_PHASE30_RESULT=stages/stage25/25-reentry-30/result.md
STAGE25_REENTRY_QUEUED_ROUTE=Stage25-um-r009a
STAGE25_REENTRY_PHASE40_ALLOWED=false
STAGE26_ALLOWED=false
NEXT_EXPECTED_COMMAND=merge PR #1005; then Stage25-reentry-main-batch
NEXT_RESEARCH_PROGRAM=docs/stage25-reentry-roadmap.md
```

## Current operation

Phase20 and its theorem-changing backflow r008a are hostile-audited and merged. The current strongest directional target interface is

`N2,j(B)>>_j B^(1/4)` for `j=a,b,c`.

Phase30 reattacks the Stage17 -> Stage19 transition at exact face-mask level. In the common canonical primitive integral-space host,

`N2,a=A_ab,ac-A3`,
`N2,b=A_ab,bc-A3`,
`N2,c=A_ac,bc-A3`,

so the only raw-pair/exactly-two discrepancy is the common three-face term `A3`. Pairwise overlap contrasts cancel `A3` exactly.

Combining the directional lower with Stage17

`N1(B)~kappa/(24*pi) B(log B)^3`

gives the audited phase30 ratio theorem

`B^(-3/4)(log B)^(-3) <<_j N2,j/N1 <<_epsilon B^(-1/2+epsilon)(log B)^(-3) -> 0`

for every `j=a,b,c`.

The semantics are locked: `N1` is the exactly-one-face stratum and `N2,j` is an exactly-two-face stratum, so these sets are disjoint. `N2,j/N1` is a matched adjacent-stratum population-size ratio, **not** literal subset survival and not a density inside the set counted by `N1`.

No claim is made on the quarter-power size of `A3`, perfect-cuboid existence/nonexistence, the true global `N2` exponent, or a strict sub-half whole-family upper. The theorem-changing Stage17/23 receiver synchronization route `Stage25-um-r009a` is authorized by phase30 audit but remains blocked until PR #1005 merges.

```text
TASK_ID=Stage25-u23-r003a
EXACT_MASK_RECEIVER_IDENTITIES_PROVED=true
COMMON_TRIPLE_CONTAMINATION=A3
TRIPLE_FREE_PAIR_CONTRASTS=true
DIRECTIONAL_STAGE23_RATIO_SEMANTICS=ADJACENT_STRATUM_POPULATION_SIZE_NOT_LITERAL_SURVIVAL
LITERAL_N2J_SUBSET_OF_N1=false
GLOBAL_N2_EXPONENT_UPGRADED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
AUDIT_STATUS=PASS
ADVANCE_ALLOWED=true
QUEUED_DERIVED_ROUTE=Stage25-um-r009a
STAGE25_REENTRY_PHASE40_ALLOWED=false
STAGE26_ALLOWED=false
MERGE_ALLOWED=true
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=merge PR #1005; then Stage25-reentry-main-batch
```
