# Stage15 roadmap — space-diagonal integrality as a comparison experiment

## Purpose

Stage15 changes viewpoint rather than adding another integrality condition.

Stage12–14 worked inside the population with integral space diagonal and then asked how one-face and two-face integrality behave. Stage15 asks the reverse comparative question:

> What changes when the space-diagonal integrality condition is removed from the two-face population, while every other convention is held as close as possible?

The aim is to separate two possible sources of the Stage14 difficulty:

1. **two-face coupling itself is already sparse/difficult**, or
2. **the additional condition that the space diagonal is integral creates the exceptional sparsity and analytic obstruction**.

Stage15 is therefore a controlled A/B comparison, not a new attempt to prove or disprove the existence of a perfect cuboid.

---

## 0. Comparison contract

### 0.1 Common geometric height

A direct comparison cannot use `d<=B` on only one side, because the no-space-diagonal family need not have integral `d`.

Use the common real geometric height

\[
R(a,b,c)=\sqrt{a^2+b^2+c^2}.
\]

For the integral-space-diagonal family, `R=d`, so this agrees exactly with the Stage14 cutoff.

All primary Stage15 counts use

\[
R(a,b,c)\le B.
\]

This is the required comparison cutoff. Edge cutoffs such as `c<=B` may be used only as secondary diagnostics and must never be mixed with the primary asymptotic comparison.

### 0.2 Common physical convention

Unless explicitly studying a secondary variant, retain

\[
0<a<b<c,\qquad \gcd(a,b,c)=1.
\]

Let

\[
I_{ab}=1_{a^2+b^2\text{ square}},\quad
I_{ac}=1_{a^2+c^2\text{ square}},\quad
I_{bc}=1_{b^2+c^2\text{ square}}.
\]

Define the ambient two-face population without imposing space-diagonal integrality:

\[
\mathcal B_2(B)=
\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ I_{ab}+I_{ac}+I_{bc}=2\}.
\]

Define

\[
M_2(B)=\#\mathcal B_2(B).
\]

Define the Stage14-comparable subpopulation

\[
\mathcal A_2(B)=
\{(a,b,c)\in\mathcal B_2(B):R(a,b,c)\in\mathbf Z\},
\]

and

\[
N_2(B)=\#\mathcal A_2(B).
\]

Thus

\[
\mathcal A_2(B)\subseteq\mathcal B_2(B)
\]

exactly, under one common cutoff and one common primitive/canonical convention.

For triple-face objects define `M_3(B)` and `N_3(B)` separately. Do not silently fold Euler bricks or perfect-cuboid candidates into the exactly-two count.

### 0.3 Primary comparison observables

The primary objects are:

- `M_2(B)` — exactly-two face integrality without the space-diagonal condition;
- `N_2(B)` — exactly-two face integrality with the space-diagonal condition;
- the survival ratio `N_2(B)/M_2(B)` when meaningful;
- directional counts according to the shared edge of the two integral faces;
- the distribution of `R^2=a^2+b^2+c^2` inside `B_2`, especially its distance from a square;
- primitive density and local congruence/squareclass statistics before and after imposing `R in Z`.

No asymptotic or survival law is assumed in advance.

---

## 1. Stage15-0 — freeze the interface and audit inherited machinery

### Goal

Prove that the A/B definitions above are exact and identify which Stage12–14 tools can be reused without changing measure, cutoff, or quantifier order.

### Tasks

1. Reconstruct the primitive/canonical conventions from merged main.
2. Verify that `R<=B` agrees exactly with Stage14 `d<=B` on `A_2`.
3. Prove the set-theoretic inclusion `A_2(B) subset B_2(B)` with no orientation or multiplicity ambiguity.
4. Separate exactly-two from exactly-three populations from the start.
5. Produce a reuse matrix for Stage12–14 tools:
   - exact reusable as-is;
   - reusable after a proved adapter;
   - diagnostic only;
   - forbidden cross-promotion.
6. Do not import claims from a review bundle merely because the bundle states them; use merged theorem sources or independently reprove the required statement.

### Exit gate

`STAGE15_COMPARISON_CONTRACT_PROVED=true`

No numerical or analytic comparison should be promoted before this gate closes.

---

## 2. Stage15-1 — exact paired enumerator

### Goal

Build one exact enumerator that produces both `B_2` and `A_2` under the same conventions and cutoff.

### Requirements

For each object retain:

