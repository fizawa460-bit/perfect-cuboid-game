# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AI_COMPLETE_MINIMAL_BISECTION_REDUCTION_14_4AJ_NEXT`
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

## §1. Ledgers and finite ceiling

Let `T(B)` count all-three-face objects and let `E(B)=O_pair_raw(B)` be the sum of the three raw face-pair incidences. Then

\[
\boxed{E(B)=N_2(B)+3T(B).}
\]

At `B=2,000,000`, two independent exact enumerators give

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,\qquad T=0.
\]

This is finite evidence only. Frozen Stage13 `R03 + Stage13-12ag` gives

\[
N_2(B)=o(B(\log B)^3)
\]

but no `B`-dependent power saving.

## §2. Exact two-face coordinates and elliptic reduction

For primitive oriented Pythagorean face data

\[
F_i=(S_i,X_i,H_i),\qquad S_i^2+X_i^2=H_i^2,
\]

put

\[
g=(S_1,S_2),\qquad L_0=\operatorname{lcm}(S_1,S_2),\qquad t_i=X_i/S_i.
\]

Primitive gluing has multiplicity one and

\[
(e,x,y)=L_0(1,t_1,t_2),
\qquad d=L_0\sqrt{1+t_1^2+t_2^2}.
\]

The space-square condition is equivalent to

\[
\boxed{(X_1X_2)^2+(gd)^2=(H_1H_2)^2.}
\]

Fixing the first face gives

\[
\boxed{E_t:Y^2=X(X-1)(X+t^2).}
\]

For the actual Pythagorean base

\[
r=\frac{X_1}{H_1+S_1},\qquad t=\frac{2r}{1-r^2},
\]

the elliptic K3 has six `I4` fibers, geometric generic Mordell--Weil rank zero, and only nonphysical rational torsion. Hence every physical raw pair lies on a positive-rank specialization.

## §3. Level-4 Kummer geometry and physical height

Stage14-4ag identifies this K3 over `Q(i)` with the classical level-4 modular surface; over `C` it is `Km(E_i x E_i)`. In the two half-angle variables,

\[
\boxed{Z^2=F(r,s):=(1+r^2)^2(1+s^2)^2-16r^2s^2.}
\]

The independent toric control surface is

\[
Y=\operatorname{Bl}_4(\mathbf P^1_r\times\mathbf P^1_s),
\]

with

\[
\boxed{L=2H_r+2H_s-E_{++}-E_{+-}-E_{-+}-E_{--}=-K_Y},
\qquad L^2=4.
\]

The branch has strict class `2L`. For the resolved double cover

\[
\pi:X\to Y,
\]

Stage14-4ah proves

\[
\boxed{M=\pi^*L=\Phi^*\mathcal O_{\mathbf P^2}(1)},
\qquad \boxed{M^2=8},
\qquad \boxed{H_M=d}.
\]

`M` is big and nef but not ample; its null curves are nonphysical toric-boundary lifts.

## §4. Active rank-jump graph

Let `V(B)` count active oriented first-face states and `E(B)` raw pair edges. Then

\[
\boxed{E(B)=\frac12V(B)\bar d(B)=N_2(B)+3T(B).}
\]

A uniform bounded-height estimate on each elliptic fiber gives

\[
\max_F\deg_B(F)=B^{o(1)},
\]

so raw edges and active vertices have identical polynomial growth exponents.

Finite data give

```text
B           V(B)     V(B)/sqrt(B)
200,000      155      0.34659
500,000      254      0.35921
1,000,000    347      0.34700
2,000,000    490      0.34648
```

with effective exponent `0.4998643818582221` on `200k -> 2m`. No asymptotic law is inferred.

## §5. Stage14-4ah extremal fixed-curve target

For a physical rational curve `C/Q`, put

\[
n=\deg(C\to\mathbf P^1_r).
\]

Because `t(r)` has degree two and `t=x/e` is a quotient of `M`-sections,

\[
M\cdot C\ge2n.
\]

There are no physical sections, hence

