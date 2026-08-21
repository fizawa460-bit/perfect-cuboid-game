# Stage29-07 — adversarial audit

```text
AUDITED_PR=1313
AUDITED_SUBMISSION_HEAD=8adf4f0099c2dd59982b8afa8078b4366393e493
AUDIT_MODE=SIGN_TOWER_GLOBAL_MAP_PLUS_POPULATION_BIJECTION_PLUS_BOUNDARY_SCOPE
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
```

## Executive verdict

The central 29-07 bridge survives fresh audit. In particular, the two-face floor is an exact degree-16 subcover of the F7 degree-64 cover, the remaining two square roots give the exact residual V4 extension, and the Stage16--20 populations admit an exact selected-subcover incidence dictionary with the frozen primitive/canonical Euclidean cutoff.

One receiver-scope defect is repaired: the original receiver `R29-G1b=JointCoverBoundaryContractionAndExceptionalCurveLedger` cannot be called fully discharged while its explicit exceptional-curve ledger remains uncomputed. The bridge-relevant normal-model part is discharged; the residual exceptional table is retained as dormant bounded work, not falsely declared proved.

## 1. KUM3A — exact two-face degree-16 floor

Let

```text
T2bar={e^2+x^2=p^2, e^2+y^2=q^2} subset P4_[e:x:y:p:q].
```

The map

```text
rho2:T2bar -> P2_[E:X:Y],
[e:x:y:p:q] |-> [e^2:x^2:y^2]
```

is globally defined: `e=x=y=0` would force `p=q=0`, impossible in projective space. The coordinates `e,x,y,p,q` are integral over the square-coordinate base, so `rho2` is finite. On the generic fiber the five independent sign choices are quotiented by simultaneous projective sign, giving

```text
deg(rho2)=2^5/2=16,
generic deck=(Z/2)^4.
```

### Fresh singular-locus check

For

```text
Q1=e^2+x^2-p^2,
Q2=e^2+y^2-q^2,
```

the Jacobian rows are

```text
(2e,2x,0,-2p,0),
(2e,0,2y,0,-2q).
```

Rank drops exactly at

```text
[0:0:1:0:+1], [0:0:1:0:-1],
[0:1:0:+1:0], [0:1:0:-1:0].
```

For example, near `[0:1:0:1:0]`, the first equation eliminates the unit coordinate `p`, and the remaining local equation is analytically

```text
q^2=e^2+y^2,
```

an ordinary double point. The other three are identical by symmetry. Hence

```text
SING(T2bar)=4*A1.
```

### Fresh resolution/Stage28 identification

Use two Pythagorean parameters `[u1:v1],[u2:v2]` and write

```text
A1=v1^2-u1^2,
A2=v2^2-u2^2.
```

The five bidegree-(2,2) sections

```text
e=A1*A2,
x=2*u1*v1*A2,
p=(u1^2+v1^2)*A2,
y=2*u2*v2*A1,
q=(u2^2+v2^2)*A1
```

satisfy the two equations of `T2bar`. Their common base locus is exactly

```text
A1=A2=0,
```

namely four rational points on `P1 x P1`. Blowing them up gives

```text
Y=Bl_4(P1 x P1),
L=2H1+2H2-E1-E2-E3-E4=-K_Y,
L^2=4.
```

The generic inverse is recovered from

```text
u1/v1 = x/(p+e),
u2/v2 = y/(q+e)
```

on the usual dense chart, so the map is birational onto its image. Since the image has anticanonical degree four and lies in the degree-four complete intersection `T2bar`, it is exactly `T2bar`; resolving the four A1 points gives the Stage28 host `Y`.

Therefore

```text
R29-KUM3A=DISCHARGED_GLOBAL_NORMAL_SUBCOVER_PLUS_EXACT_STAGE28_RESOLUTION_ADAPTER.
```

## 2. KUM3B — the residual two-root V4 is literal

The endpoint equations over `T2bar` add exactly

```text
z^2=x^2+y^2,
d^2=e^2+x^2+y^2.
```

Forgetting `z,d` is globally defined for the same projective reason and is finite because `z,d` are integral over the base coordinate ring. Generically the two squareclasses are independent, hence

```text
Sbar -> T2bar
degree=4
generic deck=(Z/2)^2.
```

On `e!=0` the radicands are exactly

```text
f_face=(x/e)^2+(y/e)^2,
f_sp=1+(x/e)^2+(y/e)^2.
```

After base change to the resolution `Y`, uniqueness of normalization gives

```text
normalization(Y x_T2bar Sbar)
 = normalization of Y in Q(Y)(sqrt(f_face),sqrt(f_sp)),
```

which is the audited joint V4 model. No generic-to-global morphism promotion is needed beyond this normal-model statement.

```text
R29-KUM3B=DISCHARGED_EXACT_RESIDUAL_TWO_ROOT_V4.
```

## 3. The 4 -> 8 -> 16 -> 32 -> 64 selected-condition tower

The six independent projective F7 Kummer classes split as

```text
2 edge-ratio classes + 3 face classes + 1 space class.
```

The edge-root cover contributes degree four, and adjoining a fixed ordered list of the remaining four square roots gives generic degrees

```text
4,8,16,32,64.
```

This is a literal selected-predicate subcover tower. It is not a tower of exact populations `M1 -> M2 -> M3`, and a failed predicate is not a rational sign sheet.

