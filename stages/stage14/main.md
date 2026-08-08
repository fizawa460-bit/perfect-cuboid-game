# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AE_COMPLETE_HEIGHT_RANK_14_4AF_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals. Stage14-1 through Stage14-3 are complete. Stage14-4 is active at proof level. The Stage13 `R03 + Stage13-12ag` downstream mathematical contract is frozen and available as upstream input.

## §1. Locked population and ledgers

For `B>=1`, count

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Let

\[
I_{ab}=\mathbf1_{a^2+b^2=\square},\quad
I_{ac}=\mathbf1_{a^2+c^2=\square},\quad
I_{bc}=\mathbf1_{b^2+c^2=\square}.
\]

Raw pair counts are

\[
O_{ab,ac}=\sum I_{ab}I_{ac},\quad
O_{ab,bc}=\sum I_{ab}I_{bc},\quad
O_{ac,bc}=\sum I_{ac}I_{bc},
\]

and the triple population is

\[
T=\sum I_{ab}I_{ac}I_{bc}.
\]

Exactly-two directions are

\[
N_a^{(2)}=O_{ab,ac}-T,
\qquad
N_b^{(2)}=O_{ab,bc}-T,
\qquad
N_c^{(2)}=O_{ac,bc}-T,
\]

where

```text
a = shared smallest edge
b = shared middle edge
c = shared largest edge
```

and

\[
N_2=N_a^{(2)}+N_b^{(2)}+N_c^{(2)}.
\]

No perfect-cuboid nonexistence assumption is made.

## §2. Frozen finite facts

Two independent exact generation routes agree at all 11 audited cutoffs through `B=2,000,000`. At the ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,
\qquad T=0.
\]

This is finite evidence only. Stage14-3 inferred no limiting ratio or monotonicity theorem.

## §3. Frozen Stage13 theorem contract

Stage13 freezes downstream mathematical content at

```text
c843e039306b40bd3693f89d6199da78c2fb4657
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
```

Stage14 may use

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad T(B)=o(B(\log B)^3),
\]

hence

\[
\boxed{N_2(B)=o(B(\log B)^3).}
\]

At inert `p=3 mod 4`, the frozen local multiplier is

\[
\lambda_p=\frac{p+5}{2(p+1)}.
\]

The R03 proof fixes a finite prime set, sends `B->infinity`, then enlarges the prime set. It proves zero density but no `B`-dependent power saving. No growing-modulus statement is imported into Stage14.

## §4. Exact two-face coordinates

Let the two integral faces share edge `e`; let the other edges be `x<y`. Take two oriented primitive Pythagorean face data

\[
F_i=(S_i,X_i,H_i),
\qquad S_i^2+X_i^2=H_i^2,
\]

where `S_i` is the distinguished shared-edge leg. Put

\[
g=\gcd(S_1,S_2),
\qquad \alpha=S_1/g,
\qquad \beta=S_2/g.
\]

The shared-edge scale equation has complete solution

\[
k_1=t\beta,
\qquad k_2=t\alpha.
\]

The minimal gluing is primitive and the physical cuboid gcd equals `t`; therefore primitive cuboids force `t=1`. Hence

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2),\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
u&=\beta H_1,\\
v&=\alpha H_2,\\
d^2&=\beta^2H_1^2+\alpha^2X_2^2.
\end{aligned}}
\]

After `x<y`, a fixed raw pair incidence has parameter-fiber multiplicity exactly `1`.

## §5. Rational-slope and product-square reductions

Define

\[
t_i=X_i/S_i,
\qquad
L=\operatorname{lcm}(S_1,S_2).
\]

Then

\[
\boxed{(e,x,y)=L(1,t_1,t_2)},
\qquad
\boxed{d=L\sqrt{1+t_1^2+t_2^2}}.
\]

The directions are only chamber inequalities:

```text
a: 1<t1<t2
b: t1<1<t2
c: t1<t2<1
```

Exactly-two excludes

\[
t_1^2+t_2^2\in(\mathbf Q^\times)^2.
\]

The space condition also has the exact product closure

\[
\boxed{(X_1X_2)^2+(gd)^2=(H_1H_2)^2.}
\]

With

\[
\rho_i=X_i/H_i,
\]

it becomes

