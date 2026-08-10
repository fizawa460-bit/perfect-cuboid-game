# Current main-track exponent after diagonal-pair genus-one closure

```yaml
ID: TB-LEDGER-current-main-after-4bq
TYPE: LEDGER
STATUS: CURRENT
TITLE: Current whole-family exponent 61/63 and remaining square-root gap after 4bq
SCOPE: MAIN
SOURCE_STAGE: Stage14-4bq
SOURCE_PR: 395
SOURCE_MERGE_SHA: aa21a3604cf72e06f797c8ba2ecff96b49e60f44
SOURCE_FILES:
  - stages/stage14/14-4bq/result.md
EXPONENT_SCALE: physical B
PREVIOUS_EXPONENT_EXACT: 41/42
CURRENT_EXPONENT_EXACT: 61/63
POST_LOCAL_SAVING_EXACT: 1/126
TARGET_EXACT: 1/2
REMAINING_GAP_EXACT: 59/126
```

## INPUT

Merged exhaustive main-track sectors after 4bq:

```text
small partner leg:  B^(20/21+o(1)),
cross branch:       B^(61/63+o(1)),
good-cell residual: B^(13/14+o(1)).
```

## OUTPUT

The maximum exponent is

```text
61/63.
```

Therefore

```text
V(B) << B^(61/63+o(1)).
```

Relative to the previous `41/42` whole-family bound,

```text
41/42 - 61/63 = 1/126.
```

This is the first proved positive whole-family direct post-local saving. The remaining gap to square-root scale is

```text
61/63 - 1/2 = 59/126.
```

The active exponent bottleneck at this checkpoint is the cross branch `61/63`.

## VARIABLE DICTIONARY

- `1/126` = already-proved whole-family post-local saving relative to `41/42`.
- `59/126` = remaining whole-family exponent reduction needed to reach `1/2` from `61/63`.

## USED BY

- Current main-track exponent comparisons after 4bq.
- Deciding whether a new sector theorem actually improves the whole-family maximum.
- Preventing continued use of `10/21` as the current remaining gap after the first full post-local saving.

## DO NOT USE FOR

- `61/63` is not a square-root theorem.
- `1/126` is already achieved saving, not remaining saving.
- The historical `10/21` scale remains valid inside stages that explicitly froze thresholds relative to `41/42`; it is merely superseded as the current whole-family gap ledger.

## PROVENANCE NOTES

Merged PR #395 recombines the exhaustive sectors and proves the exact ledger `61/63`, `1/126`, and `59/126`.