# Stage33-04 — explicit function / constant-squareclass descent wall

This checkpoint records the exact post-run state after workflow `32700429841` on PR #1362.

## Newly closed finite descent layer

The workflow completed successfully.  In addition to the previously certified 17-dimensional Q-fixed graph-residue quotient and geometric first-residue realizability, the new finite V4 divisor-parity descent adapter certifies

```text
QFIXED17_DIM_F2=17
BOUNDARY_COMPONENT_COUNT=72
BOUNDARY_COMPONENT_ORBIT_COUNT_UNDER_V4=60
ALL_17_EDGE_PATTERNS_FIXED_BY_CC=true
ALL_17_EDGE_PATTERNS_FIXED_BY_CT=true
ALL_17_EDGE_PATTERNS_EVEN_ON_EVERY_COMPONENT=true
FINITE_V4_PERMUTATION_DESCENT_COMPATIBILITY_COMPLETE=true
FINITE_DIVISOR_PARITY_DESCENT_OBSTRUCTION_ZERO=true
```

Certificate:

```text
workflow_run=32700429841
workflow_conclusion=success
qfixed17_v4_divisor_descent_sha256=9ee13811e930415e3a872a5a9cfd4da614a57d81182af3ba1637be0abdb8f8ce
artifact_id=9510324922
artifact_zip_sha256=fa055ff1330c4dc0ed4c692726b7edb032e08323432be1001251da9cbda75dff
```

Thus no residual obstruction remains at the level of the 72-component permutation action plus mod-2 divisor parity.

## What is *not* certified

This finite result does **not** yet construct an actual first-residue squareclass on the arithmetic normalization of every boundary-component orbit.  In particular it does not certify the constant-squareclass cocycle or the resulting Q-defined Brauer-class dimension.

The current repository evidence fixes the geometric curves, their 72-component inventory, 144 crossings, V4 permutation action and residue parity data, but does not yet materialize a source-locked arithmetic `P^1` coordinate / function-field model for every boundary-component orbit together with the crossing divisors in those coordinates.

That missing arithmetic normalization data is the exact next input required to turn invariant divisor parity into explicit squareclasses and to check the constant cocycle by Hilbert-90/descent rather than assuming it away.

## New exact residual kernel

```text
RESIDUAL_KERNEL=R33-BR0G-QFIXED17-FUNCTION-AND-CONSTANT-SQUARECLASS-DESCENT
LEAF_ID=L33-04-MATERIALIZE-ARITHMETIC-BOUNDARY-P1-MODELS-AND-DESCEND-17-FIRST-RESIDUES
CLASS=2
NEW_THEOREM_REQUIRED=false
FINITE_V4_DIVISOR_PARITY_DESCENT_COMPLETE=true
ACTUAL_FIRST_RESIDUE_FUNCTION_DESCENT_COMPLETE=false
CONSTANT_SQUARECLASS_DESCENT_COMPLETE=false
Q_DEFINED_BRAUER_CLASS_DIMENSION_CERTIFIED=false
PHYSICAL_OPEN_UNRAMIFIED_KERNEL_COMPLETE=false
BR0G=OPEN
UNIT_STATUS=RUNNING
```

Required next production data:

1. source-locked arithmetic normalization/parameterization of each of the 60 V4 boundary-component orbits (48 singleton geometric components and 12 conjugate pairs);
2. exact coordinates/minimal fields of every crossing point on those models;
3. for each of the 17 residue vectors, an explicit function with the required odd valuation divisor on every orbit, modulo squares;
4. exact V4/absolute-Galois comparison of those functions and the resulting constant squareclass cocycle;
5. only then, the surviving Q-defined residue/Brauer dimension and physical-open unramified kernel.

Loop guard:

```text
DO_NOT_REOPEN_QFIXED17_GRAPH_LINEAR_ALGEBRA=true
DO_NOT_REOPEN_GEOMETRIC_P1_PARITY_REALIZABILITY=true
DO_NOT_REOPEN_FINITE_V4_DIVISOR_PARITY_DESCENT=true
DO_NOT_SEARCH_MORE_Q_UNIT_FUNCTIONS_AS_A_SUBSTITUTE=true
NEXT_WORK_MUST_MATERIALIZE_ARITHMETIC_BOUNDARY_FUNCTION_FIELDS=true
```

No theorem, endpoint, obstruction, route-color, or perfect-cuboid existence/nonexistence credit follows from this checkpoint.
