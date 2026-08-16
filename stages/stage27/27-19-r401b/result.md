# Stage27-19-r401b — constant-u bisection physical-degeneration barrier

```text
TASK_ID=Stage27-19-r401b
OWNER_STAGE=Stage27
PARENT_ROUTE=Stage27-19-r401a
TRIGGER_CHECKPOINT=40
ROUTE_KIND=LOWER_REENTRY
ROUTE_LABEL=CONSTANT_U_BISECTION_HEIGHT_PREFLIGHT
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ADVANCE_TO_CHECKPOINT50=false
```

## 1. Audited parent boundary

Stage27-19-r401a passed hostile audit and PR #1032 merged at

```text
86b5428d42f7f4c7344bace93b067d580391d7ac
```

The accepted master receiver and natural genus-one fibration are

\[
x^2y^2+1=z^2(x^2+y^2),
\]

\[
\tau V^2=(u^2+\tau+1)
\Bigl((\tau+2)u^2-4(\tau+1)u+(\tau+1)(\tau+2)\Bigr),
\]

with

\[
D=u^2-\tau-1,
\]

\[
z=\frac{\tau+(u-1)^2}{D},
\qquad
x=\frac{2\tau u-\tau-u^2+2u-1}{D}.
\]

The parent proved that the generic fiber has no `Q(tau)` point. It also exhibited an algebraic degree-two closed point at `u=0`, but explicitly did not claim that this point is a physical Stage19 family or that it improves the lower exponent.

This route performs that missing physical check and then classifies every **constant rational** `u=c` bisection.

## 2. The parent `u=0` quadratic point is physically degenerate

At `u=0`,

\[
D=-\tau-1,
\qquad
z=-1,
\qquad
x=1.
\]

Hence

\[
\boxed{z^2=1,\qquad x^2=1.}
\]

This is exactly the nonphysical boundary excluded before the `tau`-fibration was introduced. In the toric Stage19 host, `x=m/n=1` forces `m=n` and kills the edge

\[
X=2rs(m^2-n^2).
\]

Therefore the explicit quadratic closed point from r401a is an algebraically valid point on the genus-one fiber but **not** a nondegenerate Stage19 object.

Likewise, at `u=1`,

\[
D=-\tau,
\qquad z=-1,
\qquad x=-1,
\]

so it is again on `z^2=1`.

```text
R401A_U0_DEGREE2_POINT_ALGEBRAIC=true
R401A_U0_DEGREE2_POINT_PHYSICAL=false
U0_PHYSICAL_DEGENERACY=z^2=1,x^2=1
U1_PHYSICAL_DEGENERACY=z^2=1,x^2=1
```

## 3. Exact constant-u bisection curve

Fix any rational constant

\[
u=c\in\mathbf Q.
\]

The fiber equation becomes

\[
\tau V^2=(\tau+c^2+1)
\Bigl(\tau^2+(c-1)(c-3)\tau+2(c-1)^2\Bigr).
\]

After setting `S=tau V`, the degree-two cover of the `tau`-line is

\[
\boxed{
S^2=H_c(\tau)
:=\tau(\tau+c^2+1)
\Bigl(\tau^2+(c-1)(c-3)\tau+2(c-1)^2\Bigr).
}
\]

This is the exact constant-`u` bisection receiver. No physical height estimate is used yet.

```text
CONSTANT_U_BISECTION_RECEIVER_DERIVED=true
CONSTANT_U_BISECTION_DEGREE_OVER_TAU=2
```

## 4. Exact discriminant and genus classification

A direct resultant calculation gives

\[
\boxed{
\operatorname{Disc}_{\tau}(H_c)
=64c^6(c-1)^6(c^2+1)^2(c^2-6c+1).
}
\]

For rational `c`, the factors `c^2+1` and `c^2-6c+1` have no rational roots: the latter has discriminant `32`, so its roots are `3+-2sqrt(2)`.

Therefore for

\[
\boxed{c\in\mathbf Q\setminus\{0,1\}}
\]

the quartic `H_c` is squarefree. Its smooth projective double cover is a genus-one curve.

