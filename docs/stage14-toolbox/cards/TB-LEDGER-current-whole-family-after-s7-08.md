# Current whole-family ledger after s7-08

```yaml
ID: TB-LEDGER-current-whole-family-after-s7-08
TYPE: LEDGER
STATUS: CURRENT
TITLE: Current whole-family exponent 18/19 and square-root gap after s7-08
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

```text
V(B) << B^(18/19+o(1)).
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19
IMPROVEMENT_OVER_20_21=2/399
CURRENT_REMAINING_GAP_TO_SQRT=17/38
```

Relative to the closed local `41/42` baseline, the cumulative direct post-local saving is

```text
41/42 - 18/19 = 23/798.
```

## VARIABLE DICTIONARY

- `V(B)` = current Stage14 physical whole-family count at the merged receiver boundary.
- `18/19` = whole-family exponent, not a single-sector exponent.
- `17/38` = remaining exponent gap to `1/2`.
- `23/798` = cumulative saving relative to the closed local `41/42` physical baseline.

## USED BY

- Any current exponent comparison or optimization.
- Deciding whether a new sector or receiver strictly improves the global ceiling.
- Superseding the former `20/21` current ledger without deleting its provenance.

## DO NOT USE FOR

- Do not claim `O(B^(1/2+epsilon))`; the remaining gap is positive.
- Historical `20/21`, `61/63`, and `41/42` checkpoints remain valid only in their recorded contexts.

## PROVENANCE NOTES

Merged s7-08 proves the first strict whole-family improvement below `20/21` by combining the 4bv thick-packet receiver with the shared-`xi` cell switch.