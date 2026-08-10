# Proved versus conditional recipe status

```yaml
ID: TB-WARNING-proved-vs-conditional-recipe-status
TYPE: WARNING
STATUS: CURRENT
TITLE: Never promote a conditional receiver optimization to the current theorem ledger
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-09
SOURCE_PR: 419
SOURCE_MERGE_SHA: dcfe86c8002b8f403fe3f35315bf71288f8be875
SOURCE_FILES:
  - stages/stage14/14-s7-08/result.md
  - stages/stage14/14-s7-09/result.md
```

## INPUT

A research recipe whose algebraic reduction is proved but whose analytic receiver still depends on an unproved uniform estimate.

## OUTPUT

A mandatory status label: the derived optimized exponent remains `CONDITIONAL` and cannot supersede the terminal CURRENT ledger.

## VARIABLE DICTIONARY

- `PROVED` = all theorem gates and exhaustive recombination are merged.
- `CONDITIONAL` = one or more explicitly named theorem gates remain open.
- current proved exponent = `18/19`.
- s7-09 conditional exponent = `16/17`.

## USED BY

- Cookbook maintenance.
- External theorem imports and hypothesis checks.
- Preventing finite computational evidence from silently becoming a theorem.

## DO NOT USE FOR

- Do not write `CURRENT=16/17` unless the mixed Fourier theorem and full transfer are actually proved and merged.
- Do not treat a candidate literature theorem as imported until every required hypothesis is checked.

## PROVENANCE NOTES

Merged s7-09 explicitly states `ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=false` and keeps `18/19` current.