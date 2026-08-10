# External theorem import status dictionary

```yaml
ID: TB-DICTIONARY-external-theorem-import-status
TYPE: DICTIONARY
STATUS: CURRENT
TITLE: CANDIDATE, HYPOTHESIS_MAPPED, REJECTED, and IMPORTED theorem states
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-10
SOURCE_PR: 425
SOURCE_MERGE_SHA: 1fca91407117c6cf486483b49299733bbbbbd519
SOURCE_FILES:
  - stages/stage14/14-s7-10/result.md
  - stages/stage14/14-4by/result.md
```

## INPUT

A literature theorem proposed as an input to a Stage14 receiver.

## OUTPUT

Exactly one status:

```text
CANDIDATE -> HYPOTHESIS_MAPPED -> IMPORTED
                             \-> REJECTED
```

## VARIABLE DICTIONARY

- `CANDIDATE`: theorem located; specialization not yet checked.
- `HYPOTHESIS_MAPPED`: every theorem hypothesis has a Stage14 counterpart or explicit open gate.
- `REJECTED`: a required hypothesis fails for the proposed specialization.
- `IMPORTED`: all required hypotheses, exception strata, uniformity, and receiver transfer are certified.

## USED BY

- Every future literature-theorem import.
- Distinguishing a failed shortcut from an open research candidate.

## DO NOT USE FOR

- A desired conclusion does not imply `IMPORTED`.
- `REJECTED` may not be silently reset without a genuinely different specialization or new hypothesis proof.

## PROVENANCE NOTES

Merged s7-10 simultaneously records an imported Katz--Laumon route and an explicitly rejected Katz 2007 shortcut; merged 4by supplies an independent imported Lei Fu route.