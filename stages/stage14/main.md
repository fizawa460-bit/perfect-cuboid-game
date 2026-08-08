# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AG_COMPLETE_KUMMER_RANK_JUMP_REDUCTION_14_4AH_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 counts primitive canonical cuboids

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B,
\]

with exactly two integral face diagonals. No perfect-cuboid nonexistence assumption is made.

## §1. Ledgers

Let `T(B)` be the all-three-face population and `O_pair_raw(B)` the sum of the three raw two-face pair ledgers. Then

\[
\boxed{O_{\rm pair}^{raw}(B)=N_2(B)+3T(B).}
\]

At the frozen finite ceiling `B=2,000,000`,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,\qquad T=0.
\]

Stage13 `R03 + Stage13-12ag` is frozen upstream and gives only

\[
N_2(B)=o(B(\log B)^3),
\]

not an explicit power saving.

## §2. Exact two-face coordinates

For primitive oriented Pythagorean face data

\[
F_i=(S_i,X_i,H_i),\qquad S_i^2+X_i^2=H_i^2,
\]

put

\[
g=(S_1,S_2),\qquad L=\operatorname{lcm}(S_1,S_2),\qquad t_i=X_i/S_i.
\]

Primitive gluing has multiplicity one and

\[
(e,x,y)=L(1,t_1,t_2),
\qquad d=L\sqrt{1+t_1^2+t_2^2}.
\]

The integer-space-diagonal condition is equivalent to

\[
\boxed{(X_1X_2)^2+(gd)^2=(H_1H_2)^2.}
\]

Fixing the first face gives the elliptic curve

\[
\boxed{E_t:Y^2=X(X-1)(X+t^2).}
\]

For a second-face Euclid parameter `q=u/v`, Stage14-4ae proves

\[
\boxed{v\asymp\sqrt{Bg/S_1}}
\]

under `d<=B`, up to absolute constants.

## §3. Actual Pythagorean base and nonphysical torsion

For

\[
r=\frac{X_1}{H_1+S_1},
\qquad t=\frac{2r}{1-r^2},
\]

the pulled-back elliptic surface has six `I4` fibers and geometric generic Mordell--Weil rank zero.

On every genuine rational Pythagorean fiber,

\[
E_t(\mathbf Q)_{tors}\cong\mathbf Z/2\times\mathbf Z/4,
\]

and all rational order-4 points map to the degenerate `q=+/-1` boundary. Hence every physical raw-pair point is non-torsion and

\[
\boxed{\text{physical raw pair}\Longrightarrow\text{positive-rank specialization}.}
\]

For a fixed first face, imposing the third integral face produces a genus-5 curve. This gives fiberwise finiteness only.

## §4. Stage14-4ag — exact level-4 modular/Kummer identification

Shimada's level-4 elliptic modular surface is

\[
Y^2=X(X-1)\left(X-\left(\frac{\sigma+\sigma^{-1}}2\right)^2\right).
\]

Set

\[
\boxed{\sigma=i\frac{1+r}{1-r}}.
\]

Then

\[
\frac{\sigma+\sigma^{-1}}2=it,
\]

so the equation is exactly `E_t`. Thus the Stage14 Pythagorean-base K3 is the classical level-4 elliptic modular surface after explicit base change over `Q(i)`. Over `C` it is the Kummer surface `Km(E_i x E_i)`.

In the two Euclidean face parameters `r,s`, the space condition is the symmetric Kummer double cover

\[
\boxed{
Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2.
}
\]

With `M=r^2s^2+r^2+s^2+1`,

\[
F=(M-4rs)(M+4rs),
\]

and over `Q(i)` this splits into four `(1,1)` factors.

## §5. Active rank-jump graph

Define `G_B` as follows.

- A vertex is a primitive **oriented** Pythagorean face state that occurs in at least one raw pair incidence with `d<=B`.
- An edge is one raw pair incidence.

Write

\[
V(B)=|\mathcal V_B|,\qquad E(B)=|\mathcal E_B|,
\]

and let `bar d(B)` be the average graph degree. Then

\[
\boxed{E(B)=O_{\rm pair}^{raw}(B)=N_2(B)+3T(B)}
\]

and

\[
\boxed{E(B)=\frac12V(B)\bar d(B)}.
\]

Therefore

\[
\boxed{N_2(B)=\frac12V(B)\bar d(B)-3T(B).}
\]

For a face state `F`, let `mu(F)` be the least physical space diagonal of any raw partner. Then

\[
V(B)=\#\{F:\mu(F)\le B\}.
\]

