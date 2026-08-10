# Historical main-track exponent after optimized cross threshold

```yaml
ID: TB-LEDGER-current-main-after-4br
TYPE: LEDGER
STATUS: SUPERSEDED
TITLE: Historical whole-family exponent 20/21 and square-root gap after 4br
SCOPE: MAIN
SOURCE_STAGE: Stage14-4br
SOURCE_PR: 396
SOURCE_MERGE_SHA: 01afa63539e32e62070a84927bbc0530241a79e9
SOURCE_FILES:
  - stages/stage14/14-4br/result.md
SUPERSEDED_BY: TB-LEDGER-current-whole-family-after-s7-08
EXPONENT_SCALE: physical B
PREVIOUS_EXPONENT_EXACT: 61/63
CHECKPOINT_EXPONENT_EXACT: 20/21
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42_EXACT: 1/42
TARGET_EXACT: 1/2
CHECKPOINT_REMAINING_GAP_EXACT: 19/42
```

## INPUT

At the 4br checkpoint the cross branch, small-partner sector, and good-cell residual recombined to

```text
V(B) << B^(20/21+o(1)).
```

## OUTPUT

The 4br checkpoint remains exactly

```text
41/42 - 20/21 = 1/42,
20/21 - 1/2   = 19/42.
```

It is no longer the current whole-family ledger because merged s7-08 proves `18/19`.

## VARIABLE DICTIONARY

- `20/21` = historical whole-family exponent at the merged 4br checkpoint.
- `19/42` = historical remaining gap at that checkpoint.
- current successor = `TB-LEDGER-current-whole-family-after-s7-08`.

## USED BY

- Historical provenance and comparison with the s7-08 improvement.
- Reproducing older 4br/4bs threshold arithmetic.

## DO NOT USE FOR

- Do not call `20/21` the current whole-family exponent.
- Do not use `19/42` as the current gap to square-root scale.

## PROVENANCE NOTES

Merged PR #396 established the `20/21` whole-family checkpoint. Merged PR #417 later improves it to `18/19`; toolbox-ak records the supersession without deleting the 4br theorem.