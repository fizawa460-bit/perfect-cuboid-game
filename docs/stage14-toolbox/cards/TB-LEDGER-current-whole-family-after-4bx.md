# Historical whole-family ledger after 4bx

```yaml
ID: TB-LEDGER-current-whole-family-after-4bx
TYPE: LEDGER
STATUS: SUPERSEDED
SUPERSEDED_BY: TB-LEDGER-current-whole-family-after-s7-10
TITLE: Historical whole-family exponent 15/16 and square-root gap after 4bx
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

At the 4bx checkpoint:

```text
HISTORICAL_PHYSICAL_WHOLE_FAMILY_EXPONENT=15/16
HISTORICAL_REMAINING_GAP_TO_SQRT=7/16
IMPROVEMENT_OVER_18_19=3/304
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=13/336
```

## VARIABLE DICTIONARY

- `15/16` = proved whole-family exponent at the 4bx checkpoint.
- `7/16` = historical square-root gap at that checkpoint.
- `H^(-4/5)` remains a current reusable thick-packet theorem even though the whole-family ledger is superseded.

## USED BY

- Historical provenance and the thick-side input to the later 13/14 theorem.
- Comparing the gain `15/16 -> 13/14 = 1/112`.

## DO NOT USE FOR

- Do not call `15/16` current after merged s7-10/4by.
- Do not interpret superseding the global ledger as superseding the 4bx packet inequality.

## PROVENANCE NOTES

Merged s7-10 and 4by later prove the previously conditional two-cell receiver and supersede this global checkpoint with `13/14`.