The Stage14 elliptic correspondence and nonphysical-torsion theorem give

\[
\boxed{\mu(F)<\infty\iff\operatorname{rank}E_F(\mathbf Q)>0}
\]

for genuine Pythagorean base states. Thus `V(B)` is the positive-rank specialization set ordered by **first small physical point height**.

## §6. Per-fiber multiplicity cannot create a power of B

Dujella's uniform bounded-height theorem applies to every Stage14 fiber because each has a rational point of exact order `2`.

For any physical partner with `d<=B`, the rational base `t`, the second-face coordinate `q`, and the elliptic point obtained by the fixed birational map all have exponential height `B^{O(1)}`. Therefore, uniformly in the active face state,

\[
\boxed{
\deg_B(F)
\le
\exp\left(C\frac{\log B}{\log\log B}\right)
=B^{o(1)}.
}
\]

Hence, for `B` beyond the first edge,

\[
\boxed{
\frac12V(B)\le E(B)\le V(B)B^{o(1)}.
}
\]

In particular,

\[
\boxed{
\limsup\frac{\log E(B)}{\log B}
=
\limsup\frac{\log V(B)}{\log B},
}
\]

and the same equality holds for `liminf`.

So the **raw-pair polynomial exponent is exactly the active rank-jump first-hit exponent**. Fiber multiplicity can change logarithmic/subpolynomial factors but cannot supply a new positive power of `B`.

## §7. Finite graph census

The exact augmented census gives:

| B | E raw edges | V active vertices | avg degree | max degree | V/sqrt(B) |
|---:|---:|---:|---:|---:|---:|
| 100,000 | 89 | 117 | 1.5214 | 6 | 0.36999 |
| 200,000 | 116 | 155 | 1.4968 | 6 | 0.34659 |
| 500,000 | 188 | 254 | 1.4803 | 8 | 0.35921 |
| 1,000,000 | 255 | 347 | 1.4697 | 8 | 0.34700 |
| 2,000,000 | 356 | 490 | 1.4531 | 9 | 0.34648 |

Across `200k -> 2m`,

\[
\boxed{
\frac{\log(490/155)}{\log 10}=0.4998643818582221.
}
\]

At `200k,500k,1m,2m`, the coefficient of variation of `V(B)/sqrt(B)` is about `1.55%`.

This is a finite diagnostic only. It does not prove `V(B)=B^{1/2+o(1)}` or `V(B)~c sqrt(B)`.

## §8. Triple subtraction remains open at the target scale

For every fixed first face, the triple locus is genus 5, but no uniform moving-base point bound is proved. Thus Stage14 still does not know

\[
T(B)=o(\sqrt B).
\]

Even after the raw-pair exponent is identified, exactly-two requires control of `3T(B)` at the same scale.

## §9. Literature boundary and next problem

The K3 geometry is a known level-4 modular/Kummer surface, not a new Stage14 construction. McKinnon's product-Kummer counting results show that bounded-height rational points can be dominated by finite accumulating curve strata. Stage14 has not yet matched the primitive/lcm physical height to the relevant Kummer divisor, so those counting asymptotics are not imported yet.

Stage14-4ah will therefore attack the remaining exponent at the correct geometric level:

1. identify the physical first-hit/lcm height on `Km(E_i x E_i)`;
2. classify accumulating rational curves/multisections capable of producing small first hits;
3. determine whether they force `V(B)=B^{1/2+o(1)}` or another law;
4. treat the third-face condition as a relative degree-two cover and seek a triple bound relative to the Kummer count.

## §10. Locked decision

```text
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
STAGE14_4AE=COMPLETE
STAGE14_4AF=COMPLETE
STAGE14_4AG=COMPLETE

LEVEL4_MODULAR_K3_IDENTIFIED_OVER_QI=true
KUMMER_EI_SELF_PRODUCT_GEOMETRY_IMPORTED=true
GLOBAL_KUMMER_DOUBLE_COVER_LOCKED=true

RANK_JUMP_GRAPH_IDENTITY_LOCKED=true
ACTIVE_VERTEX_IS_SMALL_POINT_POSITIVE_RANK_COUNT=true
DUJELLA_SUBPOLYNOMIAL_DEGREE_BOUND=true
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true

FINITE_ACTIVE_VERTEX_SQRTB_SIGNAL=true
FINITE_VERTEX_EXPONENT_200K_TO_2M=0.4998643818582221
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false

TRIPLE_FIXED_BASE_GENUS=5
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false

NEXT=Stage14-4ah Kummer height/accumulating-multisection and relative triple-thin analysis
```
