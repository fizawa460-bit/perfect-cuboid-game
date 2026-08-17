# Stage27-20-r301n — the fixed-q1 delta family has one common Jacobian

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301m
SOURCE_STAGE=Stage20

## 1. Start from the audited intersection of quadrics

For fixed physical `x=q1>1` and squareclass `delta>0`, r301i gives

\[
C_{x,\delta}:\qquad
Y^2+x^2T^2=\delta R^2,
\qquad
x^2Y^2+T^2=\delta S^2.
\]

For the pencil `lambda Q1 + mu Q2`, the determinant is

\[
\boxed{
\det(\lambda Q_1+\mu Q_2)
=\delta^2\lambda\mu
(\lambda+\mu x^2)(\lambda x^2+\mu).
}
\]

The crucial point for the moving-squareclass problem is that `delta` occurs only through the square factor `delta^2`.

For a smooth complete intersection of two quadrics in `P^3`, the determinant binary quartic gives the standard discriminant double cover whose elliptic curve is the Jacobian of the genus-one intersection. Multiplying that binary quartic by a rational square does not change the resulting elliptic curve over `Q`. Therefore

\[
\boxed{
\operatorname{Jac}(C_{x,\delta})
\cong_{\mathbf Q}
\operatorname{Jac}(C_{x,1})
\quad\text{for every physical }\delta.
}
\]

Thus the squareclass parameter does **not** produce a moving family of Jacobian quadratic twists. It changes the genus-one covering/model while the Jacobian is fixed once `x` is fixed.

## 2. Explicit Legendre representative

Put `r=lambda/mu`. The four roots of the determinant quartic are

\[
0,\quad \infty,\quad -x^2,\quad -x^{-2}.
\]

With

\[
X=-\frac{r}{x^2},
\]

the branch set becomes

\[
0,\quad\infty,\quad1,\quad x^{-4}.
\]

Up to the fixed sign convention in the determinant model, one convenient rational representative is therefore

\[
\boxed{
E_x:\quad W^2=-X(X-1)(X-x^{-4}).
}
\]

The sign is fixed and independent of `delta`; it is irrelevant to the delta-independence claim and leaves the rational 2-torsion visible.

For reduced

\[
x=\frac ab,\qquad a>b>0,\qquad (a,b)=1,
\]

clearing denominators by `U=a^4 X`, `V=a^6 W` gives

\[
\boxed{
E_{a,b}:\quad
V^2=-U(U-a^4)(U-b^4).
}
\]

Hence

\[
E_{a,b}[2](\mathbf Q)
=\{\mathcal O,(0,0),(a^4,0),(b^4,0)\}.
\]

The displayed integral model has discriminant

\[
\boxed{
\Delta_{a,b}=16a^8b^8(a^4-b^4)^2
}
\]

(up to the standard harmless convention for the sign of the cubic), so its bad-prime support is contained in

\[
\boxed{\{p:p\mid 2ab(a^4-b^4)\}}.
\]

Its `j`-invariant is exactly the audited r301k function

\[
\boxed{
j(x)=256\frac{(x^8-x^4+1)^3}{x^8(x^4-1)^2}.
}
\]

## 3. What this changes

R301i used a pointwise rank notation that was allowed to depend on `(x,delta)`. The determinant-penc\-il calculation sharpens the structure:

\[
\boxed{r_{x,\delta}=r_x:=\operatorname{rank}E_x(\mathbf Q)}
\]

for every soluble/physical fiber, because all those fibers have the same Jacobian.

This is a real compression of the arithmetic obstruction: the moving squareclass parameter can still affect the covering and height constants, but it does not create a new Mordell--Weil group or a new rank for each `delta`.

## 4. Scope firewall

This route does **not** prove that rational-point heights on all soluble `C_{x,delta}` are uniformly comparable with the Neron--Tate height on `E_x`. It therefore does not by itself promote the old pointwise fiber bound to a moving uniform estimate.

```text
STAGE27_20_R301N_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
DETERMINANT_PENCIL_DELTA_SQUARE_FACTOR_PROVED=true
COMMON_JACOBIAN_INDEPENDENT_OF_DELTA_PROVED=true
COMMON_JACOBIAN_FULL_RATIONAL_2_TORSION=true
COMMON_JACOBIAN_INTEGRAL_MODEL=V^2=-U(U-a^4)(U-b^4)
COMMON_JACOBIAN_DISCRIMINANT=16*a^8*b^8*(a^4-b^4)^2
MORDELL_WEIL_RANK_DEPENDS_ON_DELTA=false
UNIFORM_COVERING_HEIGHT_TRANSFER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301o
```
