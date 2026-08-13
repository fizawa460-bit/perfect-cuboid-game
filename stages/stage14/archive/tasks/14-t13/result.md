# Stage14-t13 — discriminant-square cover classification

## Setup

Stage14-t12 parametrizes the shared-q conic by a rational parameter `r` and reduces compatible triple points to

\[
y^2+B_{t,r}y+1=0,\qquad y=q^2,
\]

with

\[
B_{t,r}=2\frac{1-t^2}{1+t^2}-\frac{(1-r^2)^2}{t^2(1+t^2)r^2}.
\]

A necessary condition is that

\[
D_{t,r}=B_{t,r}^2-4
\]

be a rational square.

## Exact factorization

Direct symbolic factorization gives

\[
\boxed{
D_{t,r}=\frac{(r^2-2tr-1)(r^2+2tr-1)(r^4+(4t^4-2)r^2+1)}{r^4t^4(1+t^2)^2}.
}
\]

The denominator is already a square in `Q(t,r)`. Hence the normalized discriminant-square cover is birational to

\[
\boxed{
Z^2=(r^2-2tr-1)(r^2+2tr-1)(r^4+(4t^4-2)r^2+1).
}
\]

For fixed generic `t`, the branch polynomial has degree `8` in `r`.

## Generic genus

Its discriminant with respect to `r` is

\[
\boxed{
2^{40}t^{28}(t-1)^2(t+1)^2(t^2+1)^{12}.
}
\]

Therefore the degree-eight branch polynomial is squarefree for

\[
t\notin\{0,\pm1,\pm i\}.
\]

The smooth projective normalization of a squarefree double cover of `P^1_r` branched at eight points has

\[
g=(8-2)/2=3.
\]

Thus every genuine physical rational Pythagorean base has a genus-three discriminant-square fiber: physical `t` is positive rational, `1+t^2` is a rational square, and the degenerate values `0,1` are excluded from genuine primitive faces; `-1,\pm i` are nonphysical.

So there is **no physical rational base where this t12 discriminant cover drops to genus 0, 1, or 2 by branch collision**.

## Interpretation

This is a useful reduction from the original genus-five shared-q Humbert--Edge fiber: after conditioning on a raw point and parametrizing the auxiliary Pythagorean conic, the first remaining square condition is a genus-three hyperelliptic fiber.

However this does not yet count triple points. A compatible point must additionally satisfy that the chosen root

\[
y=\frac{-B_{t,r}\pm\sqrt{D_{t,r}}}{2}
\]

is itself a rational square `q^2` in the physical height window. That second square condition is a further cover of the genus-three discriminant fiber.

The factorization into two quadratic factors and one reciprocal quartic may still provide quotient maps or involutions, but factorization of the branch polynomial does not by itself decompose the hyperelliptic curve into rational components.

## Locked boundary

```text
STAGE14_T13=COMPLETE_DISCRIMINANT_COVER_GENUS_CLASSIFICATION
DISCRIMINANT_FACTORIZATION_EXACT=true
NORMALIZED_DISCRIMINANT_COVER_DEGREE_IN_R=8
GENERIC_DISCRIMINANT_COVER_GENUS=3
BRANCH_COLLISION_T_VALUES=0,+1,-1,+i,-i
PHYSICAL_RATIONAL_LOW_GENUS_FIBERS=0
ROOT_Y_IS_SQUARE_CONDITION_STILL_REQUIRED=true
PHYSICAL_HEIGHT_WINDOW_STILL_REQUIRED=true
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t14 exploit involutions/quotients of the genus-3 discriminant cover and analyze the additional y=q^2 square cover
```
