# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AH_COMPLETE_PHYSICAL_KUMMER_HEIGHT_14_4AI_NEXT`
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

## §1. Exact ledgers and frozen finite facts

Let `T(B)` be the all-three-face population and `O_pair_raw(B)` the sum of the three raw pair ledgers. Then

\[
\boxed{O_{\rm pair}^{raw}(B)=N_2(B)+3T(B).}
\]

At `B=2,000,000`, two independent exact enumerators give

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,\qquad T=0.
\]

This is finite evidence only.

Stage13 `R03 + Stage13-12ag` is frozen upstream and gives

\[
N_2(B)=o(B(\log B)^3),
\]

without a `B`-dependent power saving.

## §2. Exact two-face coordinates

For primitive oriented Pythagorean face data

\[
F_i=(S_i,X_i,H_i),
\qquad S_i^2+X_i^2=H_i^2,
\]

put

\[
g=(S_1,S_2),\qquad L=\operatorname{lcm}(S_1,S_2),\qquad t_i=X_i/S_i.
\]

Primitive gluing has parameter multiplicity one and

\[
\boxed{(e,x,y)=L(1,t_1,t_2)},
\qquad
\boxed{d=L\sqrt{1+t_1^2+t_2^2}}.
\]

The space-square condition also has the exact product closure

\[
\boxed{(X_1X_2)^2+(gd)^2=(H_1H_2)^2.}
\]

Fixing the first face gives

\[
\boxed{E_t:Y^2=X(X-1)(X+t^2).}
\]

## §3. Physical fiber height and positive-rank specialization

For second-face Euclid parameter `q=u/v` in lowest terms, Stage14-4ae gives

\[
\boxed{v\asymp\sqrt{Bg/S_1}}
\]

under the physical cutoff, uniformly up to absolute constants.

For the actual first-face Pythagorean base

\[
r=\frac{X_1}{H_1+S_1},
\qquad t=\frac{2r}{1-r^2},
\]

the pulled-back elliptic surface has six `I4` fibers and geometric generic Mordell--Weil rank zero.

On every genuine rational Pythagorean fiber,

\[
E_t(\mathbf Q)_{tors}\cong\mathbf Z/2\times\mathbf Z/4,
\]

and all torsion points are nonphysical under the Stage14 inverse coordinate. Hence

\[
\boxed{\text{physical raw pair}\Longrightarrow\text{positive-rank specialization}.}
\]

For a fixed first face, the triple/perfect-cuboid locus is a genus-5 curve. This gives fiberwise finiteness only.

## §4. Level-4 modular and Kummer geometry

With

\[
\boxed{\sigma=i\frac{1+r}{1-r}},
\]

one has

\[
\frac{\sigma+\sigma^{-1}}2=it,
\]

so the Stage14 Pythagorean-base K3 is the classical level-4 elliptic modular surface after base change over `Q(i)`. Over `C` it is `Km(E_i x E_i)`.

In the two first/second face Euclid parameters,

\[
\boxed{
Z^2=F(r,s):=(1+r^2)^2(1+s^2)^2-16r^2s^2.
}
\]

## §5. Active rank-jump graph and exponent reduction

Let `G_B` have one vertex for each primitive oriented Pythagorean face state occurring in a raw pair with `d<=B`, and one edge for each raw pair incidence. Write

\[
V(B)=|\mathcal V_B|,
\qquad E(B)=|\mathcal E_B|.
\]

Then

\[
\boxed{E(B)=N_2(B)+3T(B)=\frac12V(B)\bar d(B)}.
\]

If `mu(F)` is the least physical raw-pair height of face state `F`, then

\[
V(B)=\#\{F:\mu(F)\le B\},
\]

and for genuine Pythagorean base states

\[
\mu(F)<\infty\iff\operatorname{rank}E_F(\mathbf Q)>0.
\]

Dujella's uniform bounded-height theorem and the polynomial Stage14 coordinate-height transfer give

\[
\boxed{\max_F\deg_B(F)=B^{o(1)}}.
\]

Hence raw edges and active first-hit vertices have identical limsup and liminf polynomial growth exponents.

Finite data give

```text
B           V(B)     V(B)/sqrt(B)
200,000      155      0.34659
500,000      254      0.35921
1,000,000    347      0.34700
2,000,000    490      0.34648
```

with `200k -> 2m` effective exponent

\[
0.4998643818582221.
\]

No square-root asymptotic is inferred from this finite signal.

## §6. Stage14-4ah — the exact physical Kummer polarization

The independent e3 toric control track resolves the projective two-face map on

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1)
\]

with

\[
\boxed{L=2H_1+2H_2-E_1-E_2-E_3-E_4=-K_Y},
\qquad L^2=4.
\]

The space-square branch numerator `F(r,s)` has homogeneous bidegree `(4,4)`. The four toric corners are

\[
(r,s)=(\pm1,\pm1).
\]

At each corner it has an ordinary double point: the function and first derivatives vanish and

\[
\operatorname{Hess}(F)=
\begin{pmatrix}32&0\\0&32\end{pmatrix}.
\]

Therefore its strict transform on `Y` has class

\[
\boxed{4H_1+4H_2-2\sum E_j=2L=-2K_Y}.
\]

Let

\[
\pi:X\to Y
\]

be the resolved degree-two space-square cover. Define

\[
\boxed{M=\pi^*L}.
\]

If `Phi:X->P2` is the physical projective map, then

\[
\boxed{M=\Phi^*\mathcal O_{\mathbf P^2}(1)},
\qquad
\boxed{M^2=2L^2=8}.
\]

On every primitive Stage14 point,

\[
\boxed{H_M(P)=\sqrt{e^2+x^2+y^2}=d.}
\]

