# Stage33 post-#1478 Arsenal harvest discovery ledger

Status: `DISCOVERY_ONLY_NOT_ARSENAL_PROMOTION`

This is a persistent discovery record for the Stage33 Arsenal Harvest 1 investigation. It preserves candidate methods, exact source locators, and anti-loop boundaries for later Harvest 2 / Harvest 3 deduplication. It is not an Arsenal registry entry, not a generated card source, and not Stage33 MAIN authority.

## Hard firewalls

The following are explicitly false for this artifact:

- `formal_promotion = false`
- `provisional_card_addition = false`
- `theorem_credit = false`
- `receiver_credit = false`
- `stage33_progress_increment = false`
- `stage33_main_authority_change = false`
- `perfect_cuboid_conclusion = false`
- `merge_authorization = false`

No new `PW` ID is assigned here. `docs/arsenal/index.json`, generated cards/catalog, Stage33 `MAIN-STATE.json`, and Stage33 controller are intentionally unchanged.

## Harvest bounds and comparison rule

- Harvest stage: `Stage33`
- Previous Arsenal integration: PR `#1478`
- Checkpoint merge commit: `b5b810be420eedc74cfa8074ae043d681598b412`
- Harvest 1 upper bound/current main observed during discovery: `a3c64f5704f3d1fd297e3b95377ba1938d277178`
- Exact comparison rule: `b5b810be420eedc74cfa8074ae043d681598b412 -> a3c64f5704f3d1fd297e3b95377ba1938d277178`
- GitHub compare status at persistence time: `ahead`, `ahead_by=1568`, `behind_by=0`, merge-base exactly the checkpoint merge commit.

The old Stage33 `SOURCE_HEAD` is not used as a git-ancestry premise. This ledger records the checkpoint merge -> Harvest 1 observed-main range only.

## Discovery procedure retained from Harvest 1

The discovery was path/authority-first rather than chronological-PR-first. The Stage33 clusters inspected were:

- `stages/stage33/33-05/**` — mainly retained arithmetic/HS-d2 scope used later as a type firewall; no independent new reusable weapon promoted here.
- `stages/stage33/33-07/**` — marked Brauer/discriminant target, localization receiver, residue invariant basis, raw order-4 Bockstein and connecting-map machinery used as source-locked dependencies.
- `stages/stage33/33-12/**` — principal post-checkpoint harvest cluster; genuine H2(mu2), Cech/Cartier/purity, marked-source binding, equivariance, localization preflights, evaluation contracts, and Pic/2 adapter firewalls.
- `stages/stage33/MAIN-START-HERE.md` and `stages/stage33/MAIN-STATE.json` — read only to preserve live credit boundaries; not modified by this harvest.

Relevant source PRs/heads inspected or used as exact provenance anchors:

- PR `#1488`, head `8672a500f65d96e23b420f0d37bc16e69f09081b`, merge `f13f5c72b40cca6d557144b9290081d9c79509c0`; key V25 construction commit `9a01ec5a5c87782e44f1bffe91cc85e89db25fa1` (`Stage33: reattach named J2 to genuine H2 mu2 lift`).
- PR `#1620`, merged head `75585168c54241591fb29c9271b64e1e95d1f1f6`, merge `e2103a2de367a0a6d0826b044b6bb83d24ad6f6f`; supporting provenance only, with no retroactive hostile-audit PASS claim.
- PR `#1634`, exact head `1c76c3164681f225c42905067ee0d7d6c4a17418`, merge `cf5389b857ee52225ed44543ff7ac8d05387583a`.
- PR `#1639`, exact head `86eae9776d15479310ff6843d38614cb03498e21`, merge `dbcff26c0267416caa4fdd0515293396d0f86887`.
- PR `#1646`, exact head `5471181a4decdc319cf3f00080d85da6d6e9fbb0`, merge `749e06f82a3ffa1e9cb4e831760244e9237f34a4`.
- PR `#1649`, exact head `a1640a60d8b29b5cd8e9106df293e4e2bb3cf62c`, merge `43f3f3b135a2f5664cb8cc736d6db0b37d7b79da`.
- PR `#1653`, exact head `d7750f80571a8da7f4edfee43924121efa5aa15a`, merge `7a608ee2511192af8e293d88f8a7117aa5ad19d9`.
- PR `#1661`, exact head `da521c5091f42f4e9f40d71a81f484f232b6a5d5`, merge `f6b1d047dfd238de80ed8f5c267609d01ea1a3bb`; the V91C1T artifact remains treated here by its own `EXACT_NONCREDIT` semantics, irrespective of merge provenance.

