# Stage14-t22 — uniform fixed-direction simultaneous-completion bound

## Purpose

Stage14-t21 reduced a fixed split partition `(alpha,beta)` to primitive reduced directions

\[
(D,C)=\left(\frac d g,\frac s g\right),\qquad (D,C)=1,
\]

and left the scale-counting quantity

\[
M_{D,C}(G)
\]

for simultaneous two-face completions.  Its soft divisor treatment counted each scale separately and therefore left a factor comparable to `G`.

Stage14-t22 removes that scale factor.  After normalizing by `g`, all scales in one fixed direction lie on one fixed genus-five simultaneous-completion curve, and that curve has an explicit elliptic quotient with rational 2-torsion.  Marta Dujella's uniform bounded-height theorem then gives a subpolynomial bound for **all scales combined** in one direction.

No power saving for the number of active directions is claimed.

## 1. Normalize all scales at once

Fix a reduced direction `(D,C)` with `D>C>0` and `(D,C)=1`.  A primitive raw-pair edge in this direction has

\[
d=gD,\qquad s=gC.
\]

Let `x,y` be the other two cuboid sides and `H_1,H_2` the two already-integral face diagonals.  Put

\[
X=x/g,\quad Y=y/g,\quad P=H_1/g,\quad Q=H_2/g.
\]

Then every simultaneous completion lies on the fixed rational curve

\[
\boxed{
P^2=C^2+X^2,
\qquad
Q^2=C^2+Y^2,
\qquad
X^2+Y^2=D^2-C^2.
}
\]

The direction `(D,C)` is fixed; changing the physical scale `g` only changes the denominator of the rational point.

This projective curve is the Humbert-type simultaneous two-face curve already anticipated by the t-track.  For t22 we do not need a uniform rational-point theorem on the full genus-five curve, because it has a useful elliptic quotient.

## 2. Explicit elliptic quotient

Eliminate `Y^2` using

\[
Y^2=D^2-C^2-X^2.
\]

Since

\[
Q^2=C^2+Y^2=D^2-X^2,
\]

put

\[
R=YQ.
\]

Every simultaneous completion maps to

\[
\boxed{
R^2=(D^2-C^2-X^2)(D^2-X^2).
}
\]

This quartic has distinct branch points because `D>C>0`.  The two rational branch points `X=+-D` already show the genus-one quotient has rational 2-structure.

For an explicit cubic model, set

\[
U=\frac{2D}{D-X},
\qquad
V=\frac{2DR}{(D-X)^2}.
\]

Direct substitution gives

\[
\boxed{
V^2=(U-1)(-C^2U^2+4D^2U-4D^2).
}
\]

The root `U=1` is simple because the quadratic factor there equals `-C^2`.  Its other quadratic factor has discriminant

\[
16D^2(D^2-C^2)>0,
\]

so the cubic is smooth.

Writing

\[
x_E=-U,\qquad y_E=V/C
\]

gives the monic Weierstrass equation

\[
\boxed{
y_E^2=x_E^3+\left(1+\frac{4D^2}{C^2}\right)x_E^2
+\frac{8D^2}{C^2}x_E+\frac{4D^2}{C^2}.}
\]

It has the nonzero rational 2-torsion point

\[
\boxed{(-1,0).}
\]

The map from the full simultaneous-completion curve to this elliptic quotient has bounded degree (at most four): after `(X,R)` is fixed, the separate signs/square lifts for `P,Y,Q` give only boundedly many preimages.

## 3. The primitive scale is the canonical denominator

For a primitive edge,

\[
X=x/g,\qquad Y=y/g.
\]

Since `g|s` and

\[
\gcd(s,x,y)=1,
\]

we also have

\[
\gcd(g,x,y)=1.
\]

Therefore

\[
\operatorname{lcm}(\operatorname{den}X,\operatorname{den}Y)
=\frac{g}{\gcd(g,x,y)}=g.
\]

Hence

\[
\boxed{g=\operatorname{lcm}(\operatorname{den}X,\operatorname{den}Y).}
\]

So one normalized rational point cannot be reused at arbitrarily many primitive scales.  Its primitive physical lift has a unique scale.

This closes a real loophole in the t21 majorant: the scale variable is a height/denominator of a rational point on one fixed curve, not an independent multiplicative choice.

## 4. Polynomial physical-to-elliptic height transfer

For a physical edge with `d=gD<=B`, all sides and face diagonals are at most `d`.  For the quotient map above,

\[
U=\frac{2d}{d-x},
\]

so its rational height satisfies

\[
\boxed{H(U)\le 2d\le2B.}
\]

Likewise

\[
V=\frac{2D\,yH_2}{(d-x)^2},
\]

which gives the crude but uniform bound

\[
H(V)\le2d^3\le2B^3.
\]

