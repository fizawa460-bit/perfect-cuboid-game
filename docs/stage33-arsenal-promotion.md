# Stage33 arsenal promotion — provisional consolidated harvest

```text
REGISTRY=STAGE33-ARSENAL-PROVISIONAL-R06-CONSOLIDATED
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage33
SOURCE_PR=1476
SOURCE_BRANCH=stage33-post1475-j2-v4-generator-adapter
SOURCE_HEAD=b4ed4c898988975f485e48b3803e0f8753c65015
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
THEOREM_CREDIT=false
```

This file is the consolidated Stage33 provisional Arsenal record. It folds the former Gersten/localization and catch-all/dedup supplements into one source-routing document. Active `MAIN-STATE`, source locks, and hostile reopenings always override these provisional cards.

## Live authority override

Current Stage33 authority reopens the historical Picard-adjoint mask-6 named-source binding:

```text
main_state_path=stages/stage33/MAIN-STATE.json
main_state_blob_sha=0bfe5bde4f991cdb47c6da2f1980800ba2a64e58
main_state_canonical_sha256=7d52c93a517fc96050b2f78583ae05e5e4ff4f983c2533c673ca008060bd0226
historical_candidate_canonical_sha256=066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8
historical_mask6_named_J2_source=REOPENED_EXACT_DO_NOT_USE_AS_NAMED_SOURCE
```

The generic marked-basis/adjoint method remains reusable. The concrete historical mask-6 coordinate does not currently carry named J2 proper-Br2 source credit.

## Consolidation result

One same-object split was removed:

```text
S33-PW03 quotient/raw Bockstein adapter
  -> MERGED_INTO S33-PW02 mixed-order finite-module normal-form + liftability gate
S33-PW03_RETIRED_ID=true
ID_REUSE_ALLOWED=false
```

Reason: Smith/invariant-factor transport and raw-order/Bockstein liftability are two phases of the same mixed-order finite-module interface. Splitting them encouraged callers to consume the quotient normal form without retaining the raw extension data needed to decide liftability.

The remaining cards have different inputs/outputs and stay separate:

| Active card | Unique role |
|---|---|
| `S33-PW01` | exact arithmetic-HS zero-survival classifier on a complete invariant block |
| `S33-PW02` | mixed-order finite-module normal form + reversible coordinates + raw-order/Bockstein liftability gate |
| `S33-PW04` | method-level marked basis/dual/adjoint/semantic-orientation source adapter |
| `S33-PW05` | equivariant finite-module source-target compatibility/reachability audit |
| `S33-PW06` | absolute arithmetic `H^1` receiver construction |
| `S33-PW07` | geometric Brauer/cocycle/torsor semantics + integral-kernel/Čech validation |
| `S33-PW08` | explicit Gersten lift -> Galois difference -> arithmetic connecting/localization |

```text
CARD_COUNT_BEFORE_CONSOLIDATION=8
CARD_COUNT_AFTER_CONSOLIDATION=7
MERGED_CARD_IDS=S33-PW03->S33-PW02
FORMAL_SELECTOR_CHANGES=0
STAGE33_MAINLINE_CHANGES=0
```

## S33-PW01 — exact zero-survival HS classifier

**Type:** `ARITHMETIC_HS_CLASSIFIER`

```text
source_path=stages/stage33/33-05/result.md
source_blob_sha=d72bbaf1d7f3200754e0cf2791f53c94c25ad417
primary_canonical_sha256=a48386c523e8c98b1d2b22a7dc3d789e4cea1bfa4557e658fb150e3c6b85a585
hostile_canonical_sha256=4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9
```

A complete finite invariant Brauer block can be discharged by an exact obstruction matrix when the chosen restrictions detect the global obstruction injectively on the whole block and the exact matrix has full rank.

```text
HYPOTHESES=complete invariant block; exact obstruction map; injective detection on tested subgroup; exact rank certificate
APPLICABILITY=finite arithmetic-HS classification of a source-locked invariant block
DO_NOT_USE_FOR=general K3 vanishing; Q-defined representative; incomplete-block inference; sampled vanishing
```

## S33-PW02 — mixed-order finite-module normal form and Bockstein/liftability gate

**Type:** `FINITE_MODULE_NORMAL_FORM_AND_EXTENSION_GATE`

```text
source_path=stages/stage33/33-07/result.md
source_blob_sha=2a5f84a1fd34be395c216b343079ed85a525fb14
invariant_basis_sha256=f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939
liftability_sha256=85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312
```

Reusable contract:

