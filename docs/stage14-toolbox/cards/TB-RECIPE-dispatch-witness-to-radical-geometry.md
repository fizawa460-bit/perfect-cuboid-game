# Dispatch an integral witness to arithmetic or geometry

```yaml
ID: TB-RECIPE-dispatch-witness-to-radical-geometry
TYPE: RECIPE
STATUS: CURRENT
TITLE: Choose radical incidence or fixed-packet genus-one geometry from an integral witness
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bj
SOURCE_PR: 355
SOURCE_MERGE_SHA: 7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
  - stages/stage14/14-s6-02/result.md
  - stages/stage14/14-4bi-L/result.md
  - stages/stage14/14-4bi-S/result.md
  - stages/stage14/14-4bj/result.md
```

## INPUT

An integral witness

```text
Y^2=G0*G1*G2
```

with signed squarefree packet `d0,d1,d2`, edge kernels, and full odd radicals `R_S,R_X,R_H`.

## OUTPUT

Dispatch by the strongest available structure:

```text
large usable full radical + long incident variables
  -> composite-modulus line incidence receiver

radical-poor supported base/classes
  -> radical-poor base-count receiver

fixed signed packet requiring point geometry
  -> two-quadrics / smooth genus-one receiver

short incident variable
  -> small-D / complementary sector receiver
```

## VARIABLE DICTIONARY

- `R_S,R_X,R_H` = full odd radicals, not selected kernels.
- `d_i` = signed squarefree packet coefficients.
- `D` = generic integral-witness denominator.

## USED BY

- Avoiding largest-prime-only case splits when the full radical is stronger.
- Choosing between arithmetic incidence and fixed-curve geometry.
- Keeping coordinate savings separate from packet-existence savings.

## DO NOT USE FOR

- Do not promote an incidence density bound to a whole-family saving without a receiver-level transfer.
- Do not identify small selected kernels with small full radicals.
- Genus one alone does not close a moving family.

## PROVENANCE NOTES

This recipe packages the merged 4bi-L/4bi-S/4bj arithmetic split and the merged s6-02 fixed-packet geometry.