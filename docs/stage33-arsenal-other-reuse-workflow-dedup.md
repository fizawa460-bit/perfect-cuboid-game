# Stage33 Arsenal provisional harvest — other reusable mathematics / workflow consolidation / full dedup

```text
REGISTRY=STAGE33-ARSENAL-PROVISIONAL-R05-SUPPLEMENT-V2
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage33
SOURCE_PR=1476
SOURCE_BRANCH=stage33-post1475-j2-v4-generator-adapter
SOURCE_HEAD=b4ed4c898988975f485e48b3803e0f8753c65015
PARENT_PROMOTION_FILE=docs/stage33-arsenal-promotion.md
GERSTEN_SUPPLEMENT=docs/stage33-arsenal-gersten-residue-promotion.md
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
THEOREM_CREDIT=false
```

This is the final catch-all pass for Stage33 material not already covered by the Picard/Kummer/finite-module, Brauer/HS/descent/torsor, and Gersten/residue/localization harvests. It also deduplicates the eight current Stage33 provisional cards and workflow vocabulary. Stage33 history was not reread sequentially.

The first R05 read was made at `73a0e5fa...`. During the harvest Stage33 advanced by two commits to `b4ed4c898...`. A direct compare showed that only `.github/workflows/stage33-12-main.yml`, `MAIN-BATCH-HANDOFF.md`, `MAIN-STATE.json`, and `sync_main_state.py` changed; the Stage33-09/33-12 evidence files harvested below did not move. The new `MAIN-STATE V7` is nevertheless authority-changing: the historical Picard-adjoint mask-6 coordinate is **not authoritative as the named J2 proper-Br2 source** and is reopened pending a source-locked marked-discriminant/proper-Br2 adapter. This supplement therefore promotes only the reusable adapter method, never that concrete named-source binding.

```text
main_state_path=stages/stage33/MAIN-STATE.json
main_state_blob_sha=0bfe5bde4f991cdb47c6da2f1980800ba2a64e58
main_state_canonical_sha256=7d52c93a517fc96050b2f78583ae05e5e4ff4f983c2533c673ca008060bd0226
main_state_schema=STAGE33_MAIN_COMPACT_STATE_V7_J2_NAMED_SOURCE_REOPENED
stage33_09_result_path=stages/stage33/33-09/result.md
stage33_09_result_blob_sha=820543c4778851f5b7487e6d09a6274ee0cceed3
stage33_09_closure_path=stages/stage33/33-09/stage33-09-closure.json
stage33_09_closure_blob_sha=0e388cac1d5287ee5b2a3288c10153c16e99fb2a
stage33_09_closure_canonical_sha256=6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7
stage33_12_result_path=stages/stage33/33-12/result.md
stage33_12_result_blob_sha=fc410a317d71362153aba8aa9489b005d1d3e45d
```

## Classification

