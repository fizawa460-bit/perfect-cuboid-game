# Stage14-4ae — elliptic-fibration height/rank analysis

## Purpose

Stage14-4ad reduced the raw two-face square condition to the non-isotrivial elliptic family

\[
E_{t_1}:Y^2=X(X-1)(X+t_1^2),
\qquad t_1=X_1/S_1,
\]

but did not yet connect the original integer-space-diagonal cutoff `d<=B` to a natural height on the fiber. Stage14-4ae performs that translation and determines which part of the growth problem is genuinely elliptic-rank/height arithmetic.

The main conclusions are:

1. the physical height is uniformly comparable to `(S1/g) H2`, independently of direction;
2. the rational-circle parameter `q=u/v` of the second face satisfies `H2 asymp v^2`, so the induced fiber cutoff is genuinely of square-root size
   \[
   v\asymp\sqrt{Bg/S_1};
   \]
3. the quartic-to-elliptic birational map has the exact inverse coordinate
   \[
   q=\frac{X}{sY},\qquad s=S_1/H_1;
   \]
4. for one fixed fiber, Mordell--Weil growth under this cutoff is only polylogarithmic in `B`;
5. the elliptic surface attached to `E_t` has geometric generic Mordell--Weil rank `0`;
6. therefore the true power of `B` is controlled by specializations carrying sufficiently small non-torsion points or extra torsion, together with the gcd/lcm coupling;
7. the elliptic fibration counts raw pair incidences. Passing to exactly-two still requires independent control of the triple population at the eventual true scale.

No `sqrt(B)` asymptotic or power bound is proved here.

---

## 1. Exact physical height in terms of the second primitive face

Use the Stage14-4ab data

\[
F_i=(S_i,X_i,H_i),\qquad S_i^2+X_i^2=H_i^2,
\]

with

\[
g=\gcd(S_1,S_2),
\qquad
L=\operatorname{lcm}(S_1,S_2)=\frac{S_1S_2}{g}.
\]

The physical edges are

\[
e=L,
\qquad
x=\frac{S_2}{g}X_1,
\qquad
y=\frac{S_1}{g}X_2,
\]

and `x<y`.

Let

\[
Q_2:=\max(S_2,X_2).
\]

Since the second primitive face is a right triangle,

\[
Q_2<H_2<\sqrt2\,Q_2.
\]

The Stage14-4ac max-height is

\[
M=L\max(1,t_2)
=\frac{S_1}{g}\max(S_2,X_2)
=\frac{S_1}{g}Q_2.
\]

Together with

\[
M<d<\sqrt3\,M,
\]

this gives the uniform direction-independent comparison

\[
\boxed{
\frac{S_1H_2}{\sqrt2\,g}
<d<
\frac{\sqrt3\,S_1H_2}{g}.
}
\]

Consequently

\[
\boxed{
H_2\le \frac{Bg}{\sqrt3\,S_1}
\Longrightarrow d<B
\Longrightarrow
H_2<\frac{\sqrt2\,Bg}{S_1}.
}
\]

This is the first uniform conversion of the original Euclidean cutoff into a one-fiber arithmetic height. It does not use a chamber-specific approximation.

A separate exact identity from Stage14-4ad is

\[
d=\frac{H_1H_2}{g}\sqrt{1-\rho_1^2\rho_2^2},
\qquad \rho_i=X_i/H_i,
\]

but the max-height argument above is stronger for a uniform comparison because it removes the potentially small shape factor.

Also, since

\[
d^2=\left(\frac{S_2}{g}H_1\right)^2+\left(\frac{S_1}{g}X_2\right)^2,
\]

we always have `H1<d`, so only first-face data with `H1<B` can contribute.

---

## 2. The second rational-circle parameter has square-root height

For the second face write the Stage14-4ad rational-circle parameter as

\[
q=\frac uv,
\qquad
0<u<v,
\qquad
\gcd(u,v)=1.
\]

The unit-circle formulas are

\[
\frac{X_2}{H_2}=\frac{2uv}{u^2+v^2},
\qquad
\frac{S_2}{H_2}=\frac{v^2-u^2}{u^2+v^2}.
\]

Let

\[
\delta=\gcd(v^2-u^2,2uv,u^2+v^2)\in\{1,2\}.
\]

Then the primitive second face is exactly

\[
\boxed{
S_2=\frac{v^2-u^2}{\delta},
\qquad
X_2=\frac{2uv}{\delta},
\qquad
H_2=\frac{u^2+v^2}{\delta}.
}
\]

Hence

