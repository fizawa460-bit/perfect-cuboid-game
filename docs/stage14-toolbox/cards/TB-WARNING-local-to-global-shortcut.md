# Local-to-global shortcut warning

```yaml
ID: TB-WARNING-local-to-global-shortcut
TYPE: WARNING
STATUS: CURRENT
TITLE: Local admissibility is not global rational solubility
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s5f/result.md
  - stages/stage14/14-s6-01/result.md
```

## INPUT
A five-column / odd-prime / Q2 packet passing every frozen local test.

## OUTPUT
Only `LOCALLY_ADMISSIBLE` is obtained. A global rational point or bounded-height integral witness remains an additional requirement.

## VARIABLE DICTIONARY
- local state = compatible p-adic/real data.
- global witness = rational point that can be integerized.

## USED BY
- Separating s5 local descent from s6 global small-point work.

## DO NOT USE FOR
- Do not infer a rational point from local admissibility.
- Do not infer a physical cuboid hit from a globally soluble relaxed packet without reconstruction.

## PROVENANCE NOTES
The s5 closure and s6-01 handoff are deliberately one-way: global witness implies local admissibility, not conversely.