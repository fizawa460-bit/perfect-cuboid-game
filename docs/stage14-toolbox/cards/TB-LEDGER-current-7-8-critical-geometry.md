# Current 7/8 critical shared-label geometry

```yaml
ID: TB-LEDGER-current-7-8-critical-geometry
TYPE: LEDGER
STATUS: CURRENT
TITLE: Critical shared-label equality geometry at the current 7/8 whole-family checkpoint
SCOPE: BOTH
SOURCE_STAGE: Stage14-4cb
SOURCE_PR: 438
SOURCE_MERGE_SHA: 3fdad0c0673526ea39fed935b4ea69fcaf52a125
SOURCE_FILES:
  - stages/stage14/14-4cb/result.md
  - stages/stage14/14-s7-14/result.md
  - stages/stage14/14-s7-13/result.md
```

## INPUT

Merged s7-13 gives the current `7/8` theorem; merged 4cb and s7-14 compress its equality block to the shared squarefree label.

## OUTPUT

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
CURRENT_REMAINING_GAP_TO_SQRT=3/8
CRITICAL_XI_EXPONENT=3/4
CRITICAL_A_B_EXPONENT=3/8
CRITICAL_P_Q_EXPONENT=1/2
CRITICAL_X_Y_EXPONENT=1/16
```

with canonical form

```text
P=a*x^2,
Q=b*y^2,
xi=a*b.
```

## VARIABLE DICTIONARY

- `xi`: shared squarefree label `ab=cd`.
- `a,b`: squarefree coefficient pair of the short reduced coordinate.
- `x,y`: squarepart roots.

## USED BY

- Every next-receiver decision below the current `7/8` checkpoint.
- Critical-shell collision and realized-label sparsity stages.

## DO NOT USE FOR

- Do not claim all physical solutions have the equality exponents.
- The equality block is an exponent-critical architecture witness, not a density theorem.

## PROVENANCE NOTES

The card reorganizes merged equality geometry and does not strengthen the `7/8` theorem.