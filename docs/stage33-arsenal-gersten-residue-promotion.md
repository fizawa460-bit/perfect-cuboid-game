# Stage33 Arsenal provisional harvest — Gersten / residue / Bockstein / localization / arithmetic lift

```text
REGISTRY=STAGE33-ARSENAL-PROVISIONAL-R04-SUPPLEMENT
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage33
SOURCE_PR=1476
SOURCE_BRANCH=stage33-post1475-j2-v4-generator-adapter
SOURCE_HEAD=73a0e5fa0b1694997b99df29ae63b08cbebabf39
PARENT_PROMOTION_FILE=docs/stage33-arsenal-promotion.md
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
THEOREM_CREDIT=false
```

This targeted pass covers only Gersten complexes, residue modules, Bockstein/raw-order effects, arithmetic localization, and global arithmetic-lift boundaries. It was reverse-indexed from `stages/stage33/MAIN-STATE.json`, `stages/stage33/33-12/result.md`, the retained exact prefix of `stages/stage33/33-07/result.md`, and the directly relevant Stage33-11 hostile/repair sources. Stage33 history was not reread sequentially.

```text
main_state_path=stages/stage33/MAIN-STATE.json
main_state_blob_sha=d32fa72fc321a0d6f50485ecc8c6abd4c690a378
main_state_canonical_sha256=32baebf358ae47b99a5a1ffd40dc90e7eb090db353f58861702bba3f0db0a9fc
stage33_12_result_path=stages/stage33/33-12/result.md
stage33_12_result_blob_sha=fc410a317d71362153aba8aa9489b005d1d3e45d
stage33_11_closed_localization_canonical_sha256=233be042e92010be169206df1193f25375ee9fd768f7fb3eebb9eb696389632e
```

## R04 classification

