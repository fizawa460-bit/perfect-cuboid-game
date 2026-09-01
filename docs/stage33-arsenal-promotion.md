# Stage33 arsenal promotion — provisional harvest

```text
REGISTRY=STAGE33-ARSENAL-PROVISIONAL-R02
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage33
SOURCE_PR=1476
SOURCE_BRANCH=stage33-post1475-j2-v4-generator-adapter
SOURCE_HEAD=fd0352c05675742ffed2800ab47354e4307494e0
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
THEOREM_CREDIT=false
```

This file harvests reusable Stage33 mathematics and exact adapters before Stage33 closes. These cards are for candidate discovery and source lookup only until a final promotion audit. Stage33 has had hostile reopenings, so every card states explicitly which part survived and which promotion is forbidden.

## Targeted harvest R02 — Picard / Kummer / finite-module / coordinate-adapter band

This pass was reverse-indexed from the compact Stage33 state and closed/retained evidence. It did **not** reread Stage33 history sequentially. Source snapshot:

```text
source_head=fd0352c05675742ffed2800ab47354e4307494e0
compact_state=stages/stage33/MAIN-STATE.json
compact_state_canonical_sha256=32baebf358ae47b99a5a1ffd40dc90e7eb090db353f58861702bba3f0db0a9fc
scope=Picard marking; Pic/2; Kummer interfaces; V4 actions; Smith/finite modules; source-target coordinate transport; adjoint/basis adapters; exact finite linear algebra
```

### Classification and integration decision

| Harvest object | Class | Arsenal disposition | Exact source / SHA | Applicability | DO_NOT_USE_FOR |
|---|---|---|---|---|---|
| Exact finite-module source/target adapter with locked bases, group actions, and reachability/intertwining checks | **1. Arsenal candidate** | **Integrate into S33-PW05**; no new PW number | `stages/stage33/33-12/j2-picard-adjoint-proper-br2.json` / canonical `066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8`; `stages/stage33/33-12/full-surface-pic2-kummer-target.json` / canonical `384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890`; `stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json` / canonical `463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229` | Independently computed finite source/target coordinate systems must be joined and both module actions are explicit. Require basis hashes, coordinate conventions, exact finite arithmetic, and an exhaustive compatibility/reachability check. | A dimension match; a plausible label match; arbitrary generator relabeling; an absolute arithmetic-H1 identification; or a proof of the currently missing J2 binding. |
| Smith/invariant-factor reduction with mutually inverse integral coordinate maps | **1. Arsenal candidate, already present** | **Keep in S33-PW02**; do not split out a duplicate card | `stages/stage33/33-07/result.md` at source head above; invariant-basis SHA256 `f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939` | Exact finite abelian presentations where a unimodular Smith decomposition is retained together with forward/inverse coordinate maps and invariant factors. | Producing a global Q-defined lift; identifying an extension/Bockstein; treating quotient order two as raw order two; discarding nontrivial extension data. |
| Picard-adjoint / dual-basis -> proper-Br2 coordinate adapter | **1. Arsenal candidate, already present** | **Keep in S33-PW04**; enrich its adapter contract rather than create another card | `stages/stage33/33-12/j2-picard-adjoint-proper-br2.json` / canonical `066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8` | A Picard marking, dual/adjoint pairing, proper target basis and retained invariant basis are all explicit and source-locked. Preserve matrix direction and basis identities. | Copying `A_T[2]` coefficients into the proper dual basis; binding to a Kummer H1 target; generalizing the numerical J2 coordinate to another K3/marking. |
| Exact Smith/HNF/quotient finite-linear-algebra execution recipe | **2. Workflow candidate** | Record as workflow under PW02/PW05; not an independent theorem weapon | Same Stage33-07 retained Smith evidence plus the Stage33-12 compatibility certificates above | Build integer/F2 relation matrices exactly; compute canonical quotient/invariant bases; retain unimodular or row-reduction transforms; prove forward/inverse round trips; reduce actions in the same basis. | Claiming new arithmetic content merely from normal-form computation or silently changing quotient representatives/bases. |
| Basis/adjoint adapter audit | **2. Workflow candidate** | Fold into PW04 usage protocol | `j2-picard-adjoint-proper-br2.json`, canonical `066e6b...cb9f8` | Hash every source and target basis, state row/column convention, check the defining pairing/adjoint identity, and validate the resulting coordinate by a round trip or independent invariant projection. | Reusing coordinates after a marking/basis hash changes, or transposing a matrix by convention without checking the pairing. |
| V4 action / source-target transport audit | **2. Workflow candidate** | Fold into PW05 usage protocol | `full-surface-pic2-kummer-target.json`, canonical `384b7c...9890`; compatibility audit, canonical `463aae...58229` | Explicit generator matrices/actions on both finite modules. Test the transport against the group action and compute the reachable cohomology image before accepting a named relation. | Treating generator names as semantics; accepting a coordinate equation that fails equivariance; replacing the exhaustive compatibility test by dimension counting. |
| Marked Kc Picard basis and concrete J2 proper14/retained10 coordinates | **3. Stage33-specific — no promotion** | Provenance only; PW04 carries only the adapter pattern | `j2-picard-adjoint-proper-br2.json`, canonical `066e6b...cb9f8` | Only the locked cuboid K3 marking/bases. | Any other K3, any changed marking, or a universal Picard/Br2 coordinate theorem. |
| Concrete full-surface Pic/2 basis, 75D finite-V4 H1 basis, and locked V4 matrices/actions | **3. Stage33-specific — no promotion** | Provenance/input to PW05 only | `full-surface-pic2-kummer-target.json`, canonical `384b7c...9890` | Only the exact locked Stage33 Pic/2 module/action. | Reusing the 75D basis or action matrices as a generic Kummer module. |
| Named J2 target, semantic `u1`, weight-15 coordinate, and locked reachable-H1 dimension 13 | **3. Stage33-specific — no promotion** | Keep as hostile-audit evidence, not a reusable theorem | `stages/stage33/MAIN-STATE.json`, canonical `32baebf...a9fc`; target certificate `j2-named-v4-h1-target-before-source-orientation.json`, canonical `4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3`; compatibility audit canonical `463aae...58229` | Locked J2 repair only. | General statements about Kummer images, V4 H1 dimensions, or existence of a replacement binding. |
| Project-specific counts `29 -> 26`, `(Z/2)^23 + (Z/4)^3`, proper14/fixed10, and related concrete bases | **3. Stage33-specific — no promotion** | Keep as examples/provenance inside PW02, not generic claims | `stages/stage33/33-07/result.md` at source head; invariant-basis SHA256 `f18a5471...faa939` | The retained Stage33 residue presentation only. | Transferring the numerical ranks/invariant factors to another residue complex. |

