# Stage33 post-#1478 Arsenal harvest discovery and dedup ledger

Status: `DISCOVERY_DEDUP_COMPLETE_NOT_ARSENAL_PROMOTION`

This file is the persistent Stage33 Arsenal Harvest 1 discovery record plus the hostile Harvest 2 dedup/classification result. It is a handoff artifact only. It is not an Arsenal registry entry, not a generated card source, and not Stage33 MAIN authority.

## Hard firewalls

The following remain explicitly false:

- `formal_promotion = false`
- `provisional_card_addition = false`
- `theorem_credit = false`
- `receiver_credit = false`
- `stage33_progress_increment = false`
- `stage33_main_authority_change = false`
- `perfect_cuboid_conclusion = false`
- `merge_authorization = false`
- `new_pw_id_assignment = false`

`docs/arsenal/index.json`, generated cards/catalog, `docs/stage33-arsenal-promotion.md`, Stage33 `MAIN-STATE.json`, and Stage33 controller are intentionally unchanged in Harvest 2.

## Frozen harvest range

- Harvest stage: `Stage33`
- Previous Arsenal integration: PR `#1478`
- Checkpoint merge commit: `b5b810be420eedc74cfa8074ae043d681598b412`
- Harvest 1 upper bound: `a3c64f5704f3d1fd297e3b95377ba1938d277178`
- Exact comparison rule: `b5b810be420eedc74cfa8074ae043d681598b412 -> a3c64f5704f3d1fd297e3b95377ba1938d277178`
- Compare at persistence: `ahead_by=1568`, `behind_by=0`, merge-base exactly the checkpoint merge commit.

Harvest 2 does not expand this range. Main commits after `a3c64f5704f3d1fd297e3b95377ba1938d277178` are explicitly out of scope for this dedup pass.

The old Stage33 `SOURCE_HEAD` is not used as a git-ancestry premise.

## Harvest 1 provenance retained

Inspected Stage33 clusters:

- `stages/stage33/33-05/**`
- `stages/stage33/33-07/**`
- `stages/stage33/33-12/**`
- `stages/stage33/MAIN-START-HERE.md`
- `stages/stage33/MAIN-STATE.json`

Source PR/head anchors retained from Harvest 1:

- `#1488`, head `8672a500f65d96e23b420f0d37bc16e69f09081b`, merge `f13f5c72b40cca6d557144b9290081d9c79509c0`, key V25 commit `9a01ec5a5c87782e44f1bffe91cc85e89db25fa1`.
- `#1620`, head `75585168c54241591fb29c9271b64e1e95d1f1f6`, merge `e2103a2de367a0a6d0826b044b6bb83d24ad6f6f`; supporting provenance only, no retroactive hostile-audit PASS claim.
- `#1634`, exact head `1c76c3164681f225c42905067ee0d7d6c4a17418`, merge `cf5389b857ee52225ed44543ff7ac8d05387583a`.
- `#1639`, exact head `86eae9776d15479310ff6843d38614cb03498e21`, merge `dbcff26c0267416caa4fdd0515293396d0f86887`.
- `#1646`, exact head `5471181a4decdc319cf3f00080d85da6d6e9fbb0`, merge `749e06f82a3ffa1e9cb4e831760244e9237f34a4`.
- `#1649`, exact head `a1640a60d8b29b5cd8e9106df293e4e2bb3cf62c`, merge `43f3f3b135a2f5664cb8cc736d6db0b37d7b79da`.
- `#1653`, exact head `d7750f80571a8da7f4edfee43924121efa5aa15a`, merge `7a608ee2511192af8e293d88f8a7117aa5ad19d9`.
- `#1661`, exact head `da521c5091f42f4e9f40d71a81f484f232b6a5d5`, merge `f6b1d047dfd238de80ed8f5c267609d01ea1a3bb`; V91C1T remains governed by its own `EXACT_NONCREDIT` semantics in this frozen range.

## Harvest 2 hostile comparison basis

Every candidate was compared by source/target object, field, coefficient/module type, quantifiers, marked/unmarked semantics, hypotheses, exact output, source-lock requirements, verification contract, semantic credit boundary, and failure mode.

Exact current-at-upper-bound Stage33 cards inspected:

