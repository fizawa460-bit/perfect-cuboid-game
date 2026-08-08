# Stage14-e roadmap — two-face ambient control population

## Purpose

Stage14-e is an independent **front-side control track** for the exactly-two integral-face problem.

The main Stage14 track keeps the integer-space-diagonal condition. Stage14-e deliberately removes it. The point is not to solve an easier copy of the same problem, but to measure what the integer-space-diagonal square condition itself removes from the natural two-face ambient family.

The e-track must not replace or renumber the existing Stage14-4 / Stage14-5 roadmap.

## Literature-first rule

Stage14-e sits close to the classical rational-cuboid / Euler-brick / nearly-perfect-cuboid literature, and recent work increasingly uses the same Euclid-pair, quartic, elliptic-curve and arithmetic-surface language. Therefore **every e-substage must perform a literature collision audit before promoting a structural statement, parametrization, asymptotic mechanism or novelty claim**.

For each important claim, classify the nearest literature as one of:

```text
EXACT_COLLISION      = essentially the same object and statement already proved
ADJACENT_RESULT      = nearby cuboid family or nearby condition, but not the same count
REUSABLE_METHOD      = method/parametrization can be imported after hypotheses are checked
NO_COLLISION_FOUND   = no direct prior result found in the searched literature
```

Rules:

1. search both classical and recent sources, not only perfect-cuboid papers;
2. include Euler bricks, rational cuboids, nearly-perfect/edge/face cuboids, parametrizations, arithmetic surfaces, elliptic fibrations, search algorithms and counting results;
3. prefer original papers/preprints and publisher records over secondary summaries;
4. record exact bibliographic identity and which equation/object overlaps Stage14-e;
5. do not treat a paper's computation as proof of a Stage14-e claim unless the theorem actually covers the same hypotheses;
6. do not claim novelty from absence in a quick search; write `NO_COLLISION_FOUND_IN_CURRENT_SEARCH` until a serious survey has been made;
7. when a useful parametrization is already known, reuse/cite it and spend effort on the new height/counting/directional question rather than rediscovering it;
8. refresh the literature audit at e2, e3, e4 and e5 because this area is active.

Initial literature seed is maintained in

```text
stages/stage14/14-e1/literature-seed.md
```

The initial search already includes Leech's rational-cuboid work, van Luijk's algebraic-surface treatment, nearly-perfect-cuboid parametrizations, rational cuboid parametrizations, recent search/parametric work, and 2026 elliptic/genus-one Euler-brick work. At this checkpoint no direct source has yet been identified that proves the Stage14-e target itself: the primitive shared-edge two-face ambient population counted by real Euclidean height with directionwise asymptotics. This is a **search status, not a novelty theorem**.

## Locked ambient object

Let `e,x,y` be positive integer edges with `x<y` and

\[
\gcd(e,x,y)=1.
\]

Require two Pythagorean faces sharing `e`:

\[
e^2+x^2=u^2,
\qquad
e^2+y^2=v^2.
\]

Define the ordinary real Euclidean space diagonal only as a height

\[
D_{\mathbf R}:=\sqrt{e^2+x^2+y^2}.
\]

The cutoff is

\[
D_{\mathbf R}\le B.
\]

**No condition whatsoever is imposed that `D_R` be an integer or rational.**

The raw ambient population allows the third face to be either square or nonsquare. The exactly-two ambient population additionally imposes

\[
x^2+y^2\ne\square.
\]

The three directions are the position of the shared edge:

```text
a-ambient: e < x < y
b-ambient: x < e < y
c-ambient: x < y < e
```

Write the corresponding exactly-two ambient counts as

\[
E_a(B),\qquad E_b(B),\qquad E_c(B),
\]

and

\[
E_2(B)=E_a(B)+E_b(B)+E_c(B).
\]

These are **not** the main Stage14 counts `N_a^(2),N_b^(2),N_c^(2),N_2`; the latter also require an integer space diagonal.

## Structural link to the main Stage14 track

For two oriented primitive face data

\[
F_1=(S_1,X_1,H_1),
\qquad
F_2=(S_2,X_2,H_2),
\]

put

\[
g=(S_1,S_2),\qquad
\alpha=S_1/g,\qquad
\beta=S_2/g.
\]

The Stage14-4ab minimal gluing, which does not use the integer-space-diagonal condition, gives

\[
\boxed{
 e=\operatorname{lcm}(S_1,S_2)=g\alpha\beta,
 \quad x=\beta X_1,
 \quad y=\alpha X_2.
}
\]