### Reusable contract distilled from the targeted pass

The reusable part is not “Smith normal form” or “a Picard basis” by itself. The stronger reusable contract is:

```text
1. Pin source and target finite modules, bases, quotient conventions, and action generators by hash.
2. Compute exact normal forms/quotients with witness transforms, not only dimensions.
3. Carry coordinates through explicit forward/inverse or adjoint/basis maps.
4. Verify round-trip and pairing identities.
5. Verify group-action intertwining (including any proposed generator relabeling).
6. Compute the actually reachable quotient/cohomology subspace.
7. Accept a named source-target relation only if the target lies in that reachable image.
8. Fail closed: incompatibility revokes the relation but does not revoke independently verified source or target coordinates.
```

This contract is the promoted **candidate method** in `S33-PW05`, with `S33-PW04` supplying the source-coordinate adapter and `S33-PW02` supplying the finite-module normal-form layer.

### Existing-Arsenal / provisional-card overlap

- No current formal selector in `docs/arsenal/index.json` duplicates this Picard/Kummer finite-module adapter band; the formal selectors there concern other population/transition roles.
- `S33-PW02` already owns exact Smith/invariant-factor compression, so a new “Smith weapon” would be duplicate registry inflation.
- `S33-PW04` already owns Picard-adjoint source coordinates, so Picard marking/basis work is integrated there only at the **adapter-contract** level; the concrete Kc/J2 basis remains Stage33-specific.
- `S33-PW05` already owns source-target compatibility auditing and is the natural home for the stronger equivariant finite-module transport/reachability contract.
- `S33-PW03` remains the distinct quotient/raw-order Bockstein warning and should not be merged into Smith reduction, because Smith form alone does not recover the raw extension class.
- Stage32 `S32-PW03` (Picard lattice image/HNF gate) is adjacent but not duplicate: it is an integral lattice-image/saturation gate, whereas this Stage33 band is mod-2/proper-Br2/Pic2 finite-module coordinate transport. Keep them separate pending a later cross-stage promotion review.

