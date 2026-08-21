# Stage29-07 — exact sign-tower / joint-V4 / population bridge

```text
STAGE=Stage29
ITEM=29-07_SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Executive result

29-07 closes the main conceptual bridge that remained after 29-04/05/06.

The degree-64 F7 cover factors through the literal two-face canonical model:

\[
\boxed{
\bar S \xrightarrow{\;4\;} \bar T_2 \xrightarrow{\;16\;} \mathbf P^2_{F7}
}
\]

where

\[
\bar T_2=
\{e^2+x^2=p^2,\ e^2+y^2=q^2\}\subset\mathbf P^4.
\]

The generic groups are

```text
T2bar -> P2_F7 : (Z/2)^4, degree 16
Sbar  -> T2bar : (Z/2)^2, degree 4
Sbar  -> P2_F7 : (Z/2)^6, degree 64.
```

The residual degree-four cover adds exactly

```text
z^2=x^2+y^2                 # remaining third face
d^2=e^2+x^2+y^2             # space diagonal
```

and is exactly the joint V4 completion architecture of Stage29-02b / Stage28 after resolving the two-face base.

```text
R29-KUM3A=DISCHARGED_GLOBAL_NORMAL_SUBCOVER_PLUS_STAGE28_RESOLUTION_ADAPTER
R29-KUM3B=DISCHARGED_EXACT_RESIDUAL_TWO_ROOT_V4
```

## 2. Why the number 64 and the physical Boolean masks are related but not identical

The six independent F7 projective Kummer classes split naturally as

```text
2 edge-ratio classes
+ 3 face classes
+ 1 space class.
```

Thus

```text
64 = 2^6 = 4 * 16.
```

The factor `4` is the projective sign cover needed to recover rational edge ratios from `[e^2:x^2:y^2]`. Once an actual positive physical edge triple is fixed, those edge squareclasses are already trivial and only the four physical predicates remain.

For a selected ordering of those four predicates, the literal partial-cover degrees are

```text
edge roots only                     4
+ one selected face                 8
+ two selected faces               16
+ three selected faces             32
+ three faces + space              64.
```

This finally gives the precise version of the earlier informal picture:

```text
YES to selected predicate = rational lift to next partial cover
NO                       = failure to lift over Q
```

but

```text
NO is not another rational sign sheet.
```

Therefore

```text
BOOLEAN_MASKS_ARE_SIGN_SHEETS=false
SELECTED_PREDICATE_LIFT_TOWER_IS_LITERAL=true
```

## 3. Exact Stage28 adapter

The two-face model `T2bar` has exactly four `A1` singularities:

```text
[0:0:1:0:+1], [0:0:1:0:-1],
[0:1:0:+1:0], [0:1:0:-1:0].
```

The audited Stage28 weak-del-Pezzo surface

```text
Y=Bl_4(P1xP1), L=-K_Y, L^2=4
```

is the smooth resolution of this anticanonical P4 model. The Stage29 joint cover is therefore

```text
normalization(Y x_T2bar Sbar),
```

or equivalently the normalization of `Y` in

```text
Q(Y)(sqrt(f_face),sqrt(f_sp)),
f_face=(x/e)^2+(y/e)^2,
f_sp=1+(x/e)^2+(y/e)^2.
```

This is the exact global normal-model meaning of the old Stage28/29-02b dense-open bridge.

## 4. Population adapter: exact lift-incidence formulas

Let `M_k` denote exactly `k` integral face diagonals and define

```text
N1 = exactly one face + space
N2 = exactly two faces + space
N3 := P = exactly three faces + space.
```

For a choice of `j` satisfied face predicates, the literal selected-face incidence host has count

\[
\boxed{I_j=\sum_{k=j}^3 {k\choose j}M_k}
\]

and its space-positive part has count

\[
\boxed{I_j^S=\sum_{k=j}^3 {k\choose j}N_k}.
\]

Explicitly,

```text
I1 = M1 + 2 M2 + 3 M3
I2 = M2 + 3 M3
I3 = M3

