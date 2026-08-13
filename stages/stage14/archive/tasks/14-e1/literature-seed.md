# Stage14-e1 — literature collision seed

> STATUS: `INITIAL_LITERATURE_SEED_CREATED`
>
> ROLE: discovery map, not a novelty certificate and not a substitute for proof
>
> SEARCH PRINCIPLE: re-run and expand before every e-substage theorem or novelty claim

## 1. What Stage14-e is trying to distinguish

The e-track counts primitive positive integer triples `(e,x,y)` with `x<y` such that

\[
e^2+x^2=u^2,\qquad e^2+y^2=v^2,
\]

under the real Euclidean height

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}\le B,
\]

without requiring `D_R` to be rational or integral. The exactly-two ambient subpopulation also requires

\[
x^2+y^2\ne\square.
\]

The intended later questions are total and directionwise counting asymptotics for this ambient family, followed by a comparison with the main Stage14 integer-space-diagonal filter.

A paper is an **exact collision** only if it treats essentially this same ambient family and proves the same kind of height-counting/directional statement. Work on perfect cuboids, Euler bricks, nearly-perfect cuboids, parametrizations or elliptic fibrations is highly relevant but is not automatically an exact collision.

## 2. Verified initial source seed

### L1 — John Leech, 1977

**John Leech, “The Rational Cuboid Revisited,” The American Mathematical Monthly 84(7) (1977), 518–533. DOI: 10.1080/00029890.1977.11994405.**

Classification for Stage14-e: `ADJACENT_RESULT / REUSABLE_METHOD`.

Why it matters:

- classical rational-cuboid structure and parametrization context;
- useful for checking whether a gluing or rational normalization is genuinely new;
- predates the e-track height-counting formulation.

Current collision status:

```text
NO_EXACT_HEIGHT_COUNT_COLLISION_IDENTIFIED_IN_INITIAL_SEARCH
```

### L2 — Ronald van Luijk, 2000

**Ronald van Luijk, “On Perfect Cuboids,” Doctoraalscriptie, Universiteit Utrecht, June 2000.**

Classification: `ADJACENT_RESULT / REUSABLE_METHOD`.

Why it matters:

- treats perfect-cuboid equations through algebraic surfaces;
- contains an explicit literature survey and a geometric reformulation;
- relevant if the e-track later moves from elementary Euclid parameters to arithmetic geometry.

Current collision status:

```text
NO_EXACT_E_TRACK_COUNTING_THEOREM_IDENTIFIED_IN_INITIAL_SEARCH
```

### L3 — Ramsden–Sharipov, 2012

**John Ramsden and Ruslan Sharipov, “On two algebraic parametrizations for rational solutions of the cuboid equations,” arXiv:1208.2587 (2012).**

Classification: `ADJACENT_RESULT / REUSABLE_METHOD`.

Why it matters:

- algebraic parametrizations of rational perfect-cuboid equations;
- warning against treating a rational parametrization as new merely because it is rediscovered in different coordinates;
- relevant to later comparisons between Euclid-pair and algebraic-surface coordinates.

### L4 — Mamuka Meskhishvili, 2015

**Mamuka Meskhishvili, “Parametric Solutions for a Nearly-Perfect Cuboid,” arXiv:1502.02375 (2015).**

Classification: `ADJACENT_RESULT`.

Why it matters:

- nearly-perfect cuboids place an irrationality defect in one diagonal;
- close to the philosophy of removing one cuboid condition while retaining the others;
- different object from Stage14-e because the e-track removes the integer-space-diagonal condition before imposing a third-face structure.

### L5 — de Grey–Gibbs–Helm, 2024

**Aubrey de Grey, Philip Gibbs and Louie Helm, “Novel required properties of, and efficient algorithms to seek, perfect cuboids,” arXiv:2401.06784 (2024).**

Classification: `ADJACENT_RESULT / REUSABLE_METHOD`.

Why it matters:

- recent perfect-cuboid search algorithms and new two-parameter edge-cuboid families;
- important for collision checks against new computational search claims;
- demonstrates that the computational/parametric literature is still active.

### L6 — René Peschmann, 2026a

