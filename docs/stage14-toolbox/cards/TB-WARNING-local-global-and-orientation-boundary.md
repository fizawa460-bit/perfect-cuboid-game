# Local/global and orientation boundary

```yaml
ID: TB-WARNING-local-global-and-orientation-boundary
TYPE: WARNING
STATUS: CURRENT
TITLE: Do not reverse local implications or silently swap S/X orientation
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s5c/result.md
  - stages/stage14/14-s5f/result.md
  - stages/stage14/14-s6-01/result.md
```

## INPUT

Any attempt to move between local s5 character rows, later s6 global witness packets, or five-column notation.

## OUTPUT

Only the following implication is safe without an additional theorem:

```text
physical hit
 -> global small-point witness
 -> globally soluble descent class
 -> locally admissible character state.
```

Also enforce the orientation adapter:

```text
historical s5:
  S=m^2-n^2, X=2mn

s6-01 packetization:
  S=2mn, X=m^2-n^2.
```

The five Euclid columns are the same, but `S/X` row labels are not.

## VARIABLE DICTIONARY

- `local admissible` = passes every odd and Q2 local covering test.
- `globally soluble` = contains a rational point on the covering; strictly stronger.
- `physical hit` = satisfies the Stage14 physical reconstruction constraints; stronger again.

## USED BY

- Preventing accidental `Selmer = Mordell-Weil` reasoning.
- Transporting s5 local rows into later s6/main notation.
- Reviewing character or density arguments that use five-column support.

## DO NOT USE FOR

Never assert any of:

```text
local admissible => globally soluble
globally soluble => physical hit
nonempty local/Selmer state => small rational point
same five columns => same S/X row labels
selected X row automatic for p==3 mod4
large local-density saving => post-local global/height saving
```

## PROVENANCE NOTES

- PR #229 closes the local system only.
- PR #345 explicitly uses local solubility as a one-sided positive majorant for physical/global witnesses and retains the global-small-point problem beyond it.
- The s5/s6 orientation mismatch is mathematical notation, not a contradiction; toolbox-ae makes the required adapter explicit.