- `S33-PW01` blob `c096c1c9bb7722518aebe4edbc98eedda9d07d7a`
- `S33-PW02` blob `f2c6dbc96ad064e737953f1667b4349261d2ef50`
- `S33-PW04` blob `1702de010168d91d587bb6fb0966358c76e6e505`
- `S33-PW05` blob `8104a6523dc882b0e2e74828dc214d15894457e6`
- `S33-PW06` blob `f8ac91412293989ee1f8397601f3a5d261100484`
- `S33-PW07` blob `7f1337858bc6f9006e101d810dd72e67aef534fd`
- `S33-PW08` blob `c9e13a917811581578f833ea93619d85f717be6d`
- retired `S33-PW03` blob `a6dad075f7a7f8c6b2c8300c2178b972e2314ef7`; ID reuse forbidden.

Formal cross-Stage comparison included Stage30 (`S30-W01/W02/W03`, `S30-WF01/WF02/WF03`), Stage31 (`S31-W01/W02/W03`, `S31-WF01`), and Stage34 (`S34-W01/W02/W03`, `S34-WF01`). Stage31 and Stage34 cards have curve/integral/Mordell-Weil/receiver inputs and outputs that do not match the Stage33 cohomological candidate types. Stage30 is the only substantive cross-Stage overlap: finite equivariant identification and generic credit/certificate firewalls.

The canonical repository discovery policy was also checked. `docs/research-os/policies/repository-asset-discovery.md`, blob `bf001d4ff4375281a901d52c147c35c28643b8a3`, already owns bounded-search miss semantics.

---

# Harvest 2 final classification

Classification is complete for the frozen Harvest 1 candidate set. Discovery-local IDs below are not Arsenal IDs.

## A. NEW_WEAPON

### DISC-S33-A01 — proposed role `MARKED_KUMMER_LIFT_BINDING_ADAPTER`

**Classification:** `NEW_WEAPON`  
**Maturity if promoted later:** `PROVISIONAL`

**Reusable contract**

```text
independently named Br[2] source
+ genuine full-surface H^2_et(mu_2) representative/lift
+ locked marked Br[2] coordinate for the named source
+ exact pullback/projection/naturality when used
-> verify that the H^2(mu_2) lift maps to that same named Br[2] source
-> expose a source-bound marked Kummer lift for downstream cohomology
```

**Input type:** named geometric Brauer 2-torsion class plus literal full-surface `H^2_et(mu_2)` representative and marked Brauer coordinate.  
**Output type:** source-bound marked Kummer lift binding; not a Kummer column, not arithmetic `H^1`, not Stage33 closure.

**HYPOTHESES:** source identity independently fixed; marked coordinate independently fixed; representative is a genuine full-surface lift; any pullback/projection is exact and source-locked; revoked/raw-H1 targets are excluded.

**APPLICABILITY:** marked Kummer-sequence work where a concrete cohomological lift exists but semantic identity with a named Brauer source must be proved before downstream transport.

**DO_NOT_USE_FOR:** abstract Kummer exact-sequence surjectivity as a marked-coordinate computation; relabelling another source's equality; raw finite `H^1` as the Kummer boundary; copying J2 functions, masks, or projection to a new source.

**Nearest existing cards:** `S33-PW04`, `S33-PW07`.

**Why distinct:** `S33-PW04` transports/orients marked coordinates across Picard/dual/discriminant/Brauer implementations; it does not own the `H^2_et(mu_2) -> Br[2]` source/lift binding. `S33-PW07` starts from a Brauer representative/class and validates cocycle/torsor/literal-representative semantics; it does not certify that a given full-surface Kummer lift is the same independently named marked Brauer source. The A01 output is the missing typed bridge between those interfaces.

**Authoritative source locator:**

- source PR `#1488`, exact head `8672a500f65d96e23b420f0d37bc16e69f09081b`
- key construction commit `9a01ec5a5c87782e44f1bffe91cc85e89db25fa1`
- certificate `stages/stage33/33-12/j2-genuine-h2-mu2-kummer-adapter-v25.json`
- certificate blob `ac34f0177e3f7427f74a1d798a99fc51afdf4e66`
- canonical SHA256 `d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c`
- producer `stages/stage33/33-12/certify_j2_genuine_h2_mu2_kummer_adapter_v25.py`, blob `32404e98042b0a4cb035581fc7d9db67163eaec1`
- verifier `stages/stage33/33-12/verify_j2_genuine_h2_mu2_kummer_adapter_v25.py`, blob `7e018259d5cc683015e2b03b118740dd2ac0c525`
- principal source-lock canonicals: V21 named source `19c464602d6ad1b6c32b0b08c50a6bcc55b8e606642a5ae52e7f51fdc2f12366`; V24 raw-H1 firewall `9d104c7d4054b5d92f1df382654b152c30ca0be6ef267aa028fe8b9d78a4687d`; explicit Cech lift `6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b`; surface boundary contract `55cd01cc8570cb759e7029ddef3b9dac764625a7cdd313c76fd694e37fd478ce`.