Thus the original cutoff `d<=B` is exactly the `M`-height cutoff on the arithmetic open set.

## §7. `M` is big and nef, not ample

On `Y`, the four strict toric boundary curves

\[
H_1-E_1-E_2,\quad
H_1-E_3-E_4,\quad
H_2-E_1-E_3,\quad
H_2-E_2-E_4
\]

have `L`-degree zero. Their geometric lifts give eight `M`-null `(-2)`-curves on `X`. Hence

\[
\boxed{M\text{ is big and nef but not ample}.}
\]

These null curves are boundary and do not contain primitive positive Stage14 points.

This blocks a direct import of McKinnon's ample-height product-Kummer asymptotic. Its accumulating-curve mechanism remains a guide only.

## §8. Minimum degree of a physical rational curve

Let

\[
f:X\to\mathbf P^1_r
\]

be the first-face elliptic fibration. Its singular base values are

\[
r=0,\infty,\pm1,\pm i,
\]

whereas the physical real base lies in `0<r<1`. Thus no physical rational curve is a vertical singular-fiber component, and a smooth vertical fiber has genus one.

Any physical rational curve `C` therefore dominates the base. Put

\[
n=\deg(C\to\mathbf P^1_r)\ge1.
\]

Since

\[
t(r)=\frac{2r}{1-r^2}
\]

has degree two and `t=x/e` is a quotient of two sections of `M`,

\[
\boxed{M\cdot C\ge\deg(t|_C)=2n.}
\]

If `n=1`, `C` is a section. Generic Mordell--Weil rank is zero and every torsion section is nonphysical. Hence a physical rational curve satisfies

\[
\boxed{n\ge2},
\]

and consequently

\[
\boxed{M\cdot C\ge4.}
\]

## §9. The extremal square-root curve mechanism

Let `C/Q` be a physical rational curve with

\[
m=M\cdot C>0.
\]

After normalization `C~=P1`, the restricted height is an `O(m)` height, so its bounded-height polynomial exponent is

\[
\boxed{2/m}.
\]

Since `m>=4`, every fixed physical rational curve contributes exponent at most `1/2`.

The extremal possibility is

\[
\boxed{M\cdot C=4}.
\]

The multisection bound then forces

\[
\boxed{n=2}.
\]

Therefore the precise rational-curve target capable of explaining a square-root first-hit population is

\[
\boxed{\text{a Q-rational M-degree-4 bisection}.}
\]

Stage14-4ah does not prove existence, completeness, or dominance of such bisections.

## §10. The finite signal survives away from the non-ample boundary

To test whether the finite square-root signal is merely a cusp artifact, active vertices were recounted on fixed compact real subintervals of the first-face base:

```text
B          all V    0.1<=r<=0.9    0.2<=r<=0.8    0.25<=r<=0.75
200k         155          134             105                92
500k         254          227             174               147
1m           347          307             238               197
2m           490          426             338               283
```

The decade effective exponents are

```text
all                 0.4998643818582221
0.1 <= r <= 0.9     0.5023048007379113
0.2 <= r <= 0.8     0.5077274012077166
0.25 <= r <= 0.75   0.4879986081787350
```

Thus the finite `sqrt(B)` signal persists after fixed real cusp neighborhoods are removed. This remains finite evidence only.

## §11. Triple condition as a relative double cover

The third-face-square condition has numerator

\[
\boxed{G(r,s)=r^2(1-s^2)^2+s^2(1-r^2)^2}.
\]

It also has bidegree `(4,4)` and ordinary double points at the four toric corners, now with Hessian

\[
\begin{pmatrix}8&0\\0&8\end{pmatrix}.
\]

Hence its strict zero divisor on `Y` also has class `2L`. Pulling to `X`, the degree-two relative cover obtained by adjoining the third square root

\[
\rho:W\to X
\]

has branch class

\[
\boxed{2M}.
\]

The rational image of a generically nontrivial degree-two cover is a type-II thin subset of `X(Q)`. However, no Stage14 theorem currently gives thin-set zero density for the raw K3 population under the big-and-nef height `M`. Therefore

\[
\boxed{T(B)=o(\sqrt B)}
\]

is still unproved.

## §12. Literature boundary

The level-4/Kummer geometry is classical. McKinnon's product-Kummer point-counting framework establishes the relevance of finite accumulating curve strata for ample heights, but its asymptotic is not imported because the exact Stage14 polarization `M` is only big and nef. Explicit rational curves known on product Kummer surfaces are treated as adjacent mechanisms until their `M`-degree and physical intersection are computed.

No novelty claim is made for the classical Kummer surface or rational-curve constructions.

## §13. Locked decision

```text
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
STAGE14_4AE=COMPLETE
STAGE14_4AF=COMPLETE
STAGE14_4AG=COMPLETE
STAGE14_4AH=COMPLETE

PHYSICAL_KUMMER_POLARIZATION_LOCKED=true
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8
PHYSICAL_POLARIZATION_BIG_NEF_NOT_AMPLE=true
PHYSICAL_RATIONAL_CURVE_M_DEGREE_LOWER_BOUND=4
SQRTB_MINIMAL_RATIONAL_CURVE_TARGET=M-degree-4 rational bisection
MCKINNON_DIRECT_ASYMPTOTIC_IMPORTED=false

RANK_JUMP_GRAPH_IDENTITY_LOCKED=true
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true
FINITE_CORE_SQRTB_SIGNAL_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false

TRIPLE_FIXED_BASE_GENUS=5
TRIPLE_RELATIVE_COVER_BRANCH_CLASS=2M
TRIPLE_TYPE_II_THIN=true
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false

NEXT=Stage14-4ai classify Q-rational M-degree-4 bisections and count their first-hit height; audit triple restriction on those curves
```