\[
\boxed{
\frac{v^2}{2}<H_2<2v^2.
}
\]

Combining this with Section 1, put

\[
Q_B(F_1,g):=\sqrt{\frac{Bg}{S_1}}.
\]

Then the universal constants

\[
c_-=(2\sqrt3)^{-1/2},
\qquad
c_+=2^{3/4}
\]

satisfy

\[
\boxed{
v\le c_-Q_B(F_1,g)
\Longrightarrow d<B
\Longrightarrow
v<c_+Q_B(F_1,g).
}
\]

Thus the square-root cutoff visible in the finite data has an exact structural source: the natural projective height of `q` is the square root of the primitive Pythagorean hypotenuse height.

This does **not** yet prove that the total population is `sqrt(B)`. The first-face base and gcd strata still have to be summed.

---

## 3. Exact inverse map from the elliptic fiber to `q`

Stage14-4ad defines

\[
r=X_1/H_1,
\qquad
s=S_1/H_1,
\qquad
r^2+s^2=1,
\]

and obtains

\[
E_{t_1}:Y^2=X(X-1)(X+t_1^2),
\qquad t_1=r/s.
\]

From the Jacobi quartic coordinates,

\[
X_0=\frac{W+1}{q^2},
\quad
U=A+X_0,
\quad
V=\frac q2(X_0^2-1),
\]

and

\[
U=2s^2X,
\qquad
V=2s^3Y.
\]

Since `A=2s^2-1`, one has

\[
X_0=1+2s^2(X-1),
\]

so

\[
X_0^2-1
=4s^4(X-1)(X+t_1^2).
\]

Therefore

\[
q=\frac{2V}{X_0^2-1}
=\frac{Y}{s(X-1)(X+t_1^2)}.
\]

Using the elliptic equation,

\[
Y^2=X(X-1)(X+t_1^2),
\]

we obtain the particularly simple identity

\[
\boxed{
q(P)=\frac{X(P)}{sY(P)}.
}
\]

The boundary/torsion charts where the displayed expression has `0/0` or a pole are handled separately; physical second faces have finite `q in (0,1)`.

Thus the original cuboid height induces a standard rational-function height on the elliptic fiber.

---

## 4. Fixed-fiber elliptic height is only polylogarithmic

Let

\[
h(q)=\log H(q)
\]

be the usual logarithmic projective height on `Q`, where for reduced `q=u/v`, `H(q)=max(|u|,|v|)=v` on the physical chart.

For one fixed nonsingular fiber `E_{t_1}`, `q(P)` is a rational function of degree `2`. Standard elliptic height theory therefore gives

\[
\boxed{
h(q(P))=2\widehat h_{E_{t_1}}(P)+O_{t_1}(1).}
\]

The constant is harmless on a fixed fiber. A **uniform** version as `t_1` varies is a separate problem and is not assumed here.

The physical cutoff from Section 2 gives

\[
h(q(P))\le \frac12\log\frac{Bg}{S_1}+O(1),
\]

hence on a fixed fiber

\[
\widehat h(P)
\le
\frac14\log\frac{Bg}{S_1}+O_{t_1}(1).
\]

If the fixed fiber has Mordell--Weil rank `r`, then `E(Q)/E(Q)_tors` is a rank-`r` Euclidean lattice under the Neron--Tate pairing. Geometry of numbers gives, for fixed `E`,

\[
\#\{P:\widehat h(P)\le T\}=O_E(T^{r/2}),
\]

with the usual regulator-dependent leading volume when `r>0`.

Therefore for one fixed first face,

\[
\boxed{
\#\{\text{physical candidate points with }d\le B\}
=O_{F_1}((\log B)^{r(F_1)/2}).
}
\]

So a power such as `B^(1/2)` cannot be generated by proliferation of points on one fixed elliptic curve. Any power of `B` must arise from summing a varying family of specializations and gcd strata.

---

## 5. The generic elliptic-surface rank is zero

Now regard

\[
\mathscr E:\quad y^2=x(x-1)(x+t^2)
=x^3+(t^2-1)x^2-t^2x
\]

as an elliptic surface over the `t`-line.

For this Weierstrass model,

\[
\boxed{
\Delta(t)=16t^4(1+t^2)^2,
\qquad
c_4(t)=16(1+t^2+t^4).
}
\]

Hence over `Qbar`:

- `t=0`: `ord Delta=4`, `c4!=0`, so the fiber is `I4`;
- `t=+i`: `ord Delta=2`, `c4!=0`, so the fiber is `I2`;
- `t=-i`: likewise `I2`.

At infinity put `u=1/t` and scale

