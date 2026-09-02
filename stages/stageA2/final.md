# StageA2 final — self-contained closure of the published equation-(6) `-18` anchor family

```text
STAGE=StageA2
STATUS=CLOSED_PUBLISHED_MINUS18_FAMILY_EXCLUSION
SOURCE=Bremner-Elsholtz-Ulas_equation_6
SOURCE_COEFFICIENT=-18
PUBLISHED_EQUATION6_ANCHOR_NONDEGENERATE_POINTS=0
FAMILY_SPECIFIC_EXCLUSION_COMPLETE=true
GENERAL_COVERAGE_PROVED=false
PERFECT_CUBOID_FOUND=false
ARBITRARY_PERFECT_CUBOID_NONEXISTENCE_PROVED=false
```

This file is the permanent mathematical closeout surface for StageA2. The proof below is self-contained at the level required by `docs/FINAL-CLOSEOUT-STANDARD.md`: repository paths, hashes, audits and scripts are recorded only after the mathematics and are not needed to understand the exclusion.

## 1. Exact theorem and population

The source is Andrew Bremner, Christian Elsholtz and Maciej Ulas, *There are infinitely many Hilbert cubes of dimension 3 in the set of squares*, arXiv:2604.05459v1, PDF p.13, equation (6).

For rational projective parameter pairs

\[
[c:d]\in\mathbf P^1(\mathbf Q),\qquad [G:H]\in\mathbf P^1(\mathbf Q),
\]

the equation-(6) base term has the form

\[
a_0=(c^2+d^2)^2F_{18}(c,d,G,H)^2,
\]

where

\[
\begin{aligned}
F_{18}={}&-4c^2d^4(c^2-d^2)G^4\\
&+(c^8-18c^4d^4+d^8)G^3H\\
&+8c^2d^2(c^2-d^2)(2c^2+d^2)G^2H^2\\
&-(c^8-18c^4d^4+d^8)GH^3\\
&-4c^2d^4(c^2-d^2)H^4.
\end{aligned}
\]

StageA2 concerns the nondegenerate anchor population

\[
cdGH(c^2-d^2)(G^2-H^2)\ne0,
\qquad a_0=0.
\]

Because a nontrivial rational pair `[c:d]` cannot satisfy `c^2+d^2=0`, the anchor condition is exactly

\[
F_{18}(c,d,G,H)=0.
\]

The StageA2 theorem is

\[
\boxed{\text{There is no rational parameter pair in this nondegenerate equation-(6) anchor population.}}
\]

Equivalently, the published equation-(6) `-18` anchor boundary has zero nondegenerate rational points.

This theorem is deliberately family-specific. It does not assert that equation (6) parametrizes all anchored Hilbert cubes or all perfect cuboids.

## 2. Source lock and the `-18` coefficient

The load-bearing coefficient in the source is

\[
c^8-18c^4d^4+d^8,
\]

not the historical StageA1 auxiliary replacement with `-8`. The same `-18` occurs in the immediately preceding `(P,Q)` formula in the cited paper.

An exact nondegenerate source check is supplied by

\[
(c,d,G,H)=(3,1,7,1).
\]

For the published formula, the four Hilbert-cube entries are

```text
(a0,a1,a2,a3)=
(243180321177600,
 1521303552000000,
 1362949057806336,
 403778845016064),
```

and the eight subset sums are respectively

```text
15594240^2, 25435392^2, 40076544^2, 44832000^2,
42005760^2, 46564608^2, 55923456^2, 59424000^2.
```

Changing only `-18` to `-8` destroys seven of these eight square identities. Thus the coefficient is arithmetically substantive, not a normalization choice.

## 3. Exact reduction to a genus-one quartic

On the nondegenerate population `dH != 0`. Set

\[
x=c/d,\qquad r=G/H,\qquad k=x^2,\qquad u=r-r^{-1}.
\]

Divide `F18=0` by `d^8H^4`, then by `r^2`. Using

\[
r^2+r^{-2}=u^2+2
\]

gives the exact quadratic

\[
4k(k-1)u^2-(k^4-18k^2+1)u-16k^2(k-1)=0. \tag{3.1}
\]

Since `k != 0,1` on the nondegenerate population, a rational solution `u` forces the discriminant in `u` to be a rational square:

\[
v^2=D_{18}(k),
\]

