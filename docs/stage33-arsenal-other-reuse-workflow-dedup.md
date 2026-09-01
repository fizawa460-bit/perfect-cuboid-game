# Stage33 Arsenal provisional harvest — other reusable mathematics / workflow consolidation / full dedup

```text
REGISTRY=STAGE33-ARSENAL-PROVISIONAL-R05-SUPPLEMENT
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage33
SOURCE_PR=1476
SOURCE_BRANCH=stage33-post1475-j2-v4-generator-adapter
SOURCE_HEAD=73a0e5fa0b1694997b99df29ae63b08cbebabf39
PARENT_PROMOTION_FILE=docs/stage33-arsenal-promotion.md
GERSTEN_SUPPLEMENT=docs/stage33-arsenal-gersten-residue-promotion.md
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
THEOREM_CREDIT=false
```

This is the final targeted catch-all pass for Stage33 material not already covered by the Picard/Kummer/finite-module pass, the Brauer/HS/descent/torsor pass, or the Gersten/residue/localization pass. It also normalizes overlap among all current Stage33 provisional cards and workflow candidates.

The pass was reverse-indexed from `stages/stage33/MAIN-STATE.json`, the closed Stage33-09 Picard transport checkpoint, and the current Stage33-12 result/current-leaf source locks. Stage33 history was not reread sequentially.

```text
main_state_path=stages/stage33/MAIN-STATE.json
main_state_blob_sha=d32fa72fc321a0d6f50485ecc8c6abd4c690a378
main_state_canonical_sha256=32baebf358ae47b99a5a1ffd40dc90e7eb090db353f58861702bba3f0db0a9fc
stage33_09_result_path=stages/stage33/33-09/result.md
stage33_09_result_blob_sha=820543c4778851f5b7487e6d09a6274ee0cceed3
stage33_09_closure_path=stages/stage33/33-09/stage33-09-closure.json
stage33_09_closure_blob_sha=0e388cac1d5287ee5b2a3288c10153c16e99fb2a
stage33_09_closure_canonical_sha256=6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7
stage33_12_result_path=stages/stage33/33-12/result.md
stage33_12_result_blob_sha=fc410a317d71362153aba8aa9489b005d1d3e45d
```

## R05 classification

