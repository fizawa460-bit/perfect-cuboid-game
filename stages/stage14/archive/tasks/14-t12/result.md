# Stage14-t12 — reflected square conditioned on a raw physical point

## Purpose

Stage14-t11 fixed the correct global object: a triple requires the **same physical rational coordinate** `q` to be a small point on both reflected quotient families. This stage conditions on an already-existing raw physical point and isolates the exact additional algebraic gate imposed by the reflected square.

No statistical independence and no `T(B)=o(sqrt(B))` statement is assumed.

## Physical notation

Let

\[
s=t^2,\qquad h^2=1+t^2,
\]

with physical rational `t,h`, and

\[
A=\frac{1-s}{1+s}.
\]

A raw physical point satisfies

\[
W^2=q^4+2Aq^2+1.
\]

By Stage14-t7, the reflected square is equivalent to

\[
R^2-W^2=\frac{4q^2}{s(1+s)}
=\left(\frac{2q}{th}\right)^2.
\]

Thus, **after conditioning on `(t,h,q,W)`**, the remaining triple gate is exactly that

\[
\left(W,\frac{2q}{th},R\right)
\]

is a rational right triangle.

## Rational conic parameter

Assume `qW != 0`, as in the genuine physical locus. Introduce the standard rational Pythagorean parameter `r` by

\[
W=\frac{2q}{th}\frac{1-r^2}{2r}
=\frac{q(1-r^2)}{thr},
\]

\[
R=\frac{2q}{th}\frac{1+r^2}{2r}
=\frac{q(1+r^2)}{thr}.
\]

Conversely, every rational solution of the reflected conic with nonzero second leg is represented by rational `r` (up to the usual reciprocal/sign symmetries). Therefore the reflected-square indicator, conditioned on the raw point, is equivalent to existence of such an `r` compatible with the raw quartic.

Substituting the expression for `W` into the raw quartic and writing

\[
y=q^2
\]

gives the exact quadratic equation

\[
\boxed{
 y^2 + B_{t,r}y + 1 = 0,
}
\]

where

\[
\boxed{
B_{t,r}
=2\frac{1-t^2}{1+t^2}
-\frac{(1-r^2)^2}{t^2(1+t^2)r^2}.
}
\]

Hence a compatible triple point must satisfy **two nested conditions**:

1. the quadratic in `y` has a rational root;
2. that root is itself a rational square `y=q^2` in the physical height window.

The first condition is the discriminant-square condition

\[
\boxed{
D_{t,r}=B_{t,r}^2-4 \in \mathbf Q^{\times 2}.
}
\]

The second is strictly stronger and must not be dropped.

## Conditional counting interpretation

Let `R_B` denote raw physical small objects `(F,q)` under the Stage14 height cutoff and let `P_B` be the compatible paired objects from t11. Then

\[
P(B)=\sum_{(F,q)\in R_B}
1_{\mathrm{refl}}(F,q).
\]

Stage14-t12 rewrites the conditional indicator as

\[
1_{\mathrm{refl}}(F,q)
=1_{\exists r\in\mathbf Q:\; y=q^2\text{ solves }y^2+B_{t_F,r}y+1=0}.
\]

Thus the missing theorem is not a local residue product. It is an averaged rational-point theorem on the explicit `(t,r)` discriminant-square cover, with the additional requirement that the selected quadratic root be a rational square and obey the physical height cutoff.

This provides a concrete bridge from the t11 genus-5 fiber-product formulation to a lower-dimensional auxiliary cover.

## Relation to the main/s tracks

Stage14-4am shows that, on the raw family, most observed finite thinning occurs at the first-small-point gate after positive rank. Stage14-s5c supplies explicit local Hilbert rows for the raw full-2-descent classes. Those results govern the population `R_B` on which the t12 conditional average is taken.

The t-track contribution is now isolated cleanly: **given a raw small point, how often does the associated `(t,q)` admit a rational `r` satisfying the discriminant-square plus square-root condition above?**

No claim is made that the `r`-cover is independent of the raw descent data.

## What would suffice

Any theorem of the form

\[
\sum_{(F,q)\in R_B}1_{\mathrm{refl}}(F,q)
=o(\sqrt B)
\]

directly proves the desired triple-object bound. A relative form

\[
\frac{P(B)}{|R_B|}\to0
\]

would also be useful when combined with a sufficiently sharp raw-object estimate.

A theorem merely counting rational `(t,r)` without retaining the square-root and physical-height conditions is insufficient.

## Locked boundary

```text
STAGE14_T12=COMPLETE_CONDITIONAL_REFLECTED_SQUARE_PARAMETER_GATE
RAW_POINT_CONDITIONED=true
REFLECTED_GATE_IS_RATIONAL_PYTHAGOREAN_CONIC=true
AUXILIARY_PARAMETER_R_INTRODUCED=true
Q2_VARIABLE_Y=q^2
Y_QUADRATIC_RECIPROCAL=true
DISCRIMINANT_SQUARE_NECESSARY=true
RATIONAL_ROOT_MUST_ALSO_BE_RATIONAL_SQUARE=true
PHYSICAL_HEIGHT_MUST_BE_RETAINED=true
LOCAL_PRODUCT_SIEVE_REINSTATED=false
CONDITIONAL_PAIR_THINNING_PROVED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t13 analyze the (t,r)-discriminant-square cover: factorization, genus/fibration, and possible low-degree accumulating components
```
