# Stage15-6an - isotrivial classification and theorem-species audit for the small-kappa quartic

Base: merged Stage15-6 cycle through 6am (`PR #843`, merge commit `e67258aa`). Stage15-6am reduced the unresolved branch to the one-point binary-quartic receiver

\[
\kappa T^2=f_K(a,b)g_K(a,b),
\]

where

\[
K=A+iB_1,\qquad A^2+B_1^2=k>0,
\]

\[
f_K=A(a^2-b^2)-2B_1ab,
\qquad
g_K=B_1(a^2-b^2)+2Aab,
\]

and `z=a+ib` is primitive. The norm core `k` and coordinate core `kappa` are squarefree and coprime by 6al.

Stage15-6an classifies this quartic more sharply and audits the exact external theorem species. It does not yet apply a counting theorem.

## 1. Exact complex factorization

Put

\[
p=a+ib,\qquad q=a-ib,
\qquad \overline K=A-iB_1.
\]

Then

\[
f_K=\frac{Kp^2+\overline Kq^2}{2},
\qquad
g_K=\frac{Kp^2-\overline Kq^2}{2i}.
\]

Therefore

\[
\boxed{
4i f_K(a,b)g_K(a,b)
=K^2p^4-\overline K^{\,2}q^4.
}
\]

Over `Qbar`, choose square roots of `K`, `conj(K)` and `4 i kappa`, and set

\[
P=\sqrt K\,p,
\qquad Q=\sqrt{\overline K}\,q,
\qquad Y=\sqrt{4i\kappa}\,T.
\]

The quartic becomes

\[
\boxed{Y^2=P^4-Q^4.}
\]

Thus the small-`kappa` family is not geometrically moving. Every member is a rational twist of one fixed geometric genus-one quartic.

```text
STAGE15_6AN_QBAR_ISOTRIVIAL=true
STAGE15_6AN_UNIVERSAL_GEOMETRIC_MODEL=Y^2=P^4-Q^4
```

## 2. Binary-quartic invariants

Expanding gives

\[
\begin{aligned}
F_K(a,b):=f_Kg_K
={}&AB_1a^4+2(A^2-B_1^2)a^3b-6AB_1a^2b^2\\
&-2(A^2-B_1^2)ab^3+AB_1b^4.
\end{aligned}
\]

For a binary quartic

\[
ax^4+bx^3y+cx^2y^2+dxy^3+ey^4,
\]

use the classical invariants

\[
I=12ae-3bd+c^2,
\]

\[
J=72ace+9bcd-27ad^2-27b^2e-2c^3.
\]

Direct substitution gives

\[
\boxed{I(F_K)=12k^2,\qquad J(F_K)=0.}
\]

For the equivalent quartic `kappa*F_K`,

\[
I=12(k\kappa)^2,
\qquad J=0.
\]

Since the quartic is separable by 6am, its discriminant is nonzero. Hence every member has geometric `j=1728`, consistent with the explicit model `Y^2=P^4-Q^4`.

```text
STAGE15_6AN_BINARY_QUARTIC_I=12*k^2
STAGE15_6AN_BINARY_QUARTIC_J=0
STAGE15_6AN_GEOMETRIC_J=1728
```

The arithmetic still moves: `K`, `kappa`, signs, integral models and local solubility are twist data. Isotriviality is not permission to count one fixed rational curve and multiply by a harmless constant.

## 3. Exact theorem species required

The object to count is not an arbitrary elliptic curve family. For fixed

```text
k
Gaussian orientation K with N(K)=k
coordinate core kappa
coordinate squareclass split
norm dyadic scale N(z)~Z
```

we need a pointwise upper bound for primitive integral representatives `z=(a,b)` satisfying the exact quartic square condition, uniformly in all coefficients and twists.

The theorem must be:

```text
UNIFORM_EVERY_FIBER_RATIONAL_POINT_COUNT_ON_DEGREE4_PROJECTIVE_CURVE
```

with a projective height controlled by the physical Gaussian scale. An averaged rank, average Selmer, almost-all twist, or fixed-curve estimate is weaker than the required quantifier.

## 4. Heath-Brown uniform projective-curve theorem is the correct candidate

