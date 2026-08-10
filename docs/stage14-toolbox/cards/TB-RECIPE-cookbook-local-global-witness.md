# Local-to-global witness cookbook

```yaml
ID: TB-RECIPE-cookbook-local-global-witness
TYPE: RECIPE
STATUS: CURRENT
TITLE: Checklist for stopping local descent and entering the global witness receiver
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s5f/result.md
  - stages/stage14/14-s6-01/result.md
```

## INPUT

An orientation-normalized Stage14 local covering state with all odd rows and the `Q_2` Kummer image checked.

## OUTPUT

A checklist boundary: `LOCAL_ADMISSIBLE` remains at receiver level `L0`; level `L1` is reached only when a merged global theorem constructs the rational witness.

## VARIABLE DICTIONARY

- `L0` = local state / character row.
- `L1` = global rational witness.
- `LOCAL_ADMISSIBLE` = necessary local condition, not a rational point.

## USED BY

- Any new main/s stage that starts from five-column local data.
- Preventing local character conditions from being reused as a global parameterization.

## DO NOT USE FOR

- Do not infer global solubility from local admissibility.
- Do not silently swap the historical `S/X` orientation when importing s5 rows.

## PROVENANCE NOTES

Merged s6-01 is the explicit global-witness handoff boundary used by the toolbox.