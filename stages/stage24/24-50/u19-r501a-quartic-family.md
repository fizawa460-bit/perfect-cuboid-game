# Stage24-u19-r501a — mixed-parity quartic lift gives an infinite Stage19 family

CHECKPOINT=50
ROLE=FRESH_STAGE19_LOWER_SURGEON_BREAKTHROUGH
EVIDENCE_LEVEL=PROVED_WITH_STATED_STANDARD_THEOREMS

## 1. Source mutation: reopen the Stage18 explicit family at the parity boundary

Stage15-2 used coprime **odd** parameters `p,q` and

\[
e=4pq,\qquad x=4p^2-q^2,\qquad y=4q^2-p^2.
\]

The algebraic identities themselves do not require odd parity:

\[
e^2+x^2=(4p^2+q^2)^2,
\qquad
 e^2+y^2=(4q^2+p^2)^2,
\]

and

\[
e^2+x^2+y^2=17(p^4+q^4).
\]

The old odd/odd Stage19 lift fails globally because `17(p^4+q^4)=2 (mod 16)`. The fresh lower surgeon therefore does not discard the formula: it removes only the parity specialization and asks for mixed-parity rational points on

\[
\boxed{C_{17}:\ p^4+q^4=17Z^2.}
\]

For such a point the space diagonal is

\[
\boxed{D=17Z.}
\]

This is the exact Stage18-to-Stage19 space lift of the same ambient formula.

## 2. The quartic is a genus-one curve with positive rank

Put

\[
t=q/p,\qquad z=Z/p^2.
\]

Then `C_17` is

\[
\boxed{17z^2=t^4+1.}
\]

The quartic `t^4+1` has four simple roots over `Qbar`, so its smooth projective normalization has genus one. It has the rational point

\[
(t,z)=(2,1).
\]

There is a rational nonconstant map to

\[
\boxed{E:\ Y^2=X^3-1156X}
\]

given by

\[
X=-\frac{4t^2}{z^2},
\qquad
Y=\frac{4t(t^4-1)}{z^3}.
\]

Indeed, using `17z^2=t^4+1`,

\[
Y^2-(X^3-1156X)
=\frac{16t^2}{z^6}\left((t^4-1)^2-(t^4+1)^2+4t^4\right)=0.
\]

The rational point `(2,1)` maps to

\[
P=(-16,120)\in E(\mathbf Q).
\]

### Infinite-order certificate without a torsion classification

The discriminant of `E` has prime support only at `2` and `17`, so `31` and `41` are primes of good reduction. Exact finite-field enumeration gives

\[
\#E(\mathbf F_{31})=32,
\qquad
\#E(\mathbf F_{41})=52.
\]

The reduction of `P` modulo `31` has exact order `16`.

If `P` were rational torsion of order `N`, good-reduction injectivity on prime-to-residue-characteristic torsion gives

- from `p=31`, `N/31^{v_{31}(N)}` divides `32`;
- from `p=41`, `N/41^{v_{41}(N)}` divides `52`.

The second line removes a possible factor `31`, the first removes a possible factor `41`, and comparison of the remaining prime factors forces `N|gcd(32,52)=4`. But the reduction of `P` modulo `31` has order `16`, contradiction. Therefore

\[
\boxed{P\text{ has infinite order on }E(\mathbf Q).}
\]

A nonconstant morphism between smooth projective genus-one curves, after choosing rational origins, induces an isogeny of their Jacobians. Since `C_17(Q)` is nonempty and its Jacobian is isogenous to the positive-rank curve `E`,

\[
\boxed{\operatorname{rank} C_{17}(\mathbf Q)>0}
\]

in the usual identification of a genus-one curve with its Jacobian after choosing an origin. Hence `C_17(Q)` is infinite.

The deterministic verifier `quartic_family_audit.py` independently checks the elliptic-map identity on exact points, the two good-reduction group orders, and the order-16 reduction certificate.

## 3. Every reduced rational point gives integral mixed-parity parameters

Take a positive rational point `(t,z)` and write

\[
t=q/p
\]

in lowest positive terms. Put `Z=p^2z`. Then

\[
17Z^2=p^4+q^4\in\mathbf Z.
\]

If `Z=a/b` is reduced, then `b^2|17`; since `17` is squarefree, `b=1`. Thus

\[
\boxed{Z\in\mathbf Z.}
\]

Because `(p,q)=1`, they cannot both be even. They also cannot both be odd: then

\[
p^4+q^4\equiv2\pmod{16},
\]
while `17Z^2` is a square residue modulo `16`. Therefore every primitive rational parameter pair on `C_17` has opposite parity.

## 4. Physical primitivity and the two guaranteed square faces

For coprime opposite-parity positive `p,q`, define

\[
e=4pq,\quad x=4p^2-q^2,\quad y=4q^2-p^2,\quad D=17Z.
\]

The two face diagonals are

\[
h_x=4p^2+q^2,
\qquad
h_y=4q^2+p^2,
\]

because

\[
e^2+x^2=h_x^2,\qquad e^2+y^2=h_y^2.
\]

The space identity is

\[
e^2+x^2+y^2
=17(p^4+q^4)
=289Z^2
=D^2.
\]

Global primitivity is automatic. Let an odd prime `ell` divide `e`. Then `ell|p` or `ell|q`. If `ell|p`,

\[
x\equiv-q^2\not\equiv0\pmod\ell;
\]

if `ell|q`,

\[
y\equiv-p^2\not\equiv0\pmod\ell.
\]

The prime `2` cannot divide all three edges because opposite parity makes one of `x,y` odd. Hence

\[
\boxed{\gcd(e,x,y)=1.}
\]

## 5. A physical canonical open cone contains a rational point

Let

\[
\alpha=\frac{1+\sqrt2}{2}.
\]

