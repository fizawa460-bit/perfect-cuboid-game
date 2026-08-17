# Stage27-20-r301i — fixed `(q1,delta)` fiber is a nonisotrivial genus-one curve

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301h
SOURCE_STAGE=Stage20

## 1. Freeze one torus coordinate and the common squareclass

Fix

\[
x:=q_1\in\mathbf Q_{>1}
\]

and a positive squarefree common class `delta`.  Write the moving second coordinate as `y=q_2`.  The r301f squareclass receiver becomes

\[
\boxed{x^2+y^2=\delta r^2,}
\qquad
\boxed{x^2y^2+1=\delta s^2.}
\]

Homogenizing with

\[
y=Y/T,\qquad r=R/T,\qquad s=S/T
\]

gives the complete intersection in `P^3`:

\[
Q_1:\quad Y^2+x^2T^2=\delta R^2,
\]

\[
Q_2:\quad x^2Y^2+T^2=\delta S^2.
\]

## 2. Smoothness and genus

For the pencil `lambda Q1 + mu Q2`, the diagonal determinant is

\[
\boxed{
\det(\lambda Q_1+\mu Q_2)
=\delta^2\lambda\mu
(\lambda+\mu x^2)(\lambda x^2+\mu).
}
\]

The four singular members of the pencil are therefore at

\[
\lambda=0,\qquad \mu=0,
\qquad \lambda/\mu=-x^2,
\qquad \lambda/\mu=-x^{-2}.
\]

They are distinct whenever

\[
\delta\ne0,\qquad x\ne0,\qquad x^4\ne1.
\]

The physical branch has `x=q1>1`, so these conditions hold.  Hence the intersection of the two quadrics is smooth; a smooth complete intersection of two quadrics in `P^3` has genus one.  Thus

\[
\boxed{C_{x,\delta}\text{ is a smooth genus-one curve for every physical }x>1.}
\]

## 3. Explicit quartic model

Subtract `x^2 Q1` from `Q2`:

\[
(1-x^4)T^2=\delta(S^2-x^2R^2).
\]

On the open set `T!=0`, put

\[
z:=\frac{S+xR}{T}.
\]

Then

\[
\frac{S-xR}{T}=\frac{1-x^4}{\delta z}.
\]

Using `Q1` and defining

\[
V:=2xz\frac{Y}{T},
\]

a direct elimination gives the birational quartic receiver

\[
\boxed{
\delta V^2
=
\bigl(\delta z^2-(x^2+1)^2\bigr)
\bigl(\delta z^2-(x^2-1)^2\bigr).
}
\]

The discriminant of the quartic polynomial on the right is

\[
\boxed{
4096\,\delta^6x^8(x^4-1)^2,
}
\]

which is nonzero on the physical locus.

Over an algebraic closure its four branch points are

\[
\pm\frac{x^2+1}{\sqrt\delta},
\qquad
\pm\frac{x^2-1}{\sqrt\delta}.
\]

One cross-ratio is

\[
\boxed{x^{-4}},
\]

so the family varies nontrivially with `x`; in particular the moving-`x` genus-one family is nonisotrivial.  The squareclass `delta` acts as a twist parameter and does not remove this variation.

## 4. Pointwise fixed-fiber count

For one fixed pair `(x,delta)`, if `C_{x,delta}(Q)` is empty then the fiber contributes nothing.  Otherwise choose a rational point and identify the genus-one curve with its elliptic Jacobian.  Mordell--Weil gives finite rank `r_{x,delta}`.

The physical bound `R<=B` gives `H(y)<=2B` as in r301h, and on a fixed fiber the remaining coordinates `r,s,z,V` are rational functions of bounded degree in the physical coordinates.  Hence their projective heights are bounded by a fixed power of `B`, with constants depending on `(x,delta)`.  Standard comparison with the Neron--Tate height therefore gives the pointwise estimate

\[
\boxed{
 w_{x,\delta}(B)
 \ll_{x,\delta}
 (1+\log B)^{r_{x,\delta}/2}
 =B^{o_{x,\delta}(1)}.
}
\]

This is deliberately **pointwise only**.  The rank, generators, height-comparison constants, and lattice constants are not proved uniform as `(x,delta)` move with `B`.

## 5. Scope firewall

The fixed-fiber genus-one structure is a new exact receiver, but pointwise Mordell--Weil bounds cannot be summed over moving fibers without a uniform or averaged theorem.

```text
STAGE27_20_R301I_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
FIXED_Q1_DELTA_COMPLETE_INTERSECTION_TWO_QUADRICS=true
FIXED_Q1_DELTA_PHYSICAL_FIBER_GENUS=1
FIXED_Q1_DELTA_QUARTIC_MODEL_PROVED=true
QUARTIC_BRANCH_DISCRIMINANT=4096*delta^6*x^8*(x^4-1)^2
MOVING_Q1_FAMILY_NONISOTRIVIAL=true
POINTWISE_FIXED_FIBER_SUBPOWER_PROVED=true
UNIFORM_MOVING_FIBER_SUBPOWER_PROVED=false
POINTWISE_TO_UNIFORM_PROMOTION_FORBIDDEN=true
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301j
```