With

\[
t_1=X_1/S_1,\qquad t_2=X_2/S_2,
\qquad L=\operatorname{lcm}(S_1,S_2),
\]

this is exactly

\[
(e,x,y)=L(1,t_1,t_2)
\]

and the e-track height is

\[
\boxed{D_{\mathbf R}=L\sqrt{1+t_1^2+t_2^2}.}
\]

Thus Stage14-e studies the full primitive two-face gluing family before the main-track filter

\[
1+t_1^2+t_2^2\in(\mathbf Q^\times)^2
\]

is imposed.

## 14-e1 — definition, bijection, independent finite audit, literature seed

Status: [>] Active.

Targets:

1. lock the raw and exactly-two ambient counting conventions;
2. prove that the Stage14-4ab two-face gluing is still a bijection after the space-diagonal square condition is removed;
3. prove that the real-height formula above is exact and direction-neutral;
4. implement two materially different finite enumerators:
   - edge-first ambient enumeration;
   - oriented-face-pair ambient enumeration;
5. require exact agreement of directional counts and third-face-square counts at several small cutoffs;
6. create the initial literature seed and classify direct/adjacent methodological collisions;
7. record finite data only as a diagnostic, not as an asymptotic theorem.

## 14-e2 — finite ambient reconnaissance

Status: pending 14-e1.

Literature gate: refresh the search for tables, large enumerations and computational Euler-brick / rational-cuboid work before claiming a new census.

Targets:

- extend `E_a,E_b,E_c,E_2` to substantially larger `B`;
- record raw ambient versus exactly-two ambient populations;
- measure the third-face-square thinning separately;
- compare coarse growth candidates without promoting a finite fit to a theorem;
- compare the ambient direction vector with the main Stage14 finite direction vector.

## 14-e3 — total ambient growth

Status: pending 14-e2.

Literature gate: search explicitly for height-counting/asymptotic results on rational cuboids, Pythagorean-pair gluings, lcm-weighted Euclid parameters and related arithmetic varieties before asserting a new growth law.

Targets:

- determine the true order of `E_2(B)`;
- exploit the exact lcm / Pythagorean-slope parametrization without any space-diagonal square condition;
- isolate the contribution of the shared-leg representation multiplicity
  \[
  a(S)=2^{\omega(S)-1}
  \]
  on its valid support;
- derive a rigorous asymptotic or matching upper/lower order before introducing any comparison with the main Stage14 square filter.

## 14-e4 — directionwise ambient asymptotic

Status: pending 14-e3.

Literature gate: search for chamber/shape distributions, geometric height measures and directional statistics in cuboid/Pythagorean families.

Targets:

- determine whether
  \[
  E_a(B),E_b(B),E_c(B)
  \]
  have a common arithmetic factor times three chamber integrals;
- derive any limiting ambient direction vector from proof, not from finite ratios;
- identify whether the chamber geometry alone creates directional bias before the integer-space-diagonal condition is imposed.

## 14-e5 — space-diagonal filter comparison

Status: pending 14-e4 and sufficient progress in main Stage14.

Literature gate: refresh recent perfect-cuboid/Euler-brick obstruction and elliptic-fibration work before interpreting the square-filter thinning.

This is the bridge back to the main problem.

Compare

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
- study the ratio `N_2(B)/E_2(B)` only after both numerator and denominator have rigorous scales;
- determine whether the integer-space-diagonal filter is asymptotically direction-neutral or direction-biased;
- separate geometry/chamber bias from arithmetic square-filter bias.

## Scope boundary

Stage14-e does not assume a perfect cuboid exists or does not exist. It does not infer the main Stage14 growth order from the ambient family. It does not reuse a finite directional fit as an asymptotic law. It does not declare novelty solely because the current literature search found no exact collision.

The e-track is intentionally a control population with one major condition removed.

```text
STAGE14_E_TRACK=DEFINED
INTEGER_SPACE_DIAGONAL_CONDITION=REMOVED_FROM_E_TRACK
REAL_SPACE_DIAGONAL_USED_AS_HEIGHT_ONLY=true
MAIN_STAGE14_NUMBERING_UNCHANGED=true
LITERATURE_COLLISION_AUDIT_REQUIRED=true
NOVELTY_BY_ABSENCE_FORBIDDEN=true
NEXT_E_TASK=Stage14-e1 definition bijection independent finite audit and literature seed
```
