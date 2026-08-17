# Stage27-20-r301q — explicit two-to-one elliptic receiver gives uniform polynomial height transfer

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301p
SOURCE_STAGE=Stage20

## 1. Start from the audited fixed `(x,delta)` quartic

Let `x=q1=a/b>1` be reduced and let `delta>0` be the common positive squarefree class.  Stage27-20-r301i gives the birational quartic

\[
\delta V^2=
\bigl(\delta z^2-(x^2+1)^2\bigr)\cdot
\bigl(\delta z^2-(x^2-1)^2\bigr).
\]

Put

\[
A=(x^2+1)^2,\qquad B_0=(x^2-1)^2,
\]

and define

\[
\boxed{X=\delta z^2,\qquad Y=\delta zV.}
\]

Then directly

\[
Y^2
=\delta^2z^2V^2
=(\delta z^2)\,\delta V^2
=X(X-A)(X-B_0).
\]

Hence every rational point on the quartic maps to the elliptic curve

\[
\boxed{
E_x^\sharp:\quad Y^2=X\bigl(X-(x^2+1)^2\bigr)\bigl(X-(x^2-1)^2\bigr).
}
\]

This curve depends on `x` but **not** on `delta` and has full rational `2`-torsion.

The map has degree at most two on rational points: away from the finite locus `X=0`, a target point determines `z^2=X/delta`, and any rational lift has at most the two signs `z=+-sqrt(X/delta)`; then `V=Y/(delta z)` is forced.  The finite exceptional locus contributes only `O(1)` points.  Therefore

\[
\boxed{w_{x,\delta}(B)\le 2N_{E_x^\sharp}(H_*)+O(1)}
\]

once a common target height cutoff `H_*` for physical images is supplied.

## 2. Integral model and curve height

For reduced `x=a/b`, set

\[
\alpha=(a^2+b^2)^2,\qquad
\beta=(a^2-b^2)^2.
\]

With

\[
U=b^4X,\qquad W=b^6Y,
\]

the target becomes the integral model

\[
\boxed{
\mathcal E_{a,b}:\quad
W^2=U(U-\alpha)(U-\beta).
}
\]

Expanding,

\[
W^2=U^3-(\alpha+\beta)U^2+\alpha\beta U,
\]

where

\[
\alpha+\beta=2(a^4+b^4),\qquad
\alpha\beta=(a^4-b^4)^2.
\]

The physical height bound from r301h gives `H(x)<=2B`, hence `a,b<=2B`.  Consequently the naive coefficient height of this Weierstrass equation satisfies

\[
\boxed{H(\mathcal E_{a,b})\ll B^8.}
\]

The three rational `2`-torsion points are

\[
(0,0),\qquad (\alpha,0),\qquad (\beta,0).
\]

## 3. Uniform polynomial height of physical images

For a physical source point, r301h gives

\[
H(x),H(y)\ll B.
\]

The squareclass support theorem gives

\[
\delta_{\rm odd}\mid\operatorname{rad}(a^4-b^4),
\]

and the two-adic choice contributes at most one factor `2`; therefore

\[
\boxed{\delta\ll B^4.}
\]

From

\[
x^2+y^2=\delta r^2,
\qquad
x^2y^2+1=\delta s^2,
\]

standard rational-height arithmetic gives absolute constants `C1,C2` such that

\[
H(r),H(s)\le B^{C_1}.
\]

In the r301i chart

\[
z=s+xr,
\]

so

\[
H(z)\le B^{C_2}.
\]

The explicit receiver has

\[
U=b^4\delta z^2,
\]

and therefore there is an **absolute** constant `K0` such that every physical image satisfies

\[
\boxed{H(U)\le B^{K_0}.}
\]

No basepoint-dependent torsor-to-Jacobian height comparison is used here.  The polynomial transfer follows from the explicit rational map itself.

## 4. Consequence and scope firewall

The previous r301o obstruction `UNIFORM_COVERING_HEIGHT_TRANSFER_PROVED=false` is resolved at the level actually needed for counting: physical points admit a bounded-degree map, with bounded fibers, into one `delta`-independent elliptic curve per fixed `x`, and the target Weil height is bounded by a fixed power of `B` uniformly in all moving `x,delta`.

This route alone does not count target rational points.  The next route tests a uniform rational-point theorem for elliptic curves with rational `2`-torsion.

```text
STAGE27_20_R301Q_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
EXPLICIT_DELTA_INDEPENDENT_ELLIPTIC_RECEIVER_PROVED=true
ELLIPTIC_RECEIVER_MAP_DEGREE_AT_MOST_2=true
ELLIPTIC_RECEIVER_FULL_RATIONAL_2_TORSION=true
ELLIPTIC_RECEIVER_INTEGRAL_MODEL=W^2-U(U-(a^2+b^2)^2)(U-(a^2-b^2)^2)
ELLIPTIC_RECEIVER_CURVE_HEIGHT_POLYNOMIAL=B^8
PHYSICAL_IMAGE_WEIL_HEIGHT_POLYNOMIAL_UNIFORM=true
UNIFORM_COVERING_HEIGHT_TRANSFER_PROVED=true
UNIFORM_FIXED_X_AGGREGATE_SUBPOWER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301r
```