- `(a,b,c)`;
- `R^2=a^2+b^2+c^2`;
- whether `R` is integral;
- which two face diagonals are integral;
- the third-face defect;
- primitive/canonical status;
- Pythagorean parameters for the two integral faces;
- all deduplication provenance needed to audit multiplicity.

Cross-check against existing Stage14 finite counts after restricting to `R in Z`.

### Minimum validation

- brute-force comparison at small bounds;
- independent generation by two shared-edge Pythagorean faces;
- exact equality of the `A_2` projection with the existing Stage14 definition on overlapping tested ranges;
- duplicate and permutation audit.

### Exit gate

`PAIRED_ENUMERATOR_VALIDATED=true`

---

## 3. Stage15-2 — solve the easier ambient family first

### Goal

Understand `M_2(B)` before comparing it to `N_2(B)`.

This stage should begin with the simplest questions and stop escalating only when necessary.

### Questions, in order

1. Is infinitude of `B_2` immediate from an explicit parametrized family?
2. Is a complete parametrization by two primitive/scaled Pythagorean triples sharing one edge available with finite multiplicity?
3. What is the correct growth scale of `M_2(B)`?
4. Can matching upper/lower bounds be proved?
5. Can an asymptotic formula be proved?
6. Can directional asymptotics be proved?

### Important policy

Do not assume that because existence or infinitude is easy, the counting law is easy. Record separately:

- existence;
- infinitude;
- upper bound;
- lower bound;
- matching order;
- asymptotic formula.

### Literature gate

Perform a focused Euler-brick / shared-leg Pythagorean / simultaneous sum-of-two-squares counting review before claiming novelty.

### Exit possibilities

- `M2_ASYMPTOTIC_PROVED`
- `M2_MATCHING_ORDER_PROVED`
- `M2_ONLY_PARTIAL_BOUNDS`
- `M2_EXTERNAL_GATE`

---

## 4. Stage15-3 — numerical A/B comparison under one denominator

### Goal

Measure what the condition `R in Z` actually removes.

### Required plots/tables

For matched `R<=B` cutoffs:

1. cumulative `M_2(B)` and `N_2(B)`;
2. log-log local slopes;
3. `N_2(B)/M_2(B)` where counts are sufficiently large;
4. directional vectors for both A and B;
5. primitive versus nonprimitive diagnostic only if needed to explain an anomaly;
6. distribution of
   \[
   \Delta_R=\operatorname{nearestSquare}(R^2)-R^2;
   \]
7. normalized defect, for example
   \[
   \Delta_R/(2R),
   \]
   with sign retained;
8. congruence, squareclass, and prime-factor statistics of `R^2` and `|Delta_R|`;
9. the same statistics conditioned on direction/shared edge.

### Statistical discipline

Finite data may suggest mechanisms but must not be labeled asymptotic without proof. Predeclare any stability criterion before using it to support a conjecture.

### Main empirical question

Does imposing `R in Z` look like:

- an approximately independent thin square condition;
- a direction-dependent sieve;
- a strong arithmetic correlation with the two shared Pythagorean structures;
- a rare-event phenomenon concentrated in special parameter strata?

---

## 5. Stage15-4 — derive the exact extra condition imposed by an integral space diagonal

### Goal

Start from a clean parametrization of `B_2` and express `R in Z` as one exact arithmetic condition on those parameters.

This is the conceptual heart of the comparison.

### Required outputs

1. A minimal parametrization of the ambient exactly-two family.
2. An exact formula for `R^2` in those parameters.
3. A classification of the additional square condition into the simplest available form:
   - quadratic form;
   - quartic form;
   - conic/elliptic curve fiber;
   - squareclass condition;
   - Gaussian norm condition;
   - divisor/CRT condition;
   - or another exact normal form.
4. Exact multiplicity/fiber control for the map back to physical cuboids.
5. A proof that all primitive/canonical/exactly-two filters are preserved or are monotone restrictions.

### Comparison principle

The Stage15 question is not merely “count A again.” It is:

> In the B-family coordinates, what new arithmetic obstruction appears exactly when `R` is required to be integral?

---

## 6. Stage15-5 — quantitative survival law

### Goal

Compare the proved scales of `N_2(B)` and `M_2(B)`.

If an asymptotic or matching lower bound for `M_2(B)` is available, combine it with the certified Stage14 upper bound only after its hypotheses and cutoff are matched exactly.

### Possible outcomes

If, for example, `M_2(B)` has a proved scale much larger than `B^(1/2+o(1))`, then the integral-space-diagonal condition has a proved polynomial thinning effect.

