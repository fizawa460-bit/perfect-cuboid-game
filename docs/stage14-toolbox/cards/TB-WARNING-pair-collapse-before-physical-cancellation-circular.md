# Pair collapse before physical/norm-index cancellation is circular

```yaml
ID: TB-WARNING-pair-collapse-before-physical-cancellation-circular
TYPE: WARNING
STATUS: CURRENT
TITLE: Do not collapse physical state pairs to cross-kernel coefficient energy before signed cancellation
SCOPE: BOTH
SOURCE_STAGE: Stage14-t50
SOURCE_PR: 439
SOURCE_MERGE_SHA: 72dd462552e64c312c13746f4533c5ef7512d52a
SOURCE_FILES:
  - stages/stage14/14-t49/result.md
  - stages/stage14/14-t50/result.md
```

## INPUT

A two-state/two-prime physical correlation before angular and norm-index cancellation has been exploited.

## OUTPUT

The required order is

```text
signed physical state sum
 -> t32 angular completion
 -> common-refinement and divisor-coupled norm-index aggregation
 -> product-kernel / Frobenius bookkeeping.
```

Collapsing ordered state pairs first to cross-kernel coefficient energy imports the unresolved fourth energy and is circular.

## VARIABLE DICTIONARY

- pair collapse: replacing signed state-level sums by multiplicities of product/cross-kernel classes too early.
- fourth energy: the unresolved higher collision energy that the route is trying to control rather than assume.

## USED BY

- t51/tH14 and any future bridge from Frobenius mean square to main/s collision energy.

## DO NOT USE FOR

- Do not Cauchy/collapse over direction or common-packet cells before the signed common refinement has received the relevant cancellation.

## PROVENANCE NOTES

Merged t49 identifies the circularity; merged t50 carries the same forbidden shortcut into the minimal two-modulus theorem contract.