```text
SELECTED_PREDICATE_LIFT_TOWER_IS_LITERAL=true
EXACT_M1_M2_M3_ARE_SUCCESSIVE_TOWER_FLOORS=false
BOOLEAN_16_EQUALS_SIGN_64=false
BOOLEAN_FAILURE_IS_SIGN_SHEET=false
```

## 4. KUM4B — exact population/subcover incidence dictionary

For an object with exactly `k` integral face diagonals there are exactly `C(k,j)` choices of a labeled `j`-subset of satisfied face predicates. Therefore

```text
I1=M1+2*M2+3*M3
I2=M2+3*M3
I3=M3

I1^S=N1+2*N2+3*P
I2^S=N2+3*P
I3^S=P.
```

At the selected two-face floor the residual predicates are the remaining face condition `C` and the space condition `S`. The exact incidence cells are

```text
C=0,S=0 : M2-N2
C=0,S=1 : N2
C=1,S=0 : 3*(M3-P)
C=1,S=1 : 3*P,
```

whose sum is `M2+3*M3=I2`. The factor three is selected-two-face incidence multiplicity, not V4 sheet multiplicity.

### Primitive normalization check

A rational point on a selected partial cover can be scaled so every represented coordinate is integral. Put `g=gcd(a,b,c)`. For every already-required integral diagonal `r`, its defining equation gives

```text
g^2 | r^2.
```

Prime-by-prime valuations then imply `g|r`; dividing all represented coordinates by `g` preserves integrality of every required diagonal. The resulting edge triple is primitive. Positivity fixes the sign orbit and `0<a<b<c` fixes the permutation orbit.

Conversely every primitive canonical physical object with the selected predicates yields exactly one positive labeled incidence point. Thus algebraic sheet degree is not physical multiplicity.

### Exact height check

The counting height is defined only after the unique primitive representative is selected:

```text
H_R=sqrt(a^2+b^2+c^2).
```

This is exactly the frozen physical `R`, regardless of whether the space square root is rational. Hence

```text
HEIGHT_POWER_LOSS=0
STANDARD_WEIL_HEIGHT_IDENTIFICATION_CLAIM=false.
```

All items left open in KUM4B are therefore supplied by an exact dictionary:

```text
R29-KUM4B=DISCHARGED_EXACT_PHYSICAL_POPULATION_TO_SELECTED_SUBCOVER_INCIDENCE_ADAPTER
R29-KUM4=DISCHARGED_AFTER_A_B_SPLIT
FULL_POPULATION_SUBCOVER_COUNT_ADAPTER=true.
```

This is a representation theorem for existing Stage16--20 populations, not a new asymptotic theorem.

## 5. G1b — submitted full-discharge wording rejected

The original receiver is

```text
R29-G1b=JointCoverBoundaryContractionAndExceptionalCurveLedger.
```

29-07 does prove the bridge-relevant global normal-model statement and the physical-open compatibility. It does not enumerate the complete exceptional-curve/contraction table. Therefore the safe disposition is

```text
R29-G1b-CORE=DISCHARGED_GLOBAL_NORMAL_MODEL_AND_PHYSICAL_OPEN
R29-G1b=PARTIAL_DISCHARGE_CORE_DONE
R29-G1b-EXC=DORMANT_BOUNDED_NOT_REQUIRED_FOR_CURRENT_BRIDGE
FULL_EXCEPTIONAL_CURVE_LEDGER_COMPLETE=false.
```

The dormant remainder may be reactivated only if a later argument genuinely needs the explicit contraction table. It does not block 29-08.

## 6. X1 routing

`R29-X1` remains open: the complete cross-quotient ADE/minimal-model enumeration is not proved. The existing representative local checks and normal-cover invariants are insufficient to call it discharged.

It is coherent to transfer primary execution ownership to `J12-JOINT-V4`, but the transfer is a route assignment, not attack credit and not a proof of the missing global table.

```text
R29-X1=OPEN_BOUNDED_GLOBAL_ADE_ENUMERATION
R29-X1_PRIMARY_OWNER=J12-JOINT-V4
X1_TRANSFER_EARNS_ATTACK_CREDIT=false.
```

## 7. Backflow and scope

KUM4B is now actually closed, so the conditional backflow watch that existed solely for that adapter may be removed. Nothing here changes or repairs a Stage16--28 certified theorem contract.

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[]
OLD_STAGE_CONTRACT_REPAIR_REQUIRED=false
NEW_POPULATION_ASYMPTOTIC=false
COVER_DEGREE_AS_POPULATION_SAVING=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false.
```

## Final state

```text
AUDIT_REQUIRED=false
CHECKPOINT29_07_AUDIT=PASS
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
BOUNDED_REPAIR=G1B_CORE_VS_EXCEPTIONAL_LEDGER_SCOPE_PLUS_EXACT_RESOLUTION_CROSSCHECK
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
R29_KUM3A=DISCHARGED
R29_KUM3B=DISCHARGED
R29_KUM4B=DISCHARGED
FULL_POPULATION_SUBCOVER_COUNT_ADAPTER=true
R29_G1b=PARTIAL_DISCHARGE_CORE_DONE_DORMANT_EXCEPTIONAL_REMAINDER
R29_X1=OPEN_TRANSFERRED_TO_J12_JOINT_V4
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[]
ROADMAP_REWRITE_REQUIRED=false
NEXT_ITEM=29-08_PARAMETRIZATION_FIBRATION_AND_COVERAGE_ATLAS
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