```text
raw mixed-order presentation
-> exact Smith/invariant factors with reversible integral coordinates
-> retain raw representative/order data
-> compute doubling/Bockstein/liftability obstruction
-> only then pass legitimate order-two directions downstream
```

The key firewall is that quotient exponent two does not imply that every raw lift has order two. Reversible Smith coordinates and the raw extension data belong to the same card because the latter determines which quotient directions actually admit the desired lifts.

```text
HYPOTHESES=exact finite abelian presentation; unimodular forward/inverse transforms; raw extension represented; doubling/liftability obstruction computed
APPLICABILITY=mixed-order residue, Kummer, localization, or descent modules before order-two transport
DO_NOT_USE_FOR=global Q-defined lift; arithmetic-HS closure; discarding raw order-four representatives; recovering extension data from invariant factors alone
```

## S33-PW04 — marked basis/adjoint/semantic source adapter

**Type:** `EXACT_MARKED_SOURCE_ADAPTER`

Primary historical method source plus later bridge/orientation sources:

```text
adjoint_path=stages/stage33/33-12/j2-picard-adjoint-proper-br2.json
adjoint_blob_sha=2e70dc274afbbd20aefbb0a87409d66d6ac183bc
historical_adjoint_canonical_sha256=066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8
marked_bridge_path=stages/stage33/33-09/marked-picard-basis-bridge-certified.json
marked_bridge_blob_sha=77b16e2ee80c33af27f7a5a04e1c465e9fc1acea
semantic_orientation_path=stages/stage33/33-12/j2-cv-d2-semantic-orientation.json
semantic_orientation_blob_sha=140acdc9896d1d87a82a1807fd92ce276a620d75
semantic_orientation_canonical_sha256=0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e
```

Reusable method: lock both marked presentations; verify exact Gram/pairing transport and matrix direction; transport dual/adjoint coordinates explicitly; when a finite semantic ambiguity remains, use an independently certified exact fingerprint only if the match is unique and finish with an explicit marked adapter.

```text
HYPOTHESES=locked markings/bases; exact bridge; dual/adjoint convention; pairing/form checks; unique fingerprint when used
APPLICABILITY=source-coordinate construction across Picard/dual/discriminant/Brauer implementations
DO_NOT_USE_FOR=rank/determinant matching as a bridge; unchecked conjugation; non-unique fingerprint guesses; unrelated Pic/2 coefficient copying; historical mask-6 as current named J2 source
```

## S33-PW05 — equivariant source-target compatibility and reachability audit

**Type:** `COMPATIBILITY_AUDIT_METHOD`

```text
target_path=stages/stage33/33-12/full-surface-pic2-kummer-target.json
target_blob_sha=a29e560984034fdfdc38a8d12908efbe23e70ec1
target_canonical_sha256=384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890
audit_path=stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json
audit_blob_sha=40dc28e0bae28208fb1dda3fc1a1578b62606f13
audit_canonical_sha256=463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229
generator_diagnostic_path=stages/stage33/33-12/diagnose_j2_v4_generator_identification.py
generator_diagnostic_blob_sha=9595fb207eb4a6a18d653df1e8846258fcba59aa
```

Given explicit finite source and target modules with locked actions/bases, compute exact intertwiners/compatible extensions and reachable image. If generator labels may be the only ambiguity, exhaust the finite automorphism/relabeling set diagnostically without changing locked coordinates.

```text
HYPOTHESES=both modules/bases/actions explicit; exact compatibility equations; finite relabeling set enumerable when used
APPLICABILITY=Kummer/descent/cohomology identities assembled from independently computed coordinates
DO_NOT_USE_FOR=dimension-only binding; arbitrary relabeling; positive diagnostic as geometric identification; repairing an invalid PW04 source merely by relabeling; absolute H1 identification
```

PW04 constructs/orients a marked source coordinate. PW05 tests an independently defined source-target module relation. They are intentionally separate.

## S33-PW06 — absolute arithmetic H1 receiver construction

**Type:** `ABSOLUTE_COHOMOLOGY_RECEIVER_RECIPE`

```text
path=stages/stage33/33-10/result.md
blob_sha=49bb309f994742874572f485bd5e594fe4439ed4
closed_interface_canonical_sha256=4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f
```

Reusable method:

```text
1. Compute the exact absolute Galois-module decomposition.
2. Apply continuous Shapiro to induced/permutation summands when its hypotheses hold.
3. Handle quotient blocks through the long exact sequence, retaining kernel/cokernel terms.
4. Do not split residual extensions without proof.
5. Only then define the arithmetic H1/localization receiver.
```