\[
\boxed{1-(\rho_1\rho_2)^2\in(\mathbf Q^\times)^2.}
\]

## §6. Elliptic fiber

Fix the first face and parameterize the second rational unit-circle point by

\[
\rho_2=\frac{2q}{1+q^2}.
\]

The remaining square condition is the nonsingular Jacobi quartic

\[
W^2=q^4+2Aq^2+1,
\qquad A=1-2\rho_1^2.
\]

An explicit birational transformation gives the fiber

\[
\boxed{E_{t_1}:Y^2=X(X-1)(X+t_1^2)}.
\]

Its `j`-invariant

\[
 j(t_1)=256\frac{(1+t_1^2+t_1^4)^3}{t_1^4(1+t_1^2)^2}
\]

is nonconstant, so the family is non-isotrivial.

## §7. Stage14-4ae — exact physical fiber height

Write the second-face circle parameter in lowest terms as

\[
q=u/v,
\qquad 0<u<v,
\qquad (u,v)=1.
\]

Let

\[
\delta=\gcd(v^2-u^2,2uv,u^2+v^2)\in\{1,2\}.
\]

Then the primitive second face is exactly

\[
\boxed{
S_2=\frac{v^2-u^2}{\delta},
\quad
X_2=\frac{2uv}{\delta},
\quad
H_2=\frac{u^2+v^2}{\delta}.
}
\]

Therefore

\[
\boxed{\frac{v^2}{2}<H_2<2v^2.}
\]

Let `Q2=max(S2,X2)`. Since `Q2<H2<sqrt(2)Q2` and

\[
M=L\max(1,t_2)=\frac{S_1}{g}Q_2,
\]

the Stage14 max-height inequality `M<d<sqrt(3)M` gives

\[
\boxed{
\frac{S_1H_2}{\sqrt2\,g}
<d<
\frac{\sqrt3\,S_1H_2}{g}.
}
\]

Thus, with

\[
Q_B(F_1,g)=\sqrt{\frac{Bg}{S_1}},
\]

there are universal constants

\[
c_-=(2\sqrt3)^{-1/2},
\qquad
c_+=2^{3/4}
\]

such that

\[
\boxed{
v\le c_-Q_B\Longrightarrow d<B\Longrightarrow v<c_+Q_B.}
\]

This is the first rigorous structural explanation for the square-root scale seen in the **fiber height**. It is not yet a total-population theorem.

Also `H1<d`, so only first-face data with `H1<B` contribute.

## §8. Elliptic height comparison

Let

\[
s=S_1/H_1.
\]

The Stage14-4ad birational formulas simplify to the exact inverse

\[
\boxed{q(P)=\frac{X(P)}{sY(P)}}.
\]

For a fixed nonsingular fiber this is a rational function of degree `2`. Standard fixed-curve elliptic height theory gives

\[
\boxed{h(q(P))=2\widehat h(P)+O_{t_1}(1).}
\]

The physical cutoff therefore implies

\[
\widehat h(P)
\le \frac14\log\frac{Bg}{S_1}+O_{t_1}(1).
\]

If the fixed fiber has rank `r`, the Mordell--Weil lattice gives

\[
\#\{P:\widehat h(P)\le T\}=O_E(T^{r/2}),
\]

so one fixed first face contributes only polylogarithmically in `B`.

A uniform control of the `O_{t_1}(1)` term as the base varies is **not** assumed and remains part of the global problem.

## §9. The geometric generic Mordell--Weil rank is zero

Regard

\[
\mathscr E:y^2=x(x-1)(x+t^2)
=x^3+(t^2-1)x^2-t^2x
\]

as an elliptic surface over the `t`-line. Its invariants are

\[
\boxed{\Delta(t)=16t^4(1+t^2)^2},
\qquad
\boxed{c_4(t)=16(1+t^2+t^4)}.
\]

Over `Qbar` the singular fibers are

```text
t=0        : I4
t=+i       : I2
t=-i       : I2
t=infinity : I4
```

At infinity, `u=1/t` and the minimal equation is

\[
Y^2=X(X+1)(X-u^2).
\]

The Euler numbers sum to `12`, so this is a rational elliptic surface. Its geometric Picard number is `10`. The reducible-fiber root rank is

\[
(4-1)+(4-1)+(2-1)+(2-1)=8.
\]