\[
x=X/u^2,
\qquad
y=Y/u^3.
\]

The minimal equation becomes

\[
Y^2=X(X+1)(X-u^2),
\]

with

\[
\Delta_\infty(u)=16u^4(1+u^2)^2,
\qquad
c_{4,\infty}(u)=16(1+u^2+u^4),
\]

so the fiber at infinity is another `I4`.

Thus the geometric singular-fiber configuration is

\[
\boxed{I_4,I_4,I_2,I_2.}
\]

The Euler numbers sum to `12`, so this is a rational elliptic surface. Over `Qbar`, a rational elliptic surface has Picard number `10`.

The reducible-fiber root ranks are

\[
(4-1)+(4-1)+(2-1)+(2-1)=8.
\]

Shioda--Tate therefore gives

\[
\boxed{
\operatorname{rank}\mathscr E(\overline{\mathbf Q}(t))
=10-2-8=0.
}
\]

This is stronger than mere non-isotriviality: the family has no non-torsion generic section even after extending constants to `Qbar`.

Consequently Stage14 physical points arise from **special fibers**: rank-jump specializations and/or specializations with additional torsion. The actual counting problem is therefore a small-point specialization problem, not an average of a positive generic rank.

The fiber configuration `I4,I4,I2,I2` is one of the classical semistable rational elliptic-surface configurations; this recognition is only supplementary, because the rank calculation above is self-contained once the four fiber types are known.

---

## 6. The real global target: small points on specializations

For one first face `F_1`, let

\[
r(F_1)=\operatorname{rank}E_{t_1}(\mathbf Q)
\]

and, when the rank is positive,

\[
\lambda_1(F_1)
=\min\{\widehat h(P):P\in E_{t_1}(\mathbf Q)\setminus E_{t_1}(\mathbf Q)_{tors}\}.
\]

A rank jump by itself is not enough for Stage14. The specialization must possess a point whose `q`-height is below the square-root cutoff from Section 2.

Equivalently, after a uniform height comparison is established, a non-torsion Stage14 point requires roughly

\[
\lambda_1(F_1)
\lesssim
\frac14\log\frac{Bg}{S_1}
+\text{base-height correction}.
\]

So root-number or rank-parity information alone cannot determine the Stage14 count. One needs information on the **height of the first small point / regulator / successive minima** in the rank-jump fibers.

This is the precise sense in which Stage14-4ae turns the vague phrase "average rank problem" into a sharper "average small-point specialization problem".

---

## 7. Rigorous counting skeleton

For a first primitive face `F_1=(S_1,X_1,H_1)` and a divisor `g|S_1`, define

\[
\mathcal N_{F_1,g}(Q)
\]

to be the number of physical, non-boundary rational points `P` on `E_{t_1}(Q)` such that:

- `q(P)=u/v` is reduced with `0<u<v` and `v<=Q`;
- the reconstructed primitive second face has `gcd(S_1,S_2)=g`;
- the ordering `t_1<t_2` holds;
- the point satisfies the raw pair condition (already encoded by the elliptic fiber).

Then only `H_1<B` can contribute, and Sections 1--2 give the universal bracket

\[
\boxed{
\sum_{F_1:H_1<B}\sum_{g|S_1}
\mathcal N_{F_1,g}\!\left(c_-\sqrt{\frac{Bg}{S_1}}\right)
\le O_{\rm pair}^{raw}(B)
\le
\sum_{F_1:H_1<B}\sum_{g|S_1}
\mathcal N_{F_1,g}\!\left(c_+\sqrt{\frac{Bg}{S_1}}\right),
}
\]

where

\[
c_-=(2\sqrt3)^{-1/2},
\qquad
c_+=2^{3/4}.
\]

This is now a concrete fiber/base height sum. The remaining analytic inputs are visible rather than hidden:

1. distribution of specializations with a physical non-torsion point or extra torsion;
2. uniform comparison between `q`-height and canonical height as the base varies;
3. rank/regulator/successive-minimum control on the contributing fibers;
4. the arithmetic condition `gcd(S_1,S_2)=g`;
5. the Pythagorean restriction on the first-face base itself;
6. local restrictions inherited from Stage13 R03.

---

## 8. Raw-pair versus exactly-two warning

The elliptic fibration counts **raw pair incidences**. A triple-face object appears in all three raw pair ledgers.

Thus

\[
\boxed{
O_{\rm pair}^{raw}(B)
=O_{ab,ac}+O_{ab,bc}+O_{ac,bc}
=N_2(B)+3T(B).
}
\]

