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
COMBINATORIAL_FORD_PULLBACK_H1_RANK=1
RAMIFIED_SYMBOL_RESIDUE_PULLBACK_COMPLETE=false
MULTIQUADRATIC_PULLBACK_ACCOUNTED=false
PHYSICAL_OPEN_UNRAMIFIED_KERNEL_COMPLETE=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Exact 72-component physical-boundary skeleton

The resolved physical boundary has

```text
vertices / components = 72
codim-2 crossings      = 144
connected components   = 1
integral cycle rank    = 73
```

and is bipartite between 24 side conics and 48 exceptional curves.  The exact V4 action on the saturated rank-73 cycle lattice has character multiplicities

```text
(cc=+1, ct=+1): 61
(cc=-1, ct=+1): 12
(cc=+1, ct=-1):  0
(cc=-1, ct=-1):  0.
```

Thus the odd-primary Q-invariant residue-cycle rank and the mod-2 joint fixed dimension are both `61`.  These are residue-cycle candidates, not 61 Q-defined Brauer classes.

## 2. Exact map from the physical boundary to the seven-line arrangement

Run `32688897415` classifies every exceptional component under the endpoint sign/Kummer map

```text
[a1:a2:a3:b1:b2:b3:c] -> [a1^2:a2^2:a3^2].
```

All 48 exceptional curves lie over the six triple points of the seven-line arrangement, exactly eight over each triple point.  None lies over the three ordinary double points:

```text
six triple points:          8 exceptional curves each
three ordinary double pts:  0 exceptional curves each.
```

The 24 physical side conics map only to the three coordinate branch lines

```text
x=0, y=0, z=0.
```

Consequently the portion of the base incidence graph actually touched by the physical 72-boundary has

```text
vertices   = 9
edges      = 9
components = 1
cycle rank = 1.
```

The exact F2 cochain pullback from this touched base graph into the endpoint 72-boundary graph has

```text
COMBINATORIAL_INCIDENCE_PULLBACK_H1_F2_RANK = 1.
```

So although the endpoint residue-cycle room contains 61 Galois-fixed directions, the presently materialized Ford/seven-line incidence channel into the **physical boundary** is only rank one at the pure graph-combinatorial level.

Evidence:

```text
workflow_run = 32688897415
workflow_conclusion = success
sign_cover_boundary_map_sha256 = e98c4ba65b9320ddd5c71c7e2a03bb224ed9ef6603dcbbbb0940c2f6c06f04fb
artifact_id = 9506598888
artifact_zip_sha256 = 11fa91d005685b30a52e291f680bf05f6b34fc6427d38830db8f24924ed0d156
boundary_skeleton_sha256 = f63b65bebcbd5880e64647034fb174ebe610f90ee4d7d3cf5ac40154bfe10c26
cycle_galois_sha256 = 1104078a4c2f88a0f286a8233e80ff936c564e7f3aa7046c51629056d08d2be5
```

## 3. Firewall: rank one is not yet a Brauer class

The graph pullback rank

```text
1
```

is only the combinatorial incidence adapter.  It does not yet impose the actual Ford symbol relations after the ramified 64-fold multiquadratic pullback, nor does it certify that this one direction is unramified on the endpoint physical open.

In particular:

```text
FORD_FULL_PULLBACK_COMPLETE=false
RAMIFICATION_SYMBOL_RESIDUE_CONDITIONS_APPLIED=false
MULTIQUADRATIC_PULLBACK_ACCOUNTED=false
PHYSICAL_OPEN_UNRAMIFIED_KERNEL_COMPLETE=false
Q_DEFINED_BRAUER_CLASS_COUNT_FROM_33_04=NOT_YET_CERTIFIED
```

## 4. Next exact leaf

```text
LEAF_ID=L33-04-FORD9-TO-ENDPOINT72-RAMIFIED-RESIDUE-PULLBACK
CLASS=2
NEW_THEOREM_REQUIRED=false
INPUT_BASE_FORD_H1_DIM=9
INPUT_PHYSICAL_TOUCHED_BASE_H1_DIM=1
INPUT_COMBINATORIAL_PULLBACK_RANK=1
INPUT_ENDPOINT_Q_FIXED_RESIDUE_CYCLE_DIM=61
```

The next step is to attach actual Ford symbol residues to this rank-one combinatorial channel, include all ramification multiplicities and exceptional-divisor residues under the `(Z/2)^6` sign cover, and compute whether the direction survives in the physical-open unramified kernel.

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
