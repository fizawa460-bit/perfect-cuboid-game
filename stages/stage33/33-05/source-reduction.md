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

Use the audited Stage29 ruled model

```text
A1=v1^2-u1^2,
A2=v2^2-u2^2,
X=u1*v1*A2,
Y=u2*v2*A1,
w^2=X^2+Y^2.
```

Over `Q(i)` the branch is `B+:X+iY=0`, `B-:X-iY=0`.  Both components are smooth `(2,2)` genus-one curves meeting transversely in eight nodes.  The certified K3 Picard rank is 20, hence `dim_F2 Br(K_cbar)[2]=2`.

## Exact finite execution sub-DAG — current state

```text
05A branch normalization / branch Galois regression                    DONE
 |
 v
05B corrected L_{c,E} dimension + actual five-function basis           DONE
     Creutz--Viray divisor checks + extension mixing                    DONE
 |
 +-------> 05C source-lock saturated rank-20 Pic(K_c) generators        DONE_SOURCE_LOCK
              ruled generic-fiber restriction                           ACTIVE
              |
              v
05D x-alpha relation matrix
     total rank locked                                                   3
     explicit rows from s=1 and s=t                                     2/3 DONE
     residual row reduced to one nonzero graph line                     1/7 SELECTION OPEN
 |
 v
05E Br quotient dimension                                                2 LOCKED
     abstract quotient Galois action                                     IDENTITY EXACT
     explicit two-symbol quotient basis                                  WAITS ON FINAL GRAPH LINE
 |
 v
05F geometric invariant subspace dimension                               2 EXACT
 |
 v
05G Hochschild--Serre/descent obstruction + arithmetic representatives   OPEN
```

## Corrected finite dimensions

For `W=P1_t`, the common branch normalization is

```text
z^2=q(t), q=t^4-6t^2+1.
```

Including both the four smooth ramification fibers and the four nodal even-`e(b/w)` fibers gives

```text
Jac(B)[2] dimension              = 4
dual graph b1                    = 7
special even-e fibers            = 8
raw generator subspace mod L*2   = 12
kernel to K*L*2                  = 7
L_E=L_{c,E} dimension            = 5
im(x-alpha) dimension            = 3
Br quotient dimension            = 2.
```

The former 9-dimensional pilot omitted the nodal fibers and remains superseded.

## New exact x-alpha reduction

The lifted basis is ordered `[J1,J2,q1,q2,q3]`.  Two split horizontal divisors give

```text
s=1 -> J1       -> [1,0,0,0,0]
s=t -> J1+J2    -> [1,1,0,0,0].
```

These are exact Creutz--Viray `x-alpha` rows and have rank two.  Since the total image rank is independently three, row operations reduce the only missing relation to

```text
[0,0,a,b,c], (a,b,c) nonzero.
```

There are exactly seven remaining graph lines.  No rank-20 blind matrix construction is needed anymore: it suffices to restrict certified Picard generators until one non-Jacobian row appears.

The already materialized field action changes each `q_i` only by `J1,J2`, and complex conjugation is identity on the lifted basis.  Since `J1,J2` are now relations, the induced action on the graph quotient is identity.  Therefore the final 2D geometric Brauer quotient has identity Galois action for **every** one of the seven possible residual graph lines.

This closes geometric invariance only; it does not kill the arithmetic descent obstruction.

## Upstream Picard source lock

The immutable Testa--Stoll verification source constructs the K3 Picard group from known curves, checks rank 20 and 2-saturation, and uses the primitive generating indices

```text
[2,4,5,7,9,10,20,21,26,35,39,42,44,47,49,52,54,64,67,72].
```

The current leaf transports/restricts this finite generator set through the explicit ruled-model map; the first certified non-Jacobian row selects the final graph line.

## Current exact leaf

```text
LEAF_ID=L33-05-RESTRICT-PICARD-GENERATORS-SELECT-1-OF-7-GRAPH-LINES
CLASS=2
NEW_THEOREM_REQUIRED=false
UPSTREAM_GENERATOR_COUNT=20
KNOWN_XALPHA_ROW_RANK=2
REQUIRED_TOTAL_XALPHA_ROW_RANK=3
REMAINING_GRAPH_LINE_CANDIDATES=7
OUTPUT=FINAL_3x5_XALPHA_MATRIX_PLUS_EXPLICIT_2_SYMBOL_BRAUER_QUOTIENT
```

## Firewalls / closure target

```text
GEOMETRIC_BR2_GALOIS_ACTION_EXACT=true
GEOMETRIC_BR2_GQ_INVARIANT_DIMENSION=2
GEOMETRIC_INVARIANT_IMPLIES_ARITHMETIC_DESCENT=false
DESCENT_OBSTRUCTION_ACCOUNTED=false
Q_RELEVANT_SURVIVING_DIM_EXACT=false
ALL_SURVIVING_K3_CLASSES_HAVE_EXPLICIT_ARITHMETIC_REPRESENTATIVES=false
UNRESOLVED_UNKNOWN_IN_SCOPE>0
HOSTILE_AUDIT=PENDING
```
