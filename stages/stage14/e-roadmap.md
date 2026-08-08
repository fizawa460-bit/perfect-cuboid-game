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

Absence in a search is never a novelty certificate. Classical rational-cuboid work, Euler-brick tables, nearly-perfect cuboids, arithmetic surfaces, elliptic fibrations, modern search algorithms, and current preprints all belong in the search scope.

Canonical literature records:

```text
stages/stage14/14-e1/literature-seed.md
stages/stage14/14-e2/literature-refresh.md
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

Thus the e-track is the full primitive two-face gluing family before the main-track filter

\[
1+t_1^2+t_2^2\in(\mathbf Q^\times)^2
\]

is imposed.

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

The finite census was extended from the e1 ceiling `B=2000` to `B=1,000,000`.

At the new ceiling,

\[
\boxed{
(E_a,E_b,E_c)=(4{,}592{,}536,\ 5{,}816{,}786,\ 3{,}408{,}403)
}
\]

and

\[
\boxed{E_2(10^6)=13{,}817{,}725.}
\]

The raw two-face ambient count is `13,818,382`. Exactly `219` primitive Euler-brick objects occur below the same real-height cutoff, giving `657=3*219` third-face-square incidences.

As an independent external subpopulation cross-check, the e2 enumerator reproduces OEIS A239618 under its own strict max-edge cutoff:

```text
max edge < 10^3 -> 5 primitive Euler bricks
max edge < 10^4 -> 19
max edge < 10^5 -> 65
```

Finite growth diagnostics show

\[
\frac{E_2(B)}{B(\log B)^3}
\]

staying near `0.0052` from `B=2,000` through `B=1,000,000`. Therefore `B(log B)^3` is a high-priority e3 candidate scale, but **no asymptotic theorem is claimed**.

At `B=10^6`, the finite direction vector is approximately

```text
(0.3323655667, 0.4209655352, 0.2466688981)
```

with `b` still largest. No limiting directional vector is claimed.

The refreshed literature audit found extensive adjacent work on Euler bricks and rational/perfect cuboids—including Rathbun's tables, de Grey–Gibbs–Helm 2024, and Peschmann's 2026 quartic/elliptic Master-Hit program—but no direct theorem in the current search for the primitive two-face ambient population counted by `D_R` and split by shared-edge chamber.

Correct literature status:

```text
DIRECT_REAL_HEIGHT_TWO_FACE_AMBIENT_COUNT=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
DIRECTIONWISE_AMBIENT_ASYMPTOTIC=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

Canonical e2 artifacts:

```text
stages/stage14/14-e2/result.md
stages/stage14/14-e2/literature-refresh.md
stages/stage14/scripts/14-e2/ambient_reconnaissance.py
stages/stage14/data/14-e2/ambient_reconnaissance.json
```

## 14-e3 — total ambient growth

Status: [>] Next.

Literature gate first. Search specifically for:

- counts of simultaneous Pythagorean pairs sharing one leg;
- rational Pythagorean slopes with shared-denominator/lcm height;
- lcm-weighted Euclid-parameter sums;
- height zeta functions and rational-point counts on the associated arithmetic variety;
- toric/Manin-type mechanisms that could produce `B(log B)^k`.

Then determine the true order of `E_2(B)`. The finite `B(log B)^3` stability is a candidate to explain or reject, not an input theorem.

## 14-e4 — directionwise ambient asymptotic

Status: pending 14-e3.

Determine whether `E_a,E_b,E_c` share a common arithmetic factor times chamber integrals, and derive any limiting direction vector from proof rather than finite fitting.

Literature gate: search chamber/shape distributions and geometric-height measures in Pythagorean/cuboid families.

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

Stage14-e makes no perfect-cuboid existence/nonexistence claim, does not infer the main Stage14 growth order from the ambient family, does not promote finite ratios to asymptotic laws, and does not declare novelty solely because no collision was found in the current search.

```text
STAGE14_E_TRACK=DEFINED
STAGE14_E1=COMPLETE_DEFINITION_BIJECTION_AND_FINITE_AUDIT
STAGE14_E2=COMPLETE_FINITE_AMBIENT_RECONNAISSANCE
MAX_E_RECON_B=1000000
INTEGER_SPACE_DIAGONAL_CONDITION=REMOVED_FROM_E_TRACK
REAL_SPACE_DIAGONAL_USED_AS_HEIGHT_ONLY=true
MAIN_STAGE14_NUMBERING_UNCHANGED=true
LITERATURE_COLLISION_AUDIT_REQUIRED=true
NOVELTY_BY_ABSENCE_FORBIDDEN=true
B_LOG3_FINITE_CANDIDATE_PRIORITY=HIGH
ASYMPTOTIC_CLAIM_MADE=false
NEXT_E_TASK=Stage14-e3 total ambient growth with literature-first asymptotic collision audit
```
