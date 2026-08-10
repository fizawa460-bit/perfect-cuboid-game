# Historical conditional two-cell ledger after 4bx

```yaml
ID: TB-LEDGER-updated-conditional-two-cell-after-4bx
TYPE: LEDGER
STATUS: SUPERSEDED
SUPERSEDED_BY: TB-LEDGER-current-whole-family-after-s7-10
TITLE: Historical conditional adjacent two-cell target 13/14 before the theorem gate was closed
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bx
SOURCE_PR: 422
SOURCE_MERGE_SHA: 6774b9b6fb662cb14cc221c0b56bb74c077a3659
SOURCE_FILES:
  - stages/stage14/14-4bx/result.md
  - stages/stage14/14-s7-09/result.md
```

## INPUT

At the 4bx checkpoint the s7-09 adjacent two-cell mixed Fourier theorem was still open, while the thick side had already improved to `H^(-4/5)`.

## OUTPUT

Historical planning target:

```text
HISTORICAL_CONDITIONAL_TWO_CELL_WHOLE_FAMILY_EXPONENT=13/14
AT_4BX_TWO_CELL_MIXED_FOURIER_BOUND_PROVED=false
```

## VARIABLE DICTIONARY

- `16/17` = older s7-09 conditional target before 4bx.
- `13/14` = conditional target at 4bx, later promoted by actual theorem proofs in s7-10/4by.

## USED BY

- Provenance for the prediction that became the current `13/14` theorem.
- Distinguishing a formerly conditional target from its later proof.

## DO NOT USE FOR

- Do not call the two-cell theorem open after merged s7-10/4by.
- Do not use this historical status instead of the current terminal ledger.

## PROVENANCE NOTES

Merged s7-10 closes the missing all-frequency `O(p)` theorem and merged 4by independently confirms it, so this conditional ledger is superseded by the proved current ledger.