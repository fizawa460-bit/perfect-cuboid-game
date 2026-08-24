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
QFIXED17_GEOMETRIC_FIRST_RESIDUE_REALIZABILITY_COMPLETE=true
QFIXED17_GERSTEN_SECOND_RESIDUE_COMPATIBILITY_COMPLETE=true
PROPER_BRAUER_RESIDUE_QUOTIENT_CHANGES_QFIXED17=false
QFIXED17_ARITHMETIC_GQ_DESCENT_COMPLETE=false
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

CI run `32694342783` constructs an explicit quotient basis:

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

## Geometric first-residue realizability is now exact

The exact next leaf was added at commit `b83925ae7d10529e9555d285863f430b3106b7f3` and completed successfully in workflow run `32695734689`.

On each geometric boundary component `D_j ~= P^1` over `Qbar`, the divisor sequence

```text
0 -> k^* -> k(P^1)^* -> Div(P^1) -> Pic(P^1) -> 0,
Pic(P^1)=Z
```

shows that a finite mod-2 valuation prescription is realizable by a Kummer first residue iff its total degree is even.  For the SNC boundary this is exactly the dual-graph cycle condition already certified for every one of the 17 residual vectors.

The exact certificate therefore verifies:

```text
all 17 residual vectors even at every boundary component = true
Kummer first-residue realizability over Qbar             = complete
Gersten second-residue compatibility                     = complete
proper Brauer classes have zero boundary residue         = true
proper-Brauer residue quotient changes residual vectors  = false
```

Thus the former mixed wall

```text
QFIXED17-FIRST-RESIDUE-REALIZABILITY-AND-DESCENT
```

has been strictly reduced.  The geometric realizability half is closed; no further search for geometric residue functions is allowed by the loop guard.

## Q-unit side channel: exact but no longer the main closure path

The projection of the full rank-14 unit divisor lattice to the first 24 side components is injective and has rank 14.  All 17 ratios from the natural eighteen Q-linear factors admit unique exact lifts through this projection, but their span is only

```text
11D,
```

leaving three unit directions outside the linear-factor channel.

This remains useful explicit-function infrastructure, but materializing those three functions is not itself a Stage33-04 closure gate.

## Exact remaining wall

The remaining issue is now purely arithmetic: determine which geometrically realizable Q-fixed residue classes descend through the full absolute `G_Q` action to Q-defined Brauer classes, including coefficient action and any descent obstruction.  V4-fixedness of the cycle vectors alone is not promoted to full absolute-Galois descent.

```text
RESIDUAL_KERNEL=R33-BR0G-QFIXED17-GALOIS-DESCENT
LEAF_ID=L33-04-QFIXED17-ABSOLUTE-GALOIS-DESCENT
CLASS=2
NEW_THEOREM_REQUIRED=false
QFIXED17_GEOMETRIC_FIRST_RESIDUE_REALIZABILITY_COMPLETE=true
QFIXED17_GERSTEN_SECOND_RESIDUE_COMPATIBILITY_COMPLETE=true
QFIXED17_ARITHMETIC_GQ_DESCENT_COMPLETE=false
PHYSICAL_OPEN_UNRAMIFIED_KERNEL_COMPLETE=false
```

Loop guard:

```text
DO_NOT_REOPEN_GEOMETRIC_REALIZABILITY=true
DO_NOT_SEARCH_MORE_UNIT_FUNCTIONS_FOR_CLOSURE=true
ONLY_ARITHMETIC_DESCENT_REMAINS_FOR_QFIXED17=true
```

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