| Harvest object | Class | Disposition | Source path / SHA | Hypotheses / applicability | DO_NOT_USE_FOR |
|---|---|---|---|---|---|
| Marked Picard basis bridge with exact Gram/action transport across implementations | **1. Arsenal** | integrate `PW04` (basis/coordinate side) + `PW05` (equivariance side); no new card | `33-09/marked-picard-basis-bridge-certified.json`, blob `77b16e2ee80c33af27f7a5a04e1c465e9fc1acea`; `33-09/stage33-09-closure.json`, blob `0e388cac...`, canonical `6c3ff8f7...` | Both marked presentations and actions are source-locked; exact bridge exists; form transport and every downstream-used action are checked. | Rank/determinant matching as a bridge; unchecked conjugation; treating a rational bridge as integral/unimodular without proof; changing markings without recomputation. |
| Finite-ambiguity semantic orientation by unique lattice fingerprint + explicit marked adapter | **1. Arsenal** | integrate method into `PW04`; no new card | `33-12/j2-cv-d2-semantic-orientation.json`, blob `140acdc9896d1d87a82a1807fd92ce276a620d75`, canonical `0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e` | Candidate set and fingerprints are exact; observed invariant independently certified; match unique; final coordinate transfer uses explicit marked adapter. | Non-unique fingerprint guesses; canonical identification of distinct modules from one scalar invariant; **asserting the reopened historical mask-6 proper-Br2 coordinate is the named J2 source**. |
| Literal Čech representative -> Cartier/principal divisor -> Pic -> Pic/2 validation | **1. Arsenal** | integrate into `PW07`; `PW08` remains the later arithmetic localization layer | `33-12/j2-cc-actual-cech-global-square-overlap.json`, blob `93383a6135a05b1a1d5a55f6261b2ab5f3c94120`; result canonical `82ac2b6fe8d023c915e9cf3bb8ff38d4782dbec47f98e2593f964ea020ccc6fd` | Literal representative exists on required charts/resolved object; transition determinant is explicit; full Cartier divisor computed; Pic class transported exactly. | “Generically a square” shortcuts; arithmetic localization/absolute-H1 conclusions; exporting Stage33's concrete zero value. |
| Sparse source-preserving replay of only leaf-required rows | **2. Workflow** | **new canonical workflow `SPARSE_SOURCE_REPLAY`** | `33-12/j2-ct-six-kc-support-fullpic64-pullbacks.json`, blob `a07ab8b0c9fd0b683db5845d75e2749a2882d546`, canonical `592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d` | Required support known exactly; every needed row reconstructed independently from retained source evidence and transported through locked adapters; dependency support complete. | Interpolating missing rows; claiming equivalence to a giant historical matrix without rowwise checks; sparse replay when hidden downstream dependencies require unmaterialized rows. |
| Exhaustive finite-group generator/relabeling diagnostic | **2. Workflow** | extend `V4_EQUIVARIANT_TRANSPORT_AUDIT`; no new workflow family | `33-12/diagnose_j2_v4_generator_identification.py`, blob `9595fb207eb4a6a18d653df1e8846258fcba59aa` | Source/target actions locked; all relevant finite-group automorphisms enumerable; full compatibility/reachability equations solved for each labeling. | Positive diagnostic -> geometric extension/relation/column; changing locked coordinates to make a row pass; assuming labels are the only adapter defect. |
| Cross-basis equivariant transport audit | **2. Workflow** | alias/subroutine of `BASIS_ADJOINT_AUDIT` + `V4_EQUIVARIANT_TRANSPORT_AUDIT` | Stage33-09 result blob `820543c4...`; bridge blob `77b16e2e...`; closure canonical `6c3ff8f7...` | Verify bases, bridge, form, round-trip where defined, and action intertwining before coordinate consumption. | Same-rank/same-determinant shortcuts. |
| Lattice-fingerprint orientation audit | **2. Workflow** | subroutine of `BASIS_ADJOINT_AUDIT` | semantic certificate blob `140acdc9...`, canonical `0a5abe...` | Independent exact fingerprint and unique match. | Non-unique selection; converting semantic orientation into a named proper-Br2 source without the required live adapter. |
| Čech representative/divisor audit | **2. Workflow** | subroutine of `TORSOR_SEMANTIC_VALIDATION` | Čech blob `93383a61...`, canonical `82ac2b6f...` | Literal representative and resolved-divisor data. | Generic-symbol or arithmetic-localization shortcuts. |
| Concrete Stage33-09 bridge determinant, historical basis names, named action matrices | **3. Stage33-specific** | provenance only | Stage33-09 sources above | Frozen Stage33 Picard presentations. | Reusing constants/matrices elsewhere. |
| Concrete J2 norms/fingerprints, label `u1`, coordinate `[1,0]` | **3. Stage33-specific** | only selection method reusable | semantic canonical `0a5abe...` | Frozen marked Kc/J2 geometry. | Generic norm table; named proper-Br2 source coordinate. |
| Historical Picard-adjoint mask-6 / proper14+retained10 candidate as named J2 source | **3. Revoked/reopened — no promotion** | **DO NOT USE AS NAMED SOURCE**; generic adjoint method remains PW04 | current `MAIN-STATE`, blob `0bfe5bde...`, canonical `7d52c93a...`; historical candidate canonical `066e6b...` | None for named binding until a source-locked marked discriminant -> proper-Br2 adapter is materialized. | `C2+C3=h_J2`; named J2 source; Kummer column credit; treating old mask 6 as authoritative. |
| Concrete six-row ct support/Pic64 weights | **3. Stage33-specific** | workflow example only | sparse replay canonical `59270459...` | Frozen J2 ct leaf. | Assuming six rows suffice elsewhere. |
| Concrete Čech scalar and zero Pic/Pic2 vector | **3. Stage33-specific** | method only goes to PW07 | result canonical `82ac2b6f...` | Frozen corrected-J2 representative. | Predicting another geometric or arithmetic zero. |
| Concrete outcome of six V4 label tests | **3. Stage33-specific** | diagnostic output only | diagnostic blob `9595fb20...` | Frozen Stage33 modules/actions. | Restoring a named relation/standard column/geometric extension. |

## Card-boundary normalization

Exactly eight Stage33 provisional cards remain; R05 creates no ninth card.

| Card | Unique role after dedup | Critical live boundary |
|---|---|---|
| `S33-PW01` | exact arithmetic-HS zero-survival classifier | does not construct PW06 receiver |
| `S33-PW02` | finite presentation -> invariant factors with reversible coordinates | does not recover PW03 Bockstein/extension data |
| `S33-PW03` | quotient/raw-order and Bockstein liftability gate | starts after finite normal form; keeps raw order information |
| `S33-PW04` | **method-level** marked basis/dual/adjoint/semantic-orientation adapter | **current historical mask-6 J2 named-source binding is reopened and is not Arsenal credit** |
| `S33-PW05` | equivariant source-target compatibility/reachability | cannot repair an invalid/unlocked PW04 named source merely by relabeling |
| `S33-PW06` | absolute arithmetic `H^1` receiver construction | finite `V4` H1 is not the absolute receiver |
| `S33-PW07` | geometric Brauer/cocycle/torsor semantics + literal Čech representative validation | geometric Pic zero is not PW08 arithmetic localization zero |
| `S33-PW08` | Gersten lift -> Galois difference -> arithmetic connecting/localization | requires actual lift/valuation/purity data and lands in PW06 receiver |

