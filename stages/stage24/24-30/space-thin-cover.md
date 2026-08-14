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

is exactly an anticanonical adelic height on `Y`. Stage15-2b proves

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]

## 2. The added space-square cover

Add one coordinate `w` satisfying

\[
w^2=e^2+x^2+y^2.
\]

Let `Z -> Y` be the normalization of the corresponding quadratic function-field extension. A Stage18 physical object has integral space diagonal exactly when its rational point on `Y` lifts to a rational point of this cover.

For the primitive integral representative the radicand is an integer. If rational `w` satisfies `w^2` equal to that integer, then `w` is integral. Hence rational lifting agrees exactly with the Stage19 integral-space predicate on the physical population.

## 3. Geometric integrality: explicit generic nonsquare test

Work over an algebraic closure and on the affine chart `e=1` of the dense torus. Parametrize the two Pythagorean conics by independent parameters `t,s`:

\[
x=\frac{2t}{1-t^2},\qquad u=\frac{1+t^2}{1-t^2},
\]
\[
y=\frac{2s}{1-s^2},\qquad v=\frac{1+s^2}{1-s^2}.
\]

The function field is therefore a rational function field in `t,s`, and the space-square radicand is

\[
f=1+x^2+y^2=u^2+y^2.
\]

As a rational function of `s` over `\overline{\mathbf Q}(t)`,

\[
f=\frac{P_t(s)}{(1-s^2)^2},
\]
with
\[
P_t(s)=u^2s^4+(4-2u^2)s^2+u^2.
\]

Set `z=s^2`. The quadratic in `z` has discriminant

\[
(4-2u^2)^2-4u^4=16(1-u^2)=-16x^2.
\]

On the generic torus `x\ne0`, so this discriminant is nonzero. Its two `z`-roots are distinct; their product is one, so neither root is zero. Therefore `P_t(s)` has four distinct roots over the algebraic closure of `\overline{\mathbf Q}(t)` and in particular is not a square polynomial. The denominator `(1-s^2)^2` is already a square. Hence

\[
f\notin \overline{\mathbf Q}(Y)^{\times2}.
\]

Thus the quadratic extension obtained by adjoining `sqrt(f)` is nontrivial over the geometric function field. Consequently `Z` is geometrically integral and `Z -> Y` is generically finite of degree two.

This argument avoids relying on an unverified divisor-multiplicity assertion.

## 4. Thin-image theorem

The rational image `pi(Z(Q))` in `Y(Q)` is therefore a type-II thin subset.

Stage15-2b already verifies the hypotheses used for Browning-Loughran thin-set zero density on this same `Y` and exact height `R`:

- smooth projective split toric `Y`;
- `-K_Y` big;
- the required cohomological/Picard conditions;
- anticanonical equidistribution on the dense torus.

Hence

\[
\#\{P\in \pi(Z(\mathbf Q))\cap T(\mathbf Q):H_R(P)\le B\}
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
SPACE_THIN_COVER_NONSQUARE_PROOF=PYTHAGOREAN_RATIONAL_PARAMETERS_AND_SIMPLE_ROOTS
SPACE_THIN_COVER_DEGREE=2
SPACE_THIN_IMAGE_TYPE_II=true
SPACE_THIN_ROUTE_ZERO_DENSITY=true
SPACE_THIN_ROUTE_EFFECTIVE_POWER_SAVING=false
SPACE_THIN_ROUTE_INDEPENDENT_OF_STAGE14_UPPER=true
SPACE_THIN_ROUTE_INDEPENDENT_OF_LOCAL_SQUARECLASS_SIEVE=true
```
