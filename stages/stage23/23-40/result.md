# Stage23-40 — priority-driven upper/lower attack execution

EVIDENCE_LEVEL=ATTACK_LEDGER
CHECKPOINT=40
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## 1. Entry condition

Checkpoint30 is audited PASS and merged. Its frozen theorem remains

\[
N_2(B)/N_1(B)\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}\to0.
\]

Checkpoint40 does not reopen that theorem. It executes the priority queue fixed at checkpoint30.

## 2. Selected attacks

The checkpoint30 queue selected:

- upper side: `Q06`, `(4,4) Kummer receiver + physical height`;
- lower side: `Q03`, elliptic/Selmer analysis of the new Stage17-originating genus-one slice;
- reserves: `Q04`, then `Q11`;
- external hold: `Q05`;
- no reattack without new input: `Q07-Q10`.

This checkpoint obeys attack-history deduplication and does not rerun Stage14/15 squareclass attacks.

## 3. Q06 upper-side attack

The target population is the literal Stage19 primitive/canonical population under physical height `d<=B`. A Kummer receiver can improve the Stage23 ceiling only if two transfers are simultaneously certified:

1. every relevant Stage19 point maps to the chosen receiver with controlled multiplicity outside explicitly bounded exceptional loci;
2. the receiver height `H_K` is compared uniformly with the physical height `d` strongly enough that a rational/integral point estimate for `H_K<=X` yields a bound strictly smaller than `B^(1/2+epsilon)` for the original population.

The current repository queue provides Q06 as a reusable receiver/support weapon, but checkpoint40 does not contain a certified point-count theorem under the transferred physical height that improves the exponent or supplies a logarithmic saving. Therefore:

```text
Q06_EXECUTED=YES
Q06_APPLICABILITY=PASS
Q06_PHYSICAL_HEIGHT_TRANSFER_NEEDED=true
Q06_LITERAL_POPULATION_MULTIPLICITY_CONTROL_NEEDED=true
Q06_STRONGER_POINT_COUNT_THEOREM_FOUND=false
Q06_EXPONENT_IMPROVEMENT_PROVED=false
Q06_LOG_SAVING_PROVED=false
Q06_STATUS=ATTACKED_NO_BREAKTHROUGH_KEEP_P1_IF_NEW_HEIGHT_COUNT_INPUT
```

This is not evidence that the half-power ceiling is optimal. It records the exact missing bridge instead of silently exhausting Q06.

## 4. Q03 lower-side genus-one attack

Checkpoint30 produced the slice

\[
w^2=(t^2+1)(t^2+2t+2),\qquad t\equiv1\pmod{14}.
\]

This is a quartic genus-one curve with the rational point `(t,w)=(0,1)`, so the genus-one receiver is not merely hypothetical: it has a rational base point and hence admits an elliptic-curve model over `Q`.

The Stage23 question is stronger than existence of the elliptic model. To produce an infinite Stage19 family one needs infinitely many rational points whose `t`-coordinate is integral, satisfies `t=1 mod14`, and survives the Stage17 primitive/canonical and exactly-two conditions after substitution.

The checkpoint30 integer scan found no such positive `t<10^6` on the required congruence class. Checkpoint40 therefore records the exact elliptic arithmetic gate:

```text
Q03_EXECUTED=YES
GENUS1_RATIONAL_BASE_POINT_FOUND=true
ELLIPTIC_MODEL_EXISTS_OVER_Q=true
ELLIPTIC_RANK_COMPUTED=false
POSITIVE_RANK_PROVED=false
CONGRUENCE_COMPATIBLE_GENERATOR_FOUND=false
INTEGRAL_T_INFINITE_SET_PROVED=false
INFINITE_STAGE19_FAMILY_PROVED=false
Q03_STATUS=LIVE_ARITHMETIC_GATE
```

A positive Mordell-Weil rank alone would still not automatically prove infinitely many integral `t`; the integral/congruence transfer must be proved separately.

## 5. Reserve activation decision

Neither selected P1 attack produced a certified exponent improvement or lower family. Under the priority policy, the next compatible reserves are activated for subsequent attack rather than recycling Q06/Q03 blindly:

```text
Q04_NEXT=YES
Q04_ROLE=alternate K3/Kummer/fiber-product coordinates linking physical height or elliptic slice
Q11_NEXT=YES
Q11_ROLE=fixed-prime overlap sieve; requires uniformity to produce quantitative power/log saving
Q05_STATUS=P2_EXTERNAL_HOLD
Q07_Q10_STATUS=P3_NO_REATTACK_WITHOUT_NEW_INPUT
```

## 6. Current Stage23 boundary

```text
ZERO_DENSITY_TRANSITION_PROVED=true
CURRENT_TARGET_UPPER=N2(B)<<_epsilon B^(1/2+epsilon)
UPPER_IMPROVEMENT_AT_CHECKPOINT40=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
TARGET_UNBOUNDEDNESS_PROVED=false
INFINITE_PRIMITIVE_STAGE19_FAMILY_FOUND=false
POSITIVE_POWER_TARGET_LOWER_BOUND_FOUND=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
ATTACK_HISTORY_DEDUP=PASS
UPPER_AND_LOWER_ATTACKS_EXECUTED=true
```

Checkpoint40 therefore advances the attack ledger and exposes two precise missing bridges: a physical-height Kummer count on the upper side, and elliptic rank/integral-congruence arithmetic on the lower side. No finite computation is promoted to proof.

```text
NEXT_CHECKPOINT_AFTER_PASS=50
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
