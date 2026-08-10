# Dispatch local admissibility to a global witness

```yaml
ID: TB-RECIPE-dispatch-local-to-global-witness
TYPE: RECIPE
STATUS: CURRENT
TITLE: Stop local descent at admissibility and hand off only through a global witness
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s5f/result.md
  - stages/stage14/14-s6-01/result.md
```

## INPUT

A five-column local state that survives every odd-prime row and the exact `Q_2` covering test.

## OUTPUT

```text
LOCAL_ADMISSIBLE
  -> no global conclusion by itself
  -> if a global rational point is supplied by the physical problem,
     normalize it as Z=A/D^2, W=Y/D^3
  -> pass the resulting integral witness to the witness/kernel receivers.
```

The safe counting direction is physical hit -> global point -> integral witness.

## VARIABLE DICTIONARY

- `LOCAL_ADMISSIBLE` = all local tests pass.
- `A,D,Y` = primitive integral witness coordinates.
- `global point` = rational point actually supplied by the physical object, not inferred from local solubility.

## USED BY

- Ending the s5 local route cleanly.
- Preventing local character technology from being reused as an existence theorem.
- Entering the global-small-point chain at the correct quantifier level.

## DO NOT USE FOR

- `LOCAL_ADMISSIBLE => E(Q) nonempty` is not proved.
- Do not count all locally admissible packets as global witnesses without a separate majorant theorem.

## PROVENANCE NOTES

Merged s6-01 explicitly changes the primary problem from local admissibility to counting global small-point witnesses.