# Stage24-30 space-square thin-cover route

EVIDENCE_LEVEL=PROVED_FROM_FROZEN_STAGE15_TORIC_INTERFACE
PURPOSE=INDEPENDENT_ZERO_DENSITY_ROUTE

## 1. Base surface

Use the Stage15/18 shared-edge surface on the dense torus:

\[
u^2=e^2+x^2,\qquad v^2=e^2+y^2.
\]

Its smooth split toric resolution is the frozen Stage15 surface `Y=Bl_4(P1 x P1)`. The physical height

\[
H_R=\sqrt{e^2+x^2+y^2}
\]

is exactly an anticanonical adelic height on `Y`. Stage15-2b proves the positive physical chamber count

\[
A(B)\sim C_A B(\log B)^5,
\]

and, after the lower-order three-face subtraction,

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}=C_A>0.
\]

## 2. The added space-square cover

Add one coordinate `w` satisfying

\[
w^2=e^2+x^2+y^2.
\]

Let `Z -> Y` be the normalization of the corresponding degree-two function-field extension. A Stage18 physical object has integral space diagonal exactly when its rational point on `Y` lifts to a rational point of `Z`.

For the primitive integral representative the radicand is an integer. If a rational `w` has `w^2` equal to this integer, then `w` is integral. Thus rational lifting and the Stage19 integral-space predicate agree exactly on the physical population.

## 3. Geometric integrality

Over an algebraic closure,

\[
f:=e^2+x^2+y^2=u^2+y^2=(u+i y)(u-i y).
\]

Consider a generic irreducible component `D` of the divisor `u+i y=0` meeting the dense torus with `y!=0`. Such torus points exist; for example over the algebraic closure one may take a point satisfying

`e=1, y=1, u=-i, x^2=-2, v^2=2`,

with all torus coordinates nonzero.

At the generic point of `D`, `u-i y=-2iy` is nonzero. Hence

\[
\operatorname{ord}_D(f)=1.
\]

A square in the geometric function field has even valuation at every prime divisor. Therefore `f` is not a square in `\overline{Q}(Y)`. The cover `Z -> Y` is geometrically integral and generically finite of degree two.

## 4. Thin-image theorem

The rational image `pi(Z(Q))` in `Y(Q)` is therefore a type-II thin subset.

Stage15-2b already verifies the hypotheses used for Browning-Loughran thin-set zero density on this same `Y` and height:

- smooth projective split toric `Y`;
- `-K_Y` big;
- the required cohomological/Picard conditions;
- anticanonical equidistribution on the dense torus.

Thus

\[
\#\{P\in \pi(Z(Q))\cap T(Q):H_R(P)\le B\}
=o(B(\log B)^5).
\]

Every Stage19 exactly-two integral-space object is represented by a point in this thin image. Therefore

\[
\boxed{N_2(B)=o(B(\log B)^5)}.
\]

Since

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\]

we obtain independently

\[
\boxed{N_2(B)/M_2(B)\to0}.
\]

## 5. Directional corollary

Stage15-2b proves for each shared-edge direction `j=a,b,c`

\[
M_{2,j}(B)\sim C_jB(\log B)^5,\qquad C_j>0.
\]

Because `N_{2,j}(B)` is bounded by the same global thin-image count,

\[
N_{2,j}(B)=o(B(\log B)^5),
\]

hence

\[
\boxed{N_{2,j}(B)/M_{2,j}(B)\to0}
\]

for every direction.

## 6. Firewall

This proof is qualitative. The invoked thin-set theorem gives zero density here, not the Stage14 half-power bound. Therefore:

- do not combine its little-o saving multiplicatively with the Stage14 `B^(1/2+epsilon)` theorem;
- do not infer `N2(B)<<B^(1/2-delta)`;
- do not infer an asymptotic for `N2`;
- do not infer unboundedness or a lower bound;
- do not infer a directional limiting survivor ratio.

```text
SPACE_THIN_COVER_GEOMETRICALLY_INTEGRAL=true
SPACE_THIN_COVER_DEGREE=2
SPACE_THIN_IMAGE_TYPE_II=true
SPACE_THIN_ROUTE_ZERO_DENSITY=true
SPACE_THIN_ROUTE_EFFECTIVE_POWER_SAVING=false
SPACE_THIN_ROUTE_INDEPENDENT_OF_STAGE14_UPPER=true
SPACE_THIN_ROUTE_INDEPENDENT_OF_LOCAL_SQUARECLASS_SIEVE=true
```
