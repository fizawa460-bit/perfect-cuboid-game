# Stage25-reentry-20 — directional quarter-power theorem

```text
TASK_ID=Stage25-u24-r002a
REENTRY_PHASE=20
ROLE=STAGE24_DIRECTIONAL_REATTACK
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## Theorem candidate

Let `N_{2,j}(B)` count primitive canonical Stage19 boxes of height `R<=B` whose two integral faces share canonical edge `j in {a,b,c}`. Then

\[
\boxed{N_{2,a}(B)\gg B^{1/4}},\qquad
\boxed{N_{2,b}(B)\gg B^{1/4}},\qquad
\boxed{N_{2,c}(B)\gg B^{1/4}}.
\]

The `b` statement is the already-audited R501 cone used in Stage25 checkpoint50. The `c` statement follows from the audited R502 family. The new work here is an alternative physical cone of the same audited R501 formulas, which moves the shared raw edge to canonical edge `a` without changing the degree-eight height or the genus-seven third-face exception argument.

## 1. Audited R501 formulas

For a reduced rational parameter `t=m/n`, the R501 homogeneous family is

\[
A=16m^2n^2(m^4-9n^4),
\]
\[
B=(m^4-10m^2n^2+9n^4)(m^4+2m^2n^2+9n^4),
\]
\[
C=4mn(m^2+3n^2)(m^4-10m^2n^2+9n^4),
\]
with integral diagonals satisfying

\[
A^2+C^2=D_{AC}^2,\qquad
B^2+C^2=D_{BC}^2,\qquad
A^2+B^2+C^2=D^2,
\]
where

\[
D=m^8+46m^4n^4+81n^8.
\]

Thus the two guaranteed faces share the raw edge `C`. The audited R501 proof also establishes that the remaining face square is governed by one fixed squarefree degree-16 polynomial, hence a genus-seven hyperelliptic curve; only finitely many rational parameter values produce a third rational face. Primitive reduction preserves every required diagonal and can only decrease physical height.

## 2. New physical cone: `9/2 < t < 5`

Dehomogenize the three raw edges:

\[
A(t)=16t^2(t^4-9),
\]
\[
B(t)=(t^4-10t^2+9)(t^4+2t^2+9),
\]
\[
C(t)=4t(t^2+3)(t^4-10t^2+9).
\]

For `t>9/2`, all factors are positive. We prove that `C` is the smallest raw edge throughout the open cone `9/2<t<5`.

First,

\[
B-C=(t-3)(t-1)(t+1)(t+3)Q_1(t),
\]
where

\[
Q_1(t)=t^4-4t^3+2t^2-12t+9.
\]
Since

\[
Q_1'(t)=4(t-3)(t^2+1)>0\quad(t>9/2)
\]
and

\[
Q_1(9/2)=657/16>0,
\]
we have `B>C` on the whole cone.

Second,

\[
A-C=-4t(t^2+3)Q_2(t),
\]
where

\[
Q_2(t)=t^4-4t^3-10t^2+12t+9.
\]
Now

\[
Q_2'(t)=4H(t),\qquad H(t)=t^3-3t^2-5t+3,
\]
with

\[
H'(t)=3t^2-6t-5>0\quad(t>9/2),
\]
and `H(9/2)>0`. Hence `Q_2` is increasing on the cone. Since

\[
Q_2(5)=-56<0,
\]
we have `Q_2(t)<0` for every `9/2<t<5`, so `A>C`.

Therefore

\[
\boxed{0<C<\min(A,B)}.
\]

After primitive reduction and canonical sorting, the raw shared edge `C` is exactly the canonical smallest edge `a`. Hence every nonexceptional parameter in this cone contributes to `N_{2,a}`.

## 3. Quadratically many reduced parameters

Let `T` be large. For every `n<=T/5`, put

\[
m=5n-k,
\qquad 1\le k<n/2,
\qquad \gcd(k,n)=1.
\]

Then

\[
9/2<m/n<5,
\qquad \gcd(m,n)=1,
\qquad m\le T.
\]

For `n>2`, half of the reduced residues lie below `n/2`, so the number of such parameters is

\[
\frac12\sum_{n\le T/5}\varphi(n)+O(1)\asymp T^2.
\]

## 4. Height and multiplicity

For `m,n<=T`,

\[
D=m^8+46m^4n^4+81n^8\le128T^8.
\]

Primitive reduction only decreases `D`. Thus `T\asymp B^{1/8}` gives `\gg B^{1/4}` reduced parameters below height `B`.

To control similarity multiplicity on this new cone, use the scale-free invariant

\[
r_a(t)=\frac{C(t)}{D(t)}
=\frac{4t(t^2+3)(t^4-10t^2+9)}{t^8+46t^4+81}.
\]

It is determined by the primitive canonical box because `C` is the canonical smallest edge and `D` is the space diagonal. For a fixed rational value `r_0`, clearing denominators gives a nonzero polynomial equation of degree at most eight. Therefore every primitive canonical similarity class has at most eight R501 parameters in this cone.

The genus-seven third-face exception set is finite, exactly as in the audited R501 proof, because the missing raw face remains `(A,B)` and the same squarefree degree-16 polynomial is used. Removing finitely many parameters does not change the lower order.

Hence

\[
\boxed{N_{2,a}(B)\gg B^{1/4}}.
\]

## 5. The other two directions

### Shared canonical edge `b`

The audited R501 cone `7/2<t<4` has

\[
0<B<C<A,
\]
so the same raw shared edge `C` becomes canonical edge `b`. Its audited count gives

\[
\boxed{N_{2,b}(B)\gg B^{1/4}}.
\]

### Shared canonical edge `c`

For the audited R502 family on `7/2<t<4`, the canonical ordering is

\[
0<A<B<C,
\]
and the guaranteed faces are again `(A,C)` and `(B,C)`. Thus the shared raw edge `C` is canonical edge `c`. The audited theorem `N_{R502}(B)=Theta(B^(1/4))` therefore gives

\[
\boxed{N_{2,c}(B)\gg B^{1/4}}.
\]

Combining the three cones proves the candidate directional theorem.

## 6. Stage24 directional survival and interaction

Stage24 already imports the audited Stage18 directional asymptotics

\[
M_{2,j}(B)\sim C_jB(\log B)^5,\qquad C_j>0,
\]
for `j=a,b,c`, and the whole-family upper gives

\[
N_{2,j}(B)\le N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Therefore, for every `j=a,b,c`,

\[
\boxed{
B^{-3/4}(\log B)^{-5}
\ll_j
\frac{N_{2,j}(B)}{M_{2,j}(B)}
\ll_{\varepsilon,j}
B^{-1/2+\varepsilon}(\log B)^{-5}
}.
\]

Using the Stage16S ambient space-survival baseline `S_0(B)\asymp B^{-1}`, define

\[
J_{2,j}(B)=\frac{N_{2,j}(B)/M_{2,j}(B)}{S_0(B)}.
\]
Then

\[
\boxed{J_{2,j}(B)\gg_j B^{1/4}(\log B)^{-5}\to\infty}
\]
for all three directions. Thus the positive-divergent Stage24 interaction is not confined to one shared-edge chamber.

## 7. Stage23 overlap consequence

A Stage19 object with shared edge `a`, `b`, or `c` belongs respectively to the raw Stage17 pair-overlap channels

\[
A_{ab,ac},\qquad A_{ab,bc},\qquad A_{ac,bc}.
\]

Therefore the candidate backflow is

\[
\boxed{A_{ab,ac}(B)\gg B^{1/4}},
\quad
\boxed{A_{ab,bc}(B)\gg B^{1/4}},
\quad
\boxed{A_{ac,bc}(B)\gg B^{1/4}}.
\]

The `ab,bc` statement was already known from R501 backflow. The `ac,bc` statement upgrades the older C17 `sqrt(log B)` channel, and `ab,ac` is new.

## 8. Boundary

This directional theorem does not change the global Stage19 envelope

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

It does not identify the true exponent, prove a strict sub-half whole-family upper, or solve the moving-family/growing-modulus uniformity gate. The R503/R504/R505 residual problems remain external gates. No perfect-cuboid existence or nonexistence conclusion is made.

```text
NEW_DIRECTIONAL_THEOREM_CANDIDATE=true
ALL_SHARED_EDGE_DIRECTIONS_POSITIVE_POWER=true
DIRECTIONAL_EXPONENT_A=1/4
DIRECTIONAL_EXPONENT_B=1/4
DIRECTIONAL_EXPONENT_C=1/4
GLOBAL_N2_EXPONENT_UPGRADED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
MOVING_FAMILY_UNIFORMITY_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
PERFECT_CUBOID_CONCLUSION=NONE
FRESH_AUDIT_REQUIRED=true
```
