# Finite regression is not an external theorem import

```yaml
ID: TB-WARNING-finite-regression-not-theorem-import
TYPE: WARNING
STATUS: CURRENT
TITLE: Small-prime and symbolic regressions diagnose hypotheses but do not prove uniform asymptotics
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-10
SOURCE_PR: 425
SOURCE_MERGE_SHA: 1fca91407117c6cf486483b49299733bbbbbd519
SOURCE_FILES:
  - stages/stage14/14-s7-10/result.md
  - stages/stage14/14-4by/result.md
```

## INPUT

Finite-field enumerations, small-prime trace tables, symbolic discriminants, or finite nondegeneracy checks accompanying an external theorem application.

## OUTPUT

A deterministic regression/hypothesis diagnostic only. The uniform theorem conclusion must still come from the imported theorem plus the proved hypothesis map.

## VARIABLE DICTIONARY

- `finite regression`: reproducibility and bug-detection evidence.
- `uniform theorem`: a statement valid over the required asymptotic family with controlled constants.

## USED BY

- CI design for theorem-import stages.
- Adversarial review distinguishing exact algebra checks from asymptotic inputs.

## DO NOT USE FOR

- Do not promote an observed `O(p)` envelope on finitely many primes to a uniform `O(p)` theorem.
- Do not replace a monodromy/nondegeneracy proof by a finite sample.

## PROVENANCE NOTES

Merged s7-10 and 4by both retain small-prime regressions while explicitly using external theorems for the uniform estimate.