\[
D_{18}(k)=k^8-36k^6+256k^5-186k^4+256k^3-36k^2+1. \tag{3.2}
\]

Its polynomial discriminant is

\[
-2^{80}3^35^2\ne0,
\]

so this is a smooth genus-three hyperelliptic curve.

For `k != 0`, define

\[
z=k+k^{-1},\qquad Y=v/k^2.
\]

Using

\[
k^2+k^{-2}=z^2-2,
\qquad
k^4+k^{-4}=z^4-4z^2+2,
\]

equation (3.2) becomes

\[
E_{18}:\quad Y^2=z^4-40z^2+256z-112. \tag{3.3}
\]

The quartic discriminant is

\[
-2^{32}\,3\,5\ne0,
\]

so `E18` is a smooth genus-one curve. Every nondegenerate rational solution of the published anchor equation therefore maps to a rational point of `E18`.

The wall `k=1` maps to

\[
z=2,\qquad Y=\pm16,
\]

and is exactly `c^2=d^2`, which is excluded from the population.

## 4. Exact finite descent on `E18`

The quartic factors over `Q` as

\[
z^4-40z^2+256z-112
=(z^2-8z+28)(z^2+8z-4). \tag{4.1}
\]

Write a rational point with `z=a/b`, `gcd(a,b)=1`, `b>0`, and define

\[
F_1=a^2-8ab+28b^2,
\qquad
F_2=a^2+8ab-4b^2.
\]

Then `F1 F2` is an integer square. Moreover

\[
F_2-F_1=16b(a-2b),
\qquad
F_1(2b,b)=16b^2,
\]

and `gcd(F1,b)=gcd(F2,b)=1`, hence

\[
\gcd(F_1,F_2)\mid2^8. \tag{4.2}
\]

Thus every odd prime has even valuation in each factor separately. At `2`, primitiveness gives the exhaustive cases:

- if `a` is odd or `b` is even, both factors are odd;
- if `a=2m`, `b` is odd and `m` is even, both have `v_2=2`;
- if `a=2m`, `b` is odd and `m` is odd, both have `v_2=4`.

Hence the 2-adic valuations are also even. Finally

\[
z^2-8z+28=(z-4)^2+12>0,
\]

and the second factor is positive at a rational `E18` point because their product is `Y^2` and `z^2+8z-4` has no rational zero. Therefore each factor is itself a rational square:

\[
U^2=z^2-8z+28,
\qquad
V^2=z^2+8z-4. \tag{4.3}
\]

This is the exact first split; no additional `2`-squareclass branch is needed.

### 4.1 Parameterizing the first conic

The first conic has `(z,U)=(2,4)`. Intersect it with

\[
U=4+t(z-2).
\]

The second intersection gives

\[
z=\frac{2t^2-8t-6}{t^2-1},
\qquad
U=-4\frac{t^2+t+1}{t^2-1}. \tag{4.4}
\]

Substitution into the second equation of (4.3) yields

\[
z^2+8z-4
=16\frac{(t^2-5t-5)(t^2-t-1)}{(t^2-1)^2}. \tag{4.5}
\]

Thus

\[
(t^2-5t-5)(t^2-t-1)
\]

must be a rational square.

For reduced `t=a/b`, set

\[
A=a^2-5ab-5b^2,
\qquad
B=a^2-ab-b^2.
\]

One has

\[
B-A=4b(a+b),
\qquad
\gcd(A,b)=1,
\qquad
A(-b,b)=b^2,
\]

so `gcd(A,B)|4`. But `A` and `B` are both odd for every primitive pair `(a,b)`, hence

\[
\gcd(A,B)=1.
\]

Because `AB` is a square and neither factor has a rational zero, they have the same sign and their absolute values are individually squares. Therefore every rational point of `E18` lifts to one of exactly two covers:

\[
C_+:\quad R^2=t^2-5t-5,\qquad S^2=t^2-t-1, \tag{4.6}
\]

or

\[
C_-:\quad R^2=-(t^2-5t-5),\qquad S^2=-(t^2-t-1). \tag{4.7}
\]

This is the complete finite funnel: there are no omitted squareclasses.

A reconstruction condition from `z=k+k^{-1}` is

\[
z^2-4=-16\frac{(2t+1)(t^2-2t-2)}{(t^2-1)^2}, \tag{4.8}
\]

