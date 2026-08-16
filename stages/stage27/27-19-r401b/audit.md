# Stage27-19-r401b — hostile audit

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
STAGE27_19_R401B_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
```

## Scope

Hostile audit of PR #1033 / Stage27-19-r401b. This is a lower-reentry intermediate audit. It does not close Stage27 checkpoint40, does not improve the current global lower exponent above `1/4`, and does not identify the true `N2` exponent.

## 1. r401a degree-two point: physical check

Accepted. Using the audited reconstruction

\[
D=u^2-\tau-1,\qquad
z=\frac{\tau+(u-1)^2}{D},\qquad
x=\frac{2\tau u-\tau-u^2+2u-1}{D},
\]

one gets identically

\[
u=0\Rightarrow (x,z)=(1,-1),\qquad
u=1\Rightarrow (x,z)=(-1,-1).
\]

Thus both lie on `z^2=1`; at `u=0`, `x=m/n=1` also gives `m=n` and kills the toric edge `X=2rs(m^2-n^2)`. Therefore the algebraic degree-two point exhibited in r401a is not a nondegenerate Stage19 object.

```text
R401A_U0_DEGREE2_POINT_ALGEBRAIC=true
R401A_U0_DEGREE2_POINT_PHYSICAL=false
U0_U1_PHYSICAL_BOUNDARY_ACCEPTED=true
```

## 2. Constant-u bisection discriminant and genus

Accepted. For `u=c in Q`, the exact double cover is

\[
S^2=H_c(\tau)=\tau(\tau+c^2+1)\bigl(\tau^2+(c-1)(c-3)\tau+2(c-1)^2\bigr).
\]

Independent symbolic recomputation gives

\[
\operatorname{Disc}_{\tau}(H_c)
=64c^6(c-1)^6(c^2+1)^2(c^2-6c+1).
\]

For rational `c`, `c^2+1` has no rational zero and `c^2-6c+1` has discriminant `32`, hence no rational zero. Therefore the only rational discriminant-zero values are `c=0,1`; both are the nonphysical boundary above. Every rational `c!=0,1` gives a squarefree quartic and hence a smooth genus-one double cover.

This proves only the constant-rational-u classification. It does not classify nonconstant multisections.

```text
CONSTANT_U_BISECTION_DISCRIMINANT_ACCEPTED=true
CONSTANT_U_RATIONAL_DEGENERATIONS=0,1
CONSTANT_U_NONDEGENERATE_GENUS_ONE_ACCEPTED=true
CONSTANT_U_RATIONAL_GENUS_ZERO_PHYSICAL_ROUTE_EXISTS=false
CONSTANT_U_ROUTE_CLOSED_AS_RATIONAL_PARAMETRIC_ESCAPE=true
```

## 3. Obvious moving boundary line

Accepted. Away from denominator-zero charts the reconstruction gives

\[
z=1\iff u=\tau+1,
\qquad
z=-1\iff u=0\text{ or }1.
\]

For `u=tau+1`, the double cover reduces to

\[
S^2=\tau^3(\tau+1)^2(\tau+2),
\]

with squarefree reduction `W^2=tau(tau+2)`, but the entire line has `z=1` and is therefore nonphysical. This does not classify general affine-linear `u=a tau+b`.

```text
BOUNDARY_LINE_U_EQ_TAU_PLUS_1_ACCEPTED=true
BOUNDARY_LINE_U_EQ_TAU_PLUS_1_PHYSICAL=false
ALL_AFFINE_LINEAR_MULTISECTIONS_CLASSIFIED=false
```

## 4. Lower-bound consequence and continuation

No new lower exponent is proved. The accepted parent gate remains

\[
\kappa/h>1/4.
\]

r401b closes the constant-u rational-parametric shortcut and the obvious boundary line only. The next legitimate lower-side route is `27-19-r401c`: classify genuinely moving affine-linear/low-degree multisections and, for any surviving rational/genus-zero candidate, perform the exact physical-height, primitive, canonical, exactly-two and multiplicity audit before any exponent promotion.

```text
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
MASTER_SURFACE_RATIONALITY_DISPROVED=false
ALL_DEGREE_TWO_MULTISECTIONS_CLASSIFIED=false
CONTINUE_LOWER_EXPLORATION_AFTER_PASS=true
NEXT_DERIVED_ROUTE=27-19-r401c
```

## 5. CI / lifecycle

Submission head `531ad3eef372204a41f859d545dcbcf4386827ea` has SUCCESS for the dedicated `Stage27-19-r401b constant-u bisection barrier` workflow and relevant Stage27 regressions, including r401/r401a, checkpoint40, 40aa/40ad/40ae, 30, 20 and 10. The recurring Stage25 phase10 and Stage15-8 failures are historical lifecycle regressions and are not mathematical blockers for r401b.

```text
DEDICATED_STAGE27_19_R401B_CI_SUBMISSION_HEAD=SUCCESS
AUDIT_CLOSE_STAGE=false
ADVANCE_TO_CHECKPOINT50=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=merge PR #1033; then continue Stage27 checkpoint40 exploration
```