J2-specific payload remains quarantined under D01 below.

### DISC-S33-A02 — proposed role `RESOLVED_PURITY_CECH_CARTIER_SEED_ASSEMBLER`

**Classification:** `NEW_WEAPON`  
**Maturity if promoted later:** `PROVISIONAL`

**Reusable contract**

```text
actual height-one prime attachments
+ resolution-exceptional residue package
+ exact prime-level group transport
+ function-level scalar/unit data
-> derive, rather than assume, off-boundary purity correction
-> materialize prime-level Cech transitions
-> bind Cartier transition/correction
-> output a literal full-surface Cech-Cartier cohomological seed
```

**Input type:** resolved codimension-one/exceptional residue data with exact action and scalar transport.  
**Output type:** literal full-surface Cech-Cartier seed with audited purity correction; no marked Brauer coordinate and no localization column.

**HYPOTHESES:** codimension-one and exceptional residue audit complete; actual height-one prime attachment complete; prime-level transport explicit; scalar units source-locked; correction derived from literal differences.

**APPLICABILITY:** surface/cohomology calculations where local residue packages must be assembled into a genuine resolved full-surface representative before marked quotient or arithmetic localization work.

**DO_NOT_USE_FOR:** marked Brauer image; source-specific `H^2(mu_2)->Br[2]` quotient coordinate; Kummer column; assuming zero correction from equivariance alone.

**Nearest existing cards:** `S33-PW07`, `S33-PW08`.

**Why distinct:** PW07 validates literal representative/divisor/Cartier semantics after a Brauer-class interface is available. PW08 consumes explicit Gersten/residue data and continues through `g(L)-L` to absolute-`H^1` localization columns. A02 has a different stopping object: the resolved full-surface Cech-Cartier seed itself, which can feed A01 or other downstream constructions without committing to torsor semantics or arithmetic localization.

**Authoritative source locator:**

- source PR `#1634`, exact head `1c76c3164681f225c42905067ee0d7d6c4a17418`
- certificate `stages/stage33/33-12/e3-v91c1d-a2-02-purity-cech-cartier-assembly.json`
- certificate blob `eea5f083039abf52483c4faebbce547ae6c450c5`
- canonical SHA256 `fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14`
- selector `stages/stage33/33-12/diagnose_e3_v91c1d_a2_02_v4_transition_selector.py`, source-head blob `158c89c1538d0d3da1e332b202197028540d8ab3`
- verifier `stages/stage33/33-12/verify_e3_v91c1d_a2_02_purity_cech_cartier_assembly.py`, frozen-upper-bound blob `21827a085c0f3039ab3cd6786483de4bb13d5db9`
- principal source-lock canonicals: V91C1A `7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403`; V91C1C `ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6`; scalar descent `e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b`; Stage33-11e prime transport `1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426`.

The concrete eight-component A2_02 package and zero corrections are source-instance provenance, not the reusable theorem statement.

## B. EXTEND_EXISTING

### DISC-S33-B01 — extend `S33-PW04 EXACT_MARKED_SOURCE_ADAPTER`

**Classification:** `EXTEND_EXISTING`  
**Existing ID retained:** `S33-PW04`  
**Maturity:** `PROVISIONAL`

**Proposed extension role:** `SOURCE_BOUND_MARKED_QUOTIENT_BINDING_REQUIREMENT`.

**Reusable contract extension:** when the source object is a literal `H^2(mu_2)` representative and the target is a marked `Br[2]` basis, PW04 must require an actual source-bound quotient evaluation/adapter. A target-side Picard/discriminant adjoint is not that map.

**HYPOTHESES added:** source and target object types explicit; marked basis order locked; actual source quotient witness source-locked.

**Accepted witness forms:** direct Cech/symbol/corestriction pairing in the locked basis; exact geometric quotient/pullback adapter to an independently named class already in the basis; or source-bound Kummer extension/section data computing the quotient image.

**DO_NOT_USE_FOR added:** target-side adjoint as source quotient; dimension/rank/boundary-position coincidence; another source's marked equality; positional identification.

**Why extension, not new card:** the intended output remains the PW04 output—an exact semantically oriented marked source coordinate. V91C1F sharpens the required source-lock and failure contract rather than defining a different downstream object.