Discovery-local IDs below are not Arsenal IDs.

---

## A. probable NEW_WEAPON

### DISC-S33-A01 — SOURCE_FIRST_GENUINE_FULL_SURFACE_H2_MU2_KUMMER_BINDING

- Primary classification: `probable_NEW_WEAPON`
- Secondary classification: `probable_NEW_WORKFLOW`
- Reusable input: an independently named Brauer source; a concrete full-surface Cech `H^2(mu_2)` preimage; a locked marked Brauer coordinate for the named source; exact geometric pullback/naturality data when used.
- Reusable output: an exact source-to-lift binding in a marked Brauer coordinate system, after which downstream Kummer-cohomology calculations may be performed without relabelling an unrelated source.
- Hypotheses: source identity and marked coordinate are independently established; the Cech representative is a genuine full-surface lift; any pullback/projection used is source-locked; the historical/raw-H1 target is not silently revived.
- Failure boundary / DO_NOT_USE_FOR: an abstract Kummer exact sequence is not a marked-coordinate computation; another source's marked equality cannot be transferred by relabelling; J2-specific functions/masks/projection are not generic data.
- Why potentially reusable: the construction separates a broadly reusable proof pattern from source-specific arithmetic, and PR #1646 explicitly re-extracted this V25 method pattern as reusable while refusing direct source relabelling.
- Nearest existing Arsenal card: `S33-PW04` and `S33-PW07`.
- Suspected duplication/distinction: likely overlaps PW04's exact marked-source adapter and PW07's torsor/Brauer semantics, but V25 adds a strict source-first ordering and a genuine full-surface lift gate. Harvest 2 must decide new card vs extension.
- Source PR/head: `#1488` / `8672a500f65d96e23b420f0d37bc16e69f09081b`.
- Key source commit: `9a01ec5a5c87782e44f1bffe91cc85e89db25fa1`.
- Certificate: `stages/stage33/33-12/j2-genuine-h2-mu2-kummer-adapter-v25.json`.
- Certificate git blob: `ac34f0177e3f7427f74a1d798a99fc51afdf4e66`.
- Canonical SHA256: `d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c`.
- Producer: `stages/stage33/33-12/certify_j2_genuine_h2_mu2_kummer_adapter_v25.py`, blob `32404e98042b0a4cb035581fc7d9db67163eaec1`.
- Verifier: `stages/stage33/33-12/verify_j2_genuine_h2_mu2_kummer_adapter_v25.py`, blob `7e018259d5cc683015e2b03b118740dd2ac0c525`.
- Principal source locks: `j2-order4-swap-functional-source-v21.json` canonical `19c464602d6ad1b6c32b0b08c50a6bcc55b8e606642a5ae52e7f51fdc2f12366`; `j2-raw-h1-not-kummer-target-v24.json` canonical `9d104c7d4054b5d92f1df382654b152c30ca0be6ef267aa028fe8b9d78a4687d`; `j2-corrected-explicit-cech-mu2-lift.json` canonical `6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b`; `j2-full-surface-mu2-zero-defect-contract.json` canonical `55cd01cc8570cb759e7029ddef3b9dac764625a7cdd313c76fd694e37fd478ce`.

### DISC-S33-A02 — RESOLVED_PRIME_PURITY_CECH_CARTIER_FULL_SURFACE_SEED_ASSEMBLER

