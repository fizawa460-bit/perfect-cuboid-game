# Stage30-01 — SOURCE_LOCK_AND_ACTION_OBJECT_FREEZE

Status: `SUBMITTED_PENDING_AUDIT`.

## Result

All mandatory Stage29 inputs were fresh-read and source-locked. The targeted Arsenal rematch found no exact shortcut. The Stage30 finite action objects are now frozen without assuming the desired adapter.

### Arrangement side

```text
G_arr = Aut_P2(D), |G_arr|=24
Omega_arr_4 = {A1,A2,A3,C}
Omega_arr_3 = {B1,B2,B3}
Q-liftable subgroup order = 6
Q(i)-liftable group order = 24
```

Deterministic generator conventions are frozen as

```text
s_arr=(A1 A2)(B1 B2)
t_arr=(A1 A2 A3 C)(B1 B3).
```

### Modular side

```text
G_mod = PSL2(Z/4)
S_mod=[[0,-1],[1,0]]
T_mod=[[1,1],[0,1]]
V_mod=ker(G_mod -> PSL2(F2))
Omega_mod_3=V_mod-{1}
Omega_mod_4={order-6 complements of V_mod in G_mod}
```

The expected sizes `|G_mod|=24`, `|V_mod|=4`, `|Omega_mod_3|=3`, `|Omega_mod_4|=4` are **targets for exact Task-A certification**, not newly granted theorem credit in this file beyond the already-audited abstract `PSL2(Z/4)~=S4` fact.

### Marked data

The retained level-4 sign matrix `D4=diag(1,-1)` and all eight K8 defect elements are frozen as labels. Their semilinear/Galois interpretation is deliberately deferred to Stage30-06, in accordance with the roadmap audit repair.

## Recursive classification

No hidden Class-1 leaf is left inside 30-01.

```text
L30-ACTION-TABLE-EXTRACTION = Class 1 finite, delegated to Codex Task A
L30-QI-EQUIVARIANT-ID       = Class 2 downstream, not yet executable before Task A audit
L30-GALOIS-COCYCLE          = Class 2 downstream, mathematically derived at 30-06
NEW_CLASS3_THEOREM_GATE     = none exposed by 30-01
DORMANT_NEW_LEAF            = none
```

The Class-1 finite leaf is not carried silently: Stage30-02P emits the exact Codex Task-A prompt in this same main-batch submission.

## Hard close flags

```text
ARRANGEMENT_ACTION_OBJECTS_FROZEN=true
MODULAR_ACTION_OBJECTS_FROZEN=true
GENERATOR_CONVENTIONS_FROZEN=true
MARKED_DATA_FROZEN=true
BASE_FIELD_LEDGER_FROZEN=true
ARSENAL_TARGETED_REMATCH_COMPLETE=true
HIDDEN_CLASS1_PENDING_UNDELEGATED_COUNT=0
ABSTRACT_S4_MATCH_IS_ADAPTER=false
QI_EQUIVARIANCE_VERIFIED=false
Q_GALOIS_COCYCLE_VERIFIED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