**Authoritative source locator:** PR `#1646`, exact head `5471181a4decdc319cf3f00080d85da6d6e9fbb0`; certificate `stages/stage33/33-12/e3-v91c1f-a2-02-source-bound-kummer-quotient-marking-obstruction.json`, blob `c9cb07f374d26d52e57e16dbc285892d414d9dd2`, canonical SHA256 `4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273`; verifier `stages/stage33/33-12/verify_e3_v91c1f_a2_02_source_bound_kummer_quotient_marking_obstruction.py`, source-head blob `fe7bbd9306bc905853c21993ffb4ffa94aef8bb3`.

## C. NEW_WORKFLOW

### DISC-S33-C01 — proposed workflow `FIRST_MISSING_WITNESS_TYPE_PROVENANCE_GATE`

**Classification:** `NEW_WORKFLOW`  
**Maturity if promoted later:** `PROVISIONAL`

**Reusable procedure**

```text
freeze all already-materialized typed interfaces
-> identify the first load-bearing source->target witness that is still absent
-> state exact source and target types
-> enumerate admissible witness forms
-> prove downstream credit remains false until one is materialized
-> treat bounded search miss only as a checked-scope miss
```

**Input type:** a nearly complete proof/adapter chain with explicit source locks and one missing typed edge.  
**Output type:** a deterministic first-missing-witness contract and allowable construction routes; no mathematical value for the missing edge itself.

**HYPOTHESES:** prior interfaces source-locked; output types known; bounded search scope explicit.

**APPLICABILITY:** long adapter/cohomology/certificate chains where repeated work is caused by silently substituting a nearby object for the actual missing witness.

**DO_NOT_USE_FOR:** search miss as repository absence or mathematical nonexistence; target-side surrogate as the missing source edge; workflow PASS as theorem/receiver credit.

**Nearest existing cards/workflows:** `S33-PW04`, `S30-WF03`.

**Why distinct:** S30-WF03 governs upward credit; PW04 defines a successful marked adapter. C01's output is instead the smallest unresolved typed edge plus accepted witness species, which is a constructive proof-search/audit procedure.

**Authoritative sources:**

- PR `#1639`, head `86eae9776d15479310ff6843d38614cb03498e21`: `stages/stage33/33-12/e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json`, blob `3a2547188bb0c2aece74094fe93de5f89707e5c2`, canonical `5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f`; verifier `verify_e3_v91c1e_a2_02_marked_brauer_image_adapter_preflight.py`, frozen-upper-bound blob `f770b270787955db61551714d68b7e2705b45588`.
- PR `#1646`, head `5471181a4decdc319cf3f00080d85da6d6e9fbb0`: V91C1F obstruction certificate canonical `4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273` supplies the accepted witness forms.

### DISC-S33-C02 — proposed workflow `MARKED_QUOTIENT_EVALUATION_OBLIGATION_DECOMPOSITION`

**Classification:** `NEW_WORKFLOW`  
**Maturity if promoted later:** `PROVISIONAL`

**Reusable procedure**

```text
literal source representative
+ locked marked quotient/test basis
-> freeze basis order
-> derive one source evaluation obligation per basis direction
-> require representative-change invariance
-> require descent through the intended quotient (e.g. Pic/2)
-> require group-equivariance compatibility
-> compare with any target vector only after every source bit is independently computed
```

**Input type:** literal cohomological/source representative plus locked marked quotient basis.  
**Output type:** finite source-derived evaluation obligations; not the computed evaluation vector.

**HYPOTHESES:** every coordinate derived from source data; basis order source-locked; representative invariance and quotient descent checked; comparison target kept separate.

**APPLICABILITY:** marked quotient/functionals where an abstract quotient map is known but explicit marked coordinates are missing.

**DO_NOT_USE_FOR:** contract as a computed vector; copying target bits into source evaluations; using zero localization as a marked bit; positional label matching.

**Nearest existing card:** `S33-PW04`.

**Why distinct:** PW04 specifies the successful marked adapter. C02 is a reusable decomposition/audit workflow for constructing that adapter coordinate-by-coordinate without pretending the obligations have already been discharged.