| Harvest object | Class | Arsenal disposition | Source path / SHA | Hypotheses / applicability | DO_NOT_USE_FOR |
|---|---|---|---|---|---|
| Mixed-order residue presentation -> invariant-factor basis with reversible Smith coordinates | **1. Arsenal candidate** | **Integrate into existing `S33-PW02`**; no duplicate | `stages/stage33/33-07/result.md`, blob `2a5f84a1fd34be395c216b343079ed85a525fb14`; invariant-basis SHA256 `f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939` | Exact finite abelian residue presentation; integral relation matrix and unimodular forward/inverse transforms retained. Applies before localization/descent when coordinates must survive quotient reduction. | Global Q-defined lift; arithmetic-HS closure; Bockstein recovery from invariant factors alone; silently discarding raw order-four data. |
| Quotient order-two vs raw order-four Bockstein/liftability gate | **1. Arsenal candidate** | **Integrate into existing `S33-PW03`** | `stages/stage33/33-07/result.md`, blob `2a5f84a1fd34be395c216b343079ed85a525fb14`; liftability SHA256 `85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312` | Quotient and raw extension are both explicitly represented and doubling/liftability obstruction is computed exactly. Applies before replacing residue directions by order-two squareclasses/Kummer data. | Treating every quotient `A[2]` direction as a raw order-two lift; suppressing order-four representatives; proving a global arithmetic lift. |
| Exact absolute arithmetic H1 receiver after finite-quotient reduction | **1. Arsenal candidate** | **Keep/extend existing `S33-PW06`**; no new card | `stages/stage33/33-10/result.md`, blob `49bb309f994742874572f485bd5e594fe4439ed4`; closed-interface canonical SHA256 `4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f` | Exact Galois-module decomposition; continuous Shapiro hypotheses for induced pieces; quotient pieces handled by the long exact sequence without an unproved split. Applies as the codomain/receiver into which arithmetic localization must actually land. | Identifying finite `H1(V4,K)` with absolute `H1(G_Q,K)`; killing kernel-Galois terms; deriving localization columns from dimensions alone. |
| Explicit Gersten lift -> Galois-difference -> connecting/localization adapter | **1. Arsenal candidate** | **New `S33-PW08`** | hostile negative source `stages/stage33/33-11/audit-state.json`, blob `dfb1072cae83618e281bfd555d7f6ef25f853fa4`; repair materializer `stages/stage33/33-11/materialize_stage33_11_a2_26_explicit_gersten_difference_preimage.py`, blob `b8906f50ef8a0e82dba4eeae76d14f920cd8c87c`; independent verifier `stages/stage33/33-11/verify_stage33_11_a2_26_explicit_gersten_difference_preimage.py`, blob `4c0c042020af539ce28f4746c82a8e13874378c7`; later exact closure summarized by `stages/stage33/33-12/result.md`, blob `fc410a317d71362153aba8aa9489b005d1d3e45d`, localization canonical SHA256 `233be042e92010be169206df1193f25375ee9fd768f7fb3eebb9eb696389632e` | Exact Gersten/residue complex and group action are pinned; ambient factors are attached to the actual height-one valuations on the resolved object; purity/off-boundary correction is materialized rather than assumed; `g(L)-L` and each connecting column are computed and independently/hostile verified. Applies to arithmetic localization where a boundary invariant must be lifted through a Gersten-type complex. | Inferring zero from visible-boundary invariance; assuming a global equivariant Gersten lift or purity correction; naturality/dimension counting as a connecting-column certificate; transporting the Stage33 zero map to another problem; claiming global Q-defined arithmetic lifts merely because the connecting map vanishes. |
| Mixed-order Smith -> Bockstein -> localization execution order | **2. Workflow candidate** | Workflow spanning `PW02` + `PW03` + `PW08` | retained Stage33-07 result + Stage33-11 repair sources above | Preserve raw orders first; compute exact Smith transforms; run liftability/double obstruction; only then materialize local/Gersten representatives and connecting classes. | Mod-2 reduction before checking raw order; losing representative provenance during Smith transport. |
| Resolved-height-one valuation attachment workflow | **2. Workflow candidate** | Workflow under `PW08` | `materialize_stage33_11_a2_26_explicit_gersten_difference_preimage.py`, blob `b8906f50...` plus Stage33-11 valuation/carrier scripts (source-locked by the closed Stage33-11 checkpoint) | Ambient rational functions/factors are known but Gersten residues are indexed by height-one primes on a resolved model. Decompose/attach factors to those valuations, including exceptional valuations, before solving purity correction. | Identifying ambient hyperplane-factor invariance with Gersten-class invariance. |
| Connecting-column fail-closed hostile replay | **2. Workflow candidate** | Strengthens existing `CONNECTING_MAP_FAIL_CLOSED`; do not make a second workflow family | hostile `audit-state.json`, blob `dfb1072c...`; closed result canonical `233be042...` | Exact progress increments only after an actual connecting column is materialized and checked. After repairs, rerun hostile audit across the complete source basis. | Counting a working/provisional zero pin as exact; extrapolating one representative to all invariant-factor directions. |
| Arithmetic-lift firewall / inventory workflow | **2. Workflow candidate** | Workflow under `PW06` + `PW08` | `stages/stage33/33-07/result.md`, blob `2a5f84...`; `stages/stage33/33-12/result.md`, blob `fc410a...` | Distinguish finite boundary liftability, Gersten localization, absolute H1 receiver, and actual global-Q residue/class inventory. All four layers must be source-locked before global arithmetic credit. | Reclosing Stage33-07 from finite/local exactness; inferring a Q-defined lift from zero localization or finite V4 data. |
| Concrete mixed-order counts `(Z/2)^49+(Z/4)^12`, quotient `(Z/2)^23+(Z/4)^3`, `29 -> 26`, and `17/9` liftability split | **3. Stage33-specific — no promotion** | Example/provenance only | `stages/stage33/33-07/result.md`, blob `2a5f84...` | Locked Stage33 residue presentation only. | Copying ranks/invariant factors to another residue complex. |
| Concrete Stage33-11 26 connecting columns and exact zero localization map | **3. Stage33-specific — no promotion** | Closed prerequisite only; `PW08` promotes the adapter protocol, not the value | `stages/stage33/33-12/result.md`, blob `fc410a...`; canonical `233be042...` | Locked Stage33 arithmetic localization system. | Predicting zero localization elsewhere or treating zero localization as a global-Q lift theorem. |
| A2_26 support labels, K2,2 four-cycle, five-bit decoder, carrier primes/strict transforms and exceptional valuations | **3. Stage33-specific — no promotion** | Provenance/debug payload only | hostile `audit-state.json`, blob `dfb1072...`; Stage33-11 materializer/valuation sources | Exact Stage33 resolved geometry and chosen basis direction only. | Generic Gersten-complex structure or reusable numerical constants. |
| Historical global-Q residue-lift inventory/closure from the old Stage33-07 closure | **3. Revoked/superseded — no promotion** | **DO NOT USE** | current `stages/stage33/33-07/result.md`, blob `2a5f84...`, records hostile reopening with kernel `R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT` | None; historical provenance only. | Any theorem/receiver/endpoint credit or proof that all relevant Q-defined lifts were already accounted for. |

## S33-PW08 — explicit Gersten connecting/localization adapter