Finite data have `T(B)=0` through `B=2,000,000`, so raw-pair total and exactly-two total coincide there. Asymptotically this is not known.

Frozen R03 gives only

\[
T(B)=o(B(\log B)^3),
\]

which is not enough to conclude `T=o(sqrt(B))` or even that `T` is lower order relative to a future raw-pair law near `sqrt(B)`.

Therefore a proof of a `sqrt(B)` law for the elliptic raw-pair count would still require a separate triple-subtraction theorem before it becomes a theorem for `N_2(B)`.

Stage14-4ae keeps this gate explicit.

---

## 9. Literature collision / reusable-method note

Two nearby results are relevant but do not solve the Stage14 height count.

Jonathan R. Love, *Root numbers of a family of elliptic curves and two applications*, Indagationes Mathematicae 35 (2024), arXiv:2201.04708, studies the related family

\[
y^2=x(x+1)(x+t^2)
\]

and applications to products of slopes of rational right triangles. This is an **ADJACENT_RESULT / REUSABLE_METHOD**, not an exact collision with the Stage14 family `x(x-1)(x+t^2)` and its lcm-denominator height.

Jonathan R. Love, *Rational configuration problems and a family of curves*, Journal of Number Theory 269 (2025), arXiv:2310.02534, proves density-zero and rational-point statements for a broader genus-one configuration family. This is also a **REUSABLE_METHOD** for specialization sparsity, not a ready-made Stage14 asymptotic.

The classical `I4,I4,I2,I2` semistable rational elliptic-surface configuration is known in the Beauville list. Stage14 does not make a novelty claim for the elliptic-surface geometry itself.

```text
LITERATURE_EXACT_COLLISION_WITH_STAGE14_LCM_HEIGHT=NOT_FOUND
NOVELTY_BY_SEARCH_ABSENCE=false
```

---

## 10. Deterministic audit

The Stage14-4ae audit reuses the independent face-pair enumeration at `B=10000` and checks all 25 raw-pair incidences. It verifies for every hit:

- exact reconstruction of the second primitive face from reduced `q=u/v`;
- `v^2/2 < H2 < 2v^2`;
- the uniform physical height inequality
  \[
  S_1H_2/(\sqrt2 g)<d<\sqrt3 S_1H_2/g;
  \]
- the elliptic equation;
- the exact inverse coordinate `q=X/(sY)`.

It again reproduces exactly-two `(9,11,5)` and `T=0`.

The audit also records the self-contained elliptic-surface calculation

```text
Delta(t)=16 t^4 (1+t^2)^2
c4(t)=16(1+t^2+t^4)
fibers over Qbar: I4 at 0, I2 at +i, I2 at -i, I4 at infinity
Euler sum=12
rational elliptic surface Picard rank=10
reducible-fiber root rank=8
Shioda-Tate geometric generic MW rank=0
```

Artifacts:

```text
stages/stage14/scripts/14-4/height_rank_audit.py
stages/stage14/data/14-4/height_rank_audit.json
```

---

## 11. Stage14-4ae decision

```text
STAGE14_4AE=COMPLETE

UNIFORM_SECOND_FACE_HEIGHT_COMPARISON=true
SECOND_FACE_Q_DENOMINATOR_SQUARE_ROOT_HEIGHT=true
ELLIPTIC_Q_INVERSE=q=X/(sY)
FIXED_FIBER_POINT_GROWTH_POLYLOGARITHMIC=true

ELLIPTIC_SURFACE_FIBERS=I4_I4_I2_I2
ELLIPTIC_SURFACE_RATIONAL=true
GEOMETRIC_GENERIC_MW_RANK=0
GLOBAL_PROBLEM=SMALL_POINT_RANK_JUMP_OR_EXTRA_TORSION_SPECIALIZATIONS

RAW_PAIR_HEIGHT_SUM_LOCKED=true
RAW_PAIR_TO_EXACTLY_TWO_REQUIRES_TRIPLE_CONTROL=true

SQRT_B_STRUCTURAL_HEIGHT_SOURCE_IDENTIFIED=true
SQRT_B_ASYMPTOTIC_CLAIM=false
SQRT_B_RIGOROUS_UPPER_BOUND=false
SQRT_B_RIGOROUS_LOWER_BOUND=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
LEADING_CONSTANT_IDENTIFIED=false

NEXT=Stage14-4af small-point specialization and triple-subtraction analysis
```

The `sqrt(B)` candidate survives, and Stage14-4ae now explains why a square root naturally enters the **fiber height**. It does not yet prove that the sum over all base fibers has square-root order.