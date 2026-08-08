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
MAX_VERIFIED_B=2000000
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
PHYSICAL_RAW_PAIR_IMPLIES_POSITIVE_RANK_SPECIALIZATION=true
LEVEL4_MODULAR_K3_IDENTIFIED_OVER_QI=true
RANK_JUMP_GRAPH_IDENTITY_LOCKED=true
DUJELLA_SUBPOLYNOMIAL_DEGREE_BOUND=true
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true
TRIPLE_FIXED_BASE_GENUS=5
T_O_SQRT_B_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
NEXT=Stage14-4ah Kummer height/accumulating-multisection and relative triple-thin analysis
```

Canonical source: `stages/stage14/main.md`.

## Locked population

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

Raw-pair and triple ledgers satisfy

\[
\boxed{O_{\rm pair}^{raw}(B)=N_2(B)+3T(B).}
\]

At `B=2,000,000`, the exact census gives

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,\qquad T=0.
\]

No perfect-cuboid nonexistence assumption is made.

## Elliptic and Kummer reduction

For primitive oriented Pythagorean face data `F_i=(S_i,X_i,H_i)`, with

\[
g=(S_1,S_2),\qquad t_i=X_i/S_i,
\]

a raw pair has

\[
(e,x,y)=\operatorname{lcm}(S_1,S_2)(1,t_1,t_2)
\]

and

\[
(X_1X_2)^2+(gd)^2=(H_1H_2)^2.
\]

Fixing the first face gives

\[
E_t:Y^2=X(X-1)(X+t^2).
\]

For the actual Pythagorean base

\[
r=\frac{X_1}{H_1+S_1},\qquad t=\frac{2r}{1-r^2},
\]

the pulled-back surface is the six-`I4` K3 from Stage14-4af. Stage14-4ag identifies it explicitly over `Q(i)` with the classical level-4 elliptic modular surface by

\[
\boxed{\sigma=i\frac{1+r}{1-r}},
\qquad
\frac{\sigma+\sigma^{-1}}2=it.
\]

Over `C` this is the Kummer surface `Km(E_i x E_i)`.

In two face parameters `r,s`, the same space-square locus has the symmetric model

\[
\boxed{
Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2.
}
\]

## Active rank-jump graph

Let `G_B` have one vertex for each primitive **oriented** Pythagorean face state occurring in a raw pair with `d<=B`, and one edge for each raw pair incidence. Put

\[
V(B)=|\mathcal V_B|,\qquad E(B)=|\mathcal E_B|.
\]

Then

\[
\boxed{E(B)=N_2(B)+3T(B)}
\]

and

\[
\boxed{N_2(B)=\frac12V(B)\bar d(B)-3T(B)}.
\]

Stage14-4af implies every active vertex is a positive-rank specialization. Conversely every positive-rank genuine Pythagorean specialization eventually has a physical non-boundary partner, so `V(B)` is the positive-rank set ordered by its first physical hit height.

Every Stage14 fiber has rational 2-torsion. Dujella's uniform bounded-height theorem, combined with the polynomial height of the Stage14 birational coordinates under `d<=B`, gives

\[
\boxed{\max_F\deg_B(F)=B^{o(1)}.}
\]

Hence

\[
\frac12V(B)\le E(B)\le V(B)B^{o(1)},
\]

so raw-pair edges and active rank-jump vertices have the same polynomial growth exponent.

## Finite diagnostic

At the late cutoffs:

| B | raw edges E | active vertices V | avg degree | max degree | V/sqrt(B) |
|---:|---:|---:|---:|---:|---:|
| 200,000 | 116 | 155 | 1.4968 | 6 | 0.34659 |
| 500,000 | 188 | 254 | 1.4803 | 8 | 0.35921 |
| 1,000,000 | 255 | 347 | 1.4697 | 8 | 0.34700 |
| 2,000,000 | 356 | 490 | 1.4531 | 9 | 0.34648 |

The active-vertex effective exponent from `200k` to `2m` is

\[
0.4998643818582221.
\]

This is strong finite evidence for the location of the square-root signal, not an asymptotic theorem.

## Triple gate

For each fixed first face the triple/perfect-cuboid locus remains genus `5`, hence fiberwise finite. No uniform moving-base bound and no

\[
T(B)=o(\sqrt B)
\]

theorem is known, so a future raw-pair law cannot yet be transferred automatically to exactly-two.

## Artifacts

```text
stages/stage14/archive/stage14-4ag-kummer-rank-jump.md
stages/stage14/scripts/14-4/rank_jump_graph_audit.py
stages/stage14/data/14-4/rank_jump_graph_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## Next

Stage14-4ah will match the physical primitive/lcm height to a divisor on the Kummer surface, inspect accumulating rational curves/multisections, and treat the triple condition as a relative thin cover at that height.
