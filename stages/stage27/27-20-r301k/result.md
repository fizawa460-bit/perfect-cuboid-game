# Stage27-20-r301k — explicit moduli map and geometric twist split

STATUS=AUDITED_PASS_MERGED
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301j
SOURCE_STAGE=Stage20

## 1. Start from the audited fixed-fiber quartic

For physical `x=q1>1` and squarefree `delta>0`, r301i gives

\[
\delta V^2=
\bigl(\delta z^2-(x^2+1)^2\bigr)
\bigl(\delta z^2-(x^2-1)^2\bigr).
\]

Over `Q(sqrt(delta))`, put

\[
Z=\sqrt\delta\,z,\qquad W=\sqrt\delta\,V.
\]

Then

\[
\boxed{
W^2=(Z^2-(x^2+1)^2)(Z^2-(x^2-1)^2).
}
\]

Thus after adjoining `sqrt(delta)` the curve depends only on `x`.  In particular `delta` is geometric twist data; it does not move the geometric moduli parameter.

## 2. Explicit j-invariant

R301i exhibited the branch cross-ratio

\[
\lambda=x^{-4}.
\]

For a Legendre cross-ratio, the invariant is

\[
j(\lambda)=256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2}.
\]

Substituting `lambda=x^-4` gives

\[
\boxed{
j(x)=256\frac{(x^8-x^4+1)^3}{x^8(x^4-1)^2}.}
\]

Hence the geometric isomorphism class varies only through `x`; `delta` changes the arithmetic twist above that moduli point.

## 3. Physical multiplicity of the moduli map

For `x>1`,

\[
0<\lambda=x^{-4}<1.
\]

The six Legendre cross-ratio transforms with the same `j` are

\[
\lambda,\ 1-\lambda,\ 1/\lambda,\ 1/(1-\lambda),\
\lambda/(\lambda-1),\ (\lambda-1)/\lambda.
\]

Only `lambda` and `1-lambda` lie in `(0,1)`.  Since positive physical `x` is uniquely recovered from `lambda` by `x=lambda^{-1/4}`, a fixed `j` has at most two physical `x`-values:

\[
\boxed{\#\{x>1:j(x)=j_0\}\le2.}
\]

This is a bounded-to-one reparametrization, not a new support saving.

## 4. Scope firewall

No rank bound, conductor formula, or uniform rational-point theorem follows merely from the explicit moduli map.

```text
STAGE27_20_R301K_STATUS=AUDITED_PASS_MERGED
J_INVARIANT_FORMULA_PROVED=true
J_INVARIANT=256*(x^8-x^4+1)^3/(x^8*(x^4-1)^2)
J_DEPENDS_ONLY_ON_X=true
DELTA_GEOMETRIC_TWIST_ONLY=true
PHYSICAL_J_FIBER_MULTIPLICITY_LE_2=true
J_MAP_SUPPORT_SAVING_PROVED=false
UNIFORM_MOVING_FIBER_SUBPOWER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301l
```
