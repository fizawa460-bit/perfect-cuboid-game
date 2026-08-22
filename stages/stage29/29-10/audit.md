# Stage29-10 — fresh adversarial audit

```text
PR=1317
SUBMISSION_HEAD=791f4835304adcc89ef51ccbfe4f11ec6fee1fa6
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
BOUNDED_REPAIR=TERASOMA_DISPOSITION_SCOPE_PLUS_CURRENT_ARXIV_TITLE
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

## 1. Stage14 endpoint theorem inheritance — PASS

The submission imports, rather than re-credits, the audited Gap Scan B theorem

```text
P(B)=T(B),
R=d on the endpoint,
for every epsilon>0, P(B)=T(B)<<_epsilon B^(1/2+epsilon).
```

The exact dependence remains Stage14 `E=N2+3T`, `E<<V B^o(1)`, `V<<B^(1/2+o(1))`, plus the Stage29 objectwise endpoint dictionary. No 29-10 claim promotes this to finiteness, a global height cutoff, or nonexistence.

```text
STAGE14_ENDPOINT_IMPORT_AUDIT=PASS
STAGE14_ENDPOINT_REPLAY_ATTACK_CREDIT=false
FINITE_P_ZERO_PLUS_GLOBAL_UPPER_IMPLIES_GLOBAL_ZERO=false
```

## 2. G10-FULL-ENDPOINT — AMBER confirmed

Fresh source checking confirms the current cuboid fundamental-group paper is arXiv:2310.12710v3, revised 2026-07-06. It proves simple connectedness of the projective cuboid surface and its resolution and studies selected smooth opens on the face-cuboid surface. It does not supply the Stage29 physical endpoint open with a computed unipotent fundamental-group/Selmer/de Rham/Kim package or an effective zero-locus theorem.

The higher-dimensional `M_{0,5}` work remains a method example, not a formal transfer theorem to this endpoint surface.

Therefore

```text
R29-PI1-OPEN=AMBER_NO_EFFECTIVE_CUBOID_ENDPOINT_KIM_ADAPTER
G10_FULL_ENDPOINT=AMBER
```

No direct theorem path currently makes the physical endpoint open empty or classifies all of its rational points.

## 3. G10-LOWGENUS-PICARD — AMBER confirmed

The current Testa--Stoll publication is `Curves on the surface of cuboids`, Mathematics of Computation, DOI `10.1090/mcom/4238`, electronically published 2026-08-10. Its degree-`<=6` classification is already consumed by audited 29-02c-LG2 and earns no duplicate attack credit.

The 29-02c audit already certifies the finite negative-definite Picard reduction and the Freitag--Salvati Manni unibranch windows

```text
g=0: even d<=176
g=1: even d<=192.
```

It also explicitly certifies the three unresolved firewalls:

```text
R29-LG2     = OPEN_EXACT_FINITE_SEARCH_RUNTIME_UNCLOSED
R29-LG2-EFF = OPEN
R29-LG2-MB  = OPEN
```

Most importantly, no audited repo theorem or refreshed cited theorem was found proving that every physical endpoint rational point lies on one of the controlled rational/elliptic curves. Excluding positive-dimensional low-genus carriers therefore does not exclude arbitrary isolated endpoint rational points.

```text
LOWGENUS_ENDPOINT_POINT_COVERAGE_PROVED=false
G10_LOWGENUS_PICARD=AMBER
```

## 4. G10-K3-SIGN — AMBER confirmed

Audited 29-02e already proves globally at the semisimple l-adic non-Tate level

```text
K_a -> h8
K_b -> h16
K_c -> h32
```

for the seven coordinate-sign quotient K3 directions. Audited 29-08 gives the exact Stage20/Testa--Stoll `K_c` adapter at normal-model, resolution and physical-polarization level.

These facts are structural/cohomological. They do not imply that an image point on one K3 quotient lifts compatibly through the other endpoint square-root conditions, and they do not provide a standalone rational-point obstruction. Simultaneous compatibility remains correctly owned by `J12-JOINT-V4`.

No individual Q-defined K3 quotient theorem was found that excludes the relevant endpoint image open.

```text
K3_COHOMOLOGY_IS_ENDPOINT_POINT_OBSTRUCTION=false
K3_CROSS_COMPATIBILITY_PRIMARY_OWNER=J12-JOINT-V4
G10_K3_SIGN=AMBER
```

## 5. Terasoma receiver — PASS after bounded scope repair

The submission is correct that the old Terasoma four-quadric/K3 correspondence cannot be applied automatically to the 48-node cuboid canonical model. The cited theorem package contains smoothness/normal-crossing hypotheses; the relevant correspondence isomorphism statement is conditional on smooth `X`. No exact 48-node specialization/resolution adapter is currently certified.

It is also correct that 29-02e already supplies the specific cohomological decomposition that originally motivated this receiver. Replaying Terasoma merely to re-obtain that decomposition adds no present rational-point implication.

However, the submitted token

```text
DORMANT_DOMINATED_FOR_CURRENT_RATIONAL_POINT_ATTACK
```

was broader than the actual audit evidence. A valid future singular-specialization theorem could conceivably expose cycle/Chow-level information not contained in the 29-02e eigenspace statement. The audit therefore narrows, rather than reverses, the demotion:

```text
R29_TERA1=DORMANT_FOR_CURRENT_RATIONAL_POINT_ATTACK_COHOMOLOGY_OUTPUT_ALREADY_SUPPLIED
TERASOMA_SINGULAR_SPECIALIZATION_PROVED=false
TERASOMA_CYCLE_LEVEL_FUTURE_VALUE_NOT_RULED_OUT=true
TERASOMA_REPLAY_EARNS_ATTACK_CREDIT=false
```

This is a bounded wording/ownership repair, not a route-color change.

## 6. Bibliographic repair

The current v3 arXiv title is

```text
The fundamental group of surfaces parametrizing cuboids
```

not the submitted `On the Fundamental Groups of Surfaces Parametrizing Cuboids`. `source-refresh.md` is corrected. This has no mathematical consequence.

## 7. Ownership and double-charge — PASS

The submission respects the current execution split:

```text
individual K3/cohomology facts -> G10-K3-SIGN
simultaneous K3/V4 compatibility -> J12-JOINT-V4
Peschmann/Master-Hit/fibrations -> J12-PARAMETRIC
29-09 local arithmetic -> consumed infrastructure, not re-credited
```

No new independent primary mechanism was found and no receiver requires Stage16--28 backflow.

## Final route audit

```text
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
G10_FULL_ENDPOINT=AMBER
G10_LOWGENUS_PICARD=AMBER
G10_K3_SIGN=AMBER
GREEN_ROUTE_COUNT_29_10=0
R29_TERA1=DORMANT_FOR_CURRENT_RATIONAL_POINT_ATTACK_COHOMOLOGY_OUTPUT_ALREADY_SUPPLIED
ATTACK_ROUTE_COUNT=11
ROUTE_COUNT_CHANGE=0
TARGETED_BACKFLOW_REQUIRED=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
ROADMAP_REWRITE_REQUIRED=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-11_QUOTIENT_DESCENT_AND_MODULAR_ATTACK_PORTFOLIO
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
