# Stage27-20-r301r — Naccarato uniformity kills the moving fixed-x fiber exponent

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301q
SOURCE_STAGE=Stage20

## 1. Uniform target theorem

Stage27-20-r301q maps every physical point in a fixed `(x,delta)` fiber, with multiplicity at most two, to

\[
\mathcal E_{a,b}:\quad
W^2=U(U-(a^2+b^2)^2)(U-(a^2-b^2)^2),
\qquad x=a/b,
\]

where

\[
H(\mathcal E_{a,b})\ll B^8
\]

and every physical image has

\[
H(U)\le B^{K_0}
\]

for an absolute `K0`.

Naccarato, *Counting rational points on elliptic curves with a rational 2-torsion point*, arXiv:2105.04032, Theorem 1.1, proves that there exist absolute computable constants `C,c0` such that every elliptic curve over `Q` with a rational `2`-torsion point satisfies

\[
N_E(T)\le T^{C/\log\log T}
\]

whenever

\[
T\ge\max\{e^e,(eH(E))^{c_0}\}.
\]

The constants are absolute and therefore legal for a moving family.

Choose one absolute `K` large enough that

\[
T_B:=B^K
\]

dominates both `B^{K0}` and the theorem threshold `(eH(\mathcal E_{a,b}))^{c0}` for all sufficiently large `B`.  Since every `\mathcal E_{a,b}` has full rational `2`-torsion,

\[
\boxed{
N_{\mathcal E_{a,b}}(T_B)
\le B^{O(1/\log\log B)}
=B^{o(1)}
}
\]

**uniformly in every moving physical `x=a/b`.**

## 2. Uniform fixed `(x,delta)` count

The r301q receiver has fibers of cardinality at most two apart from `O(1)` exceptional target points.  Therefore

\[
\boxed{
w_{x,\delta}(B)=B^{o(1)}}
\]

uniformly over all physical moving pairs `(x,delta)`.

This is strictly stronger than the old r301i statement

\[
w_{x,\delta}(B)=B^{o_{x,\delta}(1)},
\]

because the exponent loss and implied asymptotic control no longer depend on the individual fiber.

## 3. Sum over squareclasses at one fixed x

R301h proved uniformly

\[
|D_x(B)|=B^{o(1)}
\]

for the set of compatible squareclasses above one fixed `x`.  Define

\[
W_x(B)=\sum_{\delta\in D_x(B)}w_{x,\delta}(B).
\]

Combining the two uniform subpolynomial factors gives

\[
\boxed{
W_x(B)=B^{o(1)}
}
\]

uniformly over every occupied physical `x`.

Thus the fixed-`x` fiber exponent in the r301j/r301o gate is now

\[
\boxed{\phi=0.}
\]

This removes the regulator/minimum-height obstruction that stopped r301p.  The remaining exponent is entirely the support exponent of occupied first coordinates.

## 4. Scope firewall

This is a genuine strengthening of the Stage27 upper receiver, but it is **not yet** a strict sub-square-root theorem.  One still needs an independent upper bound for

\[
Q(B)=\{x=q_1:\text{some Stage27 survivor with }R\le B\text{ has first coordinate }x\}.
\]

The existing half-power theorem only gives an inherited support bound through the population itself and cannot be multiplied back as an independent saving.

```text
STAGE27_20_R301R_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
NACCARATO_THEOREM_1_1_APPLIED=true
UNIFORM_MOVING_Q1_DELTA_FIBER_SUBPOWER_PROVED=true
UNIFORM_FIXED_X_AGGREGATE_SUBPOWER_PROVED=true
FIXED_X_AGGREGATE_FIBER_EXPONENT=0
REGULATOR_HEIGHT_OBSTRUCTION_REMOVED_FOR_POINT_COUNT=true
INDEPENDENT_Q1_SUPPORT_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301s
```
