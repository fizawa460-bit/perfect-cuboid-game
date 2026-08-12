# Stage14 roadmap — exactly-two integral-face population

## Canonical main-line batch entry point

The permanent execution entry for the `Stage14-4*` main line is:

```text
Stage14-main-batch
```

Before deriving a successor, read the common contract
[`docs/stage14-batch-common-contract.md`](../../docs/stage14-batch-common-contract.md)
and then the main specialization
[`docs/stage14-main-batch-task-contract.md`](../../docs/stage14-main-batch-task-contract.md)
from latest merged `main`. It follows the unique merged `NEXT` for 3--5
substantive work units on one branch and publishes one Draft PR. A newly needed
main-line H audit is frozen and executed as one clean-room work unit in the same
batch; H need alone is not a stop condition.

```text
STAGE14_MAIN_CANONICAL_EXECUTION_ENTRY=Stage14-main-batch
STAGE14_MAIN_BATCH_COMMON_CONTRACT=docs/stage14-batch-common-contract.md
STAGE14_MAIN_BATCH_ROUTE_CONTRACT=docs/stage14-main-batch-task-contract.md
STAGE14_MAIN_BATCH_MINIMUM_TARGET_WORK_UNITS=3
STAGE14_MAIN_BATCH_MAXIMUM_WORK_UNITS=5
STAGE14_MAIN_BATCH_ONE_BRANCH_ONE_PR=true
STAGE14_MAIN_BATCH_EARLY_STOP=receiver_change|unresolved_external_gate|rigorous_counterexample
STAGE14_MAIN_BATCH_INTEGRATES_NEW_H=true
STAGE14_MAIN_BATCH_H_COUNTS_AS_WORK_UNIT=true
```

## Goal

Count and explain primitive canonical exactly-two-face cuboids with integer space diagonal under `d<=B`.

## Completed main-track foundation

- `14-1` through `14-3`: definition, independent exact enumeration, finite reconnaissance.
- `14-4aa` through `14-4ae`: two-face gluing, height envelope, elliptic reduction, generic rank zero.
- `14-4af` through `14-4ag`: Pythagorean-base K3, level-4/Kummer identification, rank-jump graph.
- `14-4ah` through `14-4ak`: physical polarization and complete closure of fixed `M.C=4` rational-curve square-root mechanisms.
- `14-4al`: collective first-hit measure `V(B)=#{F:mu(F)<=B}`.
- `14-4am`: exact activation factorization `A -> Sigma -> R -> V` and complete `H<=20k` rank/Selmer census.
- `14-4an`: compress selected-prime rows, import s5d unselected rows, and close the **entire odd-prime local character matrix**; identify its exact gate reach.
- `14-4ao`: import the exact eight-state `Q_2` image, close the full local matrix, quantify the finite `A -> Sigma` gate, and formulate the height-weighted descent count.
- `14-4ap`: import the s5g centering obstruction, delimit local character-sum reach, and formulate the conditional three-retainer transfer.

## Locked geometry

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

Any square-root phenomenon must be collective.

## Locked activation factorization

```text
A      eligible primitive oriented Pythagorean bases
Sigma  nontrivial full-2-Selmer beyond rational torsion
R      positive Mordell--Weil rank
V      physical first hit by B
```

Exactly

\[
V/A=(\Sigma/A)(R/\Sigma)(V/R).
\]

At `H<=20,000`:

```text
A=6372
Sigma=5209
R in [3784,4239]
V=54
Sigma/A=0.81748
V/R in [0.01274,0.01427]
```

Thus finite Selmer and positive rank are common; the dominant observed thinning is `R -> V`.

## 14-4an — complete odd reciprocity matrix

Status: [x] Complete.

For selected odd bad primes the s5c rows compress to

```text
S / 12 : chi_p(a3)=0
X / 13 : chi_p(a2)=0 and chi_p(-1)=0
H / 23 : chi_p(a1)=0.
```

Hence selected odd `p|X` requires `p=1 mod 4`.

Merged s5d gives all unselected odd bad-prime rows:

