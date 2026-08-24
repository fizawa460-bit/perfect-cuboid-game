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
EXPLICIT_GRAPH_ASSOCIATED_GRADED_FUNCTION_COUNT=3
ASSOCIATED_GRADED_EXPLICIT_FUNCTION_COUNT=5
ASSOCIATED_GRADED_GRAPH_CHANNEL_COMPLETE=true
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

## Three explicit associated-graded graph directions

The bounded bidegree `(1,1)` channel gives two independent graph directions:

```text
g1 = (u1*u2-u2*v1)/(u1*u2-u1*v2),
g2 = (u1*v2-u2*v1)/(u1*u2-u1*v2).
```

Relative to

```text
q1=e1+e3,
q2=e1+e5,
q3=e1+e7,
```

they satisfy

```text
g1 -> q1+q2+q3,
g2 -> q3.
```

A bounded next-degree `(2,1)` synthesis now supplies the one residual direction `q1`.  Take

```text
F_e1 = u1^2*u2 + u1^2*v2 + u2*v1^2,
F_e3 = u1^2*u2 - u1^2*v2 + u1*u2*v1 + u1*v1*v2 - u2*v1^2 - v1^2*v2,
g3 = F_e1/F_e3.
```

Among the eight branch-intersection nodes, `F_e1` vanishes exactly at `e1` and `F_e3` exactly at `e3`, hence

```text
g3 -> e1+e3 = q1.
```

Therefore

```text
span(g1,g2,g3)=<q1,q2,q3>,
ASSOCIATED_GRADED_GRAPH_CHANNEL_COMPLETE=true.
```

Together with `f1,f2`, every one of the five associated-graded `L_{c,E}` directions now has an explicit rational-function candidate.

Evidence:

```text
workflow_run = 32694382836
workflow_conclusion = success
residual_graph_function_sha256 = 7ca15cb62d529d264a161aea00f963260a1a28f48da09677d696c6aecaa6e08d
artifact_id = 9508324033
artifact_zip_sha256 = 3f5fd63a46197d99db2dc343a854bb37af9933951be1556381f205a6755e971a
```

## Firewall and next exact leaf

This closes only the associated-graded function-synthesis wall.  The five displayed functions are not yet promoted to an actual basis of `L_{c,E}`: the Creutz--Viray divisor conditions and extension mixing must be checked simultaneously.  Only after that lift is exact may the rank-three `x-alpha` matrix and quotient Galois action be materialized.

```text
ASSOCIATED_GRADED_FUNCTION_SYNTHESIS_CLOSED=true
FULL_EXPLICIT_LCE_BASIS_MATERIALIZED=false
CREUTZ_VIRAY_DIVISOR_CONDITIONS_COMPLETE=false
EXTENSION_MIXING_COMPLETE=false
EXPLICIT_XALPHA_MATRIX_MATERIALIZED=false
BRAUER_QUOTIENT_CC_ACTION_EXACT=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
```

Next exact leaf:

```text
LEAF_ID=L33-05-CHECK-5-FUNCTION-CV-DIVISORS-AND-EXTENSION-MIXING-THEN-XALPHA
CLASS=2
NEW_THEOREM_REQUIRED=false
ASSOCIATED_GRADED_FUNCTION_COUNT=5
REQUIRED_XALPHA_IMAGE_RANK=3
REQUIRED_BRAUER_QUOTIENT_DIM=2
```

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
