# Stage15-2a — compactification / height / Picard-rank audit

Base: merged Stage15-2 (`PR #826`, main commit `994d6f8`). Stage15-2 proved only the polynomial exponent

\[
B\ll M_2(B)\ll B^{1+o(1)}
\]

and explicitly left the logarithmic exponent and asymptotic constant open. Its next target was to audit compactification, height, and Picard rank before importing any toric or del-Pezzo counting theorem.

## 1. Verdict

The shared-edge two-Pythagorean-face variety has a clean split toric compactification, but **the ambient toric asymptotic does not yet transfer directly to the exact Stage15 quantity `M_2(B)`**.

The geometric audit is:

```text
SHARED_EDGE_PROJECTIVE_SURFACE_IDENTIFIED=true
SURFACE_TYPE=split_singular_quartic_del_Pezzo_4A1
MINIMAL_RESOLUTION=Bl_4(P1xP1)_at_torus_fixed_corners
MINIMAL_RESOLUTION_TORIC=true
PICARD_RANK_RESOLUTION=6
PICARD_RANK_SINGULAR_CARTIER=2
ANTICANONICAL_MODEL=true
R_HEIGHT_ANTICANONICAL_COMPARABLE=true
TORIC_LOG_POWER_CANDIDATE=5
DIRECT_M2_TORIC_TRANSFER=false
DIRECT_M2_TORIC_TRANSFER_BLOCKER=exactly_two_arithmetic_subtraction
STAGE15_2A_EXIT=GEOMETRY_IDENTIFIED_TRANSFER_NOT_YET_JUSTIFIED
```

Thus Stage15-2a identifies the geometric source of a plausible `B(log B)^5` ambient scale, but **does not promote that candidate to a theorem for `M_2(B)`**.

## 2. Projective shared-edge surface

Choose a distinguished shared edge `e` and the two other legs `x,y`, with integral face diagonals `u,v`. The projective closure is

\[
X:\quad u^2=e^2+x^2,\qquad v^2=e^2+y^2
\]

in `P^4_[e:x:y:u:v]`.

This is a complete intersection of two quadrics, hence a quartic Gorenstein del-Pezzo model whenever the anticanonical interpretation is valid. It is not smooth.

The Jacobian drops rank exactly at the four rational points

\[
[0:\pm1:0:1:0],\qquad [0:0:\pm1:0:1].
\]

Near, for example, `[0:1:0:1:0]`, the first quadric solves `u` formally/analytically because its `u`-derivative is nonzero. The remaining local equation is

\[
v^2-e^2-y^2=0,
\]

which is a nondegenerate quadratic cone in three variables. Hence each of the four singularities is type `A_1`. Therefore `X` is the split singular quartic del-Pezzo surface of type `4A1` arising from this shared-edge model.

## 3. Toric parametrization and minimal resolution

Take homogeneous parameters `(m:n)` and `(r:s)` on `P^1 x P^1`. The standard two Pythagorean parametrizations synchronize the common leg through

\[
\begin{aligned}
e&=4mnrs,\\
x&=2rs(m^2-n^2),\\
y&=2mn(r^2-s^2),\\
u&=2rs(m^2+n^2),\\
v&=2mn(r^2+s^2).
\end{aligned}
\]

All five coordinates have bidegree `(2,2)` and satisfy the two quadrics identically.

The linear system has exactly four base points, the torus-fixed corners

```text
(m:n) in {(1:0),(0:1)}
(r:s) in {(1:0),(0:1)}.
```

Let

\[
Y=\operatorname{Bl}_{4}(P^1\times P^1)
\]

at those four corners. The rational map above resolves to a morphism from `Y` to `X`.

If `F_1,F_2` are the two ruling classes and `E_1,...,E_4` the exceptional divisors, then

\[
-K_Y=2F_1+2F_2-E_1-E_2-E_3-E_4.
\]

The five displayed coordinates are precisely sections of this divisor class. Thus the morphism is the anticanonical morphism.

Each of the four coordinate boundary fibers originally has self-intersection `0` and passes through two of the blown-up corners, so its strict transform has self-intersection `-2`. These four disjoint `(-2)`-curves are contracted by the anticanonical map to the four `A_1` points above.

Because the four blow-ups are torus-fixed, `Y` remains a smooth split toric surface.

## 4. Degree and Picard ranks

For `P^1 x P^1`, `K^2=8`. Four blow-ups give

\[
K_Y^2=8-4=4.
\]

Hence the anticanonical image is degree four, as expected from the intersection of two quadrics.

The geometric/rational Picard rank of the split resolution is

\[
\rho(Y)=2+4=6.
\]

The four independent contracted `A_1` root classes reduce the Cartier Neron-Severi rank of the singular model to

\[
\rho_{\mathrm{Cartier}}(X)=6-4=2.
\]

For Manin-type counting on a singular del-Pezzo surface, the relevant logarithmic exponent is naturally expressed on the minimal desingularization. Thus the toric/Manin candidate is

\[
(\log B)^{\rho(Y)-1}=(\log B)^5.
\]

