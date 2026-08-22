# Stage29-10 source refresh

This file records only source changes/materiality relevant to the three 29-10 routes. It does not reopen the broad 29-02 literature screen.

## Testa--Stoll — current publication state

Current publication:

```text
Damiano Testa and Michael Stoll
Curves on the surface of cuboids
Mathematics of Computation
DOI: 10.1090/mcom/4238
published electronically: 2026-08-10
open preprint lineage: arXiv:1009.0388
```

The current abstract states that the integral curves of degree at most six on the cuboid surface are completely classified. The repo's 29-02c-LG2 work had already consumed the corresponding degree-`<=6` computation and the public verification code, so this publication refresh does not create a new receiver or invalidate the existing finite Picard reduction.

Stable public verification lock retained from 29-02c-LG2:

```text
repo=https://github.com/MichaelStollBayreuth/Verification
commit=51233ed5ef2bf228fac9416c66db9adc0ebcaadd
file=Cuboids/cuboids.magma
```

Verdict:

```text
TESTA_STOLL_CURRENT_PUBLICATION_REFRESHED=true
NEW_POST_29_02C_LOWGENUS_THEOREM_FOUND=false
DEGREE_LE6_CLASSIFICATION_ALREADY_CONSUMED=true
```

## Terasoma — four-quadric correspondence scope

Source:

```text
Tomohide Terasoma
Complete intersections of hypersurfaces — the Fermat case and the quadric case
Japan. J. Math. 14 (1988), 309–384
DOI: 10.4099/math1924.14.309
```

The four-quadric/K3 correspondence package is stated in the normal-crossing/smooth complete-intersection setting; the smoothness hypothesis is explicit in the Tate-conjecture corollary and the correspondence isomorphism statements used by the old receiver.

The cuboid canonical model is not smooth: it has 48 A1 nodes. No source located in this refresh supplies the exact specialization/resolution theorem needed to apply the smooth statement to this singular fiber without further work.

Independently, Stage29-02e already proves the endpoint-specific seven coordinate-K3 transcendental decomposition globally by exact quotient/eigenspace arguments. Therefore the missing Terasoma specialization is not required merely to recover that cohomological decomposition.

The audit narrows the demotion claim: this does not prove that every cycle-level or future Chow-theoretic consequence of a valid singular specialization would be redundant. It only says that the cohomological target motivating the current rational-point attack receiver is already supplied, with no current endpoint rational-point consequence gained by replaying the smooth correspondence.

Verdict:

```text
R29-TERA1_SPECIALIZATION_DISCHARGED=false
TERASOMA_COHOMOLOGY_TARGET_ALREADY_SUPPLIED_BY_29_02E=true
TERASOMA_CYCLE_LEVEL_FUTURE_VALUE_NOT_RULED_OUT=true
```

## Cuboid fundamental groups / higher-dimensional Chabauty--Kim

Current cuboid source:

```text
Benjamin Enriquez, David Jarossay, Francesco Maria Saettone, Yotam Svoray
The fundamental group of surfaces parametrizing cuboids
arXiv:2310.12710v3
version date: 2026-07-06
```

The source proves simple connectedness for the projective cuboid surface and its resolution, and computes fundamental groups/Malcev completions for selected smooth opens on the face-cuboid surface. It does not provide a computed unipotent fundamental group or Kim function for the Stage29 physical endpoint open.

Method comparison source:

```text
Ishai Dan-Cohen and David Jarossay
M_{0,5}: Toward the Chabauty–Kim method in higher dimensions
Mathematika 69 (2023), 1011–1059
DOI: 10.1112/mtk.12215
```

This supplies a genuine higher-dimensional Kim-function example on `M_{0,5}`. It is not a general transfer theorem from an arbitrary smooth open surface with nontrivial unipotent fundamental group.

Verdict:

```text
R29-PI1-OPEN=AMBER_NO_EFFECTIVE_CUBOID_ENDPOINT_KIM_ADAPTER
HIGHER_DIMENSIONAL_CK_GENERALLY_IMPOSSIBLE_CLAIM=false
CUBOID_ENDPOINT_EFFECTIVE_ADAPTER_FOUND=false
```

## Source-refresh stop

No source in this targeted refresh changes the eleven-route architecture.

```text
NEW_FOUNDATION_FOUND=false
NEW_ATTACK_ROUTE_CREATED=false
ROADMAP_REWRITE_REQUIRED=false
```
