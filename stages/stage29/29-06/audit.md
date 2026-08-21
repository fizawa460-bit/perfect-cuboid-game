# Stage29-06 — adversarial audit

```text
AUDITED_PR=1312
AUDITED_SUBMISSION_HEAD=a3067fae86fcaeb2780ebd1053239c620a6cd7c3
AUDIT_MODE=GLOBAL_HUB_EDGE_DIRECTION_FIELD_RESOLUTION_SCOPE
AUDIT_VERDICT=PASS_AFTER_MATERIAL_REPAIR
```

## Executive verdict

The endpoint-hub design is useful and the submitted high-level prose was mostly careful, but the machine-readable graph failed a load-bearing resolution audit in three places. The graph mixed normal/canonical quotient models with their minimal resolutions, which changes whether displayed arrows are finite morphisms.

The repair is material because the hub is intended to be the canonical source of map direction/degree/field semantics for all later attacks.

## Attack 1 — F7 endpoint map

PASS.

The exact finite map is

```text
Sbar -> P2
degree=64
deck=(Z/2)^6
```

with the seven audited branch lines. `S -> P2` is not substituted for this finite morphism. The separate crepant resolution edge `S -> Sbar` remains explicit.

## Attack 2 — Campedelli resolution conflation

FAIL as submitted, PASS after repair.

The R01 graph used a single resolved-looking `CAMPEDELLI_H` node for both

```text
Sbar -> Cbar_H -> P2
```

and the resolved quotient. Audited 29-02hb explicitly distinguishes

```text
Cbar_H=Sbar/H,
Sbar -> Cbar_H   finite etale degree 8,
Cbar_H -> P2     finite degree 8,
```

from

```text
S -> C_H         finite etale degree 8,
C_H -> Cbar_H    minimal crepant resolution.
```

The composite `C_H -> P2` contracts six exceptional curves and is not called a finite degree-8 cover.

R02 therefore splits `CAMPEDELLI_BAR_H` and `CAMPEDELLI_H`.

```text
CAMPEDELLI_CANONICAL_RESOLUTION_SPLIT=PASS_AFTER_MATERIAL_REPAIR
```

## Attack 3 — coordinate-sign K3 quotient conflation

FAIL as submitted, PASS after repair.

Audited 29-02ha proves that quotienting `Sbar` by one coordinate-sign involution gives a normal degree-32 six-line cover; its minimal resolution is the corresponding K3.

The R01 graph instead drew a finite degree-two arrow directly from `Sbar` to a smooth K3 node. R02 splits

```text
Sbar -> Kbar_j       finite coordinate-sign quotient
K_j  -> Kbar_j       minimal crepant resolution
```

for `j=a,b,c`.

The cohomological labels `h8,h16,h32` remain attached to the smooth K3s and are not geometric-isomorphism claims for the Stage19/20 marginal K3s.

```text
K3_NORMAL_RESOLUTION_SPLIT=PASS_AFTER_MATERIAL_REPAIR
```

## Attack 4 — non-Fano normal cover versus Hirzebruch resolution

FAIL as submitted, PASS after repair.

R01 used one `NONFANO_M2` node for both the normal standard Kummer cover and its resolution, and attached the Q branch-arrangement recognition directly to that mixed node.

Audited 29-02hc requires three distinct layers:

```text
P2_NONFANO         standard branch arrangement
NONFANO_BAR        standard normal N=2 Kummer cover
NONFANO_M2         minimal Hirzebruch resolution
```

with

```text
P2_F7 ~=_Q P2_NONFANO                         branch-arrangement only
Sbar x Q(i) ~= NONFANO_BAR x Q(i)             normal covers
S    x Q(i) ~= NONFANO_M2  x Q(i)             resolutions
```

and over Q only an explicit constant-sign twist relation between the cuboid and standard cover forms.

```text
STANDARD_NONFANO_Q_COVER_IDENTIFICATION=false
QI_NORMAL_COVER_IDENTIFICATION=true
QI_RESOLUTION_IDENTIFICATION=true
Q_TWIST_RELATION_IS_Q_MORPHISM=false
```

`R29-NF1QISO` remains ledger-only dormant; this repair does not reactivate it.

## Attack 5 — Beauville direction

PASS.

The hub keeps

```text
X_cub -> Sbar
```

as the Q-descended canonical degree-two cover. It is not reversed to fit an F7 hierarchy. On `U_phys` the cover is finite etale with constant deck `Z/2`, but a Q-point lifts only to its associated quadratic twist in general. No finite twist set is proved.

## Attack 6 — joint V4 generic/global scope

PASS.

`K_endpoint=K_joint` is exact at the function-field/dense-open level. `R29-G1b` remains open for the boundary/canonical-model ledger and `R29-X1` remains open for the cross-quotient complete ADE/minimal-model audit.

No generic function-field identity is promoted to a globally finite endpoint isomorphism.

## Attack 7 — modular field and degree scope

PASS.

The Testa--Stoll modular presentation is retained over `Q(i)`. The degree-24 forgetting map is generic/moduli-level with residual `S4`, not an everywhere finite compactified morphism. Ordinary unrestricted symplectic 8-congruence remains RED.

The arrangement `S4` and modular residual `S4` are not identified without `R29-KUM5`.

## Attack 8 — cohomology versus morphisms

PASS.

The `3*h16+h32+3*h8` endpoint package and V4/K3 module matches are cohomological edges only. No rational-point pushforward/lift, geometric isomorphism, or independent rarity probability is inferred from them.

## Attack 9 — physical-open / population semantics

PASS after scope tightening.

The audited algebraic open is

```text
U=Sbar intersect D_+(a1*a2*a3),
```

which is smooth and resolution-isomorphic. It is not itself the canonical primitive Stage16--20 counting object. Ordering, primitive normalization, physical height and multiplicity remain separate population adapters.

```text
PROJECTIVE_Q_POINT_IS_CANONICAL_PRIMITIVE_POPULATION_OBJECT=false
HEIGHT_TRANSFER_AUTOMATIC=false
PRIMITIVITY_TRANSFER_AUTOMATIC=false
CANONICAL_ORDER_TRANSFER_AUTOMATIC=false
MULTIPLICITY_TRANSFER_AUTOMATIC=false
ASYMPTOTIC_TRANSFER_AUTOMATIC=false
```

## Attack 10 — receiver ownership / anti-loop

PASS.

The open synthesis set remains

```text
R29-KUM5
R29-NF3
R29-NF4
R29-NF5
R29-NF6
R29-NF7
```

and

```text
R29-NF1QISO=LEDGER_ONLY_DORMANT_OPEN_NOT_NEEDED.
```

The 29-07 bridge queue is unchanged:

```text
R29-KUM3A
R29-KUM3B
R29-KUM4B
R29-G1b
R29-X1
```

KUM4A replay remains forbidden. No current receiver becomes unowned and no twelfth attack route is created.

## Backflow / roadmap

The repaired graph clarifies map targets but changes no frozen Stage16--28 theorem contract.

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[R29-KUM4B]
ROADMAP_REWRITE_REQUIRED=false
```

## Final state

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_06_AUDIT=PASS
BOUNDED_REPAIR=CANONICAL_RESOLUTION_NODE_SPLIT_FOR_CAMPEDELLI_K3_NONFANO_PLUS_PHYSICAL_POPULATION_FIREWALL
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ATTACK_ROUTE_COUNT_RETAINED=11
SYNTHESIS_ATTACK_CREDIT=false
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[R29-KUM4B]
ROADMAP_REWRITE_REQUIRED=false
NEXT_ITEM=29-07_SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