```text
HYPOTHESES=exact Galois-module decomposition; valid continuous-Shapiro and LES inputs
APPLICABILITY=absolute H1 receivers when finite quotient action is known but kernel Galois terms may contribute
DO_NOT_USE_FOR=H1(V4,K)=H1(G_Q,K); killing kernel terms; automatic localization values; unproved splitting
```

PW06 defines the receiver; PW08 constructs classes that land in it. They are not duplicates.

## S33-PW07 — geometric Brauer/cocycle/torsor and literal representative validation

**Type:** `TORSOR_BRAUER_INTEGRAL_KERNEL_ADAPTER`

```text
torsor_path=stages/stage33/33-05/j2-r4-correct-translation-torsor.json
torsor_blob_sha=5a0ac87e7afc7b048d6bbe9c12bea7fe91a0348b
torsor_canonical_sha256=ef72c43811428acb2d4c1ea58d4867d7bbcc5c20774b6724eb8b272450cd0725
hostile_kernel_path=stages/stage33/33-05/j2-r4-hostile-torsor-brauer-kernel-verification.json
hostile_kernel_blob_sha=32be9c1f272a4b12d032bbba00d9bbea1edf2622
cech_path=stages/stage33/33-12/j2-cc-actual-cech-global-square-overlap.json
cech_blob_sha=93383a6135a05b1a1d5a55f6261b2ab5f3c94120
cech_result_canonical_sha256=82ac2b6fe8d023c915e9cf3bb8ff38d4782dbec47f98e2593f964ea020ccc6fd
```

Reusable contract:

```text
Brauer representative/class
-> exact cohomological/translation-valued cocycle
-> semilinear translation descent using the SAME cocycle
-> genus-one torsor with the intended Jacobian
-> Brauer/Ogg-Shafarevich identification
-> integral transcendental-kernel identification when hypotheses apply
```

For literal representatives, compute the actual transition function/divisor/Cartier data and transport the resulting Picard class exactly; “generically a square” is not enough.

```text
HYPOTHESES=exact common cocycle; intended relative Jacobian; valid Brauer/OS dictionary; semilinear descent; resolved literal representative when used; integral-kernel theorem hypotheses
APPLICABILITY=geometric Brauer classes with explicit torsor semantics and exact representative/divisor data
DO_NOT_USE_FOR=Q-defined descent; arbitrary genus-one curves; isogeny-cover substitution; same-j-invariant inference; rational Hodge isometry alone; geometric Pic zero as arithmetic localization zero
```

## S33-PW08 — explicit Gersten connecting/localization adapter

**Type:** `GERSTEN_CONNECTING_LOCALIZATION_ADAPTER`

```text
hostile_negative_path=stages/stage33/33-11/audit-state.json
hostile_negative_blob_sha=dfb1072cae83618e281bfd555d7f6ef25f853fa4
materializer_path=stages/stage33/33-11/materialize_stage33_11_a2_26_explicit_gersten_difference_preimage.py
materializer_blob_sha=b8906f50ef8a0e82dba4eeae76d14f920cd8c87c
verifier_path=stages/stage33/33-11/verify_stage33_11_a2_26_explicit_gersten_difference_preimage.py
verifier_blob_sha=4c0c042020af539ce28f4746c82a8e13874378c7
closure_path=stages/stage33/33-12/result.md
closure_blob_sha=fc410a317d71362153aba8aa9489b005d1d3e45d
localization_canonical_sha256=233be042e92010be169206df1193f25375ee9fd768f7fb3eebb9eb696389632e
```

Reusable contract:

```text
1. Pin the residue/Gersten complex, source basis, target kernel and group action.
2. Materialize a representative lift without assuming equivariance.
3. Attach ambient factors to the actual height-one valuations on the resolved object, including exceptional contributions.
4. Materialize the required purity/off-boundary correction.
5. Compute g(L)-L for every required generator/direction.
6. Reduce into the locked absolute-H1 receiver coordinates.
7. Materialize every connecting/localization column.
8. Independently verify and hostile-replay the complete column set.
```

```text
HYPOTHESES=exact Gersten/residue complex; explicit group action; actual valuation attachment; materialized purity correction; locked PW06 receiver; complete column verification
APPLICABILITY=arithmetic localization/connecting morphisms built from explicit residue representatives
DO_NOT_USE_FOR=visible-boundary invariance shortcut; assumed equivariant lift; dimension-only zero; project-independent zero localization; global-Q lift from zero localization
```

