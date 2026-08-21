# Stage29-08 — audited parametrization, fibration and coverage atlas

```text
STAGE=Stage29
ITEM=29-08_PARAMETRIZATION_FIBRATION_AND_COVERAGE_ATLAS
STATUS=AUDITED_PASS_PENDING_MERGE
AUDIT_VERDICT=PASS_AFTER_MATERIAL_POSITIVE_REPAIR
ATTACK_CREDIT=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Exact Peschmann crosswalk — discharged

For

```text
(U1,V1,W1)=(a^2-b^2,2ab,a^2+b^2)
(U2,V2,W2)=(m^2-n^2,2mn,m^2+n^2)
```

and

```text
e=U1U2, x=V1U2, y=U1V2,
t1=x/e=V1/U1, t2=y/e=V2/U2,
```

direct algebra gives

```text
Master/e^2=t1^2+t2^2=f_face
H-total/e^2=1+t1^2+t2^2=f_sp.
```

Thus Peschmann is an exact chart of the audited two-face / residual joint-V4 architecture, not a ninth endpoint foundation.

```text
R29-PESCH1=DISCHARGED
PESCHMANN_PROVEN_F2_ADAPTER=true
PESCHMANN_INDEPENDENCE_RESOLVED=true
PESCHMANN_INDEPENDENT_FOUNDATION=false
```

## 2. Material positive repair — global coverage is proved

The submission left global Euler-brick coverage open because `arXiv:2604.28072` and `arXiv:2605.00573` make contradictory scope statements. Fresh audit independently re-derived Theorem 2.4 of `2604.28072` and accepts its proof.

For a primitive Euler brick `(X,Y,Z)` with unique odd edge `X`, set

```text
d=gcd(X,Y), e=gcd(X,Z).
```

The two primitive Pythagorean faces uniquely give

```text
X/d=U1, Y/d=V1,
X/e=U2, Z/e=V2.
```

Primitivity gives `gcd(d,e)=1`; hence with `g=gcd(U1,U2)`,

```text
d=U2/g, e=U1/g,
(X,Y,Z)=(U1U2/g, V1U2/g, U1V2/g).
```

The third-face condition gives

```text
Master=g^2*(Y^2+Z^2)=square.
```

So every primitive Euler brick is exactly the gcd-normalized representative of a Master-Hit. Space-squarehood is invariant under the same scaling. Therefore every primitive perfect-cuboid candidate is also covered.

```text
PESCHMANN_GLOBAL_EULER_BRICK_COVERAGE_CERTIFIED=true
PESCHMANN_GLOBAL_ENDPOINT_COVERAGE_VIA_MASTER_HITS=true
R29-PESCH-COV=DISCHARGED_BY_INDEPENDENT_PROOF_AUDIT
PESCHMANN_SOURCE_CONTRADICTION_PRESENT=true
```

The later disclaimer is recorded as a source contradiction; it does not overturn the independently checked theorem.

## 3. Exponent-one blocker becomes a global endpoint receiver

The May-2026 exponent-one blocker remains Conjecture 4.1 and is only finitely verified. But the coverage dependency is gone. If it is proved for every Master-Hit, then every globally covered endpoint candidate has nonsquare space norm.

```text
R29-PESCH-E1=AMBER_CONJECTURAL_GLOBAL_ENDPOINT_BLOCKER
PESCH_E1_IF_PROVED_IMPLIES_PERFECT_CUBOID_NONEXISTENCE=true
PESCH_E1_CURRENTLY_PROVED=false
FINITE_VERIFICATION_IS_NOT_THEOREM=true
```

This is a strengthened attack receiver, not a present nonexistence theorem.

## 4. May Mordell-Weil fibration

`H_mn` is exactly the Master/third-face marginal quartic. Its Weierstrass lift criterion is

```text
P in E_mn(Q) \ ({O} union T_tau)
tau(P) in Q_{>0}^square
```

followed by the reduced Euclid positivity/parity/coprimality checks. The total `(m,n)` fibration is a globally covering Euler-marginal atlas by the reduction theorem, but any bounded Mordell-Weil enumeration remains finite.

```text
PESCH_TOTAL_FIBRATION_GLOBAL_MARGINAL_COVERAGE=true
BOUNDED_MW_ENUMERATION_GLOBAL_COVERAGE=false
R29-PESCH2=OPEN_BOUNDED_FIBRATION_CLASS_AND_POLARIZATION_MATCH
```

## 5. Stage20 / Testa--Stoll Euler K3 adapter — discharged

Quotienting the endpoint by the space-diagonal sign forgets `d` and leaves exactly the three face equations in `P5`, i.e. both the Testa--Stoll normal Euler K3 `Kbar_c` and the Stage20 third-face completion. Their minimal resolutions agree over `Q`.

The physical polarization is the same `P5` hyperplane system:

```text
M_face=pi_face^*(-K_Y)
M_face^2=8
h0(M_face)=6
sections=[e:x:y:p:q:z].
```

```text
R29-K1=DISCHARGED
STAGE20_X_FACE_EQUALS_TESTA_STOLL_K_C_AT_NORMAL_AND_RESOLUTION_LEVEL=true
PHYSICAL_POLARIZATION_MATCH=true
```

## 6. Fibration field firewall

The Testa--Stoll counts are retained as geometric counts:

```text
ENDPOINT_GENUS5_FIBRATION_COUNT=28_GEOMETRIC
EULER_K3_ELLIPTIC_FIBRATION_COUNT=15_GEOMETRIC
```

but not every individual fibration is certified over `Q`. Rank-4 rulings require splitting fields; the first endpoint pair is explicitly over `Q(i)`. Downstream arithmetic must therefore record the field of definition per fibration.

```text
ALL_28_FIBRATIONS_Q_DEFINED_CERTIFIED=false
ALL_15_FIBRATIONS_Q_DEFINED_CERTIFIED=false
R29-FIB1=OPEN_PHYSICAL_CLASS_PLUS_FIELD_OF_DEFINITION_LEDGER
R29-FIB2=OPEN_ARITHMETIC_SPECIALIZATION_AND_RESIDUAL_SPACE_LIFT
```

Geometric fibration coverage is not rational-section or rational-point coverage.

## 7. Other family scopes

Saunderson remains a thin Stage20 curve; StageA2 remains one specific family; the low-degree endpoint theorem classifies curves only in its stated degree range. The 1,072 Peschmann exclusions and larger databases remain finite computations.

## 8. Routing

No new attack route is created. `J12-PARAMETRIC` is materially strengthened because global Master-Hit coverage is now certified, but the existing R2 order remains valid.

```text
ATTACK_ROUTE_COUNT_RETAINED=11
TARGETED_BACKFLOW_REQUIRED=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
ROADMAP_REWRITE_REQUIRED=false
AUDIT_REQUIRED=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-09_FULL_ENDPOINT_LOCAL_ARITHMETIC
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
