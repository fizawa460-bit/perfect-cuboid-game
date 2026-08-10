# Automatic square-factor double-count warning

```yaml
ID: TB-WARNING-automatic-square-factor-double-count
TYPE: WARNING
STATUS: CURRENT
TITLE: Do not charge a gcd cell twice after it becomes an automatic square factor
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-08
SOURCE_PR: 369
SOURCE_MERGE_SHA: e9916a9e21dc305fa30e240d3db962a26af1653b
SOURCE_FILES:
  - stages/stage14/14-s6-08/result.md
```

## INPUT
The four good gcd cells have already been extracted from the raw cross-square detector.

## OUTPUT
Their product enters as a square factor, so the residual condition is the normalized same-kernel/square condition. The extracted gcd size is not a new independent sieve constraint.

## VARIABLE DICTIONARY
- raw detector = pre-normalization square equation.
- normalized residual = equation after automatic square factors are removed.

## USED BY
- Preventing repeated `large q => 1/q` charges.

## DO NOT USE FOR
- Do not claim a fresh density saving solely from a large gcd cell that already divides the square detector with even valuation.
- A new saving requires a condition remaining after normalization.

## PROVENANCE NOTES
s6-08 proves the full good-gcd product is an automatic square prefactor and explicitly rejects the naive repeated gcd-cell saving.