\[
\boxed{n\ge2},\qquad \boxed{M\cdot C\ge4}.
\]

For `C~=P1`, a fixed `M`-degree `m` curve contributes bounded-height polynomial exponent `2/m`. Therefore a fixed curve can reach exponent `1/2` only if

\[
\boxed{M\cdot C=4,\qquad n=2.}
\]

Stage14-4ai attacks exactly this minimal bisection problem.

## §6. Stage14-4ai second projection bound

The second half-angle also satisfies

\[
t(s)=\frac{2s}{1-s^2}=y/e,
\]

a quotient of `M`-sections. Hence on a minimal curve

\[
\boxed{\deg(C\to\mathbf P^1_s)\le2.}
\]

Let

\[
D=\pi(C),\qquad \delta=\deg(C\to D)\in\{1,2\}.
\]

This degree bound makes the image-class analysis finite.

## §7. New symmetric `(lambda,mu)` Kummer coordinates

Define

\[
\boxed{\lambda=\frac{1-rs}{r-s}},
\qquad
\boxed{\mu=\frac{1+rs}{r+s}}.
\]

For `0<r<s<1`,

\[
\lambda<-1<1<\mu.
\]

One has the exact identities

\[
\boxed{
(\lambda^2-1)(\mu^2-1)
=\left(\frac{(1-r^2)(1-s^2)}{(r-s)(r+s)}\right)^2,
}
\]

and

\[
\boxed{
(\lambda^2+1)(\mu^2+1)
=\frac{F(r,s)}{(r-s)^2(r+s)^2}.
}
\]

Consequently the Stage14 rationality and space-square conditions combine to

\[
\boxed{(\lambda^4-1)(\mu^4-1)=\square.}
\]

These coordinates are the preferred input for the next CM/Kummer contact analysis.

## §8. `delta=2` is eliminated

If `delta=2`, then `D->P1_r` has degree one and `D->P1_s` has degree at most one. After removal of forced null-boundary components, only two movable mechanisms remain.

### Constant section

For `s=c`,

\[
\operatorname{disc}_rF(r,c)
=2^{16}c^4(c-1)^4(c+1)^4(c^2+1)^4.
\]

For rational `0<c<1` it is nonzero, so the connected inverse image has genus one.

### Opposite-corner `(1,1)` pencil

A representative is

\[
1-rs+k(s-r)=0.
\]

The resolved branch restriction leaves

\[
Q_k=(k^2+1)r^4-8kr^3+6(k^2+1)r^2-8kr+(k^2+1),
\]

with

\[
\operatorname{disc}Q_k=2^{14}(k-1)^6(k+1)^6.
\]

The only rational degenerations are `k=+/-1`, where the defining curve itself splits into toric boundary components.

Therefore

\[
\boxed{\delta=2\text{ gives no physical irreducible }M\text{-degree-4 bisection}.}
\]

## §9. `delta=1`: all genus-zero image classes are eliminated

Now `C` maps birationally to a splitting/contact curve

\[
D=aH_r+2H_s-\sum m_jE_j,
\qquad a\le2,
\]

with

\[
L\cdot D=4,
\qquad \sum m_j=2a.
\]

### Arithmetic-genus-zero cores

For `a=1`, nonnegative arithmetic genus forces two simple toric-corner conditions. After removing forced boundary components, four physical-position classes remain, in two symmetry orbits: same-`r` and opposite-corner.

For `a=2`, the arithmetic-genus-zero multiplicity pattern is `(2,1,1,0)`. Exhausting all placements and removing negative-intersection boundary components reduces every such class to an `a=1` core or a degree-one section.

The two `a=1` orbits are then eliminated by exact square-contact algebra.

#### Same-r orbit

For

\[
P=r\{(-c-d-f)s^2-es+c\}+ds^2+es+f=0,
\]

the resolved branch restriction is `R_-R_+`, with

\[
R_+-R_-=4s(c+f)^2(s^2+1),
\]

and