This is a **candidate inherited from the compactification**, not yet a proved asymptotic for the Stage15 exactly-two count.

## 5. Stage15 geometric height versus anticanonical height

On the real shared-edge locus relevant to boxes,

\[
u^2=e^2+x^2,\qquad v^2=e^2+y^2.
\]

Let

\[
H_\infty=\max(|e|,|x|,|y|,|u|,|v|)
\]

for primitive projective coordinates and let

\[
R=\sqrt{e^2+x^2+y^2}.
\]

Then

\[
H_\infty\le R\le \sqrt3\,H_\infty.
\]

Indeed `|e|,|x|,|y|<=R`, while `u^2=e^2+x^2<=R^2` and `v^2=e^2+y^2<=R^2`; the reverse inequality follows from the three edge coordinates being bounded by `H_inf`.

Therefore the Stage15 cutoff `R<=B` is equivalent up to fixed constants to the standard projective anticanonical sup-height cutoff on this model. This preserves polynomial and logarithmic exponents.

The primitive condition also matches projective primitiveness: if `gcd(e,x,y)=1`, then no integer greater than one divides all five projective coordinates.

## 6. What toric counting would count

Classical height-zeta results for smooth projective toric varieties apply to `Y` and its dense torus, with anticanonical height as a standard case. The geometry above therefore makes a `B(log B)^5` law a natural expectation for the **full oriented shared-edge rational-point population on the torus**, after the usual removal of accumulating boundary strata and with a positive archimedean chamber restriction.

The strict positivity/order conditions used for physical cuboids are semialgebraic real-place restrictions and are compatible in principle with adelic/equidistribution formulations. Finite sign choices and canonical ordering do not alter an exponent.

However, the Stage15 target is not the full torus population.

## 7. Why direct transfer to `M_2(B)` is blocked

`M_2(B)` requires **exactly two** integral face diagonals. On the shared-edge surface, the forbidden third integral face is

\[
x^2+y^2=z^2
\]

for some integer/rational `z`.

This is not the deletion of a fixed Zariski-closed subset of `X`. It is the image of rational points on the generically degree-two cover

\[
W:\quad z^2=x^2+y^2\longrightarrow X.
\]

Thus the Euler-brick/triple-face population is an arithmetic thin-type subset, not an ordinary boundary divisor. A toric asymptotic for all rational points on the dense torus does **not by itself** prove that subtracting this cover-image changes only a lower-order term.

Consequently the implication

```text
full shared-edge toric count ~ c B(log B)^5
=> M2(B) ~ c' B(log B)^5
```

is not licensed at Stage15-2a.

A quantitative theorem showing that the third-face-square cover contributes `o(B(log B)^5)` in the same height/chamber is required before that transfer.

## 8. Relation to the explicit Stage15-2 family

The Stage15-2 family

\[
e=4pq,\quad x=4p^2-q^2,\quad y=4q^2-p^2
\]

is obtained from the toric parametrization by the two Euclid pairs

\[
(m,n)=(2p,q),\qquad (r,s)=(2q,p),
\]

up to the synchronized projective scaling. The exact identity

\[
R^2=17(p^4+q^4)
\]

is therefore a two-dimensional subcone calculation inside the same anticanonical model, not a separate geometry.

This explains why the Stage15-2 linear lower bound is compatible with, but much weaker than, a possible `B(log B)^5` total law.

## 9. Literature gate

Primary references used only for the transfer audit, not as substitutes for the explicit calculations above:

1. V. Batyrev and Y. Tschinkel, *Manin's conjecture for toric varieties*, arXiv:alg-geom/9510014. Proves the anticanonical Manin asymptotic for smooth projective toric varieties.
2. V. Batyrev and Y. Tschinkel, *Height zeta functions of toric varieties*, arXiv:alg-geom/9606003. Treats height zeta functions and more general line bundles on toric varieties.
3. U. Derenthal, *Singular del Pezzo surfaces whose universal torsors are hypersurfaces*, arXiv:math/0604194. Gives the generalized-del-Pezzo/Cox-ring framework relevant to singular del-Pezzo counting.
4. Z. Huang, *Equidistribution of rational points and the geometric sieve for toric varieties*, arXiv:2111.01509. Supplies modern equidistribution/geometric-sieve tools for smooth split toric varieties and adelic restrictions.

These references support the statement that the toric geometry is promising. None is invoked here as an off-the-shelf theorem that already removes the specific third-face-square cover in the Stage15 count.

## 10. Next target

The next mathematically narrow task should be the exact subtraction gate:

> Prove or disprove that the rational points on `z^2=x^2+y^2` lying above the positive shared-edge torus contribute `o(B(log B)^5)` with the Stage15 anticanonical-equivalent height.

Until that is done, retain

```text
M2_ASYMPTOTIC_PROVED=false
M2_LOG_POWER_PROVED=false
M2_LOG_POWER_CANDIDATE=5
```

Stage15-2a therefore closes the compactification/height/Picard-rank audit without over-promoting the toric heuristic.