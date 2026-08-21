# Stage29-06 — audited-source crosswalk for hub edges

This file is provenance for the audited `endpoint-hub-graph.json`. It does not promote any source claim beyond its audited scope.

| Hub content | Primary audited Stage29 source | Scope retained in 29-06 |
|---|---|---|
| Full endpoint `(2,2,2,2)` canonical surface, 48 A1 nodes, low-degree geometry | `29-02a` / PR #1287 | `Sbar` canonical model versus `S` minimal resolution kept separate; no isolated-Q-point conclusion |
| Joint V4 field and quotient diamond over `Y` | `29-02b` / PR #1288 | exact dense-open/function-field V4 structure; `R29-G1b` and `R29-X1` retain boundary/minimal-model work |
| Beauville Q-descended degree-two cover | `29-02d` / PR #1297 | arrow `X_cub -> Sbar`; physical-open twist lift; no finite twist set |
| Endpoint/K3 modular non-Tate decomposition | `29-02e` / PR #1298 | cohomological/module identities only; same newform does not prove geometric isomorphism |
| Physical-open boundary/Brauer reductions | `29-02f` / PR #1300 | `U=Sbar∩D_+(a1a2a3)` is smooth and resolution-isomorphic; no Brauer-Manin obstruction claimed |
| Modular `M(4,8)` / degree-24 forgetting map | `29-02g` / PR #1301 | exact `Q(i)` modular presentation; degree 24 only generic/moduli-level; ordinary 8-congruence RED |
| Degree-64 seven-line sign/Kummer cover | `29-02ha` / PR #1303 | exact finite `Sbar -> P2`; coordinate-sign finite quotients target normal six-line covers whose minimal resolutions are K3 |
| Ten Campedelli quotients | `29-02hb` / PR #1304 | exact `Sbar -> Cbar_H -> P2`; separately exact resolved etale `S -> C_H`; `6+2+2` is Q-S3 orbit decomposition only |
| Non-Fano/Hirzebruch recognition | `29-02hc` / PR #1305 | Q branch-arrangement equivalence; `Sbar_Q(i) ~= Xbar_2,Q(i)` and `S_Q(i) ~= M_2,Q(i)` separately; explicit Q twist |
| Broad-screen retained candidates | `29-02hd` / PR #1306 | no ninth foundation in that pass; Peschmann independence open; retained adapters stay scoped |
| Population/F7 pointwise squareclass crosswalk | `29-04` / PR #1309 | KUM4A discharged pointwise; KUM4B counting adapter remains open |
| Route ownership/dedup | `29-05` / PR #1310 | 11 attack routes, 3 infrastructure routes, 1 synthesis owner; uncovered receiver count zero |
| Third-pass roadmap review | `GAP_SCAN_A` / PR #1311 | R2 still valid; NF1QISO dormant anti-loop; 29-06 may contain explicit open edges |

## Resolution-level audit repair

The R01 graph used resolved names as targets of finite canonical-cover maps in three places. The audited R02 graph repairs all three:

```text
Sbar -> Cbar_H -> P2          finite canonical-level Campedelli maps
S    -> C_H                   finite etale resolved Campedelli quotient

Sbar -> Kbar_j                finite coordinate-sign quotient
K_j  -> Kbar_j                minimal crepant resolution

Sbar_Q(i) -> NONFANO_BAR_Q(i) normal-cover isomorphism
S_Q(i)    -> NONFANO_M2_Q(i)  resolved-surface isomorphism
NONFANO_M2 -> NONFANO_BAR      crepant resolution
```

A resolved surface followed by contraction to a normal quotient/base is not silently called finite.

## Non-transfer locks

```text
SAME_NEWFORM_DOES_NOT_PROVE_GEOMETRIC_ISOMORPHISM=true
ABSTRACT_S4_ISOMORPHISM_DOES_NOT_PROVE_ACTION_IDENTIFICATION=true
QI_ISOMORPHISM_DOES_NOT_TRANSFER_Q_RATIONAL_POINTS_AUTOMATICALLY=true
GENERIC_MODULI_QUOTIENT_DOES_NOT_PROVE_EVERYWHERE_FINITE_MAP=true
FUNCTION_FIELD_IDENTIFICATION_DOES_NOT_DISCHARGE_BOUNDARY_LEDGER=true
COHOMOLOGICAL_DECOMPOSITION_IS_NOT_RATIONAL_POINT_MAP=true
RESOLUTION_DOES_NOT_PRESERVE_FINITE_MAP_TO_BASE_AUTOMATICALLY=true
PROJECTIVE_Q_POINT_IS_NOT_AUTOMATICALLY_A_CANONICAL_PRIMITIVE_COUNTING_OBJECT=true
SYNTHESIS_IS_NOT_ATTACK_CREDIT=true
```
