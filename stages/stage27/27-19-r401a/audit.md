# Stage27-19-r401a — hostile audit

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
STAGE27_19_R401A_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
```

## Scope

Hostile audit of PR #1032 / Stage27-19-r401a. This audit is lower-reentry only. It does not close the active Stage27 checkpoint40 program, does not improve the global lower exponent above `1/4`, and does not identify the true `N2` exponent.

## 1. Split factorization and conic parameterization

Accepted. The parent receiver

\[
x^2y^2+1=z^2(x^2+y^2)
\]

is equivalent to

\[
(x^2-z^2)(y^2-z^2)=z^4-1.
\]

On the physical nondegenerate chart `z^2 != 1`, defining

\[
\tau=(x^2-z^2)/(z^2-1)
\]

gives the two exact square relations used in the submission. The first conic has the rational point `(1,1)` and the displayed `u`-parameterization substitutes correctly. The second square condition becomes

\[
\tau V^2=(u^2+\tau+1)\bigl((\tau+2)u^2-4(\tau+1)u+(\tau+1)(\tau+2)\bigr).
\]

```text
MASTER_SPLIT_FACTORIZATION_ACCEPTED=true
FIRST_CONIC_PARAMETRIZATION_ACCEPTED=true
GENERIC_FIBER_QUARTIC_MODEL_ACCEPTED=true
```

## 2. Smooth genus-one and nonisotriviality

Accepted. Independent algebraic recomputation gives the branch-polynomial discriminant

\[
\Delta=4096\tau^2(\tau+1)^8.
\]

At `tau=-2` the affine polynomial drops to degree three but has cubic discriminant `1024`; the fourth branch point is the simple point at infinity, so the binary-quartic/projective discriminant remains nonzero. Hence all physical `tau != 0,-1` fibers are smooth genus one.

The binary-quartic invariants are

\[
I=16(\tau+1)^2(\tau^2+\tau+1),
\]

\[
J=64(\tau-1)(\tau+1)^3(\tau+2)(2\tau+1),
\]

and `J^2/I^3` is nonconstant. Therefore the associated Jacobian family has nonconstant `j`, and the genus-one fibration is nonisotrivial.

```text
BINARY_QUARTIC_DISCRIMINANT_ACCEPTED=true
PHYSICAL_GENERIC_FIBER_SMOOTH_ACCEPTED=true
PHYSICAL_GENERIC_FIBER_GENUS=1
GENUS_ONE_FIBRATION_NONISOTRIVIAL_ACCEPTED=true
```

## 3. Tau-adic local obstruction

Accepted. Over `K0=Q((tau))`, the left side has odd valuation `1+2v(V)`. For the right side:

- if `v(u)<0`, both quadratic factors have valuation `2v(u)`, giving total `4v(u)`;
- if `v(u)>=0` and residue `u0 != 1`, reduction gives `2(u0^2+1)(u0-1)^2`, a nonzero rational residue;
- if `u=1+w`, `v(w)>0`, the second factor is `tau^2-2tau w+(tau+2)w^2`; for `v(w)>1` it has valuation exactly `2`, while for `v(w)=1` its `tau^2` coefficient is `1-2a+2a^2=((2a-1)^2+1)/2`, never zero over `Q`.

Thus every affine RHS valuation is even. At infinity, a point would require

\[
Y^2=(\tau+2)/\tau,
\]

whose valuation is `-1`, so it is not a square in `Q((tau))`. Therefore

\[
C_\tau(Q((\tau)))=\varnothing,
\qquad C_\tau(Q(\tau))=\varnothing.
\]

Hence this specific natural `tau`-fibration has no rational section.

```text
TAU_ADIC_LOCAL_OBSTRUCTION_ACCEPTED=true
GENERIC_FIBER_QTAU_POINT_EXISTS=false
GENERIC_RATIONAL_SECTION_EXISTS=false
DEGREE1_SECTION_ROUTE_CLOSED=true
```

## 4. Degree-two escape and scope firewall

Accepted. At `u=0`, adjoining `sqrt((tau+2)/tau)` gives a genuine quadratic generic point because the squareclass has odd `tau`-adic valuation. This exhibits a degree-two closed point/multisection candidate, but does not determine its physical height or imply a better lower exponent.

The submission correctly does not claim that the master surface is nonrational in all birational models, does not classify all multisections or Stage19 parametrizations, and does not promote the torsor obstruction to global `1/4` optimality.

```text
GENERIC_DEGREE2_CLOSED_POINT_EXHIBITED=true
ALL_MULTISECTIONS_CLASSIFIED=false
ALL_STAGE19_PARAMETRIZATIONS_CLASSIFIED=false
MASTER_SURFACE_RATIONALITY_DISPROVED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
```

## 5. CI / lifecycle

Submission head `63a5641b7eb21258551890a5d9b95c5078229238` has SUCCESS for the dedicated `Stage27-19-r401a genus-one torsor barrier` workflow and relevant Stage27 regressions, including r401, checkpoint40, 40aa, 40ad, 40ae, 30, 20, and 10. The recurring Stage25 phase10 / Stage15-8 failures are unrelated historical lifecycle regressions and are not blockers for this lower-reentry mathematics.

```text
DEDICATED_STAGE27_19_R401A_CI_SUBMISSION_HEAD=SUCCESS
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CONTINUE_LOWER_EXPLORATION_AFTER_PASS=true
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_DERIVED_ROUTE=27-19-r401b
NEXT_EXPECTED_COMMAND=merge PR #1032; then continue Stage27 checkpoint40 exploration
```
