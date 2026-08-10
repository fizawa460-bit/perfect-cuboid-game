# Historical main-track exponent after diagonal-pair genus-one closure

```yaml
ID: TB-LEDGER-current-main-after-4bq
TYPE: LEDGER
STATUS: SUPERSEDED
TITLE: Historical whole-family exponent 61/63 and square-root gap after 4bq
SCOPE: MAIN
SOURCE_STAGE: Stage14-4bq
SOURCE_PR: 395
SOURCE_MERGE_SHA: aa21a3604cf72e06f797c8ba2ecff96b49e60f44
SOURCE_FILES:
  - stages/stage14/14-4bq/result.md
EXPONENT_SCALE: physical B
PREVIOUS_EXPONENT_EXACT: 41/42
CURRENT_AT_SOURCE_EXACT: 61/63
POST_LOCAL_SAVING_AT_SOURCE_EXACT: 1/126
TARGET_EXACT: 1/2
REMAINING_GAP_AT_SOURCE_EXACT: 59/126
SUPERSEDED_BY: TB-LEDGER-current-main-after-4br
```

## INPUT

Merged exhaustive main-track sectors at the 4bq checkpoint:

```text
small partner leg:  B^(20/21+o(1)),
cross branch:       B^(61/63+o(1)),
good-cell residual: B^(13/14+o(1)).
```

## OUTPUT

At that checkpoint the maximum exponent was

```text
61/63,
```

so

```text
V(B) << B^(61/63+o(1)).
```

Relative to `41/42`, the newly proved direct post-local saving was

```text
41/42 - 61/63 = 1/126,
```

and the remaining square-root gap was

```text
61/63 - 1/2 = 59/126.
```

Merged Stage14-4br later improves the cross branch and whole-family exponent to `20/21`, so this is now a historical checkpoint ledger.

## VARIABLE DICTIONARY

- `1/126` = post-local saving proved at the 4bq checkpoint.
- `59/126` = remaining gap at the 4bq checkpoint.

## USED BY

- Reconstructing the first full post-local improvement.
- Provenance for the 4bq genus-one good-cell closure.
- Comparing the later 4br threshold optimization against its immediate predecessor.

## DO NOT USE FOR

- Do not report `61/63` as the current whole-family exponent after merged 4br.
- Do not report `59/126` as the current remaining square-root gap.
- The `13/14` good-cell residual bound itself remains current as a sector theorem unless separately superseded.

## PROVENANCE NOTES

Merged PR #395 proves `61/63`, `1/126`, and `59/126`. Merged PR #396 later supersedes this card as the current global exponent ledger without invalidating the 4bq geometry or good-cell residual theorem.