# Stage29-07 — audited exact sign-tower / joint-V4 / population bridge

```text
STAGE=Stage29
ITEM=29-07_SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
STATUS=AUDITED_PASS_AFTER_BOUNDED_REPAIR
AUDIT_RECORD=stages/stage29/29-07/audit.md
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Exact degree-64 factorization

Fresh audit confirms the global finite factorization

\[
\boxed{\bar S\xrightarrow{4}\bar T_2\xrightarrow{16}\mathbf P^2_{F7}}
\]

with

\[
\bar T_2=\{e^2+x^2=p^2,\ e^2+y^2=q^2\}\subset\mathbf P^4.
\]

The maps and generic groups are

```text
T2bar -> P2_F7 : degree 16, (Z/2)^4
Sbar  -> T2bar : degree 4,  (Z/2)^2
Sbar  -> P2_F7 : degree 64, (Z/2)^6.
```

The degree-four residual cover adds exactly

```text
z^2=x^2+y^2
d^2=e^2+x^2+y^2,
```

so it is literally the third-face x space-diagonal V4 completion.

```text
R29-KUM3A=DISCHARGED
R29-KUM3B=DISCHARGED
```

## 2. Fresh exact Stage28 resolution cross-check

`T2bar` has exactly four singular points

```text
[0:0:1:0:+1], [0:0:1:0:-1],
[0:1:0:+1:0], [0:1:0:-1:0],
```

and each is A1.

An explicit two-Pythagorean anticanonical map gives the exact Stage28 resolution. For `[u_i:v_i] in P1`, put

```text
A1=v1^2-u1^2
A2=v2^2-u2^2

e=A1*A2
x=2*u1*v1*A2
p=(u1^2+v1^2)*A2
y=2*u2*v2*A1
q=(u2^2+v2^2)*A1.
```

These five `(2,2)` sections have exactly four basepoints `A1=A2=0`. Blowing them up gives

```text
Y=Bl_4(P1xP1),
-K_Y=2H1+2H2-E1-E2-E3-E4,
(-K_Y)^2=4.
```

The generic inverse is recovered by `u1/v1=x/(p+e)` and `u2/v2=y/(q+e)`, so the anticanonical map is birational onto the degree-four complete intersection `T2bar`.

After base change,

```text
normalization(Y x_T2bar Sbar)
 = normalization of Y in Q(Y)(sqrt(f_face),sqrt(f_sp)),
```

with

```text
f_face=(x/e)^2+(y/e)^2
f_sp=1+(x/e)^2+(y/e)^2.
```

This is the audited joint V4 model, not a lookalike birational surface.

## 3. Exact selected-predicate tower

The six F7 projective Kummer classes split as

```text
2 edge-ratio classes + 3 face classes + 1 space class.
```

After the edge-root floor, adjoining a fixed ordered list of the four physical square roots gives generic degrees

```text
4 -> 8 -> 16 -> 32 -> 64.
```

Therefore

```text
SELECTED_PREDICATE_LIFT_TOWER_IS_LITERAL=true
EXACT_M1_M2_M3_ARE_SUCCESSIVE_TOWER_FLOORS=false
BOOLEAN_16_EQUALS_SIGN_64=false
BOOLEAN_FAILURE_IS_SIGN_SHEET=false.
```

A YES predicate is rational lift to the next selected partial cover; a NO predicate is nonlift over Q, not another rational sign sheet.

## 4. Exact population/subcover incidence adapter

For exactly `k` integral face diagonals, a physical object contains `C(k,j)` labeled choices of `j` satisfied face predicates. Hence

\[
I_j=\sum_{k=j}^3 {k\choose j}M_k,
\qquad
I_j^S=\sum_{k=j}^3 {k\choose j}N_k,
\quad N_3=P.
\]

Explicitly,

```text
I1=M1+2*M2+3*M3
I2=M2+3*M3
I3=M3

