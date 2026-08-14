# Stage23-30 — asymptotic upper thinning and priority-driven attack repair

EVIDENCE_LEVEL=PROVED
CHECKPOINT=30
STATUS=PROVED_AUDITED_PASS_WITH_LATER_SUPERSESSION_ADDENDUM

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

At checkpoint30 the integer investigation stopped at the finite diagnostic scan `1<=t<10^6`, `t=1 mod 14`, with zero hits. That statement was not mathematically false, but the attack depth was retrospectively incomplete.

## Later supersession / addendum from checkpoint40

Checkpoint40 subsequently proves, directly from the same checkpoint30 equation, that for every integer `t`,

\[
(t^2+1)(t^2+2t+2)\equiv2\pmod8.
\]

Since square residues modulo 8 are only `0,1,4`, the integer pullback is globally empty:

\[
\boxed{\text{no integer }t\text{ satisfies }w^2=(t^2+1)(t^2+2t+2).}
\]

Therefore the checkpoint30 finite-scan line is superseded by a proof-level global exclusion. The checkpoint30 PASS is not withdrawn: its mathematics was correct, but the later stronger result must be read as the canonical status of this slice.

```text
STAGE30_MATHEMATICS_FALSE=false
STAGE30_ATTACK_DEPTH_RETROSPECTIVELY_INCOMPLETE=true
STAGE30_SUPERSEDED_SLICE_STATUS=GLOBAL_INTEGER_EXCLUSION_BY_MOD8
FINITE_SCAN_CANONICAL_STATUS=SUPERSEDED_BY_PROOF
Q03_FALSE_CLAIM_ORIGIN=CHECKPOINT40_ONLY
```

The audit repair does not reopen the zero-density theorem. It integrates the Stage14/15 deep-review attack ledger and fixes a compatibility-driven attack queue in `stages/stage23/23-30/attack-priority-ledger.md`.

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
Q03_ROLE=genus-one slice attack; later globally excluded over integer t by mod 8 at checkpoint40
Q03_INFINITE_STAGE19_FAMILY_PROVED=false

NEXT_P1_RESERVES=Q04,Q11
P2_HOLD=Q05
P3_NO_REATTACK=Q07,Q08,Q09,Q10
```

Q06 is not rejected merely because the inherited `B^(1/2+epsilon)` ceiling already exists. It stays active until the physical-height transfer and Kummer point-count support either produce a stronger bound or are shown not to improve the literal Stage19 count at the current input resolution.

```text
STAGE14_15_ATTACK_LEDGER_INTEGRATED=true
ATTACK_IDS_ACCEPTED_REJECTED_RECORDED=true
DEEP_REVIEW_QUEUE_CHECK=PASS
ZERO_DENSITY_MATHEMATICS_REOPENED=false
STAGE30_SUPERSESSION_ADDENDUM_MATERIALIZED=true
AUDIT_REQUIRED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT_AFTER_PASS=40
CODEX_REQUIRED=false
```
