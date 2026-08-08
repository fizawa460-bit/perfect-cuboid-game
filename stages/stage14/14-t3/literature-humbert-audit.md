# Stage14-t3 — literature audit for Humbert-Edge and elliptic-factor structure

## Auffarth--Lucchini Arteche--Rojas

Robert Auffarth, Giancarlo Lucchini Arteche, Anita M. Rojas, *A decomposition of the Jacobian of a Humbert-Edge curve*, arXiv:1905.12690.

Classification:

```text
DIRECT_REUSABLE_STRUCTURE — HUMBERT_EDGE_TYPE4_JACOBIAN_DECOMPOSITION
```

The paper defines a Humbert--Edge curve of type `n` as a smooth nondegenerate complete intersection of `n-1` diagonal quadrics in `P^n`, with natural sign group `(Z/2Z)^n`. It records the genus

\[
g_n=2^{n-2}(n-3)+1.
\]

Its refined decomposition theorem gives, for each `m`, exactly

\[
\binom{n+1}{2m+2}
\]

factors of dimension `m`. For `n=4`, the genus is `5`, the largest factor has dimension `1`, and there are

\[
\binom54=5
\]

elliptic factors. This is precisely the structure needed after the Stage14-t diagonal-quadric identification.

The theorem is not used to claim any rank bound: it changes the rank problem from one genus-5 Jacobian to five explicit elliptic factors.

## Carvacho--Hidalgo--Quispe

Mariela Carvacho, Rubén A. Hidalgo, Saúl Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903.

Classification:

```text
DIRECT_REUSABLE_STRUCTURE — GENERALIZED_FERMAT_(2,4)_ELLIPTIC_DECOMPOSITION
```

Generalized Fermat curves of type `(2,n)` are the complex-analytic/generalized-Fermat realization of Humbert curves. The paper decomposes their Jacobians through quotient curves attached to subgroups of the sign group and gives explicit quotient equations. It also exhibits positive-dimensional families whose Jacobians are isogenous to products of elliptic curves.

Stage14-t3 uses the more specialized Humbert--Edge theorem above for the factor count, while this source confirms that complete elliptic decomposability is a standard structural feature of the `(2,4)` setting rather than an accidental finite-data phenomenon.

## Hidalgo

Rubén A. Hidalgo, *Hyperelliptic quotients of generalized Humbert curves*, arXiv:1705.09337.

Classification:

```text
DIRECT_REUSABLE_STRUCTURE — UNIQUENESS_OF_HUMBERT_GROUP
```

For generalized Humbert curves of type `n>=4`, the paper records that the generalized Humbert group is unique. Therefore any automorphism of a type-4 fiber normalizes the sign group and descends to an automorphism of the five-point quotient orbifold.

Stage14-t3 combines this uniqueness theorem with an exact symbolic permutation audit of the five Stage14 branch values. The audit finds no nontrivial Möbius symmetry for rational physical `s=t^2>0`, so no enlarged-automorphism physical Pythagorean stratum remains.

## Peschmann — quartic and elliptic obstruction route

René Peschmann, *Quartic reductions and elliptic obstructions for perfect Euler bricks*, arXiv:2604.09328.

Classification:

```text
ADJACENT_RESULT — ELLIPTIC_QUOTIENT_OBSTRUCTION
```

This work reduces a perfect-cuboid formulation to a one-parameter genus-3 hyperelliptic family and studies a distinguished elliptic quotient using Kummer-character and 2-descent obstructions. It explicitly discusses a genus-5 covering obstruction as part of the remaining problem.

Stage14-t3 is complementary: the Stage14 genus-5 covering is identified as a type-4 Humbert--Edge curve whose entire Jacobian decomposes into five elliptic factors.

## Peschmann — torsion intersection on explicit fibers

René Peschmann, *A torsion-intersection proof of perfect-cuboid nonexistence on 1,072 explicit master-tuple fibers*, arXiv:2604.28072.

Classification:

```text
ADJACENT_RESULT / REUSABLE_METHOD — RANK_ZERO_PLUS_TORSION_INTERSECTION
```

This paper proves perfect-cuboid nonexistence on `1,072` explicit fibers by combining elliptic quotients with rank-zero certificates and torsion/lift analysis. The result is fiberwise and does not supply a moving-height asymptotic for the Stage14 triple count.

It does, however, identify the most concrete next attack after t3: obtain explicit Weierstrass models for the five Stage14 quotient factors, audit their torsion and rank behavior over Pythagorean bases, and determine whether a rank-zero/torsion intersection eliminates a positive-density or height-dominant portion of the moving family.

## Peschmann — elliptic fibration and square lifts

René Peschmann, *Exponent-one blockers and a Mordell-Weil construction of Euler bricks*, arXiv:2605.00573.

Classification:

```text
ADJACENT_RESULT — MOVING_ELLIPTIC_FIBRATION_AND_SQUARE_LIFT_FILTER
```

The paper uses an elliptic fibration over Euclid parameters and a rational function whose square-value condition selects admissible lifts. This is structurally close to the Stage14-t3 conclusion that triple points should be studied through elliptic factors plus explicit lift conditions rather than through genus-5 point counts alone.

## Collision / novelty boundary

The literature clearly contains the general Humbert--Edge decomposition and recent perfect-cuboid elliptic-quotient strategies. Stage14-t3 therefore makes no novelty claim for either ingredient in isolation.

The repository-specific contribution is the exact identification of the frozen Stage14 triple family with a one-parameter rational subfamily of type-4 Humbert--Edge curves, together with the explicit branch set

\[
\{\infty,0,1,-1/t^2,1/(1-t^2)\},
\]

the five concrete quotient models, and the proof that the physical rational base contains no singular or enlarged-automorphism stratum.

```text
NOVELTY_BY_SEARCH_ABSENCE=false
GENERAL_HUMBERT_DECOMPOSITION_KNOWN=true
PERFECT_CUBOID_ELLIPTIC_QUOTIENT_METHOD_KNOWN=true
DIRECT_STAGE14_FIVE_FACTOR_IDENTIFICATION=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
```
