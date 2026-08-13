# Stage14-t1 — literature boundary for the moving triple family

## Scope

Stage14-t1 asks only what is currently justified for the triple correction `T(B)`. It does not claim a new quantitative theorem.

The fixed first-face triple locus is the connected `(Z/2)^2` cover

\[
W^2=q^4+2Aq^2+1,\qquad R^2=q^4+2Cq^2+1,
\]

with

\[
A=\frac{1-t^2}{1+t^2},\qquad C=\frac2{t^2}-1.
\]

For genuine physical Pythagorean `t`, both quartics are smooth and their branch sets are disjoint, so the fiber has genus `5`.

## 1. Faltings — fixed-fiber finiteness only

Faltings' theorem gives finiteness of rational points on each fixed smooth genus-5 fiber. This is exactly the qualitative statement already used by Stage14-4af.

Classification:

```text
REUSABLE_METHOD — FIBERWISE_FINITENESS_ONLY
```

It does not by itself supply a uniform bound as the Pythagorean base `t` moves, nor a usable dependence on the physical height `d<=B`.

## 2. Browning--Heath-Brown--Salberger — global determinant method

T. D. Browning, D. R. Heath-Brown and P. Salberger, *Counting rational points on algebraic varieties*, arXiv:math/0410117.

Their result gives height bounds uniform for projective geometrically integral varieties of fixed degree and fixed dimension. This is directly relevant as a possible quantitative tool once the Stage14 genus-5 fibers are placed in a fixed-degree projective model and the projective height is compared uniformly with the physical `(t,q)` height.

Classification:

```text
REUSABLE_METHOD — UNIFORM_FIXED_DEGREE_HEIGHT_COUNTING
```

Stage14-t1 does **not** invoke a numerical exponent from this paper yet. Before doing so, t2 must lock the actual projective embedding, degree, coefficient-height dependence, and the summation over the moving Pythagorean base.

## 3. Liu — explicit global determinant method

Chunhui Liu, *On the global determinant method*, arXiv:2101.07453.

This work develops Salberger's global determinant method explicitly and studies degree dependence for rational points of bounded height on plane curves.

Classification:

```text
REUSABLE_METHOD — EXPLICIT_DETERMINANT_METHOD_DEPENDENCE
```

It is a candidate for t2 after a low-degree plane/projective model and a uniform physical-height comparison are fixed.

## 4. Caporaso--Harris--Mazur uniformity boundary

The Caporaso--Harris--Mazur uniformity principle shows, conditional on Lang-type conjectures, that curves of fixed genus over a fixed number field would have a uniform bound on the number of rational points.

Classification:

```text
CONDITIONAL_CONTEXT — NOT_AN_UNCONDITIONAL_STAGE14_INPUT
```

This explains why a uniform genus-5 cardinality bound is a genuinely strong statement. Stage14-t does not assume Lang's conjecture or use conditional uniform boundedness.

## 5. Peschmann 2026 — direct perfect-cuboid adjacency

René Peschmann, *Quartic reductions and elliptic obstructions for perfect Euler bricks*, arXiv:2604.09328.

Peschmann reduces the perfect-cuboid problem to simultaneous quartic square conditions, obtains a one-parameter genus-3 hyperelliptic family with elliptic quotients, proves several torsion/descent obstructions, and explicitly discusses a remaining genus-5 covering obstruction. The paper does not prove perfect-cuboid nonexistence and does not provide the Stage14 bounded-height asymptotic for `T(B)`.

Classification:

```text
ADJACENT_RESULT — DIRECT_PERFECT_CUBOID_QUARTIC_AND_GENUS_COVER_GEOMETRY
```

The Stage14 fixed-base genus-5 fiber is therefore not treated as a novelty claim merely because its coordinates differ from Peschmann's reduction.

## 6. Exact theorem gap for t2

The current unconditional chain is

```text
fixed physical base t
-> smooth genus-5 curve
-> finitely many rational points.
```

What is missing is a **moving-base quantitative statement** compatible with

```text
base t = X1/S1 from primitive Pythagorean faces,
q=u/v,
v asymp sqrt(B*g/S1),
d<=B.
```

A result sufficient for the desired transfer would bound the total number of physical rational points after summing over all admissible base states by `o(sqrt(B))`. A stronger target is `B^(1/2-delta+o(1))` for some `delta>0`.

The determinant method is the first unconditional route to audit in t2, but no exponent is promoted until the embedding/height/base-sum bookkeeping is complete.

```text
DIRECT_STAGE14_T_BOUNDED_HEIGHT_TRIPLE_ASYMPTOTIC=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
UNCONDITIONAL_UNIFORM_GENUS5_CARDINALITY_IMPORTED=false
DETERMINANT_METHOD_NUMERICAL_EXPONENT_IMPORTED=false
T_O_SQRT_B_PROVED=false
NOVELTY_BY_SEARCH_ABSENCE=false
```
