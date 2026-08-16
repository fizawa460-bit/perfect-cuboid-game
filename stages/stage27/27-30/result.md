# Stage27-30 — corridor normalization and receiver calculus

```text
TASK_ID=Stage27-30
CHECKPOINT=30
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=PROVED_DERIVED_RECEIVER_CALCULUS_CANDIDATE
PARENT_CHECKPOINT=Stage27-20
PARENT_PR=1023
PARENT_MERGE_COMMIT=ecbd182f25dcb010319789855c82477eee7077c7
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
```

## 1. Frozen same-measure transition

Stage27 keeps the literal Stage18 -> Stage19 transition under the exact primitive/canonical Euclidean contract `R<=B`:

- `M2(B)`: exactly two integral face diagonals, no space requirement;
- `N2(B)`: the same physical population with the additional requirement `R in Z`.

The current audited theorem surface is

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

For each canonical shared-edge chamber `j=a,b,c`,

\[
M_{2,j}(B)\sim C_jB(\log B)^5,\qquad C_j>0,
\]

and currently

\[
N_{2,j}(B)\gg_j B^{1/4}.
\]

Checkpoint20's finite effective exponent is diagnostic only and is not substituted for any exponent below.

## 2. Generic global lower receiver

Suppose a later Stage27 checkpoint proves, on this exact population and cutoff, a genuine lower theorem

\[
N_2(B)\gg B^\beta
\]

for some fixed `beta>0`. Then the literal Stage18 -> Stage19 survival ratio

\[
S_2(B):=\frac{N_2(B)}{M_2(B)}
\]

satisfies

\[
\boxed{S_2(B)\gg B^{\beta-1}(\log B)^{-5}}.
\]

Stage23 already freezes `N1(B) asy B(log B)^3` at the ratio-interface level, so the same lower gives

\[
\boxed{\frac{N_2(B)}{N_1(B)}\gg B^{\beta-1}(\log B)^{-3}}.
\]

Using the audited Stage22 interface

\[
\frac{M_2(B)}{M_1(B)}\asymp B^{-1}(\log B)^4,
\]

the Stage23 second-order cross-ratio

\[
I(B):=\frac{N_2/N_1}{M_2/M_1}
\]

obeys

\[
\boxed{I(B)\gg B^\beta(\log B)^{-7}}.
\]

Likewise the Stage16S ambient space-survival baseline is `S0(B) asy B^-1`; hence the Stage24 interaction

\[
J_2(B):=\frac{S_2(B)}{S_0(B)}
\]

obeys

\[
\boxed{J_2(B)\gg B^\beta(\log B)^{-5}}.
\]

The current `beta=1/4` recovers the already-audited Stage23/24 lower interfaces. A genuine global lower-exponent improvement is therefore exactly `beta>1/4`.

## 3. Generic global upper receiver

Suppose instead that a later checkpoint proves, for some fixed `mu<1`,

\[
N_2(B)\ll_\varepsilon B^{\mu+\varepsilon}
\qquad(\forall\varepsilon>0).
\]

Then

\[
\boxed{S_2(B)\ll_\varepsilon B^{\mu-1+\varepsilon}(\log B)^{-5}},
\]

\[
\boxed{\frac{N_2(B)}{N_1(B)}\ll_\varepsilon B^{\mu-1+\varepsilon}(\log B)^{-3}},
\]

\[
\boxed{I(B)\ll_\varepsilon B^{\mu+\varepsilon}(\log B)^{-7}},
\]

and

\[
\boxed{J_2(B)\ll_\varepsilon B^{\mu+\varepsilon}(\log B)^{-5}}.
\]

The current theorem has `mu=1/2`. Thus a strict whole-family sub-square-root improvement is exactly a theorem with

\[
\boxed{\mu<1/2}.
\]

No such theorem is claimed at checkpoint30.

## 4. Directional receiver calculus

A directional lower theorem must be proved direction by direction. If

\[
N_{2,j}(B)\gg_j B^{\beta_j},
\]

then

\[
\boxed{\frac{N_{2,j}(B)}{M_{2,j}(B)}\gg_j B^{\beta_j-1}(\log B)^{-5}},
\]

and

\[
\boxed{J_{2,j}(B)\gg_j B^{\beta_j}(\log B)^{-5}}.
\]

Under the exact shared-edge map used by Stage23,

- `j=a` feeds raw overlap `A_ab,ac`;
- `j=b` feeds raw overlap `A_ab,bc`;
- `j=c` feeds raw overlap `A_ac,bc`.

Thus a proved directional exponent `beta_j` also gives the corresponding raw-overlap lower `A_pair(B)>>B^(beta_j)`.

However, a **global** theorem `N2(B)>>B^beta` does not by itself prove the same lower exponent in each named direction. It may only force substantial mass in at least one chamber. Therefore all-three-direction propagation requires directional hypotheses.

On the upper side, a global theorem `N2(B)<<_epsilon B^(mu+epsilon)` automatically bounds every `N2,j<=N2`; together with `M2,j~C_j B(log B)^5` it yields

\[
\frac{N_{2,j}(B)}{M_{2,j}(B)}
\ll_{j,\varepsilon}B^{\mu-1+\varepsilon}(\log B)^{-5}
\]

for every `j`.

## 5. What would identify the exponent

A finite effective slope cannot identify the true exponent. A polynomial exponent `alpha` would be identified at exponent level if, for every fixed `epsilon>0`, one had compatible theorem-level bounds

\[
B^{\alpha-\varepsilon}\ll_\varepsilon N_2(B)
\ll_\varepsilon B^{\alpha+\varepsilon}.
\]

This would imply

\[
\frac{\log N_2(B)}{\log B}\to\alpha,
\]

but would still **not** prove an asymptotic constant or logarithmic secondary factor.

## 6. Attack gates for checkpoints40 and50

Checkpoint40 upper attack counts as exponent progress only if it proves a same-measure theorem with `mu<1/2`; fixed-prime zero density or finite `N2/sqrt(B)` decay is insufficient.

Checkpoint50 lower attack counts as global exponent progress only if it proves `beta>1/4` after primitivity, canonicalization, exact height, integral-space, exactly-two, and fiber control. Propagation to all Stage23 overlap channels additionally requires directional versions.

```text
CURRENT_GLOBAL_BETA=1/4
CURRENT_GLOBAL_MU=1/2
CURRENT_SURVIVAL_LOWER=N2/M2>>B^(-3/4)(log B)^(-5)
CURRENT_SURVIVAL_UPPER=N2/M2<<_epsilon B^(-1/2+epsilon)(log B)^(-5)
GLOBAL_LOWER_PROGRESS_GATE=beta>1/4
GLOBAL_UPPER_PROGRESS_GATE=mu<1/2
GLOBAL_LOWER_IMPLIES_ALL_DIRECTIONAL_LOWER=false
GLOBAL_UPPER_IMPLIES_ALL_DIRECTIONAL_UPPER=true
EXPONENT_IDENTIFICATION_REQUIRES_MATCHED_THEOREM_BOUNDS=true
FINITE_EFFECTIVE_EXPONENT_AS_THEOREM=false
NEW_N2_EXPONENT_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage27-audit
```
