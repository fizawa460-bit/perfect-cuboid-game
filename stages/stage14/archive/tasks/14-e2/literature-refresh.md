# Stage14-e2 — refreshed literature collision audit

## Scope of this refresh

Stage14-e2 counts the primitive shared-edge two-face ambient family

\[
e^2+x^2=\square,\qquad e^2+y^2=\square,
\qquad \gcd(e,x,y)=1,
\]

with `x<y` and real Euclidean height

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}\le B,
\]

without requiring `D_R` to be rational or integral. The exactly-two ambient count excludes `x^2+y^2=square`.

The e2 literature question is therefore narrower than “does the perfect cuboid exist?” and different from the classical Euler-brick census: has this primitive **two-face ambient** family already been counted by real Euclidean height, especially directionwise according to the position of the shared edge?

## Classification vocabulary

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
```

Absence in this search is not a novelty theorem.

## 1. John Leech, The Rational Cuboid Revisited (1977)

Bibliography: John Leech, *The Rational Cuboid Revisited*, American Mathematical Monthly 84(7), 518–533 (1977), DOI 10.1080/00029890.1977.11994405.

Classification:

```text
ADJACENT_RESULT + REUSABLE_METHOD
```

Leech is foundational for rational-cuboid parametrization and structural reductions. It is relevant background for gluing Pythagorean faces, but the present search did not find the Stage14-e real-height primitive two-face directional counting problem stated or solved there.

## 2. Ronald van Luijk, On Perfect Cuboids (2000)

Bibliography: Ronald van Luijk, *On Perfect Cuboids*, Utrecht University thesis, June 2000.

Classification:

```text
ADJACENT_RESULT + REUSABLE_METHOD
```

This treats the perfect-cuboid equations through algebraic surfaces. It is relevant if the e-track later changes viewpoint to arithmetic geometry, but its object retains the full rational/perfect-cuboid constraints rather than the Stage14-e two-face ambient population.

## 3. Ramsden–Sharipov rational cuboid parametrizations (2012)

Bibliography: John Ramsden and Ruslan Sharipov, *On two algebraic parametrizations for rational solutions of the cuboid equations*, arXiv:1208.2587.

Classification:

```text
ADJACENT_RESULT + REUSABLE_METHOD
```

The paper parametrizes rational solutions associated with the perfect-cuboid equations. It does not provide the Stage14-e height count found in the present search.

## 4. Meskhishvili nearly-perfect cuboids (2012, 2015)

Bibliography:

- Mamuka Meskhishvili, *Perfect Cuboid and Congruent Number Equation Solutions*, arXiv:1211.6548.
- Mamuka Meskhishvili, *Parametric Solutions for a Nearly-Perfect Cuboid*, arXiv:1502.02375.

Classification:

```text
ADJACENT_RESULT
```

These are especially close to the **main Stage14 track**: the nearly-perfect cuboid has one irrational face diagonal while the body diagonal remains rational. Stage14-e intentionally removes the body-diagonal rationality condition, so the object is larger and the height problem is different.

## 5. Rathbun integer-cuboid tables and Euler-brick census

Bibliography:

- Randall L. Rathbun, *The Rational Cuboid Table of Maurice Kraitchik*, arXiv:math/0111229.
- Randall L. Rathbun, *The Integer Cuboid Table*, arXiv:1705.05929.
- OEIS A239618, primitive Euler-brick counts under the strict box cutoff `a<b<c<10^n`.

Classification:

```text
ADJACENT_RESULT + REUSABLE_COMPUTATIONAL_CHECK
```

Rathbun's work gives large exhaustive tables for body/Euler, edge and face cuboids under edge-based search conventions. OEIS A239618 records primitive Euler bricks, i.e. the Stage14-e subpopulation for which the **third** face diagonal is also integral, but uses a maximum-edge box rather than the real Euclidean height `D_R`.

This gives a useful external audit. The e2 code independently reproduces

```text
max edge < 10^3  -> 5 primitive Euler bricks
max edge < 10^4  -> 19
max edge < 10^5  -> 65
```

matching A239618. This validates the third-face-square subpopulation machinery but is not an exact collision with `E_2(B)`.

## 6. de Grey–Gibbs–Helm (2024)

Bibliography: Aubrey de Grey, Philip Gibbs, Louie Helm, *Novel required properties of, and efficient algorithms to seek, perfect cuboids*, arXiv:2401.06784.

Classification:

```text
ADJACENT_RESULT + REUSABLE_METHOD
```

This paper develops efficient perfect-cuboid searches and new two-parameter edge-cuboid families. It is highly relevant for algorithmic cross-checks and parametrization awareness, but the present search found no real-height asymptotic/directional count of the Stage14-e ambient family.

## 7. Himane primitive Euler-brick generator (2024)

Bibliography: Djamel Himane, *Primitive Euler brick generator*, arXiv:2405.13061.

Classification:

```text
ADJACENT_RESULT
```

The target is the all-three-face Euler-brick subpopulation and parametric generation, not the two-face ambient population.

## 8. Peschmann 2026 trilogy

Bibliography:

- René Peschmann, *Quartic reductions and elliptic obstructions for perfect Euler bricks*, arXiv:2604.09328.
- René Peschmann, *A torsion-intersection proof of perfect-cuboid nonexistence on 1,072 explicit master-tuple fibers*, arXiv:2604.28072.
- René Peschmann, *Exponent-one blockers and a Mordell-Weil construction of Euler bricks*, arXiv:2605.00573.

Classification:

```text
ADJACENT_RESULT + REUSABLE_METHOD
```

These papers are now mandatory reading for any e-track move into quartics, elliptic fibrations, Master-Hit coordinates or Euler-brick generation. In particular arXiv:2605.00573 works with body/Euler cuboids parametrized by two coprime Pythagorean pairs and reports an extended database of 1,284,670 Master-Hits. arXiv:2604.28072 states a structural classification of primitive Euler bricks in the standard parameterization.

They concern the all-three-face Euler-brick locus and the subsequent perfect-space-diagonal obstruction. Stage14-e2 counts the much larger pre-third-face ambient family and asks for real-height and chamber-direction statistics. No theorem in the searched material was found that supplies that count.

## Current collision decision

At this checkpoint:

```text
DIRECT_REAL_HEIGHT_TWO_FACE_AMBIENT_COUNT=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
DIRECTIONWISE_Ea_Eb_Ec_ASYMPTOTIC=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
EULER_BRICK_SUBPOPULATION_TABLES=ADJACENT_RESULT
PYTHAGOREAN_PAIR_PARAMETRIZATIONS=REUSABLE_METHOD
ELLIPTIC_QUARTIC_EULER_BRICK_METHODS=REUSABLE_METHOD_FOR_LATER_STAGES
NOVELTY_BY_SEARCH_ABSENCE=false
```

The most important correction to a naive novelty narrative is that the **Euler-brick subpopulation is very heavily studied and tabulated**. Stage14-e should not spend effort rediscovering its basic generators or tables. The potentially distinct contribution is the ambient two-face population under `D_R` height, its total growth, and its shared-edge chamber distribution.

## Gate for Stage14-e3

Before promoting any `B(log B)^k` law in e3, search specifically for:

- height zeta functions or Manin-type counts on varieties defined by two Pythagorean conditions;
- asymptotics for pairs of rational Pythagorean slopes with lcm/shared-denominator height;
- counts of simultaneous Pythagorean pairs sharing one leg;
- lcm-weighted Euclid-parameter sums;
- rational-point counts on related toric/arithmetic surfaces.

No asymptotic novelty claim is authorized by e2 alone.
