# Stage29-06 — global foundation synthesis / endpoint-hub graph

```text
STAGE=Stage29
ITEM=29-06_GLOBAL_FOUNDATION_SYNTHESIS
MODE=PRE_ATTACK_SYNTHESIS
ROADMAP_REVISION=R2_POST_29_02_FOUNDATION_SCREEN_AUDITED
SYNTHESIS_ATTACK_CREDIT=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Purpose

The audited Stage29 foundation screen produced several exact models and theorem ecosystems around the same endpoint. 29-06 does not choose a winner and does not force them into one quotient tower. It freezes a field-aware, direction-aware endpoint-hub graph so later stages can attack several routes without silently reversing maps, confusing a cohomological decomposition with a morphism, or transferring `Q(i)` statements to `Q`.

Canonical machine-readable graph:

```text
stages/stage29/29-06/endpoint-hub-graph.json
```

## 2. Central endpoint node

The central geometric endpoint remains the canonical cuboid surface

```text
Sbar = complete intersection (2,2,2,2) in P6 over Q
48 A1 nodes
minimal resolution S: K^2=16, pg=7, q=0, geometric Picard rank 64
```

The positive physical rational-box locus is the smooth open

```text
U_phys = Sbar intersect D_+(a1*a2*a3).
```

This central node has several genuinely different outgoing/incoming structures.

## 3. Exact geometric morphisms already certified

### 3.1 F7 sign/Kummer presentation

The same canonical endpoint has the exact global map

```text
Sbar -> P2
[x:y:z]=[a1^2:a2^2:a3^2]
```

of generic degree `64` with deck group `(Z/2)^6`, branched on

```text
xyz(x+y)(x+z)(y+z)(x+y+z)=0.
```

This is full endpoint coverage, not a thin parametrized family.

The F7 presentation is therefore an exact presentation of `Sbar`, not a second independent physical endpoint surface.

### 3.2 Campedelli quotients

For each of the ten audited admissible rank-three kernels `H`,

```text
Sbar -> Cbar_H -> P2
 degree 8    degree 8
```

is a Q-defined global quotient factorization. After minimal resolution,

```text
S -> C_H
```

is finite etale of degree eight. The certified Q-symmetry orbit decomposition is `6+2+2`; this is not a theorem that there are exactly three Q-isomorphism classes.

Endpoint Q-points push forward to every `C_H(Q)`. Converse lifting is an `H`-torsor problem.

### 3.3 Beauville cover

The arrow is load-bearingly in the opposite direction:

```text
X_cub -> Sbar
```

with degree two after the audited Q-descent. On the physical smooth open it is finite etale with constant deck group `Z/2`.

An endpoint Q-point need not lift to the untwisted `X_cub`; it determines a quadratic torsor/twist class. No finite twist set is proved.

Therefore Beauville is not rewritten as an F7 quotient merely to make a single hierarchy.

## 4. Joint V4 / Stage28 hub

The Stage28 common base is

```text
Y=Bl_4(P1xP1),  L=-K_Y, L^2=4.
```

The simultaneous completion field is exactly

```text
K(Y)(sqrt(f_face),sqrt(f_sp)),
f_face=t1^2+t2^2,
f_sp=1+t1^2+t2^2.
```

This gives the dense-open V4 diamond

```text
                 X_joint
              /     |     \
           X_sp   X_face  X_cross
              \     |     /
                    Y
