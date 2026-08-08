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
MAX_VERIFIED_B=2000000
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
PHYSICAL_RAW_PAIR_IMPLIES_POSITIVE_RANK_SPECIALIZATION=true
LEVEL4_MODULAR_K3_IDENTIFIED_OVER_QI=true
RANK_JUMP_GRAPH_IDENTITY_LOCKED=true
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true
PHYSICAL_KUMMER_POLARIZATION_LOCKED=true
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8
PHYSICAL_POLARIZATION_BIG_NEF_NOT_AMPLE=true
PHYSICAL_RATIONAL_CURVE_M_DEGREE_LOWER_BOUND=4
SQRTB_MINIMAL_RATIONAL_CURVE_TARGET=M-degree-4 rational bisection
FINITE_CORE_SQRTB_SIGNAL_SURVIVES=true
TRIPLE_RELATIVE_COVER_BRANCH_CLASS=2M
T_O_SQRT_B_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
NEXT=Stage14-4ai classify Q-rational M-degree-4 bisections and count their first-hit height
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

This is finite evidence only; no perfect-cuboid nonexistence assumption is made.

## Frozen Stage13 input

Stage13 freezes `R03 + Stage13-12ag`. Stage14 may use

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad T(B)=o(B(\log B)^3),
\]

hence

\[
N_2(B)=o(B(\log B)^3).
\]

The R03 fixed-prime sieve gives zero density but no `B`-dependent power saving.

## Exact two-face and Kummer coordinates

For primitive oriented Pythagorean face data

\[
F_i=(S_i,X_i,H_i),
\qquad g=(S_1,S_2),
\qquad t_i=X_i/S_i,
\]

primitive gluing is bijective and

\[
(e,x,y)=\operatorname{lcm}(S_1,S_2)(1,t_1,t_2).
\]

The integer-space-diagonal condition has the product closure

\[
(X_1X_2)^2+(gd)^2=(H_1H_2)^2
\]

and, after fixing the first face, the elliptic model

\[
E_t:Y^2=X(X-1)(X+t^2).
\]

With the actual Pythagorean Euclid base

\[
r=\frac{X_1}{H_1+S_1},
\qquad t=\frac{2r}{1-r^2},
\]

Stage14-4ag identifies the K3 over `Q(i)` with the level-4 elliptic modular surface by

\[
\sigma=i\frac{1+r}{1-r}.
\]

Over `C` it is `Km(E_i x E_i)`. In two face parameters,

\[
\boxed{Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2.}
\]

## Rank-jump graph

Let `V(B)` count primitive oriented first-face states that have acquired a physical raw partner by height `B`, and `E(B)` count raw pair incidences. Then

\[
E(B)=N_2(B)+3T(B)=\frac12V(B)\bar d(B).
\]

Every physical point is non-torsion; active vertices are positive-rank specializations ordered by first physical hit height. Dujella's uniform bounded-height theorem gives

\[
\max_F\deg_B(F)=B^{o(1)},
\]

so `E(B)` and `V(B)` have the same polynomial growth exponent.

At `200k,500k,1m,2m`,

```text
V(B)        155, 254, 347, 490
V/sqrt(B)   0.34659, 0.35921, 0.34700, 0.34648
```

and the decade effective exponent is `0.4998643818582221`. This remains a finite diagnostic.

## Stage14-4ah — exact physical Kummer height

The independent e3 toric model is

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad
L=2H_1+2H_2-\sum E_j=-K_Y.
\]

The Stage14 space-square branch numerator has bidegree `(4,4)` and multiplicity two at all four toric corners, so its strict transform has class

\[
2L.
\]

For the resolved double cover

\[
\pi:X\to Y,
\]

the physical Kummer line bundle is exactly

\[
\boxed{M=\pi^*L=\Phi^*\mathcal O_{\mathbf P^2}(1)},
\qquad
\boxed{M^2=8}.
\]

On a primitive Stage14 point,

\[
\boxed{H_M(P)=\sqrt{e^2+x^2+y^2}=d.}
\]

Thus `d<=B` is the actual `M`-height cutoff, not merely a comparable height.

`M` is big and nef but not ample: it contracts the lifts of the toric null boundary. Those curves are nonphysical.

## Minimum rational-curve mechanism

Let `C` be a physical rational curve and let

\[
n=\deg(C\to\mathbf P^1_r).
\]

Since `t(r)=2r/(1-r^2)` has degree two and `t=x/e` is a ratio of two `M`-sections,

\[
\boxed{M\cdot C\ge2n.}
\]

A degree-one multisection would be a section. The generic Mordell--Weil rank is zero and all torsion sections are nonphysical, so a physical rational curve has `n>=2`. Therefore

\[
\boxed{M\cdot C\ge4.}
\]

For a rational curve with `m=M.C`, its fixed-curve bounded-height exponent is `2/m`. Hence no fixed physical rational curve can contribute a power larger than `B^(1/2)`. The extremal square-root target is exactly

\[
\boxed{\text{a Q-rational M-degree-4 bisection}.}
\]

Existence, classification and dominance of such bisections are **not** yet proved.

## Finite core diagnostic

The active-vertex square-root signal survives after removing fixed real cusp neighborhoods:

```text
B          all V    0.1<=r<=0.9    0.2<=r<=0.8    0.25<=r<=0.75
200k         155          134             105                92
500k         254          227             174               147
1m           347          307             238               197
2m           490          426             338               283
```

The `200k -> 2m` effective exponents are respectively

```text
0.49986438, 0.50230480, 0.50772740, 0.48799861.
```

So the finite signal is not obviously a pure non-ample boundary artifact. No asymptotic conclusion is drawn.

## Triple gate on the Kummer surface

The third-face-square numerator

\[
G=r^2(1-s^2)^2+s^2(1-r^2)^2
\]

also has strict class `2L` on `Y`. Therefore the relative degree-two triple cover

\[
\rho:W\to X
\]

has branch class

\[
\boxed{2M}.
\]

Its rational image is a type-II thin subset of the Kummer surface. Stage14 does **not** currently have a thin-set zero-density theorem for the raw K3 population under the big-and-nef height `M`; therefore this does not prove

\[
T(B)=o(\sqrt B).
\]

## Literature boundary

McKinnon's product-Kummer bounded-height counting is relevant to the accumulating-curve mechanism but is stated for ample heights. Because Stage14 `M` is only big and nef, no McKinnon asymptotic is imported directly. Explicit rational-curve constructions on product Kummer surfaces are treated only as adjacent geometry until their `M`-degree is calculated.

## Artifacts

```text
stages/stage14/archive/stage14-4ah-kummer-height.md
stages/stage14/scripts/14-4/kummer_height_audit.py
stages/stage14/data/14-4/kummer_height_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## Next

Stage14-4ai will classify `Q`-rational `M`-degree-four bisections, determine which meet the primitive physical open set, count their first-hit heights, and restrict the triple cover to them.