**Authoritative source locator:** PR `#1653`, exact head `d7750f80571a8da7f4edfee43924121efa5aa15a`; certificate `stages/stage33/33-12/e3-v91c1l-a2-02-cech-to-marked-discriminant-dual-evaluation-contract.json`, blob `02eda1efe38c1cca42aa96c2139bcdd66bc5ec81`, canonical SHA256 `6ae7e0464c2acd012c1c486e6a12fdb806d65049359c0c6c2440168be138e3dc`; verifier `stages/stage33/33-12/verify_e3_v91c1l_a2_02_cech_to_marked_discriminant_dual_evaluation_contract.py`, frozen-upper-bound blob `fa162fdd7d01ebc18f1179cb162f8c4a4240b5f8`.

The source certificate itself materializes zero evaluation bits and is noncredit; only the workflow contract is the candidate.

## D. HISTORICAL_OR_NEGATIVE

These are retained for anti-loop/search value, not promoted as weapons in Harvest 3.

- `DISC-S33-C03 LITERAL_DIVISOR_TO_PIC2_TYPE_FIREWALL`: a nonzero literal divisor/package difference does not imply a nonzero `Pic/2` class without a source-bound divisor-to-Picard adapter. Source: PR `#1661`, `e3-v91c1t-a2-02-swap23-pic2-adapter-preflight.json`, blob `1ba6a44f5ac98e8c231cb659512f0cd24e19475c`, canonical `6c064cf02fb7a0908242317bf7ac1b20b0586751b78e07b26d6c7889060ffdfa`. Keep as negative because the positive adapter was not materialized in the frozen range.
- `DISC-S33-C05 BOUNDED_SEARCH_MISS_SEMANTICS`: useful anti-loop rule, but canonical ownership already belongs to `docs/research-os/policies/repository-asset-discovery.md`; no Arsenal card should duplicate it.
- `DISC-S33-E01`: `S33-PW03` is RETIRED; successor `S33-PW02`; ID reuse forbidden.
- `DISC-S33-E02`: historical named-J2 Kummer glue and revoked raw-H1 target are not revived.
- `DISC-S33-E03`: an abstract Kummer quotient arrow is not a marked-coordinate computation.
- `DISC-S33-E04`: a target-side Picard/discriminant adjoint is not a source `H^2(mu_2)->Br[2]` quotient binding.
- `DISC-S33-E05`: fixed-subspace membership is not unique marked-coordinate identification.
- `DISC-S33-E06`: a localization receiver or zero localization is not a geometric marked Brauer coordinate and is not an automatic global lift.
- `DISC-S33-E07`: a nonzero literal divisor difference is not a nonzero `Pic/2` class without a source-bound adapter.
- `DISC-S33-E08`: bounded search miss is not repository absence or mathematical nonexistence; positional/dimension coincidence is not an adapter.

C03/E07 and C05/E08 intentionally remain redundant historical traces at the source-instance and generic anti-loop levels. Harvest 3 should not create duplicate cards for them.

## E. STAGE33_SPECIFIC

- `DISC-S33-D01 J2_SPECIFIC_V25_PAYLOAD`: `J2=(f2,1)`, `{f2,g22}`, `beta1`, marked coordinate `[1,0]`, proper14 mask `25`, retained10 mask `6`, and `forget c` projection. Only A01's method contract is reusable.
- `DISC-S33-D02 E3_A2_02_TARGET_NUMERICS_AND_FIXED_SPACE_COUNTS`: e3/mask20, proper14/fixed-subspace dimensions/cardinality and concrete A2_02 target numerics. Only the generic action/constraint methodology is reusable.
- `DISC-S33-D03 SWAP23_PACKAGE_COUNTS`: exact swap23 component counts, strict/exceptional package hashes, carrier-image inventory misses, and concrete masks. Only the C03 type firewall survives as negative history.

## F. REJECT_DUPLICATE

### DISC-S33-B02 — `EQUIVARIANCE_FIXED_SUBSPACE_CONSTRAINT_NOT_IDENTIFICATION`

**Classification:** `REJECT_DUPLICATE`  
**Duplicate target:** `S33-PW05`, with formal parent `S30-W01` / workflow `S30-WF01`.

Reason: PW05 already takes explicit source/target module actions and computes compatible intertwiners/extensions and reachable image, while explicitly forbidding a positive finite diagnostic from becoming semantic identification. Naturality-induced joint fixed-subspace pruning is a concrete implementation of that existing reachable-image contract, not a new interface.

Source instance retained for provenance: PR `#1649`; `e3-v91c1g-a2-02-v4-naturality-fixed-subspace-preflight.json`, blob `2aa21e9d318fe47a2405e4899850dc046e3506bf`, canonical `2a176993614fac6f4b1555855794642702f3eeb055d710b8f04ac5097e9fb370`.