Heath-Brown, *The density of rational points on curves and surfaces*, Annals of Mathematics 155 (2002), arXiv:math/0405392, proves a uniform curve estimate: for an irreducible projective curve `C` of degree `d` in projective space, the number of rational points of height at most `H` is

\[
\ll_{d,\varepsilon} H^{2/d+\varepsilon}.
\]

For degree `d=4` this gives

\[
\boxed{N(C;H)\ll_\varepsilon H^{1/2+\varepsilon},}
\]

with the implied constant independent of the particular quartic coefficients.

This is the right quantifier species for Stage15: pointwise for every fixed fiber and uniform in the moving twists. It does not require rank control, Selmer averaging, or an exceptional-set argument.

Primary source:

```text
D. R. Heath-Brown,
The density of rational points on curves and surfaces,
Ann. of Math. 155 (2002), 553-598,
arXiv:math/0405392,
Theorem 5 (via the uniform projective-curve determinant method).
```

```text
STAGE15_6AN_HEATH_BROWN_CURVE_THEOREM_SPECIES_MATCH=true
STAGE15_6AN_HEATH_BROWN_THEOREM_APPLIED=false
```

## 5. Why the theorem is not applied yet

The small-`kappa` equation is naturally written in weighted quartic form, while Heath-Brown counts rational points in ordinary projective height. Before applying it Stage15 must expose an exact degree-four embedding in ordinary `P^3` whose integral coordinates have a height bound derived from `N(z)~Z` and `N(K)=k`.

The required adapter is already suggested by primitivity. If

\[
\operatorname{sf}(f_K)=\kappa_f,
\qquad \operatorname{sf}(g_K)=\kappa_g,
\qquad \kappa_f\kappa_g=\kappa,
\]

then actual points have

\[
f_K=\kappa_f c^2,
\qquad g_K=\kappa_g d^2.
\]

These are two quadrics in `[a:b:c:d]`. Stage15-6ao must prove:

1. this split is exact and costs only `B^o(1)` for fixed `kappa`;
2. the resulting curve is geometrically integral degree `4`;
3. each physical primitive `z` maps with only `O(1)` multiplicity;
4. its projective height is `O(k^(1/4) Z^(1/2))`;
5. all physical masks are monotone postfilters.

Only after those items are frozen is Heath-Brown a legal direct theorem application.

## 6. Arsenal / firewall audit

```text
AR-016=FINITE coordinate-squareclass split only
AR-023/024=physical/global measure unchanged
AR-027=NOT_NEEDED_FOR_HEATH_BROWN_POINTWISE_THEOREM
AR-028=PASS; kappa remains distinct from norm core k
AR-030=physical masks retained as postfilters
```

Bhargava-Shankar style average binary-quartic/Selmer results are not used. Their average quantifier would require AR-027, while the Heath-Brown theorem candidate is already pointwise uniform.

## 7. Frozen exit

```text
STAGE15_6_SUBSTAGE=6an
STAGE15_6AN_STARTING_GATE=SMALL_KAPPA_MOVING_QUARTIC_THEOREM_AUDIT
STAGE15_6AN_QBAR_ISOTRIVIAL=true
STAGE15_6AN_UNIVERSAL_GEOMETRIC_MODEL=Y^2=P^4-Q^4
STAGE15_6AN_BINARY_QUARTIC_I=12*k^2
STAGE15_6AN_BINARY_QUARTIC_J=0
STAGE15_6AN_GEOMETRIC_J=1728
STAGE15_6AN_ARBITRARY_MOVING_ELLIPTIC_FAMILY=false
STAGE15_6AN_HEATH_BROWN_CURVE_THEOREM_SPECIES_MATCH=true
STAGE15_6AN_HEATH_BROWN_THEOREM_APPLIED=false
STAGE15_6AN_HEIGHT_EMBEDDING_ADAPTER_PROVED=false
STAGE15_6AN_EXIT=UNIFORM_DEGREE4_P3_HEIGHT_ADAPTER_READY
```

## 8. Next narrow gate

Stage15-6ao should construct the exact two-quadric `P^3` model for fixed coordinate squareclass split, prove the physical-to-projective height bound, and then apply Heath-Brown's degree-four theorem pointwise.