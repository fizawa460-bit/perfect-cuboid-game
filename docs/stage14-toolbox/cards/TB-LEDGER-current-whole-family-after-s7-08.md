# Historical whole-family ledger after s7-08

```yaml
ID: TB-LEDGER-current-whole-family-after-s7-08
TYPE: LEDGER
STATUS: SUPERSEDED
SUPERSEDED_BY: TB-LEDGER-current-whole-family-after-4bx
TITLE: Historical whole-family exponent 18/19 and square-root gap after s7-08
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-08
SOURCE_PR: 417
SOURCE_MERGE_SHA: 29e08fea3ebc1838fde2418957b9c0490456e1b1
SOURCE_FILES:
  - stages/stage14/14-s7-08/result.md
```

## INPUT

The merged exhaustive s7-08 recombination with

```text
lambda=9/19,
tau=2/19,
theta=8/19.
```

## OUTPUT

At the s7-08 checkpoint:

```text
V(B) << B^(18/19+o(1)).
HISTORICAL_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19
IMPROVEMENT_OVER_20_21=2/399
HISTORICAL_REMAINING_GAP_TO_SQRT=17/38
```

Relative to the closed local `41/42` baseline:

```text
41/42 - 18/19 = 23/798.
```

## VARIABLE DICTIONARY

- `18/19` = proved whole-family exponent at the s7-08 checkpoint.
- `17/38` = historical remaining gap at that checkpoint.
- `23/798` = saving from the closed local baseline at that checkpoint.

## USED BY

- Historical provenance for the first strict improvement below `20/21`.
- The one-cell recipe still reused inside later 4bx.
- Comparing the later `15/16` improvement against its predecessor.

## DO NOT USE FOR

- Do not call `18/19` current after merged 4bx.
- Do not claim square-root scale.

## PROVENANCE NOTES

Merged s7-08 remains the canonical first source of `18/19`; merged 4bx later supersedes it as the current whole-family ledger while reusing its one-cell thin receiver.