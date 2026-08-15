# Stage25-30 — direct endpoint ratio and three-way path consistency

EVIDENCE_LEVEL=PROVED_FROM_AUDITED_INTERFACES
CHECKPOINT=30
STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT
STAGE=Stage25
TRANSITION=Stage16->Stage19

## 1. Matched endpoint interfaces

Stage25 compares population sizes under the common physical cutoff `R<=B`:

- `M1(B)`: primitive canonical exactly-one-face objects, no space requirement;
- `N2(B)`: primitive canonical exactly-two-face objects with integral space diagonal.

The masks are disjoint, so `N2/M1` is a matched population-size ratio, not objectwise survival.

Audited source and target interfaces are

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\]

and, after the Stage24-50 lower breakthrough,

\[
\sqrt{\log B}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

## 2. Direct endpoint theorem

Dividing the lower and upper target bounds by the positive source asymptotic gives

\[
\boxed{
B^{-2}(\log B)^{-1/2}
\ll
\frac{N_2(B)}{M_1(B)}
\ll_\varepsilon
B^{-3/2+\varepsilon}(\log B)^{-1}
}.
\]

For any fixed `0<epsilon<3/2`, the upper bound tends to zero, hence

\[
\boxed{\frac{N_2(B)}{M_1(B)}\to0}.
\]

At the same time Stage24 proves `N2(B)->infinity`. Therefore Stage25 checkpoint30 classifies the combined endpoint comparison as

```text
ENDPOINT_RATIO_CLASS=VANISHING_POPULATION_RATIO_WITH_INFINITE_TARGET
TARGET_UNBOUNDEDNESS_PROVED=true
RATIO_LIMIT_ZERO=true
```

This does **not** identify a true polynomial exponent.

```text
TRUE_RATIO_EXPONENT_IDENTIFIED=false
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_TARGET_LOWER_BOUND_PROVED=false
STRICT_SUB_SQRT_TARGET_UPPER_PROVED=false
```

## 3. Path A — Stage22 then Stage24

Stage22 gives

\[
\frac{M_2}{M_1}\sim \frac{4\pi^2 C_{M_2}}3\frac{(\log B)^4}{B}.
\]

Stage24 gives

\[
B^{-1}(\log B)^{-9/2}\ll\frac{N_2}{M_2}
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

At the exact count-identity level,

\[
\frac{M_2}{M_1}\frac{N_2}{M_2}=\frac{N_2}{M_1}.
\]

The lower and upper scales become respectively

\[
B^{-2}(\log B)^{-1/2},
\qquad
B^{-3/2+\varepsilon}(\log B)^{-1}.
\]

Thus Path A reproduces the direct endpoint envelope.

## 4. Path B — Stage21 then Stage23

Stage21 gives

\[
\frac{N_1}{M_1}\sim \frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

The audited post-Stage24 Stage23 reinvestigation gives

\[
B^{-1}(\log B)^{-5/2}\ll\frac{N_2}{N_1}
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

Again,

\[
\frac{N_1}{M_1}\frac{N_2}{N_1}=\frac{N_2}{M_1},
\]

and the same lower and upper endpoint scales result. Thus Path B reproduces the direct endpoint envelope.

## 5. Three-way consistency theorem

For all sufficiently large `B` for which the denominators are nonzero,

\[
\boxed{
\frac{N_2}{M_1}
=
\frac{M_2}{M_1}\frac{N_2}{M_2}
=
\frac{N_1}{M_1}\frac{N_2}{N_1}
}.
\]

This is algebraic cancellation of population counts. It is **not** a probabilistic factorization and does not assert independence of face-integrality and space-integrality conditions.

```text
DIRECT_ENDPOINT_RATIO_CHECK=PASS
PATH_A_PRODUCT_CHECK=PASS
PATH_B_PRODUCT_CHECK=PASS
THREE_WAY_CONSISTENCY=PASS
PROBABILISTIC_INDEPENDENCE_INFERRED=false
DOUBLE_CHARGE_FIREWALL=ACTIVE
```

## 6. Directional boundary — repaired after fresh audit

The first checkpoint30 submission incorrectly used one symbol `j` for two different indexing systems:

- Stage21 `q`: order chambers with leading factors `I_q`;
- Stage23 `c`: an exactly-two shared-edge / face-mask channel, namely the channel with `ac` and `bc` integral.

No chamber-to-shared-edge source adapter has been proved. Therefore checkpoint30 **withdraws** the claims

\[
N_{2,j}/M_{1,j}\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}
\]

for shared-edge directions and the claimed two-sided `c`-channel ratio envelope.

The independently audited Stage23 target-only fact remains valid:

\[
\boxed{N_{2,c}(B)\gg\sqrt{\log B}}.
\]

But no denominator theorem `M_{1,c}(B)~c_c B^2 log B` is imported or asserted here. Hence no `N2,c/M1,c` ratio theorem follows at checkpoint30.

```text
DIRECTIONAL_STAGE23_C_LOWER=PROVED_TARGET_ONLY
DIRECTIONAL_SOURCE_CHANNEL_ADAPTER_PROVED=false
DIRECTIONAL_UPPER_ALL=NOT_PROVED
DIRECTIONAL_C_TWO_SIDED_ENVELOPE=NOT_PROVED
DIRECTIONAL_RATIO_REFINEMENT_STATUS=OPEN_GATE_ADAPTER_REQUIRED
DIRECTIONAL_A_B_LOWER=OPEN_GATE
DIRECTIONAL_OVERCLAIM_REPAIRED=true
```

This downgrade does not affect the global `N2/M1` theorem or either exact path identity.

## 7. Constant/refinement boundary

The source leading constant is explicit, but the Stage24 lower constant is implicit and the Stage19/Stage14 upper constant is epsilon-dependent/implicit. Therefore checkpoint30 cannot produce a leading constant for `N2/M1`.

```text
CONSTANT_REFINEMENT_CHECK=NOT_APPLICABLE_WITH_CURRENT_TARGET_BOUNDS
LEADING_ENDPOINT_CONSTANT_RECOVERED=false
LOG_POWER_ENVELOPE_RECOVERED=true
```

## 8. Finite baseline boundary

Checkpoint20's exact matched panel is used only as a regression/transcription check. Its sparse nonmonotone behavior is not used to prove any exponent or logarithmic power above.

```text
FINITE_DATA_USED_AS_PROOF=false
FINITE_POWER_FIT_PROMOTED=false
```

## 9. Repair and exit state

Fresh audit accepted the global endpoint theorem and both exact path products, but rejected the unproved directional ratio adapter and required restoration of checkpoint10/20 controller provenance. This repair chooses the permitted downgrade route; no global mathematics or counts are recomputed.

```text
REPAIR_SCOPE=DIRECTIONAL_DOWNGRADE_PLUS_CONTROLLER_HISTORY_RESTORE
GLOBAL_ENDPOINT_RATIO_REOPENED=false
COUNTS_RECOMPUTED=false
CONTROLLER_HISTORY_RESTORE_REQUIRED=true
CONTROLLER_HISTORY_RESTORE_STATUS=COMPLETE_IN_CONTROLLER
REPO_REUSE_PREFLIGHT=PASS
DISCOVERY_CHECKPOINT=Stage25-30
EXPLORATION_EVIDENCE_COMPLETE=true
UPSTREAM_PREMISE_CHECK=PASS_GLOBAL_DIRECTIONAL_ADAPTER_OPEN
RETURN_TO_SOURCE_REQUIRED=false
SUBLANES_OPENED=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=30
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
CODEX_REQUIRED=false
```
