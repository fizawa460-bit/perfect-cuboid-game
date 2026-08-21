# Stage29-02a — Testa--Stoll source lock

```text
TASK=Stage29-02a
SOURCE_KIND=PUBLISHED_IN_PRESS_MATHEMATICS_OF_COMPUTATION
SOURCE_AUDIT=PASS
```

Primary source:

- Damiano Testa, Michael Stoll, `Curves on the surface of cuboids` / current author-PDF title `The surface parametrizing cuboids`.
- *Mathematics of Computation*, DOI `10.1090/mcom/4238`, accepted 20 April 2026.
- Open preprint locator: arXiv `1009.0388`; author PDF `https://www.mathe2.uni-bayreuth.de/stoll/papers/Cuboidi.pdf`.

## Exact locators used

The current author PDF gives the following load-bearing locators.

- Introduction / Theorems 1--2: full automorphism group and geometric Picard rank `64`.
- Lemma 3 / Section 2: the cuboid surface is a geometrically integral `(2,2,2,2)` complete-intersection surface in `P^6` with `48` isolated `A1` singularities.
- Immediately after Lemma 3: adjunction/canonical-model calculation; the minimal desingularization has `K^2=16`, `p_g=7`, `q=0`, canonical divisor big and nef, hence is a minimal surface of general type and the singular projective surface is its canonical model.
- Definition 6: the explicit low-degree set `G=G0 union G1 union G2 union G3` consisting of exceptional curves, conics in `a_j=0` or `c=0`, genus-one curves in `b_j=0`, and genus-one curves in `a_j=±a_{j+1}` or `a_j=±ic`.
- Section 5: the rank-3/rank-4 quadric construction yields exactly `6+2*11=28` fibrations; generic fibers are smooth canonically embedded genus-5 curves of projective degree `8`.
- Section 6: quotient by the sign change of the long diagonal `c` gives `Kbar_c`; its minimal desingularization `K_c` is a K3 surface explicitly stated to parametrize Euler bricks.
- Section 6: the rank-3/rank-4 quadrics on `K_c` yield exactly `3+2*6=15` elliptic fibrations.
- Theorem 15: conics / degree-4 curve classification.
- Theorem 16: curves spanning `P^2`, `P^3`, `P^4`; the `P^4` case has degree `8` and is a fiber of one of the 28 fibrations.
- Theorem 17: **there are no integral curves of degree 6 on the cuboid surface**.
- Corollary 18: the explicit set `G` is precisely the set of integral curves whose canonical degree is at most `6` on the desingularization.
- Lemma 21: a rational curve other than a conic has exceptional-divisor intersection at least `8`; a geometric-genus-one curve has exceptional-divisor intersection at least `4`.

## Applicability adapter to Stage29

Stage29 F1 uses coordinates `[a:b:c:x:y:z:d]` with

```text
a^2+b^2=x^2
a^2+c^2=y^2
b^2+c^2=z^2
a^2+b^2+c^2=d^2.
```

Testa--Stoll use sides `a1,a2,a3`, face diagonals `b1,b2,b3`, and long diagonal `c`, with the same four quadratic relations up to relabeling. Therefore the projective endpoint variety is the same exact algebraic surface. The physical Stage29 constraints select arithmetic/chamber representatives on this surface; they do not alter the projective geometric statements.

```text
PROJECTIVE_ENDPOINT_MODEL_MATCH=true
COORDINATE_ADAPTER=RENAMING_ONLY
GEOMETRIC_THEOREM_TRANSFER_LOSS=0
PHYSICAL_COUNTING_ADAPTER_STILL_REQUIRED=true
```

## Positive physical chamber adapter

For a positive rational-box endpoint:

- `a_j=0`, `c=0`, or `b_j=0` is degenerate;
- `a_j=±a_{j+1}` with nonzero rational sides forces the corresponding rational face diagonal to be `sqrt(2)|a_j|`, impossible over `Q`;
- `a_j=±ic` has no positive real point;
- exceptional curves lie over the singular/degenerate locus.

Thus the canonical-degree-<=6 classification excludes positive nondegenerate **curve-family carriers**. It does not exclude isolated rational points or points on higher-degree curves.

## Firewalls

```text
GENERAL_TYPE_IMPLIES_RATIONAL_POINT_FINITE=false
DEGREE6_CURVE_ABSENCE_IMPLIES_NO_PERFECT_CUBOID=false
LOW_DEGREE_CURVE_FILTER_IS_WHOLE_ENDPOINT_CLOSURE=false
STAGE20_M_FACE_DEGREE_EQUALS_ENDPOINT_CANONICAL_DEGREE=false
TESTA_STOLL_KC_EQUALS_STAGE20_XFACE_WITHOUT_ADAPTER=false
FIBRATION_IMPLIES_COUNTING_EXPONENT=false
```

The exact downstream bridge remains

```text
R29-K1=Stage20ToricK3ToTestaStollEulerK3BirationalPolarizationAdapter
```
