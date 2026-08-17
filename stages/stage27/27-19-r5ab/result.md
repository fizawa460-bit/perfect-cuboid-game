# Stage27-19-r5ab — normalized squareclass collapse and diagonal genus-one receiver

```text
TASK_ID=Stage27-19-r5ab
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5aa
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
```

This route feeds the exact `r5aa` tau/core normalization back into the frozen Stage19 integral-space squareclass condition. The purpose is to expose the remaining moving-fiber arithmetic without importing the `t`-dependent Mordell-Weil constants of r402b.

Retain

\[
n=dn_0,\qquad s=ds_0,\qquad (n_0,s_0)=1,
\]
\[
M=m^2+n^2=ha,\qquad K=r^2-s^2=hb,\qquad (a,b)=1,
\]

and the exact r5aa identities

\[
p=s_0^2a,\qquad q=n_0^2b,\qquad g=d^2h.
\]

The primitive slope conditions also give

\[
(d,h)=1.
\]

Indeed `h|M,K`, while every prime dividing `d` divides both `n` and `s`; from `(m,n)=(r,s)=1` it divides neither `M=m^2+n^2` nor `K=r^2-s^2`.

## 1. Collapse of the two Gaussian norms

Stage19's frozen integral-space receiver uses

\[
U=m^2r^2+n^2s^2,
\qquad
V=m^2s^2+n^2r^2,
\]

with

\[
R\in\mathbf Z\iff UV\in\mathbf Z^2.
\]

From r5aa,

\[
m^2=ah-d^2n_0^2,
\qquad
r^2=bh+d^2s_0^2.
\]

Direct expansion gives

\[
\boxed{
U=h\Bigl(ab h+d^2(a s_0^2-b n_0^2)\Bigr)
}
\]

and

\[
\boxed{
V=d^2h(a s_0^2+b n_0^2).
}
\]

Since

\[
a s_0^2=p,\qquad b n_0^2=q,
\]

these become

\[
\boxed{U=hJ},
\qquad
\boxed{V=d^2h(p+q)},
\]

where

\[
\boxed{J=ab h+d^2(p-q)}.
\]

Therefore

\[
UV=d^2h^2(p+q)J.
\]

The factor `d^2h^2` is a square, so the Stage19 integral-space condition is exactly

\[
\boxed{R\in\mathbf Z\iff (p+q)J\in\mathbf Z^2.}
\]

Equivalently,

\[
\boxed{\operatorname{sf}(J)=\operatorname{sf}(p+q)}.
\]

This is an exact moving-label squareclass receiver, not a heuristic local condition.

## 2. Canonical squarefree coefficient

Let

\[
\kappa=\operatorname{sf}(p+q),
\qquad
p+q=\kappa c^2.
\]

Then the space condition is equivalent to the existence of a positive integer `w` such that

\[
\boxed{J=\kappa w^2}.
\]

Using the two reconstruction formulas,

\[
J=bm^2+a d^2s_0^2
\]

and

\[
J=ar^2-b d^2n_0^2.
\]

Hence every Stage19 survivor on the reduced tau label `p/q`, after one of the subpower-many square-divisor choices `(s_0,n_0)`, lies on the simultaneous diagonal quadrics

\[
\boxed{\kappa w^2=bm^2+a s_0^2d^2},
\]

\[
\boxed{\kappa w^2=ar^2-b n_0^2d^2}.
\]

Equivalently,

\[
\boxed{ar^2-bm^2=(p+q)d^2}.
\]

The last equality is the normalized fixed-tau conic; the common `w` equation is precisely the extra integral-space squareclass cut.

Thus the physical fixed-tau problem is represented by an intersection of two diagonal quadrics in `(m,r,d,w)`. This is the same theorem species as the smooth genus-one fiber from r402b, but the coefficients are now exposed arithmetically in terms of the reduced tau and its canonical square divisors.

## 3. Core form of the squareclass condition

Since `g=d^2h`, multiplying `J=ab h+d^2(p-q)` by `d^2` gives

\[
d^2J=abg+d^4(p-q).
\]

Because `d^2` is a square, the integral-space condition is also exactly

\[
\boxed{
(p+q)\Bigl(abg+(p-q)d^4\Bigr)\in\mathbf Z^2.
}
\]

Writing `v=dw`, this is

\[
\boxed{
abg+(p-q)d^4=\kappa v^2,
\qquad d\mid v.
}
\]

Therefore the unresolved distinct-core problem from r5aa is not an arbitrary count of `g`: for each reduced tau and each square-divisor decomposition of `(p,q)`, every realized core must lie in this explicit quartic-square receiver.

No claim is made that the receiver alone has sub-half support. Its role is to replace an unconstrained `g` count by a concrete squareclass/diagonal-quadrics problem suitable for a square sieve, 2-descent, determinant method, or equivalent uniform arithmetic input.

## 4. Height facts retained on the normalized model

From r402a,

\[
m^2+n^2<2B,\qquad r^2+s^2<2B,
\]

so

\[
m,r,dn_0,ds_0\ll B^{1/2}.
\]

Also

\[
ah=M<2B,
\qquad
bh=K<2B,
\]

and r402c gives on `T<=H(p/q)<2T`

\[
g=d^2h\ll B^2/T.
\]

Thus the diagonal-quadrics receiver is on a polynomial physical height box with all coefficient dependence explicit in `(p,q,s_0,n_0)`.

## 5. What has and has not been reduced

The following part of the r402f restart request is now explicit:

- r5aa removes representation multiplicity at fixed `(tau,g)` up to `B^o(1)`;
- r5ab expresses the admissible `g` values by a canonical squareclass equation;
- the remaining fixed-power task is a **uniform moving-family count** for the displayed diagonal-quadrics / quartic-square receiver.

This route does not convert pointwise Mordell-Weil into a uniform theorem, does not assume bounded rank, and does not infer a fixed-power saving from squareclass language alone.

```text
D_H_COPRIME_PROVED=true
GAUSSIAN_NORMS_NORMALIZED=true
NORMALIZED_U=h*(ab*h+d^2*(p-q))
NORMALIZED_V=d^2*h*(p+q)
SPACE_SQUARECLASS_COLLAPSE_PROVED=true
SPACE_SQUARECLASS_RECEIVER=sf(ab*h+d^2*(p-q))=sf(p+q)
DIAGONAL_TWO_QUADRICS_RECEIVER_PROVED=true
CORE_QUARTIC_SQUARE_RECEIVER_PROVED=true
CORE_QUARTIC_SQUARE_RECEIVER=ab*g+(p-q)*d^4=kappa*v^2_with_d_divides_v
UNIFORM_MOVING_RECEIVER_COUNT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_ARITHMETIC_TARGET=UNIFORM_COUNT_ON_MOVING_DIAGONAL_TWO_QUADRICS_OR_CORE_QUARTIC_SQUARE_RECEIVER
NEXT_DERIVED_ROUTE=27-19-r5ac
```
