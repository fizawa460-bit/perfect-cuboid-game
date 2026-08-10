# Current main-track exponent after optimized cross threshold

```yaml
ID: TB-LEDGER-current-main-after-4br
TYPE: LEDGER
STATUS: CURRENT
TITLE: Current whole-family exponent 20/21 and remaining square-root gap after 4br
SCOPE: MAIN
SOURCE_STAGE: Stage14-4br
SOURCE_PR: 396
SOURCE_MERGE_SHA: 01afa63539e32e62070a84927bbc0530241a79e9
SOURCE_FILES:
  - stages/stage14/14-4br/result.md
EXPONENT_SCALE: physical B
PREVIOUS_EXPONENT_EXACT: 61/63
CURRENT_EXPONENT_EXACT: 20/21
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42_EXACT: 1/42
TARGET_EXACT: 1/2
REMAINING_GAP_EXACT: 19/42
```

## INPUT

Merged 4br reoptimizes the 4bm cross-factor threshold using

```text
X2_cross <= 2^a * c * h^2,
X2_cross >= B^(4/21),
```

and the already-proved counting consequences for large `2^a`, `c`, or `h`. The optimal common threshold is

```text
delta = (4/21)/4 = 1/21.
```

This gives

```text
E_cross(B) << B^(20/21+o(1)).
```

The other merged sectors are

```text
small partner leg:  B^(20/21+o(1)),
good-cell residual: B^(13/14+o(1)).
```

## OUTPUT

The whole-family maximum is therefore

```text
V(B) << B^(20/21+o(1)).
```

Relative to the closed local baseline `41/42`, the cumulative direct post-local saving is

```text
41/42 - 20/21 = 1/42.
```

The current remaining gap to square-root scale is

```text
20/21 - 1/2 = 19/42.
```

## VARIABLE DICTIONARY

- `20/21` = current merged whole-family physical exponent at the 4br checkpoint.
- `1/42` = cumulative proved direct post-local saving from `41/42`.
- `19/42` = current remaining exponent gap from `20/21` to `1/2`.

## USED BY

- Current main-track exponent comparisons after merged 4br.
- Deciding whether later sector work improves the whole-family maximum.
- Distinguishing the local baseline `41/42` from the current post-local bound `20/21`.

## DO NOT USE FOR

- `20/21` is not a square-root theorem.
- Do not identify the cumulative saving `1/42` with the remaining gap `19/42`.
- Do not overwrite historical stage thresholds that were correctly frozen at earlier checkpoints.

## PROVENANCE NOTES

Merged PR #396 improves the 4bq cross-branch exponent `61/63` to `20/21` and recombines all merged sectors to prove the current whole-family `20/21` upper bound.