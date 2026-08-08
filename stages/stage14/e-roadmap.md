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

### Toric compactification

For `q_i=[u_i:v_i]`, the map to projective shape coordinates `[1:t_1:t_2]` is represented by

\[
\begin{aligned}
s_0&=4u_1v_1u_2v_2,\\
s_1&=2(u_1^2-v_1^2)u_2v_2,\\
s_2&=2(u_2^2-v_2^2)u_1v_1.
\end{aligned}
\]

These are bidegree `(2,2)` sections on `P^1 x P^1`. Their base locus consists of the four torus-fixed corners. Blow up those four simple base points:

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1).
\]

The resolved line bundle is

\[
L=2H_1+2H_2-\sum_{j=1}^4E_j=-K_Y.
\]

Since

\[
\rho(Y)=2+4=6,
\]

the toric anticanonical Manin exponent is

\[
\rho(Y)-1=5.
\]

Batyrev–Tschinkel supplies the anticanonical toric height count; the physical Euclidean height is comparable to a fixed anticanonical height because the resolved morphism pulls back `O_P2(1)` to `-K_Y` and

\[
\max(e,x,y)\le D_{\mathbf R}\le\sqrt3\max(e,x,y).
\]

Hence the raw ambient family has order

\[
E_{\rm raw}(B)\asymp B(\log B)^5.
\]

### Exactly-two lower bound

No density-zero claim for Euler bricks is assumed. Instead impose the fixed 5-adic open condition

\[
q_1\equiv2,\qquad q_2\equiv3\pmod5.
\]

Then

\[
t_1\equiv2,\qquad t_2\equiv3\pmod5,
\]

and

\[
t_1^2+t_2^2\equiv3\pmod5,
\]

which is a nonsquare unit. Thus the third face cannot be rational/integral square.

Huang's adelic equidistribution theorem gives a positive-order family in the product of this 5-adic neighbourhood with any nonempty real open subset of the positive ordered chamber. Therefore

\[
E_2(B)\gg B(\log B)^5.
\]

Together with `E_2<=E_raw`,

\[
\boxed{E_2(B)\asymp B(\log B)^5.}
\]

The e2 `B(log B)^3` candidate is therefore rejected as the true asymptotic order and retained only as pre-asymptotic finite behaviour.

No exact leading constant is claimed in e3.

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

Status: [>] Next.

Purpose:

- split the positive ordered real torus chamber into the three shared-edge regions
  `e<x<y`, `x<e<y`, `x<y<e`;
- use the toric height/Tamagawa measure rather than finite fitting;
- determine whether each direction has order `B(log B)^5`;
- derive the raw directional leading proportions if the archimedean measure is explicit enough;
- separately determine what can be proved for the exactly-two directions under local blockers;
- do not assume that the 5-adic blocker used for the total lower bound is direction-neutral until checked.

Literature gate: search chamber/shape distributions and explicit Peyre/Tamagawa measures for toric surfaces with this anticanonical model.

## 14-e5 — space-diagonal filter comparison

Status: pending 14-e4 and sufficient progress in main Stage14.

Compare

\[
N_2(B)\subset E_2(B)
\]

and directionwise `N_a^(2),N_b^(2),N_c^(2)` against `E_a,E_b,E_c` to isolate the thinning and directional bias caused specifically by

\[
e^2+x^2+y^2=\square.
\]

Before interpretation, refresh the current perfect-cuboid/Euler-brick obstruction and elliptic-fibration literature.

## Scope boundary

Stage14-e makes no perfect-cuboid existence/nonexistence claim and does not infer the main Stage14 growth order from the ambient family. Stage14-e3 proves a matching upper/lower total order only; it does not yet freeze an exactly-two leading constant or limiting directional vector. No novelty claim is made solely from literature-search absence.

```text
STAGE14_E_TRACK=DEFINED
STAGE14_E1=COMPLETE_DEFINITION_BIJECTION_AND_FINITE_AUDIT
STAGE14_E2=COMPLETE_FINITE_AMBIENT_RECONNAISSANCE
STAGE14_E3=COMPLETE_TOTAL_GROWTH_ORDER
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
B_LOG3_FINITE_CANDIDATE_PRIORITY=REJECTED_AS_ASYMPTOTIC_ORDER
EXACT_LEADING_CONSTANT_PROVED=false
DIRECTIONAL_ASYMPTOTIC_PROVED=false
NEXT_E_TASK=Stage14-e4 directionwise ambient asymptotic via real-chamber toric measures
```
