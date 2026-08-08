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
stages/stage14/14-e5/literature-filter-audit.md
```

## Locked ambient object

Let `e,x,y` be positive integers with `x<y` and

\[
\gcd(e,x,y)=1.
\]

Require

\[
e^2+x^2=\square,
\qquad e^2+y^2=\square.
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

The main Stage14 counts form the subpopulation obtained by imposing in addition

\[
e^2+x^2+y^2=\square.
\]

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

Stage14-e3 adds rational torus coordinates

\[
q_i=h_i+t_i>1,
\qquad
 t_i=\frac{q_i-q_i^{-1}}2,
\qquad
 h_i=\frac{q_i+q_i^{-1}}2.
\]

Thus the raw two-face ambient family is a positive ordered real chamber of `(G_m)^2`.

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

The finite census reaches `B=1,000,000`. At that ceiling,

\[
(E_a,E_b,E_c)=(4{,}592{,}536,\ 5{,}816{,}786,\ 3{,}408{,}403),
\]

\[
E_2(10^6)=13{,}817{,}725.
\]

The raw ambient count is `13,818,382`; there are `219` primitive Euler-brick objects below the same real-height cutoff.

The finite normalization `E_2(B)/(B(log B)^3)` looked unusually stable through `10^6`; e2 deliberately recorded it only as a candidate.

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

For `q_i=[u_i:v_i]`, the map to `[1:t_1:t_2]` is represented by three bidegree `(2,2)` sections with four torus-fixed base points. Blowing up those corners gives

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad
L=2H_1+2H_2-\sum_{j=1}^4E_j=-K_Y.
\]

Since `rho(Y)=6`, the toric anticanonical logarithmic exponent is five. Batyrev–Tschinkel and Huang give the ambient order, and the exactly-two population has matching order:

\[
\boxed{E_2(B)\asymp B(\log B)^5.}
\]

The e2 `B(log B)^3` finite candidate is rejected as the asymptotic order.

Canonical artifacts:

```text
stages/stage14/14-e3/result.md
stages/stage14/14-e3/literature-asymptotic-audit.md
stages/stage14/scripts/14-e3/toric_growth_audit.py
stages/stage14/data/14-e3/toric_growth_audit.json
```

## 14-e4 — directionwise ambient asymptotic

Status: [x] Complete.

For the actual Euclidean projective metric, the real Tamagawa density becomes

\[
 d\tau_\infty
 \propto
 \frac{d\theta_1\,d\theta_2}
 {\sqrt{1-\sin^2\theta_1\sin^2\theta_2}},
\qquad
0<\theta_1<\theta_2<\frac\pi2.
\]

The threshold `t=1` is `theta=pi/4`. The chamber masses are

\[
M_a=0.7295086229844189\ldots,
\quad
M_b=0.6753521849589658\ldots,
\quad
M_c=0.3139356465617057\ldots,
\]

with

\[
M=1.7187964545050902\ldots.
\]

The normalized ambient direction vector is

\[
\boxed{
(p_a,p_b,p_c)=
(0.4244299091217717\ldots,
0.3929215604260869\ldots,
0.1826485304521414\ldots).
}
\]

The third-face-square locus `w^2=t_1^2+t_2^2` is Type-II thin, so removing it does not change the chamber main terms. There exists one common positive arithmetic factor `Lambda_E` such that

\[
\boxed{E_q(B)\sim\Lambda_E M_qB(\log B)^5.}
\]

Canonical artifacts:

```text
stages/stage14/14-e4/result.md
stages/stage14/14-e4/literature-directional-audit.md
stages/stage14/scripts/14-e4/directional_tamagawa_audit.py
stages/stage14/data/14-e4/directional_tamagawa_audit.json
```

Historical e4 handoff lock retained for compatibility:

```text
HISTORICAL_NEXT_E_TASK=Stage14-e5 space-diagonal filter comparison
```

## 14-e5 — space-diagonal filter comparison

Status: [x] Complete.

This stage bridges the solved ambient control population back to main Stage14.

The main counts satisfy

\[
N_q^{(2)}(B)\subset E_q(B),
\qquad q=a,b,c,
\]

and the frozen R03 pair-overlap theorem gives separately

\[
N_q^{(2)}(B)=o(B(\log B)^3).
\]

Together with e4,

\[
E_q(B)\sim\Lambda_EM_qB(\log B)^5,
\qquad M_q>0,
\]

this yields the directionwise filter survival theorem

\[
\boxed{
\frac{N_q^{(2)}(B)}{E_q(B)}=o((\log B)^{-2}),
\qquad q=a,b,c.
}
\]

Likewise

\[
\boxed{
\frac{N_2(B)}{E_2(B)}=o((\log B)^{-2}).
}
\]

Thus the integer-space-diagonal square condition removes more than two full logarithmic powers relative to the ambient main term, globally and in every chamber. This still does not identify the true main Stage14 power of `B`.

Define

\[
S_q(B)=\frac{N_q^{(2)}(B)}{E_q(B)},
\qquad
S(B)=\frac{N_2(B)}{E_2(B)}.
\]

Then the exact bias decomposition is

\[
\boxed{
\frac{N_q^{(2)}(B)}{N_2(B)}
=
\frac{E_q(B)}{E_2(B)}
\frac{S_q(B)}{S(B)}.
}
\]

Hence asymptotic direction-neutrality is equivalent to

\[
S_q(B)/S(B)\to1
\]

for all three directions. No such neutrality theorem is currently proved.

Main Stage14-4af explains the unresolved numerator structurally: after the actual Pythagorean base change the elliptic K3 has generic Mordell-Weil rank zero, all rational torsion is nonphysical, and every physical main hit requires a positive-rank specialization carrying a sufficiently small non-torsion point. The true main growth order therefore remains a quantitative rank-jump/small-point problem rather than a consequence of the ambient toric law.

At the same finite cutoff `B=10,000`, the main vector `(9,11,5)` sits inside the ambient vector `(12464,18198,11004)`, giving total survival about `0.0006000096`; this is diagnostic only. At `B=2,000,000`, the main finite direction vector `(142,134,80)/356` is also retained only as finite evidence.

Canonical artifacts:

```text
stages/stage14/14-e5/result.md
stages/stage14/14-e5/literature-filter-audit.md
stages/stage14/scripts/14-e5/space_filter_comparison_audit.py
stages/stage14/data/14-e5/space_filter_comparison_audit.json
```

## e-track completion boundary

The planned Stage14-e control experiment is complete. It has determined the natural two-face ambient population, its true total growth order, its directionwise main terms, and a rigorous comparison with the main space-diagonal-square subpopulation.

It does **not** close main Stage14. In particular it does not prove:

- the true asymptotic order of `N_2(B)`;
- a main Stage14 leading constant;
- a main direction limit;
- direction-neutrality of the space-square filter;
- a uniform triple/perfect-cuboid bound;
- perfect-cuboid existence or nonexistence.

Future e-track work is triggered only by a new quantitative theorem on the main Stage14 numerator that can be inserted into the e5 bias comparison.

## Scope boundary

Stage14-e makes no perfect-cuboid existence/nonexistence claim and does not infer the main Stage14 growth order from the ambient family. No novelty claim is made solely from literature-search absence.

```text
STAGE14_E_TRACK=DEFINED
STAGE14_E1=COMPLETE_DEFINITION_BIJECTION_AND_FINITE_AUDIT
STAGE14_E2=COMPLETE_FINITE_AMBIENT_RECONNAISSANCE
STAGE14_E3=COMPLETE_TOTAL_GROWTH_ORDER
STAGE14_E4=COMPLETE_DIRECTIONAL_ASYMPTOTIC
STAGE14_E5=COMPLETE_SPACE_FILTER_COMPARISON
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
TOTAL_SPACE_FILTER_SURVIVAL=o(LOG^-2)
DIRECTIONWISE_SPACE_FILTER_SURVIVAL=o(LOG^-2)
DIRECTION_NEUTRALITY_PROVED=false
MAIN_TRUE_GROWTH_ORDER_PROVED=false
MAIN_DIRECTION_LIMIT_PROVED=false
E_TRACK_CONTROL_EXPERIMENT=COMPLETE
NEXT_E_ACTION=WAIT_FOR_MAIN_STAGE14_QUANTITATIVE_GROWTH_OR_DIRECTION_RESULT
```
