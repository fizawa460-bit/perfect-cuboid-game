# Stage33-05 — K3 Br[2] Q(i)/Q descent production state

```text
STAGE33_UNIT=33-05
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
K3_GEOMETRIC_BR2_DIM=2
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
QI_OVER_Q_ACTION_MATRIX_EXACT=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

This batch does not guess the arithmetic survivor dimension. It converts the frozen Stage29 wall into the exact finite sub-DAG recorded in `source-reduction.md` and adds an independent symbolic regression for the ruled branch model.

The preflight certifies only the source geometry needed to start the arithmetic presentation:

```text
F=(X+iY)(X-iY) over Q(i)
B+,B- have bidegree (2,2)
complex conjugation swaps B+ and B-
B+ intersect B- in exactly 8 frozen points
all 8 intersections are transverse
```

The following inference is explicitly forbidden:

```text
branch-component swap => action on Br(K_c_Qbar)[2]
```

The next exact Class-2 leaf is

```text
L33-05-CV-PRESENTATION
```

which must materialize `L_{c,E}`, a certified `NS(K_c)` basis on the ruled model, the `x-alpha` relation matrix, and an explicit two-dimensional geometric Brauer quotient/symbol basis. Only then can Stage33 compute a meaningful `Q(i)/Q` action matrix, descent obstruction, and exact `Q_RELEVANT_SURVIVING_DIM`.

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