\[
\begin{aligned}
\operatorname{Res}(R_-,R_+)=2^{10}(c+f)^8&(c^2+f^2)((d-f)^2+e^2)\\
&((c+d+f)^2+d^2)((2c+d+f)^2+e^2).
\end{aligned}
\]

The rational resultant-zero branches are reducible/boundary or lower-degree. In the coprime branch, square parity plus the difference identity reduces to discriminant-zero cases; the remaining quartic factor has the sum-of-squares certificate

\[
\mathcal R=(p^2+2pq)^2+4q^2(p+2f)^2,
\qquad p=c-f,\ q=d+f,
\]

and again only boundary/reduced cases survive.

#### Opposite-corner orbit

For

\[
P=r\{-(c+e)s^2-(d+f)s+c\}+ds^2+es+f=0,
\]

the resolved restriction is `U_2U_6`, with

\[
\operatorname{disc}U_2=-4(c^2+ce+df)^2.
\]

The only nontrivial resultant-zero branch is `c^2+ce+df=0`. On `c=1`, write `e=-1-df`; then

\[
U_2=(1+f^2)(ds-1)^2,
\]

\[
U_6=(ds-1)^2Q_f(s),
\]

where

\[
Q_f=(1+f^2)s^4-8fs^3+6(1+f^2)s^2-8fs+(1+f^2),
\]

and

\[
\operatorname{disc}Q_f=2^{14}(f-1)^6(f+1)^6.
\]

The rational degenerations `f=+/-1` are boundary factorizations. Thus no genus-zero split core survives.

Hence

\[
\boxed{\text{all genus-zero }\delta=1\text{ minimal image mechanisms are eliminated}.}
\]

## §10. The unique unresolved minimal mechanism

There is one class that must **not** be discarded by setting arithmetic genus equal to geometric genus.

For `a=2` with four simple corner conditions,

\[
\boxed{D=L=-K_Y},
\]

\[
D^2=4,
\qquad p_a(D)=1.
\]

A singular member of `|L|` may have normalization `P1`. If the branch restriction on such a singular rational anticanonical curve is even / a square in `Q(D)`, then `pi^{-1}(D)` splits and produces a physical `M.C=4` rational bisection.

Therefore Stage14-4ai proves only

\[
\boxed{
\text{any remaining fixed-curve }\sqrt B\text{ mechanism must be a split singular anticanonical curve }D\in|L|.
}
\]

It does **not** yet prove that this locus is empty.

## §11. Triple restriction on a hypothetical minimal survivor

The third-face relative cover has branch class `2M`. On a hypothetical minimal rational bisection `C`,

\[
(2M)\cdot C=8.
\]

With eight simple branch intersections, the induced double cover of `C~=P1` has genus

\[
\boxed{3}.
\]

Special tangencies/splitting must be audited separately; no `T=o(sqrt(B))` conclusion follows here. The independent Stage14-t track handles that gate.

## §12. Locked decision

```text
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
STAGE14_4AE=COMPLETE
STAGE14_4AF=COMPLETE
STAGE14_4AG=COMPLETE
STAGE14_4AH=COMPLETE
STAGE14_4AI=COMPLETE_MINIMAL_BISECTION_REDUCTION

PHYSICAL_KUMMER_POLARIZATION_LOCKED=true
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8
LAMBDA_MU_KUMMER_COORDINATES_LOCKED=true

DEGREE_TWO_IMAGE_M4_MECHANISM_ELIMINATED=true
GENUS_ZERO_SPLIT_M4_MECHANISM_ELIMINATED=true
ONLY_REMAINING_FIXED_SQRTB_CURVE_TARGET=split singular anticanonical D in |L|
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=false

RANK_JUMP_GRAPH_IDENTITY_LOCKED=true
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true
FINITE_CORE_SQRTB_SIGNAL_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false

TRIPLE_FIXED_BASE_GENUS=5
TRIPLE_RELATIVE_COVER_BRANCH_CLASS=2M
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false

NEXT=Stage14-4aj singular anticanonical contact discriminant / CM-Kummer lattice classification
```
