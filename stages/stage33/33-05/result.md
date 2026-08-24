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
CV_PRESENTATION_CONNECTING_COCYCLE_EXACT=true
J2_FIXED_LCE_LIFT_EXISTS=true
Q1_FIXED_LCE_LIFT_EXISTS=false
J2_QI_GENERIC_FUNCTION_MATERIALIZED=true
DESCENT_OBSTRUCTION_ACCOUNTED=false
Q_DEFINED_ARITHMETIC_REPRESENTATIVES_MATERIALIZED=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact geometric presentation

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

The common normalization is

```text
z^2=t^4-6t^2+1,
s_plus =  i*(1-t^2+z)/(2*t),
s_minus = -i*(1-t^2+z)/(2*t),
```

and the exact `L_{c,E}` basis is `[J1,J2,q1,q2,q3]` with graph classes

```text
q1=e1+e3,
q2=e1+e5,
q3=e1+e7.
```

## True x-alpha repair

The old `xalpha_split_section_rows.py` pure-Jac row interpretation is superseded; it remains only a norm-level regression.  The actual section class is the pair

```text
(f-s_plus, f-s_minus)
```

modulo diagonal `K(t)^*` and component squares.  Exact node incidences give

```text
s=1                    -> graph q1+q2,
s=t                    -> graph q1+q2+q3,
s=-i*(t-i)/(t+i)       -> graph q1+q2.
```

An explicit square witness proves

```text
xalpha(-i*(t-i)/(t+i)) + xalpha(1) = J1,
```

so `J1` lies in `im(x-alpha)`.  Since the first two graph projections are independent and the total image dimension is independently three,

```text
im(x-alpha)
 = span_F2 {
     J1,
     b*J2+q1+q2,
     d*J2+q1+q2+q3
   },
   b,d in F2.
```

The two undetermined `J2` coefficients do not affect the quotient: for every `b,d`, `[J2,q1]` maps to a basis of the two-dimensional geometric Brauer quotient.  The former seven-graph-line/Picard-generator search is therefore retired.

## Full-pair Galois action

The old half-point corrections remain valid as single-component data but are not the full action on `L=k(B+) x k(B-)`.  The corrected full-pair action is

```text
tau = identity,
cc  = identity,
ct(q1)=q1+J1,
ct(q2)=q2+J1,
ct(q3)=q3,
ct(J1)=J1,
ct(J2)=J2.
```

Because `J1` is an `x-alpha` relation, the action induced on `[J2,q1]` is identity.  Thus

```text
Br(K_cbar)[2] ~= (F2)^2,
Br(K_cbar)[2]^G_Q dimension = 2.
```

This remains geometric invariance only.

## First exact descent filter: presentation connecting cocycle

Apply Galois invariants to the finite presentation

```text
0 -> R=im(x-alpha) -> L_{c,E} -> Br(K_cbar)[2] -> 0.
```

For every value of the immaterial coefficients `b,d`, the full-pair `ct` action fixes `R` pointwise.  Hence for the effective `C2` action

```text
H^1(C2,R)=Hom(C2,R)=R
```

and there are no nonzero coboundaries.

The exact connecting classes of the geometric quotient basis are

```text
J2 : delta(ct)=0,
q1 : delta(ct)=J1 != 0.
```

Therefore

```text
J2 has a Galois-fixed L_{c,E} lift,
q1 has no Galois-fixed L_{c,E} lift,
```

and adding any `x-alpha` relation does not remove the `q1` cocycle.  This is a genuine split in the arithmetic workload.

Important firewall: this connecting class belongs to the Creutz--Viray presentation exact sequence.  It is **not yet identified with the Hochschild--Serre d2 obstruction**.  In particular `q1` is not declared non-descending; its `J1` cocycle must first be lifted through the Neron--Severi/divisor relation.

## J2: explicit Q(i)-level generic function

The `J2` component squareclass initially uses `sqrt(2)`.  The new checker removes it exactly by a Hilbert-90 computation.  With

```text
f2=(t+1+sqrt(2))/(t-1+sqrt(2)),
h=((t-(sqrt(2)-1))*(t-(1-sqrt(2))))/z,
h*ct(h)=1,
g=1+h,
```

one has `ct(g)/g=1/h`, and

```text
f2*g^2
 = 2*(t^2+z-3)/(t^2-2*t-1)
```

on `z^2=t^4-6t^2+1`.  The right-hand side contains no `sqrt(2)`, so a `Q(i)`-defined generic branch-component function representing the geometric `J2` squareclass is materialized.

This does **not** yet certify an unramified arithmetic CSA over `Q(i)`: as Creutz--Viray's arithmetic example illustrates, geometric unramifiedness does not by itself rule out ground-field nonsquare residues on exceptional divisors.  Those residue checks and subsequent `Q(i)/Q` descent remain open.

## Authoritative exact execution

```text
xalpha repair checker        = xalpha_pair_galois_repair.py
presentation descent checker = descent_presentation_cocycle.py
latest workflow_run          = 32710954883
latest workflow_number       = 43
latest workflow_conclusion   = success
artifact_id                  = 9514049977
artifact_sha256              = a249ff59ed92bec4e75acea7b8f0c6050b4787e7b0184f2587be8684cafb48b2
```

## Next exact leaves

The single descent leaf has now split into two bounded receivers:

```text
L33-05-J2-QI-ARITHMETIC-RESIDUES-AND-QI-OVER-Q-DESCENT
L33-05-Q1-LIFT-CONNECTING-J1-THROUGH-NS-THEN-HS-D2
```

Required before closure:

```text
DESCENT_OBSTRUCTION_ACCOUNTED=false
Q_DEFINED_ARITHMETIC_REPRESENTATIVES_MATERIALIZED=false
Q_RELEVANT_SURVIVING_DIM=NOT_YET_CERTIFIED
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
