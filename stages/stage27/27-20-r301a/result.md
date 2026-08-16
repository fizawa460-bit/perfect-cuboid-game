# Stage27-20-r301a — space-diagonal completion cover on the common two-face host

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
SOURCE_STAGE=Stage20
PARENT=Stage27-20-r301

## 1. Common host

On the audited Stage14-e shared-edge two-face host write

\[
t_1=x/e,\qquad t_2=y/e,
\]

with both shared-edge face diagonals rational/integral on the physical population. The compactified host is

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),\qquad -K_Y=2H_1+2H_2-\sum_{j=1}^4E_j.
\]

Stage20 completion imposes the third-face square `t_1^2+t_2^2=square`. Stage27 N2 space completion instead imposes

\[
\boxed{1+t_1^2+t_2^2=w^2}.
\]

The populations are not identified; only the common host is reused.

## 2. Pythagorean-coordinate branch polynomial

Write

\[
t_i=\frac{u_i^2-v_i^2}{2u_iv_i}.
\]

Clearing the common denominator `16u_1^2v_1^2u_2^2v_2^2`, the space-diagonal cover has branch numerator

\[
\boxed{
F_{\rm sp}=16u_1^2v_1^2u_2^2v_2^2
+4(u_1^2-v_1^2)^2u_2^2v_2^2
+4(u_2^2-v_2^2)^2u_1^2v_1^2.
}
\]

Every term has degree four in `(u_1,v_1)` and degree four in `(u_2,v_2)`, so the zero divisor on `P1 x P1` has bidegree `(4,4)`.

At every torus-fixed corner, choose the vanishing homogeneous coordinate in each factor as local parameters `(r,s)`. The two last summands give nonzero multiples of `r^2` and `s^2` to lowest order, while the first summand has order at least four. Therefore the branch divisor has multiplicity exactly two at each of the four corners.

Hence its strict transform on `Y` has class

\[
\boxed{D_{\rm sp}\sim4H_1+4H_2-2\sum E_j=-2K_Y.}
\]

## 3. Double-cover canonical class

For the normalization of the double cover

\[
\pi_{\rm sp}:Z_{\rm sp}\to Y
\]

branched over the odd branch divisor `D_sp`, double-cover adjunction gives

\[
K_{Z_{\rm sp}}=\pi_{\rm sp}^*(K_Y+D_{\rm sp}/2)=0.
\]

After resolving boundary rational double points when present, the compactified space-diagonal completion surface is therefore K3-type, exactly at the level of canonical divisor class used in Stage14-e8.

This does NOT identify it with the Stage20 third-face K3 surface, and does not transfer Stage20 local densities.

## 4. Scope

SPACE_DIAGONAL_DOUBLE_COVER_DERIVED=true
SPACE_DIAGONAL_BRANCH_BIDEGREE=4_4
SPACE_DIAGONAL_CORNER_MULTIPLICITY=2_EACH
SPACE_DIAGONAL_BRANCH_CLASS=-2K_Y
SPACE_DIAGONAL_K3_TYPE_PROVED=true
STAGE20_THIRD_FACE_COVER_IDENTIFIED_WITH_SPACE_COVER=false
STAGE20_LOCAL_FACTORS_TRANSFERRED=false
STRICT_SUB_SQRT_UPPER_PROVED=false

NEXT_DERIVED_ROUTE=27-20-r301b
