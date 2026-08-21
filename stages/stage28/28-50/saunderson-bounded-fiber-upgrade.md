# Stage28-50 — bounded-fiber upgrade for the generalized Saunderson construction

```text
ROUTE=L1_GENERAL_SAUNDERSON_BOUNDED_FIBER
STATUS=NEW_THEOREM_CANDIDATE_PENDING_FRESH_AUDIT
TARGET_POPULATION=Stage20 M3
COMMON_CUTOFF=R<=B
PRIOR_LOWER=M3(B)>>_epsilon B^(1/3-epsilon)
NEW_LOWER_CANDIDATE=M3(B)>>B^(1/3)
```

## 1. Audited upstream construction

Stage26 checkpoint60 / PR #1019 already proves that every primitive Pythagorean triple

\[
u^2+v^2=w^2
\]

produces a primitive Euler cuboid by the generalized Saunderson formulas

\[
A=u|4v^2-w^2|,\qquad
B=v|4u^2-w^2|,\qquad
C=4uvw.
\]

Its three integral face diagonals are

\[
D=w^3,\qquad
E=u(4v^2+w^2),\qquad
F=v(4u^2+w^2),
\]

with `D` the diagonal of the `(A,B)` face.  In Euclid parameters

\[
u=r^2-s^2,\qquad v=2rs,\qquad w=r^2+s^2,
\]

the primitive opposite-parity parameter set with `r,s<=T` has cardinality `>>T^2`, and every resulting physical cuboid satisfies

\[
R<72T^6.
\]

The only loss in the Stage26 lower theorem came from bounding the number of input triples that can map to one canonical Euler cuboid by `B^o(1)`.

## 2. Exact inverse information retained by a physical output

Let a primitive canonical Euler cuboid in the image be fixed.  A preimage input `(u,v,w)` has the distinguished face diagonal

\[
D=w^3.
\]

There are only three physical faces.  Therefore there are at most three choices for which output face diagonal is `w^3`.

Fix one such choice.  Since the chosen diagonal is a positive integer cube, `w` is uniquely determined by its integer cube root.

The edge opposite that face is also determined by the physical incidence structure.  For a Saunderson preimage this opposite edge is exactly

\[
C=4uvw.
\]

Hence the product is recovered exactly:

\[
\boxed{uv=C/(4w).}
\]

Together with

\[
\boxed{u^2+v^2=w^2,}
\]

this determines the unordered pair `{u,v}` uniquely, because

\[
(u+v)^2=w^2+2uv,
\qquad
(u-v)^2=w^2-2uv.
\]

Equivalently, `u^2` and `v^2` are the two roots of

\[
X^2-w^2X+(uv)^2=0.
\]

For a primitive Pythagorean triple exactly one leg is even, so the standard orientation convention fixes the ordered input as well.  Thus each chosen cube face yields at most one primitive input triple.

Therefore the generalized Saunderson map from primitive oriented Pythagorean input triples to primitive canonical Euler cuboids has the absolute fiber bound

\[
\boxed{\#\operatorname{fiber}\le3.}
\]

```text
OUTPUT_CUBE_FACE_CHOICES_AT_MOST=3
FIXED_CUBE_FACE_DETERMINES_W=true
OPPOSITE_EDGE_DETERMINES_UV=true
SUM_OF_SQUARES_DETERMINES_UNORDERED_U_V=true
PRIMITIVE_PARITY_DETERMINES_ORIENTATION=true
GLOBAL_FIBER_BOUND=3
DIVISOR_FIBER_BOUND_NEEDED=false
```

## 3. Epsilon-free one-third lower

Let `P(T)` be the primitive opposite-parity Euclidean parameter set

\[
1\le s<r\le T,
\qquad (r,s)=1,
\qquad r-s\equiv1\pmod2.
\]

The audited Stage26 parameter count gives

\[
\#P(T)\gg T^2.
\]

All outputs have `R<72T^6`, and each physical output has at most three preimages by the preceding argument.  Therefore

\[
M_3(72T^6)\ge \frac13\#P(T)\gg T^2.
\]

Taking `T=floor((B/72)^(1/6))` gives, for all sufficiently large `B`,

\[
\boxed{M_3(B)\gg B^{1/3}.}
\]

No epsilon loss is required.

```text
M3_LOWER_B_ONE_THIRD_CANDIDATE=true
M3_LOWER_B_ONE_THIRD_MINUS_EPSILON_SUPERSEDED_IF_AUDITED=true
TRUE_M3_EXPONENT_IDENTIFIED=false
M3_ASYMPTOTIC_PROVED=false
UPPER_LOWER_MATCH=false
```

## 4. Consistency and scope firewalls

This is a lower-bound theorem only.  It does not show that the true `M3` exponent is `1/3`; the current upper theorem remains much larger.  It also gives no information about whether any Euler cuboid in this family has integral space diagonal.

The inversion uses only data already present in the physical Euler cuboid: its three face diagonals and the edge opposite each face.  It does not label an arbitrary face as the distinguished one for free; instead all at most three possibilities are enumerated, which is exactly why the safe global fiber bound is `3` rather than `1`.

```text
CANONICAL_SORTING_LOSES_FACE_INCIDENCE=false
FIBER_INJECTIVITY_CLAIM=false
SAFE_FIBER_BOUND_ONLY=true
PERFECT_CUBOID_ENDPOINT_USED=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_REQUIRED=true
```