| Harvest object | Class | Arsenal disposition | Source path / SHA | Hypotheses / applicability | DO_NOT_USE_FOR |
|---|---|---|---|---|---|
| Exact marked Picard basis bridge + Gram/action intertwining across implementations/bases | **1. Arsenal candidate** | **Integrate into `S33-PW04` and `S33-PW05`; no new card.** PW04 owns basis/coordinate transport; PW05 owns equivariance/intertwining. | `stages/stage33/33-09/marked-picard-basis-bridge-certified.json`, blob `77b16e2ee80c33af27f7a5a04e1c465e9fc1acea`; closure `stages/stage33/33-09/stage33-09-closure.json`, blob `0e388cac1d5287ee5b2a3288c10153c16e99fb2a`, canonical `6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7` | Two presentations of the same marked lattice/module are source-locked; an exact bridge is known; Gram forms and named group actions are available on both sides. Reuse requires checking transport of the form and intertwining of every action actually used downstream. | Treating an invertible rational bridge as an integral/unimodular identification when it is not; transporting an action not explicitly checked; identifying semantically different markings merely because dimensions match. |
| Lattice-fingerprint semantic orientation under a finite ambiguity | **1. Arsenal candidate** | **Integrate into `S33-PW04`** as a semantic-orientation sub-adapter; no new card. | `stages/stage33/33-12/j2-cv-d2-semantic-orientation.json`, blob `140acdc9896d1d87a82a1807fd92ce276a620d75`, canonical `0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e` | A finite candidate set is already exact; each candidate has a source-locked invariant fingerprint; the observed geometric object has an independently certified invariant; the fingerprint match is unique; any subsequent coordinate identification is made through an explicit marked adapter. | Guessing a label from a non-unique norm/discriminant; claiming a canonical identification of two different modules from a matching scalar invariant; bypassing explicit basis/marking adapters. |
| Exact Čech representative -> divisor/Pic class -> mod-2 coordinate validation | **1. Arsenal candidate** | **Integrate into `S33-PW07`**; `PW08` begins only at the later arithmetic Gersten/localization layer. | `stages/stage33/33-12/j2-cc-actual-cech-global-square-overlap.json`, blob `93383a6135a05b1a1d5a55f6261b2ab5f3c94120`; exact conclusion summarized in `33-12/result.md`, canonical `82ac2b6fe8d023c915e9cf3bb8ff38d4782dbec47f98e2593f964ea020ccc6fd` | A literal Čech/overlap representative is materialized on the required charts; transition/basis-change determinant is explicit as a rational function; its Cartier divisor is computed on the smooth/resolved object; the resulting integral Pic class is then transported to Pic/2 coordinates. | Replacing an actual representative calculation by “the symbol is generically a square”; inferring an arithmetic localization/absolute-H1 statement from a geometric Pic-class zero; reusing the Stage33 zero value elsewhere. |
| Exact sparse source-preserving replay of only the rows needed by a leaf | **2. Workflow candidate** | **New workflow candidate `SPARSE_SOURCE_REPLAY`**. This is operational reuse, not a mathematical card. | `stages/stage33/33-12/j2-ct-six-kc-support-fullpic64-pullbacks.json`, blob `a07ab8b0c9fd0b683db5845d75e2749a2882d546`, canonical `592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d`; `33-12/result.md`, blob `fc410a317d71362153aba8aa9489b005d1d3e45d` | The target leaf depends on a small, explicitly known support; each needed row can be independently reconstructed from retained source formulas/evidence and transported through source-locked adapters; support closure is verified. | Synthesizing missing rows by interpolation; claiming equivalence to a historical giant matrix without rowwise verification; using sparse replay when downstream operations depend on unmaterialized rows. |
| Exhaustive finite-group generator/relabeling diagnostic | **2. Workflow candidate** | **Extend existing `V4_EQUIVARIANT_TRANSPORT_AUDIT`; do not create a second workflow family.** | `stages/stage33/33-12/diagnose_j2_v4_generator_identification.py`, blob `9595fb207eb4a6a18d653df1e8846258fcba59aa` | Source and target actions are independently locked; the finite group automorphism set is small enough to enumerate exactly; each relabeling is tested against the complete compatibility/reachability equations rather than label names alone. | Promoting a positive diagnostic row to a geometric extension, named relation, or standard matrix column; changing locked source/target coordinates to make a diagnostic pass; treating label mismatch as the only possible adapter defect without exhaustive test. |
| Cross-basis equivariant transport audit | **2. Workflow candidate** | **Extend `BASIS_ADJOINT_AUDIT` + `V4_EQUIVARIANT_TRANSPORT_AUDIT`; alias only, not a new canonical workflow.** | Stage33-09 result/blob `820543c4778851f5b7487e6d09a6274ee0cceed3`; certified bridge blob `77b16e2e...`; closure canonical `6c3ff8f7...` | Verify source/target bases, bridge, form transport, inverse/round-trip where applicable, and action intertwining before consuming coordinates. | “Same rank” or “same Gram determinant” as a coordinate adapter; action transport by unchecked conjugation. |
| Lattice-fingerprint semantic-orientation audit | **2. Workflow candidate** | **Extend `BASIS_ADJOINT_AUDIT`; no separate workflow family.** | semantic orientation blob `140acdc9896d1d87a82a1807fd92ce276a620d75`, canonical `0a5abe...` | Candidate fingerprints and observed invariant are independently exact and the match is unique. | Non-unique fingerprint matching; canonical-module claims unsupported by an explicit adapter. |
| Čech representative/divisor audit | **2. Workflow candidate** | **Extend `TORSOR_SEMANTIC_VALIDATION`; no separate workflow family.** | Čech certificate blob `93383a6135a05b1a1d5a55f6261b2ab5f3c94120`; result canonical `82ac2b6f...` | Literal representative and divisor data exist on the actual resolved geometry. | Generic-symbol shortcuts; arithmetic localization conclusions. |
| Concrete Stage33-09 basis bridge determinant, historical basis labels, named `cc/ct`/coordinate-swap matrices, and project-specific marked actions | **3. Stage33-specific — no promotion** | Provenance/example only | `stages/stage33/33-09/*`, especially certified bridge blob `77b16e2e...` and closure blob `0e388cac...` | Locked Stage33 Fermat-quartic/Picard presentations only. | Reusing dimensions, determinant, matrices, or labels in another surface/lattice. |
| Concrete J2 minimum norm `8`, the three `4/8/12` fingerprints, semantic label `u1`, marked coordinate `[1,0]` | **3. Stage33-specific — no promotion** | Only the fingerprint-selection method is integrated into PW04 | semantic orientation canonical `0a5abe...` | Locked Kc/J2 marked transcendental lattice only. | Generic norm tables or naming another class. |
| Concrete six-row ct support, Pic64 weights, and exact Stage33 sparse-replay payload | **3. Stage33-specific — no promotion** | Workflow example only | sparse replay canonical `59270459...` | Locked J2 ct defect and Stage33 Pic64 transport only. | Assuming six rows suffice for a different leaf/matrix. |
| Concrete Čech scalar/overlap and resulting zero Pic/2 vector | **3. Stage33-specific — no promotion** | Method goes to PW07; value remains local | Čech result canonical `82ac2b6f...` | Locked corrected-J2 Čech representative only. | Predicting zero for another torsor/cocycle or arithmetic connecting map. |
| Concrete result of the six V4 relative label tests | **3. Stage33-specific — no promotion** | Diagnostic outcome only | diagnostic script blob `9595fb20...`; PR #1476 current leaf remains source-target repair | Locked Stage33 Pic/2, proper-Br2 and J2 target/source modules only. | Restoring `C2+C3=h_J2`, assigning a standard Kummer column, or claiming the geometric extension has been identified. |

