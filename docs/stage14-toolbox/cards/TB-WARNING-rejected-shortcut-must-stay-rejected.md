# Rejected theorem shortcuts stay rejected

```yaml
ID: TB-WARNING-rejected-shortcut-must-stay-rejected
TYPE: WARNING
STATUS: CURRENT
TITLE: A failed theorem specialization cannot be revived by relabeling the same hypotheses
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-10
SOURCE_PR: 425
SOURCE_MERGE_SHA: 1fca91407117c6cf486483b49299733bbbbbd519
SOURCE_FILES:
  - stages/stage14/14-s7-10/result.md
```

## INPUT

A proposed external theorem specialization for which a required hypothesis has been proved false.

## OUTPUT

Status `REJECTED`, together with the exact failed hypothesis and the different theorem route, if any, that replaces it.

## VARIABLE DICTIONARY

For the live two-cell detector, the direct Katz 2007 nonsingular-polynomial shortcut fails because the highest homogeneous part contains repeated factors `R^2 S^2`.

## USED BY

- Preventing later stages from re-importing an already-audited invalid shortcut.
- Distinguishing a rejected specialization from a rejected theorem family.

## DO NOT USE FOR

- Rejection of one specialization does not reject every theorem in the same paper or author family.
- A later import requires a genuinely different theorem statement or a newly proved hypothesis map.

## PROVENANCE NOTES

Merged s7-10 freezes `DIRECT_KATZ_2007_DELIGNE_POLYNOMIAL_SHORTCUT_APPLICABLE=false` and replaces it with an SNC stationary-phase route.