### Hostile-audit / revoked exclusions

The following are explicitly **not** Arsenal weapons:

```text
C2 + C3 = h_J2
status=REVOKED_EXACT_DO_NOT_USE
revoking_certificate=stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json
revoking_canonical_sha256=463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229

copy_u1_A_T2_vector_into_proper_Br2_dual_basis
status=REJECTED_EXACT_DO_NOT_RETRY

order4_direct_picard_pullback_route
status=SUPERSEDED_DO_NOT_REOPEN
```

An incompatibility finding may be reused as a **methodological audit pattern**, but the revoked equation itself receives zero weapon/theorem credit.

## S33-PW01 — exact zero-survival classifier for the locked K3 Brauer 2-block

**Type:** `ARITHMETIC_HS_CLASSIFIER`

Source lock:

```text
path=stages/stage33/33-05/result.md
blob_sha=d72bbaf1d7f3200754e0cf2791f53c94c25ad417
primary_certificate=stage33-05-br2-zero-q-survival-after-j2-nogo.json
primary_canonical_sha256=a48386c523e8c98b1d2b22a7dc3d789e4cea1bfa4557e658fb150e3c6b85a585
hostile_replay_canonical_sha256=4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9
```

For the locked cuboid K3 block,

```text
Br(Kc_bar)[2]^G_Q = span_F2{J2,q1}
dim=2
rank_F2(d2|_<ct>)=2
ker(global d2 on the invariant block)=0
Q_RELEVANT_SURVIVING_DIM=0
```

The useful reusable pattern is: identify the entire finite invariant block, compute obstruction signatures on enough fixed tests to prove full rank, and allow **exact zero survival** as a valid downstream interface rather than forcing an explicit descended representative.

```text
ID=S33-PW01
SAME_KC_SOURCE_LOCK_REQUIRED=true
ZERO_SURVIVAL_IS_VALID_INTERFACE=true
CORRECTED_J2_Q_DEFINED_PREIMAGE=false
DO_NOT_GENERALIZE_TO_OTHER_K3S_WITHOUT_ADAPTER=true
```

## S33-PW02 — two-primary residue module -> invariant-factor reduction

**Type:** `FINITE_MODULE_REDUCTION`

Primary source: `stages/stage33/33-07/result.md` at Stage33 source head `fd0352c05675742ffed2800ab47354e4307494e0` (current reopened unit; only the retained exact prefix below is harvested).

The arithmetic repair was reduced exactly to

```text
FINITE_RAMIFIED_BOUNDARY_MODULE=(Z/2)^49 direct_sum (Z/4)^12
KNOWN_GLOBAL_U44=(Z/2)^44
BOUNDARY_QUOTIENT_AFTER_U44=(Z/2)^23 direct_sum (Z/4)^3
PRESENTATION_INPUT_GENERATORS=29
MINIMAL_INVARIANT_FACTOR_GENERATORS=26
PROPER_GEOMETRIC_BR2_DIMENSION_F2=14
PROPER_GEOMETRIC_BR2_V4_FIXED_DIMENSION_F2=10
FINITE_V4_H1_PROPER_BR2_DIMENSION_F2=16
TWO_PRIMARY_RESIDUE_INVARIANT_BASIS_SHA256=f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939
```

An explicit unimodular Smith decomposition gives mutually inverse integer coordinate maps between the 29 presentation generators and the 26 invariant-factor generators.

Use when a large residue presentation should be compressed to a canonical finite abelian basis before localization/descent calculations. For reuse, retain the relation matrix convention, invariant factors, and the exact forward/inverse witness transforms; a list of invariant factors alone is insufficient for coordinate transport.

