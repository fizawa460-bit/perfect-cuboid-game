# Historical post-local square-root gap from 41/42

```yaml
ID: TB-LEDGER-post-local-sqrt-gap
TYPE: LEDGER
STATUS: SUPERSEDED
TITLE: Historical post-local saving required from 41/42 to square-root scale
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-00
SOURCE_PR: 341
SOURCE_MERGE_SHA: b4c9408441e501cb4d8f9a98b71f809d30a25f97
SOURCE_FILES:
  - stages/stage14/14-s6-00/result.md
EXPONENT_SCALE: physical B
EXPONENT_EXACT: 41/42
TARGET_EXACT: 1/2
SAVING_EXACT: 10/21
CONVERSION: 41/42 - 1/2 = 10/21
SUPERSEDED_BY: TB-LEDGER-current-main-after-4bq
```

## INPUT

- Closed local whole-family physical upper bound `B^(41/42+epsilon)` from Stage14-s5u.
- Target upper-bound scale `B^(1/2+epsilon)`.

## OUTPUT

At that historical checkpoint,

```text
41/42 - 1/2 = 10/21.
```

Thus `10/21` was the exact additional whole-family saving required before any direct post-local saving had been proved.

Merged Stage14-4bq later proves the improved whole-family exponent `61/63`, so this card is no longer the current gap ledger. Use `TB-LEDGER-current-main-after-4bq` for the current whole-family position.

## VARIABLE DICTIONARY

- `delta_gs` / `delta_post` = additional physical `B`-scale post-local saving beyond the closed s5 input.
- `10/21` = historical missing exponent from `41/42` to `1/2`.

## USED BY

- Reconstructing threshold choices in Stage14-4bj and s6 stages that were frozen while `41/42` was the active whole-family exponent.
- Historical provenance for denominator/radical/incidence critical scales.

## DO NOT USE FOR

- Do not report `10/21` as the current remaining whole-family gap after merged 4bq.
- Do not rewrite historical stages whose valid thresholds were defined relative to the then-current `41/42` ledger.
- A structural variable forced to have size `B^(10/21)` does not itself yield a `B^(-10/21)` counting gain.

## PROVENANCE NOTES

Stage14-s6-00 froze this budget after importing the closed s5u exponent. Merged Stage14-4bq later proves `V(B)<<B^(61/63+o(1))`, superseding this card only as the current global exponent ledger, not invalidating historical threshold calculations.