**Type:** `GERSTEN_CONNECTING_LOCALIZATION_ADAPTER`

The reusable contract is the separation of four logically different assertions:

```text
boundary/residue package is G-stable
!= there exists a global Gersten lift
!= there exists a G-equivariant choice of lift/purity correction
!= the connecting obstruction is zero.
```

A valid exact computation instead follows:

```text
1. Pin the residue/Gersten complex, source basis, target kernel and group action.
2. Materialize a representative lift without assuming equivariance.
3. Attach ambient factors to actual height-one valuations on the resolved object,
   including exceptional contributions.
4. Solve/materialize the required off-boundary purity correction.
5. Compute g(L)-L for each relevant group generator.
6. Reduce that difference into the locked kernel/absolute-H1 receiver coordinates.
7. Materialize every required connecting/localization column.
8. Independently verify and hostile-replay the complete column set.
```

Stage33 is a useful hostile example: the first audit explicitly rejected a `26/26` working zero map because visible-boundary V4-fixity did not provide an equivariant global Gersten representative or purity correction. The later repaired Stage33-11 closure computed and hostile-audited all 26 columns and obtained an exact zero map. The **protocol** is portable; that zero value is not.

```text
ID=S33-PW08
HYPOTHESES=exact Gersten/residue complex; explicit group action; actual height-one valuation attachment; materialized purity correction; locked absolute receiver; complete independent/hostile column verification
APPLICABILITY=arithmetic localization and connecting morphisms built from explicit residue/Gersten representatives
DO_NOT_USE_FOR=visible-boundary-invariance shortcut; assumed equivariant lift; dimension-only zero; project-independent zero localization; global-Q arithmetic lift without separate inventory/descent proof
FORMAL_SELECTOR=false
THEOREM_CREDIT=false
```

## Overlap / integration decision

- No formal selector in `docs/arsenal/index.json` duplicates this Gersten/localization adapter band.
- `S33-PW02` already owns reversible Smith/invariant-factor residue compression. Do not create another residue-normal-form card.
- `S33-PW03` already owns the raw-order/Bockstein wall. `PW08` starts after a legitimate lift direction/representative is available and therefore does not subsume `PW03`.
- `S33-PW06` owns the absolute cohomology receiver. `PW08` owns construction of the connecting/localization class that must land in that receiver. Keep them separate.
- The R03 workflow `CONNECTING_MAP_FAIL_CLOSED` is strengthened by `PW08`; it is not duplicated under a new workflow name.
- The concrete Stage33-11 zero map is intentionally not a weapon. Only the verified method of constructing it is harvested.

## Revoked / hostile exclusions

```text
visible_boundary_V4_fixed => V4_fixed_global_Gersten_representative
status=REJECTED_BY_HOSTILE_AUDIT

choose_Q_defined_or_V4_fixed_offboundary_purity_correction => connecting_column_zero
status=REJECTED_CIRCULAR_ASSUMPTION

working_zero_map_26_of_26_before_actual_columns
status=NON_AUTHORITATIVE_DO_NOT_PROMOTE

old_Stage33_07_global_Q_residue_lift_inventory_closes_arithmetic_descent
status=SUPERSEDED_BY_STAGE33_08_HOSTILE_REOPEN

quotient_A2_order_two => every_raw_residue_lift_has_order_two
status=FALSE_BOCKSTEIN_SHORTCUT
```

The current Stage33-12 unit remains open. Exact finite residue reduction, exact Bockstein gates, and the exact Stage33-11 zero localization map do **not** by themselves restore global-Q arithmetic-lift inventory, Stage33-07 closure, Stage33-08 release, theorem credit, receiver credit, or endpoint credit.

```text
TARGETED_R04_NEW_CARD_COUNT=1
TARGETED_R04_NEW_CARD=S33-PW08
TARGETED_R04_INTEGRATED_CARDS=S33-PW02,S33-PW03,S33-PW06
TARGETED_R04_WORKFLOW_CANDIDATES=MIXED_ORDER_RESIDUE_TO_LOCALIZATION,RESOLVED_VALUATION_ATTACHMENT,CONNECTING_MAP_FAIL_CLOSED,ARITHMETIC_LIFT_FIREWALL
TARGETED_R04_STAGE33_SPECIFIC_DATA_PROMOTED=false
TARGETED_R04_REVOKED_CLAIMS_PROMOTED=false
ROUTEABLE_FOR_CANDIDATE_DISCOVERY=true
FORMAL_PROMOTION_ACTIVE=false
PERFECT_CUBOID_CONCLUSION=NONE
```