```text
R05_CARD_COUNT_BEFORE=8
R05_CARD_COUNT_AFTER=8
R05_NEW_CARD_COUNT=0
R05_MERGED_OR_DELETED_CARD_COUNT=0
R05_FORMAL_SELECTOR_CHANGES=0
```

## Workflow consolidation

Canonical workflow vocabulary:

| Workflow | Status after R05 | Includes |
|---|---|---|
| `SMITH_ROUNDTRIP` | retain | presentation/invariant-factor coordinate witnesses |
| `BASIS_ADJOINT_AUDIT` | extend | dual conventions; marked cross-basis bridge; Gram/pairing checks; unique lattice-fingerprint orientation |
| `V4_EQUIVARIANT_TRANSPORT_AUDIT` | extend | action intertwining; reachable image; exhaustive finite-group label diagnostics |
| `HS_ZERO_SURVIVAL_MATRIX` | retain | complete invariant block + exact obstruction rank |
| `ABSOLUTE_H1_RECEIVER_DECOMPOSITION` | retain | continuous-H1 receiver construction |
| `TORSOR_SEMANTIC_VALIDATION` | extend | exact torsor/cocycle semantics + literal Čech/divisor validation |
| `CONNECTING_MAP_FAIL_CLOSED` | retain | actual columns before credit; hostile replay after repair |
| `MIXED_ORDER_RESIDUE_TO_LOCALIZATION` | retain | Smith -> Bockstein -> localization order |
| `RESOLVED_VALUATION_ATTACHMENT` | retain | ambient factors -> actual height-one primes/exceptions |
| `ARITHMETIC_LIFT_FIREWALL` | retain | finite/local exactness != global-Q lift |
| `SPARSE_SOURCE_REPLAY` | **new** | exact support-only reconstruction from source formulas/adapters |

Do not create separate canonical workflow names for cross-basis equivariant transport, lattice-fingerprint orientation, Čech divisor audit, or generator relabeling: they are subroutines above.

## Revoked / hostile / superseded exclusions

```text
C2 + C3 = h_J2
status=REVOKED_EXACT_DO_NOT_USE
revoking_sha256=463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229

historical_picard_adjoint_mask6_as_named_J2_source
status=REOPENED_EXACT_DO_NOT_USE_AS_NAMED_SOURCE
current_main_state_sha256=7d52c93a517fc96050b2f78583ae05e5e4ff4f983c2533c673ca008060bd0226

copy_u1_A_T_2_coefficients_into_proper_Br2_dual_basis
status=REJECTED_EXACT_DO_NOT_RETRY

direct_order4_picard_pullback_route_for_J2_source
status=SUPERSEDED_DO_NOT_REOPEN

visible_boundary_fixed_implies_equivariant_global_Gersten_lift
status=REJECTED_BY_HOSTILE_AUDIT

pre_repair_working_zero_localization_columns
status=NON_AUTHORITATIVE_DO_NOT_PROMOTE

old_Stage33_07_global_Q_residue_lift_inventory_closes_arithmetic_descent
status=SUPERSEDED_BY_HOSTILE_REOPEN
```

Additional R05 firewalls:

```text
matching_lattice_fingerprint_without_uniqueness => NO_SEMANTIC_ORIENTATION_CREDIT
semantic_orientation_without_live_discriminant_to_proper_Br2_adapter => NO_NAMED_SOURCE_CREDIT
positive_generator_relabeling_diagnostic => NO_GEOMETRIC_EXTENSION_OR_COLUMN_CREDIT
sparse_support_replay_without_complete_dependency_support => NO_EQUIVALENCE_TO_FULL_MATRIX
geometric_Cech_Pic_zero => NO_AUTOMATIC_ARITHMETIC_LOCALIZATION_ZERO
```

```text
TARGETED_R05_NEW_CARD_COUNT=0
TARGETED_R05_INTEGRATED_METHOD_CARDS=S33-PW04,S33-PW05,S33-PW07
TARGETED_R05_LIVE_OVERRIDE=S33-PW04_HISTORICAL_MASK6_NAMED_BINDING_REOPENED
TARGETED_R05_NEW_WORKFLOW_CANDIDATE=SPARSE_SOURCE_REPLAY
TARGETED_R05_WORKFLOW_EXTENSIONS=BASIS_ADJOINT_AUDIT,V4_EQUIVARIANT_TRANSPORT_AUDIT,TORSOR_SEMANTIC_VALIDATION
TARGETED_R05_STAGE33_SPECIFIC_DATA_PROMOTED=false
TARGETED_R05_REVOKED_CLAIMS_PROMOTED=false
TARGETED_R05_DUPLICATE_CARDS_CREATED=false
PROVISIONAL_STAGE33_CARD_COUNT=8
ROUTEABLE_FOR_CANDIDATE_DISCOVERY=true
FORMAL_PROMOTION_ACTIVE=false
PERFECT_CUBOID_CONCLUSION=NONE
```