```

with three quadratic character quotients. The endpoint and `X_joint` have the same function field. The full boundary/canonical-model identification is retained explicitly as an open adapter rather than silently promoted:

```text
R29-G1b = JointCoverBoundaryContractionAndExceptionalCurveLedger
R29-X1  = CrossQuotientCompleteADESingularityAndMinimalModelAudit
```

Thus 29-06 records the edge as exact on function fields/dense opens, with global boundary status visible. 29-07 owns the exact bridge refinements.

## 5. Seven coordinate-sign K3 quotients

The endpoint has seven exact degree-two coordinate-sign quotients, in Q-symmetry orbits

```text
3*K_a + 3*K_b + 1*K_c.
```

Their audited transcendental labels are

```text
K_a -> h8
K_b -> h16
K_c -> h32.
```

The Stage19 and Stage20 marginal K3s have audited non-Tate modules

```text
X_sp   -> h16
X_face -> h32
```

and the V4 cross quotient has

```text
X_cross -> 2*h16+3*h8.
```

These module matches are **not** promoted to geometric isomorphisms between the Stage28 marginal K3s and particular coordinate-sign K3 quotients. Cohomological equality is a separate edge species.

## 6. Modular model and the S4 coincidence

Over `K=Q(i)`, the endpoint has the exact modular presentation

```text
Sbar_K ~= (X(8) x X(8))/Delta G0,
G0 ~= (Z/2)^3.
```

Forgetting the retained level-4 data gives only a generic moduli quotient of degree `24`, with residual group `S4`, to a target birational to Fisher's ordinary `Z(8,1)` surface.

The bare ordinary 8-congruence obstruction is already RED. Useful endpoint arithmetic must retain the conjugate-self level-4 datum.

The seven-line arrangement also has geometric base automorphism group `S4`, but the graph does not identify these two `S4` actions merely because the abstract groups agree:

```text
R29-KUM5 = ArrangementS4VsModularResidualS4ActionAndQDescentCocycle
STATUS=OPEN
```

No action-level or Q-descent identification is claimed in 29-06.

## 7. Non-Fano / Hirzebruch recognition

The cuboid seven-line divisor is PGL3(Q)-equivalent to the classical non-Fano arrangement. The cover arithmetic is subtler:

```text
STANDARD_NONFANO_Q_COVER_IDENTIFICATION=false
QI_GEOMETRIC_HIRZEBRUCH_IDENTIFICATION=true
CUBOID_Q_FORM_IS_EXPLICIT_CONSTANT_SIGN_TWIST=true
```

All 24 rational projective arrangement equivalences fail to lift to the standard cover over Q and lift over `Q(i)`.

Therefore the hub records:

- exact Q branch-arrangement recognition;
- exact Q(i) cover/resolution identification;
- an explicit Q twist relation;
- no automatic Q-rational-point transfer through the Q(i) isomorphism.

Per the audited GAP_SCAN_A anti-loop repair,

```text
R29-NF1QISO=LEDGER_ONLY_DORMANT_OPEN_NOT_NEEDED
```

and is not reactivated.

The active synthesis receivers remain

```text
R29-NF3
R29-NF4
R29-NF5
R29-NF6
R29-NF7
```

as explicitly OPEN internal adapters attached to the graph. None is promoted to a twelfth attack route.

## 8. L-function / character node is not a geometric node

The endpoint non-Tate representation is

```text
T(S)=3*h16+h32+3*h8.
```

This is represented in the hub by a cohomological node and typed edges from the endpoint/K3 objects. It is not a surface, quotient, cover, or rational-point map.

Likewise the V4 identity

```text
T(S)=T(X_sp)+T(X_face)+T(X_cross)
```

and the finite-field V4 point-count identity are structural/cohomological decompositions. They cannot be used as three independent rational-point probabilities.

## 9. Brauer/open-boundary relation

The physical open has 72 geometric boundary components on the resolution. The proper odd-primary nonconstant Brauer contribution is audited absent, but the physical open still has live extended-Picard, Gersten-residue and two-primary evaluation receivers.

These attach to `U_phys` as arithmetic tools, not as extra geometric endpoint models. In particular:

```text
NONFANO_MOD2_RESONANCE_IMPLIES_BRAUER_OBSTRUCTION=false
CLIFFORD_RECEIVER_IMPLIES_ENDPOINT_OBSTRUCTION=false
```

Any later Brauer obstruction must compute the relevant group and local evaluation maps.

## 10. Relation taxonomy locked

29-06 freezes the following relation classes as distinct:

```text
FINITE_COVER_OR_QUOTIENT
CREPANT_RESOLUTION
BIRATIONAL_OR_FUNCTION_FIELD_IDENTIFICATION
MODEL_ALIAS
BASE_CHANGE_ISOMORPHISM
Q_TWIST_RELATION
GENERIC_MODULI_QUOTIENT
COHOMOLOGICAL_DECOMPOSITION_OR_MODULE_MATCH
OPEN_INTERNAL_ADAPTER
```

A downstream argument may compose arrows only when field, direction and rational-point semantics are compatible.

## 11. Exact unresolved edge queue after synthesis

The graph intentionally retains unresolved edges. Primary next-stage bridge queue:

```text
29-07:
R29-KUM3A
R29-KUM3B
R29-KUM4B
R29-G1b
R29-X1
```

Synthesis-owned open adapters retained without replay:

```text
R29-KUM5
R29-NF3
R29-NF4
R29-NF5
R29-NF6
R29-NF7
```

`R29-NF1QISO` remains dormant ledger-only.

## 12. No route compression / no endpoint theorem

The hub does not imply that all foundations are independent, nor that one is universal. It also does not create a rational point or obstruction.

```text
ENDPOINT_HUB_GRAPH_MATERIALIZED=true
F7_UNIVERSAL_ORGANIZER_ASSUMED=false
PREMATURE_SINGLE_ROUTE_SELECTION=false
ATTACK_ROUTE_COUNT_RETAINED=11
SYNTHESIS_ATTACK_CREDIT=false
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[R29-KUM4B]
ROADMAP_REWRITE_REQUIRED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 13. Routing

The canonical controller is intentionally not edited by the main-lane submission. The audit may synchronize it only after checking every graph edge against the audited source records.

```text
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM=29-07_SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
NEXT_EXPECTED_COMMAND=Stage29-audit
```
