# Proved versus conditional recipe status

```yaml
ID: TB-WARNING-proved-vs-conditional-recipe-status
TYPE: WARNING
STATUS: CURRENT
TITLE: Never promote a conditional receiver optimization to the current theorem ledger
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bx
SOURCE_PR: 422
SOURCE_MERGE_SHA: 6774b9b6fb662cb14cc221c0b56bb74c077a3659
SOURCE_FILES:
  - stages/stage14/14-s7-09/result.md
  - stages/stage14/14-4bx/result.md
```

## INPUT

A research recipe whose algebraic reduction is proved but whose analytic receiver still depends on an unproved uniform estimate.

## OUTPUT

A mandatory status label: the optimized exponent remains `CONDITIONAL` and cannot supersede the terminal CURRENT theorem ledger.

## VARIABLE DICTIONARY

- `PROVED` = all theorem gates and exhaustive recombination are merged.
- `CONDITIONAL` = one or more explicitly named theorem gates remain open.
- current proved exponent = `15/16`.
- historical s7-09 conditional target = `16/17`.
- updated conditional target after 4bx = `13/14`.

## USED BY

- Cookbook maintenance.
- External theorem imports and hypothesis checks.
- Preventing finite computational evidence from silently becoming a theorem.

## DO NOT USE FOR

- Do not write `CURRENT=13/14` unless the two-cell mixed Fourier theorem and full transfer are actually proved and merged.
- Do not treat a candidate literature theorem as imported until every required hypothesis is checked.

## PROVENANCE NOTES

Merged 4bx proves `15/16`, improves the conditional two-cell target to `13/14`, and explicitly keeps `S7_09_TWO_CELL_MIXED_FOURIER_BOUND_PROVED=false`.