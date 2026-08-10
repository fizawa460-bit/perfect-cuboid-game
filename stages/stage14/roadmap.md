# Stage14 roadmap — exactly-two integral-face population

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

The second reciprocal therefore has no independent fixed-power support. The newly exposed exact receiver is the simultaneous balanced squarefree two-cell factorization of the complementary cofactors

```text
M_+=oddpart(D^2+A^2)/C_* = S*T * B^o(1),
M_-=oddpart(D^2-A^2)/u_* = R*J * B^o(1).
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
S_ROUTE_CURRENT_RECEIVER=SquareRootQuarterScaleMixedFourthRootDualBalancedXiCofactorSplitPhysicalAdmissibilityDensity
S_ROUTE_NEXT=Stage14-s7-47
```

The user is **not** expected to decide whether the s-route should be restarted. Any later mainline, `t`, `X`, toolbox, q/literature, or other Stage14 stage that materially changes the surviving receiver must explicitly evaluate whether the new result creates a genuinely new s-specific exact structure or theorem bridge.

Required decision fields for any such material receiver change:

```text
MATERIAL_RECEIVER_CHANGE_REQUIRES_S_REACTIVATION_CHECK=true
S_ROUTE_REACTIVATION_NEEDED=true|false
```

If the answer is `true`, the same stage result or immediate roadmap update must also record:

```text
S_ROUTE_REACTIVATION_TRIGGER=<exact new identity/theorem/bridge>
S_ROUTE_REACTIVATION_TARGET=<named next s stage>
S_ROUTE_REACTIVATION_REASON=<why the new structure is actionable in s coordinates>
```

and the roadmap must visibly tell the user that the s-route should be restarted. A new route name by itself, a stronger global exponent by itself, or a theorem with merely similar notation is not enough: an explicit bridge back to an s-specific receiver is required.

If a later stage answers `false`, s remains in its then-current state and no s stage should be scheduled merely to re-audit an already exhausted obstruction.

Operational lock:

```text
S_REACTIVATION_REQUIRES_NEW_EXACT_STRUCTURE_OR_THEOREM_BRIDGE=true
S_REACTIVATION_REQUIRES_EXPLICIT_RECEIVER=true
S_REACTIVATION_MUST_BE_SURFACED_TO_USER_IN_ROADMAP=true
S_ROUTE_MUST_NOT_BE_RESTARTED_BY_USER_GUESS=true
NO_NEW_S_SPECIFIC_RECEIVER_MEANS_KEEP_S_CLOSED=true
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

In particular, once `tH23` (or any other H stage) starts, later `t82/t83/...` work must not repeatedly rewrite the `tH23` target. The H result is merged as a certificate about its recorded source snapshot. If later reductions expose a materially different receiver that needs another external audit, open `tH24` rather than revising `tH23`.

Prefer to start H from a merged source stage. If true parallelism is useful before the source merges, freeze the exact source head SHA, use a Draft/stacked H PR, and after the source merges perform only a mechanical retarget/rebase without changing the mathematical target.

The only normal reason to cancel a running snapshot audit is a substantive mathematical invalidation of its source stage; a stronger later reduction or a newer global exponent is not invalidation.

## Scope boundary

No true Stage14 growth exponent, leading constant, family large-sieve theorem, uniform first-small-point lower-tail theorem, perfect-cuboid nonexistence theorem, or `T=o(sqrt(B))` theorem is established.

```text
NEXT=Stage14-4aq isolate the global-solubility/Sha retainer and formulate a uniform averaging target compatible with the centered local sieve
```
