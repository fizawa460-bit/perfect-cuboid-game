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
MAX_VERIFIED_B=2000000
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
STAGE13_DOWNSTREAM_MATHEMATICAL_CONTENT=FROZEN
R03_GROK_VERDICT=CLOSED
R03_QWEN_VERDICT=CLOSED
R03_COPILOT_VERDICT=PENDING_FINAL_REVIEW
R03_PAIR_OVERLAP_LITTLE_O_IMPORTED=true
BIJECTIVE_TWO_FACE_PARAMETER_SPACE_LOCKED=true
RATIONAL_SLOPE_HEIGHT_FACTORIZATION_LOCKED=true
TRUE_GROWTH_ORDER_IDENTIFIED=false
SQRT_B_FINITE_CANDIDATE_PRIORITY=HIGH
NEXT=Stage14-4ad quantitative square-condition thinning and sqrt(B) test
```

Canonical source: `stages/stage14/main.md`.

## Counting convention

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The exactly-two directions are

```text
a = ab+ac only = smallest shared edge
b = ab+bc only = middle shared edge
c = ac+bc only = largest shared edge
```

with

\[
N_a^{(2)}=O_{ab,ac}-T,\qquad
N_b^{(2)}=O_{ab,bc}-T,\qquad
N_c^{(2)}=O_{ac,bc}-T.
\]

No perfect-cuboid nonexistence assumption is made.

## Frozen finite census

Two materially different exact cuboid-generation routes agree through `B=2,000,000`. At the ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),\qquad N_2=356,\qquad T=0.
\]

No triple object was found through this finite ceiling; this is not a nonexistence proof.

## Stage13 frozen upstream map

Stage13-12ah freezes the downstream mathematical content at

```text
c843e039306b40bd3693f89d6199da78c2fb4657
```

with contract `R03 + Stage13-12ag`. Stage14 may use the raw directional theorem, fixed-local-factor transfer, exact inert-prime local state, weighted-Wiener/harmonic closure, and pair/triple lower-order theorem.

In particular,

\[
O_{qr}(B)=o(B(\log B)^3),\qquad T(B)=o(B(\log B)^3),
\]

so

\[
\boxed{N_2(B)=o(B(\log B)^3).}
\]

This remains only an inherited ceiling.

## Stage14-4ab — exact two-face bijection

Take two oriented primitive Pythagorean face data

\[
F_1=(S_1,X_1,H_1),\qquad F_2=(S_2,X_2,H_2),
\]

where `S_i` is the leg designated to become the shared edge. Put

\[
g=(S_1,S_2),\qquad \alpha=S_1/g,\qquad \beta=S_2/g.
\]

Primitivity kills exactly the common gluing scale, leaving

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2),\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
d^2&=\beta^2H_1^2+\alpha^2X_2^2.
\end{aligned}}
\]

with `x<y`, exact square test for `d`, and `d<=B`. The parameter-fiber multiplicity of a fixed raw pair incidence is exactly `1`.

## Stage14-4ac — rational-slope height envelope

Define

\[
t_1=X_1/S_1,\qquad t_2=X_2/S_2,\qquad L=\operatorname{lcm}(S_1,S_2).
\]

Then exactly

\[
\boxed{(e,x,y)=L(1,t_1,t_2)}
\]

and

\[
\boxed{d=L\sqrt{1+t_1^2+t_2^2}.}
\]

A raw pair incidence is therefore a pair of positive rational Pythagorean slopes `0<t1<t2` satisfying the third rational-square condition

\[
1+t_1^2+t_2^2\in(\mathbf Q^\times)^2.
\]

The directions become

```text
a: 1<t1<t2
b: t1<1<t2
c: t1<t2<1
```

and exactly-two excludes

\[
t_1^2+t_2^2\in(\mathbf Q^\times)^2.
\]

If

\[
M=L\max(1,t_2)=\max(e,y),
\]

then universally

\[
\boxed{M<d<\sqrt3\,M.}
\]

Thus the Euclidean cutoff is comparable to a max-height cutoff independently of direction.

## Divisor multiplicity before the space-square condition

Let `a(S)` be the number of oriented primitive Pythagorean faces whose distinguished shared leg is `S`. Stage14-4ac proves

\[
\boxed{
a(S)=
\begin{cases}
0,&S\le1\text{ or }S\equiv2\pmod4,\\
2^{\omega(S)-1},&\text{otherwise}.
\end{cases}}
\]

The audit verifies this for every `S<=1000`.

If the space-diagonal square condition is temporarily ignored, the lcm denominator envelope

\[
E(B)=\sum_{\operatorname{lcm}(S_1,S_2)\le B}a(S_1)a(S_2)
\]

has standard Selberg--Delange scale

\[
\boxed{B(\log B)^7}.
\]

For the majorant `c(n)=2^omega(n)`, the exact odd-prime local factor is

\[
1+\frac{8p^{-s}}{(1-p^{-s})^2},
\]

so the Dirichlet pole order is `8`. This is only a pre-space denominator envelope, not the Stage14 population.

The contrast explains why Stage13 R03 is so useful: it replaces this very loose face-pair envelope by the genuine integer-space-diagonal ceiling `o(B(log B)^3)`.

## First Stage14-4 growth candidate

The frozen finite totals give

```text
B          N2       N2/sqrt(B)
200,000    116      0.2593838854
500,000    188      0.2658721497
1,000,000  255      0.2550000000
2,000,000  356      0.2517300141
```

The late-range coefficient of variation of `N2/sqrt(B)` is about `0.02053`.

This makes `sqrt(B)` a high-priority candidate for Stage14-4ad, but Stage14 does **not** currently claim

\[
N_2(B)\sim C\sqrt B
\]

or any `sqrt(B)` upper/lower bound.

Artifacts:

```text
stages/stage14/archive/stage14-4ac-height-envelope.md
stages/stage14/scripts/14-4/height_envelope_audit.py
stages/stage14/data/14-4/height_envelope_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## What remains unknown

Stage14 still has not identified the true growth order, leading constant, limiting directional vector, eventual leader, or whether `T(B)` ever becomes positive.

Next:

```text
14-4ad  quantify the extra second-face rational-square thinning inside the
        frozen Stage13 R03 one-face ambient family, and directly test whether
        the observed sqrt(B) scale can be proved or decisively rejected.
```
