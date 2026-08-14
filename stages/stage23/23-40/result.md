# Stage23-40 — deep execution of Q06 and Q03

EVIDENCE_LEVEL=ATTACK_LEDGER+PROVED_OBSTRUCTION
CHECKPOINT=40
STATUS=SUBMITTED_FOR_FRESH_AUDIT
REPAIR_SCOPE=Q06_SOURCE_LEVEL_RECEIVER_EXECUTION_AND_Q03_RESULT_SYNC_ONLY

## 1. Entry condition

Checkpoint30 is audited PASS and merged. Its frozen theorem remains

\[
N_2(B)/N_1(B)\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}\to0.
\]

Checkpoint40 does not reopen that theorem.

## 2. Q03 deep execution — closed on this slice

Checkpoint30 produced

\[
w^2=(t^2+1)(t^2+2t+2).
\]

The previously written claim that `(t,w)=(0,1)` is a rational point was false and is withdrawn: at `t=0` the right side equals `2`.

For every integer `t`, one of `t,t+1` is even. Direct parity calculation gives

\[
(t^2+1)(t^2+2t+2)\equiv2\pmod 8.
\]

But a square modulo `8` is only `0,1,4`. Therefore

\[
\boxed{w^2=(t^2+1)(t^2+2t+2)\text{ has no integer }t.}
\]

This eliminates the entire consecutive-parameter Stage17 slice for Stage19, including the required subclass `t=1 mod14`. The earlier finite scan is no longer load-bearing.

```text
Q03_DEEP_EXECUTION=PASS
Q03_FALSE_RATIONAL_POINT_CLAIM_WITHDRAWN=true
Q03_MOD8_OBSTRUCTION_PROVED=true
Q03_INTEGER_T_SURVIVORS=0
Q03_REOPEN_REQUIRED=false
```

## 3. Q06 source-level receiver execution

Q06 is now executed from its actual Stage14 source chain rather than from the queue label alone. Detailed derivation is in `stages/stage23/23-40/q06-source-execution.md`.

Opened source attack IDs:

- `Stage14-4ah` / PR #164 — exact physical Kummer polarization and height;
- `Stage14-tH15` / PR #457 — explicit projective `(4,4)` squareclass receiver and transverse Frobenius incidence;
- `Stage14-t64` / PR #497 — sharper cross-ratio/Jacobi quotient of that `(4,4)` receiver.

### Physical height

Stage14-4ah proves on the resolved two-face Kummer surface

\[
M=\pi^*(-K_Y),\qquad H_M(P)=\sqrt{e^2+x^2+y^2}=d.
\]

Stage23/Stage19 uses the literal cutoff `d<=B`. Hence

```text
Q06_PHYSICAL_HEIGHT_IDENTITY=H_M=d
Q06_HEIGHT_ADAPTER_LOSS=0
```

There is no polynomial distortion in transporting the Stage19 cutoff to the Kummer receiver.

### Actual receiver map and multiplicity

Stage14-tH15 fixes primitive Gaussian `U` and projective slopes from the moving canonical prime `pi` and primitive cofactor `V`. Each fixed-squareclass branch is represented by

\[
Z^2=\kappa P_U(x,y),
\]

with `P_U` of bidegree at most `(4,4)`. It gives the exact partition

\[
E_U=R_U+I_{same\,\pi}+I_{same\,V}+I_{transverse},
\]

and a Cauchy-free positive Frobenius receiver for the transverse term.

A canonical Stage19 object has exactly two integral faces. Choosing one of those faces and the bounded orientation data maps it into this Stage14 two-face receiver with `O(1)` combinatorial multiplicity. Thus the population adapter does not create a power loss. The nontrivial multiplicity is the arithmetic multiplicity already represented by row/column/transverse receiver fibers.

### Sharper receiver after t64

Stage14-t64 reduces the generic `(4,4)` label by

\[
T=t^2,\quad X=x^2,\quad R=\frac{X-T}{1-TX},
\]

with exact squareclass identity `[F]=[R]`. Fixing `R=s` gives

\[
X=\frac{T+s}{1+sT},
\]

and restoring the physical square lift produces

\[
y^2=(t^2+s)(1+s t^2).
\]

So the minimal unresolved Q06 object is not an anonymous K3 point count. It is the moving **transverse Jacobi square-lift incidence** under the exact height `d=H_M`.

### Height/multiplicity push result

The source chain proves:

```text
Q06_SOURCE_ATTACK_IDS_OPENED=true
Q06_ACTUAL_RECEIVER_MAP_MATERIALIZED=true
Q06_PHYSICAL_HEIGHT_IDENTITY_PROVED=true
Q06_HEIGHT_LOSS=0
Q06_STAGE23_ORIENTATION_MULTIPLICITY=O(1)
Q06_ROW_COLUMN_MULTIPLICITY_PARTITIONED=true
Q06_TRANSVERSE_RECEIVER=SharedUTransverseJacobiSquareLiftIncidence
```

Stage14-4ah further proves every fixed physical rational curve has `M.C>=4`, so any single fixed rational curve contributes at most half-power scale under `d<=B`. This explains why Q06 naturally meets the existing `1/2` barrier.

What remains unproved is a uniform bound on the **moving family** of transverse Jacobi/Kummer fibers. Neither tH15 nor t64 proves the required transverse dispersion. Therefore no stronger Stage23 upper exponent follows.

```text
Q06_SINGLE_FIXED_CURVE_EXPONENT_LE_1_2=true
Q06_MOVING_FAMILY_COUNT_CONTROL_PROVED=false
Q06_TRANSVERSE_DISPERSION_PROVED=false
Q06_EXPONENT_IMPROVEMENT_PROVED=false
Q06_LOG_SAVING_PROVED=false
Q06_INTERNAL_SOURCE_EXECUTION_EXHAUSTED_AT_CURRENT_INPUT=true
```

This is now a source-level boundary, not a failure to inspect the source.

## 4. Reserve policy

Per the checkpoint40 audit, Q04/Q11 are still deferred until Q06/Q03 are audited at this depth. They are not activated in this repair.

```text
Q04_Q11_ACTIVATION_DEFERRED=true
Q05_STATUS=P2_EXTERNAL_HOLD
Q07_Q10_STATUS=P3_NO_REATTACK_WITHOUT_NEW_INPUT
```

## 5. Current Stage23 boundary

```text
ZERO_DENSITY_TRANSITION_PROVED=true
CURRENT_TARGET_UPPER=N2(B)<<_epsilon B^(1/2+epsilon)
UPPER_IMPROVEMENT_AT_CHECKPOINT40=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
TARGET_UNBOUNDEDNESS_PROVED=false
INFINITE_PRIMITIVE_STAGE19_FAMILY_FOUND=false
POSITIVE_POWER_TARGET_LOWER_BOUND_FOUND=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
Q03_DEEP_EXECUTION=PASS
Q06_SOURCE_LEVEL_EXECUTION=PASS_WITH_NO_BREAKTHROUGH
FINITE_DATA_USED_AS_PROOF=false
```

```text
NEXT_CHECKPOINT_AFTER_PASS=50
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