- Primary classification: `probable_NEW_WEAPON`
- Secondary classification: `probable_EXTEND_EXISTING` for `S33-PW07`.
- Reusable input: actual height-one prime attachments; resolution-exceptional residue data; exact prime-level group transport; function-level scalar-unit data.
- Reusable output: an off-boundary purity correction derived from literal divisor differences, prime-level Cech transitions, Cartier transition binding, and a literal full-surface Cech-Cartier seed.
- Hypotheses: codimension-one and resolution-exceptional residue audit is complete; prime-level transport is explicit; correction terms are derived from actual differences rather than assumed from equivariance.
- Failure boundary / DO_NOT_USE_FOR: does not compute a marked Brauer image, source-specific quotient coordinate, or genuine downstream Kummer column by itself.
- Why potentially reusable: it is a generic assembly discipline for turning resolved local packages into a full-surface cohomological seed while preserving literal purity data.
- Nearest existing Arsenal card: `S33-PW07`.
- Suspected duplication/distinction: PW07 already covers Brauer/torsor/Cech semantics; V91C1D may be a substantial extension rather than a separate card. Harvest 2 decides.
- Source PR/head: `#1634` / `1c76c3164681f225c42905067ee0d7d6c4a17418`.
- Certificate: `stages/stage33/33-12/e3-v91c1d-a2-02-purity-cech-cartier-assembly.json`.
- Certificate git blob at source head: `eea5f083039abf52483c4faebbce547ae6c450c5`.
- Canonical SHA256: `fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14`.
- Diagnostic selector: `stages/stage33/33-12/diagnose_e3_v91c1d_a2_02_v4_transition_selector.py`, source-head blob `158c89c1538d0d3da1e332b202197028540d8ab3`.
- Verifier: `stages/stage33/33-12/verify_e3_v91c1d_a2_02_purity_cech_cartier_assembly.py`.
- Principal source locks: `e3-v91c1a-a2-02-literal-boundary-seed-localization.json` canonical `7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403`; `e3-v91c1c-a2-02-strict-transform-prime-refinement.json` canonical `ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6`; `boundary-function-scalar-descent-certificate.json` canonical `e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b`; Stage33-11e prime Galois transport verifier/certificate chain canonical `1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426`.

---

## B. probable EXTEND_EXISTING

### DISC-S33-B01 — SOURCE_BOUND_MARKED_BRAUER_QUOTIENT_TYPE_PROVENANCE_FIREWALL

- Primary classification: `probable_EXTEND_EXISTING`.
- Nearest existing Arsenal card: `S33-PW04`.
- Reusable input: a literal full-surface `H^2(mu_2)` seed and a separately locked marked target basis.
- Reusable output: a fail-closed test for whether an actual source-specific `H^2(mu_2) -> Br[2]` marked quotient evaluation has been materialized.
- Hypotheses: source and target object types are explicit; target-side Picard/discriminant data are distinguished from the missing source quotient map.
- Failure boundary / DO_NOT_USE_FOR: do not use target-side Picard adjoints, dimensions, boundary positions, or another source's marked equality as the missing source quotient evaluation.
- Why potentially reusable: this is a general type/provenance obstruction for marked cohomological adapters.
- Suspected duplication/distinction: strong PW04 extension; probably not standalone unless Harvest 2 finds PW04 too narrow.
- Source PR/head: `#1646` / `5471181a4decdc319cf3f00080d85da6d6e9fbb0`.
- Certificate: `stages/stage33/33-12/e3-v91c1f-a2-02-source-bound-kummer-quotient-marking-obstruction.json`.
- Certificate source-head blob: `c9cb07f374d26d52e57e16dbc285892d414d9dd2`.
- Canonical SHA256: `4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273`.
- Verifier: `stages/stage33/33-12/verify_e3_v91c1f_a2_02_source_bound_kummer_quotient_marking_obstruction.py`, source-head blob `fe7bbd9306bc905853c21993ffb4ffa94aef8bb3`.
- Key locks: V25 canonical `d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c`; V91C1D canonical `fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14`; V91C1E canonical `5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f`; type-safe interface canonical `da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754`.

### DISC-S33-B02 — EQUIVARIANCE_FIXED_SUBSPACE_CONSTRAINT_NOT_IDENTIFICATION

- Primary classification: `probable_EXTEND_EXISTING`.
- Nearest existing Arsenal card: `S33-PW05`.
- Reusable input: an exact finite-group action on source data; a marked finite module on the target; naturality of the relevant quotient/map.
- Reusable output: a mathematically valid fixed-subspace/reachability constraint on possible target images.
- Hypotheses: source action and target representation are source-locked; naturality applies to the same object.
- Failure boundary / DO_NOT_USE_FOR: fixed-subspace membership is not a unique marked-coordinate identification; target fixedness of a desired vector does not prove that it is the source image.
- Why potentially reusable: converts equivariance into safe finite-module pruning without overclaiming identification.
- Suspected duplication/distinction: direct strengthening of PW05.
- Source PR/head: `#1649` / `a1640a60d8b29b5cd8e9106df293e4e2bb3cf62c`.
- Certificate: `stages/stage33/33-12/e3-v91c1g-a2-02-v4-naturality-fixed-subspace-preflight.json`.
- Certificate source-head blob: `2aa21e9d318fe47a2405e4899850dc046e3506bf`.
- Canonical SHA256: `2a176993614fac6f4b1555855794642702f3eeb055d710b8f04ac5097e9fb370`.
- Verifier: `stages/stage33/33-12/verify_e3_v91c1g_a2_02_v4_naturality_fixed_subspace_preflight.py`, source-head blob `c673ffdd4a633c251b6a9f94984d89546e159dcf`.
- Principal locks: `stages/stage33/33-07/proper-brauer2-from-discriminant.json` canonical `c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf`; V91C1D and V91C1F canonicals above.

