# Stage29-06 — audited-source crosswalk for hub edges

This file is provenance for `endpoint-hub-graph.json`. It does not promote any source claim beyond its audited scope.

| Hub content | Primary audited Stage29 source | Scope retained in 29-06 |
|---|---|---|
| Full endpoint `(2,2,2,2)` canonical surface, 48 A1 nodes, low-degree geometry | `29-02a` / PR #1287 | exact endpoint geometry; no isolated-Q-point conclusion |
| Joint V4 field and quotient diamond over `Y` | `29-02b` / PR #1288 | exact dense-open/function-field V4 structure; boundary/minimal-model receivers remain visible |
| Beauville Q-descended degree-two cover | `29-02d` / PR #1297 | arrow `X_cub -> S_endpoint`; physical-open twist lift; no finite twist set |
| Endpoint/K3 modular non-Tate decomposition | `29-02e` / PR #1298 | cohomological/module identities only; no geometric isomorphism inferred from same newform |
| Physical-open boundary/Brauer reductions | `29-02f` / PR #1300 | tools on `U_phys`; no Brauer-Manin obstruction claimed |
| Modular `M(4,8)` / degree-24 forgetting map | `29-02g` / PR #1301 | exact Q(i) modular presentation and generic quotient scope; ordinary 8-congruence RED |
| Degree-64 seven-line sign/Kummer cover | `29-02ha` / PR #1303 | exact global F7 cover, seven sign-K3 quotients, Q/Q(i) symmetry distinction |
| Ten Campedelli quotients | `29-02hb` / PR #1304 | exact Q-defined quotients; `6+2+2` certified Q S3 orbit decomposition only |
| Non-Fano/Hirzebruch recognition | `29-02hc` / PR #1305 | Q branch-arrangement equivalence; Q(i) cover isomorphism; explicit Q twist |
| Broad-screen retained candidates | `29-02hd` / PR #1306 | no ninth foundation in that pass; Peschmann independence open; retained adapters stay scoped |
| Population/F7 pointwise squareclass crosswalk | `29-04` / PR #1309 | KUM4A discharged pointwise; KUM4B counting adapter remains open |
| Route ownership/dedup | `29-05` / PR #1310 | 11 attack routes, 3 infrastructure routes, 1 synthesis owner; uncovered receiver count zero |
| Third-pass roadmap review | `GAP_SCAN_A` / PR #1311 | R2 still valid; NF1QISO dormant anti-loop; 29-06 may contain explicit open edges |

## Non-transfer locks

```text
SAME_NEWFORM_DOES_NOT_PROVE_GEOMETRIC_ISOMORPHISM=true
ABSTRACT_S4_ISOMORPHISM_DOES_NOT_PROVE_ACTION_IDENTIFICATION=true
QI_ISOMORPHISM_DOES_NOT_TRANSFER_Q_RATIONAL_POINTS_AUTOMATICALLY=true
GENERIC_MODULI_QUOTIENT_DOES_NOT_PROVE_EVERYWHERE_FINITE_MAP=true
FUNCTION_FIELD_IDENTIFICATION_DOES_NOT_DISCHARGE_BOUNDARY_LEDGER=true
COHOMOLOGICAL_DECOMPOSITION_IS_NOT_RATIONAL_POINT_MAP=true
SYNTHESIS_IS_NOT_ATTACK_CREDIT=true
```
