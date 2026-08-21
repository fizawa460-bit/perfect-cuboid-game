# Stage29-06 — audited global foundation synthesis / endpoint-hub graph

```text
STAGE=Stage29
ITEM=29-06_GLOBAL_FOUNDATION_SYNTHESIS
MODE=PRE_ATTACK_SYNTHESIS
AUDIT_VERDICT=PASS_AFTER_MATERIAL_REPAIR
SYNTHESIS_ATTACK_CREDIT=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Audit verdict

The endpoint-hub strategy survives, but the submitted machine-readable graph did **not** pass as written. It collapsed canonical/normal quotient models with their minimal resolutions in three places. That changes whether displayed maps are finite and is therefore a material graph defect, not cosmetic notation.

The repaired graph is `endpoint-hub-graph.json`, schema `STAGE29_06_ENDPOINT_HUB_GRAPH_R02_AUDITED`.

```text
CANONICAL_RESOLUTION_SCOPE_AUDIT=PASS_AFTER_MATERIAL_REPAIR
F7_UNIVERSAL_ORGANIZER_ASSUMED=false
ENDPOINT_HUB_GRAPH_MATERIALIZED=true
```

## 2. Central endpoint and F7 presentation

The central endpoint remains

```text
Sbar = (2,2,2,2) complete intersection in P6 over Q
S    = minimal resolution of Sbar
```

with 48 A1 nodes and resolved invariants `K^2=16, pg=7, q=0`.

The exact finite global F7 map is

```text
Sbar -> P2
[a1:a2:a3:...] -> [a1^2:a2^2:a3^2]
degree=64
deck=(Z/2)^6
branch=xyz(x+y)(x+z)(y+z)(x+y+z)=0.
```

`S -> P2` is **not** substituted for this finite map: the resolution contracts exceptional curves through `S -> Sbar` first.

The four physical face/space predicates remain the audited pointwise squareclass tests on this same F7 presentation (`R29-KUM4A`), while the population/subcover count adapter `R29-KUM4B` stays open.

## 3. Material repair A — Campedelli canonical model versus resolution

The submitted prose already had the correct distinction, but the R01 graph node `CAMPEDELLI_H` mixed it back together. The exact global finite factorization is

```text
Sbar --degree 8 etale--> Cbar_H --degree 8--> P2,
```

where `Cbar_H=Sbar/H` is normal and has six A1 singularities.

Separately, after minimal resolutions,

```text
S --degree 8 etale--> C_H
|                     |
v                     v
Sbar ---------------> Cbar_H
```

is the audited resolution-level finite etale quotient. The composite `C_H -> Cbar_H -> P2` is not called a finite degree-8 cover because the six exceptional curves are contracted.

The repaired graph therefore has distinct nodes

```text
CAMPEDELLI_BAR_H
CAMPEDELLI_H
```

and distinct canonical/resolved edges.

The arithmetic orbit firewall is unchanged:

```text
GEOMETRIC_Qi_KERNEL_ORBITS=8+2
CERTIFIED_Q_S3_KERNEL_ORBITS=6+2+2
EXACT_Q_ISOMORPHISM_CLASS_COUNT_PROVED=false
```

## 4. Material repair B — coordinate-sign K3 quotient versus K3 resolution

For a coordinate sign involution, the finite degree-two quotient of `Sbar` is a **normal degree-32 six-line cover**. Its minimal resolution is the K3 surface.

The R01 graph incorrectly drew

```text
Sbar --degree 2 finite--> smooth K3
```

directly. The repaired graph splits each orbit into

```text
Sbar -> Kbar_a, Kbar_b, Kbar_c     finite normal quotients
K_a  -> Kbar_a                     minimal crepant resolution
K_b  -> Kbar_b
K_c  -> Kbar_c
```

with Q-orbit multiplicities `3+3+1` and non-Tate labels

```text
K_a -> h8
K_b -> h16
K_c -> h32.
```

The Stage19/20 marginal K3 module matches remain only cohomological/module matches:

```text
X_sp   -> h16
X_face -> h32
```

and do **not** prove geometric isomorphism to `K_b` or `K_c`.

## 5. Material repair C — standard non-Fano normal cover versus Hirzebruch resolution

The R01 graph also used one node `NONFANO_M2` for both the standard normal Kummer cover and its resolution. That is repaired into

```text
P2_NONFANO
NONFANO_BAR = standard normal N=2 Kummer cover
NONFANO_M2  = its minimal resolution.
```

The exact field statements are now represented separately:

```text
P2_F7 ~=_Q P2_NONFANO as branch arrangements
Sbar x Q(i) ~= NONFANO_BAR x Q(i)
S    x Q(i) ~= NONFANO_M2  x Q(i)
```

Over Q there is an explicit constant-sign twist relation, **not** a Q-isomorphism of the standard covers.

```text
STANDARD_NONFANO_Q_COVER_IDENTIFICATION=false
QI_GEOMETRIC_HIRZEBRUCH_IDENTIFICATION=true
CUBOID_Q_FORM_IS_EXPLICIT_CONSTANT_SIGN_TWIST=true
```

`R29-NF1QISO` remains ledger-only dormant and is not reactivated.

## 6. Beauville, modular and V4 arrows survive

The Beauville direction remains

```text
X_cub -> Sbar
degree=2 over Q.
```

On the physical smooth open it is finite etale with constant deck group `Z/2`; an endpoint Q-point determines a quadratic twist class and need not lift to the untwisted cover. No finite twist set is proved.

The modular presentation remains exact after base change to `Q(i)`:

```text
Sbar_Q(i) ~= (X(8)xX(8))/Delta G0,
G0=(Z/2)^3.
```

The subsequent forgetting map has generic degree `24` and residual `S4` only at the audited generic/moduli level. It is not promoted to an everywhere finite compactified morphism. Ordinary unrestricted symplectic 8-congruence remains RED.

The arrangement `S4` and modular residual `S4` remain unrelated at action level until `R29-KUM5` is solved.

For the joint V4 model,

```text
K_endpoint = Q(Y)(sqrt(f_face),sqrt(f_sp))
```

is exact on function fields/dense opens. The global boundary/canonical-model and cross minimal-model ledgers remain open as

```text
R29-G1b
R29-X1.
```

No generic-to-global promotion was added in 29-06.

## 7. Cohomology is not a rational-point map

The endpoint non-Tate representation

```text
3*h16 + h32 + 3*h8
```

and the V4/K3 decompositions are kept as cohomological edges only. They are not quotient maps, rational-point implications, or independent probability factors.

Likewise `R29-QWEB-CLIFFORD`, Brauer, characteristic-variety and resonance data remain theorem/adaptor tools; no obstruction is certified merely by attaching them to the hub.

## 8. Physical-open and population firewall

The algebraic physical open is

```text
U = Sbar intersect D_+(a1*a2*a3),
```

which is smooth and identified with its inverse image on `S`. It is the nonzero-side algebraic locus relevant to rational boxes. Canonical ordering, primitive normalization, physical height and counting multiplicity are **not** encoded by an open immersion in the hub.

```text
PROJECTIVE_Q_POINT_IS_CANONICAL_PRIMITIVE_POPULATION_OBJECT=false
HEIGHT_TRANSFER_AUTOMATIC=false
PRIMITIVITY_TRANSFER_AUTOMATIC=false
CANONICAL_ORDER_TRANSFER_AUTOMATIC=false
MULTIPLICITY_TRANSFER_AUTOMATIC=false
ASYMPTOTIC_TRANSFER_AUTOMATIC=false
```

Thus the hub does not turn the exact Q-point formulations into Stage16--20 population equalities.

## 9. Open synthesis / next bridge queue

Synthesis-owned open adapters remain

```text
R29-KUM5
R29-NF3
R29-NF4
R29-NF5
R29-NF6
R29-NF7
```

with

```text
R29-NF1QISO=LEDGER_ONLY_DORMANT_OPEN_NOT_NEEDED.
```

The 29-07 primary bridge queue remains

```text
R29-KUM3A
R29-KUM3B
R29-KUM4B
R29-G1b
R29-X1
```

and KUM4A replay is forbidden.

No Stage16--28 contract was changed by the repaired graph, so

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[R29-KUM4B]
```

remains correct.

## 10. Final state

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
ROADMAP_REWRITE_REQUIRED=false
NEXT_ITEM=29-07_SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