### DISC-S33-B03 — LITERAL_CECH_CARTIER_SEMANTICS_FOR_TORSOR_BRAUER_ADAPTER

- Primary classification: `probable_EXTEND_EXISTING`.
- Nearest existing Arsenal card: `S33-PW07`.
- Reusable input/output: V25 source/lift binding discipline plus V91C1D literal full-surface Cech-Cartier assembly.
- Hypotheses: a named Brauer class/common cocycle is independently available when the full PW07 adapter is invoked.
- Failure boundary / DO_NOT_USE_FOR: the literal Cech seed alone does not name its marked Brauer quotient coordinate.
- Why potentially reusable: closes a semantic gap between literal cohomological representatives and torsor/Brauer adapters.
- Suspected duplication/distinction: likely extension, not a separate new weapon.
- Source locators: V25 and V91C1D records above; applicability classification source `stages/stage33/33-12/e3-v91c1k-a2-02-arsenal-applicability-matrix.json`, source-head blob `166fe5b38e8794cb5cbec847cff0c78a2bee4350`, canonical `16ccf10acd65fd7101acd6a776771896cd3e3e91aa3a2bd49dba43e0d6cd11b3`.
- Verifier: `stages/stage33/33-12/verify_e3_v91c1k_a2_02_arsenal_applicability_matrix.py`.

### DISC-S33-B04 — LOCALIZATION_CONNECTING_MAP_TYPE_SEPARATION

- Primary classification: `probable_EXTEND_EXISTING`.
- Nearest existing Arsenal card: `S33-PW08`.
- Reusable input: source-bound residue/receiver data, an exact connecting-map/localization construction, and the desired target object type.
- Reusable output: a typed separation between a finite/localization diagnostic and the actual source-bound extension or geometric marked quotient being sought.
- Hypotheses: receiver and coefficient module are explicit; finite-group H1 is not silently identified with absolute H1; the actual connecting map/evaluation is tracked separately.
- Failure boundary / DO_NOT_USE_FOR: a coordinate frame is not the connecting map; zero localization is not a marked geometric Brauer coordinate, not automatically geometric zero, and not automatically a global lift.
- Why potentially reusable: exact Gersten/localization calculations frequently fail by type collapse; this gives a reusable audit boundary.
- Suspected duplication/distinction: strong PW08 extension.
- Source PR/head: `#1653` / `d7750f80571a8da7f4edfee43924121efa5aa15a`.
- Certificate: `stages/stage33/33-12/e3-v91c1h-a2-02-stage33-07-localization-quotient-preflight.json`.
- Certificate source-head blob: `d99b7c381ad6ecef68f2a92d12f10db204f9a8cf`.
- Canonical SHA256: `d05672463ce6340773b6a4394851398360cf58b03f544ea4c00ff0d345089be2`.
- Verifier: `stages/stage33/33-12/verify_e3_v91c1h_a2_02_stage33_07_localization_quotient_preflight.py`.
- Principal source-lock locators: `stages/stage33/33-07/materialize_order2_localization_receiver.py` (producer blob locked by V91C1H as `886332f254789edeba6757191fb0ce5e20813a43`); `stages/stage33/33-07/certify_order2_quotient_raw_order4_bockstein.py`; `stages/stage33/33-07/two-primary-residue-invariant-basis.json` canonical `f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939`; proper Brauer target canonical `c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf`.

---

## C. probable NEW_WORKFLOW

### DISC-S33-C01 — FIRST_MISSING_WITNESS_TYPE_PROVENANCE_GATE

- Reusable input: a nearly complete source/target construction with one unmaterialized load-bearing adapter.
- Reusable output: an exact statement of the first missing witness plus an allowed witness-form list, while preserving all downstream credit as false.
- Hypotheses: existing assets are source-locked and their output types are known.
- Failure boundary / DO_NOT_USE_FOR: bounded search miss is not repository-wide absence or mathematical nonexistence.
- Why potentially reusable: prevents long proof chains from crossing an implicit adapter gap.
- Nearest existing Arsenal card: `S33-PW04`; may be a workflow extension rather than a new card.
- Source: V91C1E and V91C1F.
- V91C1E certificate: `stages/stage33/33-12/e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json`; blob at Harvest upper bound `3a2547188bb0c2aece74094fe93de5f89707e5c2`; canonical `5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f`; verifier `stages/stage33/33-12/verify_e3_v91c1e_a2_02_marked_brauer_image_adapter_preflight.py`.

