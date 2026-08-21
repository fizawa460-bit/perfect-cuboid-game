# Stage29-08 — fresh adversarial audit

```text
PR=1314
SUBMISSION_HEAD=a007164e8bc203d65d978e297ea9fef659b2f6b6
AUDIT_VERDICT=PASS_AFTER_MATERIAL_POSITIVE_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

## 1. Peschmann crosswalk — PASS

The Euclid-pair formulas

```text
e=U1*U2, x=V1*U2, y=U1*V2,
p=W1*U2, q=U1*W2
```

land on the exact Stage29-07 two-face model. On `e!=0`, with `t1=V1/U1`, `t2=V2/U2`, direct algebra gives

```text
Master/e^2=t1^2+t2^2=f_face
H-total/e^2=1+t1^2+t2^2=f_sp.
```

This is the same residual joint-V4 pair, not an analogy. Therefore

```text
R29-PESCH1=DISCHARGED
PESCHMANN_PROVEN_F2_ADAPTER=true
PESCHMANN_INDEPENDENT_FOUNDATION=false
```

## 2. Material positive repair — global Master-Hit coverage is actually proved

The submission left global Euler-brick coverage open because `arXiv:2604.28072` and `arXiv:2605.00573` contain contradictory scope statements. Fresh audit does not resolve this by choosing prose. It independently audits Theorem 2.4 and its proof in `2604.28072`.

Let `(X,Y,Z)` be a primitive Euler brick, with `X` its unique odd edge. Put

```text
d=gcd(X,Y), e=gcd(X,Z).
```

Then the two primitive Pythagorean faces give unique primitive Euclid pairs

```text
X/d=U1, Y/d=V1,
X/e=U2, Z/e=V2.
```

Primitivity gives `gcd(d,e)=1`. From `X=d*U1=e*U2`, with `g=gcd(U1,U2)`, one gets exactly

```text
d=U2/g, e=U1/g,
(X,Y,Z)=(U1U2/g, V1U2/g, U1V2/g).
```

Since the third face is integral,

```text
M=(V1U2)^2+(U1V2)^2=g^2*(Y^2+Z^2)
```

is a square, so the tuple is a Master-Hit. Thus every primitive Euler brick is the gcd-normalized representative of a Master-Hit. The Stage29-07 primitive normalization makes this an exact adapter, not merely an up-to-scale slogan.

For the space condition, the unnormalized Master-Hit brick is `g*(X,Y,Z)`, hence its space norm is `g^2*(X^2+Y^2+Z^2)`. Therefore squarehood is preserved both ways under the scaling/gcd normalization.

```text
PESCHMANN_GLOBAL_EULER_BRICK_COVERAGE_CERTIFIED=true
PESCHMANN_GLOBAL_ENDPOINT_COVERAGE_VIA_MASTER_HITS=true
R29-PESCH-COV=DISCHARGED_BY_INDEPENDENT_PROOF_AUDIT
```

The later `2605.00573` Remark 2.3 explicitly disclaims this converse. That is a genuine source contradiction, but it does not invalidate the independently checked proof in Theorem 2.4.

```text
PESCHMANN_SOURCE_CONTRADICTION_PRESENT=true
SOURCE_CONTRADICTION_INVALIDATES_CHECKED_THEOREM=false
```

## 3. Consequence for exponent-one blocker receiver

`2605.00573` Conjecture 4.1 remains conjectural and is only finitely verified. But after the global coverage theorem is certified, its logical strength changes: proving the universal exponent-one blocker for every Master-Hit would force the space norm to be nonsquare for every globally covered primitive endpoint candidate.

```text
R29-PESCH-E1=AMBER_CONJECTURAL_GLOBAL_ENDPOINT_BLOCKER
PESCH_E1_IF_PROVED_IMPLIES_PERFECT_CUBOID_NONEXISTENCE=true
PESCH_E1_CURRENTLY_PROVED=false
FINITE_VERIFICATION_IS_GLOBAL_THEOREM=false
```

No nonexistence conclusion is claimed now.

## 4. May Mordell-Weil fibration — PASS with lift-domain firewall

The quartic `H_mn` is exactly the Master/third-face equation. The `tau` test is exact only on

```text
E_mn(Q) minus ({O} union T_tau),
```

where `T_tau` is the two-torsion pole set. A positive rational square `tau(P)` gives `t` only after the positivity/parity/coprimality checks on the reduced Euclid pair. Thus the total `(m,n)` fibration is a globally covering marginal chart via Theorem 2.4, but a bounded Mordell-Weil enumeration is not globally exhaustive.

```text
PESCH_TOTAL_FIBRATION_GLOBAL_MARGINAL_COVERAGE=true
BOUNDED_MW_ENUMERATION_GLOBAL_COVERAGE=false
R29-PESCH2=OPEN_BOUNDED_FIBRATION_CLASS_AND_POLARIZATION_MATCH
```

## 5. Stage20 / K_c exact adapter — PASS

Quotienting the endpoint normal model by the long-diagonal sign forgets only `d` and leaves exactly the three face equations in `P5`. This is the Testa--Stoll normal Euler K3 `Kbar_c` and the Stage20 third-face completion normal model. Their minimal resolutions therefore agree over `Q`.

The physical polarization also matches at equation level:

```text
M_face=pi_face^*(-K_Y), M_face^2=8, h0(M_face)=6,
```

with the six physical sections `[e:x:y:p:q:z]`, i.e. the `P5` hyperplane system.

```text
R29-K1=DISCHARGED
STAGE20_X_FACE_EQUALS_TESTA_STOLL_K_C_AT_NORMAL_AND_RESOLUTION_LEVEL=true
PHYSICAL_POLARIZATION_MATCH=true
```

The analogous Stage19 statement is only for the physically labeled complementary `K_b` quotient; no arbitrary-orbit equality is inferred.

## 6. Fibration field-scope repair

Testa--Stoll's counts `28` genus-5 fibrations on the endpoint and `15` elliptic fibrations on `K_c` are valid geometric counts. They are not a certificate that every individual fibration is defined over `Q`. Rank-4 quadrics require a splitting field for their rulings; the first endpoint rank-4 pair is explicitly over `Q(i)`.

Therefore downstream arithmetic use must ledger field of definition per fibration.

```text
ENDPOINT_GENUS5_FIBRATION_COUNT=28_GEOMETRIC
ALL_28_FIBRATIONS_Q_DEFINED_CERTIFIED=false
EULER_K3_ELLIPTIC_FIBRATION_COUNT=15_GEOMETRIC
ALL_15_FIBRATIONS_Q_DEFINED_CERTIFIED=false
R29-FIB1=OPEN_PHYSICAL_CLASS_PLUS_FIELD_OF_DEFINITION_LEDGER
R29-FIB2=OPEN_ARITHMETIC_SPECIALIZATION_AND_RESIDUAL_SPACE_LIFT
```

Geometric fibration coverage is not rational-point coverage.

## 7. Existing family firewalls — PASS

Saunderson remains a thin Stage20 rational curve with the audited nonsplit endpoint genus-3 lift. StageA2 remains one specific family. Low-degree endpoint curve classification does not cover isolated points or higher-degree curves. No finite Peschmann database is promoted to a population or density theorem.

## 8. Routing

The global-coverage positive repair strengthens `J12-PARAMETRIC` but creates no twelfth route and requires no Stage16--28 backflow. `R29-PESCH-COV` is discharged; `R29-PESCH-E1` becomes a direct global endpoint theorem receiver inside the existing route.

```text
ATTACK_ROUTE_COUNT_RETAINED=11
ATTACK_CREDIT=false
TARGETED_BACKFLOW_REQUIRED=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
ROADMAP_REWRITE_REQUIRED=false
NEXT_ITEM=29-09_FULL_ENDPOINT_LOCAL_ARITHMETIC
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
