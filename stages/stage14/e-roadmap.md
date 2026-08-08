# Stage14-e roadmap — two-face ambient control population

## Purpose

Stage14-e is an independent front-side control track for the exactly-two integral-face problem. The main Stage14 track keeps the integer-space-diagonal condition; Stage14-e deliberately removes it to measure what that final square condition removes from the natural two-face ambient family.

The e-track does not replace or renumber Stage14-4 / Stage14-5.

## Literature-first rule

Every e-substage must refresh the relevant literature before promoting a parametrization, structural theorem, asymptotic mechanism, or novelty claim. Classify the nearest literature as

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
```

Absence in a search is never a novelty certificate. Classical rational-cuboid work, Euler-brick tables, nearly-perfect cuboids, arithmetic surfaces, elliptic fibrations, modern search algorithms, current preprints, and general height-counting theorems all belong in the search scope.

Canonical literature records:

```text
stages/stage14/14-e1/literature-seed.md
stages/stage14/14-e2/literature-refresh.md
stages/stage14/14-e3/literature-asymptotic-audit.md
stages/stage14/14-e4/literature-directional-audit.md
```

## Locked ambient object

Let `e,x,y` be positive integers with `x<y` and

\[
\gcd(e,x,y)=1.
\]

Require

\[
e^2+x^2=\square,
\qquad
e^2+y^2=\square.
\]

Define the real Euclidean height

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}\le B.
\]

**No condition whatsoever is imposed that `D_R` be an integer or rational.**

The exactly-two ambient population further requires

\[
x^2+y^2\ne\square.
\]

Directions are the shared-edge chambers

```text
a: e<x<y
b: x<e<y
c: x<y<e
```

with counts `E_a(B),E_b(B),E_c(B)` and

\[
E_2(B)=E_a(B)+E_b(B)+E_c(B).
\]

These are not the main Stage14 counts, which additionally require an integer space diagonal.

## Structural coordinates

For two oriented primitive Pythagorean face data

\[
F_i=(S_i,X_i,H_i),
\]

put

\[
g=(S_1,S_2),\qquad \alpha=S_1/g,\qquad \beta=S_2/g,
\qquad L=\operatorname{lcm}(S_1,S_2).
\]

Stage14-e1 proves the primitive minimal gluing is bijective:

\[
\boxed{e=L,\qquad x=\beta X_1,\qquad y=\alpha X_2.}
\]

With `t_i=X_i/S_i`,

\[
(e,x,y)=L(1,t_1,t_2),
\qquad
\boxed{D_{\mathbf R}=L\sqrt{1+t_1^2+t_2^2}.}
\]

Stage14-e3 adds the rational torus coordinate

\[
q_i=h_i+t_i>1,
\qquad
 t_i=\frac{q_i-q_i^{-1}}2,
\qquad
 h_i=\frac{q_i+q_i^{-1}}2.
\]

Thus the raw two-face ambient family is a positive ordered real chamber of the rational torus `(G_m)^2`.

## 14-e1 — definition, bijection, independent finite audit, literature seed

Status: [x] Complete.

Locked results:

```text
space-diagonal rationality removed
real D_R used as height only
edge-first = face-pair-first through B=2000
parameter-fiber multiplicity = 1
no asymptotic claim
```

Canonical result:

```text
stages/stage14/14-e1/result.md
```

## 14-e2 — finite ambient reconnaissance + literature refresh

Status: [x] Complete.

The finite census reaches `B=1,000,000`.

At that ceiling,

\[
(E_a,E_b,E_c)=(4{,}592{,}536,\ 5{,}816{,}786,\ 3{,}408{,}403),
\]

\[
E_2(10^6)=13{,}817{,}725.
\]

The raw ambient count is `13,818,382`; there are `219` primitive Euler-brick objects below the same real-height cutoff.

The finite normalization

\[
E_2(B)/(B(\log B)^3)
\]

looked unusually stable through `10^6`. e2 deliberately recorded this only as a candidate and made no theorem claim.

The OEIS A239618 primitive Euler-brick subpopulation was independently reproduced at strict max-edge cutoffs `10^3,10^4,10^5`.

Canonical artifacts:

```text
stages/stage14/14-e2/result.md
stages/stage14/14-e2/literature-refresh.md
stages/stage14/scripts/14-e2/ambient_reconnaissance.py
stages/stage14/data/14-e2/ambient_reconnaissance.json
```

## 14-e3 — total ambient growth via toric height

Status: [x] Complete.

For `q_i=[u_i:v_i]`, the map to projective shape coordinates `[1:t_1:t_2]` is represented by three bidegree `(2,2)` sections with four torus-fixed base points. Blowing up those corners gives

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad
L=2H_1+2H_2-\sum_{j=1}^4E_j=-K_Y.
\]

Since

\[
\rho(Y)=6,
\]

the toric anticanonical logarithmic exponent is five. Batyrev–Tschinkel and Huang then give the raw ambient order, while a fixed 5-adic nonsquare neighbourhood supplies an exactly-two lower bound. Thus

\[
\boxed{E_2(B)\asymp B(\log B)^5.}
\]

The e2 `B(log B)^3` candidate is rejected as the true asymptotic order and retained only as pre-asymptotic finite behaviour.

Canonical artifacts:

```text
stages/stage14/14-e3/result.md
stages/stage14/14-e3/literature-asymptotic-audit.md
stages/stage14/scripts/14-e3/toric_growth_audit.py
stages/stage14/data/14-e3/toric_growth_audit.json
```

Literature status:

```text
COMMON_SIDE_FIXED_LEG_FORMULAS=ADJACENT_RESULT_PLUS_REUSABLE_METHOD
TORIC_MANIN_HEIGHT_COUNT=REUSABLE_METHOD_THEOREM_INPUT
TORIC_ADELIC_EQUIDISTRIBUTION=REUSABLE_METHOD_THEOREM_INPUT
DIRECT_CUBOID_LANGUAGE_E3_THEOREM=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