### DISC-S33-C02 — MARKED_EVALUATION_OBLIGATION_CONTRACT

- Reusable input: a literal source cohomology representative, a locked marked quotient basis, and a target vector to compare only after computation.
- Reusable output: a finite list of source-derived marked evaluation obligations with basis order, representative-change invariance, Pic/2 descent, equivariance, and comparison gates made explicit.
- Hypotheses: every bit is computed from the source representative and is expressed in the same locked target order.
- Failure boundary / DO_NOT_USE_FOR: the contract is not the computed evaluation; target bits may not be copied into source data; zero localization may not be used as a marked bit.
- Why potentially reusable: turns an abstract quotient gap into deterministic finite proof obligations.
- Nearest existing Arsenal card: `S33-PW04`; possible workflow-card distinction unresolved.
- Source PR/head: `#1653` / `d7750f80571a8da7f4edfee43924121efa5aa15a`.
- Certificate: `stages/stage33/33-12/e3-v91c1l-a2-02-cech-to-marked-discriminant-dual-evaluation-contract.json`.
- Certificate source-head blob: `02eda1efe38c1cca42aa96c2139bcdd66bc5ec81`.
- Canonical SHA256: `6ae7e0464c2acd012c1c486e6a12fdb806d65049359c0c6c2440168be138e3dc`.
- Verifier: `stages/stage33/33-12/verify_e3_v91c1l_a2_02_cech_to_marked_discriminant_dual_evaluation_contract.py`.
- Principal locks: V89 dual bridge canonical `26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639`; V91 marked Picard dual canonical `729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9`; V91C1D and V91C1K canonicals above; type-safe interface canonical `da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754`.

### DISC-S33-C03 — LITERAL_DIVISOR_TO_PIC2_TYPE_FIREWALL

- Reusable input: an explicitly transported literal divisor/package difference and a candidate Picard/Pic/2 target.
- Reusable output: a hard gate requiring an actual source-bound divisor-to-Picard class adapter before reduction mod 2 or Pic/2 fixedness/nonzero conclusions.
- Hypotheses: actual strict-transform and exceptional attachments are tracked, not merely carrier labels.
- Failure boundary / DO_NOT_USE_FOR: nonzero literal divisor difference is not automatically a nonzero Pic/2 class; a retained inventory miss is not repository absence; a historical source-specific Pic/2 script cannot be relabelled.
- Why potentially reusable: separates divisor-level evidence from quotient-class evidence, a common proof failure mode.
- Nearest existing Arsenal card: no clean decision; potentially workflow or negative-ledger extension.
- Source PR/head: `#1661` / `da521c5091f42f4e9f40d71a81f484f232b6a5d5`.
- Certificate: `stages/stage33/33-12/e3-v91c1t-a2-02-swap23-pic2-adapter-preflight.json`.
- Certificate source-head blob: `1ba6a44f5ac98e8c231cb659512f0cd24e19475c`.
- Canonical SHA256: `6c064cf02fb7a0908242317bf7ac1b20b0586751b78e07b26d6c7889060ffdfa`.
- Verifier: `stages/stage33/33-12/verify_e3_v91c1t_a2_02_swap23_pic2_adapter_preflight.py`, source-head blob `491aaa810b8dbed33d8691730f32b59af6c441d6`.
- Source-lock locators: `audit_j2_current_v4_pic2_cocycle_v32.py`; `proper-brauer2-from-discriminant.json`; `e3-retained-at-marked-picard-dual-source-v91.json`; V91C1D seed; V91C1L evaluation contract; `diagnose_e3_v91c1s_swap23_prime_attached_cech_difference.py`.

### DISC-S33-C04 — EQUIVARIANT_REACHABILITY_TARGET_PRUNING

