# Stage29-02a — research notes

## New endpoint-specific information

The strongest immediate new information is not a population bound but a geometric exclusion layer on the full endpoint surface.

- There are no integral projective curves of degree 6 on the full cuboid surface.
- Degree 2 and degree 4 curves are explicitly classified; smooth rational quartics do not occur.
- Curves contained in low-dimensional linear spans are rigidly classified; a curve spanning `P^4` has degree 8 and is a fiber of one of 28 fibrations.
- Low-genus curves must meet the exceptional divisor substantially: rational non-conics at least 8, genus-one curves at least 4, in the source's intersection convention.

These statements create a new family-testing strategy for Stage29:

```text
candidate endpoint family
  -> exact map to full cuboid surface
  -> compute canonical/projective degree + genus + node incidence
  -> compare with Testa--Stoll low-degree classification
```

This is materially different from the Stage27/28 population-count gates and can eliminate endpoint families without needing a whole-population theorem.

## Relation to StageA2

StageA2 closes one explicit family by quotient/two-cover/descent.  Stage29-02a provides a complementary *global-surface* filter.  A future family may be killed either because its induced endpoint curve lies in a classified forbidden low-degree class, or because a surviving higher-degree slice admits an A2-style descent.  These are not independent savings and should not be multiplied.

## Relation to joint cover

The full endpoint surface and the Stage29 joint cover are two descriptions of simultaneous completion.  The crucial missing adapter is currently geometric rather than analytic:

```text
R29-G1=GlobalEndpointSurfaceToToricJointCoverAdapter
```

It must identify the rational map on dense opens, exceptional/branch loci, degree, physical height distortion, and symmetry/multiplicity.  Once this exists, endpoint-curve degree restrictions can potentially be pulled back to the joint-cover side.

## Provisional verdict

```text
NEW_REPO_WEAPON_FOUND=true
WEAPON_KIND=GLOBAL_ENDPOINT_LOW_DEGREE_GEOMETRY
OLD_STAGE_REENTRY_REQUIRED=false
KEEP_STAGE29_NATIVE=true
FURTHER_29_02A_RESEARCH_REQUIRED=true
```