## Reusable contracts integrated in R05

### PW04 extension — marked basis and semantic orientation

PW04 now owns the general source-side preparation boundary:

```text
exact source object
-> exact marked basis/dual-basis conventions
-> explicit bridge between coordinate systems
-> Gram/pairing round-trip
-> finite candidate semantic orientation by independently certified unique invariants
-> exact source coordinate
```

The semantic fingerprint is a selector only when uniqueness is certified. A matching norm or discriminant by itself is not a basis identification.

### PW05 extension — equivariant transport and finite relabeling

PW05 begins after source and target coordinates/actions are independently defined:

```text
locked source action + locked target action
-> verify bridge/action intertwining
-> if generator labels may differ, enumerate all relevant finite-group automorphisms exactly
-> solve the full compatibility/extension equations for each identification
-> compute reachable quotient/cohomology image
-> accept a named binding only if the locked target lies in the reachable image
```

A relabeling diagnostic is evidence about the adapter space, not evidence that a geometric extension or named Kummer relation exists.

### PW07 extension — literal representative semantics before arithmetic localization

PW07 owns validation that a geometric cocycle/torsor representative actually means what is claimed:

```text
literal Čech/transition representative
-> exact basis change / overlap ratio
-> Cartier/principal divisor on the actual resolved geometry
-> integral Pic class
-> Pic/2 or geometric cocycle coordinate
```

PW08 starts later, when a boundary/residue class must be lifted through the Gersten complex and mapped by an arithmetic connecting/localization morphism. This keeps geometric representative-zero and arithmetic localization-zero logically separate.

## Workflow consolidation

Canonical Stage33 workflow vocabulary after R05:

| Canonical workflow | R05 treatment | Includes / aliases |
|---|---|---|
| `SMITH_ROUNDTRIP` | retain | exact presentation <-> invariant-factor coordinate witnesses |
| `BASIS_ADJOINT_AUDIT` | extend | dual-basis conventions; cross-basis bridge; Gram/pairing round-trip; lattice-fingerprint semantic orientation |
| `V4_EQUIVARIANT_TRANSPORT_AUDIT` | extend | action intertwining; source-target reachability; exhaustive finite-group generator relabeling diagnostics |
| `HS_ZERO_SURVIVAL_MATRIX` | retain | exact HS differential/survival matrix protocol |
| `ABSOLUTE_H1_RECEIVER_DECOMPOSITION` | retain | finite quotient vs absolute continuous-H1 receiver construction |
| `TORSOR_SEMANTIC_VALIDATION` | extend | exact cocycle/torsor semantics; Čech representative/divisor validation |
| `CONNECTING_MAP_FAIL_CLOSED` | retain/extended by PW08 | no connecting credit before actual columns; hostile replay after repair |
| `MIXED_ORDER_RESIDUE_TO_LOCALIZATION` | retain | residue normal form -> Bockstein -> localization ordering |
| `RESOLVED_VALUATION_ATTACHMENT` | retain | ambient factors -> actual height-one valuations/exceptions |
| `ARITHMETIC_LIFT_FIREWALL` | retain | finite/local exactness != global-Q arithmetic lift |
| `SPARSE_SOURCE_REPLAY` | **new workflow candidate** | reconstruct only required support from source formulas with rowwise locks; avoid giant black-box regeneration |