## 14-e4 — directionwise ambient asymptotic

Status: [x] Complete.

Stage14-e4 fixes the actual Euclidean projective metric rather than merely a comparable anticanonical height. On the positive torus the archimedean Tamagawa density is, up to one common normalization factor,

\[
 d\tau_\infty
 \propto
 \frac{dq_1\,dq_2}
 {q_1q_2\sqrt{1+t_1^2+t_2^2}}.
\]

With `r_i=log q_i` and then `t_i=tan(theta_i)`, this becomes

\[
 d\tau_\infty
 \propto
 \frac{d\theta_1\,d\theta_2}
 {\sqrt{1-\sin^2\theta_1\sin^2\theta_2}},
\qquad
0<\theta_1<\theta_2<\frac\pi2.
\]

The shared-edge threshold `t=1` is `theta=pi/4`, so the three chamber masses are explicit integrals. Deterministic Gauss–Legendre quadrature gives

\[
M_a=0.7295086229844189\ldots,
\]

\[
M_b=0.6753521849589658\ldots,
\]

\[
M_c=0.3139356465617057\ldots,
\]

with

\[
M=1.7187964545050902\ldots.
\]

The normalized direction vector is therefore

\[
\boxed{
(p_a,p_b,p_c)
=
(0.4244299091217717\ldots,
0.3929215604260869\ldots,
0.1826485304521414\ldots).
}
\]

The third-face-square locus is the image of the generically degree-two cover

\[
w^2=t_1^2+t_2^2.
\]

This is a Type-II thin set. Browning–Loughran's thin-set theorem, together with Huang's equidistribution, gives zero leading density for that locus. Hence the raw and exactly-two populations have the same chamber main terms.

There exists one positive common global arithmetic factor `Lambda_E` such that

\[
\boxed{
E_q(B)\sim\Lambda_E M_q B(\log B)^5,
\qquad q\in\{a,b,c\}.
}
\]

and

\[
\boxed{
E_2(B)\sim\Lambda_E M B(\log B)^5.
}
\]

The common constant `Lambda_E` is not evaluated as an explicit Euler product in e4; it cancels from the direction ratios.