but it will not be needed: the two covers themselves close completely.

## 5. Complete rational-point closure of the two covers

### 5.1 The `C+` quartic

Use the rational point `(t,R)=(-1,1)` and the line

\[
R=1+m(t+1).
\]

The second intersection is

\[
t=-\frac{m^2+2m+6}{m^2-1},
\qquad
R=-\frac{m^2+7m+1}{m^2-1}.
\]

Writing `S=y/(m^2-1)` gives the smooth genus-one quartic

\[
Q_+:\quad y^2=m^4+6m^3+23m^2+22m+29. \tag{5.1}
\]

### 5.2 The `C-` quartic

Use `(t,R)=(1,3)` and

\[
R=3+m(t-1).
\]

Then

\[
t=\frac{m^2-6m+4}{m^2+1},
\qquad
R=-3\frac{m^2-m-1}{m^2+1},
\]

and with `S=y/(m^2+1)` one obtains

\[
Q_-:\quad y^2=m^4+6m^3-37m^2+42m-11. \tag{5.2}
\]

Both quartic polynomials have discriminant

\[
12960000=2^8 3^4 5^4\ne0.
\]

For a binary quartic

\[
f=am^4+bm^3+cm^2+dm+e,
\]

use the classical invariants

\[
I=12ae-3bd+c^2,
\]

\[
J=72ace+9bcd-27ad^2-27b^2e-2c^3.
\]

For both `Q+` and `Q-`,

\[
I=481,\qquad J=9758.
\]

Hence both have Jacobian

\[
E:\quad Y^2=X^3-27IX-27J
=X^3-12987X-263466
=(X+102)(X+21)(X-123). \tag{5.3}
\]

The LMFDB curve `15.a5` has minimal model

\[
y^2+xy+y=x^3+x^2-10x-10.
\]

The explicit rational change of variables

\[
X=36x+15,
\qquad
Y=108(2y+x+1) \tag{5.4}
\]

maps that model isomorphically over `Q` to (5.3). LMFDB records rank `0` and torsion

\[
\mathbf Z/2\mathbf Z\times\mathbf Z/4\mathbf Z,
\]

so `E(Q)` has exactly eight points. The same short model and its complete eight-point list also appear in Leprévost--Pohst--Schöpp, *Units in some parametric families of quartic fields*, Acta Arith. 127 (2007), 205--216, proof of Theorem 2.5. The group structure here is taken from LMFDB; only the identical model and cardinality-eight point list are used from that paper.

Each quartic `Q+` and `Q-` is a smooth genus-one curve with a rational point. Choosing such a point as origin identifies it over `Q` with its Jacobian. Therefore each has exactly eight rational points.

The eight points of `Q+` are

```text
m=-7/2, y=+/-45/4,
m= 1,   y=+/-9,
m=-1,   y=+/-5,
and the two quartic points at infinity.
```

Their images on `C+` give exactly

\[
t\in\{-1,\infty\}.
\]

More precisely, `m=-7/2` gives `t=-1,R=1`; the two quartic infinities give `t=-1,R=-1`; and `m=+/-1` give the four projective points with `t=\infty`.

The eight points of `Q-` are

```text
m=1/2, y=+/-5/4,
m=1,   y=+/-1,
m=3,   y=+/-5,
and the two quartic points at infinity.
```

Their images on `C-` give exactly

\[
t\in\{1,-1/2\}.
\]

Specifically, `m=1/2` and the quartic infinities give `t=1`, while `m=1` and `m=3` give `t=-1/2` with the two possible signs of `S`.

Thus the displayed representatives exhaust both two-cover rational point sets.

## 6. Terminal images and all boundary cases

The map (4.4) is

\[
z=\frac{2t^2-8t-6}{t^2-1}.
\]

The terminal values behave as follows:

- `C+`, `t=-1`: denominator zero, so the point maps to a projective infinity of `E18`;
- `C-`, `t=1`: denominator zero, so the point maps to the other projective infinity of `E18`;
- `C+`, `t=\infty`: `z=2` and `U=-4`;
- `C-`, `t=-1/2`: `z=2`.

For `z=2`, the reconstruction equation

\[
k+k^{-1}=2
\]

forces `(k-1)^2=0`, hence