The only rational constant-`u` degenerations are exactly `c=0` and `c=1`, and Section 2 shows that both are on the excluded physical boundary `z^2=1`.

Thus

\[
\boxed{
\text{every nondegenerate rational constant-}u\text{ bisection is genus one.}
}
\]

In particular, no nondegenerate constant rational `u=c` produces a rationally parametrized degree-two multisection over the `tau`-line.

This is a route-specific statement. It does not classify nonconstant `u(tau)` multisections.

```text
CONSTANT_U_BISECTION_DISCRIMINANT_PROVED=true
CONSTANT_U_NONDEGENERATE_GENUS_ONE=true
CONSTANT_U_RATIONAL_GENUS_ZERO_PHYSICAL_ROUTE_EXISTS=false
CONSTANT_U_ROUTE_CLOSED_AS_RATIONAL_PARAMETRIC_ESCAPE=true
```

## 5. The obvious affine-linear genus-zero line is also boundary

The reconstruction formula itself gives an exact physical-boundary identity:

\[
z=1
\iff
u=\tau+1
\]

away from denominator-zero charts, while

\[
z=-1
\iff
u=0\text{ or }1.
\]

On the affine-linear line `u=tau+1`, the bisection equation collapses to

\[
S^2=\tau^3(\tau+1)^2(\tau+2),
\]

whose squarefree reduction is the rational conic

\[
W^2=\tau(\tau+2).
\]

But the entire line has `z=1`, hence `z^2=1`, so this genus-zero collapse is again nonphysical.

This observation is not promoted to a classification of all affine-linear `u=a tau+b`. It only removes the most immediate moving genus-zero escape found by the split coordinates.

```text
BOUNDARY_LINE_U_EQ_TAU_PLUS_1_PROVED=true
BOUNDARY_LINE_U_EQ_TAU_PLUS_1_GENUS_ZERO=true
BOUNDARY_LINE_U_EQ_TAU_PLUS_1_PHYSICAL=false
ALL_AFFINE_LINEAR_MULTISECTIONS_CLASSIFIED=false
```

## 6. Lower-bound consequence

The parent lower progress gate remains

\[
\boxed{\kappa/h>1/4}.
\]

r401b proves no new exponent. Its contribution is structural:

1. the explicit algebraic degree-two point from r401a does not survive the physical nondegeneracy filter;
2. every fixed rational nondegenerate constant-`u` bisection is genus one, not a rational curve;
3. the simplest affine-linear genus-zero collapse `u=tau+1` is also entirely on the excluded boundary.

Therefore a stronger lower family cannot come merely from choosing a constant rational `u` in the natural bisection, nor from the obvious boundary line `u=tau+1`.

The next executable lower route is to allow a genuinely moving low-degree function

\[
u(\tau)=a\tau+b
\]

or another low-degree multisection, classify the resulting double-cover genus and then pass every surviving rational/genus-zero candidate through the exact physical height and primitive/canonical/exactly-two adapters.

## 7. Scope firewall

- No `beta>1/4` lower is proved.
- No matching half-power lower is proved.
- No claim is made that all degree-two multisections are genus one.
- No claim is made that the master surface is nonrational.
- No moving-`u` affine-linear classification is claimed.
- No finite search is used as an asymptotic theorem.
- No perfect-cuboid existence/nonexistence conclusion is drawn.

```text
STAGE27_19_R401B_ATTACK_EXECUTED=true
PARENT_R401A_AUDITED_PASS_MERGED=true
R401A_U0_DEGREE2_POINT_PHYSICAL=false
CONSTANT_U_BISECTION_DISCRIMINANT_PROVED=true
CONSTANT_U_NONDEGENERATE_GENUS_ONE=true
CONSTANT_U_RATIONAL_GENUS_ZERO_PHYSICAL_ROUTE_EXISTS=false
BOUNDARY_LINE_U_EQ_TAU_PLUS_1_PHYSICAL=false
ALL_AFFINE_LINEAR_MULTISECTIONS_CLASSIFIED=false
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_DERIVED_ROUTE=27-19-r401c
NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit
```
