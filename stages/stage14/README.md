# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_3=COMPLETE
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
STAGE14_4AE=COMPLETE
STAGE14_4AF=COMPLETE
MAX_VERIFIED_B=2000000
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
BIJECTIVE_TWO_FACE_PARAMETER_SPACE_LOCKED=true
ELLIPTIC_FIBRATION_NON_ISOTRIVIAL=true
PYTHAGOREAN_BASE_CHANGE_K3=true
PYTHAGOREAN_BASE_GENERIC_MW_RANK=0
TORSION_EXACT_Z2xZ4_ON_GENUINE_BASES=true
PHYSICAL_RAW_PAIR_IMPLIES_POSITIVE_RANK_SPECIALIZATION=true
TRIPLE_FIXED_BASE_GENUS=5
UNIFORM_TRIPLE_POINT_BOUND_PROVED=false
SQRT_B_STRUCTURAL_HEIGHT_SOURCE_IDENTIFIED=true
TRUE_GROWTH_ORDER_IDENTIFIED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
NEXT=Stage14-4ag quantitative rank-jump/small-point counting with uniform triple control
```

Canonical source: `stages/stage14/main.md`.

## Locked population

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The exactly-two directions are

```text
a = ab+ac only = smallest shared edge
b = ab+bc only = middle shared edge
c = ac+bc only = largest shared edge
```

with

\[
N_a^{(2)}=O_{ab,ac}-T,\qquad
N_b^{(2)}=O_{ab,bc}-T,\qquad
N_c^{(2)}=O_{ac,bc}-T.
\]

No perfect-cuboid nonexistence assumption is made.

Two independent exact generation routes agree through `B=2,000,000`; there

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,\qquad T=0.
\]

This is only a finite statement.

## Frozen Stage13 input

Stage13 freezes the downstream `R03 + Stage13-12ag` contract. In particular Stage14 may use

\[
O_{qr}(B)=o(B(\log B)^3),\qquad
T(B)=o(B(\log B)^3),
\]

hence

\[
\boxed{N_2(B)=o(B(\log B)^3).}
\]

The R03 fixed-prime sieve gives zero density, not a `B`-dependent power saving.

## Exact two-face / elliptic coordinates

For primitive oriented Pythagorean face data

\[
F_i=(S_i,X_i,H_i),\qquad S_i^2+X_i^2=H_i^2,
\]

put

\[
g=(S_1,S_2),\qquad L=\operatorname{lcm}(S_1,S_2),\qquad t_i=X_i/S_i.
\]

A primitive raw-pair incidence is represented exactly once and satisfies

\[
(e,x,y)=L(1,t_1,t_2),
\qquad d=L\sqrt{1+t_1^2+t_2^2},
\]

and the product closure

\[
\boxed{(X_1X_2)^2+(gd)^2=(H_1H_2)^2.}
\]

After fixing the first face, the space-square condition is birational to

\[
\boxed{E_{t_1}:Y^2=X(X-1)(X+t_1^2).}
\]

## Stage14-4ae — physical height

For reduced `q=u/v`, `0<u<v`, the second primitive face has

\[
H_2=\frac{u^2+v^2}{\delta},\qquad \delta\in\{1,2\},
\]

so

\[
\frac{v^2}{2}<H_2<2v^2.
\]

The original cutoff satisfies uniformly

\[
\boxed{
\frac{S_1H_2}{\sqrt2\,g}<d<\frac{\sqrt3\,S_1H_2}{g},
}
\]

hence

\[
\boxed{v\asymp\sqrt{Bg/S_1}.}
\]

The elliptic inverse is

\[
q=\frac{X}{sY},\qquad s=S_1/H_1.
\]

The full `t`-line elliptic surface has geometric generic rank `0`.

## Stage14-4af — the actual Pythagorean base

A first-face Pythagorean slope has the degree-two parameterization

\[
\boxed{
t=\frac{2u}{1-u^2},
\qquad
\frac{H_1}{S_1}=\frac{1+u^2}{1-u^2}.
}
\]

After this base change the elliptic surface has six geometric `I4` fibers,

```text
u=0, infinity, +1, -1, +i, -i,
```

Euler number `24`, and is a K3 surface. Its trivial lattice already has rank

\[
2+6(4-1)=20.
\]

Since a K3 has geometric Picard rank at most `20`, Shioda--Tate gives

\[
\boxed{\operatorname{rank}E(\overline{\mathbf Q}(u))=0.}
\]

Thus the generic-rank-zero conclusion survives the **actual** Pythagorean restriction.

On every genuine Pythagorean fiber,

\[
\boxed{E_t(\mathbf Q)_{tors}\cong\mathbf Z/2\times\mathbf Z/4.}
\]

The rational order-4 points map under the Stage14 inverse to

\[
q=\pm1,
\]

the degenerate second-face boundary. Rational 8-torsion would force three rational squares `h-1,h,h+1` in arithmetic progression of common difference `1`, equivalently a rational right triangle of area `1`, which is impossible.

Therefore

\[
\boxed{
\text{every physical Stage14 raw-pair point is non-torsion and lies on a positive-rank specialization.}
}
\]

The `extra torsion` alternative from Stage14-4ae is no longer a physical source.

## Triple / perfect-cuboid gate

For fixed first-face slope `t`, the space condition is

\[
W^2=q^4+2Aq^2+1,
\qquad A=\frac{1-t^2}{1+t^2},
\]

while the third-face condition is

\[
R^2=q^4+2Cq^2+1,
\qquad C=\frac{2}{t^2}-1.
\]

Their branch sets are disjoint because

\[
A-C=-\frac{2}{t^2(1+t^2)}\ne0.
\]

The fiber product is therefore a connected degree-4 cover of `P^1_q` with eight simple branch values. Riemann--Hurwitz gives

\[
\boxed{g=5.}
\]

Thus for each fixed first face the triple locus is a genus-5 curve and has finitely many rational points. This is only fiberwise finiteness: no uniform moving-base bound and no `T=o(sqrt(B))` theorem is claimed.

The exact ledger identity remains

\[
\boxed{O_{\rm pair}^{raw}(B)=N_2(B)+3T(B).}
\]

## Validation

At `B=10000`, the Stage14-4af deterministic audit records

```text
oriented primitive first-face data  3186
raw pair incidences                   25
distinct first-face fibers            23
exactly-two direction              (9,11,5)
T                                      0
q denominator range                 5..57
```

Every physical hit has `0<q<1` and is not killed by multiplication by `8`.

Artifacts:

```text
stages/stage14/archive/stage14-4af-specialization-triple.md
stages/stage14/scripts/14-4/specialization_triple_audit.py
stages/stage14/data/14-4/specialization_triple_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## What remains unknown

The true growth exponent is still unknown. The remaining raw-pair problem is quantitative:

> count Pythagorean base specializations that acquire a sufficiently small non-torsion point.

The exactly-two transfer additionally needs uniform control of the moving genus-5 triple fibers.

```text
NEXT=Stage14-4ag quantitative rank-jump/small-point counting with uniform triple control
```
