# Current whole-family ledger after 4bx

```yaml
ID: TB-LEDGER-current-whole-family-after-4bx
TYPE: LEDGER
STATUS: CURRENT
TITLE: Current whole-family exponent 15/16 and square-root gap after 4bx
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bx
SOURCE_PR: 422
SOURCE_MERGE_SHA: 6774b9b6fb662cb14cc221c0b56bb74c077a3659
SOURCE_FILES:
  - stages/stage14/14-4bx/result.md
```

## INPUT

Merged 4bx reoptimizes the thick packet square sieve to `H^(-4/5)` and recombines it with the merged one-cell thin receiver.

## OUTPUT

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=15/16
CURRENT_REMAINING_GAP_TO_SQRT=7/16
IMPROVEMENT_OVER_18_19=3/304
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=13/336
```

## VARIABLE DICTIONARY

- `15/16` = current proved whole-family exponent.
- `7/16` = remaining exponent gap to square-root scale.
- `3/304` = strict improvement over the prior `18/19` current checkpoint.
- `13/336` = cumulative saving from the closed local `41/42` baseline.

## USED BY

- Every current Stage14 main/s exponent comparison after merged 4bx.
- Deciding whether a later receiver improves the whole-family ceiling.

## DO NOT USE FOR

- `15/16` is not the square-root theorem.
- Do not replace it by the conditional `13/14` two-cell target without the missing mixed Fourier theorem.

## PROVENANCE NOTES

Merged PR #422 is the current unconditional whole-family source at toolbox-al time.