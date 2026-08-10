# Barrier-obstruction atlas status vocabulary

```yaml
ID: TB-DICTIONARY-obstruction-atlas-status
TYPE: DICTIONARY
STATUS: CURRENT
TITLE: Status vocabulary for current, closed, live, bridge, support, and forbidden Stage14 obstructions
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-14
SOURCE_PR: 437
SOURCE_MERGE_SHA: 31c3636016f5f0ff80133f0c1b6a9cbbd91a3697
SOURCE_FILES:
  - stages/stage14/14-s7-14/result.md
  - stages/stage14/14-4cb/result.md
  - stages/stage14/14-t50/result.md
```

## INPUT

Merged s7-14, 4cb, and t50 distinguish solved obstructions, audited dead ends, direct live theorem targets, support-route targets, and invalid shortcuts.

## OUTPUT

The atlas-only vocabulary

```text
CURRENT_CHECKPOINT
HISTORICAL_ARCHITECTURE
CLOSED_POSITIVE
CLOSED_NEGATIVE
LIVE_PRIMARY
LIVE_BRIDGE
SUPPORT_TRIGGERED
FORBIDDEN
```

is frozen for barrier triage. These labels do not replace canonical card `STATUS` values.

## VARIABLE DICTIONARY

- `LIVE_PRIMARY`: a theorem with a merged direct sufficient contract for a new main/s saving.
- `LIVE_BRIDGE`: useful receiver on another exact object; operator/quantifier bridge still required.
- `CLOSED_NEGATIVE`: route rigorously shown insufficient under its frozen ingredients.
- `FORBIDDEN`: invalid or circular shortcut.

## USED BY

- `barrier-obstruction-atlas.md`.
- `next-receiver-selector.md`.
- Future stages deciding whether a proposed route is new work or a reopened closed path.

## DO NOT USE FOR

- Do not reinterpret `CLOSED_NEGATIVE` as mathematical impossibility under stronger future hypotheses.
- Do not promote `LIVE_BRIDGE` to a main/s theorem without the recorded bridge.

## PROVENANCE NOTES

The vocabulary only classifies merged obstruction statements; it adds no theorem.