Shioda--Tate therefore gives

\[
\boxed{\operatorname{rank}\mathscr E(\overline{\mathbf Q}(t))=10-2-8=0.}
\]

Hence there is no non-torsion generic section even after extending constants. Stage14 physical points must come from special fibers: rank-jump specializations and/or specializations with extra torsion.

The true global question is therefore not merely average rank. It is an **average small-point specialization problem**: which Pythagorean base values acquire a point whose canonical / `q` height is low enough to satisfy the physical cutoff?

## §10. Rigorous raw-pair counting skeleton

For first face `F1=(S1,X1,H1)` and divisor `g|S1`, let

\[
\mathcal N_{F_1,g}(Q)
\]

count physical non-boundary points on `E_{t1}` with reduced `q=u/v`, `v<=Q`, reconstructed `gcd(S1,S2)=g`, and the correct ordering `t1<t2`.

Then

\[
\boxed{
\sum_{F_1:H_1<B}\sum_{g|S_1}
\mathcal N_{F_1,g}\!\left(c_-\sqrt{\frac{Bg}{S_1}}\right)
\le O_{\rm pair}^{raw}(B)
\le
\sum_{F_1:H_1<B}\sum_{g|S_1}
\mathcal N_{F_1,g}\!\left(c_+\sqrt{\frac{Bg}{S_1}}\right).
}
\]

The remaining inputs are now explicit:

1. frequency of rank-jump / extra-torsion specializations with a physical point;
2. uniform `q`-height versus canonical-height comparison;
3. first small-point height / regulator / successive minima;
4. the `gcd(S1,S2)=g` coupling;
5. the primitive Pythagorean restriction on the base;
6. the frozen R03 local restrictions.

## §11. Raw pair is not yet exactly-two

The elliptic fibration counts raw pair incidences. Exactly

\[
\boxed{
O_{\rm pair}^{raw}(B)
=O_{ab,ac}+O_{ab,bc}+O_{ac,bc}
=N_2(B)+3T(B).
}
\]

Finite data have `T=0` through `B=2,000,000`, but frozen R03 only proves

\[
T(B)=o(B(\log B)^3).
\]

That is insufficient to deduce `T=o(sqrt(B))`. Therefore even a future `sqrt(B)` raw-pair theorem requires a separate triple-subtraction theorem before it becomes a theorem for exactly-two.

## §12. Validation and locked decision

The Stage14-4ae deterministic audit checks all 25 raw-pair incidences at `B=10000`. It reproduces exactly-two `(9,11,5)` with `T=0` and verifies:

```text
second primitive face reconstructed from reduced q=u/v
v^2/2 < H2 < 2v^2
S1 H2/(sqrt(2)g) < d < sqrt(3) S1 H2/g
elliptic equation
q=X/(sY)
```

Artifacts:

```text
stages/stage14/archive/stage14-4ae-height-rank.md
stages/stage14/scripts/14-4/height_rank_audit.py
stages/stage14/data/14-4/height_rank_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

```text
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
STAGE14_4AE=COMPLETE

UNIFORM_SECOND_FACE_HEIGHT_COMPARISON=true
SECOND_FACE_Q_DENOMINATOR_SQUARE_ROOT_HEIGHT=true
ELLIPTIC_Q_INVERSE=q=X/(sY)
FIXED_FIBER_POINT_GROWTH_POLYLOGARITHMIC=true
ELLIPTIC_SURFACE_FIBERS=I4_I4_I2_I2
GEOMETRIC_GENERIC_MW_RANK=0
GLOBAL_PROBLEM=SMALL_POINT_RANK_JUMP_OR_EXTRA_TORSION_SPECIALIZATIONS
RAW_PAIR_HEIGHT_SUM_LOCKED=true
RAW_PAIR_TO_EXACTLY_TWO_REQUIRES_TRIPLE_CONTROL=true
SQRT_B_STRUCTURAL_HEIGHT_SOURCE_IDENTIFIED=true
SQRT_B_ASYMPTOTIC_CLAIM=false
SQRT_B_RIGOROUS_UPPER_BOUND=false
SQRT_B_RIGOROUS_LOWER_BOUND=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
LEADING_CONSTANT_IDENTIFIED=false

NEXT=Stage14-4af small-point specialization and triple-subtraction analysis
```
