# Theorem-name match is not a hypothesis match

```yaml
ID: TB-WARNING-theorem-name-match-not-hypothesis-match
TYPE: WARNING
STATUS: CURRENT
TITLE: A desired conclusion or familiar theorem family does not certify the live specialization
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-10
SOURCE_PR: 425
SOURCE_MERGE_SHA: 1fca91407117c6cf486483b49299733bbbbbd519
SOURCE_FILES:
  - stages/stage14/14-s7-10/result.md
  - stages/stage14/14-4by/result.md
```

## INPUT

A literature theorem whose advertised conclusion resembles the needed Stage14 bound.

## OUTPUT

No import until every required hypothesis, uniformity parameter, exceptional stratum, and receiver transfer is explicitly mapped.

## VARIABLE DICTIONARY

`conclusion match` and `hypothesis match` are separate checks. The latter controls import legality.

## USED BY

- Literature search handoffs.
- Adversarial review of external theorem dependencies.

## DO NOT USE FOR

- Do not write “by Deligne/Katz/large sieve” as a proof step without the exact specialization contract.
- Do not infer uniformity from a theorem stated for one fixed object.

## PROVENANCE NOTES

Merged s7-10 rejects one tempting Katz shortcut even though its desired conclusion has the correct `O(p)` scale, while s7-10 and 4by validate different theorem routes by full hypothesis checks.