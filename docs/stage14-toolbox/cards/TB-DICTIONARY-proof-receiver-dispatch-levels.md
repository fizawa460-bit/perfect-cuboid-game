# Proof receiver dispatch levels

```yaml
ID: TB-DICTIONARY-proof-receiver-dispatch-levels
TYPE: DICTIONARY
STATUS: CURRENT
TITLE: Canonical Stage14 main/s proof-receiver levels and legal handoffs
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-08
SOURCE_PR: 417
SOURCE_MERGE_SHA: 29e08fea3ebc1838fde2418957b9c0490456e1b1
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
  - stages/stage14/14-s6-02/result.md
  - stages/stage14/14-s6-09/result.md
  - stages/stage14/14-s7-07/result.md
  - stages/stage14/14-s7-08/result.md
  - stages/stage14/14-4bv/result.md
```

## INPUT

Any proved Stage14 main/s statement that must be routed into the next counting argument.

## OUTPUT

Use the following receiver levels, in order of increasing quantifier scope:

```text
L0 local state / character row
L1 global rational witness
L2 integral witness coordinate
L3 fixed signed kernel packet
L4 fixed curve / fixed fiber
L5 physical edge / transferred face pair
L6 active direction / reduced-coordinate base
L7 restricted square-part or coefficient sector
L8 whole physical family
```

A result may move only to the same level or to the next level for which an explicit merged transfer theorem is available.

## VARIABLE DICTIONARY

- `receiver` = the next theorem interface that consumes a proved object.
- `handoff` = a proved implication preserving the required physical image and counting multiplicity.
- `L0..L8` = quantifier levels, not chronological stages.

## USED BY

- Selecting the next proof tool without rereading the full route history.
- Checking whether a local, coordinate, fiber, or sector saving is globally usable.
- Building dependency graphs for main and s.

## DO NOT USE FOR

- Do not infer that every level is reachable from every previous level.
- Do not treat a structural identity as a counting transfer.
- Do not skip the physical-image or moving-family multiplicity checks.

## PROVENANCE NOTES

The level ordering packages the merged quantifier boundaries through s6/s7 and the first merged whole-family recombination below `20/21` in s7-08.