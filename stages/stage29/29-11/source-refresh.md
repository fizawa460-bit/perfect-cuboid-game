# Stage29-11 source refresh — audited

```text
STATUS=AUDITED_SOURCE_REFRESH
CURRENT_WEB_REFRESH_ATTEMPTED=true
CURRENT_WEB_REFRESH_AVAILABLE=true
```

## Campedelli

Primary source checked directly:

```text
A. Calabri, M. Mendes Lopes, R. Pardini
Involutions on numerical Campedelli surfaces
Tohoku Math. J. 60 (2008), 1--22
DOI 10.2748/tmj/1206734404
```

For a classical Campedelli surface, the paper states that all involutions are composed with the bicanonical map. Its general analysis then gives the geometric quotient dichotomy: rational or birational to an Enriques surface. Since the classical deck group is `(Z/2)^3`, this covers all seven nontrivial involutions.

This certifies only the geometric/birational child receiver:

```text
R29-CAMP3-GEOM=DISCHARGED_GEOMETRIC_RATIONAL_OR_ENRIQUES_DICHOTOMY
```

It does not determine the exact rational-versus-Enriques assignment for the cuboid inherited Q-forms, and it does not descend a geometric rational parametrization to Q. Hence

```text
R29-CAMP3=PARTIAL_GEOMETRIC_DONE_Q_FORM_AND_EXACT_INVOLUTION_ASSIGNMENT_OPEN
```

The exact ten-kernel and `8+2` geometric / `6+2+2` certified-Q orbit data remain the audited repo computation; no exact Q-isomorphism-class count is inferred.

## Beauville

Primary source retained:

```text
A. Beauville, A tale of two surfaces
```

The current surfaced PDF places the etale `(Z/2)^2` tower and Albanese pullback discussion in **Remark 2**. The historical Stage29-02d audit recorded **Remark 1**. This is treated as a source-version/locator provenance repair only; the tower itself was already independently audited in-repo and its mathematical content is unchanged.

The exact Q-form degree-two cover, constant `Z/2` deck group, and pointwise twist decomposition remain certified. No theorem found in this refresh forces the physical twist classes into a finite subset of `Q*/Q*^2`, and no individual genus-two Selmer algorithm supplies uniform closure over the whole physical family.

## Modular

The Stage29-02g audit remains authoritative:

```text
K8=ker(SL2(Z/8)->SL2(Z/4)), |K8|=8,
ordinary symplectic conjugacy class sizes = 1,3,3,1.
```

The current refresh found no already-completed sigma-twisted retained level-4 action identifying those four abstract classes with the exact arithmetic endpoint strata. `R29-MOD1C` therefore stays open.

Likewise, the arrangement `S4` and generic modular residual `S4` are not identified at action/cocycle level. Thus

```text
R29-KUM5=OPEN_ACTION_LEVEL_S4_Q_DESCENT_ADAPTER.
```

## Brauer

The current Testa--Stoll cuboid PDF was checked directly. Its **Theorem 10** states that the algebraic part of the Brauer group of the smooth proper cuboid surface is exactly the image of `Br(Q)`. Thus the repo's theorem locator is current and correct.

The Stage29-02f proper odd-primary transcendental exclusion remains separately derived and audited. Neither result computes the physical-open extended Picard/Gersten boundary problem or the two-primary local evaluation maps.

No source found in this refresh supplies an open Brauer--Manin obstruction for the physical endpoint open.

## Source-refresh verdict

```text
NEW_FOUNDATION_FOUND=false
NEW_ATTACK_ROUTE_CREATED=false
GREEN_ROUTE_CREATED=false
ROADMAP_REWRITE_REQUIRED=false
BOUNDED_SOURCE_REPAIR=BEAUVILLE_CURRENT_REMARK_2_LOCATOR_PROVENANCE
```
