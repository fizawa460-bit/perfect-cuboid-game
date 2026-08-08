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
MAX_VERIFIED_B=2000000
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
R03_PAIR_OVERLAP_LITTLE_O_IMPORTED=true
BIJECTIVE_TWO_FACE_PARAMETER_SPACE_LOCKED=true
ELLIPTIC_FIBRATION_NON_ISOTRIVIAL=true
GEOMETRIC_GENERIC_MW_RANK=0
SQRT_B_STRUCTURAL_HEIGHT_SOURCE_IDENTIFIED=true
RAW_PAIR_TO_EXACTLY_TWO_REQUIRES_TRIPLE_CONTROL=true
TRUE_GROWTH_ORDER_IDENTIFIED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
NEXT=Stage14-4af small-point specialization and triple-subtraction analysis
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
N_a^{(2)}=O_{ab,ac}-T,\quad
N_b^{(2)}=O_{ab,bc}-T,\quad
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

Stage13 freezes the downstream `R03 + Stage13-12ag` contract. Stage14 may use

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

\[
O_{qr}(B)=o(B(\log B)^3),\qquad T(B)=o(B(\log B)^3),
\]

hence

\[
\boxed{N_2(B)=o(B(\log B)^3).}
\]

The R03 fixed-prime sieve gives zero density, not a `B`-dependent power saving; no growing-modulus theorem is imported.

## Exact two-face coordinates

For primitive oriented Pythagorean face data

\[
F_i=(S_i,X_i,H_i),\qquad S_i^2+X_i^2=H_i^2,
\]

put

\[
g=(S_1,S_2),\qquad L=\operatorname{lcm}(S_1,S_2),
\qquad t_i=X_i/S_i.
\]

The primitive raw-pair incidence is represented exactly once and satisfies

\[
(e,x,y)=L(1,t_1,t_2),
\qquad d=L\sqrt{1+t_1^2+t_2^2}.
\]

The space-square condition has the product closure

\[
\boxed{(X_1X_2)^2+(gd)^2=(H_1H_2)^2.}
\]

After fixing the first face, it becomes the non-isotrivial elliptic fiber

\[
\boxed{E_{t_1}:Y^2=X(X-1)(X+t_1^2).}
\]

## Stage14-4ae — fiber height and generic rank

Let the second primitive face be parameterized by reduced

\[
q=u/v,\qquad 0<u<v.
\]

Then for `delta in {1,2}`,

\[
S_2=\frac{v^2-u^2}{\delta},\qquad
X_2=\frac{2uv}{\delta},\qquad
H_2=\frac{u^2+v^2}{\delta},
\]

so

\[
\boxed{v^2/2<H_2<2v^2.}
\]

More importantly, the original Euclidean cutoff has the uniform comparison

\[
\boxed{
\frac{S_1H_2}{\sqrt2\,g}<d<\frac{\sqrt3\,S_1H_2}{g}.
}
\]

Therefore the induced one-fiber cutoff is

\[
\boxed{v\asymp\sqrt{Bg/S_1}.}
\]

This explains why a square root appears naturally in the fiber height. It does not prove a total `sqrt(B)` population law.

On the elliptic fiber, with `s=S1/H1`, the Stage14-4ad birational map has the exact inverse

\[
\boxed{q(P)=\frac{X(P)}{sY(P)}.}
\]

For a fixed fiber this is a degree-2 rational function, so standard elliptic height theory gives

\[
h(q(P))=2\widehat h(P)+O_{t_1}(1).
\]

Thus a fixed rank-`r` fiber contributes only polylogarithmically in `B` under the physical cutoff. A power of `B` must come from varying specializations, not from one fixed elliptic curve.

The elliptic surface

\[
\mathscr E:y^2=x(x-1)(x+t^2)
\]

has

\[
\Delta=16t^4(1+t^2)^2,
\qquad c_4=16(1+t^2+t^4),
\]

with geometric singular fibers

```text
I4 at t=0
I2 at t=+i
I2 at t=-i
I4 at t=infinity
```

Their Euler numbers sum to `12`, so the surface is rational. The reducible-fiber root rank is `8`; with geometric Picard rank `10`, Shioda--Tate gives

\[
\boxed{\operatorname{rank}\mathscr E(\overline{\mathbf Q}(t))=0.}
\]

Hence Stage14 points live on specializations with rank jump and/or extra torsion. The true global target is the distribution of **small points on special fibers**, together with the gcd/lcm coupling and the R03 local restrictions.

## Raw-pair versus exactly-two gate

The elliptic family counts raw pair incidences. Exactly

\[
\boxed{O_{\rm pair}^{raw}(B)=N_2(B)+3T(B).}
\]

Although `T=0` through `B=2,000,000`, the frozen theorem only gives `T=o(B(log B)^3)`. Therefore even a future `sqrt(B)` theorem for raw pairs would still require a new triple-subtraction result before it becomes a theorem for `N_2`.

## Validation

The Stage14-4ae deterministic audit checks all 25 raw-pair incidences at `B=10000`, reproduces exactly-two `(9,11,5)` with `T=0`, and verifies every second-face reconstruction, square-root height bound, physical height sandwich and elliptic inverse coordinate.

Artifacts:

```text
stages/stage14/archive/stage14-4ae-height-rank.md
stages/stage14/scripts/14-4/height_rank_audit.py
stages/stage14/data/14-4/height_rank_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## What remains unknown

Stage14 still has not identified the true growth exponent, leading constant, limiting directional vector, eventual leader, or whether `T(B)` ever becomes positive.

```text
NEXT=Stage14-4af small-point specialization and triple-subtraction analysis
```