```text
p|S : chi_p(d3)=+1
p|H : chi_p(d1)=+1
p|X : chi_p(d2)=+1 OR chi_p(-d2)=+1.
```

Therefore

```text
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
```

The `H<=20,000` support audit gives

```text
selected-row mean surviving support fraction       0.1695801
selected-row bases with no nonempty support        0
complete-odd mean surviving support fraction       0.04556219
complete-odd mean surviving supports                4.09149
bases with no nonempty homogeneous odd support     779
```

The `779` count is not a Selmer base count: it is the homogeneous odd-only slice. The remaining local problem is covering-specific `Q_2` solubility; s5d has already reduced the product-square state space to 64 states.

Locked boundary:

```text
STAGE14_4AN=COMPLETE_ODD_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY
S5D_ALL_ODD_BAD_PRIME_ROWS_IMPORTED=true
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS=true
Q2_COVERING_SPECIFIC_SOLUBILITY_CLASSIFIED=false
FULL_LOCAL_SELMER_MATRIX_COMPLETE=false
CHARACTER_MATRIX_CONTROLS_SIGMA_TO_R=false
CHARACTER_MATRIX_CONTROLS_R_TO_V=false
HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING=true
```

## 14-4ao — Q2 completion + height-weighted descent count

Status: [x] Complete.

The exact `Q_2` image contains 8 of the 64 product-square states. Together with 4an this completes the local character system. At `H<=20,000`, the full local gate is `Sigma/A=5209/6372=0.8174827369742624`, while `V/R` remains only about `1.3--1.4%`.

The locked height-weighted count retains local admissibility, global solubility/Sha, and the s3 logarithmic canonical-height window. No family power saving or small-point lower-tail theorem is claimed.

## 14-4ap — family character sum with global/height coupling

Status: [x] Complete.

Merged s5g forces exact local mean subtraction: the uncentered character-sum target has local resonances. Even a centered family estimate controls only `Sigma/A`; it does not determine global solubility/Sha or the s3 first-small-point window.

For retainers `Sigma/A`, `R/Sigma`, and `H/R`, conditional exponents add. A square-root upper-bound scale requires total saving at least `1/2`. No individual uniform retainer estimate is proved.

## 14-4aq — global-solubility/Sha retainer

Status: [>] Next.

Isolate the global-solubility/Sha retainer `R/Sigma` and formulate a uniform averaging target compatible with the centered local sieve. Keep the s3 first-small-point retainer separate; do not infer global solubility from local character cancellation.

## Parallel arithmetic track

The s-track is a direct input to the main line:

- s5a: Euclid-parameter descent target;
- s5b: odd reciprocity skeleton;
- s5c: selected-prime local rows;
- s5d: complete odd local rows and 64-state `Q_2` reduction;
- later s5 stages: exact `Q_2` covering classification and family-level analytic estimates.

## s-route lifecycle / reactivation rule

The later `s7` route exhausted its then-known exact gcd/CRT/common-core/Cayley/root-line/row-column/reciprocal-reconstruction reductions at the square-root scale and was closed by merged `Stage14-s7-45`.

Stage14-4de subsequently produced a genuinely new exact bridge which was not available at that closure snapshot: on full-residual square-root saturation, the common core and first signed residual have only `B^o(1)` cross gcd and combine into a quarter-scale mixed fourth-root modulus

```text
Q_mix=C_*u_*=B^(1/4+o(1)),
t^2=-1 mod C_*,
t^2=+1 mod u_*,
t^4=1 mod Q_mix,
```

with the `C_*/u_*` prime-power allocation recovered from `(Q_mix,t)` by `gcd(Q_mix,t^2+1)` and `gcd(Q_mix,t^2-1)`.

Stage14-s7-46 consumes that reactivation and proves that the mixed-root tuple also reconstructs, with only `B^o(1)` fibers,

```text
first-residual sign allocation,
xi-switch product S*T,
xi-agreement product R*J,
first signed quotient/agreement pair,
second reciprocal / X13 physical completion.
```

The second reciprocal therefore has no independent fixed-power support. The exposed cofactors are

