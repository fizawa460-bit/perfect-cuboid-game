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

## Exact finite execution sub-DAG — corrected current state

```text
05A branch normalization / branch Galois regression                         DONE
 |
 v
05B corrected L_{c,E} dimension + actual five-function basis                DONE
     Creutz--Viray divisor checks                                            DONE
     single-component graph-lift corrections                                 DONE
 |
 v
05C true x-alpha pair audit
     old norm-level pure-Jac row interpretation                              SUPERSEDED
     J1 in im(x-alpha) by explicit square witness                            DONE
     graph projection of s=1 = q1+q2                                         DONE
     graph projection of s=t = q1+q2+q3                                      DONE
     graph projection rank                                                    2 DONE
     total x-alpha rank                                                       3 LOCKED
     seven-graph-line selection                                               RETIRED
 |
 v
05D geometric Brauer quotient
     dimension                                                               2 LOCKED
     explicit quotient basis                                                  J2,q1 DONE
 |
 v
05E full-pair Galois repair
     tau                                                                      IDENTITY
     cc                                                                       IDENTITY
     ct                                                                       q1,q2 ADD J1
     quotient action on [J2,q1]                                               IDENTITY EXACT
 |
 v
05F geometric invariant subspace dimension                                   2 EXACT
 |
 v
05G Hochschild--Serre/descent obstruction + Q-defined representatives        OPEN ACTIVE
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

## True x-alpha repair

The lifted basis is ordered `[J1,J2,q1,q2,q3]`.  For a horizontal section `s=f(t)`, the actual generic-fiber `x-alpha` element is the pair

```text
(f-s_plus, f-s_minus)
```

in the two branch normalization fields, modulo diagonal `K(t)^*` and squares.  Consequently the old `Gp(f)/Gm(f)` norm computation is not by itself a full `x-alpha` row.

The exact repaired graph projections are

```text
s=1                  -> q1+q2,
s=t                  -> q1+q2+q3,
s=-i*(t-i)/(t+i)     -> q1+q2.
```

The first and third have the same graph class.  Their ratio is computed exactly on `z^2=q`; an explicit square witness proves

```text
xalpha(-i*(t-i)/(t+i)) + xalpha(1) = J1.
```

Thus `J1` is an exact relation.  The two graph projections from `s=1` and `s=t` are independent, so together with `J1` they already have rank three.  Since the independently locked image rank is three, the entire image is

```text
im(x-alpha)
 = span_F2 {
     J1,
     b*J2+q1+q2,
     d*J2+q1+q2+q3
   },
   b,d in F2.
```

The unresolved `J2` coefficients `b,d` are immaterial for the quotient: for every choice, `[J2,q1]` is a basis of `L_{c,E}/im(x-alpha)`.  Therefore neither a blind rank-20 restriction matrix nor the former seven-line search is required to enter arithmetic descent.

## Full-pair Galois correction

The exact half-point calculations in `cv_exact_graph_lifts_and_galois.py` are retained as single-component data.  They must be combined with the conjugate branch component before reading the action on

```text
L=k(B+) x k(B-).
```

Using

```text
cc*tau*cc = tau,
cc*ct*cc  = tau*ct
```

in the degree-eight normal splitting field gives the full-pair action

```text
tau = identity,
cc  = identity,
ct(q1)=q1+J1,
ct(q2)=q2+J1,
ct(q3)=q3,
ct(J1)=J1,
ct(J2)=J2.
```

Because `J1` is in `im(x-alpha)`, the induced action on the quotient basis `[J2,q1]` is identity.  Hence

```text
Br(K_cbar)[2]^G_Q = Br(K_cbar)[2]
dimension = 2.
```

This is geometric invariance, not arithmetic descent.

## Upstream Picard source lock

The immutable Testa--Stoll verification source remains load-bearing for rank 20 and 2-saturation, with primitive generating indices

```text
[2,4,5,7,9,10,20,21,26,35,39,42,44,47,49,52,54,64,67,72].
```

However, the former task of restricting these generators merely to choose one of seven residual graph lines is retired by the exact pair repair above.

## Authoritative repair execution

```text
CHECKER=xalpha_pair_galois_repair.py
CERTIFICATE=xalpha-pair-galois-repair.json
WORKFLOW_RUN=32710572932
WORKFLOW_NUMBER=39
CONCLUSION=success
ARTIFACT_ID=9513914592
ARTIFACT_SHA256=f909a226bffb4a469ae9cc85458742caac38598a2f70c7358ff5652de6e26fa4
```

## Current exact leaf

Creutz--Viray Theorem I is explicitly an exact sequence of Galois modules over the separable closure.  It supplies the geometric presentation and supports Galois analysis, but it does not identify `Br(K_c)` with all Galois-fixed elements of `Br(K_cbar)`.  The paper itself emphasizes that arithmetic use needs representatives defined over the ground field.

The remaining receiver is therefore

```text
LEAF_ID=L33-05-HOCHSCHILD-SERRE-DESCENT-OF-J2-Q1
CLASS=2
NEW_THEOREM_REQUIRED=false
GEOMETRIC_BRAUER_BASIS=J2,q1
GEOMETRIC_GQ_INVARIANT_DIMENSION=2
REQUIRED_OUTPUT=DESCENT_OBSTRUCTION_FOR_EACH_BASIS_CLASS
                PLUS_Q_DEFINED_CSA_REPRESENTATIVES_FOR_SURVIVORS
```

## Firewalls / closure target

```text
FULL_PAIR_GALOIS_ACTION_EXACT=true
GEOMETRIC_BR2_GQ_INVARIANT_DIMENSION=2
EXPLICIT_GEOMETRIC_BRAUER_QUOTIENT_BASIS=true
GEOMETRIC_INVARIANT_IMPLIES_ARITHMETIC_DESCENT=false
DESCENT_OBSTRUCTION_ACCOUNTED=false
Q_RELEVANT_SURVIVING_DIM_EXACT=false
ALL_SURVIVING_K3_CLASSES_HAVE_EXPLICIT_ARITHMETIC_REPRESENTATIVES=false
UNRESOLVED_UNKNOWN_IN_SCOPE>0
HOSTILE_AUDIT=PENDING
```
