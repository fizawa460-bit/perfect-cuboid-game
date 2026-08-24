# Stage33-05 — K3 Br[2] Q(i)/Q descent production state

```text
STAGE33_UNIT=33-05
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
K3_GEOMETRIC_BR2_DIM=2
LCE_DIMENSION=5
XALPHA_IMAGE_DIMENSION=3
COMMON_NORMALIZATION_EXACT=true
LCE_FILTERED_QUOTIENT_EXACT=true
LCE_ASSOCIATED_GRADED_JAC_DIM=2
LCE_ASSOCIATED_GRADED_GRAPH_DIM=3
EXPLICIT_JACOBIAN_QUOTIENT_FUNCTION_COUNT=2
FULL_EXPLICIT_LCE_BASIS_MATERIALIZED=false
FULL_LCE_CC_ACTION_EXACT=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
QI_OVER_Q_ACTION_MATRIX_EXACT=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Corrected exact Creutz--Viray target

The ruled model over `Q(i)` has

```text
F=(X+iY)(X-iY),
B+,B- smooth (2,2),
8 transverse intersections,
z^2 = q(t) = t^4 - 6*t^2 + 1
```

as the common normalization.  After inclusion of the four nodal even-e fibers `0,1,-1,infinity`, the exact dimensions are

```text
Jac(B)[2] dimension       = 4
dual graph b1             = 7
raw generator dimension   = 12
K*L^2 relation dimension  = 7
L_E=L_{c,E} dimension     = 5
im(x-alpha) dimension     = 3
Br(K_cbar)[2] dimension   = 2.
```

## Filtered five-dimensional quotient

CI run `32690996286` materializes the associated-graded quotient of the 12-dimensional candidate space by the seven `K*L^2` relations.  At filtration level these relations consist of

```text
2 diagonal Jac(B+)[2] / Jac(B-)[2] identifications,
4 nodal pair-cycle relations,
1 leading ell_1 relation.
```

Hence

```text
L_{c,E} associated graded:
  Jacobian quotient = 2 dimensions
  graph quotient    = 3 dimensions
  ell_1 quotient    = 0 dimensions
  total             = 5 dimensions.
```

Convenient graph quotient cycle representatives are

```text
e1+e3,
e1+e5,
e1+e7.
```

These are quotient classes; their explicit `ell_C` rational functions are not yet materialized.

## Two explicit Jacobian quotient functions

Let the roots of `q` be

```text
r1 = 1+sqrt(2)
r2 = -(1+sqrt(2))
r3 = sqrt(2)-1
r4 = 1-sqrt(2).
```

On `z^2=q(t)` the two quotient directions can be represented by

```text
f1 = (t-r1)/(t-r4)
f2 = (t-r2)/(t-r4),
```

using pairs `(f1,1)` and `(f2,1)` in the two normalization components.  The third branch-ratio is dependent because

```text
f1*f2*f3 = q(t)/(t-r4)^4,
```

which is a square on `z^2=q(t)`.

Evidence:

```text
workflow_run = 32690996286
workflow_conclusion = success
lce_filtered_quotient_sha256 = 129215ed58f85271cbbdcca4fdd085a74877769900f35f9da8c77bf120b22943
artifact_id = 9507230128
artifact_zip_sha256 = 46ba5cd90ca87e65099d854c958f3fbbda78293df109c1fbac0f4a551966a84b
```

## Firewall and next exact leaf

The associated-graded quotient does not determine extension mixing in the actual `L_{c,E}` module.  In particular it does not determine the full complex-conjugation action, the rank-three `x-alpha` matrix, or Q-survival of the final two geometric Brauer directions.

```text
FULL_EXPLICIT_LCE_BASIS_MATERIALIZED=false
EXPLICIT_GRAPH_CYCLE_FUNCTIONS_MATERIALIZED=false
EXPLICIT_XALPHA_MATRIX_MATERIALIZED=false
BRAUER_QUOTIENT_CC_ACTION_EXACT=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
```

The remaining explicit-function wall has been reduced from five unknown basis functions to three graph-cycle functions:

```text
LEAF_ID=L33-05-SYNTHESIZE-3-GRAPH-FUNCTIONS-THEN-XALPHA
CLASS=2
NEW_THEOREM_REQUIRED=false
GRAPH_CYCLE_TARGETS=[e1+e3,e1+e5,e1+e7]
EXPLICIT_JACOBIAN_FUNCTIONS_ALREADY_MATERIALIZED=2
REQUIRED_XALPHA_IMAGE_RANK=3
REQUIRED_BRAUER_QUOTIENT_DIM=2
```

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
