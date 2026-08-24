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
LOWDEGREE_GRAPH_FUNCTION_CHANNEL_EXACT=true
LOWDEGREE_GRAPH_FUNCTION_SPAN_DIM=2
REMAINING_GRAPH_DIRECTION_DIM=1
FULL_EXPLICIT_LCE_BASIS_MATERIALIZED=false
FULL_LCE_CC_ACTION_EXACT=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
QI_OVER_Q_ACTION_MATRIX_EXACT=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Corrected exact Creutz--Viray target

Over `Q(i)` the branch is two smooth `(2,2)` genus-one components meeting transversely at eight nodes, with common normalization

```text
z^2=t^4-6*t^2+1.
```

After the nodal-fiber correction the exact finite dimensions remain

```text
Jac(B)[2] dimension       = 4
dual graph b1             = 7
raw generator dimension   = 12
K*L^2 relation dimension  = 7
L_E=L_{c,E} dimension     = 5
im(x-alpha) dimension     = 3
Br(K_cbar)[2] dimension   = 2.
```

The exact associated-graded five-dimensional quotient is

```text
Jacobian quotient = 2D
graph quotient    = 3D
ell_1 quotient    = 0D.
```

## Two explicit Jacobian directions

With

```text
r1=1+sqrt(2),
r2=-(1+sqrt(2)),
r4=1-sqrt(2),
```

two Jacobian quotient directions are represented on the common normalization by

```text
f1=(t-r1)/(t-r4),
f2=(t-r2)/(t-r4).
```

The third branch-ratio is dependent because its product with `f1*f2` is `q(t)/(t-r4)^4`, a square on `z^2=q(t)`.

## Two explicit low-degree graph directions

CI run `32692459136` exhaustively checks twelve stable bidegree `(1,1)` forms whose zero sets pass through exactly four of the eight nodes.  Ratios to the base form

```text
F01=u1*(v2-u2)
```

span exactly a two-dimensional subspace of the corrected three-dimensional graph quotient.

An explicit independent pair is

```text
g1 = (u1*u2-u2*v1)/(u1*u2-u1*v2),
g2 = (u1*v2-u2*v1)/(u1*u2-u1*v2).
```

Relative to the quotient basis

```text
q1=e1+e3,
q2=e1+e5,
q3=e1+e7,
```

their node-parity classes are

```text
g1 -> q1+q2+q3,
g2 -> q3.
```

Therefore the low-degree channel spans

```text
<q3, q1+q2>
```

and leaves only one associated-graded graph direction unresolved; it may be taken as `q1` (equivalently `q2` modulo the selected span).

Evidence:

```text
workflow_run = 32692459136
workflow_conclusion = success
lowdegree_graph_functions_sha256 = 5f72e6ae2b2a815b711ed8b0996be12ba181aba1da9206bbff6dba78e42afdc1
artifact_id = 9507702781
artifact_zip_sha256 = 094757bb9ec86ee24d6679bf7000aaf6e3fcec7eee9efa241b93e483b5668825
```

## Firewall and next exact leaf

The node-parity calculation is an associated-graded graph certificate.  It does not yet prove that the two displayed low-degree ratios satisfy every Creutz--Viray divisor condition needed for a compatible `L_{c,E}` lift, and it does not resolve extension mixing, the rank-three `x-alpha` matrix, the final quotient action, or Q-survival.

```text
FULL_EXPLICIT_LCE_BASIS_MATERIALIZED=false
CREUTZ_VIRAY_DIVISOR_CONDITIONS_FOR_LOWDEGREE_FUNCTIONS_COMPLETE=false
EXPLICIT_XALPHA_MATRIX_MATERIALIZED=false
BRAUER_QUOTIENT_CC_ACTION_EXACT=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
```

Next exact leaf:

```text
LEAF_ID=L33-05-SYNTHESIZE-ONE-RESIDUAL-GRAPH-FUNCTION-AND-CHECK-CV-DIVISORS-THEN-XALPHA
CLASS=2
NEW_THEOREM_REQUIRED=false
EXPLICIT_JACOBIAN_FUNCTIONS=2
LOWDEGREE_GRAPH_DIRECTIONS=2
REMAINING_ASSOCIATED_GRADED_GRAPH_DIM=1
REQUIRED_XALPHA_IMAGE_RANK=3
REQUIRED_BRAUER_QUOTIENT_DIM=2
```

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