```text
ID=S33-PW02
EXACT_FINITE_RESIDUE_MODULE_ONLY=true
REVERSIBLE_COORDINATE_WITNESSES_REQUIRED=true
GLOBAL_Q_LIFT_NOT_IMPLIED=true
ABSOLUTE_H1_NOT_IDENTIFIED_WITH_FINITE_V4_H1=true
UNIT_33_07_REMAINS_REOPENED=true
```

## S33-PW03 — quotient-order2 vs raw-order4 Bockstein adapter

**Type:** `EXTENSION_WARNING_ADAPTER`

Primary source: `stages/stage33/33-07/result.md` at Stage33 source head `fd0352c05675742ffed2800ab47354e4307494e0`.

The quotient `A[2]=(Z/2)^26` cannot be treated as 26 raw squareclass directions. Exact raw-residue analysis gives

```text
QUOTIENT_A2_DIMENSION_F2=26
RAW_ORDER2_FIRST_RESIDUE_FUNCTION_LIFTABLE=17
QUOTIENT_ONLY_ORDER2_WITH_RAW_ORDER4_RESIDUE=9
QUOTIENT_TO_RAW_DOUBLE_OBSTRUCTION_RANK_F2=9
ORDER2_FIRST_RESIDUE_LIFTABILITY_CERTIFICATE_SHA256=85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312
```

The nine remaining directions must stay order four until the Bockstein/extension is resolved; forcing them into order-two Kummer squareclasses is invalid.

Use as a general warning/adapter pattern whenever a quotient has exponent two but the raw extension may retain order-four representatives.

```text
ID=S33-PW03
QUOTIENT_ORDER2_DOES_NOT_IMPLY_RAW_ORDER2=true
CHECK_DOUBLE_OBSTRUCTION_BEFORE_SQUARECLASS_MODEL=true
PROJECT_SPECIFIC_NUMBERS_REQUIRE_SOURCE_MATCH=true
```

## S33-PW04 — Picard-adjoint -> proper Brauer source-coordinate adapter

**Type:** `EXACT_SOURCE_ADAPTER`

Current active-source lock:

```text
path=stages/stage33/33-12/j2-picard-adjoint-proper-br2.json
canonical_sha256=066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8
proper14_coordinate=[1,0,0,1,1,0,0,0,0,0,0,0,0,0]
retained10_coordinate=[0,1,1,0,0,0,0,0,0,0]
source_ref=stage33-post1475-j2-v4-generator-adapter@fd0352c05675742ffed2800ab47354e4307494e0
```

The exact Picard-adjoint map supplies the corrected J2 coordinate in the proper geometric Brauer module and its retained 10-dimensional invariant basis. This source coordinate is reusable independently of the revoked historical direct order-four pullback route.

For adapter reuse, the hypotheses are stronger than “same dimensions”: the Picard marking, source dual/adjoint convention, proper14 target basis, retained10 basis, and matrix direction must all match their locked hashes/conventions. Pairing/adjoint identities and an exact coordinate round trip or independent invariant projection should be checked before consuming the coordinate.

```text
ID=S33-PW04
SOURCE_COORDINATE_EXACT=true
BASIS_AND_ADJOINT_CONVENTIONS_ARE_HYPOTHESES=true
TARGET_75D_BINDING_NOT_IMPLIED=true
OLD_C2_PLUS_C3_RELATION_NOT_AUTHORIZED=true
REQUIRES_LOCKED_PICARD_ADJOINT_BASIS=true
DO_NOT_COPY_A_T2_COEFFICIENTS_INTO_PROPER_DUAL_BASIS=true
```

## S33-PW05 — finite module-extension source/target reachability audit

**Type:** `COMPATIBILITY_AUDIT_METHOD`

Current active-source locks:

```text
source_path=stages/stage33/33-12/j2-picard-adjoint-proper-br2.json
source_canonical_sha256=066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8
target_path=stages/stage33/33-12/full-surface-pic2-kummer-target.json
target_basis_canonical_sha256=384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890
audit_path=stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json
audit_canonical_sha256=463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229
locked_source_reachable_H1_dimension_f2=13
compatible=false
source_ref=stage33-post1475-j2-v4-generator-adapter@fd0352c05675742ffed2800ab47354e4307494e0
```

