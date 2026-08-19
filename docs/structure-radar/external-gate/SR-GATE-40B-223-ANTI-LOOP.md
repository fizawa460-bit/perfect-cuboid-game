# StructureRadar batch 40B — SR-STR-223 anti-loop precheck

## Live endpoint

`SR-STR-223` remains an `EXTERNAL_GATE` for moving compatible small-point / fiber-product family control.

Merged StructureRadar provenance preserves the essential firewall: fixed-fiber geometry, local surjectivity, finite diagnostics, or subpolynomial per-fiber multiplicity do not imply a family-level fixed-power saving for the moving compatible-small-point locus. Arsenal classification #1195 therefore retained this card as an external gate.

## Dependency / duplication check

This lane is adjacent to, but not identical with, `SR-STR-162`.

- `SR-STR-162` asks for frequency control for a first small point in the thin Pythagorean family.
- `SR-STR-223` asks for compatible small-point control in a moving paired/fiber-product geometry.

A proof of the 162 endpoint would not by itself prove the 223 compatibility theorem, and the existing 223 fixed-fiber geometry does not prove 162. They must not be counted as independent savings or used to justify one another.

## Anti-loop decision

`ANTI_LOOP_STATE=THEOREM_GATE_PAUSED`

No new merged identity, exact family-counting theorem, strict receiver weakening, or exact source/range match removes the family-level compatibility obstruction. Further subdivision into another moving-small-point adapter would only repackage the same missing fixed-power theorem.

## Frozen boundary

```text
SR_STR_223_STATUS=EXTERNAL_GATE
ANTI_LOOP_STATE=THEOREM_GATE_PAUSED
FROZEN_ENDPOINT=MovingCompatibleSmallPointFiberProductFamilyControl
SR_STR_162_IS_NOT_A_SUBSTITUTE=true
FIXED_FIBER_TO_MOVING_FAMILY_PROMOTION=false
NEW_FIXED_POWER_SAVING=false
GATE_CLOSED=false
```

Reopen only on new merged proof evidence, an exact family-uniform theorem/range match, a focused Work result, or explicit operator override.

No whole-family exponent improvement and no perfect-cuboid existence/nonexistence claim is made.
