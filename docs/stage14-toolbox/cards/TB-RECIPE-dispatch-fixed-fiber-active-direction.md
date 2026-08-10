# Dispatch fixed-fiber control to active-direction counting

```yaml
ID: TB-RECIPE-dispatch-fixed-fiber-active-direction
TYPE: RECIPE
STATUS: CURRENT
TITLE: Use fixed-fiber B^o(1) multiplicity only to expose the active-direction receiver
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-09
SOURCE_PR: 373
SOURCE_MERGE_SHA: 54aa839606d2ebeee8747837acec940da26a1534
SOURCE_FILES:
  - stages/stage14/14-s6-09/result.md
```

## INPUT

A fixed primitive direction or fixed reduced coordinate for which compatible partners are bounded by `B^o(1)`.

## OUTPUT

Replace the unresolved edge count by an active-base count up to subpolynomial multiplicity:

```text
A_phys(B) <= E_phys(B) <= A_phys(B)*B^o(1).
```

The next receiver is therefore the number of directions/bases supporting at least one compatible physical partner.

## VARIABLE DICTIONARY

- `A_phys(B)` = active primitive directions/bases.
- `E_phys(B)` = physical edges/incidences in the receiver.
- `B^o(1)` = fixed-fiber multiplicity, not a power saving in the number of active bases.

## USED BY

- Deciding when genus-one or fixed-squareclass multiplicity has done all it can.
- Preventing repeated work inside already-closed fibers.
- Moving attention to the support set that still controls the power exponent.

## DO NOT USE FOR

- Do not infer `A_phys(B)` is sparse from small fiber multiplicity.
- Do not multiply a fixed-fiber saving into a whole-family exponent without controlling the number of fibers.

## PROVENANCE NOTES

Merged s6-09 closes the fixed-direction analytic fiber and isolates active-direction counting as the remaining global receiver.