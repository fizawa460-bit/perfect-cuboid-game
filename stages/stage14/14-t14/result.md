# Stage14-t14 — elliptic quotient and second-square cover

## Purpose

Stage14-t13 reduced the compatible shared-q gate to the genus-three hyperelliptic curve

\[
Z^2=(r^2-2tr-1)(r^2+2tr-1)(r^4+(4t^4-2)r^2+1),
\]

for each genuine physical rational base `t`, together with the essential second condition that the reciprocal-quadratic root `y=q^2` is itself a rational square.

This stage exploits the even/reciprocal symmetry and rewrites the second square condition intrinsically on the discriminant cover.

## 1. The involution r -> -r gives a genus-one quotient

The branch polynomial is even in `r`. Put

\[
x=r^2.
\]

Then the quotient by `r -> -r` is

\[
\boxed{
E_t:\quad Z^2=((x-1)^2-4t^2x)(x^2+(4t^4-2)x+1).
}
\]

The right-hand side is a quartic in `x`. For the same physical parameter set as Stage14-t13 (`t != 0, +-1, +-i`), the branch points are distinct, so its smooth projective normalization has genus one.

Thus the genus-three discriminant cover is bielliptic over `Q(t)` via the degree-two map

\[
(r,Z)\mapsto (x=r^2,Z).
\]

This is a genuine structural reduction: the first square gate can be studied on an elliptic quotient, but lifting back to the genus-three curve still requires `x` to be a rational square.

## 2. The second condition y=q^2 is another explicit square cover

From Stage14-t12,

\[
y^2+B_{t,r}y+1=0,
\]

where

\[
B_{t,r}=-\frac{r^4+2r^2t^4-2r^2t^2-2r^2+1}
{r^2t^2(1+t^2)}.
\]

Because `y=q^2`, we have

\[
-B_{t,r}=q^2+q^{-2}.
\]

Hence

\[
\boxed{-B_{t,r}-2=(q-q^{-1})^2.}
\]

Conversely, on the discriminant-square cover, if `-B-2` is a rational square then `2-B` is also a rational square because

\[
(B^2-4)=(-B-2)(2-B),
\]

and therefore the reciprocal quadratic has a rational root that is a rational square. So the `y=q^2` condition is equivalent, on the t13 discriminant cover, to the additional square condition

\[
\boxed{-B_{t,r}-2\in (\mathbf Q^\times)^2.}
\]

This factor has the exact form

\[
\boxed{
-B_{t,r}-2=
\frac{(r^2-2tr-1)(r^2+2tr-1)}{r^2t^2(1+t^2)}.
}
\]

Since a physical first-face base satisfies `1+t^2=h^2`, the denominator is a rational square. Therefore the second cover is simply

\[
\boxed{
U^2=(r^2-2tr-1)(r^2+2tr-1)
=((r^2-1)^2-4t^2r^2).
}
\]

In the quotient coordinate `x=r^2`, this becomes

\[
\boxed{U^2=(x-1)^2-4t^2x.}
\]

This is a conic over `Q(t)`, not a new positive-genus obstruction by itself.

## 3. Simultaneous structure

The genus-one quotient may therefore be written as

\[
Z^2=U^2\,V^2,
\]

with

\[
U^2=(x-1)^2-4t^2x,
\]

\[
V^2=x^2+(4t^4-2)x+1,
\]

when both square factors are required individually.

Equivalently, the original compatible-pair condition decomposes into two explicit conic square conditions in `x=r^2`, together with the lift condition

\[
x\in (\mathbf Q^\times)^2.
\]

The product-square condition alone is the elliptic quotient `E_t`; the physical triple condition requires the stronger simultaneous factor-square lift and then the physical height bound.

This is important: the genus-one quotient does **not** mean every rational point on `E_t` lifts to a triple point.

## 4. Boundary

Stage14-t14 proves a structural decomposition, not a counting theorem. No rank statement for `E_t`, no uniform rational-point bound, and no density saving for simultaneous factor-square lifts is claimed.

The next stage should analyze the simultaneous conic system

\[
U^2=(x-1)^2-4t^2x,
\]

\[
V^2=x^2+(4t^4-2)x+1,
\]

with `x` itself a rational square and the physical height cutoff retained. This is now a concrete three-square fiber-product problem over the physical Pythagorean base family.

```text
STAGE14_T14=COMPLETE_BIELLIPTIC_QUOTIENT_AND_SECOND_SQUARE_DECOMPOSITION
GENUS3_COVER_HAS_R_TO_MINUS_R_INVOLUTION=true
QUOTIENT_BY_R_SIGN_GENUS=1
SECOND_Y_EQUALS_Q2_CONDITION_EQUIVALENT_TO_MINUS_B_MINUS_2_SQUARE=true
SECOND_SQUARE_FACTOR_CONIC=true
PHYSICAL_TRIPLE_REQUIRES_BOTH_QUARTIC_FACTORS_SQUARE=true
PHYSICAL_TRIPLE_REQUIRES_X_EQUALS_R2_SQUARE=true
ELLIPTIC_QUOTIENT_POINT_SUFFICIENT_FOR_TRIPLE=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t15 simultaneous two-conic plus x-square fiber-product classification/counting boundary
```
