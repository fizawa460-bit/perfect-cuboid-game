# Integral witness arithmetic/geometry cookbook

```yaml
ID: TB-RECIPE-cookbook-witness-kernel-geometry
TYPE: RECIPE
STATUS: CURRENT
TITLE: Checklist for routing an integral witness to radical incidence or fixed-packet geometry
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bj
SOURCE_PR: 355
SOURCE_MERGE_SHA: 7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
  - stages/stage14/14-s6-02/result.md
  - stages/stage14/14-4bi-S/result.md
  - stages/stage14/14-4bj/result.md
```

## INPUT

An integral witness `Y^2=G0*G1*G2` with the exact pairwise gcd-support identities.

## OUTPUT

A legal choice between the full-radical incidence receiver and the fixed signed-packet two-quadrics/genus-one receiver.

## VARIABLE DICTIONARY

- `L2` = integral witness coordinate.
- `L3` = fixed signed kernel packet.
- `L4` = fixed curve/fiber.
- `R_S,R_X,R_H` = full odd radical moduli, distinct from selected packet kernels.

## USED BY

- Choosing the arithmetic or geometric continuation after witness integralization.
- Keeping full-radical coordinate density separate from packet/family counts.

## DO NOT USE FOR

- Do not promote an incidence saving directly to packet existence.
- Do not promote a fixed genus-one point bound directly to a moving-family saving.

## PROVENANCE NOTES

The recipe combines only merged witness, radical, and fixed-packet interfaces; it adds no new counting theorem.