Do not assume any particular exponent in advance.

### Desired statements, strongest first

1. asymptotic survival law;
2. matching-order survival law;
3. fixed-power upper bound for survival probability;
4. qualitative density-zero result;
5. only finite-data comparison.

### Forbidden inference

A small observed ratio does not prove density zero. A Stage14 upper bound alone does not determine survival unless a sufficiently strong lower description of `M_2(B)` is proved.

---

## 7. Stage15-6 — mechanism audit: why does `R in Z` matter?

### Goal

Identify which structural features change between B and A.

Audit at least:

- parameter dimension/fiber dimension;
- squareclass freedom;
- Gaussian-factor allocation;
- local congruence restrictions;
- gcd/primitive interactions;
- moving moduli/conductors;
- divisor support;
- elliptic/genus-one fibers;
- direction/shared-edge dependence;
- exceptional or saturated packets.

### Stage14 weapon test

For every obstruction discovered, first ask whether an existing Stage14 tool applies **with the same measure and quantifier order**.

Classify each tool as:

- `DIRECT_REUSE`
- `REUSE_AFTER_EXACT_ADAPTER`
- `SAME_KERNEL_DIFFERENT_MEASURE`
- `TOO_STRONG_FOR_STAGE15`
- `NOT_APPLICABLE`

The point is to reuse Stage14's mathematics without reusing its historical complexity unnecessarily.

---

## 8. Stage15-7 — causal comparison verdict

### Goal

Answer the original Stage15 question in the strongest form justified by proof.

Possible verdicts include:

### Verdict A — space-diagonal integrality is the main thinning mechanism

Requires a theorem showing that the ambient two-face family is substantially larger/easier and that `R in Z` introduces the decisive loss.

### Verdict B — two-face coupling is already the hard part

Requires evidence/theorems showing that the ambient family already exhibits comparable sparsity or the same structural obstruction before `R in Z` is imposed.

### Verdict C — both mechanisms matter

The ambient family is nontrivial, but the space-diagonal condition creates an additional quantitatively identifiable loss.

### Verdict D — comparison unresolved

Use this if only partial bounds are known. Do not force a causal narrative from finite data.

---

## 9. Stage15-8 — final extraction and publication bundle

When the mathematical comparison is stable:

1. build a logical-order self-contained review, not a chronological research diary;
2. separate proved theorem, numerical evidence, and conjectures;
3. record exact Stage12–14 dependencies;
4. include a standalone A/B definition and common-cutoff proof;
5. identify reusable lemmas abstractable beyond perfect cuboids;
6. perform novelty/literature audit;
7. perform independent adversarial review;
8. freeze only after all MAJOR review findings are either repaired or explicitly converted into theorem assumptions/gates.

---

## 10. Recommended execution order

The intended route is deliberately narrow at the start:

```text
15-0 comparison contract
  -> 15-1 paired exact enumerator
  -> 15-2 ambient B-family mathematics
  -> 15-3 matched numerical comparison
  -> 15-4 exact extra square condition
  -> 15-5 quantitative survival law
  -> 15-6 mechanism audit
  -> 15-7 causal verdict
  -> 15-8 final bundle
```

Do not create parallel MAIN/S/T/X/q/H machinery by default.

Parallel routes should be created only when a mathematically distinct obstruction is stable enough to justify them.

---

## 11. Initial Stage15 questions

The first work session should answer only these questions:

1. Is the common cutoff `R<=B` fully compatible with the existing Stage14 cutoff on the integral-space-diagonal subfamily?
2. Can the exactly-two no-space-diagonal family be parametrized with auditable finite multiplicity?
3. Is its infinitude immediate?
4. What is already known in the literature about counting this shared-edge two-Pythagorean-face family?
5. What exact equation does `R in Z` impose in the cleanest ambient parametrization?

These five answers determine whether Stage15 remains short or becomes a deeper comparison project.

---

## 12. Non-claims at roadmap creation

At Stage15 roadmap creation time, none of the following is assumed:

```text
M2_ASYMPTOTIC_PROVED=false
M2_MATCHING_LOWER_BOUND_PROVED=false
SURVIVAL_RATIO_ASYMPTOTIC_PROVED=false
SPACE_DIAGONAL_CAUSAL_THINNING_PROVED=false
STAGE14_SQRT_EXPONENT_SHARP=false
PERFECT_CUBOID_EXISTENCE_OR_NONEXISTENCE_PROVED=false
```

The roadmap is designed to discover which of these questions is actually tractable before escalating the research machinery.
