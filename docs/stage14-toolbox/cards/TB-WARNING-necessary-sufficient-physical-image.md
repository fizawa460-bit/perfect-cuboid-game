# Necessary-versus-sufficient physical-image warning

```yaml
ID: TB-WARNING-necessary-sufficient-physical-image
TYPE: WARNING
STATUS: CURRENT
TITLE: Do not reverse a transferred physical-image equation without reconstruction
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-08
SOURCE_PR: 369
SOURCE_MERGE_SHA: e9916a9e21dc305fa30e240d3db962a26af1653b
SOURCE_FILES:
  - stages/stage14/14-s6-07/result.md
  - stages/stage14/14-s6-08/result.md
```

## INPUT
An equation known for every physical image, for example the transferred cross-square or its half-angle factorization.

## OUTPUT
Treat it as a necessary condition unless a later stage proves an inverse construction, primitivity, orientation, and the exact cutoff.

## VARIABLE DICTIONARY
- physical image = data obtained from an actual Stage14 edge.
- converse = reconstruction from abstract arithmetic data back to a physical edge.

## USED BY
- Screening ambient Diophantine solutions before declaring them physical.

## DO NOT USE FOR
- Do not count all solutions of the necessary equation as physical without a justified upper-majorant relation.
- Do not call a necessary equation a bijection unless reconstruction and cutoff are proved.

## PROVENANCE NOTES
s6-07/s6-08 deliberately state the transferred square as a physical-image condition; later stages may strengthen the converse separately.