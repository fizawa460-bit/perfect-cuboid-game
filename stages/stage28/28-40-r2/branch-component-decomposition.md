# Stage28-40-r2 — exact branch-component decomposition

```text
ROUTE=U10_BRANCH_COMPONENT_PROFILE
STATUS=REPAIRED_PENDING_FRESH_REAUDIT
BASE_HOST=Y=Bl_4(P1xP1)
AUDIT_REPAIR=replace_false_sum_of_pair_products_by_exact_four_factor_product
```

The merged PR #1042 proved only the coarse equality

```text
same base Y
same cover degree 2
same branch class -2K_Y
same K3 canonical type
actual branch divisors different
```

This route resolves the geometric difference much more sharply.

## 1. Common Pythagorean coordinates

Write

\[
t_i=\frac{u_i^2-v_i^2}{2u_iv_i}.
\]

For Stage20 third-face completion, clearing the common square denominator from

\[
t_1^2+t_2^2=z^2
\]

gives, up to the irrelevant square factor `4`,

\[
F_{\rm face}/4=
(u_1^2-v_1^2)^2u_2^2v_2^2
+(u_2^2-v_2^2)^2u_1^2v_1^2.
\]

For Stage19 space completion, merged r301a gives

\[
F_{\rm sp}=
16u_1^2v_1^2u_2^2v_2^2
+4(u_1^2-v_1^2)^2u_2^2v_2^2
+4(u_2^2-v_2^2)^2u_1^2v_1^2.
\]

## 2. Third-face branch: two genus-one anticanonical components

Over `Q(i)`, set

\[
A=(u_1^2-v_1^2)u_2v_2,
\qquad
C=(u_2^2-v_2^2)u_1v_1.
\]

Then

\[
\boxed{F_{\rm face}/4=(A+iC)(A-iC).}
\]

Each factor has bidegree `(2,2)` on `P1xP1` and passes simply through all four toric corners.  Its strict transform on

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1)
\]

therefore has class

\[
2H_1+2H_2-\sum_{j=1}^4E_j=-K_Y.
\]

Each component is geometrically irreducible.  On the affine chart `v1=v2=1`, one component is

\[
y(x^2-1)+ix(y^2-1)=0.
\]

Viewed as a quadratic in `x`, its discriminant is

\[
-(y^4-6y^2+1).
\]

The quartic `y^4-6y^2+1` has four simple roots, so the discriminant is not a square in `C(y)`.  By Gauss' lemma the `(2,2)` polynomial is irreducible over `C`.  The conjugate factor is likewise irreducible.

Adjunction for `C_face ~ -K_Y` gives

\[
2g-2=C_{\rm face}(C_{\rm face}+K_Y)=0,
\]

hence

\[
\boxed{g(C_{\rm face})=1.}
\]

Thus the geometric branch profile of the Stage20 cover is

```text
THIRD_FACE_BRANCH_GEOMETRIC_COMPONENTS=2
THIRD_FACE_COMPONENT_CLASS=-K_Y
THIRD_FACE_COMPONENT_GENUS_MULTISET={1,1}
```

## 3. Space branch: four rational (1,1) components

Use

\[
4u_1^2v_1^2+(u_1^2-v_1^2)^2=(u_1^2+v_1^2)^2.
\]

The fresh hostile audit correctly identified that the original submission head wrote a false `+` between the two conjugate-pair products.  The exact identity is the product of all four factors:

\[
\boxed{
F_{\rm sp}/4=
(u_1u_2-iv_1v_2)(u_1u_2+iv_1v_2)
(u_1v_2-iu_2v_1)(u_1v_2+iu_2v_1).
}
\]

Multiplying the conjugate pairs first gives

\[
(u_1^2u_2^2+v_1^2v_2^2)
(u_1^2v_2^2+u_2^2v_1^2),
\]

and direct expansion gives exactly

\[
4u_1^2v_1^2u_2^2v_2^2
+(u_1^2-v_1^2)^2u_2^2v_2^2
+(u_2^2-v_2^2)^2u_1^2v_1^2
=F_{\rm sp}/4.
\]

Thus the repaired factorization is an exact polynomial identity, not merely an equality of divisor classes.

Each factor is a rank-two bilinear form and hence an irreducible `(1,1)` curve over `C`.

The first conjugate pair passes through the two opposite toric corners `(0,infinity)` and `(infinity,0)`; the second pair passes through `(0,0)` and `(infinity,infinity)`.  After blowing up those corners, every component has class of the form

\[
H_1+H_2-E_j-E_k.
\]

Its self-intersection is `0`, and

\[
C(C+K_Y)=-2,
\]

so adjunction gives genus zero.

Thus

```text
SPACE_BRANCH_GEOMETRIC_COMPONENTS=4
SPACE_COMPONENT_BIDEGREE=1_1
SPACE_COMPONENT_GENUS_MULTISET={0,0,0,0}
TOTAL_SPACE_BRANCH_CLASS=-2K_Y
U10_FACTORISATION_REPAIRED=true
U10_FACTORISATION_EXPANSION_CHECK=PASS_EXACT
```

## 4. New comparison consequence

The branch divisors have the same total class but different geometric irreducible-component profiles:

\[
\boxed{
D_{\rm sp}:4\times g0
\qquad\text{versus}\qquad
D_{\rm face}:2\times g1.
}
\]

Therefore no automorphism of `Y_Qbar` can carry the Stage19 branch divisor to the Stage20 branch divisor: an automorphism preserves the number and genera of geometric irreducible components.

This proves a genuine global geometric asymmetry that the coarse `-2K_Y` comparison in PR #1042 could not see.

It does **not** prove that the resolved K3 surfaces are non-isomorphic or non-birational, and it does not produce a count inequality by itself.

```text
SAME_TOTAL_BRANCH_CLASS=true
SAME_BRANCH_COMPONENT_PROFILE=false
BASE_AUTOMORPHISM_IDENTIFYING_BRANCHES=false
K3_NONISOMORPHISM_PROVED=false
K3_NONBIRATIONALITY_PROVED=false
BRIDGE_ORDERING_PROVED=false
```
