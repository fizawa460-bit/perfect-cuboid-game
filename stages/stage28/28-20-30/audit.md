# Stage28-20/30 fresh audit

```text
AUDIT_VERDICT=PASS
AUDITED_PR=1275
CHECKPOINT20_AUDIT=PASS
CHECKPOINT30_AUDIT=PASS
NUM_REUSE_AUDIT=PASS
FINITE_COMMON_CUTOFF_PANEL_AUDIT=PASS
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
BRIDGE_RATIO_LOWER_AUDIT=PASS
BRIDGE_RATIO_UPPER_AUDIT=PASS
NON_SUBSET_SEMANTICS_AUDIT=PASS
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ADVANCE_TO_CHECKPOINT40=true
NEXT_CHECKPOINT=40
NEXT_EXPECTED_COMMAND=Stage28-main-batch
```

## Findings

Checkpoint20 correctly reuses exact matched finite counts only. The `N2` values `(25,62,116,255)` at `B=(10k,50k,200k,1m)` agree with the existing Stage27 exact finite ladder, while the `M3` values `(18,42,82,219)` agree with the audited Stage20 exact Euler census at the same Euclidean cutoffs. The resulting finite ratios are exact diagnostics only; the nonmonotone panel through `1m` is not promoted to an asymptotic ordering or limit.

Checkpoint30 correctly derives the lower bridge corridor by dividing the current Stage26 lower `M3(B)>>_epsilon B^(1/3-epsilon)` by the Stage27 upper `N2(B)<<_epsilon B^(1/2+epsilon)`. For every fixed `zeta>0` this yields

\[
M_3(B)/N_2(B)\gg_\zeta B^{-1/6-\zeta}.
\]

The upper corridor also passes. Stage26's audited common-host share satisfies `Phi20=o((log B)^(-delta))` for every fixed `0<delta<1/46`, while Stage27/Stage18 give `Sigma19>>B^(-3/4)(log B)^(-5)`. Therefore

\[
M_3(B)/N_2(B)=\Phi_{20}/\Sigma_{19}=o(B^{3/4}(\log B)^{5-\delta}).
\]

This is stronger than the corresponding coarse whole-family big-O division. The broad corridor does not resolve whether `M3/N2` tends to zero, remains bounded/oscillatory, or tends to infinity, so the submission correctly keeps the Stage19/Stage20 asymptotic ordering open.

The Stage28 checkpoint10 firewall is preserved: `M3/N2` is a matched population-size bridge ratio on the common `H_ge2=M2+M3` host, not an objectwise survival probability. No perfect-cuboid conclusion or point-exponent promotion is introduced.
