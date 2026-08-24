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

The frozen audited facts are:

```text
B+ and B- are smooth (2,2) curves;
B+ intersect B- in 8 transverse nodes;
the double-cover hypotheses required by Creutz--Viray are discharged;
rank NS(K_c)=20;
dim_F2 Br(K_c_Qbar)[2]=2.
```

No arithmetic survival over `Q` follows from dimension two alone.

## Exact finite execution sub-DAG

Stage29 identified the remaining wall as the explicit Creutz--Viray presentation plus Galois descent. Stage33-05 therefore freezes the following bounded sub-DAG:

```text
05A  branch normalization / Q(i)/Q component-action regression
 |
 v
05B  materialize an explicit finite basis of L_{c,E}
 |
 +-------> 05C transport a certified NS(K_c) basis to the ruled model
              |
              v
05D  construct the exact x-alpha relation matrix
 |
 v
05E  quotient L_{c,E}/im(x-alpha); certify geometric F2 dimension exactly 2
 |
 v
05F  compute complex-conjugation action on the quotient basis
 |
 v
05G  compute invariant/descended subspace and descent obstruction;
     materialize every surviving Q-defined arithmetic representative,
     or certify exact zero survival
```

`05A` is a source/regression preflight. `05B--05G` are the actual Class-2 wall. Failure to materialize them is not permission to infer `Q_RELEVANT_SURVIVING_DIM=0`.

## Exact current smaller leaf

```text
LEAF_ID=L33-05-CV-PRESENTATION
CLASS=2
STATEMENT=materialize L_{c,E}, a certified ruled-model NS basis, the x-alpha matrix, and the resulting two-dimensional geometric Brauer quotient with explicit symbols
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
