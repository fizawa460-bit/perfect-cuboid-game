# Stage29-05 — dependency, equivalence, route ownership, and double-charge ledger

```text
TASK=29-05_DEPENDENCY_EQUIVALENCE_ROUTE_OWNERSHIP_AND_DOUBLE_CHARGE_LEDGER
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
INPUT_29_04=PR1309_AUDITED_PASS_MERGED
PREMATURE_SINGLE_ROUTE_SELECTION=false
MULTI_ROUTE_ATTACK_ALLOWED=true
UNIQUE_PRIMARY_OWNER_REQUIRED=true
```

## 1. Purpose

Stage29 now has many descriptions of the endpoint: the full four-quadric surface, the degree-64 F7 sign/Kummer presentation, seven K3 quotients, joint V4 and cross quotient, Campedelli quotients, Beauville's irregular cover, modular 8-congruence, local squareclass systems, and parametrized families. 29-05 does **not** choose one winner. It prevents the same mathematical condition or map from being counted as several independent attacks and gives every live receiver one primary execution owner.

## 2. Load-bearing input from 29-04

On the physical host, with

```text
[x:y:z]=[a^2:b^2:c^2],
```

the two edge-ratio Kummer classes are automatically trivial and the four remaining coordinate-squareclass tests are exactly

```text
F_ab, F_ac, F_bc, S.
```

Thus:

```text
R29-KUM4A=DISCHARGED
R29-KUM4B=OPEN
BOOLEAN_16_EQUALS_SIGN_64=false
```

This exact pointwise identity is now a deduplication rule: a physical face/space predicate and its corresponding F7 coordinate-squareclass triviality test are one predicate, not two independent savings.

## 3. Canonical route registry

The canonical live attack families are:

```text
G10-FULL-ENDPOINT       owner=29-10  full surface / F7 direct curve-fibration geometry
G10-LOWGENUS-PICARD     owner=29-10  Testa-Stoll + finite Picard low-genus reduction/effectivity/multibranch
G10-K3-SIGN             owner=29-10  seven sign/K3 quotient directions and exact K3 theorem adapters
Q11-CAMPEDELLI          owner=29-11  Q-defined Campedelli quotient obstruction/descent
Q11-BEAUVILLE           owner=29-11  Beauville cover, twist/descent, Albanese
Q11-MODULAR             owner=29-11  M(4,8)/X(8) modular descent and residual S4
Q11-BRAUER              owner=29-11  proper/open Brauer obstruction receivers
J12-JOINT-V4            owner=29-12  joint completion/cross quotient arithmetic after 29-07 bridge
J12-LOCAL-SQUARECLASS   owner=29-12  seven-linear-form/local valuation attack using 29-09 infrastructure
J12-PARAMETRIC          owner=29-12  exact adapted parametrized/fibration families, no coverage promotion
J12-POP-INTERACTION     owner=29-12  common-host population/branch/moving-complement interaction route
```

Pre-attack infrastructure has separate owners but is not counted as an attack route:

```text
I07-KUMMER-BRIDGE       owner=29-07
I08-COVERAGE-ATLAS      owner=29-08
I09-LOCAL-INFRA         owner=29-09
```

## 4. Receiver ownership lock

```text
R29-KUM3A       -> I07-KUMMER-BRIDGE
R29-KUM3B       -> I07-KUMMER-BRIDGE ; depends_on=KUM3A
R29-KUM4B       -> I07-KUMMER-BRIDGE ; 29-04 pointwise precondition already satisfied
R29-G1b         -> I07-KUMMER-BRIDGE
R29-X1          -> I07-KUMMER-BRIDGE

R29-PESCH1      -> I08-COVERAGE-ATLAS ; independence unresolved until exact crosswalk

R29-KUM-LOC1    -> I09-LOCAL-INFRA
R29-KUM-LOC2    -> I09-LOCAL-INFRA

R29-LG2         -> G10-LOWGENUS-PICARD
R29-LG2-EFF     -> G10-LOWGENUS-PICARD
R29-LG2-MB      -> G10-LOWGENUS-PICARD

R29-CAMP2       -> Q11-CAMPEDELLI
R29-CAMP3       -> Q11-CAMPEDELLI
R29-CAMP4       -> Q11-CAMPEDELLI

R29-BEAU1B      -> Q11-BEAUVILLE
R29-BEAU1C      -> Q11-BEAUVILLE
R29-BEAU2A      -> Q11-BEAUVILLE
R29-BEAU2       -> Q11-BEAUVILLE
R29-BEAU3       -> Q11-BEAUVILLE

R29-MOD1C       -> Q11-MODULAR
R29-MOD1D       -> Q11-MODULAR
R29-MOD2B       -> Q11-MODULAR

R29-BR0A        -> Q11-BRAUER
R29-BR0B        -> Q11-BRAUER
R29-BR0G        -> Q11-BRAUER
R29-BR2A        -> Q11-BRAUER
R29-BR2B        -> Q11-BRAUER

R29-L2-ALG      -> J12-JOINT-V4
R29-L2-BAD      -> J12-JOINT-V4
```