**René Peschmann, “Quartic reductions and elliptic obstructions for perfect Euler bricks,” arXiv:2604.09328 (2026).**

Classification: `ADJACENT_RESULT / REUSABLE_METHOD`.

Why it matters:

- reduces a perfect-Euler-brick condition to genus-3 curves with elliptic quotients;
- directly relevant if a later e-track square-filter comparison produces quartic/genus-one fibers;
- not an exact collision with the e-track ambient count because the e-track has removed the space-diagonal square condition.

### L7 — René Peschmann, 2026b

**René Peschmann, “A torsion-intersection proof of perfect-cuboid nonexistence on 1,072 explicit master-tuple fibers,” arXiv:2604.28072 (2026).**

Classification: `ADJACENT_RESULT / REUSABLE_METHOD`.

Why it matters:

- gives a structural classification statement for primitive Euler bricks in its master-tuple framework;
- uses elliptic quotients and exact rank/torsion certification on explicit fibers;
- any future Stage14-e claim about “all Euler-brick-type parametrizations” must be checked against this work rather than asserted from finite experiments.

### L8 — René Peschmann, 2026c

**René Peschmann, “Exponent-one blockers and a Mordell-Weil construction of Euler bricks,” arXiv:2605.00573 (2026).**

Classification: `ADJACENT_RESULT / REUSABLE_METHOD`.

Why it matters:

- works with coprime Pythagorean pairs and a genus-one quartic / elliptic fibration;
- produces large numbers of Euler-brick master hits using Mordell–Weil points;
- this is especially close to any future attempt to reinterpret Stage14 through elliptic fibers;
- therefore Stage14-e should not spend months “discovering” an elliptic-fibration viewpoint without first checking this paper carefully.

## 3. Initial collision assessment

The verified seed shows substantial prior work on:

```text
rational cuboid parametrizations
Euler-brick parametrizations
nearly-perfect cuboids
algebraic surfaces
quartic/genus-one reductions
elliptic fibrations and Mordell-Weil generation
large computational searches
```

The initial search has **not yet identified** a source proving the specific Stage14-e target:

```text
primitive shared-edge two-Pythagorean-face ambient objects
+ no rational/integer condition on the real space diagonal
+ Euclidean height D_R <= B
+ total asymptotic count
+ directionwise a/b/c chamber asymptotics
```

The correct repository wording is therefore

```text
NO_EXACT_COLLISION_FOUND_IN_CURRENT_SEARCH
```

and **not**

```text
NOVEL_THEOREM_CONFIRMED
```

## 4. Mandatory search questions for later e-substages

Before Stage14-e2:

- search Euler-brick/rational-cuboid tables and computational enumerations for an equivalent height ordering;
- check whether known tables can independently validate the e-track ambient census.

Before Stage14-e3:

- search for asymptotic counting of Pythagorean pairs sharing a leg;
- search for lcm-weighted counts of primitive Euclid parameters;
- search for rational-point counting on the corresponding open surface under anticanonical/Euclidean/comparable heights;
- check Manin-type counting literature if the compactified variety suggests it.

Before Stage14-e4:

- search for shape/chamber distributions in Pythagorean and rational-cuboid families;
- check whether ordering chambers have already been integrated in a height-counting theorem.

Before Stage14-e5:

- refresh all 2024–present perfect-cuboid / Euler-brick obstruction, elliptic and computational literature;
- identify whether any published/preprint result already quantifies the space-diagonal square thinning.

## 5. Citation discipline

For every imported paper result, Stage14-e must record:

```text
exact source identity
exact theorem/lemma/equation used
version checked (publisher / arXiv version)
hypotheses of the source
mapping from source variables to Stage14-e variables
whether the source proves the claim or only motivates it
```

When arXiv and published numbering differ, record both or cite the version actually checked. No theorem is to be cited only from memory.

```text
STAGE14_E_LITERATURE_POLICY=MANDATORY
INITIAL_VERIFIED_SOURCE_SEED_COUNT=8
NOVELTY_BY_SEARCH_ABSENCE=false
EXACT_COLLISION_FOUND=false
NEXT_LITERATURE_ACTION=EXPAND_BY_E2_AND_BEFORE_ANY_ASYMPTOTIC_CLAIM
```
