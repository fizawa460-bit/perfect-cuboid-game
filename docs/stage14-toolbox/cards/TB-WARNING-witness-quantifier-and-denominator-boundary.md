# Witness quantifier and denominator boundary

```yaml
ID: TB-WARNING-witness-quantifier-and-denominator-boundary
TYPE: WARNING
STATUS: CURRENT
TITLE: Do not reverse witness majorants or identify generic and compact denominators
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
  - stages/stage14/14-s6-05/result.md
```

## INPUT

Any argument importing the integral witness variables `(A,D,Y,G0,G1,G2)` into later main/s work.

## OUTPUT

Keep these locks active:

```text
physical -> global witness -> integral witness
integral witness -> physical                         NOT AVAILABLE
local admissible -> global witness                   NOT AVAILABLE
polynomial coordinate density -> unweighted packet saving  NOT AUTOMATIC
D = generic rational witness denominator
D_T = later compact physical torsion-translate denominator
D != D_T unless separately proved in a specific argument
G_i=0 = torsion boundary, not non-torsion witness
```

## VARIABLE DICTIONARY

- `D` is the denominator from the monic cubic integerization.
- `D_T` is the distinct compact physical denominator introduced later in s6-05/s6-06.

## USED BY

- Preventing quantifier errors when applying square-sieve or incidence bounds to witness coordinates.
- Preventing silent denominator substitutions across s6 stages.

## DO NOT USE FOR

- Do not use a fixed-packet coordinate saving as a whole-family saving without multiplicity transfer.
- Do not infer a physical solution from a bare integral solution of the cleared cubic equation.

## PROVENANCE NOTES

PR #345 establishes the one-sided witness majorant. Later merged denominator stages introduce different optimized selectors; this card keeps those notions separated.