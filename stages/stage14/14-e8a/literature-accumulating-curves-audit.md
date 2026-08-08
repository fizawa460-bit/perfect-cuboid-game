# Stage14-e8a — literature audit for accumulating curves

## Search question

Stage14-e8a does not ask for another generator of Euler bricks in general. It asks whether the finite `R_EB(B) ~ sqrt(B)` signal seen through `B=10^6` can be attributed to a known low-degree rational curve, or to an accumulating-curve mechanism already treated in the K3 literature.

The collision labels remain

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

## 1. Saunderson / Himane

Djamel Himane, *Primitive Euler brick generator*, arXiv:2405.13061 (2024).

Himane records the classical Saunderson family. For a primitive Pythagorean triple

\[
u^2+v^2=w^2,
\]

the edges

\[
A=u(4v^2-w^2),\quad
B=v(4u^2-w^2),\quad
C=4uvw
\]

form an Euler brick, with one face diagonal equal to `w^3`.

Classification:

```text
ADJACENT_RESULT — EXPLICIT_RATIONAL_CURVE_FAMILY
```

Stage14-e8a reuses the formula but asks a different question: its counting exponent under the repository's physical Euclidean height.

## 2. Spohn — derived cuboid

W. G. Spohn, *On the Derived Cuboid*, Canadian Mathematical Bulletin 17 (1974), 575–577, DOI `10.4153/CMB-1974-102-6`.

Spohn studies the cuboid derived from an Eulerian family. The elementary projective operation is

\[
(a,b,c)\longmapsto (bc,ac,ab)
\]

followed by primitive normalization.

Classification:

```text
ADJACENT_RESULT — CLASSICAL_DERIVED_FAMILY
```

For a primitive Saunderson brick, e8a computes the normalized derived formula and its physical-height degree explicitly. This is used only to decide whether the derived family can explain a square-root counting layer.

## 3. McKinnon — accumulating curves on K3 surfaces

David McKinnon, *Counting Rational Points on K3 Surfaces*, Journal of Number Theory 84 (2000), 49–62; arXiv:math/9903013.

McKinnon studies bounded-height rational points on hyperelliptic/Kummer K3 surfaces and constructs finite unions of curves that form an accumulating layer in the relevant examples.

Classification:

```text
REUSABLE_METHOD — ACCUMULATING_CURVE_FRAMEWORK
```

This is a conceptual warning and a method source: on a K3 surface, a small finite collection of low-height-degree rational curves can dominate the visible counting function. It does **not** identify the Euler-brick K3 or its physical Euclidean polarization with one of McKinnon's explicit Kummer examples.

A later related paper is David McKinnon, *A Reduction of the Batyrev-Manin Conjecture for Kummer Surfaces*, Canadian Mathematical Bulletin 47 (2004), 398–406.

## 4. Peschmann — global Euler-brick parametrization context

René Peschmann, *A torsion-intersection proof of perfect-cuboid nonexistence on 1,072 explicit master-tuple fibers*, arXiv:2604.28072 (2026).

The paper states a structural classification in which primitive Euler bricks arise from a standard master-tuple parametrization up to scale. This is useful context for avoiding a false novelty claim about parametrizing Euler bricks.

Classification:

```text
ADJACENT_RESULT — GLOBAL_PARAMETRIZATION_CONTEXT
```

Stage14-e8a is not a competing all-bricks parametrization. It is a height-degree/accumulation audit for specific rational curves on the K3 model.

## 5. Collision result for the square-root source

The current search found classical Euler-brick rational families and general K3 accumulating-curve theory, but no primary source that identifies a `Q`-rational degree-four curve for the repository's Euler-brick K3 and physical Euclidean height, nor a source proving that such curves do not exist.

```text
DIRECT_STAGE14_E8A_DEGREE4_CURVE=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

In particular, absence of a search hit is not used as a classification theorem. The repository keeps

```text
DEGREE4_CURVE_CLASSIFICATION_COMPLETE=false
```

unless a full Neron-Severi/lattice computation closes that question.
