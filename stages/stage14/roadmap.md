# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain the primitive canonical exactly-two-face population inside the integer-space-diagonal cuboid family

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

```text
a-direction = ab+ac only
b-direction = ab+bc only
c-direction = ac+bc only
```

## 14-1 — Definition and counting interface

Status: [x] Complete.

## 14-2 — Complete finite enumeration

Status: [x] Complete. Two independent exact generation routes agree through `B=2,000,000`.

## 14-3 — Finite directional reconnaissance

Status: [x] Complete. No finite fit was promoted to an asymptotic theorem.

## Frozen Stage13 upstream contract

Stage13 freezes `R03 + Stage13-12ag`, including

\[
N_2(B)=o(B(\log B)^3).
\]

The fixed-prime overlap sieve gives zero density but no growing-modulus theorem and no explicit power saving in `B`.

## 14-4 — True total growth order

Status: [>] Active.

### 14-4aa — independent two-face parametrization

Status: [x] Complete. All directions are chambers of one shared-edge arithmetic object.

### 14-4ab — exact matching bijection

Status: [x] Complete. Primitive face-pair data give a fixed raw pair incidence with fiber multiplicity one.

### 14-4ac — rational-slope height envelope

Status: [x] Complete.

\[
(e,x,y)=L(1,t_1,t_2),
\qquad d=L\sqrt{1+t_1^2+t_2^2},
\qquad L=\operatorname{lcm}(S_1,S_2).
\]

The pre-space denominator envelope is `B(log B)^7`; `sqrt(B)` was retained only as a finite candidate.

### 14-4ad — elliptic square thinning

Status: [x] Complete.

The global square condition is

\[
(X_1X_2)^2+(gd)^2=(H_1H_2)^2
\]

and, after fixing the first face,

\[
\boxed{E_{t_1}:Y^2=X(X-1)(X+t_1^2)}.
\]

The family is non-isotrivial. R03 supplies local obstructions but not the missing power exponent.

### 14-4ae — fiber/base height and generic rank

Status: [x] Complete.

Write the second rational-circle parameter as reduced `q=u/v`, `0<u<v`. Its primitive face is

\[
S_2=(v^2-u^2)/\delta,
\quad X_2=2uv/\delta,
\quad H_2=(u^2+v^2)/\delta,
\quad \delta\in\{1,2\}.
\]

Hence

\[
\boxed{v^2/2<H_2<2v^2.}
\]

The original physical height satisfies uniformly

\[
\boxed{
\frac{S_1H_2}{\sqrt2\,g}<d<\frac{\sqrt3 S_1H_2}{g},
\qquad g=(S_1,S_2).
}
\]

Therefore the natural fiber cutoff is

\[
\boxed{v\asymp\sqrt{Bg/S_1}.}
\]

This is a structural source for a square root in the fiber height, but not a proof that the total population is `sqrt(B)`.

The elliptic birational map has exact inverse

\[
\boxed{q=X/(sY),\qquad s=S_1/H_1.}
\]

For a fixed fiber, standard height theory gives `h(q)=2 hhat+O_t1(1)`, hence only polylogarithmic point growth for fixed Mordell--Weil rank.

The elliptic surface

\[
y^2=x(x-1)(x+t^2)
\]

has

\[
\Delta=16t^4(1+t^2)^2,
\qquad c_4=16(1+t^2+t^4),
\]

and geometric fiber configuration

```text
I4, I4, I2, I2.
```

The Euler sum is `12`, so it is a rational elliptic surface. Shioda--Tate gives

\[
\boxed{\operatorname{rank}E(\overline{\mathbf Q}(t))=0.}
\]

Thus Stage14 is not averaging points on a positive-rank generic family. It must count specializations with rank jump and/or extra torsion that possess sufficiently small physical points.

A rigorous raw-pair height skeleton is now available:

\[
\sum_{F_1:H_1<B}\sum_{g|S_1}
\mathcal N_{F_1,g}\!\left(c_-\sqrt{Bg/S_1}\right)
\le O_{\rm pair}^{raw}(B)
\le
\sum_{F_1:H_1<B}\sum_{g|S_1}
\mathcal N_{F_1,g}\!\left(c_+\sqrt{Bg/S_1}\right),
\]

with `c_-=(2sqrt(3))^(-1/2)` and `c_+=2^(3/4)`.

Exactly-two still has a separate gate:

\[
\boxed{O_{\rm pair}^{raw}(B)=N_2(B)+3T(B).}
\]

No `T=o(sqrt(B))` theorem is currently known.

Decision:

```text
STAGE14_4AE=COMPLETE
UNIFORM_SECOND_FACE_HEIGHT_COMPARISON=true
SECOND_FACE_Q_DENOMINATOR_SQUARE_ROOT_HEIGHT=true
ELLIPTIC_Q_INVERSE=q=X/(sY)
FIXED_FIBER_POINT_GROWTH_POLYLOGARITHMIC=true
ELLIPTIC_SURFACE_FIBERS=I4_I4_I2_I2
GEOMETRIC_GENERIC_MW_RANK=0
GLOBAL_PROBLEM=SMALL_POINT_RANK_JUMP_OR_EXTRA_TORSION_SPECIALIZATIONS
RAW_PAIR_HEIGHT_SUM_LOCKED=true
RAW_PAIR_TO_EXACTLY_TWO_REQUIRES_TRIPLE_CONTROL=true
SQRT_B_STRUCTURAL_HEIGHT_SOURCE_IDENTIFIED=true
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
```

Artifacts:

```text
stages/stage14/archive/stage14-4ae-height-rank.md
stages/stage14/scripts/14-4/height_rank_audit.py
stages/stage14/data/14-4/height_rank_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

### 14-4af — small-point specialization and triple-subtraction analysis

Status: [>] Next.

Purpose:

- characterize which Pythagorean base specializations `t1=X1/S1` acquire non-generic rational points;
- separate rank jumps from extra-torsion specializations;
- obtain quantitative information on the first non-torsion canonical height / regulator / successive minima;
- make the `q`-height versus canonical-height comparison uniform enough to sum over the base;
- incorporate `gcd(S1,S2)=g` and frozen R03 local restrictions;
- simultaneously analyze the triple locus strongly enough to decide whether a raw-pair growth law transfers to exactly-two;
- only then promote or reject a `sqrt(B)`-type total law.

## 14-5 — Directionwise asymptotic structure

Status: pending Stage14-4.

## Scope boundary

No true growth exponent, leading constant, limiting directional ratio, eventual leader, Euler-side equality, or perfect-cuboid nonexistence theorem is currently established for Stage14.

```text
NEXT=Stage14-4af small-point specialization and triple-subtraction analysis
```