- Reusable input: exact finite-module actions and a source stabilizer/naturality statement.
- Reusable output: target candidate-space pruning and minimal discriminating coordinate selection, without source-coordinate promotion.
- Hypotheses: action matrices and stabilizer semantics refer to the same source object; seed-level transport is separately checked before using source-residue stabilizers as cohomology stabilizers.
- Failure boundary / DO_NOT_USE_FOR: a residue-source stabilizer is not automatically a full Cech/H2 seed stabilizer; target-moving words alone do not exclude a marked image.
- Why potentially reusable: supports efficient finite-state reachability and discriminator selection while preserving the source-binding gate.
- Nearest existing Arsenal card: `S33-PW05`.
- Source locators: V91C1G plus `diagnose_e3_v91c1m_joint_fixed_coordinate_discriminator.py`, `e3-v91c1n-minimal-joint-v4-fixed-coordinate-discriminator.json`, and V91C1O-S diagnostics under `stages/stage33/33-12/`.

### DISC-S33-C05 — BOUNDED_SEARCH_MISS_SEMANTICS

- Reusable input: an Arsenal-first search followed by a bounded, source-scoped repository search triggered by materially new mathematical information.
- Reusable output: a precise checked-scope miss that identifies the next construction interface.
- Hypotheses: search scope is recorded; new search repetitions require materially new signal; existing card/source locks are checked first.
- Failure boundary / DO_NOT_USE_FOR: never promote a bounded search miss to repository-wide absence or mathematical nonexistence.
- Why potentially reusable: preserves negative search results as actionable workflow evidence without poisoning mathematical claims.
- Nearest existing Arsenal relation: Research OS repository discovery policy plus the current Stage33 Arsenal-first routing discipline; classification as Arsenal workflow vs Research OS-only remains unresolved.
- Source: V91C1E bounded preflight, V91C1K applicability matrix, Stage33 current discovery policy at Harvest 1.

---

## D. STAGE33_SPECIFIC / not promotable as reusable mathematical output

### DISC-S33-D01 — J2-specific V25 payload

Do not Arsenal-promote the concrete J2 marking data by relabelling: corrected `J2=(f2,1)`, the `{f2,g22}` representative, named functional `beta1`, marked coordinate `[1,0]`, proper14 mask `25`, retained10 mask `6`, and the `forget c` projection are source-specific. Only the method pattern in DISC-S33-A01 is a reuse candidate.

### DISC-S33-D02 — e3/A2_02 target numerics and fixed-space counts

Do not promote the particular e3/A2_02/proper14 masks/supports, the 14D/10D fixed-space dimensions, cardinality 1024, or the particular source component labels as generic weapons. The reusable content is the fixed-space/naturality methodology and its identification firewall.

### DISC-S33-D03 — swap23 package counts

Do not promote the Stage33-specific swap23 counts, component list, strict/exceptional nonzero-coefficient counts, or mask movement as generic results. The reusable content is the literal-divisor-to-Pic/2 type boundary only.

---

## E. NEGATIVE_OR_HISTORICAL / anti-loop value only

The following are retained as anti-loop rules rather than positive weapons:

1. `S33-PW03` is `RETIRED`; never reuse or reassign it.
2. Historical named-J2 Kummer glue / revoked raw-H1 targets are not revived by V25.
3. Abstract `Pic/2 -> H^2(mu_2) -> Br[2]` does not itself compute a marked source coordinate.
4. Target-side Picard/discriminant adjoints do not substitute for a missing source-bound `H^2(mu_2) -> Br[2]` evaluation.
5. Equivariance or joint-fixed-space membership constrains but does not uniquely identify a marked image.
6. Localization receiver coordinates or zero localization do not equal a geometric marked Brauer coordinate and do not by themselves prove a global lift.
7. Nonzero literal divisor difference does not imply a nonzero Pic/2 class without a source-bound divisor-to-Picard adapter.
8. Bounded repository/Arsenal search miss does not prove repository absence or mathematical nonexistence; positional/dimension coincidence is not an adapter.

---

## F. unresolved classification for Harvest 2

1. Whether DISC-S33-A01 deserves a new standalone weapon card or should extend `S33-PW04`/`S33-PW07`.
2. Whether DISC-S33-A02 is sufficiently distinct from `S33-PW07` to become a new weapon rather than a substantial PW07 extension.
3. Whether DISC-S33-C02 should become a dedicated workflow card or remain a PW04 proof-obligation extension.
4. Whether DISC-S33-C03 belongs in a workflow card, an existing marked-source/Picard adapter card, or only the negative/historical ledger.

No deduplication decision is made in this file.

## Harvest 2 handoff contract

Harvest 2 should compare only these discovery candidates against the exact current bodies/source locks of the nearest Arsenal cards. It should not redo the checkpoint-to-main exploration unless a locator in this ledger is invalid. Promotion, formal ID assignment, registry edits, generated-card regeneration, or theorem/receiver credit must be separate explicit actions after deduplication.
