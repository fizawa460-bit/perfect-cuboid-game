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
FULL_EXPLICIT_LCE_BASIS_MATERIALIZED=true
CREUTZ_VIRAY_DIVISOR_CONDITIONS_COMPLETE=true
EXTENSION_MIXING_COMPLETE=true
EXPLICIT_XALPHA_ROW_COUNT=2
EXPLICIT_XALPHA_ROW_RANK=2
FULL_XALPHA_MATRIX_MATERIALIZED=false
XALPHA_RESIDUAL_RELATION_DIMENSION=1
XALPHA_RESIDUAL_GRAPH_LINE_CANDIDATE_COUNT=7
BRAUER_QUOTIENT_DIMENSION=2
GEOMETRIC_BR2_GALOIS_ACTION_EXACT=true
GEOMETRIC_BR2_GALOIS_ACTION=IDENTITY
GEOMETRIC_BR2_GQ_INVARIANT_DIMENSION=2
DESCENT_OBSTRUCTION_ACCOUNTED=false
Q_DEFINED_ARITHMETIC_REPRESENTATIVES_MATERIALIZED=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact five-dimensional presentation input

The corrected Creutz--Viray computation is frozen at

```text
Jac(B)[2] dimension       = 4
dual graph b1             = 7
raw generator dimension   = 12
K*L^2 relation dimension  = 7
L_E=L_{c,E} dimension     = 5
im(x-alpha) dimension     = 3
Br(K_cbar)[2] dimension   = 2.
```

The common normalization is `z^2=t^4-6*t^2+1`.  The exact lifted basis from `cv_exact_graph_lifts_and_galois.py` is ordered

```text
[J1,J2,q1,q2,q3].
```

All three graph functions now satisfy the actual Creutz--Viray divisor conditions; the old parity-only `g3` pilot is retired.  The full extension mixing is materialized over the degree-eight normal splitting field.

## Two exact x-alpha rows

Two horizontal split divisors on the generic ruled fiber give actual `x-alpha` relations, not dimension-only predictions.

For `s=1`, after removing the diagonal `K(t)^*` factor `t^2-1`, the half-divisor class on `E:y^2=x^3-x` is `(0,0)=J1`.  For `s=t`, the corresponding half-divisor class is `(-1,0)=J1+J2`.  Hence

```text
s=1  -> [1,0,0,0,0]
s=t  -> [1,1,0,0,0]
```

and these rows have rank two.  Since the independently locked total image rank is three, only one relation remains.  Row operations using the two certified Jacobian rows put it in the exact normal form

```text
[0,0,a,b,c],  (a,b,c) != (0,0,0).
```

Thus the remaining NS restriction problem is reduced to selecting one of exactly seven graph lines.

## Quotient Galois action closes before the last graph line

The exact extension action on `[J1,J2,q1,q2,q3]` has the property that `tau` and `ct` change each `q_i` only by Jacobian directions, while `cc` is already the identity.  Because `J1,J2` are now certified `x-alpha` relations, all three generators act identically on the three-dimensional graph quotient.  Quotienting by any of the seven possible final graph lines therefore gives

```text
Br(K_cbar)[2] ~= (F2)^2
Galois action on Br(K_cbar)[2] = identity
Br(K_cbar)[2]^G_Q dimension = 2.
```

This is a geometric invariant-subspace statement only.  It does **not** yet prove that the two invariant geometric classes descend to arithmetic classes in `Br(K_c)/Br(Q)`; the Hochschild--Serre/descent obstruction and explicit representatives remain open.

Evidence before the present row certificate:

```text
workflow_run = 32699237446
workflow_conclusion = success
```

New exact checker:

```text
xalpha_split_section_rows.py
output = xalpha-two-rows-quotient-action.json
```

## Next exact leaf

The upstream Testa--Stoll verification source gives an explicit rank-20 saturated Picard generating set for `K_c`.  The next bounded computation is to restrict those generators to the ruled generic fiber until one non-Jacobian `x-alpha` row is found.  That one row selects the final graph line and immediately materializes an explicit two-symbol Brauer quotient.

```text
LEAF_ID=L33-05-RESTRICT-PICARD-GENERATORS-SELECT-1-OF-7-GRAPH-LINES
CLASS=2
NEW_THEOREM_REQUIRED=false
UPSTREAM_PICARD_RANK=20
REMAINING_GRAPH_LINE_CANDIDATES=7
REQUIRED_NEW_INDEPENDENT_XALPHA_ROW_COUNT=1
DESCENT_OBSTRUCTION_AFTER_THIS=true
```

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