I1^S=N1+2*N2+3*P
I2^S=N2+3*P
I3^S=P.
```

At the two-face floor the residual V4 cells are exactly

```text
third NO,  space NO  : M2-N2
third NO,  space YES : N2
third YES, space NO  : 3*(M3-P)
third YES, space YES : 3*P,
```

summing to `M2+3*M3`. The factor three is two-face incidence multiplicity inside a three-face cuboid, not algebraic V4 sheet multiplicity.

## 5. Primitive, sign, order and physical-height audit

A rational selected-partial-cover point can be scaled to integral represented coordinates. If `g=gcd(a,b,c)`, every represented integral diagonal `r` satisfies `g^2|r^2`, hence `g|r` prime by prime. Dividing by `g` therefore preserves every required integral diagonal and gives the unique primitive edge triple.

Then

```text
positivity       -> unique sign representative
0<a<b<c          -> canonical permutation representative
R=sqrt(a^2+b^2+c^2) -> exact frozen physical cutoff.
```

If the space condition fails, `R` is still the same real Euclidean norm; no rational `d` is needed to define the cutoff.

```text
PRIMITIVITY_ADAPTER=EXACT
CANONICAL_ORDER_ADAPTER=EXACT
HEIGHT_POWER_LOSS=0
ALGEBRAIC_SIGN_DEGREE_IS_PHYSICAL_MULTIPLICITY=false
STANDARD_WEIL_HEIGHT_IDENTIFICATION_CLAIM=false.
```

Therefore

```text
R29-KUM4A=DISCHARGED_BY_29_04
R29-KUM4B=DISCHARGED_EXACT_PHYSICAL_POPULATION_TO_SELECTED_SUBCOVER_INCIDENCE_ADAPTER
R29-KUM4=DISCHARGED_AFTER_A_B_SPLIT
FULL_POPULATION_SUBCOVER_COUNT_ADAPTER=true.
```

No new asymptotic or independent probability factor is claimed.

## 6. Bounded audit repair — G1b is not fully discharged

The historical receiver is

```text
R29-G1b=JointCoverBoundaryContractionAndExceptionalCurveLedger.
```

29-07 closes the global normal-model bridge and the physical-open compatibility, but it does not enumerate the complete exceptional-curve/contraction table. The submitted full-discharge wording is therefore narrowed to

```text
R29-G1b-CORE=DISCHARGED_GLOBAL_NORMAL_MODEL_AND_PHYSICAL_OPEN
R29-G1b=PARTIAL_DISCHARGE_CORE_DONE
R29-G1b-EXC=DORMANT_BOUNDED_NOT_REQUIRED_FOR_CURRENT_BRIDGE
FULL_EXCEPTIONAL_CURVE_LEDGER_COMPLETE=false.
```

The dormant remainder does not block 29-08 and is reactivated only if a later theorem actually needs it.

## 7. X1 remains open

The cross quotient retains the audited normal-cover/cohomological package

```text
K^2 signal=8
pg=5, q=0
non-Tate=2*h16+3*h8
representative visible singularities=ADE/crepant.
```

But the complete global ADE/minimal-model enumeration is not done.

```text
R29-X1=OPEN_BOUNDED_GLOBAL_ADE_ENUMERATION
R29-X1_PRIMARY_OWNER=J12-JOINT-V4
X1_TRANSFER_EARNS_ATTACK_CREDIT=false.
```

## 8. Backflow and route scope

KUM4B is now closed, so its conditional Stage16--28 backflow watch is removed. No frozen old-stage theorem contract changes.

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[]
OLD_STAGE_CONTRACT_REPAIR_REQUIRED=false
NEW_POPULATION_ASYMPTOTIC=false
COVER_DEGREE_AS_POPULATION_SAVING=false
ROADMAP_REWRITE_REQUIRED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false.
```

## 9. Final audit state

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_07_AUDIT=PASS
BOUNDED_REPAIR=G1B_CORE_VS_EXCEPTIONAL_LEDGER_SCOPE_PLUS_EXACT_RESOLUTION_CROSSCHECK
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ATTACK_ROUTE_COUNT_RETAINED=11
R29_KUM3A=DISCHARGED
R29_KUM3B=DISCHARGED
R29_KUM4B=DISCHARGED
FULL_POPULATION_SUBCOVER_COUNT_ADAPTER=true
R29_G1b=PARTIAL_DISCHARGE_CORE_DONE_DORMANT_EXCEPTIONAL_REMAINDER
R29_X1=OPEN_TRANSFERRED_TO_J12_JOINT_V4
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[]
NEXT_ITEM=29-08_PARAMETRIZATION_FIBRATION_AND_COVERAGE_ATLAS
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
