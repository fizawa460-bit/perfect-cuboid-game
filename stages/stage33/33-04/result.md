# Stage33-04 — BR0G physical-boundary residue production state

```text
STAGE33_UNIT=33-04
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0G=OPEN
BOUNDARY_COMPONENT_COUNT=72
BOUNDARY_SNC_SKELETON_EXACT=true
GEOMETRIC_BOUNDARY_RESIDUE_CYCLE_MODULE_EXACT=true
GALOIS_ACTION_ON_RESIDUE_CYCLE_MODULE_EXACT=true
Q_GALOIS_INVARIANT_CYCLE_MODULE_EXACT=true
SIGN_COVER_BOUNDARY_BASEMAP_EXACT=true
FORD_KUMMER_PULLBACK_EXACT=true
FORD_KUMMER_PULLBACK_RANK=0
UNIT_SYMBOL_SECONDARY_RESIDUE_SPAN_EXACT=true
UNIT_SYMBOL_SECONDARY_RESIDUE_SPAN_RANK_F2=44
QFIXED_RESIDUE_CYCLE_DIM_F2=61
QFIXED_RESIDUAL_QUOTIENT_DIM_F2=17
QFIXED17_EXPLICIT_BASIS_EXACT=true
LINEAR_FACTOR_Q_UNIT_SPAN_RANK=11
UNIT_SIDE_PROJECTION_RANK=14
PHYSICAL_OPEN_UNRAMIFIED_KERNEL_COMPLETE=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact boundary/Galois reduction

The resolved physical boundary has

```text
components = 72
crossings  = 144
dual-graph components = 1
cycle rank = 73.
```

The exact `V4=Gal(Q(i,sqrt(2))/Q)` action on the rank-73 cycle lattice has rational character multiplicities

```text
(+,+)=61,
(-,+)=12,
(+,-)=0,
(-,-)=0,
```

and the mod-2 joint fixed cycle dimension is exactly `61`.  This is a residue-cycle candidate dimension, not a Brauer-class count.

## Ford/seven-line source branch closes to zero

Under

```text
[a1:a2:a3:b1:b2:b3:c] -> [a1^2:a2^2:a3^2]
```

all seven arrangement forms acquire explicit square roots (`a1,a2,a3,b1,b2,b3,c`).  Hence every Ford 2-symbol generator pulls back to zero and

```text
FORD_KUMMER_PULLBACK_RANK=0.
```

This kills the inherited seven-line/Ford source branch inside 33-04, but not the endpoint-intrinsic boundary branch.

## Intrinsic unit-symbol image and exact 17D residual

The audited Stage33-02 unit divisor lattice has rank `14`.  The `91=C(14,2)` divisor-level 2-symbol secondary-residue footprints span exactly

```text
44D
```

inside the `61D` Q-fixed graph-cycle space.

CI run `32694342783` now constructs an explicit quotient basis:

```text
Q-fixed graph-compatible cycle space = 61D
known unit-symbol footprint image     = 44D
exact residual quotient               = 17D.
```

All seventeen residual basis vectors are materialized both in the stable 73-coordinate cycle basis and as 144 crossing-edge vectors, and every vector is independently checked to be a graph cycle and fixed by both V4 generators.

```text
QFIXED17_EXPLICIT_BASIS_EXACT=true
QFIXED17_IS_CERTIFIED_BRAUER_GROUP=false
```

Evidence:

```text
workflow_run = 32694342783
workflow_conclusion = success
qfixed17_graph_residual_sha256 = e3eec759c40779becda1786d4f1e9ab150d6d4d27114fdcf942aa7387603524a
artifact_id = 9508334788
artifact_zip_sha256 = 2be766a8c1ddb895cc3bb901afe0aed8409fcc1ab79bd1fb07100f64ef3152d3
```

## Q-unit side channel: exact but no longer the main closure path

The projection of the full rank-14 unit divisor lattice to the first 24 side components is injective and has rank 14.  All 17 ratios from the natural eighteen Q-linear factors admit unique exact lifts through this projection, but their span is only

```text
11D,
```

leaving three unit directions outside the linear-factor channel.

This is useful explicit-function infrastructure, but materializing those three functions is not itself a Stage33-04 closure gate.  The main path therefore returns to the residue adapter rather than opening an unbounded function-search quest.

## Exact remaining wall

The 17D quotient is **not** promoted to seventeen Brauer classes.  What remains is to decide which of these graph-compatible Q-fixed secondary-residue patterns are realizable by first-residue classes on the normalized rational boundary components, incorporate the coefficient/Galois descent correctly, and quotient any proper-Brauer contribution before declaring the physical-open unramified kernel.

```text
RESIDUAL_KERNEL=R33-BR0G-QFIXED17-FIRST-RESIDUE-REALIZABILITY-AND-DESCENT
LEAF_ID=L33-04-REALIZE-OR-KILL-QFIXED17-IN-BOUNDARY-H1-THEN-QUOTIENT-PROPER-BRAUER
CLASS=2
NEW_THEOREM_REQUIRED=false
QFIXED17_BRAUER_REALIZABILITY_COMPLETE=false
CYLCOTOMIC_COEFFICIENT_DESCENT_COMPLETE=false
PROPER_BRAUER_QUOTIENT_COMPLETE=false
PHYSICAL_OPEN_UNRAMIFIED_KERNEL_COMPLETE=false
```

The rationality of all 72 boundary components suggests a bounded residue-sequence adapter rather than a new global theorem, but no such adapter is credited until the normalizations/intersection divisors and descent maps are materialized exactly.

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
