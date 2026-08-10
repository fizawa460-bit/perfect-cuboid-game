# Stage14-toolbox-ak — proof receiver dispatch and lemma dependency map

## Purpose

Turn the accumulated Stage14 toolbox into an executable research interface: given a proved object, identify the next legal proof receiver, the required quantifier handoff, and the current whole-family ledger.

No new mathematical theorem is owned by toolbox-ak. All canonical cards cite merged source stages.

## Main deliverables

- `docs/stage14-toolbox/proof-receiver-dependency-map.md`
- nine new canonical cards covering receiver levels, legal dispatch recipes, composition safety, and the new current ledger
- master registry advanced from 67 to 76 cards
- 4br `20/21` ledger preserved but marked `SUPERSEDED`
- merged s7-08 `18/19` ledger promoted to `CURRENT`
- human exponent ledger updated through the s7-08 optimization

## Receiver chain frozen

```text
L0 local state
 -> L1 global rational witness
 -> L2 integral witness coordinate
 -> L3 fixed signed kernel packet
 -> L4 fixed curve/fiber
 -> L5 physical edge/pair
 -> L6 active direction/base
 -> L7 restricted square-part/coefficient sector
 -> L8 whole physical family
```

A level may be skipped only when a merged theorem supplies the corresponding explicit transfer.

## New canonical cards

```text
TB-DICTIONARY-proof-receiver-dispatch-levels
TB-RECIPE-dispatch-local-to-global-witness
TB-RECIPE-dispatch-witness-to-radical-geometry
TB-RECIPE-dispatch-compact-half-angle-physical
TB-RECIPE-dispatch-fixed-fiber-active-direction
TB-RECIPE-dispatch-balanced-inert-square-sieve
TB-RECIPE-dispatch-shared-xi-cell-switch
TB-WARNING-proof-receiver-composition-boundary
TB-LEDGER-current-whole-family-after-s7-08
```

## Current exponent maintenance

Merged s7-08 proves

```text
V(B) << B^(18/19+o(1)).
```

with optimized thresholds

```text
lambda=9/19,
tau=2/19,
theta=8/19.
```

Hence

```text
20/21 - 18/19 = 2/399,
18/19 - 1/2   = 17/38,
41/42 - 18/19 = 23/798.
```

The former 4br current ledger remains in the registry as historical `SUPERSEDED` provenance.

## Boundary

```text
STAGE14_TOOLBOX_AK=COMPLETE_PROOF_RECEIVER_DISPATCH_AND_LEMMA_DEPENDENCY_MAP
CANONICAL_NEW_CARD_COUNT=9
CANONICAL_TOTAL_CARD_COUNT=76
PROOF_RECEIVER_LEVEL_COUNT=9
PROOF_RECEIVER_QUANTIFIER_LADDER_FROZEN=true
LOCAL_TO_GLOBAL_REQUIRES_EXPLICIT_GLOBAL_WITNESS=true
WITNESS_ARITHMETIC_GEOMETRY_DISPATCH_FROZEN=true
COMPACT_HALF_ANGLE_RECEIVER_DISPATCH_FROZEN=true
FIXED_FIBER_TO_ACTIVE_DIRECTION_HANDOFF_FROZEN=true
BALANCED_INERT_SQUARE_SIEVE_RECEIVER_FROZEN=true
SHARED_XI_CELL_SWITCH_RECEIVER_FROZEN=true
RECEIVER_COMPOSITION_WITHOUT_TRANSFER_ALLOWED=false
HISTORICAL_4BR_LEDGER_SUPERSEDED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19
IMPROVEMENT_OVER_20_21=2/399
CURRENT_REMAINING_GAP_TO_SQRT=17/38
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=23/798
SQRT_B_UPPER_BOUND_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_OWNED_BY_TOOLBOX_AK=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-al proof recipe cookbook and receiver checklists
```
