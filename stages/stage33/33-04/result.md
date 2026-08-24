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
MULTIQUADRATIC_PULLBACK_ACCOUNTED=false
PHYSICAL_OPEN_UNRAMIFIED_KERNEL_COMPLETE=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact physical-boundary geometry

Successful CI run `32687634248` reconstructs the complete audited 72-component resolved boundary and certifies

```text
vertices / components = 72
codim-2 crossings      = 144
connected components   = 1
integral cycle rank    = 144 - 72 + 1 = 73
```

The resolved boundary is exactly bipartite:

```text
24 side conics: each degree 6
48 exceptional curves:
  24 of degree 2
  24 of degree 4
side-side off diagonal intersection          = 0
exceptional-exceptional off diagonal         = 0
side-exceptional nonzero intersection         = 1
```

Hence every nonzero side/exceptional incidence is one transverse codimension-two crossing and no triple boundary point is omitted.  The saturated integral graph cycle lattice has rank 73.  Prime-by-prime, this is the exact finite-support residue-compatibility skeleton for rational boundary components.  It is not by itself a list of Q-defined Brauer classes.

## Exact boundary Galois action

The pinned Testa--Stoll source was independently rerun in the same CI job.  On the 72 physical components:

```text
sqrt(2)-conjugation ct: fixes all 72 components
complex conjugation cc: fixes 48 components and swaps the remaining 24 in 12 pairs
```

All 144 crossing points are stable as a set.  The induced exact V4 action on the saturated rank-73 cycle lattice has rational character multiplicities

```text
(cc=+1, ct=+1): 61
(cc=-1, ct=+1): 12
(cc=+1, ct=-1):  0
(cc=-1, ct=-1):  0
```

Therefore, for every odd prime `ell`, where the V4 action is semisimple,

```text
Q-GALOIS-INVARIANT ODD-PRIMARY CYCLE RANK = 61.
```

The two-primary action is treated separately rather than reusing odd-primary semisimplicity.  Exact reduction mod 2 gives

```text
F2 joint fixed dimension = 61.
```

This is a large surviving **residue-cycle candidate space**.  It does not assert 61 independent Q-defined Brauer classes: actual descent, multiquadratic pullback, proper/open identifications, and the final unramified physical-open kernel still have to be computed.

## Evidence

```text
workflow_run = 32687634248
workflow_conclusion = success
boundary_skeleton_sha256 = f63b65bebcbd5880e64647034fb174ebe610f90ee4d7d3cf5ac40154bfe10c26
cycle_galois_sha256 = 1104078a4c2f88a0f286a8233e80ff936c564e7f3aa7046c51629056d08d2be5
artifact_id = 9506202722
artifact_zip_sha256 = ac0d8ab55eee27aefeceac0cdd18e3a1fdfce5d2a69cdf76b15ec48182ea7385
```

## Next exact leaf

```text
LEAF_ID=L33-04-MULTIQUADRATIC-PULLBACK-AND-UNRAMIFIED-KERNEL
CLASS=2
NEW_THEOREM_REQUIRED=false
INPUT_GEOMETRIC_CYCLE_RANK=73
INPUT_Q_INVARIANT_ODD_PRIMARY_RANK=61
INPUT_F2_FIXED_DIM=61
```

Remaining work:

1. attach the endpoint multiquadratic pullback to the 61-dimensional invariant residue-cycle subspace;
2. account exactly for exceptional-divisor residues under that pullback;
3. identify/trivialize duplicates and residues that do not define endpoint-relevant open classes;
4. compute the exact physical-open unramified kernel;
5. hostile-audit BR0G before releasing dependent 33-06/33-07 work.

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