Do not add separate canonical workflow names for `CROSS_BASIS_EQUIVARIANT_TRANSPORT_AUDIT`, `LATTICE_FINGERPRINT_SEMANTIC_ORIENTATION`, `CECH_REPRESENTATIVE_DIVISOR_AUDIT`, or `FINITE_GROUP_GENERATOR_RELABELING_DIAGNOSTIC`; they are subroutines of the canonical workflows above.

## Full Stage33 provisional-card dedup boundary

There are still exactly eight provisional cards. R05 creates no ninth card.

| Card | Unique reusable role | Nearest overlap and boundary |
|---|---|---|
| `S33-PW01` | exact arithmetic-HS zero-survival classifier | PW06 constructs the receiver; PW01 decides survival/differential behavior in a locked arithmetic-HS problem |
| `S33-PW02` | exact finite residue/module presentation -> invariant factors with reversible coordinates | PW03 starts where extension/raw-order information matters; Smith form alone cannot recover Bockstein data |
| `S33-PW03` | quotient-vs-raw order / Bockstein liftability gate | PW02 normalizes the finite module; PW03 prevents order-two quotient data from erasing order-four lift information |
| `S33-PW04` | source-side marked basis/dual/adjoint/semantic-orientation adapter | PW05 does not define the source coordinate; it tests source-target equivariance/reachability after both sides are locked |
| `S33-PW05` | exact equivariant source-target compatibility/reachability adapter | PW04 prepares coordinates; PW05 checks whether a named binding is realizable under compatible group-module structure |
| `S33-PW06` | exact absolute arithmetic H1 receiver construction / finite-H1 warning | PW01 is a survival gate; PW08 constructs connecting/localization classes that must land in the PW06 receiver |
| `S33-PW07` | geometric Brauer/cocycle/translation-torsor/integral-kernel semantics, including literal Čech representative validation | PW08 is later arithmetic Gersten localization; geometric representative zero does not imply arithmetic connecting zero |
| `S33-PW08` | explicit Gersten lift -> Galois difference -> connecting/localization adapter | PW07 validates the geometric representative; PW06 supplies the absolute receiver; PW08 computes the arithmetic connecting class |

```text
R05_DEDUP_CARD_COUNT_BEFORE=8
R05_DEDUP_CARD_COUNT_AFTER=8
R05_NEW_CARD_COUNT=0
R05_MERGED_OR_DELETED_CARD_COUNT=0
R05_FORMAL_SELECTOR_CHANGES=0
```

## Revoked / hostile / superseded exclusions

The following remain outside Arsenal credit:

```text
C2 + C3 = h_J2
status=REVOKED_EXACT_DO_NOT_USE
revoking_sha256=463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229

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
positive_generator_relabeling_diagnostic => NO_GEOMETRIC_EXTENSION_OR_COLUMN_CREDIT
sparse_support_replay_without_complete_dependency_support => NO_EQUIVALENCE_TO_FULL_MATRIX
geometric_Cech_Pic_zero => NO_AUTOMATIC_ARITHMETIC_LOCALIZATION_ZERO
```

The active Stage33 source remains authoritative. These provisional cards/workflows are discovery aids only and must be source-revalidated before reuse.

```text
TARGETED_R05_NEW_CARD_COUNT=0
TARGETED_R05_INTEGRATED_CARDS=S33-PW04,S33-PW05,S33-PW07
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