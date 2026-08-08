# Stage14-4aj — lock the singular-anticanonical / Shimada lattice interface

## Purpose

Stage14-4ai reduced every fixed-curve `sqrt(B)` mechanism to one unresolved case:

\[
D\in |L|,\qquad L=-K_Y,\qquad p_a(D)=1,
\]

where `D` is singular with rational normalization and the raw Kummer double cover splits above `D`.

PR #185 supplied the missing literature/computation map for Shimada's level-4 modular K3 data. Stage14-4aj turns that handoff into an exact finite lattice-search interface and, crucially, identifies the Stage14 deck involution in the already locked elliptic coordinates.

This substage does **not** claim that the surviving degree-four locus is empty or nonempty. It removes ambiguity from the computation that must decide it.

## 1. Frozen Stage14 geometry

Write

\[
Y=\operatorname{Bl}_4(\mathbf P^1_r\times\mathbf P^1_s),
\qquad
L=2H_r+2H_s-E_{++}-E_{+-}-E_{-+}-E_{--},
\]

and let

\[
\pi:X\to Y
\]

be the resolved Stage14 double cover. The physical polarization is

\[
\boxed{M=\pi^*L},\qquad M^2=8,
\]

and the physical height is `H_M=d`.

The raw affine equation is

\[
Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2.
\]

Stage14-4ai proved that every still-possible fixed rational square-root curve `C` must satisfy

\[
C\simeq\mathbf P^1,\qquad M\cdot C=4,
\qquad \deg(C\to\mathbf P^1_r)=2,
\]

and must lie above a split singular member `D in |L|`.

## 2. The complete anticanonical linear system in `(r,s)`

A bidegree `(2,2)` polynomial vanishing at the four toric corners `(+-1,+-1)` has a five-dimensional vector space of sections. A convenient basis is

\[
\boxed{
\begin{aligned}
&r^2-1,\qquad s^2-1,\qquad r^2s^2-1,\\
&r(s^2-1),\qquad s(r^2-1).
\end{aligned}}
\]

Hence every anticanonical member is represented by

\[
\boxed{
P=a(r^2-1)+b(s^2-1)+c(r^2s^2-1)
+d\,r(s^2-1)+e\,s(r^2-1).
}
\]

The four corner conditions have rank four inside the nine-dimensional bidegree `(2,2)` space, so this basis is complete and `|L|` has projective dimension four.

This gives a coordinate-side route to the singular discriminant, but the primary 14-4aj route is the finite Neron-Severi lattice calculation below.

## 3. Exact Stage14 deck involution on the elliptic fiber

Stage14-4ad/4ae use

\[
E_t:\quad y^2=x(x-1)(x+t^2)
\]

and the inverse physical second-half-angle coordinate

\[
\boxed{q=\frac{x}{s_0y}},
\]

where `s_0=S_1/H_1` is constant on a fixed first-face fiber.

The raw Kummer deck involution changes the square-root sign while fixing `q`. Solving the quadratic relation for the second point with the same `q` gives

\[
\boxed{
\delta_t(x,y)=
\left(-\frac{t^2}{x},-\frac{t^2y}{x^2}\right).
}
\]

Direct substitution gives

\[
\delta_t(E_t)=E_t,\qquad q\circ\delta_t=q,
\qquad \delta_t^2=1.
\]

For the group law with zero at infinity, translation by the two-torsion point

\[
T_0=(0,0)
\]

has the standard `x`-transformation `x -> -t^2/x`. The sign above is therefore

\[
\boxed{\delta_t(P)=T_0-P=\tau_{T_0}\circ[-1](P).}
\]

This is the key bridge to Shimada's data.

## 4. Consequence for Shimada's `iotasigmaz` / `Tsigma`

Shimada's level-4 model is identified with Stage14 by

\[
\sigma=i\frac{1+r}{1-r},
\qquad
\left(\frac{\sigma+\sigma^{-1}}2\right)^2=-t^2,
\]

so the Weierstrass `x`-coordinate is the same one used above.

The computation package records

```text
GramS0
L40vs
SixFs
fsigma
zsigma
AutX0f
MWtorsigmaz
Tsigma
iotasigmaz
Galmu
Wout0
```

with `MWtorsigmaz` identifying the torsion group with `(Z/4Z)^2`, `Tsigma` giving translation matrices, and `iotasigmaz` giving elliptic inversion.

