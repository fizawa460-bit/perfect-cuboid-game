# External theorem import preflight recipe

```yaml
ID: TB-RECIPE-external-theorem-import-preflight
TYPE: RECIPE
STATUS: CURRENT
TITLE: Mandatory hypothesis and transfer preflight before importing a literature theorem
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-10
SOURCE_PR: 425
SOURCE_MERGE_SHA: 1fca91407117c6cf486483b49299733bbbbbd519
SOURCE_FILES:
  - stages/stage14/14-s7-10/result.md
  - stages/stage14/14-4by/result.md
```

## INPUT

A theorem candidate and the exact Stage14 object it is intended to control.

## OUTPUT

A completed import ledger covering theorem locator, object map, hypotheses, uniformity, exceptions, bad primes, output scale, and post-theorem receiver transfer.

## VARIABLE DICTIONARY

Required checks include field/characteristic, moving dimension, character orders, divisor or Newton support, smoothness/SNC or nondegeneracy, monodromy, infinity, parameter chambers, exceptional parameters, uniformity, and constant dependence.

## USED BY

- Character-sum, large-sieve, geometry, or automorphic theorem imports.
- Review bundles that must distinguish theorem input from finite regression.

## DO NOT USE FOR

- Do not cite only a paper title when an exact theorem/corollary specialization is required.
- Do not skip exceptional frequencies or the transfer from complete sums to counted Stage14 objects.

## PROVENANCE NOTES

The checklist abstracts the explicit external-theorem contracts used independently in merged s7-10 and merged 4by.