I1^S = N1 + 2 N2 + 3 P
I2^S = N2 + 3 P
I3^S = P.
```

These are exact physical-object incidence identities, not asymptotics.

For the Stage28 two-face floor, the residual V4 states have exact counts

```text
third face NO,  space NO  : M2 - N2
third face NO,  space YES : N2
third face YES, space NO  : 3*(M3-P)
third face YES, space YES : 3*P.
```

Their sum is

```text
M2 + 3 M3.
```

The factor three is the number of two-face subsets inside a three-face cuboid. It is not the algebraic V4 sign multiplicity.

## 5. Height, signs, primitivity and ordering

The remaining KUM4B bookkeeping also closes exactly.

A positive rational partial-cover point is converted to a unique primitive physical representative by:

```text
clear denominators
-> divide by gcd(a,b,c)
-> impose 0<a<b<c
-> choose positive diagonal signs.
```

If the edge gcd is `g`, every already-required integral diagonal is divisible by `g`, so primitive normalization preserves the relevant square conditions.

The physical height is defined on the primitive representative by

```text
H_R=sqrt(a^2+b^2+c^2)=R.
```

If the space predicate succeeds, the rational `d` coordinate equals `R`; if it fails, the same real Euclidean norm still defines the frozen cutoff.

Hence

```text
HEIGHT_POWER_LOSS=0
ALGEBRAIC_SIGN_DEGREE_IS_PHYSICAL_MULTIPLICITY=false
PRIMITIVITY_ADAPTER=EXACT
CANONICAL_ORDER_ADAPTER=EXACT
```

No standard-Weil-height equivalence or asymptotic transfer is claimed.

## 6. KUM4 verdict

Stage29-04 had already discharged the pointwise squareclass crosswalk `KUM4A`. 29-07 now supplies the missing population/subcover dictionary:

```text
R29-KUM4A=DISCHARGED_POINTWISE_PHYSICAL_TO_F7_SQUARECLASS_CROSSWALK
R29-KUM4B=DISCHARGED_EXACT_PHYSICAL_POPULATION_TO_SELECTED_SUBCOVER_INCIDENCE_ADAPTER
R29-KUM4=DISCHARGED_AFTER_A_B_SPLIT
FULL_POPULATION_SUBCOVER_COUNT_ADAPTER=true
```

This does **not** turn the exact populations into successive tower floors:

```text
M1 -> M2 -> M3 is not objectwise survival.
```

Rather, exact strata are differences/intersections of rational lift loci on the selected-predicate tower.

## 7. Backflow verdict

Nothing proved here repairs or changes a frozen Stage16-28 theorem. It gives a new exact representation of those populations inside the Stage29 endpoint architecture.

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[]
OLD_STAGE_CONTRACT_REPAIR_REQUIRED=false
```

The old KUM4 conditional backflow watch can therefore be removed if fresh audit accepts the counting adapter.

## 8. G1b / X1 status

The exact finite factorization and base-change normalization close the global normal-model part of the old boundary adapter:

```text
R29-G1b=DISCHARGED_FOR_GLOBAL_NORMAL_MODEL_AND_PHYSICAL_OPEN
R29-G1b-EXC=OPTIONAL_BOUNDED_EXPLICIT_EXCEPTIONAL_CURVE_TABLE
```

The cross quotient remains useful but its complete global ADE/minimal-model ledger is not faked:

```text
R29-X1=OPEN_BOUNDED_GLOBAL_ADE_ENUMERATION
```

Already-audited data retained:

```text
cross K^2 signal = 8
cross pg=5, q=0
cross non-Tate = 2*h16+3*h8
visible local singularities = ADE/crepant
```

Proposed owner after 29-07 is `J12-JOINT-V4`, because the remaining global ADE table is attack-object detail rather than a blocker for the bridge.

## 9. Consequence for the Stage29 architecture

The central bridge is now not merely an analogy:

```text
F7 P2 square base
 -> edge-root floor
 -> selected face-condition subcovers
 -> exact two-face degree-16 floor T2bar / Stage28 Y resolution
 -> residual third-face x space V4
 -> full degree-64 endpoint Sbar.
```

At the same time, the firewall survives:

```text
16 Boolean success/failure masks != 64 sign sheets.
```

The exact relationship is:

```text
Boolean masks record whether rational lifts exist along four residual quadratic conditions;
sign sheets record the choices of square roots once those lifts exist.
```

## 10. Routing

```text
ATTACK_ROUTE_COUNT_RETAINED=11
SYNTHESIS_ATTACK_CREDIT=false
NEW_POPULATION_ASYMPTOTIC=false
ROADMAP_REWRITE_REQUIRED=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM=29-08_PARAMETRIZATION_FIBRATION_AND_COVERAGE_ATLAS
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```