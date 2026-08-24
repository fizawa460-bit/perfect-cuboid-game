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
QFIXED_RESIDUE_COMPLEMENT_DIM_F2=17
PHYSICAL_OPEN_UNRAMIFIED_KERNEL_COMPLETE=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Boundary and Galois skeleton

The resolved physical boundary has

```text
components = 72
crossings  = 144
components of dual graph = 1
cycle rank = 73.
```

The exact V4 action on the rank-73 cycle lattice has character multiplicities

```text
(cc=+1, ct=+1): 61
(cc=-1, ct=+1): 12
(cc=+1, ct=-1):  0
(cc=-1, ct=-1):  0,
```

so the mod-2 joint fixed residue-cycle candidate dimension is `61`.  This is not itself a Q-defined Brauer-class count.

## Seven-line/Ford source branch is killed by the endpoint Kummer cover

The endpoint map is

```text
[a1:a2:a3:b1:b2:b3:c] -> [a1^2:a2^2:a3^2].
```

On its function field all seven line forms have explicit square roots:

```text
x         = a1^2
 y        = a2^2
 z        = a3^2
 x+y      = b3^2
 x+z      = b2^2
 y+z      = b1^2
 x+y+z    = c^2.
```

Therefore the source-certified Ford group

```text
Br(P2bar-D)[2] ~= (Z/2)^9
```

has exact pullback rank

```text
FORD_KUMMER_PULLBACK_RANK = 0.
```

Thus the earlier graph-combinatorial rank-one channel dies after the actual Kummer symbol pullback is imposed.  This closes the Ford/seven-line source branch inside 33-04, but not the endpoint-intrinsic residue branch.

Evidence:

```text
workflow_run = 32691135447
ford_kummer_pullback_zero_sha256 = 0fd1746fcea0e30257b84460bb025d561738fbbdc1e604700a15f4b9807d7f61
```

## Endpoint-intrinsic unit-symbol residue span

The audited Stage33-02 unit divisor lattice has rank `14`.  For every pair of basis units, the divisor-level secondary tame residue at a transverse crossing `D_a cap D_b` is computed mod 2 as

```text
v_a*w_b - w_a*v_b.
```

All `C(14,2)=91` resulting edge patterns are exact graph cycles and are fixed by both V4 generators.  Their span has

```text
UNIT_SYMBOL_SECONDARY_RESIDUE_SPAN_RANK_F2 = 44.
```

Since the total Q-fixed boundary cycle dimension is `61`, the current unexplained Q-fixed complement has dimension

```text
61 - 44 = 17.
```

Evidence:

```text
workflow_run = 32691135447
workflow_conclusion = success
unit_symbol_residue_span_sha256 = 53abf58c647a6cf504839b74b19113c5fb2929010c335f86e1c57c537169b8e8
artifact_id = 9507293510
artifact_zip_sha256 = b8df5948de1ba3f7074dbc6b8c1e64f3b80fcd46e29e21e7afd02d8d39d41aed
```

## Firewall and next leaf

The value `44` is a divisor-level secondary-residue span, not 44 certified Q-defined Brauer classes.  Actual Q-rational unit functions, symbol representatives, first residues, duplicate/trivial relations, and the final physical-open unramified kernel remain to be materialized.

```text
Q_DEFINED_BRAUER_CLASS_COUNT_FROM_33_04=NOT_YET_CERTIFIED
PHYSICAL_OPEN_UNRAMIFIED_KERNEL_COMPLETE=false
```

Next exact leaf:

```text
LEAF_ID=L33-04-MATERIALIZE-14-Q-UNITS-AND-LIFT-44-SYMBOL-RESIDUES
CLASS=2
NEW_THEOREM_REQUIRED=false
INPUT_UNIT_RANK=14
INPUT_SYMBOL_PAIR_COUNT=91
INPUT_SECONDARY_RESIDUE_SPAN_RANK_F2=44
INPUT_QFIXED_COMPLEMENT_DIM_F2=17
```

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
