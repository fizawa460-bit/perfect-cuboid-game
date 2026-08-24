# Stage33-05 — K3 Br[2] Q(i)/Q descent source reduction

```text
STAGE33_UNIT=33-05
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
K3_GEOMETRIC_BR2_DIM=2
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Frozen input

Use the audited Stage29 `K_c` ruled-double-cover model

```text
A1 = v1^2-u1^2
A2 = v2^2-u2^2
X  = u1*v1*A2
Y  = u2*v2*A1
F  = X^2+Y^2
w^2 = F
```

on `P1 x P1`. Over `Q(i)` the branch is

```text
B+ : X+iY=0
B- : X-iY=0.
```

Frozen audited facts:

```text
B+ and B- are smooth (2,2) curves;
B+ intersect B- in 8 transverse nodes;
rank NS(K_c)=20;
dim_F2 Br(K_c_Qbar)[2]=2.
```

## Exact finite execution sub-DAG

```text
05A  branch normalization / Q(i)/Q component-action regression       DONE
 |
 v
05B  materialize finite L_{c,E} structure
     - corrected exact dimension / quotient skeleton                 DONE
     - explicit compatible 5-element function basis                  OPEN
 |
 +-------> 05C transport a certified NS(K_c) basis to the ruled model OPEN
              |
              v
05D  construct the exact x-alpha relation matrix                      OPEN
 |
 v
05E  quotient L_{c,E}/im(x-alpha); certify geometric F2 dimension 2   DIMENSION_LOCKED, SYMBOL BASIS OPEN
 |
 v
05F  compute complex-conjugation action on the quotient basis         OPEN
 |
 v
05G  compute invariant/descended subspace and descent obstruction;
     materialize every surviving Q-defined arithmetic representative,
     or certify exact zero survival                                   OPEN
```

## Corrected exact dimension reduction

For the first ruling `W=P1_t`, both branch components have common discriminant squareclass

```text
q(t)=t^4-6t^2+1.
```

The normalization consists of two genus-one components; the dual graph is two vertices joined by eight edges.  The exact checker certifies

```text
Jac(B)[2] dimension = 4
b1(Gamma)           = 7
K-squareclass kernel dimension = 1
c square on generic fiber      = true
```

The source's `e(b/w)` at a singular branch point is the sum of ramification indices over normalization points.  Therefore the special ruling values are not only the four smooth ramification fibers `q=0`, but also the four nodal fibers

```text
0, 1, -1, infinity,
```

where every node has `e(b/w)=1+1=2`.

Hence

```text
special even-e fibers            = 8
raw generator subspace mod L*2   = 12
kernel to K*L*2                  = 7
L_E dimension                    = 5
L_{c,E}=L_E                      = true
L_{c,E} dimension                = 5
im(x-alpha) dimension            = 3
Br quotient dimension            = 2
```

The previous 9-dimensional pilot omitted the nodal fibers and is superseded.

## Exact current smaller leaf

```text
LEAF_ID=L33-05-CV-EXPLICIT-5D-PRESENTATION
CLASS=2
STATEMENT=materialize an explicit 5-element L_{c,E} function basis, transport a certified ruled-model NS basis, construct a rank-3 x-alpha relation matrix, and output two explicit quotient symbols
INPUT_DIMENSION=5
RELATION_RANK=3
QUOTIENT_DIMENSION=2
NEW_THEOREM_REQUIRED=false
```

Only after this leaf closes is a concrete `Q(i)/Q` Brauer action matrix well-defined on a certified quotient basis.

## Firewalls

```text
CONJUGATION_SWAPS_BPLUS_BMINUS_IMPLIES_BRAUER_ACTION_KNOWN=false
GEOMETRIC_BR2_DIM2_IMPLIES_Q_SURVIVING_DIM2=false
GEOMETRIC_BR2_DIM2_IMPLIES_Q_SURVIVING_DIM_NONZERO=false
MODULAR_LABEL_KC_TO_H32_IMPLIES_CV_SYMBOL_ACTION=false
BRANCH_COMPONENT_ACTION_IMPLIES_DESCENT_OBSTRUCTION_ZERO=false
LCE_DIMENSION_5_IMPLIES_EXPLICIT_BASIS_MATERIALIZED=false
XALPHA_IMAGE_DIMENSION_3_IMPLIES_RELATION_MATRIX_MATERIALIZED=false
```

## Closure target

Stage33-05 remains open until all unit-contract conditions are met:

```text
QI_OVER_Q_ACTION_MATRIX_EXACT=true
INVARIANT_DESCENDED_SUBSPACE_EXACT=true
DESCENT_OBSTRUCTION_ACCOUNTED=true
Q_RELEVANT_SURVIVING_DIM_EXACT=true
ALL_SURVIVING_K3_CLASSES_HAVE_EXPLICIT_ARITHMETIC_REPRESENTATIVES=true
  OR EXACT_ZERO_SURVIVAL_CERTIFICATE=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
HOSTILE_AUDIT=PASS
```
