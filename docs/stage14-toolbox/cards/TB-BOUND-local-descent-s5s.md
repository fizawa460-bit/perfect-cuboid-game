# Conservative local descent bound at s5s

```yaml
ID: TB-BOUND-local-descent-s5s
TYPE: BOUND
STATUS: SUPERSEDED
TITLE: Conservative s5 local-descent saving 1/200 on Euclid scale
SCOPE: BOTH
SOURCE_STAGE: Stage14-s5s
SOURCE_PR: 328
SOURCE_MERGE_SHA: 3cbdde9bc94c55c63f72946805d3315e83c35097
SOURCE_FILES:
  - stages/stage14/14-s5s/result.md
SUPERSEDED_BY: TB-BOUND-local-descent-s5t
EXPONENT_SCALE: M and physical B
SAVING_EXACT: 1/200 on M-scale
CONVERSION: M<=sqrt(B)
```

## INPUT

- The actual locally-soluble s5 descent system on regular Euclid boxes.
- Euclid scale `M` and physical cutoff `M<=sqrt(B)`.
- One-sided upper-bound use: a physical hit gives a globally soluble class, hence a locally soluble class.

## OUTPUT

```text
N_loc(M) << M^(2-1/200+epsilon)
#Q_B^phys << B^(399/400+epsilon)
```

The physical saving relative to exponent `1` is `1/400`.

## VARIABLE DICTIONARY

- `M` = Euclid-parameter scale.
- `B` = physical height / space-diagonal cutoff.
- `N_loc(M)` = locally-soluble descent-class count.

## USED BY

- Historical exponent-chain audits.
- Checking scale conversions in later main/s imports.

## DO NOT USE FOR

- Do not use `1/200` as the current local saving.
- Do not reverse locally soluble => globally soluble.
- Do not compare an `M`-scale saving directly with a `B`-scale saving without conversion.

## PROVENANCE NOTES

Stage14-s5t showed this saving was conservative bookkeeping rather than a structural wall and improved the same normalized local problem to `1/41`.