Therefore the Stage14 deck matrix is not to be guessed as bare `iotasigmaz`. It is

\[
\boxed{\delta=\tau_{T_0}\,\iota_{\sigma,z}}
\]

for the nonzero order-two section corresponding to `(x,y)=(0,0)`.

If the arbitrary `(Z/4Z)^2` label used in the data is not already matched to the displayed Weierstrass roots, there are only three nonzero order-two labels to test. Fiber-component incidence determines which one is `(0,0)`.

## 5. The split anticanonical condition becomes a root-pair identity

Suppose an irreducible singular `D in |L|` has rational normalization and its inverse image splits:

\[
\pi^{-1}(D)=C+\delta(C),
\]

with `C` a rational component. Since `pi^*D=M`,

\[
\boxed{M=C+\delta(C).}
\]

Adjunction on the K3 gives

\[
C^2=\delta(C)^2=-2.
\]

The Stage14 extremal degree is

\[
M\cdot C=4.
\]

These identities force

\[
\boxed{C\cdot\delta(C)=6}
\]

and, conversely, from only

\[
M^2=8,\quad C^2=-2,\quad M\cdot C=4
\]

one automatically gets

\[
(M-C)^2=-2,
\qquad C\cdot(M-C)=6.
\]

Thus the remaining geometry is naturally a search for root pairs summing to `M`, with the additional exact requirement

\[
\boxed{\delta(C)=M-C.}
\]

Effectivity, irreducibility of the image, Q-descent, and the physical open conditions remain mandatory; a numerical root alone is not enough.

## 6. A concrete intrinsic fingerprint for the physical class `M`

The old handoff said that the missing object was the coordinate vector of `M` in Shimada's basis. Stage14 geometry gives substantially more structure than only `M^2=8`.

Let

\[
f_r=\pi^*H_r,\qquad f_s=\pi^*H_s.
\]

These are the two symmetric genus-one/elliptic fiber classes. Let `e_{++},e_{+-},e_{-+},e_{--}` denote the four rational curves lying above the exceptional divisors of the four blown-up corners. Then

\[
\boxed{
M=2f_r+2f_s-e_{++}-e_{+-}-e_{-+}-e_{--}.
}
\]

The intersection data are

\[
f_r^2=f_s^2=0,
\qquad f_r\cdot f_s=2,
\]

\[
e_j^2=-2,
\qquad f_r\cdot e_j=f_s\cdot e_j=0,
\qquad e_j\cdot e_k=0\ (j\ne k),
\]

so immediately

\[
M^2=8,
\qquad M\cdot f_r=M\cdot f_s=4.
\]

This formula gives a direct way to construct the Shimada vector once the second symmetric fiber class and the four common corner components are located.

## 7. The eight `M`-null boundary roots are visible inside `L40`

The four `L`-null toric boundary curves on `Y` are

```text
r=+1, r=-1, s=+1, s=-1.
```

Their inverse images split, giving exactly eight `M`-null `(-2)` curves on `X`.

For the `r`-fibration, the modular coordinate

\[
\sigma=i\frac{1+r}{1-r}
\]

sends

```text
r=-1 -> sigma=0
r=+1 -> sigma=infinity.
```

Therefore four of the eight null roots are the two opposite non-exceptional components in each of the `I4` quadrangles `F_0` and `F_infinity` recorded by `SixFs`.

The other four null roots are the lifts of `s=+-1`. Stage14-4af already identified the `q=+-1` boundary with the rational order-four points halving the visible two-torsion point `(1,0)`. Hence these four roots are a four-element half-set of one nonzero order-two class in `MWtorsigmaz`.

The deck two-torsion `(0,0)` and the boundary two-torsion `(1,0)` are distinct. Thus, before using incidence data, there are only

\[
3\times2=6
\]

ordered label pairs `(T_deck,T_boundary)` to test inside `(Z/4Z)^2`.

This is a much smaller identification problem than an unconstrained search through a rank-20 lattice.

## 8. How to identify `f_s` and build `M` from Shimada data

Shimada proves that the orbit of the distinguished fiber class `fsigma` under `Aut(X0,h0)` has five elements. The data provide `AutX0h0`, so this orbit is directly computable.

For each candidate `f'` in the four nontrivial orbit elements:

1. require `fsigma.f'=2`, as for the two Stage14 rulings;
2. find roots in `L40vs` orthogonal to both fiber classes;
3. require the four corner exceptional roots to appear with the Stage14 `2 x 2` corner incidence pattern;
4. form
   \[
   m=2\,fsigma+2f'-\sum_{j=1}^4 e_j;
   \]