\[
k=1\quad\Longrightarrow\quad c^2=d^2,
\]

which is an excluded nondegeneracy wall.

The affine reduction excluded `k=0` only because `c=0` is already a source wall, and it excluded `k=1` only because `c^2=d^2` is already a source wall. The charts `d=0` and `H=0`, and the values `G=0`, `c=0`, `G^2=H^2`, are likewise outside the stated population by definition. The two quartic points at infinity on each genus-one model have been included explicitly above. No pole, projective point, denominator-zero value, or parameterization base point remains unclassified in the claimed population.

Consequently every rational point of `E18` supplied by the exact factor descent lands either at projective infinity or at the excluded `k=1` wall. Therefore

\[
\boxed{E_{18}(\mathbf Q)\text{ has no nondegenerate point relevant to the published anchor.}}
\]

## 7. Final implication and firewalls

Every nondegenerate rational solution of `F18=0` maps by Section 3 to a rational point of `E18`. Sections 4--6 classify every such rational point and show that all terminal images are either projective infinities or the excluded wall `c^2=d^2`. Hence no nondegenerate rational solution of the published equation-(6) anchor equation exists.

The later reconstruction requirements from the reciprocal tower -- `k` a rational square, `u^2+4` a rational square, and the remaining source-factor nonvanishing/positivity checks -- never need to be reached, because the quotient receiver has already closed.

The exact StageA2 conclusion is therefore

```text
PUBLISHED_EQUATION6_MINUS18_ANCHOR_NONDEGENERATE_RATIONAL_POINTS=0
FAMILY_SPECIFIC_EXCLUSION_COMPLETE=true
```

The following statements are **not** proved:

1. equation (6) does not parametrize every anchored Hilbert cube;
2. no reverse map from an arbitrary perfect cuboid into equation (6) is established;
3. arbitrary perfect-cuboid nonexistence is not proved;
4. a perfect cuboid is not constructed;
5. the historical StageA1 `-8` quartic, its Jacobian, multiplier classes and 7-adic refinements are not constraints on this published `-18` family.

Thus StageA2 closes exactly one published two-projective-parameter family boundary and nothing larger.

## 8. External references

- A. Bremner, C. Elsholtz, M. Ulas, *There are infinitely many Hilbert cubes of dimension 3 in the set of squares*, arXiv:2604.05459v1, PDF p.13, equation (6). This supplies the published family and the `-18` coefficient.
- LMFDB elliptic curve `15.a5`. This supplies the rank-zero and `Z/2Z x Z/4Z` Mordell--Weil datum for the minimal model explicitly isomorphic to (5.3).
- F. Leprévost, M. Pohst, A. Schöpp, *Units in some parametric families of quartic fields*, Acta Arith. 127 (2007), 205--216, DOI `10.4064/aa127-3-1`, proof of Theorem 2.5. This supplies an independent occurrence of the identical short model and its complete eight rational points.

## 9. Repository provenance and reproducibility

The mathematical chain was originally developed and independently audited in:

```text
stages/stageA2/A2-3/result.md
stages/stageA2/A2-3/audit.md
stages/stageA2/A2-4/result.md
stages/stageA2/A2-4/audit.md
stages/stageA2/A2-5/result.md
stages/stageA2/A2-5/audit.md
stages/stageA2/A2-CLOSE/result.md
stages/stageA2/A2-CLOSE/audit.md
stages/stageA2/controller.json
```

The independent audit verdicts were:

```text
A2-3:    PASS
A2-4:    PASS_WITH_ELEMENTARY_STRENGTHENING_AND_LANDMARK_REPAIR
A2-5:    PASS_WITH_CONTROLLER_HISTORY_REPAIR
A2-CLOSE: PASS
```

The A2-4 final argument in this file uses the audited strengthening: the first exact squareclass is `1` only, the second exact squareclasses are `+1` and `-1` only, and `t=\infty` is explicitly classified. The earlier `delta=2` and `delta=+/-2` local branches were valid over-approximations but are not load-bearing here.

No StageA2-specific exact-head CI was configured at closeout; the mathematical audit chain, not an unrelated workflow, is the recorded verification authority.

```text
SELF_CONTAINED_FINAL=PASS
STAGE_A2_STATUS=CLOSED_PUBLISHED_MINUS18_FAMILY_EXCLUSION
```
