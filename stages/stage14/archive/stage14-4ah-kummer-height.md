# Stage14-4ah — physical Kummer height and the minimum bisection target

## Purpose

Stage14-4ag reduced the raw-pair polynomial exponent to the first-hit frequency of active positive-rank Pythagorean fibers. Stage14-4ah asks what the **physical cutoff** `d<=B` is geometrically on the level-4 Kummer surface and what kind of rational curves can possibly create a square-root population.

The output of this substage is structural. It does **not** claim

\[
V(B)\asymp \sqrt B,
\qquad
O_{\rm pair}^{raw}(B)\asymp \sqrt B,
\qquad
N_2(B)\asymp \sqrt B.
\]

## 1. Ambient toric height recalled from the e-track

The independent Stage14-e3 control track resolves the two-face projective map on

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1)
\]

and identifies the physical projective line bundle as

\[
L=2H_1+2H_2-E_1-E_2-E_3-E_4=-K_Y.
\]

Its self-intersection is

\[
L^2=(2H_1+2H_2)^2-4=8-4=4.
\]

The projective morphism is

\[
\phi:Y\to\mathbf P^2,
\qquad
(q_1,q_2)\mapsto[1:t_1:t_2],
\]

with `phi^* O(1)=L`.

## 2. The space-square double cover has branch class `2L`

Use the actual Stage14 Pythagorean Euclid parameters

\[
t_1=\frac{2r}{1-r^2},
\qquad
t_2=\frac{2s}{1-s^2}.
\]

The condition

\[
1+t_1^2+t_2^2\in(\mathbf Q^\times)^2
\]

has common square numerator

\[
\boxed{
F(r,s)=(1+r^2)^2(1+s^2)^2-16r^2s^2.
}
\]

Homogeneously this is a divisor of bidegree `(4,4)` on `P1 x P1`.

The four base corners of the ambient projective map are, in the `r,s` coordinates,

\[
(r,s)=(\pm1,\pm1).
\]

At each corner,

\[
F=F_r=F_s=0,
\]

and the quadratic Hessian is nondegenerate:

\[
\operatorname{Hess}(F)=
\begin{pmatrix}32&0\\0&32\end{pmatrix}.
\]

Thus each corner is an ordinary double point of the branch divisor. Its strict transform on `Y` has class

\[
\begin{aligned}
B_X
&=4H_1+4H_2-2(E_1+E_2+E_3+E_4)\\
&=2L=-2K_Y.
\end{aligned}
\]

Therefore the resolved double cover

\[
\pi:X\to Y
\]

is the canonical K3 double cover associated with `L`.

This is the same K3 already identified in Stage14-4ag with the level-4 elliptic modular surface and, over `C`, `Km(E_i x E_i)`.

## 3. Exact physical polarization on the K3

Define

\[
\boxed{M=\pi^*L.}
\]

Equivalently, if

\[
\Phi=\phi\circ\pi:X\to\mathbf P^2,
\]

then

\[
\boxed{M=\Phi^*\mathcal O_{\mathbf P^2}(1).}
\]

Hence

\[
\boxed{M^2=2L^2=8.}
\]

Most importantly, this is not merely a comparable auxiliary height. On a primitive Stage14 point

\[
\Phi(P)=[e:x:y],
\]

with integer space diagonal,

\[
\boxed{
H_M(P)=\sqrt{e^2+x^2+y^2}=d.
}
\]

Thus the physical cutoff `d<=B` is exactly the bounded-height problem for `M` on the Stage14 arithmetic open set.

## 4. `M` is big and nef, but not ample

The anticanonical line bundle `L=-K_Y` is nef and big on the four-corner blowup but has zero intersection with the four strict toric boundary curves

\[
H_1-E_1-E_2,\quad
H_1-E_3-E_4,\quad
H_2-E_1-E_3,\quad
H_2-E_2-E_4.
\]

Consequently `M=pi^*L` is big and nef but not ample. Geometrically the four null boundary curves split under the K3 cover into eight `(-2)`-curves contracted by the physical projective morphism.

These curves lie on the toric boundary and do not contribute primitive positive Stage14 objects.

This point matters for the literature interface: McKinnon's product-Kummer point-counting theorem is stated for an **ample** height. Stage14 therefore does not import its asymptotic directly for `M`. Its accumulating-curve philosophy remains relevant, but the Stage14 height must be analyzed on its own nef boundary.

## 5. Minimum degree of a physical rational multisection

Let

\[
f:X\to\mathbf P^1_r
\]

be the first-face elliptic fibration. The singular fibers occur at

\[
r=0,\infty,\pm1,\pm i.
\]

The physical interval is

\[
0<r<1,
\]

so a physical rational curve cannot be a vertical component of a singular fiber. A smooth vertical fiber has genus one and is not rational.

Hence any physical rational curve `C` must dominate the first-face base. Put

\[
n=\deg(C\to\mathbf P^1_r)\ge1.
\]

The physical slope

\[
t(r)=\frac{2r}{1-r^2}
\]

has degree two as a map `P1_r -> P1_t`. Therefore

\[
\deg(t|_C)=2n.
\]

But `t=x/e` is a quotient of two global sections of `M`. On `C`, the degree of this rational function is at most the degree of `M|_C`. Thus

\[
\boxed{M\cdot C\ge2n.}
\]

If `n=1`, `C` is a rational section of the elliptic fibration. The geometric generic Mordell--Weil rank is zero, and Stage14-4af proved that all rational torsion sections are nonphysical. Therefore no physical rational section exists.

Consequently

\[
\boxed{n\ge2}
\]

for every physical rational curve, and hence

\[
\boxed{M\cdot C\ge4.}
\]

## 6. Why degree four is the exact square-root curve target

