# Stage14-e5 — literature-first space-diagonal filter audit

## Scope

Stage14-e5 compares two populations on the same primitive shared-edge two-face geometry.

The front-side ambient control population requires

\[
e^2+x^2=\square,\qquad e^2+y^2=\square,
\qquad \gcd(e,x,y)=1,
\qquad x<y,
\]

under the real Euclidean height

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}\le B,
\]

but imposes no rationality or integrality condition on `D_R`. Stage14-e4 proves its exactly-two chamber asymptotics.

The main Stage14 population adds the integer-space-diagonal condition

\[
e^2+x^2+y^2=d^2,
\qquad d\in\mathbf Z.
\]

The literature question is not merely whether perfect cuboids or Euler bricks have been studied. It is whether an existing result directly quantifies the survival probability and directional bias of this specific space-diagonal-square filter inside the Stage14-e anticanonical ambient population.

Classification vocabulary remains

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

## 1. Peschmann 2026 — space-diagonal blockers and elliptic fibers

René Peschmann,
*Exponent-one blockers and a Mordell-Weil construction of Euler bricks*,
arXiv:2605.00573, 2026.

Classification:

```text
ADJACENT_RESULT + REUSABLE_METHOD
```

This is the closest current computational/arithmetic literature found for the **space-diagonal square obstruction**. It studies body/Euler cuboids parameterized by two Pythagorean pairs, identifies a genus-one quartic / elliptic fibration, and records an exponent-one prime blocker phenomenon on a very large database of Master-Hits.

Its object is nevertheless different from Stage14-e5 in two important ways:

1. it starts on the all-three-face Euler-brick locus rather than the Stage14-e exactly-two ambient family;
2. it does not state a bounded-height asymptotic survival probability relative to the two-face anticanonical ambient population, nor the shared-edge directional survival ratios considered here.

Therefore the blocker phenomenon is important interpretation and a future computational cross-check, but it is not an exact collision with the e5 comparison theorem.

## 2. Peschmann 2026 — quartic / elliptic obstruction framework

René Peschmann,
*Quartic reductions and elliptic obstructions for perfect Euler bricks*,
arXiv:2604.09328, 2026.

Classification:

```text
ADJACENT_RESULT + REUSABLE_METHOD
```

This work reduces perfect-Euler-brick conditions to quartic and elliptic obstructions. It reinforces the point already found independently in main Stage14-4ad through 4af: imposing an additional square condition naturally produces genus-one/elliptic arithmetic rather than a direction-neutral random thinning rule.

It does not supply the Stage14-e5 height-normalized comparison or an asymptotic direction vector.

## 3. Silverman specialization and current rank-specialization literature

The main Stage14 space-square filter is birational, after fixing the first Pythagorean face, to

\[
E_t:Y^2=X(X-1)(X+t^2).
\]

After the actual Pythagorean base change, Stage14-4af obtains an elliptic K3 surface of generic Mordell-Weil rank zero. Physical hits therefore occur only on positive-rank specializations and must additionally contain a sufficiently small non-torsion point.

Silverman's specialization theorem is foundational for comparing generic and specialized ranks, but generic rank zero gives no quantitative count of positive-rank fibers with a small first point.

Recent adjacent literature includes:

- Mentzelos Melistas, *Low rank specialisations of elliptic surfaces*, Bulletin of the Australian Mathematical Society (2025), preprint arXiv:2408.02419;
- Hector Pasten and Cecília Salgado, *Non-thin rank jumps for double elliptic K3 surfaces*, manuscripta mathematica 175 (2024), 771–781;
- Alice Garbagnati and Cecília Salgado, *Rank jumps and multisections of elliptic fibrations on K3 surfaces*, Forum of Mathematics, Sigma 14 (2026), e1.

Classification:

```text
ADJACENT_RESULT + REUSABLE_CONTEXT
```

These results show that rank-jump phenomena on elliptic surfaces and K3 surfaces are subtle and can be arithmetically large. None of the searched results gives the specific quantitative weighted count required by main Stage14:

```text
Pythagorean base
+ gcd/lcm coupling
+ physical q-height cutoff
+ positive-rank specialization
+ small non-torsion point
+ R03 local restrictions.
```

Thus e5 must not promote the finite `sqrt(B)` clue to a theorem.

## 4. Browning–Loughran / Huang / Batyrev–Tschinkel remain ambient inputs

Stage14-e4 already uses the following theorem-level inputs on the **ambient** side:

- Batyrev–Tschinkel: anticanonical height asymptotics on smooth projective toric varieties;
- Huang: adelic equidistribution on split toric varieties;
- Browning–Loughran: thin subsets have zero leading density under the relevant equidistribution hypotheses.

Classification:

```text
REUSABLE_METHOD — AMBIENT_THEOREM_INPUT
```

These theorems determine the denominator population `E_q(B)`. They do not determine the numerator `N_q^(2)(B)` after imposing the space-diagonal square condition.

## 5. Direct collision decision

The current search found no paper stating the precise comparison

\[
\frac{N_q^{(2)}(B)}{E_q(B)}
\]

for the Stage14 shared-edge chambers under the same Euclidean height, nor a theorem identifying the main-track direction vector from the ambient vector.

Current status:

```text
SPACE_DIAGONAL_BLOCKER_LITERATURE=ADJACENT_RESULT_PLUS_REUSABLE_METHOD
ELLIPTIC_K3_RANK_JUMP_LITERATURE=ADJACENT_RESULT_PLUS_REUSABLE_CONTEXT
AMBIENT_TORIC_HEIGHT_THEOREMS=REUSABLE_METHOD_THEOREM_INPUT
DIRECT_STAGE14_E5_FILTER_SURVIVAL_THEOREM=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
DIRECT_STAGE14_E5_DIRECTION_BIAS_THEOREM=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

The e5 logarithmic survival bound itself is a repository-local consequence of two already-frozen inputs: the e4 ambient main term and the Stage13 R03 pair-overlap little-o theorem. It should not be advertised as a new general thin-set or elliptic-surface theorem.
