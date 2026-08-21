# Stage29-02a — Testa--Stoll Euler-K3 bridge candidate

## Published quotient

Testa--Stoll Section 6 takes the full cuboid surface and quotients by the involution changing the sign of the long diagonal `c`.  The resulting singular model `Kbar_c` is the intersection of the three face-diagonal quadrics in `P^5`:

```text
a1^2+a2^2=b3^2
a1^2+a3^2=b2^2
a2^2+a3^2=b1^2.
```

Its minimal desingularization `K_c` is a K3 surface, and the source explicitly states that it parametrizes Euler bricks.  The quotient map `S -> K_c` is induced by forgetting the sign of the long diagonal.  The paper also obtains 15 elliptic fibrations on `K_c`.

## Relation to Stage20

Stage20 / Stage14-e8 constructs the Euler-brick locus as the degree-two third-face completion cover

```text
X_face -> Y=Bl_4(P1xP1)
```

and resolves it to a K3 surface.  Both `X_face` and `K_c` therefore describe the same labeled Euler-brick moduli on dense nondegenerate opens, but they arise from different presentations:

- `X_face`: double cover of the two-face toric base;
- `K_c`: complete intersection of three quadrics after quotienting the full cuboid surface by long-diagonal sign.

The expected relation is birational on the common physical open; because smooth projective K3 surfaces are minimal, a proved birational map would upgrade to an isomorphism.  Stage29-02a does **not** yet claim the exact global isomorphism or identify the two polarizations.

```text
TESTA_STOLL_KC_PARAMETRIZES_EULER_BRICKS=true
STAGE20_XFACE_PARAMETRIZES_EULER_BRICKS=true
DENSE_OPEN_BIRATIONAL_IDENTIFICATION_EXPECTED=true
GLOBAL_K3_ISOMORPHISM_PROVED_IN_REPO=false
POLARIZATION_ADAPTER_PROVED=false
```

## Why this matters

Testa--Stoll compute structural information on `K_c` not yet used by Stage20/28, including the Picard lattice interface and 15 elliptic fibrations.  Stage28's unresolved construction-side receiver is

```text
UniformMovingEllipticFibreSquareLiftHeightCount
```

so the published `K_c` fibrations may provide explicit geometric models for the moving-fibre side after an exact identification/height adapter.

This creates a new Stage29 receiver:

```text
R29-K1=Stage20ToricK3ToTestaStollEulerK3BirationalPolarizationAdapter
```

Required fields:

1. explicit dense-open map in both directions;
2. exceptional divisors / singular-model correspondence;
3. identification of Stage28 `M_face` with a divisor class in `Pic(K_c)`;
4. degree/height conversion with no hidden power loss;
5. matching of the 15 elliptic fibrations to Stage20 physical coordinates.

Until R29-K1 is proved, Testa--Stoll projective/hyperplane degrees and Stage28 `M_face` degrees are kept distinct.
