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

## 1. Exact ruled-branch preflight

The source-locked ruled model is independently regressed:

```text
F=(X+iY)(X-iY) over Q(i)
B+,B- have bidegree (2,2)
complex conjugation swaps B+ and B-
B+ intersect B- in exactly 8 frozen points
all 8 intersections are transverse
```

No action on `Br(K_c_Qbar)[2]` is inferred merely from the branch-component swap.

## 2. Corrected exact Creutz--Viray dimension skeleton

Relative to the first ruling `W=P1_t`, both normalized branch components have the same quadratic function field

```text
K(sqrt(q)),
q(t)=t^4-6t^2+1.
```

The normalization is

```text
B = B+ disjoint_union B-,
component genera = 1,1,
h0(B)=2,
Creutz--Viray g(B)=1,
Jac(B)[2] dimension=4.
```

The dual graph has two vertices joined by eight edges, so

```text
b1(Gamma)=7.
```

The generic quartic double-cover equation has square leading coefficient `t^2`; after `y=w/t` the source constant `c` may be chosen square.

### Mandatory singular-fiber correction

A first Stage33 dimension pilot counted only the four smooth ramification fibers `q(t)=0`.  That pilot is **superseded**.  Creutz--Viray define `e(b/w)` at a singular branch point as the sum of ramification indices over all normalization points above `b`.  Therefore the four nodal ruling values

```text
t = 0, 1, -1, infinity
```

also satisfy `e(b/w)=1+1=2` at every branch point in the fiber.  They must be included in the source formula.

Thus the exact special-fiber count is

```text
smooth common ramification fibers = 4
nodal even-e fibers                = 4
total special fibers              = 8.
```

The two branch-component function fields are the same quadratic extension, so

```text
dim ((K* intersect L*2) / K*2) = 1.
```

Using the exact Creutz--Viray dimension formulas then gives

```text
raw generator subspace mod L*2 = 12
kernel to K*L*2                = 8 - 1 = 7
L_E dimension                  = 5
L_{c,E}=L_E                    = true   # W=P1 rational
L_{c,E} dimension              = 5
```

With the audited `rank NS(K_c)=20`, the `(4,4)` source formula still gives

```text
dim_F2 Br(K_c_Qbar)[2] = 2.
```

Hence the explicit presentation must have

```text
dim im(x-alpha) = 3
```

inside a five-dimensional `L_{c,E}` space.

This correction makes the remaining finite problem **smaller**, not larger: the next explicit relation matrix has target shape rank `3` in dimension `5`, rather than the superseded `7` in `9` pilot.

## 3. Current exact Class-2 leaf

```text
LEAF_ID=L33-05-CV-EXPLICIT-5D-PRESENTATION
CLASS=2
NEW_THEOREM_REQUIRED=false
INPUT_SPACE_DIM=5
REQUIRED_XALPHA_IMAGE_RANK=3
REQUIRED_BRAUER_QUOTIENT_DIM=2
```

Remaining bounded work:

```text
1. materialize a compatible explicit 5-element basis of L_{c,E};
2. transport a certified NS(K_c) generating set to the ruled model / generic fiber;
3. compute the exact rank-3 x-alpha relation matrix;
4. choose two explicit quotient symbol representatives;
5. compute complex-conjugation action on that quotient basis;
6. compute the invariant/descended subspace and descent obstruction;
7. materialize every surviving Q-defined arithmetic representative, or exact zero survival.
```

A partial geometric function skeleton is already explicit: on each normalized component `z^2=q(t)`, ratios `(t-r_i)/(t-r_j)` represent twice 2-torsion divisor classes.  The full five-element quotient basis still requires compatible handling of the node-cycle generators and the seven-dimensional `K*L*2` relation subspace.

```text
EXPLICIT_LCE_BASIS_MATERIALIZED=false
EXPLICIT_XALPHA_MATRIX_MATERIALIZED=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
