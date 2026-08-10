# Current whole-family ledger after s7-10 / 4by

```yaml
ID: TB-LEDGER-current-whole-family-after-s7-10
TYPE: LEDGER
STATUS: CURRENT
TITLE: Current whole-family exponent 13/14 and square-root gap after the proved two-cell receiver
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-10
SOURCE_PR: 425
SOURCE_MERGE_SHA: 1fca91407117c6cf486483b49299733bbbbbd519
SOURCE_FILES:
  - stages/stage14/14-s7-10/result.md
  - stages/stage14/14-4by/result.md
  - stages/stage14/14-4bz/result.md
```

## INPUT

Merged s7-10 and 4by prove the adjacent two-cell mixed Fourier receiver and combine it with the merged 4bx thick-packet estimate.

## OUTPUT

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=13/14
IMPROVEMENT_OVER_15_16=1/112
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=1/21
CURRENT_REMAINING_GAP_TO_SQRT=3/7
CURRENT_SQUARE_ROOT_SQUARE_SIEVE_ARCHITECTURE_BARRIER=13/14
SQRT_B_UPPER_BOUND_PROVED=false
```

## VARIABLE DICTIONARY

- `13/14` = current proved whole-family exponent.
- `1/112` = gain over merged 4bx `15/16`.
- `1/21` = cumulative saving from the closed local `41/42` baseline.
- `3/7` = remaining gap to exponent `1/2`.

## USED BY

- Every current main/s exponent comparison after s7-10/4by.
- Selecting genuinely new receivers beyond the present square-sieve architecture.

## DO NOT USE FOR

- Do not claim a square-root upper bound.
- Do not expect threshold retuning or naive 3-/4-cell enlargement to improve this ceiling; merged 4bz/s7-11 rule those routes out within the current architecture.

## PROVENANCE NOTES

Merged s7-10 first closes the missing s7-09 theorem gate; merged 4by independently rederives the same `13/14`; merged 4bz records the resulting architecture barrier.