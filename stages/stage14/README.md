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
STAGE14_4AG=COMPLETE
STAGE14_4AH=COMPLETE
STAGE14_4AI=COMPLETE_MINIMAL_BISECTION_REDUCTION
STAGE14_4AJ=COMPLETE_SHIMADA_LATTICE_INTERFACE
STAGE14_4AK=COMPLETE_SPLIT_ROOT_COSET_VOID
MAX_VERIFIED_B=2000000
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
LEVEL4_MODULAR_K3_IDENTIFIED_OVER_QI=true
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-4al collective rank-jump / first-small-point mechanism
```

Canonical source: `stages/stage14/main.md`.

## Locked population and finite ceiling

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The exact ledgers satisfy

\[
\boxed{O_{\rm pair}^{raw}(B)=N_2(B)+3T(B).}
\]

At `B=2,000,000`, two independent exact generation routes give

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,\qquad T=0.
\]

The finite zero triple census is not a perfect-cuboid nonexistence theorem.

## Kummer/rank-jump reduction

For Pythagorean half-angle parameters `r,s`, the raw pair surface is

\[
\boxed{Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2.}
\]

Over `Q(i)` it is the level-4 elliptic modular K3; over `C` it is `Km(E_i x E_i)`.

The physical compactification is

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad
L=2H_r+2H_s-\sum E_j=-K_Y,
\]

with resolved double cover `pi:X->Y`. Stage14-4ah identifies

\[
\boxed{M=\pi^*L},\qquad \boxed{M^2=8},\qquad \boxed{H_M=d}.
\]

Let `V(B)` count active oriented first-face states and `E(B)` raw pair incidences. The uniform per-fiber bounded-height input gives maximum fiber degree `B^{o(1)}`, so `E(B)` and `V(B)` have the same polynomial growth exponent. Finite `V(B)/sqrt(B)` remains strikingly stable through `2m`, but no square-root theorem is claimed.

## Stage14-4ai — reduce every fixed sqrt(B) curve to one target

A fixed physical rational curve capable of exponent `1/2` must satisfy

\[
M\cdot C=4,
\qquad
\deg(C\to\mathbf P^1_r)=2,
\qquad
\deg(C\to\mathbf P^1_s)\le2.
\]

Stage14-4ai eliminates:

- every connected degree-two image mechanism;
- every arithmetic-genus-zero splitting/contact mechanism.

The only remaining case was a split singular anticanonical member

\[
D\in|L|,
\qquad p_a(D)=1,
\qquad \widetilde D\simeq\mathbf P^1.
\]

## Stage14-4aj/4ak — exact Shimada lattice closure

Stage14-4aj identifies the raw Kummer deck involution on

\[
E_t:y^2=x(x-1)(x+t^2)
\]

as

\[
\delta(P)=(0,0)-P,
\]

so in Shimada's level-4 data it is a nonzero 2-torsion translation composed with elliptic inversion.

For a hypothetical split component,

\[
M=C+\delta(C),\qquad C^2=-2,\qquad M\cdot C=4.
\]

Putting

\[
\boxed{x=2C-M}
\]

reduces the complete remaining problem to

\[
\boxed{\delta(x)=-x,\qquad x^2=-16,\qquad x\equiv M\pmod2.}
\]

Stage14-4ak consumes Shimada's published `GramS0`, `SixFs`, `fsigma`, automorphism, torsion-translation and inversion matrices. The physical labeling search gives two candidates after the exact `r<->s` coordinate-swap fingerprint, and 64 elements of `AutX0f` identify those two labelings. Hence there is one physical labeling up to the relevant symmetry.

For a representative, the saturated anti-invariant lattice has

```text
rank = 6
det positive form = 256
```

and exact vector census

```text
norm 0   :    1
norm 4   :   60
norm 8   :  252
norm 12  :  544
norm 16  : 1020
```

The norm-16 shell is nonempty, but the required Stage14 parity coset is empty:

```text
norm-16 vectors                       = 1020
PARI qfminim +/- representatives      = 510
parity-compatible norm-16 vectors     = 0
parity-compatible split-root pairs    = 0
```

PARI/GP Fincke--Pohst enumeration and an independent exact rational-LDL recursion agree.

Therefore

\[
\boxed{\text{no split singular-anticanonical }M\text{-degree-4 bisection exists}.}
\]

Combined with 14-4ai:

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

This closes the complete fixed rational-curve explanation of the observed finite `sqrt(B)` signal. It does **not** reject a collective `sqrt(B)` law.

## What remains

The main-track bottleneck returns to the moving arithmetic problem already isolated by the `14-s` branch:

```text
positive-rank specialization
+ first non-torsion point small enough in the physical height
+ moving Pythagorean base distribution
```

Thus Stage14-4al must study the collective rank-jump / first-small-point mechanism rather than search for more fixed accumulating curves.

The independent triple track still must control

\[
T(B)=o(\sqrt B)
\]

before any raw-pair square-root law could transfer to exactly-two.

## Primary artifacts

```text
stages/stage14/archive/stage14-4ai-degree4-bisections.md
stages/stage14/archive/stage14-4aj-shimada-lattice-interface.md
stages/stage14/archive/stage14-4ak-shimada-split-root-void.md
stages/stage14/data/14-4/shimada_stage14_4ak_result.json
stages/stage14/scripts/14-4/shimada_stage14_identify.py
stages/stage14/scripts/14-4/shimada_stage14_refine.py
stages/stage14/scripts/14-4/shimada_stage14_equiv.py
stages/stage14/scripts/14-4/shimada_stage14_roots.py
stages/stage14/scripts/14-4/shimada_stage14_verify.py
.github/workflows/stage14-4ak-shimada-probe.yml
```