```text
M_+=oddpart(D^2+A^2)/C_* = S*T * B^o(1),
M_-=oddpart(D^2-A^2)/u_* = R*J * B^o(1).
```

Stage14-s7-47 peels the same-sign overlaps

```text
W_+=gcd(C_*,M_+),
W_-=gcd(u_*,M_-),
```

and proves that every fixed-power overlap block is strict sub-square-root. Possible square-root saturation therefore has the four norm blocks `C_*,M_+,u_*,M_-` pairwise separated at fixed-power scale.

Stage14-s7-48 exhausts the remaining elementary two-square algebra. With

```text
Z=D+iA,
m=D+A,
n=D-A,
```

the two complementary square identities become

```text
N(Z)=D^2+A^2=epsilon_+ C_* S T,
mn=D^2-A^2=epsilon_- u_* R J.
```

For fixed plus triple `(C_*,S,T)` or fixed minus triple `(u_*,R,J)`, the full physical completion is only `B^o(1)`, but each source triple has total exponent exactly `1/2`. The two-square elimination ideal among the product variables is trivial, so no second deterministic resultant or divisor switch beats the square-root bound.

The immutable Stage14-sH48 audit then verifies that no surveyed off-the-shelf theorem directly supplies a fixed-power saving for the positive product/norm correlation receiver. It returns

```text
OFF_THE_SHELF_THEOREM_APPLICABLE=false
CERTIFIED_B_POWER_SAVING_EXPONENT=0
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

and asks for an exact centered dispersion adapter rather than another uncentered theorem application.

Stage14-s7-49 constructs that adapter. Pairwise separation gives `gcd(C_*,mn)=1`, so

```text
1_{C_*|m^2+n^2}
 = r_-(C_*)/C_*
 + (1/C_*) sum_{rho^2=-1 mod C_*} sum_{h!=0 mod C_*}
     e_{C_*}(h(m-rho n)).
