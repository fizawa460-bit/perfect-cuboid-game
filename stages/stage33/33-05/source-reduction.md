# Stage33-05 — K3 Br[2] Q(i)/Q descent source reduction

```text
STAGE33_UNIT=33-05
UNIT_STATUS=READY_FOR_AUDIT
MAIN_PRODUCTION_COMPLETE=true
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
K3_GEOMETRIC_BR2_DIM=2
Q_RELEVANT_SURVIVING_DIM=1
Q_RELEVANT_SURVIVING_DIM_EXACT=true
HOSTILE_AUDIT=PENDING
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

Over `Q(i)` the branch is `B+:X+iY=0`, `B-:X-iY=0`. Both are smooth `(2,2)` genus-one components meeting transversely in eight nodes. The certified K3 Picard rank is 20, hence `dim_F2 Br(K_cbar)[2]=2`.

## Exact finite execution sub-DAG

```text
05A branch normalization / branch Galois regression                         DONE
 |
 v
05B corrected L_{c,E} dimension + actual five-function basis                DONE
     Creutz--Viray divisor checks                                            DONE
     exact graph lifts                                                       DONE
 |
 v
05C true x-alpha pair audit
     old norm-level pure-Jac interpretation                                  SUPERSEDED
     J1 in im(x-alpha)                                                       DONE
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
05G CV-presentation connecting filter
     delta(J2)                                                                0
     delta(q1)                                                                ct -> J1
     |
     +--> 05G-J2 Hilbert-90 sqrt(2) elimination                              DONE
     |          Q-defined branch-algebra function                             DONE
     |          exact norm square                                             DONE
     |          vertical/horizontal residues                                  DONE
     |          simple-node exceptional residues                              DONE
     |          Q-defined unramified CSA                                      DONE
     |          J2 Q-descent                                                   DONE
     |
     +--> 05G-q1 integral NS lift D                                           DONE
                invariant odd-pairing non-norm certificate                    DONE
                Kummer/Leray Bockstein = HS d2 bridge                         DONE
                d2(q1)|_<ct>=[D] != 0                                         DONE
                q1 Q-descent                                                   REJECTED
 |
 v
05H exact arithmetic survival
     geometric invariant dimension                                            2
     surviving basis                                                          J2
     Q-relevant surviving dimension                                           1 EXACT
 |
 v
05I main-production disposition                                               READY_FOR_AUDIT
```

## Corrected finite presentation

On `z^2=t^4-6t^2+1`,

```text
L_E=L_{c,E} dimension = 5,
im(x-alpha) dimension = 3,
Br quotient dimension = 2.
```

In basis `[J1,J2,q1,q2,q3]`, true section graph projections are

```text
s=1                  -> q1+q2,
s=t                  -> q1+q2+q3,
s=-i*(t-i)/(t+i)     -> q1+q2,
```

with explicit square witness

```text
xalpha(-i*(t-i)/(t+i)) + xalpha(1) = J1.
```

Therefore

```text
im(x-alpha)
 = span_F2 {
     J1,
     b*J2+q1+q2,
     d*J2+q1+q2+q3
   }, b,d in F2,
```

and `[J2,q1]` is a quotient basis for every `b,d`.

The corrected full-pair action is

```text
tau = cc = identity,
ct(q1)=q1+J1,
ct(q2)=q2+J1,
ct(q3)=q3,
ct(J1)=J1,
ct(J2)=J2.
```

Thus `Br(K_cbar)[2]^G_Q` has dimension two and basis `[J2,q1]`.

## J2 arithmetic branch

Hilbert--90 gives the normalization representative

```text
ell_z=2*(t^2+z-3)/(t^2-2*t-1).
```

In

```text
L=Q(t)[alpha]/(t^2*(1-alpha^2)^2+alpha^2*(1-t^2)^2)
```

this becomes

```text
ell_J2=
4*(alpha^2*t^2+t^4-4*t^2+2)
 / ((t^2-1)*(t^2-2*t-1)).
```

The exact resultant is

```text
Norm_{L/Q(t)}(ell_J2)
 = 1024/(t^2-2*t-1)^4
 = (32/(t^2-2*t-1)^2)^2.
