# Stage25-reentry phase30 hostile audit

Status: **PASS; EXACT MASK IDENTITIES ACCEPTED; ADJACENT-STRATUM SEMANTICS LOCKED**

TASK_ID=Stage25-u23-r003a
REENTRY_PHASE=30
PR=1005

## Verdict

The phase30 mathematical strengthening is accepted.

Inside the common primitive canonical integral-space host

`U(B)={0<a<b<c, gcd(a,b,c)=1, a^2+b^2+c^2=d^2, d<=B}`,

Stage13 defines the raw pair overlaps by products of the three face-square indicators and defines `A3` by their triple product. Therefore the truth table gives exactly

`N2,a=A_ab,ac-A3`,
`N2,b=A_ab,bc-A3`,
`N2,c=A_ac,bc-A3`,

and hence

`N2=A_ab,ac+A_ab,bc+A_ac,bc-3*A3`.

The three pair-overlap contrasts cancel the common `A3` term identically. No assumption on the existence or nonexistence of a perfect cuboid enters these identities.

The directional normalization is also accepted. From the audited phase20/r008a lower `N2,j(B)>>_j B^(1/4)`, the audited Stage17 law `N1(B)~kappa/(24*pi) B(log B)^3`, and `N2,j<=N2<<_epsilon B^(1/2+epsilon)`, one obtains for each `j=a,b,c`

`B^(-3/4)(log B)^(-3) <<_j N2,j(B)/N1(B) <<_epsilon B^(-1/2+epsilon)(log B)^(-3) -> 0`.

## Required semantic firewall

Stage17 `N1` is the **exactly-one-face** stratum and `N2,j` lies in the **exactly-two-face** stratum. These populations are disjoint. Therefore `N2,j/N1` is a matched adjacent-stratum population-size ratio, not a literal subset survival probability and not a density *inside* the set counted by `N1`.

The submission's phrases `Directional Stage23 survival`, `zero-density inside the Stage17 source population`, and `normalized second-face survival` are accepted only after being rewritten to adjacent-stratum language. The numerical ratio theorem is unchanged.

## Scope firewall

Accepted:
- exact common-`A3` mask receiver identities;
- exact triple-free pair-overlap contrasts;
- all-direction adjacent-stratum ratio bounds and limit zero;
- every directional Stage19 target chamber is unbounded/positive-power.

Not accepted or claimed:
- `N2,j` is a subset of `N1`;
- objectwise survival probability from Stage17 to Stage19;
- quarter-power control of `A3`;
- a perfect-cuboid existence or nonexistence conclusion;
- an improved global `N2` exponent;
- a strict whole-family sub-half upper;
- independence of the raw overlaps.

The theorem-changing receiver route `Stage25-um-r009a` is authorized by this audit but remains blocked until PR #1005 is merged. Phase40 remains blocked until r009a is synchronized and freshly audited/merged under the reentry propagation policy.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
TASK_ID=Stage25-u23-r003a
CURRENT_REENTRY_PHASE=30
PHASE30_STATUS=AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW
EXACT_MASK_RECEIVER_IDENTITIES_ACCEPTED=true
TRIPLE_FREE_PAIR_CONTRASTS_ACCEPTED=true
DIRECTIONAL_ADJACENT_STRATUM_RATIO_ACCEPTED=true
LITERAL_N2J_SUBSET_OF_N1=false
LITERAL_SURVIVAL_INTERPRETATION=false
A3_QUARTER_POWER_CONTROL_PROVED=false
ADVANCE_ALLOWED=true
NEXT_REENTRY_PHASE=30
TARGET_PHASE_AFTER_BACKFLOW=40
QUEUED_PROPAGATION_PROPOSALS=Stage25-um-r009a
MERGE_ALLOWED=true
STAGE26_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #1005; then Stage25-reentry-main-batch
```