Instead of accepting a source/target relation because the two sides have plausible dimensions or labels, enumerate/test every module extension compatible with the locked source and target group actions, compute the reachable cohomology subspace, and verify that the named target is actually reachable. In the locked J2 case, the source reaches only a 13-dimensional H1 subspace and the named 75D target lies outside it, revoking the old relation.

The reusable contract also covers source-target coordinate transport: pin both bases and action generators, preserve exact forward/inverse or quotient-coordinate witnesses, test action intertwining under any proposed generator adapter, and only then test target reachability. A failed binding does not invalidate independently certified source and target coordinates.

Use this method before promoting an explicit Kummer/descent source-target identity assembled from independently computed coordinate systems.

```text
ID=S33-PW05
TEST_EXTENSION_COMPATIBILITY_BEFORE_BINDING=true
EXACT_BASIS_AND_ACTION_LOCKS_REQUIRED=true
INTERTWINING_CHECK_REQUIRED=true
REACHABLE_IMAGE_CHECK_REQUIRED=true
DIMENSION_MATCH_ALONE_INSUFFICIENT=true
GENERATOR_LABEL_MATCH_ALONE_INSUFFICIENT=true
GAUGE_SANITY_REQUIRED=true
CURRENT_J2_BINDING_REPAIR_OPEN=true
DO_NOT_USE_REVOKED_C2_PLUS_C3_EQUATION=true
```

## S33-PW06 — finite-quotient cohomology is not the absolute arithmetic obstruction

**Type:** `DESCENT_WARNING_RECIPE`

Primary source: `stages/stage33/33-07/result.md` at Stage33 source head `fd0352c05675742ffed2800ab47354e4307494e0`.

When the coefficient action factors through

```text
L=Q(i,sqrt(2)), Gal(L/Q)=V4,
```

inflation--restriction leaves a genuine `G_L` restriction term. The corrected decision order is

```text
Stage A: F2^26 -> ((L*/L*2) tensor_F2 Br(Sbar)[2])^V4
Stage B: ker(Stage A) -> H^1(V4,Br(Sbar)[2]).
```

The finite `V4` H1 receiver alone does not determine the absolute obstruction; genuine geometric lift/squareclass data are required.

```text
ID=S33-PW06
FINITE_QUOTIENT_H1_IS_NOT_ABSOLUTE_H1=true
INFLATION_RESTRICTION_TERM_MUST_BE_CHECKED=true
ABSTRACT_ENDPOINT_MODULES_DO_NOT_DETERMINE_GEOMETRIC_LIFT=true
```

## Promotion firewalls

- These are provisional active-Stage cards and are not formal `selectors`.
- Stage33 hostile reopenings override older successful-looking relations. Only the exact surviving interface stated in a card may be reused.
- `S33-PW01` is a result for the locked K3 block, not a general K3 theorem.
- `S33-PW02/PW03/PW06` explicitly do not promote finite residue/cohomology data to global Q-defined classes.
- `S33-PW04` gives a source coordinate only. `S33-PW05` currently says the old J2 source-target binding is incompatible; it does not supply the replacement binding.
- Concrete Picard markings, Pic/2 bases, V4 matrices, J2 coordinates, 75D target coordinates, and Stage33-specific ranks/invariant factors are provenance, not portable weapon claims.
- At Stage33 close, rerun hostile promotion review and activate/revise/retire each card.

```text
PROVISIONAL_WEAPONS=S33-PW01,S33-PW02,S33-PW03,S33-PW04,S33-PW05,S33-PW06
TARGETED_R02_NEW_CARD_COUNT=0
TARGETED_R02_INTEGRATED_CARDS=S33-PW02,S33-PW04,S33-PW05
TARGETED_R02_WORKFLOW_CANDIDATES=SMITH_ROUNDTRIP,BASIS_ADJOINT_AUDIT,V4_EQUIVARIANT_TRANSPORT_AUDIT
ROUTEABLE_FOR_CANDIDATE_DISCOVERY=true
FORMAL_PROMOTION_ACTIVE=false
PERFECT_CUBOID_CONCLUSION=NONE
```
