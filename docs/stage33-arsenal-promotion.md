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

## Post-#1478 second provisional harvest provenance

This section records the second Stage33 provisional harvest implemented after the discovery/dedup ledger in PR `#1665`. It does not replace the first-harvest provenance above.

```text
PREVIOUS_ARSENAL_INTEGRATION_PR=1478
PREVIOUS_ARSENAL_MERGE_COMMIT=b5b810be420eedc74cfa8074ae043d681598b412
DISCOVERY_DEDUP_PR=1665
DISCOVERY_DEDUP_EXACT_HEAD=4fb7d980be0452277aab9d5b96e64fabf4d5e9a7
DISCOVERY_DEDUP_FRESHNESS_SYNC_COMMIT=4fb7d980be0452277aab9d5b96e64fabf4d5e9a7
DISCOVERY_DEDUP_SYNCED_MAIN_HEAD=f8522bd1a38fa551186ad370f51d17c73c7927e2
DISCOVERY_DEDUP_STATE_AT_HARVEST3=OPEN_NOT_MERGED
DISCOVERY_LOWER_BOUND=b5b810be420eedc74cfa8074ae043d681598b412
HARVEST_UPPER_BOUND=a3c64f5704f3d1fd297e3b95377ba1938d277178
EXACT_COMPARISON_RULE=#1478 merge -> Harvest 1 upper bound
HARVEST3_RANGE_EXPANDED=false
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
MATURITY=PROVISIONAL
STAGE33_PROGRESS_CHANGE=0
STAGE33_MAIN_AUTHORITY_CHANGE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_CONCLUSION=NONE
```

Inspected scope was the frozen post-#1478 Stage33 range represented by `33-05`, `33-07`, and principally `33-12`, together with the existing Stage33 provisional cards and Stage30/31/34 formal dedup comparators. Main commits after `a3c64f5704f3d1fd297e3b95377ba1938d277178` are outside this harvest.

Harvest 2 classification implemented here:

- new provisional weapons: `S33-PW09`, `S33-PW10`;
- extended existing weapon: `S33-PW04`;
- new provisional workflows: `S33-WF01`, `S33-WF02`;
- rejected duplicates: `DISC-S33-B02`, `DISC-S33-B03`, `DISC-S33-B04`, `DISC-S33-C04`;
- historical/negative only: 10 classification units;
- Stage33-specific/nonpromoted: J2/V25 concrete labels and masks, e3/mask20/fixed-space numerics, and swap23 package counts.

Freshness synchronization of PR `#1665` changed only its ancestry against current main `f8522bd1a38fa551186ad370f51d17c73c7927e2`. The immutable harvest upper bound remains `a3c64f5704f3d1fd297e3b95377ba1938d277178`; the later `#1663` main commit is not harvested by this promotion.

The discovery PR is provenance, not Stage33 MAIN authority. Active `stages/stage33/MAIN-STATE.json` and controller/source locks must be refetched at card use. The mutable live Stage state is deliberately not part of the permanent mathematical identity of these cards.

## Prior-harvest live-authority snapshot

