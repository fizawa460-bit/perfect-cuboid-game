# Stage29-02a — Testa--Stoll source lock

Primary source:

- Damiano Testa, Michael Stoll, `Curves on the surface of cuboids` / current open preprint title `The surface parametrizing cuboids`.
- Mathematics of Computation, DOI `10.1090/mcom/4238`, accepted 20 April 2026.
- Open preprint locator: arXiv `1009.0388`; author PDF `https://www.mathe2.uni-bayreuth.de/stoll/papers/Cuboidi.pdf`.

## Exact locators used

The current author PDF states:

- Introduction / Theorems 1--2: full automorphism group and geometric Picard rank `64`.
- Lemma 3 (Section 2): the cuboid surface is a geometrically integral `(2,2,2,2)` complete-intersection surface in `P^6` with `48` isolated `A1` singularities.
- Immediately after Lemma 3: adjunction/canonical-model calculation; the minimal desingularization has `K^2=16`, `p_g=7`, `q=0`, canonical divisor big and nef, hence is a minimal surface of general type and the singular projective surface is its canonical model.
- Section 7, Theorem 15: conics / degree-4 curve classification.
- Section 7, Theorem 16: curves spanning `P^2`, `P^3`, `P^4`; the `P^4` case has degree 8 and belongs to one of 28 fibrations.
- Section 7, Theorem 17: **there are no integral curves of degree 6 on the cuboid surface**.
- Corollary 18: the explicitly known set `G` is precisely the set of integral curves whose canonical degree is at most 6 on the desingularization.
- Lemma 21: a rational curve other than a conic has exceptional-divisor intersection at least 8; a geometric-genus-one curve has exceptional-divisor intersection at least 4.

## Applicability adapter to Stage29

Stage29 F1 uses coordinates `[a:b:c:x:y:z:d]` with

```text
a^2+b^2=x^2
a^2+c^2=y^2
b^2+c^2=z^2
a^2+b^2+c^2=d^2.
```

Testa--Stoll use sides `a1,a2,a3`, face diagonals `b1,b2,b3`, and long diagonal `c`, with the same four quadratic relations up to relabeling.  Therefore the projective endpoint variety is the same exact algebraic surface.  The physical Stage29 constraints `a,b,c>0`, canonical ordering, primitivity, and `d=R<=B` select arithmetic/chamber representatives on this surface; they do not alter the projective geometric statements.

```text
PROJECTIVE_ENDPOINT_MODEL_MATCH=true
COORDINATE_ADAPTER=RENAMING_ONLY
GEOMETRIC_THEOREM_TRANSFER_LOSS=0
PHYSICAL_COUNTING_ADAPTER_STILL_REQUIRED=true
```

## Key firewall

Projective canonical degree on the full endpoint surface is not automatically equal to the Stage20/Stage28 physical polarization degree on a marginal K3 cover.  In particular, the audited degree-six Saunderson rational curve on the Stage20 K3 cannot be compared numerically with Theorem 17 until a map/polarization adapter to the full endpoint surface is proved.
