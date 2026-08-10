# Fixed-fiber to active-direction cookbook

```yaml
ID: TB-RECIPE-cookbook-fixed-fiber-active-direction
TYPE: RECIPE
STATUS: CURRENT
TITLE: Checklist for using fixed-fiber multiplicity without inventing active-direction sparsity
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-09
SOURCE_PR: 373
SOURCE_MERGE_SHA: 54aa839606d2ebeee8747837acec940da26a1534
SOURCE_FILES:
  - stages/stage14/14-s6-09/result.md
```

## INPUT

A fixed-curve/fiber theorem giving subpolynomial or otherwise controlled partner multiplicity.

## OUTPUT

An explicit handoff to the still-moving active direction/base receiver, with no global count asserted until that family is independently controlled.

## VARIABLE DICTIONARY

- `L4` = fixed curve/fiber.
- `L6` = active direction/base.
- fixed-fiber multiplicity and active-direction count are separate factors.

## USED BY

- Any stage attempting to multiply a fiber bound by a direction/base count.
- Detecting the missing moving-family factor before claiming a power saving.

## DO NOT USE FOR

- `B^o(1)` partners per fixed direction does not imply only `B^o(1)` active directions.
- Do not skip from `L4` to `L8` without a merged transfer.

## PROVENANCE NOTES

Merged s6-09 records exactly this quantifier boundary.