Suppose `C/Q` is a physical rational curve, `C` has a rational point, and

\[
m=M\cdot C>0.
\]

After normalization `C ~= P1`, the restricted height is an `O(m)` height. Standard bounded-height counting on `P1` gives polynomial exponent

\[
\boxed{2/m.}
\]

Since every physical rational curve satisfies `m>=4`, any **fixed** physical rational curve contributes at most

\[
B^{1/2+o(1)}.
\]

Equality of the polynomial exponent with `1/2` requires

\[
\boxed{M\cdot C=4.}
\]

The multisection inequality then forces `n=2`. Therefore the minimum rational-curve mechanism capable of producing the observed square-root scale is precisely

\[
\boxed{\text{a Q-rational M-degree-4 bisection}.}
\]

Stage14-4ah does not yet prove that such bisections exist in the physical open set, classify them, or prove that they dominate the active first-hit count. Those are the next obligations.

## 7. The finite square-root signal is not confined to the real cusps

A possible false explanation for the `V(B)/sqrt(B)` stability is that `M` is non-ample and active points accumulate only near the contracted toric boundary.

The exact Stage14 census was therefore re-read after deleting fixed neighborhoods of the real base endpoints `r=0,1`.

```text
B          all V    0.1<=r<=0.9    0.2<=r<=0.8    0.25<=r<=0.75
200k         155          134             105                92
500k         254          227             174               147
1m           347          307             238               197
2m           490          426             338               283
```

The decade effective exponents `200k -> 2m` are

```text
all                 0.4998643818582221
0.1 <= r <= 0.9     0.5023048007379113
0.2 <= r <= 0.8     0.5077274012077166
0.25 <= r <= 0.75   0.4879986081787350
```

Thus the finite square-root signal survives on fixed compact real subintervals well away from the two physical cusps. This is **finite evidence only**. It does not prove that an interior bisection family controls the asymptotic.

## 8. Triple condition as a relative double cover of the K3

The third-face condition is

\[
t_1^2+t_2^2\in(\mathbf Q^\times)^2.
\]

In `r,s` coordinates its zero numerator is

\[
\boxed{
G(r,s)=r^2(1-s^2)^2+s^2(1-r^2)^2.
}
\]

Again this has homogeneous bidegree `(4,4)`. At each `(+-1,+-1)` corner it has multiplicity two, with Hessian

\[
\begin{pmatrix}8&0\\0&8\end{pmatrix}.
\]

Hence its strict zero divisor on `Y` also has class

\[
2L.
\]

After pulling back to the space-square K3, adjoining the third square root produces a generically degree-two relative cover

\[
\rho:W\to X
\]

with branch class

\[
\boxed{2M.}
\]

Its rational image in `X(Q)` is therefore a type-II thin subset of the Kummer surface.

However, Stage14 has **no equidistribution or thin-set zero-density theorem for the actual K3 population ordered by the big-and-nef height `M`**. Thinness by itself does not imply

\[
T(B)=o(\sqrt B).
\]

So the triple-subtraction gate remains open.

## 9. Literature interface

- Ichiro Shimada, *The elliptic modular surface of level 4 and its reduction modulo 3* (2018), supplies the classical six-`I4`, Picard-20 level-4 K3 and its complex `Km(E_i x E_i)` identification used in Stage14-4ag.
- David McKinnon, *Counting Rational Points on K3 Surfaces* (2000), studies bounded-height points on product Kummer surfaces and finite accumulating curve strata for ample heights. Stage14 does not import that counting asymptotic because `M` is not ample.
- Damián Gvirtz-Chen, *Mazur's Conjecture and An Unexpected Rational Curve on Kummer Surfaces and their Superelliptic Generalisations* (2019), confirms that explicit rational curves on product Kummer surfaces are a real arithmetic mechanism. Stage14 does not identify its target degree-four bisections with the curves in that paper without an explicit divisor calculation.

No novelty claim is made for classical Kummer geometry or rational-curve constructions.

## 10. Locked conclusion

Stage14-4ah has now located the square-root mechanism much more precisely:

\[
\boxed{
\text{physical height}=H_M,
\quad M=\pi^*(-K_Y),
\quad M^2=8,
}
\]

and every physical rational curve obeys

\[
\boxed{M\cdot C\ge4.}
\]

Therefore a fixed rational accumulating curve can contribute polynomial exponent at most `1/2`, and the extremal target is an `M`-degree-four rational bisection.

What is still missing is exactly what now matters:

1. classify the `Q`-rational `M`-degree-four bisections of the level-4 Kummer surface;
2. determine which meet the physical primitive open set;
3. count their first-hit heights and decide whether they yield `V(B)=B^{1/2+o(1)}` or a full `c sqrt(B)` law;
4. restrict the relative triple cover to those curves and show whether the triple points have smaller order.

```text
STAGE14_4AH=COMPLETE
PHYSICAL_KUMMER_POLARIZATION_LOCKED=true
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8
PHYSICAL_POLARIZATION_BIG_NEF_NOT_AMPLE=true
PHYSICAL_RATIONAL_CURVE_M_DEGREE_LOWER_BOUND=4
SQRTB_MINIMAL_RATIONAL_CURVE_TARGET=M-degree-4 rational bisection
MCKINNON_DIRECT_ASYMPTOTIC_IMPORTED=false
FINITE_CORE_SQRTB_SIGNAL_SURVIVES=true
TRIPLE_RELATIVE_COVER_BRANCH_CLASS=2M
TRIPLE_TYPE_II_THIN=true
T_O_SQRT_B_PROVED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
NEXT=Stage14-4ai classify Q-rational M-degree-4 bisections and count their first-hit height; audit triple restriction on those curves
```
