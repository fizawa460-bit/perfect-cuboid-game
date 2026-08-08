# Stage14-e8 — literature-first audit for quantitative Euler-brick counting

## Scope

Stage14-e8 isolates the third-face-square subpopulation inside the solved Stage14-e ambient model.  Write

\[
R_{\rm EB}(B)
\]

for the number of primitive unordered Euler bricks with real Euclidean space height

\[
D_{\mathbf R}=\sqrt{a^2+b^2+c^2}\le B.
\]

Equivalently, the raw Stage14-e incidence ledger contains exactly `3 R_EB(B)` third-face-square incidences, one for each choice of shared edge.

The literature gate is the same as in e1--e7:

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

The target here is a theorem-level quantitative upper envelope under the **same Euclidean height**, not another parametrization or a box/minimum-edge search table.

## 1. Rathbun — exhaustive integer-cuboid tables

Randall L. Rathbun, *The Integer Cuboid Table*, arXiv:1705.05929 (2017).

Classification:

```text
ADJACENT_RESULT — LARGE_COMPUTATIONAL_CENSUS
```

Rathbun classifies body/Euler, edge and face cuboids and gives an exhaustive search procedure based on the Pythagorean group.  The paper reports 167,043 integer cuboids over a very large smallest-edge range.

This is valuable external finite geography, but its ordering/cutoff is not the Stage14-e physical Euclidean height and it does not state an asymptotic or upper bound for `R_EB(B)`.

Related earlier source:

Randall L. Rathbun, *The Rational Cuboid Table of Maurice Kraitchik*, arXiv:math/0111229 (2001).

Again this is a search/table result under a different ordering convention.

## 2. Himane — primitive Euler-brick generator

Djamel Himane, *Primitive Euler brick generator*, arXiv:2405.13061 (2024).

Classification:

```text
ADJACENT_RESULT — PARAMETRIC_GENERATION
```

The paper discusses the classical Saunderson construction and searches for further generating formulas.  It is directly about primitive Euler bricks, but it is not a bounded-height counting theorem and does not provide the Stage14-e Euclidean-height asymptotic.

## 3. Peschmann 2026 — structural classification and Master-Hits

René Peschmann, *A torsion-intersection proof of perfect-cuboid nonexistence on 1,072 explicit master-tuple fibers*, arXiv:2604.28072 (2026).

Classification:

```text
REUSABLE_METHOD — COMPLETE_STRUCTURAL_CLASSIFICATION
```

Theorem 2.4 of that preprint states that every primitive Euler brick, after choosing its unique odd edge and ordering the other two edges, arises from a unique coprime opposite-parity master tuple `(a,b,m,n)`.  Thus current Euler-brick work should not pretend that the two-Pythagorean-pair master parametrization is new.

The same paper is aimed at perfect-cuboid obstructions on explicit fibers, not at counting all primitive Euler bricks by `D_R`.

René Peschmann, *Exponent-one blockers and a Mordell-Weil construction of Euler bricks*, arXiv:2605.00573 (2026).

Classification:

```text
ADJACENT_RESULT — LARGE_MASTER_HIT_GENERATION
```

This paper uses genus-one quartic/elliptic fibers to generate more than one million Master-Hits and studies the extra space-diagonal square obstruction.  It is highly relevant to generation and fiber arithmetic, but it does not state a Euclidean-height counting asymptotic for all primitive Euler bricks.

## 4. Euler-brick surface as a K3 surface

The Euler-brick equations admit the projective model

\[
U^2=E^2+X^2,
\qquad
V^2=E^2+Y^2,
\qquad
Z^2=X^2+Y^2
\]

in `P^5`.  This is an intersection of three quadrics.  On the positive physical locus it is smooth, and the double-cover description used in Stage14-e4 has branch class `-2K_Y`; after normalization/minimal resolution the compactification is a K3 surface.

General K3 point counting is delicate.  David McKinnon, *Counting Rational Points on K3 Surfaces*, arXiv:math/9903013, gives detailed counting for Kummer surfaces arising from products of elliptic curves and exhibits accumulating curves.  Stage14-e8 does **not** identify the present physical Euler-brick K3 with the precise product-Kummer hypotheses of that theorem, so McKinnon's numerical exponents are not imported.

Classification:

```text
REUSABLE_CONTEXT — K3_HEIGHT_COUNTING_WARNING
```

This geometry explains why the qualitative thin-set theorem from e4 does not automatically upgrade to an elementary uniform power saving.

## 5. What the current search did not find

The current primary-source search did not find a theorem of the form

\[
R_{\rm EB}(B)\ll B^{1-\delta}
\]

for any fixed `delta>0`, nor a theorem

\[
R_{\rm EB}(B)\ll B(\log B)^A
\qquad(A<5)
\]

under the Stage14-e physical Euclidean height.

Stage14-e8 therefore derives its own unconditional divisor-envelope bound rather than promoting a search heuristic or a fit.

```text
DIRECT_STAGE14_E8_EUCLIDEAN_COUNT=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
FIXED_POWER_SAVING_FOUND_IN_LITERATURE=false
LOG_POWER_SAVING_FOUND_IN_LITERATURE=false
NOVELTY_BY_SEARCH_ABSENCE=false
```

This is a search boundary, not a novelty certificate.