The following block is retained as historical first-harvest provenance, not as current mutable authority. Current Stage33 `MAIN-STATE`/controller must be refetched before any provisional card is used.

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
HYPOTHESES=locked markings/bases; exact bridge; dual/adjoint convention; pairing/form checks; unique fingerprint when used; when a literal H2(mu2)->Br[2] marked quotient is load-bearing, a source-bound quotient witness for that literal source is required
APPLICABILITY=source-coordinate construction across Picard/dual/discriminant/Brauer implementations; source-bound marked quotient provenance checks
DO_NOT_USE_FOR=rank/determinant matching as a bridge; unchecked conjugation; non-unique fingerprint guesses; unrelated Pic/2 coefficient copying; historical mask-6 as current named J2 source; abstract Kummer quotient arrow as marked-coordinate computation; target-side Picard/discriminant adjoint or dimension/position coincidence as the missing source quotient map; another source's marked equality by relabelling
```

Post-#1478 extension source lock:

```text
source_pr=1646
source_exact_head=5471181a4decdc319cf3f00080d85da6d6e9fbb0
obstruction_path=stages/stage33/33-12/e3-v91c1f-a2-02-source-bound-kummer-quotient-marking-obstruction.json
obstruction_blob_sha=c9cb07f374d26d52e57e16dbc285892d414d9dd2
obstruction_canonical_sha256=4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273
verifier_path=stages/stage33/33-12/verify_e3_v91c1f_a2_02_source_bound_kummer_quotient_marking_obstruction.py
verifier_blob_sha=fe7bbd9306bc905853c21993ffb4ffa94aef8bb3
```

When that source-bound quotient witness is missing, acceptable witness forms are limited to: a direct Čech/symbol/corestriction evaluation in the locked marked basis; an exact geometric quotient/pullback adapter to an independently named Brauer class already marked there; or a source-bound Kummer extension/section datum computing the literal seed's quotient image. This extension adds a failure contract to PW04; it does not make the V91C1F Stage33 source itself a successful marked image.

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

## S33-PW09 — marked Kummer lift binding adapter

**Type:** `MARKED_KUMMER_LIFT_BINDING_ADAPTER`

```text
source_pr=1488
source_exact_head=8672a500f65d96e23b420f0d37bc16e69f09081b
key_source_commit=9a01ec5a5c87782e44f1bffe91cc85e89db25fa1
certificate_path=stages/stage33/33-12/j2-genuine-h2-mu2-kummer-adapter-v25.json
certificate_blob_sha=ac34f0177e3f7427f74a1d798a99fc51afdf4e66
certificate_canonical_sha256=d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c
producer_path=stages/stage33/33-12/certify_j2_genuine_h2_mu2_kummer_adapter_v25.py
producer_blob_sha=32404e98042b0a4cb035581fc7d9db67163eaec1
verifier_path=stages/stage33/33-12/verify_j2_genuine_h2_mu2_kummer_adapter_v25.py
verifier_blob_sha=7e018259d5cc683015e2b03b118740dd2ac0c525
```

Reusable contract:

```text
independently named Br[2] source
+ concrete genuine full-surface Cech H2(mu2) preimage/lift
+ independently locked marked Brauer coordinate for that named source
+ exact source-locked geometric pullback/projection when used
-> verify that the concrete lift and the named source have the same marked Brauer image
-> only then permit downstream Kummer/cohomology computation from that lift
```

```text
HYPOTHESES=named Brauer source independently established; genuine full-surface H2(mu2) lift materialized; marked Brauer coordinate independently established; source/lift equality proved in that marking; every pullback/projection source-locked
APPLICABILITY=source-bound Kummer lift construction when a concrete cohomological representative must be tied to an independently named Brauer class before downstream calculations
DO_NOT_USE_FOR=abstract Kummer exact sequence as marked equality; another source's equality by relabelling; raw H1 proxy as a Kummer boundary; source-specific functions/masks/projections as generic constants; downstream connecting cocycle or Kummer column unless separately materialized
```

Exact upstream locks include V21 canonical `19c464602d6ad1b6c32b0b08c50a6bcc55b8e606642a5ae52e7f51fdc2f12366`, V24 canonical `9d104c7d4054b5d92f1df382654b152c30ca0be6ef267aa028fe8b9d78a4687d`, explicit lift canonical `6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b`, and surface contract canonical `55cd01cc8570cb759e7029ddef3b9dac764625a7cdd313c76fd694e37fd478ce`. J2 names, functions, masks, and `forget c` are provenance only and do not transfer.

## S33-PW10 — resolved purity / Čech-Cartier full-surface seed assembler

**Type:** `RESOLVED_PURITY_CECH_CARTIER_SEED_ASSEMBLER`

```text
source_pr=1634
source_exact_head=1c76c3164681f225c42905067ee0d7d6c4a17418
certificate_path=stages/stage33/33-12/e3-v91c1d-a2-02-purity-cech-cartier-assembly.json
certificate_blob_sha=eea5f083039abf52483c4faebbce547ae6c450c5
certificate_canonical_sha256=fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14
diagnostic_path=stages/stage33/33-12/diagnose_e3_v91c1d_a2_02_v4_transition_selector.py
diagnostic_blob_sha=158c89c1538d0d3da1e332b202197028540d8ab3
verifier_path=stages/stage33/33-12/verify_e3_v91c1d_a2_02_purity_cech_cartier_assembly.py
verifier_blob_sha=21827a085c0f3039ab3cd6786483de4bb13d5db9
```

Reusable contract:

```text
actual resolved height-one prime attachments
+ resolution-exceptional residue data
+ exact prime-level group transport
+ function-level scalar-unit data
-> compute literal prime-package differences
-> derive, rather than assume, purity/off-boundary correction
-> materialize prime-level Cech transition data
-> bind the Cartier transition/correction
-> assemble a literal full-surface Cech-Cartier seed
```

```text
HYPOTHESES=codimension-one and resolution-exceptional residue audit complete; actual height-one attachments explicit; prime-level transport source-locked; scalar units exact; off-boundary correction derived from literal differences
APPLICABILITY=resolved-surface cohomological constructions where local residue packages must become a literal full-surface representative before a later marked quotient/localization step
DO_NOT_USE_FOR=marked Brauer image; source-specific H2(mu2)->Br[2] quotient coordinate; genuine named downstream Kummer lift; Kummer column; assumed equivariance in place of purity correction
```

Exact upstream locks include the literal boundary seed canonical `7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403`, strict-transform prime refinement canonical `ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6`, boundary scalar descent canonical `e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b`, and Stage33-11e prime transport chain canonical `1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426`.

The Stage33 A2_02 component IDs, counts, and target numerics are not part of this reusable contract.

## S33-WF01 — first missing witness type/provenance gate

**Type / placement:** `FIRST_MISSING_WITNESS_TYPE_PROVENANCE_GATE` / `PROVISIONAL_WORKFLOW`

```text
source_prs=1639,1646
source_heads=86eae9776d15479310ff6843d38614cb03498e21,5471181a4decdc319cf3f00080d85da6d6e9fbb0
preflight_path=stages/stage33/33-12/e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json
preflight_blob_sha=3a2547188bb0c2aece74094fe93de5f89707e5c2
preflight_canonical_sha256=5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f
preflight_verifier=stages/stage33/33-12/verify_e3_v91c1e_a2_02_marked_brauer_image_adapter_preflight.py
preflight_verifier_blob_sha=f770b270787955db61551714d68b7e2705b45588
obstruction_canonical_sha256=4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273
```

Reusable workflow:

```text
1. lock the already-materialized source and target objects and their semantic types;
2. identify the first load-bearing edge that is not actually materialized;
3. state its exact input type and required output type;
4. enumerate acceptable witness forms capable of filling that edge;
5. distinguish a bounded search miss from repository-wide absence or mathematical nonexistence;
6. fail-close every downstream credit that depends on the missing edge;
7. resume construction at that first missing witness rather than rerunning upstream work.
```

```text
HYPOTHESES=upstream assets source-locked; semantic input/output types explicit; downstream dependency on the missing edge explicit
APPLICABILITY=long certificate/adapter chains where many neighboring interfaces exist and one source-bound witness controls further credit
DO_NOT_USE_FOR=search miss as nonexistence; missing implementation as theorem obstruction; skipping upstream source validation; granting credit because target-side data have the right dimension or shape
```

This workflow specializes the generic `S30-WF03` credit firewall by locating the next constructive witness. It is not a mathematical selector.

## S33-WF02 — marked quotient evaluation-obligation decomposition

**Type / placement:** `MARKED_QUOTIENT_EVALUATION_OBLIGATION_DECOMPOSITION` / `PROVISIONAL_WORKFLOW`

```text
source_pr=1653
source_exact_head=d7750f80571a8da7f4edfee43924121efa5aa15a
certificate_path=stages/stage33/33-12/e3-v91c1l-a2-02-cech-to-marked-discriminant-dual-evaluation-contract.json
certificate_blob_sha=02eda1efe38c1cca42aa96c2139bcdd66bc5ec81
certificate_canonical_sha256=6ae7e0464c2acd012c1c486e6a12fdb806d65049359c0c6c2440168be138e3dc
verifier_path=stages/stage33/33-12/verify_e3_v91c1l_a2_02_cech_to_marked_discriminant_dual_evaluation_contract.py
verifier_blob_sha=fa162fdd7d01ebc18f1179cb162f8c4a4240b5f8
```

Reusable workflow:

```text
literal source representative
+ locked marked quotient basis/order
+ independently defined comparison target
-> expand the missing quotient map into finitely many named source-derived evaluation obligations
-> require representative-change invariance for each evaluation
-> require descent through the intended quotient, e.g. Pic/2
-> require group-equivariance checks when the target is equivariant
-> compare with the target only after all source evaluations are in the same locked order
```

```text
HYPOTHESES=marked basis/order source-locked; every evaluation derived from the literal source; representative-change invariance checkable; quotient descent and equivariance conditions explicit
APPLICABILITY=marked finite-dimensional quotient/functionals where an abstract cohomological arrow must be replaced by explicit coordinate evaluations
DO_NOT_USE_FOR=the obligation contract as a computed evaluation vector; copying target bits into source data; positional labels as coordinates; zero localization as a marked quotient bit
```

The Stage33 instance required 14 bits, but the reusable workflow is finite-basis evaluation decomposition, not the number 14 or target mask20.

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
| `S33-WF01 FIRST_MISSING_WITNESS_TYPE_PROVENANCE_GATE` | localize the first unmaterialized typed edge and acceptable witness forms; fail-close downstream credit |
| `S33-WF02 MARKED_QUOTIENT_EVALUATION_OBLIGATION_DECOMPOSITION` | convert an abstract marked quotient gap into finite source-derived evaluation obligations |

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

Post-#1478 hostile dedup decisions:

- `DISC-S33-B02` fixed-subspace/naturality pruning is already represented by `S33-PW05` plus the Stage30 finite-equivariant parent.
- `DISC-S33-B03` literal Čech/Cartier semantics is already within `S33-PW07` when used as a Brauer/torsor representative validation step.
- `DISC-S33-B04` finite/localization-versus-absolute-H1 type separation is already represented by `S33-PW06` + `S33-PW08`.
- `DISC-S33-C04` equivariant reachability target pruning is already represented by `S33-PW05` + `S30-WF01`.
- bounded-search miss semantics remains Research OS/history, not a new Arsenal card.

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

Post-#1478 historical/negative exclusions additionally retain: abstract Kummer quotient is not a marked-coordinate computation; target-side Picard/discriminant adjoint is not a source H2-to-Br quotient binding; fixed-subspace membership is not unique marked identification; localization receiver/zero localization is not a geometric marked Brauer coordinate or automatic global lift; nonzero literal divisor difference is not a nonzero Pic/2 class without a source-bound adapter; bounded search miss is not repository absence or mathematical nonexistence; positional/dimension coincidence is not an adapter. These are anti-loop provenance, not current weapon IDs.

Stage33-specific data deliberately not promoted include the V25 J2 functions/labels/masks/projection, e3/mask20/fixed-subspace concrete numerics, and swap23 package/count/hash payloads.

## Final provisional boundary

```text
PROVISIONAL_WEAPONS=S33-PW01,S33-PW02,S33-PW04,S33-PW05,S33-PW06,S33-PW07,S33-PW08,S33-PW09,S33-PW10
PROVISIONAL_WORKFLOWS=S33-WF01,S33-WF02
EXTENDED_EXISTING_IDS=S33-PW04
RETIRED_MERGED_IDS=S33-PW03->S33-PW02
PROVISIONAL_WEAPON_COUNT=9
PROVISIONAL_WORKFLOW_COUNT=2
STAGE33_SPECIFIC_DATA_PROMOTED=false
REVOKED_CLAIMS_PROMOTED=false
ROUTEABLE_FOR_CANDIDATE_DISCOVERY=true
FORMAL_PROMOTION_ACTIVE=false
HOSTILE_AUDIT_REVIEW_REQUIRED_BEFORE_ANY_FORMAL_TREATMENT=true
FINAL_PROMOTION_REVIEW_REQUIRED_AT_STAGE33_CLOSE=true
STAGE33_PROGRESS_CHANGE=0
STAGE33_MAIN_AUTHORITY_CHANGE=false
STAGE33_12_CLOSURE_CHANGE=false
STAGE33_13_RELEASE_CHANGE=false
RECEIVER_CREDIT_CHANGE=false
THEOREM_CREDIT_CHANGE=false
ENDPOINT_CREDIT_CHANGE=false
PERFECT_CUBOID_CONCLUSION=NONE
```
