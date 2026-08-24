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
TRUE_XALPHA_PAIR_REPAIR_EXACT=true
J1_IN_XALPHA_IMAGE_EXACT=true
XALPHA_GRAPH_PROJECTION_RANK=2
XALPHA_IMAGE_SPANNED_EXACTLY=true
SEVEN_GRAPH_LINE_SEARCH_RETIRED=true
BRAUER_QUOTIENT_DIMENSION=2
EXPLICIT_GEOMETRIC_BRAUER_QUOTIENT_BASIS=J2,q1
FULL_PAIR_GALOIS_ACTION_EXACT=true
GEOMETRIC_BR2_GALOIS_ACTION=IDENTITY
GEOMETRIC_BR2_GQ_INVARIANT_DIMENSION=2
DESCENT_OBSTRUCTION_ACCOUNTED=false
Q_DEFINED_ARITHMETIC_REPRESENTATIVES_MATERIALIZED=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact five-dimensional presentation

The corrected Creutz--Viray computation remains frozen at

```text
Jac(B)[2] dimension       = 4
dual graph b1             = 7
raw generator dimension   = 12
K*L^2 relation dimension  = 7
L_E=L_{c,E} dimension     = 5
im(x-alpha) dimension     = 3
Br(K_cbar)[2] dimension   = 2.
```

The common normalization is

```text
z^2=t^4-6t^2+1,
s_plus =  i*(1-t^2+z)/(2*t),
s_minus = -i*(1-t^2+z)/(2*t).
```

The lifted `L_{c,E}` basis is ordered

```text
[J1,J2,q1,q2,q3],
```

where `J1,J2` are the two Jacobian squareclasses and

```text
q1=e1+e3,
q2=e1+e5,
q3=e1+e7
```

are the graph-quotient classes.

## Supersession of the old two-row pilot

`xalpha_split_section_rows.py` remains only as a norm-level regression.  Its former interpretation

```text
s=1 -> J1,
s=t -> J1+J2
```

as full `x-alpha` rows is superseded.

Creutz--Viray `x-alpha` on a horizontal section `s=f(t)` is represented on the two normalized branch components by the pair

```text
(f-s_plus, f-s_minus)
```

modulo the diagonal `K(t)^*` class and componentwise squares.  Computing the actual node incidences gives

```text
s=1                    -> graph q1+q2,
s=t                    -> graph q1+q2+q3,
s=-i*(t-i)/(t+i)       -> graph q1+q2.
```

Thus the first two graph projections are independent.

The two sections `s=1` and `s=-i*(t-i)/(t+i)` have the same graph projection.  Their quotient is therefore Jacobian-only.  `xalpha_pair_galois_repair.py` gives an explicit square witness on `z^2=t^4-6t^2+1` and proves exactly

```text
xalpha(-i*(t-i)/(t+i)) + xalpha(1) = J1.
```

Hence `J1` is in `im(x-alpha)`.

Together with the two independent graph projections and the independently locked total image dimension three, this determines the image exactly up to two immaterial `J2` coefficients:

```text
im(x-alpha)
 = span_F2 {
     J1,
     b*J2 + q1+q2,
     d*J2 + q1+q2+q3
   },
   b,d in F2.
```

The values of `b,d` do not affect the quotient.  For all four possibilities the classes

```text
[J2,q1]
```

map to a basis of the two-dimensional geometric Brauer quotient.  Therefore the former residual-seven-graph-line search is retired; restricting twenty Picard generators merely to select one of seven graph lines is no longer a required leaf.

## Full-pair Galois action repair

`cv_exact_graph_lifts_and_galois.py` correctly computes the half-point correction on one branch component, but its old 5D matrices must not be read as the action on the full pair in

```text
L = k(B+) x k(B-).
```

After combining the two components, the exact action on `[J1,J2,q1,q2,q3]` is

```text
tau = identity,
cc  = identity,
ct(q1)=q1+J1,
ct(q2)=q2+J1,
ct(q3)=q3,
ct(J1)=J1,
ct(J2)=J2.
```

Since `J1` is an exact `x-alpha` relation, all three generators induce the identity on the quotient basis `[J2,q1]`.  Hence

```text
Br(K_cbar)[2] ~= (F2)^2,
G_Q action on Br(K_cbar)[2] = identity,
Br(K_cbar)[2]^G_Q dimension = 2.
```

This is still a geometric invariant statement.  It does **not** by itself certify that either invariant class lies in the image of `Br(K_c)` over `Q`.

## Authoritative repair certificate

```text
checker = xalpha_pair_galois_repair.py
output  = xalpha-pair-galois-repair.json
workflow_run = 32710572932
workflow_number = 39
workflow_conclusion = success
artifact_id = 9513914592
artifact_sha256 = f909a226bffb4a469ae9cc85458742caac38598a2f70c7358ff5652de6e26fa4
```

## Next exact leaf

The next wall is no longer geometric quotient construction.  It is arithmetic descent of the two explicit geometric quotient classes:

```text
LEAF_ID=L33-05-HOCHSCHILD-SERRE-DESCENT-OF-J2-Q1
CLASS=2
NEW_THEOREM_REQUIRED=false
GEOMETRIC_QUOTIENT_BASIS=J2,q1
GEOMETRIC_INVARIANT_DIMENSION=2
REQUIRED_OUTPUT=DESCENT_OBSTRUCTION_PLUS_Q_DEFINED_ARITHMETIC_REPRESENTATIVES
```

Theorem I of Creutz--Viray gives the finite presentation as a Galois module; its introduction explicitly warns that invariant group structure alone does not replace explicit arithmetic representatives.  Stage33-05 therefore keeps the firewall

```text
DESCENT_OBSTRUCTION_ACCOUNTED=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