5. verify `m^2=8`, `m.fsigma=m.f'=4` and nefness;
6. verify that `m` is orthogonal to the eight boundary roots described in Section 7;
7. require `m` to be fixed by the candidate deck involution `delta`.

The correct Stage14 embedding must pass all of these tests simultaneously.

This turns the formerly unspecified `M`-coordinate problem into a finite cross-check over at most five fiber classes and six torsion-label pairings, before chamber/effectivity filtering.

## 9. Final degree-four root enumeration once `M` is fixed

After the Shimada coordinate vector `m` and deck matrix `delta` are fixed, enumerate integral classes `c in S0` satisfying

\[
\boxed{
 c^2=-2,\qquad f\cdot c=2,\qquad m\cdot c=4,
 \qquad c\delta=m-c.
}
\]

Then apply, in this order:

1. nef/effectivity chamber tests using `Wout0`;
2. remove `M`-null boundary contamination;
3. quotient by the subgroup preserving `m`, `f`, and `delta` (start from `AutX0f`);
4. impose `Galmu` / Q-descent;
5. impose the Stage14 real physical chamber and primitive positivity/order conditions.

Only candidates surviving all five gates can represent a physical Q-rational `M`-degree-four bisection.

## 10. Source-backed data contract from PR #185

The official Shimada computational-data note fixes the following conventions used by the planned enumerator:

- lattice vectors are row vectors in a fixed basis;
- lattice isometries act from the right;
- `GramS0` is the Gram matrix of the rank-20 Neron-Severi lattice `S0`;
- `L40vs` gives the 40 distinguished `(-2)`-curve classes;
- `Wout0` gives outer walls of the initial Borcherds chamber;
- `AutX0h0` has order 3840;
- `fsigma` and `zsigma` are the fiber and zero-section classes;
- `AutX0f` has order 768;
- `iotasigmaz` is elliptic inversion;
- `MWtorsigmaz` labels the 16 torsion sections by `(Z/4Z)^2`;
- `Tsigma` gives their translation matrices;
- `Galmu` has order 32.

Official sources:

```text
https://home.hiroshima-u.ac.jp/ichiro-shimada/ComputationData.html
https://home.hiroshima-u.ac.jp/ichiro-shimada/preprints/X0X3/PreprintX0X3/X0X3compdata.pdf
https://home.hiroshima-u.ac.jp/ichiro-shimada/preprints/X0X3/PreprintX0X3/shimadaX0X3Ver3.pdf
```

## 11. Deterministic audit

The script

```text
stages/stage14/scripts/14-4/shimada_lattice_interface_audit.py
```

checks without external data:

- the five-dimensional anticanonical basis above;
- the exact deck-involution formula on several rational symbolic-specialization identities;
- preservation of the elliptic equation and of the physical `q` coordinate;
- the involution identity;
- the root-complement intersection identities;
- the intrinsic formula for `M^2` and `M.f_r=M.f_s=4`.

It deliberately records

```text
FULL_SHIMADA_ENUMERATION_EXECUTED=false
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=false
```

until `S0S3.txt` and `Borcherds.txt` are actually ingested and the finite lattice enumeration is run.

## 12. Status

```text
STAGE14_4AJ=SHIMADA_LATTICE_INTERFACE_LOCKED
ANTICANONICAL_LINEAR_SYSTEM_PARAMETERIZED=true
STAGE14_DECK_INVOLUTION_ON_ELLIPTIC_FIBER_LOCKED=true
DECK_IS_TORSION_TRANSLATE_OF_SHIMADA_INVERSION=true
SPLIT_ANTICANONICAL_ROOT_PAIR_IDENTITY_LOCKED=true
PHYSICAL_M_INTRINSIC_FIBER_CORNER_FORMULA_LOCKED=true
M_SHIMADA_IDENTIFICATION_REDUCED_TO_FINITE_LABEL_SEARCH=true
FULL_SHIMADA_ENUMERATION_EXECUTED=false
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-4ak ingest Shimada S0 data, identify M/deck labels, enumerate effective M-degree-4 roots
```

The important advance is that 14-4ai's last geometric survivor is no longer an open-ended contact-discriminant search: it is an explicit finite lattice/root computation with a separately auditable coordinate-side anticanonical model.