```

The geometric divisor is `4*infinity_minus-2*P1-2*P2`, hence all vertical branch valuations are even. Combined with the square norm and the Creutz--Viray simple-node exceptional-divisor criterion, this gives a Q-defined unramified corestriction class whose geometric image is `J2`.

```text
J2_Q_DESCENT_CERTIFIED=true
J2_GEOMETRIC_NONTRIVIAL=true
```

## q1 arithmetic branch

The presentation defect is

```text
ct(q1)-q1=J1.
```

The Stage29 ruled map closes the two sections producing `J1` to

```text
Cb : i*A1+B1=i*A2+B2=i*A3+B3=0,
E_P0, P0=[0:1:0:-1:0:1],
```

so an integral NS lift is

```text
D=Cb+E_P0.
```

Both are `ct`-invariant.  The invariant test conic

```text
T : A1=0, A2+B3=0, A3-B2=0
```

satisfies, by exact tangent-space calculation,

```text
Cb.T=1,
E_P0.T=0,
D.T=1.
```

Hence `D` cannot be `(1+ct)E`, since any norm has even pairing against an invariant test class. Therefore

```text
[D] != 0 in H^2(<ct>,Pic(K_cbar)).
```

For a K3, `Pic(K_cbar)` is torsion-free. Kummer supplies

```text
0 -> Pic/2 -> H^2_et(K_cbar,mu_2) -> Br(K_cbar)[2] -> 0.
```

Creutz--Viray's Galois-equivariant finite presentation is compatible with this Kummer lift: their `gamma` is the corestriction/cup-product construction, and their explicit Picard/divisor/Brauer cocycle calculation identifies the same defect.  Thus the `J1=D mod 2` presentation cocycle is the Kummer defect of `q1`.

For `C2=<ct>`, lifting the nontrivial 1-cocycle value by `D` gives

```text
(dJ)(ct,ct)=2D,
Bockstein(J1)(ct,ct)=D.
```

The Kummer/Leray naturality chase identifies this Bockstein with the restricted Hochschild--Serre differential. Therefore

```text
d2(q1)|_<ct>=[D] != 0,
d2(q1) != 0,
Q1_Q_DESCENT=false.
```

## Exact survival

Since `J2` descends and `q1` does not,

```text
ker(d2 | Br(K_cbar)[2]^G_Q)=span_F2{J2},
Q_RELEVANT_SURVIVING_DIM=1.
```

No unresolved arithmetic-descent unknown remains inside Stage33-05 main production.

## Source locks for the final bridge

- Stacks Project, tag `03PK`, Kummer theory, Lemma 59.28.1 and its long exact sequence.
- Stacks Project, tag `03QA` / Proposition 59.54.2, Leray spectral sequence.
- Brendan Creutz, Bianca Viray, *Two torsion in the Brauer group of a hyperelliptic curve*, Manuscripta Math. 147 (2015), Remark 3.1, Proposition 3.2, Lemmas 3.4--3.5.
- Brendan Creutz, Bianca Viray, *On Brauer groups of double covers of ruled surfaces*, Math. Ann. 362 (2015), Theorem 2.5 and Theorem I.
- Testa--Stoll verification source `MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma`, for the rank-20 torsion-free Picard lattice and known-curve geometry.

## Authoritative execution

```text
PAIR_REPAIR_CHECKER=xalpha_pair_galois_repair.py
DESCENT_FRONTEND_CHECKER=descent_presentation_cocycle.py
J2_ARITHMETIC_CHECKER=j2_arithmetic_descent.py
Q1_NS_CHECKER=q1_ns_lift_parity.py
Q1_HS_D2_CHECKER=q1_hs_d2_bockstein.py
LATEST_MATHEMATICAL_WORKFLOW_RUN=32712441163
LATEST_MATHEMATICAL_WORKFLOW_NUMBER=55
CONCLUSION=success
ARTIFACT_ID=9514610852
ARTIFACT_SHA256=075f4ec28170e62f86a895f9c65028a8daaa1516c5b2a2dba8298d710ebb5d3e
```

## Firewalls / disposition

```text
FULL_PAIR_GALOIS_ACTION_EXACT=true
GEOMETRIC_BR2_GQ_INVARIANT_DIMENSION=2
DESCENT_OBSTRUCTION_ACCOUNTED=true
Q_RELEVANT_SURVIVING_DIM_EXACT=true
Q_RELEVANT_SURVIVING_DIM=1
ALL_Q_SURVIVING_K3_BR2_CLASSES_HAVE_EXPLICIT_ARITHMETIC_REPRESENTATIVES=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
MAIN_PRODUCTION_COMPLETE=true
HOSTILE_AUDIT=PENDING
UNIT_STATUS=READY_FOR_AUDIT
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
```