On the open interval

\[
1<t=q/p<\alpha
\]

we have

\[
x>0,\qquad x<y,\qquad e>x,\qquad e>y.
\]

The last inequality is exactly

\[
4t>4t^2-1,
\]
which holds for `t<alpha`. Therefore the canonical ordering is

\[
\boxed{(a,b,c)=(x,y,e)}.
\]

The cone is nonempty on `C_17(Q)`. An exact point is

\[
(p,q,Z)=(38,43,569),
\]
so

\[
(a,b,c,D)=(3927,5952,6536,9673).
\]

Its two guaranteed face diagonals are `7625` and `8840`, and its third face is nonsquare. A second exact mixed-parity point is

\[
(p,q,Z)=(859,1186,385241),
\]
which gives

\[
(a,b,c,D)=(1544928,4075096,4888503,6549097)
\]

after canonical sorting; the raw shared-edge ordering is `(x,y,e)=(1544928,4888503,4075096)`, so this second witness lies outside the largest-shared-edge cone and is used only as a regression witness.

For points in the cone the parameter ratio is recoverable from the box. Indeed

\[
x+y=3(p^2+q^2),
\qquad
y-x=5(q^2-p^2),
\]
so `p^2,q^2` are uniquely determined. Hence distinct reduced positive ratios in this cone give distinct primitive canonical boxes.

## 6. Infinitely many C17 rational points enter the physical cone

Choose any rational origin on the genus-one curve. Since `C_17(Q)` has positive rank, it contains a non-torsion rational point `R`. Replacing `R` by `2R` if necessary places it in the identity component of `C_17(R)`.

The identity component of a real elliptic curve is a circle group. The cyclic subgroup generated by a non-torsion point is dense in that circle. Translating by the physical rational point `(38,43,569)` therefore gives infinitely many rational points of `C_17` in every sufficiently small real neighborhood of `43/38`, hence infinitely many with

\[
1<q/p<\alpha.
\]

This step uses only the standard real Lie-group description of an elliptic curve; it does not use the finite census.

## 7. The third-square sublocus has genus five, hence only finitely many rational points

The third face is square exactly when there is `w in Q` with

\[
w^2=(4-t^2)^2+(4t^2-1)^2
=17t^4-16t^2+17.
\]

Thus triple-face points inside the quartic family lie on the normalization of

\[
17z^2=t^4+1,
\qquad
w^2=17t^4-16t^2+17.
\]

Over `Qbar(t)` the two squareclasses are independent:

- `t^4+1` has four simple roots;
- `17t^4-16t^2+17` has four simple roots, since its derivative is `4t(17t^2-8)`, while its values at the derivative-critical squares are nonzero;
- the two branch sets are disjoint, because at a root of `t^4+1` the second polynomial equals `-16t^2`, which cannot vanish there.

The normalized fiber product is therefore a connected `V_4` degree-four cover of `P^1` with eight disjoint simple branch values. At each branch value two points upstairs have ramification index two, so the total ramification contribution is `16`. Riemann-Hurwitz gives

\[
2g-2=4(-2)+16=8,
\]
therefore

\[
\boxed{g=5.}
\]

By Faltings' theorem, a smooth projective genus-five curve over `Q` has only finitely many rational points. Consequently only finitely many rational points of `C_17` make the third face square.

This is a statement only about the present special family. It is **not** a perfect-cuboid nonexistence theorem.

Combining Sections 6 and 7, infinitely many rational points remain in the physical cone with exactly two, not three, integral face diagonals. Therefore

\[
\boxed{N_2(B)\to\infty.}
\]

Equivalently, Stage19 now has a certified infinite primitive construction, pending fresh checkpoint50 audit.

## 8. Quantitative lower bound from elliptic height

The same construction gives more than bare unboundedness.

Let `Q_n=Q_0+nR` on `C_17`, with `R` a fixed non-torsion rational point in the relevant real component. Standard elliptic height theory gives, for the fixed rational function `t`,

\[
h(t(Q_n))=O(n^2).
\]

Writing `t(Q_n)=q_n/p_n` in lowest terms therefore gives

\[
\max(p_n,q_n)\le \exp(Cn^2)
\]
for a fixed constant `C`. Since

\[
D_n=17Z_n,
\qquad
Z_n^2=\frac{p_n^4+q_n^4}{17},
\]
we have

\[
D_n\le \sqrt{34}\,\max(p_n,q_n)^2
\le \exp(C' n^2).
\]

The non-torsion rotation is equidistributed on its real circle component, so a fixed positive proportion of `1<=n<=N` enter a small open interval contained in the physical cone. The projection `C_17 -> P^1_t` has fixed degree two, and the physical box map is injective on reduced positive `t` in the cone; hence this produces `gg N` distinct physical boxes. Removing the finitely many genus-five triple points changes only `O(1)` terms.

Taking `N` proportional to `sqrt(log B)` yields

\[
\boxed{N_2(B)\gg \sqrt{\log B}}
\]
for all sufficiently large `B`.

The implied constant and threshold are existential; Faltings is used only to remove a finite exceptional set. This is not a positive power of `B`.

## 9. Exact theorem boundary

The new lower stack is therefore

\[
\boxed{\sqrt{\log B}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}.
\]

What is newly proved at checkpoint50, subject to fresh audit:

```text
STAGE19_UNBOUNDEDNESS_PROVED=true
INFINITE_PRIMITIVE_STAGE19_CONSTRUCTION_PROVED=true
NEW_LOWER_BOUND=N2(B)>>sqrt(log B)
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
```

The old Stage19 checkpoint50 statement `unboundedness not proved` is therefore a historical statement superseded by this later Stage24 discovery if and only if fresh Stage24 checkpoint50 audit passes.