`R29-KUM5` is cross-route synthesis between F7 arrangement symmetry and modular residual `S4`; primary owner is `29-06 GLOBAL_FOUNDATION_SYNTHESIS`, not a new attack route. Any later arithmetic residue is re-routed once after 29-06.

## 5. Exact equivalence / non-equivalence ledger

### 5.1 MERGED as descriptions/adapters

```text
F7 seven-line cover <-> non-Fano/Hirzebruch N=2 recognition over Q(i)
```

This is one geometric object with a named classical-theory adapter and explicit Q twist. It is not two independent endpoint foundations and cannot be credited twice.

The Horie-Yamauchi newform decomposition and the seven K3 quotient decomposition are attached arithmetic/cohomological descriptions of the K3 geometry. A theorem derived from one may still be new progress, but the existence of both descriptions is not two independent rarity mechanisms.

### 5.2 Same physical predicate, different coordinates

```text
Stage19 space-square predicate
= physical S on the exact-two host
= its audited Gaussian-norm/squareclass normal form on that chart
= the corresponding F7 coordinate-squareclass triviality test on the physical locus.
```

Likewise the Stage20 third-face completion predicate is the missing face-square predicate on the two-face host and its F7 coordinate-squareclass test. Local blocker laws, squareclass formulas, and cover equations are tools for the same predicate unless an independent theorem proves an additional restriction.

Therefore:

```text
NO_MULTIPLY_STAGE19_SQUARECLASS_SAVING_BY_F7_SQUARECLASS_SAVING=true
NO_MULTIPLY_STAGE20_LOCAL_BLOCKER_BY_SAME_FACE_PREDICATE_AGAIN=true
```

### 5.3 Distinct dependent attack routes retained

Campedelli quotients depend geometrically on F7 but are retained because a Q-point-free quotient would give a different endpoint obstruction by Q-defined pushforward. Converse lifting still needs torsor/descent analysis.

Beauville is retained separately because the audited direction is a degree-two cover `X_cub -> S_endpoint`; it is not an F7 quotient. Modular is retained separately because its generic birational/forgetful route and Q(i)/Q descent problem are different. Brauer is retained as obstruction technology rather than being declared equivalent to any quotient route.

### 5.4 Joint V4 scope

The joint V4 model is an endpoint presentation over the Stage28 two-face base, not a new population beyond the endpoint. Its marginal K3 covers and cross quotient are correlated pieces of one V4 character decomposition. The identity

```text
#X_joint = #X_face + #X_sp + #X_cross - 2#Y
```

must not be interpreted as three independent probabilistic savings.

### 5.5 Parametrized families

Saunderson, A2, Meskhishvili-style, and Peschmann-style families remain family/image data until exact coverage is proved. Closing a family or a slice does not close the endpoint and is not an independent global rarity factor.

## 6. Double-charge rules for later attack stages

Every future claimed saving/obstruction must record:

```text
ROUTE_ID
PREDICATE_OR_GEOMETRIC_MAP
HOST
FIELD_OF_DEFINITION
THEOREM_SPECIES
IS_NEW_RESTRICTION=true/false
DUPLICATE_OF_OR_NONE
CAN_COMBINE_WITH_OTHER_SAVING=true/false_with_reason
```

The default is `CAN_COMBINE=false` when two arguments enforce the same physical predicate through different coordinates.

No product of local density, thin-cover saving, K3 geometry, squareclass parity, or population ratio may be formed merely because all are numerically small.

## 7. Current route statuses

29-05 is a registry stage, not a pruning stage. No live route is made RED merely for depending on another model.

```text
G10-FULL-ENDPOINT=LIVE
G10-LOWGENUS-PICARD=LIVE
G10-K3-SIGN=LIVE
Q11-CAMPEDELLI=LIVE
Q11-BEAUVILLE=LIVE
Q11-MODULAR=LIVE
Q11-BRAUER=LIVE
J12-JOINT-V4=LIVE_CONDITIONAL_ON_29_07
J12-LOCAL-SQUARECLASS=LIVE_CONDITIONAL_ON_29_09
J12-PARAMETRIC=LIVE_WITH_COVERAGE_FIREWALL
J12-POP-INTERACTION=LIVE
```

The non-Fano/Hirzebruch adapter is `MERGED_WITH_F7_AS_DESCRIPTION`, not a separate route. Ordinary unconstrained symplectic 8-congruence remains RED as already audited; the twisted/conjugate-self modular route remains live.

## 8. Backflow / roadmap verdict

No old-stage contract repair is forced by this deduplication.

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[R29-KUM4B]
ROADMAP_MATERIALITY_CERTIFICATE=false
ROADMAP_REWRITE_REQUIRED=false
```

29-05 supplies the route registry needed for `GAP_SCAN_A / ROADMAP_REVIEW_A` after fresh audit.

## 9. Exit

```text
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM=GAP_SCAN_A_ROADMAP_REVIEW_A
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