```

The first term is the exact local zero mode. Its `C_*^{-1}` density cancels the `B^chi` choice of `C_*`, reproducing the existing exponent `1/2` and identifying the square-root barrier with the principal local density.

For the nonzero modes, use the same physical product `P_-=mn` and `n=P_-*inverse(m) mod C_*` to obtain the exact inverse-fraction phase

```text
e_{C_*}(h*m-h*rho*P_-*inverse(m)).
```

Thus the missing Kloosterman/inverse-fraction adapter is proved. The remaining internal issue is conductor loss: for

```text
g=gcd(h,C_*),
q=C_*/g,
```

the phase reduces to effective modulus `q`, and the exact-conductor frequency multiplicity is `phi(q)`.

Stage14-s7-50 peels this conductor loss without an external theorem. For

```text
d=gcd(h,C_*),
q=C_*/d,
d=B^(lambda+o(1)),
```

the exact-conductor frequency block has normalized Fourier coefficient mass

```text
phi(q)/C_* <= q/C_* = 1/d.
```

Charging the merged s7-48 plus-side complete coordinate system `(C_*,S,T)` exactly once gives

```text
E_s7-50(lambda) <= 1/2-lambda.
```

Hence every fixed-power conductor loss is strict sub-square-root and possible saturation is confined to

```text
gcd(h,C_*)=B^o(1),
q=C_* B^o(1).
```

Merged X15 is compatible with this endpoint and must be retained. Its k-agreement projection gives the same root line in the equivalent form

```text
delta*s == -rho*alpha*r (mod q),
```

not a second independent modulus. X15 also proves that triple centering retains the principal term, three pairwise covariance terms, and the genuine triple covariance. Therefore an absolute power-saving bound for only the oscillatory full-conductor error cannot by itself beat the square-root principal density.

The frozen Stage14-sH50 audit now checks the full-conductor theorem landscape. It confirms that the old sH48 centering/conductor objections are resolved, but no surveyed theorem controls the **full physical principal-density plus covariance count** with a fixed power saving. Complete/incomplete Kloosterman theorems are cancellation tools for oscillatory errors; the required mask-preserving coefficient packaging is not yet proved, and even an ideal oscillatory error bound would leave the exponent-`1/2` principal term unless a new marginal-density loss or main-term-scale signed anti-correlation is supplied.

```text
STAGE14_SH50=COMPLETE
OFF_THE_SHELF_THEOREM_APPLICABLE=false
OSCILLATORY_ERROR_POWER_SAVING_CERTIFIED=false
PRINCIPAL_DENSITY_FIXED_POWER_LOSS_CERTIFIED=false
MAIN_TERM_SCALE_SIGNED_ANTICORRELATION_CERTIFIED=false
X15_ALL_COVARIANCE_TERMS_CONTROLLED=false
CERTIFIED_B_POWER_SAVING_EXPONENT=0
```

The sharpened receiver is

```text
FullConductorPrimitiveQuarterPythagoreanThreeProjectionConditionalPrincipalDensityAndSignedCovarianceCorrelation.
```

Current route state:

```text
S_ROUTE_CURRENT_STATE=ACTIVE_REACTIVATED
S_ROUTE_CLOSED_BY=Stage14-s7-45
S_ROUTE_REACTIVATION_TRIGGERED_BY=Stage14-4de
S_ROUTE_REACTIVATION_CONSUMED_BY=Stage14-s7-46
S_ROUTE_REACTIVATION_NEEDED=false
USER_DECIDES_S_ROUTE_REACTIVATION=false
ROADMAP_DECIDES_S_ROUTE_REACTIVATION=true
S_ROUTE_CURRENT_RECEIVER=FullConductorPrimitiveQuarterPythagoreanThreeProjectionConditionalPrincipalDensityAndSignedCovarianceCorrelation
S_ROUTE_BLOCKED_WAITING_FOR_H=false
S_ROUTE_AUXILIARY_H=Stage14-sH50_COMPLETE
S_ROUTE_NEXT=Stage14-s7-51
```

The user is **not** expected to decide whether the s-route should be restarted. Reactivation checks are relevant when the s route is CLOSED; while it is ACTIVE, downstream Stage14 work must preserve the current route state rather than overwrite it with an older snapshot.

When the s route is closed again, any later mainline, `t`, `X`, toolbox, q/literature, or other Stage14 stage that materially changes the surviving receiver must explicitly evaluate whether the new result creates a genuinely new s-specific exact structure or theorem bridge.

Required decision fields for such a material receiver change while s is CLOSED:

```text
MATERIAL_RECEIVER_CHANGE_REQUIRES_S_REACTIVATION_CHECK=true
S_ROUTE_REACTIVATION_NEEDED=true|false
```

If the answer is `true`, the same stage result or immediate roadmap update must also record

```text
S_ROUTE_REACTIVATION_TRIGGER=<exact new identity/theorem/bridge>
S_ROUTE_REACTIVATION_TARGET=<named next s stage>
S_ROUTE_REACTIVATION_REASON=<why the new structure is actionable in s coordinates>
```

and the roadmap must visibly tell the user that the s-route should be restarted.

Operational lock:

```text
S_REACTIVATION_REQUIRES_NEW_EXACT_STRUCTURE_OR_THEOREM_BRIDGE=true
S_REACTIVATION_REQUIRES_EXPLICIT_RECEIVER=true
S_REACTIVATION_MUST_BE_SURFACED_TO_USER_IN_ROADMAP=true
S_ROUTE_MUST_NOT_BE_RESTARTED_BY_USER_GUESS=true
NO_NEW_S_SPECIFIC_RECEIVER_MEANS_KEEP_S_CLOSED=true
```

## S-route final decision lock — s7-162 through s7-164 only

The S route has reached its square-root barrier without a certified strict sub-square-root saving. To prevent receiver renaming or routine XQ reclassification from becoming an unbounded continuation mechanism, the active S route is now under a **final bounded decision batch**.

Only the following stages may be executed under this lock:

```text
Stage14-s7-162
Stage14-s7-163
Stage14-s7-164
```

They must preserve the full physical packet and test the already isolated reduced-modulus/character receiver. They are not permission to introduce another receiver solely to continue the route. A new external theorem audit or sH unit may occur only when needed to decide the stated gate, must be frozen to its source snapshot, and counts within this three-stage decision budget.

After `Stage14-s7-164`, record exactly one terminal decision:

```text
S_FINAL_DECISION=CONTINUE|PARKED_EXTERNAL_GATE
S_FINAL_DECISION_EVIDENCE=<named proved result or named obstruction>
S_FINAL_DECISION_STAGE=Stage14-s7-164
```

`CONTINUE` is permitted only if the final batch proves at least one of:

```text
FULL_PHYSICAL_MAIN_TERM_DOMINANCE_PROVED=true
VALID_EXISTING_THEOREM_ADAPTER_PROVED=true
```

A proposed adapter must be a proved uniform, mask-preserving application to the full physical packet; a literature resemblance, an oscillatory-error estimate that leaves the principal density, or a receiver renaming does not qualify.

If neither condition is proved, the mandatory decision is:

```text
S_FINAL_DECISION=PARKED_EXTERNAL_GATE
S_ROUTE_CURRENT_STATE=PARKED_EXTERNAL_GATE
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_NEXT=NONE
S_ROUTE_RESTART_REQUIRES_NEW_EXACT_STRUCTURE_OR_THEOREM_BRIDGE=true
```

In that parked state, no `Stage14-s7-165` or later S stage, and no routine XQ/q follow-up, may be created. A later restart requires a material new exact structure or theorem bridge under the existing reactivation rule, with the exact bridge and a fresh target stage surfaced in the roadmap. XQ is reserved for one final **continue-or-park audit** after the `s7-164` decision; it must not run between `s7-162`, `s7-163`, and `s7-164`.

```text
S_FINAL_DECISION_BATCH_START=Stage14-s7-162
S_FINAL_DECISION_BATCH_END=Stage14-s7-164
S_FINAL_DECISION_BATCH_STAGE_COUNT=3
S_FINAL_DECISION_NO_RECEIVER_RENAMING_CONTINUATION=true
S_FINAL_DECISION_REQUIRES_FULL_PHYSICAL_PACKET=true
S_FINAL_DECISION_XQ_INTERMEDIATE_RUNS_FORBIDDEN=true
S_FINAL_DECISION_XQ_FINAL_AUDIT_ONLY=true
S_FINAL_DECISION_DEFAULT_IF_GATE_FAILS=PARKED_EXTERNAL_GATE
```

## Triple gate

The exact identity remains

\[
N_2(B)=E(B)-3T(B).
\]

A future raw-pair law cannot transfer to exactly-two until sufficiently strong triple control is proved, ideally `T(B)=o(sqrt(B))`.

## Auxiliary H / tH / sH theorem-audit protocol

All Stage14 auxiliary theorem/literature lanes are governed by [`H-PROTOCOL.md`](./H-PROTOCOL.md).

The operational rule is deliberately snapshot-based:

```text
ONE_H_REQUEST_ONE_SNAPSHOT=true
H_TARGET_FREEZES_AT_DISPATCH=true
RUNNING_H_CHASES_LATER_PARENT_STAGES=false
PARENT_ROUTE_MAY_CONTINUE_WHEN_H_NONBLOCKING=true
COMPLETED_H_MERGES_AS_SCOPED_SNAPSHOT_RESULT=true
LATER_RECEIVER_REQUIRING_AUDIT_USES_NEXT_H_NUMBER=true
```

A completed H result is a scoped certificate about its frozen source snapshot. Later parent progress does not rewrite it. If a materially different later receiver requires another theorem audit, use the next H number.

Prefer to start H from a merged source stage. If true parallelism is useful before the source merges, freeze the exact source head SHA, use a Draft/stacked H PR, and after the source merges perform only a mechanical retarget/rebase without changing the mathematical target.

## Scope boundary

No true Stage14 growth exponent, leading constant, family large-sieve theorem, uniform first-small-point lower-tail theorem, perfect-cuboid nonexistence theorem, or `T=o(sqrt(B))` theorem is established.

```text
NEXT=Stage14-4aq isolate the global-solubility/Sha retainer and formulate a uniform averaging target compatible with the centered local sieve
```
