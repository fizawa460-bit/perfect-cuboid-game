# StageA1 A1-7 — proposed integration verdict

## Proposed verdict

```text
PROPOSED_STAGE_A1_VERDICT=NEW_FAMILY_EXCLUSION
```

This verdict is submitted together with A1-6 and is not final until independent audit passes.

## Why this category fits

StageA1 has produced rigorous family-specific mathematics:

- A1-2 excludes anchored nondegenerate members of the displayed Theorem 1.5 and Theorem 1.6 Hilbert-cube families;
- A1-3 gives the corrected equation-(6) anchor boundary and proves that this parametrization is not a universal reverse map for arbitrary anchored cubes;
- A1-4 identifies a positive-rank genus-1 quotient, the exact first-two-cover receiver, a height-5000 zero-survivor computation, and the fixed-prime divisibility sieve;
- A1-5 converts that receiver to a primitive Pythagorean descent and eliminates the `g=2,3` branches, leaving only `g=1,6`;
- A1-6 proves that the A1-4 trivial-reduction prime list is complete, that its nonvacuous primes are p-adically saturated, and that the nondegenerate first-two-cover curve is everywhere locally soluble.

The correct integration category is therefore `NEW_FAMILY_EXCLUSION`, not `RECONNAISSANCE_NEGATIVE`: StageA1 did rigorously exclude explicit published dimension-3 Hilbert-cube families at the anchor and derived additional exact arithmetic structure on the larger equation-(6) boundary.

## Why the stronger categories do not fit

### Not `NEW_GENERAL_CONSTRAINT`

No StageA1 statement has been proved necessary for every perfect cuboid. The dimension argument in A1-3 explicitly blocks that promotion: equation (6) is not a proved universal parametrization of the full anchored-cube variety.

### Not `NEW_STAGE27_WEAPON`

No exact adapter currently maps the family-specific A1-5/A1-6 receiver into a Stage27 receiver for arbitrary perfect cuboids. Stage27 and StructureRadar remain unchanged.

### Not a perfect-cuboid existence/nonexistence result

The general equation-(6) boundary is not globally closed. The first-two-cover curve is everywhere locally soluble, so the remaining obstruction is genuinely global.

## Frozen external wall

If audit accepts A1-6, the productive elementary/local reconnaissance has reached a natural endpoint. The unresolved wall is:

```text
GLOBAL_WALL = rational points on the everywhere-locally-soluble
              first-two-cover / reconstruction-cover tower for the
              corrected equation-(6) anchor family.
```

A future reopening should require one of:

- a theorem or exact computational method that determines the relevant rational points;
- a new Jacobian/cover decomposition that materially lowers the global problem;
- a proved coverage/reverse-map theorem connecting this family to arbitrary anchored cubes;
- an exact adapter into another already-proved receiver.

Merely increasing the rational search bound, scanning more primes of the already-completed trivial-reduction type, or rewriting the same `g=1,6` descent is not a reopening condition.

## Proposed transition after audit

If the independent audit passes without a substantive repair:

```text
STAGE_A1_STATUS=CLOSED_NEW_FAMILY_EXCLUSION
STOP_AFTER_AUDIT=true
NEXT_EXPECTED_COMMAND=NONE
```

If audit finds that A1-6's completeness or local-solubility claim fails, this integration verdict must be withdrawn and repaired before closure.

## Firewalls

```text
A1_7_PROPOSED_VERDICT=NEW_FAMILY_EXCLUSION
NEW_GENERAL_CONSTRAINT=false
NEW_STAGE27_WEAPON=false
EQUATION6_GLOBAL_EXCLUSION=false
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
STAGE27_STRUCTURE_RADAR_CHANGED=false
AUDIT_REQUIRED=true
```
