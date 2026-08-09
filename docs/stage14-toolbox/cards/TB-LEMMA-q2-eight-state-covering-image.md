# Exact eight-state Q2 covering image

```yaml
ID: TB-LEMMA-q2-eight-state-covering-image
TYPE: LEMMA
STATUS: CURRENT
TITLE: Exact eight-state Q2 Kummer image for the Stage14 covering
SCOPE: BOTH
SOURCE_STAGE: Stage14-s5f
SOURCE_PR: 229
SOURCE_MERGE_SHA: dd13e6ffae243a4fa3b1144ab97d33e7c8a0ae23
SOURCE_FILES:
  - stages/stage14/14-s5e/result.md
  - stages/stage14/14-s5f/result.md
```

## INPUT

The normalized local Kummer triple

```text
[q], [q-1], [q+t^2]
```

with `v2(t)>=2`, represented in `Q2*/Q2*^2` by `1,3,5,7,2,6,10,14`.

## OUTPUT

Exactly eight of the 64 product-square states occur:

```text
(1,1,1)
(3,7,5)
(5,1,5)
(7,7,1)
(2,1,2)
(6,7,10)
(10,1,10)
(14,7,2).
```

Hence

```text
Q2_PRODUCT_SQUARE_STATE_COUNT=64
Q2_COVERING_SOLUBLE_STATE_COUNT=8.
```

## VARIABLE DICTIONARY

- `q` = normalized rational Kummer coordinate.
- `t=X/S` in the historical s5 local normalization, with `v2(t)>=2`.
- the ordered triple records the three local squareclasses in the covering.

## USED BY

- Final prime-2 row of the full local 2-descent character system.
- Full local admissibility checks after the odd rows have passed.
- Main-track imports of the closed local Selmer/Kummer gate.

## DO NOT USE FOR

- Do not replace this theorem by a finite-modulus survival test.
- Do not infer global solubility from membership in the eight-state table.
- Do not assume the eight states are equally likely in a moving physical family.

## PROVENANCE NOTES

- PR #224 fixes exact Q2 squareclass algebra.
- Merged PR #229 performs the covering-specific valuation-cylinder classification and closes the prime-2 local image.
