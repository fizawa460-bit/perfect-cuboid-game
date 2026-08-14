# Stage23-30 — priority-driven attack selection ledger

Status: **REPAIR ARTIFACT**

This ledger integrates the Stage14/15 deep-review queue into Stage23 without reopening frozen mathematics. Its purpose is to prevent duplicate attacks and to choose the next weapon by direct Stage23 compatibility rather than by queue age or arbitrary order.

## Selection policy

```text
ATTACK_SELECTION_POLICY=PRIORITY_DRIVEN
P1_BEFORE_P2=true
P3_REOPEN_REQUIRES_NEW_INPUT=true
SELECT_BY_STAGE23_COMPATIBILITY=true
UPPER_AND_LOWER_ATTACKS_BOTH_ALLOWED=true
ATTACK_HISTORY_DEDUP_REQUIRED=true
```

Priority meanings:

- `P0`: already under active attack; do not duplicate.
- `P1`: reusable now; choose by direct compatibility with the current Stage23 checkpoint.
- `P2`: potentially useful only after an external/new theorem input.
- `P3`: internally exhausted; reopening requires genuinely new equations, height information, or average theorem input.
- `P4`: wrong population for a direct Stage23 attack; may be contextual only.

## Stage23 checkpoint30 compatibility ranking

The queue items supplied by the Stage14/15 deep-review ledger are classified as follows.

| queue | class | Stage23 role | checkpoint30 decision |
|---|---|---|---|
| Q06 `(4,4) Kummer receiver + physical height` | P1 | upper/support attack | **SELECTED_UPPER_1** |
| Q03 elliptic/Selmer | P1 | current genus-1 slice, small points / generator height | **SELECTED_LOWER_1_PARALLEL** |
| Q04 K3/Kummer/fiber-product alternate coordinates | P1 | alternate geometric receiver if Q06/Q03 stall | QUEUED_2 |
| Q11 fixed-prime local overlap sieve | P1 | possible uniform fixed-power upper improvement | QUEUED_3 |
| Q05 moving genus-one | P2 | requires external theorem/input to restart | HOLD_EXTERNAL |
| Q07-Q10 | P3 | internally exhausted at current equation/height resolution | NO_REATTACK_WITHOUT_NEW_INPUT |

No strict global order among all P1 weapons is claimed. The order above is **checkpoint30-specific**: Q06 is selected first because checkpoint30 already has a one-sided half-power upper theorem and explicitly permits upper-bound improvement; Q03 is selected in parallel because checkpoint30 has just produced a genus-1 Stage17-originating slice.

## Q06 upper/support attack: applicability test

Current certified upper theorem:

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Q06 is accepted as the first upper-side weapon because a `(4,4)` Kummer receiver together with a proved physical-height comparison could in principle replace or refine the current host-counting support. The Stage23 attack question is not merely whether a Kummer model exists, but whether its rational/integral point count under the **physical cutoff** `R=d<=B` yields a strictly stronger exponent or logarithmic saving for the literal Stage19 population.

Checkpoint30 outcome:

```text
Q06_STAGE23_COMPATIBLE=true
Q06_SELECTED=true
Q06_REQUIRED_OUTPUT=physical-height transfer + point-count bound on literal Stage19 population
Q06_CURRENT_EXPONENT_IMPROVEMENT_PROVED=false
Q06_REASON_NOT_YET_IMPROVED=no newly certified Kummer point-count theorem under the Stage23 physical height is materialized in this checkpoint
Q06_REJECTED=false
Q06_STATUS=ACTIVE_P1_UPPER
```

Thus Q06 is **not** discarded and the existing half-power ceiling is **not** declared optimal. It remains the first upper-side attack receiver.

## Q03 lower-side parallel attack: applicability test

Checkpoint30's fresh Stage17-originating slice found

\[
w^2=(t^2+1)(t^2+2t+2),
\qquad t\equiv1\pmod{14},
\]

a genus-1 degeneration candidate. This makes Q03 directly compatible for elliptic/Selmer, small-point and generator-height analysis.

```text
Q03_STAGE23_COMPATIBLE=true
Q03_SELECTED=true
Q03_TRIGGER=GENUS1_DEGENERATION_FOUND_AT_CHECKPOINT30
Q03_REQUIRED_OUTPUT=elliptic model + rational/integral point structure + congruence-compatible generator/height analysis
Q03_INFINITE_STAGE19_FAMILY_PROVED=false
Q03_STATUS=ACTIVE_P1_LOWER_PARALLEL
```

The zero-hit finite scan is not used to reject Q03.

## Q04 and Q11 reserve rules

Q04 becomes the next geometry weapon if Q06 does not produce a stronger physical-height count or if Q03's elliptic model suggests a K3/Kummer/fiber-product lift.

Q11 becomes the next local-sieve upper weapon if a uniformity statement is available that converts fixed-prime overlap rejection into a bound that is genuinely stronger than qualitative zero density. Its existing qualitative zero-density role is not double-counted with the Stage14 half-power theorem.

```text
Q04_STATUS=P1_RESERVE
Q11_STATUS=P1_RESERVE
Q11_FIXED_POWER_IMPROVEMENT_PROVED=false
DOUBLE_CHARGE_FORBIDDEN=true
```

## Dedup / re-entry rules

```text
REPEAT_STAGE14_15_SQUARECLASS_ATTACK_WITHOUT_NEW_INPUT=false
REPEAT_Q07_Q10=false
Q07_Q10_REENTRY_CONDITION=NEW_EQUATION_OR_HEIGHT_OR_AVERAGE_THEOREM
P2_AUTOMATIC_PROMOTION=false
P2_PROMOTION_REQUIRES_NEW_EXTERNAL_INPUT=true
POPULATION_MISMATCH_DIRECT_ATTACK=false
```

## Checkpoint30 repair verdict

The audit-required Stage14/15 attack ledger is now integrated and a checkpoint-specific priority queue is explicit. Both upper and lower routes remain live.

```text
STAGE14_15_ATTACK_LEDGER_INTEGRATED=true
ATTACK_IDS_ACCEPTED_REJECTED_RECORDED=true
DEEP_REVIEW_QUEUE_CHECK=PASS
CURRENT_UPPER_ATTACK=Q06
CURRENT_LOWER_ATTACK=Q03
NEXT_P1_RESERVES=Q04,Q11
P2_HOLD=Q05
P3_NO_REATTACK=Q07,Q08,Q09,Q10
ZERO_DENSITY_MATHEMATICS_REOPENED=false
FRESH_GENUS1_ATTACK_REOPENED=false
```
