# Full local 2-descent character check

```yaml
ID: TB-RECIPE-full-local-character-check
TYPE: RECIPE
STATUS: CURRENT
TITLE: End-to-end local admissibility check over five moving columns
SCOPE: BOTH
SOURCE_STAGE: Stage14-s5f
SOURCE_PR: 229
SOURCE_MERGE_SHA: dd13e6ffae243a4fa3b1144ab97d33e7c8a0ae23
SOURCE_FILES:
  - stages/stage14/14-s5b/result.md
  - stages/stage14/14-s5c/result.md
  - stages/stage14/14-s5d/result.md
  - stages/stage14/14-s5e/result.md
  - stages/stage14/14-s5f/result.md
```

## INPUT

A primitive oriented Pythagorean base and one supported full-2-descent squareclass packet.

## OUTPUT

Apply the following pipeline:

```text
1. Fix the oriented covering and identify actual S,X,H.
2. Split odd bad-prime support among m,n,m-n,m+n,m^2+n^2.
3. Use the orientation adapter to determine whether each column is an S-, X-, or H-column.
4. For every odd bad prime determine selected vs unselected.
5. Apply the corresponding exact odd local row.
6. Encode the prime-2 squareclass triple.
7. Require membership in the exact eight-state Q2 covering image.
8. If all places pass, mark the packet LOCAL_ADMISSIBLE.
```

The output is the complete merged Stage14 local 2-descent character condition.

## VARIABLE DICTIONARY

- `LOCAL_ADMISSIBLE` = locally soluble with respect to the complete merged odd + Q2 covering conditions.
- `selected/unselected` = whether the bad prime occurs in the squarefree support of the `di`.
- `five columns` = `m,n,m-n,m+n,m^2+n^2`.

## USED BY

- Local Selmer/Kummer majorants.
- Character-sum and large-sieve expansions of the closed local system.
- Checking whether a global/physical packet has passed all local necessary conditions.

## DO NOT USE FOR

- `LOCAL_ADMISSIBLE` is not the same as globally soluble.
- The recipe does not average the character system and does not itself prove a power saving.
- The recipe contains no small-point height distribution theorem.

## PROVENANCE NOTES

- PR #229 records `FULL_LOCAL_2_DESCENT_CHARACTER_SYSTEM_COMPLETE=true` after importing the merged odd rows and exact Q2 image.
