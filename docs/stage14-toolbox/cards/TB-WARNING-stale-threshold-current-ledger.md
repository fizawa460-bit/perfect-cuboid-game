# Historical threshold versus current ledger warning

```yaml
ID: TB-WARNING-stale-threshold-current-ledger
TYPE: WARNING
STATUS: CURRENT
TITLE: Historical thresholds remain valid in context but are not the current whole-family gap
SCOPE: BOTH
SOURCE_STAGE: Stage14-4br
SOURCE_PR: 396
SOURCE_MERGE_SHA: 01afa63539e32e62070a84927bbc0530241a79e9
SOURCE_FILES:
  - stages/stage14/14-s6-00/result.md
  - stages/stage14/14-4bq/result.md
  - stages/stage14/14-4br/result.md
```

## INPUT
A threshold or required saving frozen at an earlier whole-family checkpoint, such as `10/21` relative to `41/42`.

## OUTPUT
Keep the historical arithmetic attached to its source stage, but consult the CURRENT exponent ledger before using language such as `remaining gap`, `current saving required`, or `whole-family exponent`.

## VARIABLE DICTIONARY
- historical threshold = correct number for an earlier decomposition/checkpoint.
- current ledger = latest merged whole-family exponent and current gap to the target.

## USED BY
- Reusing old lemmas after main-track exponent improvements.

## DO NOT USE FOR
- Do not silently replace the provenance of an old threshold.
- Do not call an old `10/21` requirement the current gap after the whole-family exponent moved to `20/21`.

## PROVENANCE NOTES
Merged 4br improves the whole-family exponent to `20/21`, while older stages retain their internally correct `41/42`-based thresholds.