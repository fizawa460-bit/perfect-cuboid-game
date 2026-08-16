# Stage25-reentry phase30 — Stage23 second-face receiver reattack

TASK_ID=Stage25-u23-r003a
REENTRY_PHASE=30
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARENT_BACKFLOW=Stage25-um-r008a
PARENT_BACKFLOW_PR=1004
PARENT_BACKFLOW_MERGE=11075adf8e30c73e5058790ee6ed6e2a9b6c9e2b

## Main candidate

Work in the canonical primitive integral-space host

`U(B)={0<a<b<c, gcd(a,b,c)=1, a^2+b^2+c^2=d^2, d<=B}`.

Let `A_ab,ac`, `A_ab,bc`, `A_ac,bc` be the Stage13 raw pair-overlap counts and `A3` the raw three-face overlap. Let `N2,a`, `N2,b`, `N2,c` be exactly-two-face integral-space objects classified by their canonical shared edge.

The face masks give the exact identities

`N2,a = A_ab,ac - A3`,
`N2,b = A_ab,bc - A3`,
`N2,c = A_ac,bc - A3`.

Hence, writing `P2=A_ab,ac+A_ab,bc+A_ac,bc`,

`N2 = P2 - 3*A3`.

The three contrast identities are triple-free:

`A_ab,ac-A_ab,bc = N2,a-N2,b`,
`A_ab,ac-A_ac,bc = N2,a-N2,c`,
`A_ab,bc-A_ac,bc = N2,b-N2,c`.

Thus the only obstruction to converting an individual raw pair overlap into its exactly-two receiver is the same common three-face term `A3`. No assumption on existence or nonexistence of perfect cuboids is used.

## Directional Stage23 survival

Audited phase20 plus audited r008a gives

`N2,j(B) >>_j B^(1/4)` for `j=a,b,c`.

Audited Stage17 gives

`N1(B) ~ kappa/(24*pi) * B(log B)^3`, with positive constant.

The whole-family Stage19 upper gives `N2,j<=N2<<_epsilon B^(1/2+epsilon)`.
Therefore, for every shared-edge chamber,

`B^(-3/4)(log B)^(-3) <<_j N2,j(B)/N1(B)`
`N2,j(B)/N1(B) <<_epsilon B^(-1/2+epsilon)(log B)^(-3) -> 0`.

Consequently each of the three second-face channels is individually infinite/positive-power but zero-density inside the Stage17 source population.

## Boundary

This does not prove a perfect cuboid exists or does not exist. It does not bound `A3` on the quarter-power scale, identify the true `N2` exponent, prove a strict whole-family sub-half upper, or promote raw pair-overlap ratios to independent probabilities.

A future asymptotic for any two pair overlaps can be compared directionally without controlling `A3`, because the common triple term cancels in pairwise contrasts.

```text
EXACT_MASK_RECEIVER_IDENTITIES_PROVED_CANDIDATE=true
COMMON_TRIPLE_CONTAMINATION=A3
TRIPLE_FREE_PAIR_CONTRASTS=true
DIRECTIONAL_STAGE23_LOWER=N2,j/N1>>_j B^(-3/4)(log B)^(-3)
DIRECTIONAL_STAGE23_UPPER=N2,j/N1<<_epsilon B^(-1/2+epsilon)(log B)^(-3)
DIRECTIONAL_STAGE23_RATIO_LIMIT=0
ALL_THREE_TARGET_CHAMBERS_UNBOUNDED=true
GLOBAL_N2_EXPONENT_UPGRADED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
STAGE26_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-reentry-audit
```
