# Historical whole-family ledger after s7-10 / 4by

```yaml
ID: TB-LEDGER-current-whole-family-after-s7-10
TYPE: LEDGER
STATUS: SUPERSEDED
SUPERSEDED_BY: TB-LEDGER-current-whole-family-after-s7-13
TITLE: Historical whole-family exponent 13/14 after the proved two-cell receiver
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

At that checkpoint:

```text
HISTORICAL_PHYSICAL_WHOLE_FAMILY_EXPONENT=13/14
IMPROVEMENT_OVER_15_16=1/112
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=1/21
HISTORICAL_REMAINING_GAP_TO_SQRT=3/7
SQUARE_ROOT_SQUARE_SIEVE_ARCHITECTURE_BARRIER=13/14
```

## VARIABLE DICTIONARY

- `13/14` = proved global checkpoint and a reusable two-cell/square-sieve receiver architecture.
- the all-frequency `O(p)` theorem and `(RS)^(-1/3)` coefficient saving remain valid inputs after this global ledger is superseded.

## USED BY

- External-theorem import provenance.
- The later full-coordinate refinements that use the proved two-cell theorem.

## DO NOT USE FOR

- Do not call `13/14` the current whole-family ceiling after merged s7-13.
- Do not infer that superseding the global exponent invalidates the two-cell theorem.

## PROVENANCE NOTES

Merged s7-13 imports the s7-10 two-cell theorem inside a finer common-coordinate refinement and improves the whole-family exponent to `7/8`.