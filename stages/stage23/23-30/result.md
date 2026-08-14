# Stage23-30 — asymptotic upper thinning and priority-driven attack repair

EVIDENCE_LEVEL=PROVED
CHECKPOINT=30
STATUS=REPAIR_SUBMITTED_FOR_FRESH_REAUDIT

The frozen ratio deduction remains unchanged:

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\qquad
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]
so
\[
\boxed{\frac{N_2(B)}{N_1(B)}\ll_\varepsilon\frac{B^{-1/2+\varepsilon}}{(\log B)^3}\to0}.
\]

This proves only zero density. It does not identify the true target exponent or ratio order.

Checkpoint20's fixed-`n` AR-039 attack remains frozen. Checkpoint30 independently materialized the consecutive-parameter Stage17 slice `m=n+1`, `n=t=1 mod 14`, producing the genus-1 degeneration

\[
\boxed{w^2=(t^2+1)(t^2+2t+2)}.
\]

The finite scan `1<=t<10^6`, `t=1 mod 14` found no hit; this is finite diagnostic evidence only.

The audit repair does not reopen either theorem. It integrates the Stage14/15 deep-review attack ledger and fixes a compatibility-driven attack queue in `stages/stage23/23-30/attack-priority-ledger.md`.

```text
ATTACK_SELECTION_POLICY=PRIORITY_DRIVEN
P1_BEFORE_P2=true
P3_REOPEN_REQUIRES_NEW_INPUT=true
SELECT_BY_STAGE23_COMPATIBILITY=true
UPPER_AND_LOWER_ATTACKS_BOTH_ALLOWED=true
ATTACK_HISTORY_DEDUP_REQUIRED=true
```

Checkpoint30-specific P1 selection is:

```text
CURRENT_UPPER_ATTACK=Q06
Q06_ROLE=(4,4) Kummer receiver + physical-height upper/support attack
Q06_EXPONENT_IMPROVEMENT_PROVED=false

CURRENT_LOWER_ATTACK=Q03
Q03_ROLE=elliptic/Selmer attack on the newly found genus-1 Stage17 slice
Q03_INFINITE_STAGE19_FAMILY_PROVED=false

NEXT_P1_RESERVES=Q04,Q11
P2_HOLD=Q05
P3_NO_REATTACK=Q07,Q08,Q09,Q10
```

Q06 is not rejected merely because the inherited `B^(1/2+epsilon)` ceiling already exists. It stays active until the physical-height transfer and Kummer point-count support either produce a stronger bound or are shown not to improve the literal Stage19 count at the current input resolution.

Q03 is activated in parallel because the new checkpoint30 slice is genuinely genus 1. Q04 is the next alternate-geometry receiver; Q11 is the next local-sieve upper weapon if sufficient uniformity becomes available. Q05 remains external-input gated. Q07-Q10 are not re-attacked without new equations, height control, or average-theorem input.

```text
STAGE14_15_ATTACK_LEDGER_INTEGRATED=true
ATTACK_IDS_ACCEPTED_REJECTED_RECORDED=true
DEEP_REVIEW_QUEUE_CHECK=PASS
ZERO_DENSITY_MATHEMATICS_REOPENED=false
FRESH_ATTACK_REOPENED=false
REPAIR_SCOPE=STAGE14_15_ATTACK_LEDGER_INTEGRATION_AND_PRIORITY_QUEUE_ONLY
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=40
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