### DISC-S33-B03 — `LITERAL_CECH_CARTIER_SEMANTICS_FOR_TORSOR_BRAUER_ADAPTER`

**Classification:** `REJECT_DUPLICATE`  
**Duplicate target:** `S33-PW07`.

Reason: PW07 already explicitly requires the actual transition function/divisor/Cartier data for literal representatives and exact Picard transport. Combining V25/A02 as a PW07 use case adds no independent PW07 input/output contract. The genuinely distinct pieces are already separated as A01 and A02.

### DISC-S33-B04 — `LOCALIZATION_CONNECTING_MAP_TYPE_SEPARATION`

**Classification:** `REJECT_DUPLICATE`  
**Duplicate targets:** `S33-PW06` + `S33-PW08`.

Reason: PW06 already forbids identifying finite quotient `H^1` with absolute arithmetic `H^1`; PW08 already requires actual source-bound localization columns in the locked absolute receiver and forbids dimension-only/project-independent zero or global-lift inference. The V91C1H preflight is a useful Stage33 instance of those exact existing firewalls, not a new Arsenal contract.

Source provenance remains `stages/stage33/33-12/e3-v91c1h-a2-02-stage33-07-localization-quotient-preflight.json`, canonical `d05672463ce6340773b6a4394851398360cf58b03f544ea4c00ff0d345089be2`.

### DISC-S33-C04 — `EQUIVARIANT_REACHABILITY_TARGET_PRUNING`

**Classification:** `REJECT_DUPLICATE`  
**Duplicate targets:** `S33-PW05` + `S30-WF01`.

Reason: exact finite-module reachability/candidate pruning and finite relabeling diagnostics are already the PW05/S30-WF01 contract. Choosing a small discriminating coordinate after pruning is a proof-planning tactic inside that contract, not a separate reusable mathematical/workflow output.

---

## Final Harvest 2 census

```text
TOTAL_CLASSIFICATION_UNITS = 22
NEW_WEAPON = 2
EXTEND_EXISTING = 1
NEW_WORKFLOW = 2
HISTORICAL_OR_NEGATIVE = 10
STAGE33_SPECIFIC = 3
REJECT_DUPLICATE = 4
NEW_ID_REQUIRED_IF_HARVEST3_PROMOTES = 4
EXISTING_ID_STRENGTHENINGS = 1
REJECTED_OR_NEGATIVE = 14
```

No PW/WF ID is assigned in this file.

# Harvest 3 human-readable handoff

Harvest 3 should implement only the completed classification above; it should not redo discovery or dedup unless a frozen locator is invalid.

Exact intended changes:

1. Amend `docs/stage33-arsenal-promotion.md` with two new **provisional source sections** corresponding to A01 and A02. Assign stable IDs only in Harvest 3 after checking the registry naming/collection convention.
2. Extend the existing `S33-PW04` authoritative source section with B01's source-bound `H^2(mu_2)->Br[2]` quotient requirement, accepted witness forms, and new DO_NOT_USE cases. Keep ID `S33-PW04`.
3. Add two **provisional workflow source sections** for C01 and C02. Do not coerce them into mathematical weapon semantics. If the current registry has no provisional-workflow collection, Harvest 3 must make the smallest schema-consistent registry change rather than misclassifying them.
4. Update `docs/arsenal/index.json` only in Harvest 3: register the two new weapons and two workflows, update PW04 metadata/source relation as needed, and optionally add this dedup ledger as one `HISTORICAL` support record. Do not register D/E/F items as weapons.
5. Run `python3 -B docs/arsenal/sync_arsenal_catalog.py` and `python3 -B docs/arsenal/sync_arsenal_catalog.py --check`; generated catalog/cards may change only as a consequence of Harvest 3 registry/source edits.
6. Preserve `S33-PW03` as RETIRED with no ID reuse.
7. Preserve all credit firewalls: no Stage33 MAIN progress/authority change, theorem/receiver/endpoint credit, or perfect-cuboid conclusion follows from Arsenal promotion.
8. Before any Harvest 3 promotion commit, revalidate only the exact listed source paths/blobs/canonical hashes needed by the four new-ID candidates and the PW04 extension. Do not expand the mathematical harvest range beyond the frozen upper bound for this batch.

Machine-readable Harvest 3 handoff is in `docs/arsenal/stage33-post1478-discovery.json` under `harvest3_handoff`.