The Weierstrass coefficient height is polynomial in `D,C`, hence polynomial in `B`.  Thus both the elliptic model and every physical quotient point lie in a `B^{O(1)}` height window.

## 5. Uniform all-scale bound from rational 2-torsion

Marta Dujella, *Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves*, arXiv:2312.03655, Theorem 1.1 / Corollary 1.3, proves that an elliptic curve over a fixed number field with a rational point of exact prime order has

\[
\#\{P:H(P)\le H\}
\le
\exp\!\left(C\frac{\log H}{\log\log H}\right)
\]

uniformly in the curve (after the stated equation-height threshold).  Here the field is `Q` and the quotient has the exact rational 2-torsion point `(-1,0)`.

Because the equation height is `B^{O(1)}` and the physical point height is `B^{O(1)}`, enlarging the counting threshold by one fixed power of `B` satisfies Dujella's model-height condition without changing the final exponent class.  The bounded-degree quotient then yields, uniformly in every reduced direction,

\[
\boxed{
M_{D,C}(G)
\le
\exp\!\left(O\!\left(\frac{\log(DG)}{\log\log(DG)}\right)\right)
=(DG)^{o(1)}.
}
\]

Under the Stage14 cutoff `d=gD<=B`, this is simply

\[
\boxed{M_{D,C}(B/D)=B^{o(1)}.}
\]

More strongly, the total number of raw edges over one fixed direction, including the bounded number of lifts per elliptic quotient point, is `B^{o(1)}`.  Thus the missing t21 power cannot come from repeatedly reusing one direction at many scales.

## 6. New active-direction second moment

For a split partition `(alpha,beta)`, define

\[
A_{\alpha,\beta}(B)
=
\#\{\text{reduced generalized-Pell directions in }(\alpha,\beta)
\text{ that have at least one physical raw edge with }d\le B\}.
\]

The all-scale bound gives

\[
\boxed{
N_{\alpha,\beta}(B)
\le B^{o(1)}A_{\alpha,\beta}(B).
}
\]

Define

\[
Q_{\rm active-dir}(B)
=\sum_{\alpha,\beta}A_{\alpha,\beta}(B)^2.
\]

Then

\[
\boxed{
Q_{\rm split}(B)
\le B^{o(1)}Q_{\rm active-dir}(B).
}
\]

Consequently any fixed power saving

\[
Q_{\rm active-dir}(B)=O(B^{1-\delta})
\]

implies `Q_split(B)=o(B)`, then `Q_edge(B)=o(B)`, and finally

\[
T(B)=o(\sqrt B).
\]

This is the correct post-t22 target.  Scale multiplicity is closed at the polynomial-exponent level; the remaining issue is the frequency and collision energy of **active reduced directions**.

## 7. Frozen finite audit

The standard-library audit regenerates every raw-pair edge through `B=2,000,000` and checks both orientations on every edge.

For every frozen edge it verifies:

- the normalized three-equation simultaneous-completion curve;
- the quartic elliptic quotient;
- the explicit cubic transformation;
- the simple rational 2-torsion root structurally;
- `g=lcm(den(X),den(Y))`;
- `H(U)<=2d` and `H(V)<=2d^3`.

At `B=2,000,000`:

```text
raw-pair edges                         356
canonical-scale identity checks        356
elliptic quotient identity checks      712
smooth cubic checks                     356
active reduced directions               356
max edges per reduced direction           1
Q_active-dir (finite)                   356
```

At all 11 frozen cutoffs the observed active directions and split partitions remain injective, so the finite active-direction second moment equals the raw edge count.  This remains diagnostic only.

## Locked boundary

```text
STAGE14_T22=COMPLETE_UNIFORM_FIXED_DIRECTION_ELLIPTIC_QUOTIENT_BOUND
SIMULTANEOUS_COMPLETION_NORMALIZED_CURVE_EXPLICIT=true
ELLIPTIC_QUOTIENT_EXPLICIT=true
ELLIPTIC_QUOTIENT_RATIONAL_2_TORSION=true
PRIMITIVE_SCALE_IS_CANONICAL_DENOMINATOR=true
PHYSICAL_TO_QUOTIENT_HEIGHT_POLYNOMIAL=true
DUJELLA_UNIFORM_BOUND_APPLIES=true
FIXED_DIRECTION_ALL_SCALE_MULTIPLICITY=B^o(1)
N_ALPHA_BETA_LE_B_O1_ACTIVE_DIRECTIONS=true
Q_SPLIT_LE_B_O1_Q_ACTIVE_DIRECTION=true
ACTIVE_DIRECTION_SECOND_MOMENT_POWER_SAVING_PROVED=false
Q_SPLIT_POWER_SAVING_PROVED=false
Q_EDGE_O_B_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t23 attack the active generalized-Pell direction second moment; classify torsion/positive-rank activation and seek a power-saving family count
```