The concrete Stage33 zero map is provenance only; PW08 promotes the construction/audit protocol, not that value.

## Workflow vocabulary after consolidation

Canonical workflows:

| Workflow | Includes |
|---|---|
| `SMITH_ROUNDTRIP` | reversible normal-form coordinates inside PW02 |
| `MIXED_ORDER_RESIDUE_TO_LOCALIZATION` | PW02 normal form + Bockstein gate -> legitimate representative -> PW08 localization |
| `BASIS_ADJOINT_AUDIT` | marked bridge, dual/adjoint conventions, form checks, unique semantic orientation |
| `V4_EQUIVARIANT_TRANSPORT_AUDIT` | action intertwining, reachable image, exhaustive finite-group relabeling diagnostics |
| `HS_ZERO_SURVIVAL_MATRIX` | complete invariant block + exact obstruction rank |
| `ABSOLUTE_H1_RECEIVER_DECOMPOSITION` | continuous absolute-H1 receiver construction |
| `TORSOR_SEMANTIC_VALIDATION` | exact torsor/cocycle semantics + literal Čech/divisor validation |
| `CONNECTING_MAP_FAIL_CLOSED` | actual columns before credit + hostile replay after repair |
| `RESOLVED_VALUATION_ATTACHMENT` | ambient factors -> actual resolved height-one valuations |
| `ARITHMETIC_LIFT_FIREWALL` | finite/local exactness != global-Q lift |
| `SPARSE_SOURCE_REPLAY` | reconstruct only exact leaf-required support from retained source formulas/adapters |

`SPARSE_SOURCE_REPLAY` source lock:

```text
path=stages/stage33/33-12/j2-ct-six-kc-support-fullpic64-pullbacks.json
blob_sha=a07ab8b0c9fd0b683db5845d75e2749a2882d546
canonical_sha256=592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d
```

Cross-basis transport, lattice-fingerprint orientation, Čech divisor audit, and generator relabeling are subroutines of the canonical workflows above, not separate workflow families.

## Duplicate check

The full Stage33 provisional set was checked after merging PW03:

- PW01 vs PW06: classifier/obstruction elimination vs construction of the absolute cohomology receiver — distinct.
- PW02 vs PW08: finite normal form/liftability vs explicit Gersten connecting class — distinct; PW08 consumes legitimate directions from PW02.
- PW04 vs PW05: source construction/orientation vs independent source-target equivariance/reachability — distinct.
- PW06 vs PW08: receiver vs map/class construction into the receiver — distinct.
- PW07 vs PW08: geometric Brauer/torsor/Čech semantics vs arithmetic Gersten localization — distinct.
- PW02 and former PW03 were the only card-level same-object split and are now merged.

Stage32 PW05 and Stage33 PW05 both use finite-group structure, but Stage32 reconstructs invariant values from symmetry orbits whereas Stage33 audits an independently defined source-target intertwiner/reachability relation; they are not duplicates.

## Revoked / hostile / Stage33-specific non-promotion boundary

Do not promote or restore:

```text
C2 + C3 = h_J2
historical_picard_adjoint_mask6_as_named_J2_source
copy_u1_A_T_2_coefficients_into_proper_Br2_dual_basis
direct_order4_picard_pullback_route_for_J2_source
visible_boundary_fixed_implies_equivariant_global_Gersten_lift
pre_repair_working_zero_localization_columns
old_Stage33_07_global_Q_residue_lift_inventory_closes_arithmetic_descent
```

Concrete Stage33 ranks, invariant-factor counts, J2/Kc coordinates, basis names, action matrices, torsor coefficients, six-row sparse support, Čech zero vector, localization-zero columns, and individual relabeling-test outcomes remain provenance only.

## Final provisional boundary

```text
PROVISIONAL_WEAPONS=S33-PW01,S33-PW02,S33-PW04,S33-PW05,S33-PW06,S33-PW07,S33-PW08
RETIRED_MERGED_IDS=S33-PW03->S33-PW02
PROVISIONAL_CARD_COUNT=7
STAGE33_SPECIFIC_DATA_PROMOTED=false
REVOKED_CLAIMS_PROMOTED=false
ROUTEABLE_FOR_CANDIDATE_DISCOVERY=true
FORMAL_PROMOTION_ACTIVE=false
FINAL_PROMOTION_REVIEW_REQUIRED_AT_STAGE33_CLOSE=true
PERFECT_CUBOID_CONCLUSION=NONE
```