Canonical artifacts:

```text
stages/stage14/14-e4/result.md
stages/stage14/14-e4/literature-directional-audit.md
stages/stage14/scripts/14-e4/directional_tamagawa_audit.py
stages/stage14/data/14-e4/directional_tamagawa_audit.json
```

Literature status:

```text
TORIC_ADELIC_EQUIDISTRIBUTION=REUSABLE_METHOD_THEOREM_INPUT
THIN_SET_ZERO_DENSITY=REUSABLE_METHOD_THEOREM_INPUT
ONE_CIRCLE_ANGULAR_DISTRIBUTION=ADJACENT_RESULT
COMMON_SIDE_FIXED_LEG_DISTRIBUTION=ADJACENT_RESULT
DIRECT_STAGE14_E4_DIRECTIONAL_THEOREM=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

## 14-e5 — space-diagonal filter comparison

Status: [>] Next.

This is the bridge back to the main Stage14 problem. Compare

\[
N_2(B)\subset E_2(B)
\]

and directionwise

\[
N_a^{(2)}(B)\subset E_a(B),\qquad
N_b^{(2)}(B)\subset E_b(B),\qquad
N_c^{(2)}(B)\subset E_c(B).
\]

Targets:

- quantify the thinning caused specifically by
  \[
  e^2+x^2+y^2=\square;
  \]
- compare the main-track scale against the now-proved ambient scale `B(log B)^5`;
- compare any proved/conditional main-track direction vector with the ambient vector
  `(0.4244299091,0.3929215604,0.1826485305)`;
- determine whether the integer-space-diagonal filter is asymptotically direction-neutral or direction-biased;
- keep a strict boundary between finite diagnostics, conditional consequences, and proved main-track theorems;
- refresh perfect-cuboid/Euler-brick obstruction and elliptic-fibration literature before interpreting the filter.

## Scope boundary

Stage14-e makes no perfect-cuboid existence/nonexistence claim and does not infer the main Stage14 growth order from the ambient family. The e4 ambient directional theorem concerns only the control population with the space-diagonal rationality/integrality condition removed. No novelty claim is made solely from literature-search absence.

```text
STAGE14_E_TRACK=DEFINED
STAGE14_E1=COMPLETE_DEFINITION_BIJECTION_AND_FINITE_AUDIT
STAGE14_E2=COMPLETE_FINITE_AMBIENT_RECONNAISSANCE
STAGE14_E3=COMPLETE_TOTAL_GROWTH_ORDER
STAGE14_E4=COMPLETE_DIRECTIONAL_ASYMPTOTIC
MAX_E_RECON_B=1000000
INTEGER_SPACE_DIAGONAL_CONDITION=REMOVED_FROM_E_TRACK
REAL_SPACE_DIAGONAL_USED_AS_HEIGHT_ONLY=true
MAIN_STAGE14_NUMBERING_UNCHANGED=true
LITERATURE_COLLISION_AUDIT_REQUIRED=true
NOVELTY_BY_ABSENCE_FORBIDDEN=true
TORIC_MODEL=P1xP1_BLOWUP_AT_FOUR_TORUS_FIXED_CORNERS
ANTICANONICAL_HEIGHT_IDENTIFICATION=true
PICARD_RANK=6
TORIC_LOG_POWER=5
TRUE_TOTAL_GROWTH_ORDER=THETA_B_LOG5
E2_B_LOG3_FINITE_CANDIDATE=REJECTED_AS_ASYMPTOTIC_ORDER
EXACTLY_TWO_THIRD_FACE_SQUARE_LOCUS=THIN_TYPE_II
EXACTLY_TWO_FULL_MAIN_TERM_EXISTENCE_PROVED=true
DIRECTIONAL_ASYMPTOTIC_PROVED=true
PA=0.4244299091218
PB=0.3929215604261
PC=0.1826485304521
GLOBAL_ARITHMETIC_CONSTANT_LAMBDA_E_EVALUATED=false
NEXT_E_TASK=Stage14-e5 space-diagonal filter comparison
```
