# Stage25-30 — direct endpoint ratio and three-way path consistency

EVIDENCE_LEVEL=PROVED_FROM_AUDITED_INTERFACES
CHECKPOINT=30
STATUS=PROVED_SUBMITTED_FOR_FRESH_AUDIT
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

This does **not** identify a true polynomial exponent. The current theorem envelope only places any hypothetical pure polynomial exponent between the lower-side power `-2` and upper-side power `-3/2` (up to logarithms and epsilon).

```text
TRUE_RATIO_EXPONENT_IDENTIFIED=false
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_TARGET_LOWER_BOUND_PROVED=false
STRICT_SUB_SQRT_TARGET_UPPER_PROVED=false
```

## 3. Path A — Stage22 then Stage24

Stage22 gives

\[
\frac{M_2}{M_1}
\sim
\frac{4\pi^2 C_{M_2}}3\frac{(\log B)^4}{B}.
\]

Stage24 gives

\[
B^{-1}(\log B)^{-9/2}
\ll
\frac{N_2}{M_2}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

Multiplying the two count ratios gives, exactly at the count-identity level,

\[
\frac{M_2}{M_1}\frac{N_2}{M_2}=\frac{N_2}{M_1}.
\]

The powers combine as

\[
B^{-1}(\log B)^4\cdot B^{-1}(\log B)^{-9/2}
=B^{-2}(\log B)^{-1/2},
\]

and

\[
B^{-1}(\log B)^4\cdot B^{-1/2+\varepsilon}(\log B)^{-5}
=B^{-3/2+\varepsilon}(\log B)^{-1}.
\]

Thus Path A reproduces the direct endpoint envelope exactly in polynomial/logarithmic scale.

## 4. Path B — Stage21 then Stage23

Stage21 gives

\[
\frac{N_1}{M_1}
\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

The audited post-Stage24 Stage23 reinvestigation gives

\[
B^{-1}(\log B)^{-5/2}
\ll
\frac{N_2}{N_1}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

Again the exact count identity is

\[
\frac{N_1}{M_1}\frac{N_2}{N_1}=\frac{N_2}{M_1}.
\]

The powers combine as

\[
B^{-1}(\log B)^2\cdot B^{-1}(\log B)^{-5/2}
=B^{-2}(\log B)^{-1/2},
\]

and

\[
B^{-1}(\log B)^2\cdot B^{-1/2+\varepsilon}(\log B)^{-3}
=B^{-3/2+\varepsilon}(\log B)^{-1}.
\]

Thus Path B also reproduces the direct endpoint envelope exactly in polynomial/logarithmic scale.

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

## 6. Directional refinement

Stage21's audited source theorem gives, for each direction/chamber `j`,

\[
M_{1,j}(B)\sim c_j B^2\log B,
\qquad c_j>0.
\]

Since `N2,j(B)<=N2(B)`, every direction satisfies

\[
\boxed{
\frac{N_{2,j}(B)}{M_{1,j}(B)}
\ll_{\varepsilon,j}
B^{-3/2+\varepsilon}(\log B)^{-1}
\to0
}.
\]

The Stage23 post-Stage24 reinvestigation additionally proves

\[
N_{2,c}(B)\gg\sqrt{\log B}.
\]

Therefore the `c` target direction has the two-sided endpoint envelope

\[
\boxed{
B^{-2}(\log B)^{-1/2}
\ll
\frac{N_{2,c}(B)}{M_{1,c}(B)}
\ll_\varepsilon
B^{-3/2+\varepsilon}(\log B)^{-1}
}.
\]

No corresponding positive lower theorem is currently imported here for the `a` or `b` target directions, so checkpoint30 does not invent one.

```text
DIRECTIONAL_UPPER_ALL=PROVED
DIRECTIONAL_C_LOWER=PROVED
DIRECTIONAL_C_TWO_SIDED_ENVELOPE=PROVED
DIRECTIONAL_A_B_LOWER=OPEN_GATE
```

## 7. Constant/refinement boundary

The source leading constant is explicit, but the Stage24 lower constant is implicit and the Stage19/Stage14 upper constant is epsilon-dependent/implicit. Therefore checkpoint30 cannot produce a leading constant for `N2/M1`.

The Stage18 constant `C_M2` and Stage21 constant `kappa` appear on the two intermediate paths, but they do not create an independent endpoint leading constant because the adjacent ratios only have two-sided bounds on the `N2` side.

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

## 9. Exit state

```text
REPO_REUSE_PREFLIGHT=PASS
DISCOVERY_CHECKPOINT=Stage25-30
EXPLORATION_EVIDENCE_COMPLETE=true
UPSTREAM_PREMISE_CHECK=PASS
RETURN_TO_SOURCE_REQUIRED=false
SUBLANES_OPENED=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=30
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
CODEX_REQUIRED=false
```
