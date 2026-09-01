# Stage33 arsenal promotion — provisional harvest

```text
REGISTRY=STAGE33-ARSENAL-PROVISIONAL-R03
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage33
SOURCE_PR=1476
SOURCE_BRANCH=stage33-post1475-j2-v4-generator-adapter
SOURCE_HEAD=fd0352c05675742ffed2800ab47354e4307494e0
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
THEOREM_CREDIT=false
```

This file harvests reusable Stage33 mathematics and exact adapters before Stage33 closes. It is a candidate-discovery/source-routing layer only. Hostile reopenings and current Stage33 source locks override every provisional card.

## Targeted harvest R03 — Brauer / Hochschild–Serre / descent / torsor / cohomology

This pass was reverse-indexed from `stages/stage33/MAIN-STATE.json`, closed prerequisite summaries, retained unit results, and the exact certificates named by those sources. Stage33 history was not reread sequentially.

```text
source_head=fd0352c05675742ffed2800ab47354e4307494e0
main_state_blob_sha=d32fa72fc321a0d6f50485ecc8c6abd4c690a378
main_state_canonical_sha256=32baebf358ae47b99a5a1ffd40dc90e7eb090db353f58861702bba3f0db0a9fc
scope=Brauer; Hochschild-Serre; descent; torsors; cohomology; supporting Picard/Pic2/Kummer finite-module adapters
```

### R03 classification

| Harvest object | Class | Arsenal disposition | Source / SHA | Hypotheses and applicability | DO_NOT_USE_FOR |
|---|---|---|---|---|---|
| Complete finite invariant Brauer block + exact HS obstruction matrix giving zero survivor | **1. Arsenal candidate** | retain `S33-PW01` | `stages/stage33/33-05/result.md`, blob `d72bbaf1d7f3200754e0cf2791f53c94c25ad417`; primary canonical `a48386c523e8c98b1d2b22a7dc3d789e4cea1bfa4557e658fb150e3c6b85a585`; hostile canonical `4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9` | The entire relevant invariant block is known, the tested restriction detects the global obstruction injectively on that block, and the exact pairing/signature matrix is full rank. | General K3 vanishing; a Q-defined representative; extrapolation from an incomplete invariant block or non-injective local test. |
| Finite residue presentation -> invariant factors with reversible Smith coordinates | **1. Arsenal candidate** | retain `S33-PW02` | `stages/stage33/33-07/result.md`, blob `2a5f84a1fd34be395c216b343079ed85a525fb14`; invariant-basis SHA256 `f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939` | Exact finite abelian presentation; unimodular witness transforms retained in both directions. | Global Q-lifts; arithmetic HS closure; recovering extension data from invariant factors alone. |
| Quotient order two vs raw order four / Bockstein extension wall | **1. Arsenal candidate** | retain `S33-PW03` | `stages/stage33/33-07/result.md`, blob `2a5f84a1fd34be395c216b343079ed85a525fb14`; liftability SHA256 `85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312` | Quotient and raw extension are both explicitly represented; doubling obstruction is computed. | Replacing all quotient 2-torsion by raw squareclasses; suppressing order-four representatives. |
| Picard-adjoint -> proper Brauer source coordinate | **1. Arsenal candidate** | retain `S33-PW04`; supporting adapter | `stages/stage33/33-12/j2-picard-adjoint-proper-br2.json`, blob `2e70dc274afbbd20aefbb0a87409d66d6ac183bc`, canonical `066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8` | Picard marking, dual/adjoint convention, target basis and matrix direction are source-locked and pairing identities are verified. | Kummer target binding; copying unrelated Pic/2 coefficients into the proper dual basis; changing markings without recomputation. |
| Exact cohomological source-target compatibility/reachability audit | **1. Arsenal candidate** | retain `S33-PW05` | source canonical `066e6b...cb9f8`; Pic/2 target `stages/stage33/33-12/full-surface-pic2-kummer-target.json`, blob `a29e560984034fdfdc38a8d12908efbe23e70ec1`, canonical `384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890`; audit `j2-kummer-source-target-module-compatibility-audit.json`, blob `40dc28e0bae28208fb1dda3fc1a1578b62606f13`, canonical `463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229` | Both finite modules and group actions are explicit; basis/generator conventions are pinned; compatible extensions/reachable image are computed exactly. | Dimension/label matching; arbitrary generator relabeling; the revoked J2 relation; identifying finite H1 with absolute H1. |
| Finite quotient H1 -> exact absolute-H1 receiver via induced modules, Shapiro and LES | **1. Arsenal candidate** | **extend `S33-PW06`**, no duplicate card | `stages/stage33/33-10/result.md`, blob `49bb309f994742874572f485bd5e594fe4439ed4`; closed-interface canonical `4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f`; supporting reopened `33-07/result.md` blob `2a5f84...` | Exact Galois-module decomposition is established. Induced/permutation pieces satisfy the Shapiro hypotheses; quotient blocks are handled by the long exact sequence without assuming a splitting. | Killing kernel-Galois terms; treating `H1(V4,K)` as `H1(G_Q,K)`; splitting the residual extension without proof; computing arithmetic localization automatically. |
| Brauer class -> translation-valued cocycle -> correct genus-one torsor -> integral transcendental-kernel adapter | **1. Arsenal candidate** | **new `S33-PW07`** | torsor `stages/stage33/33-05/j2-r4-correct-translation-torsor.json`, blob `5a0ac87e7afc7b048d6bbe9c12bea7fe91a0348b`, canonical `ef72c43811428acb2d4c1ea58d4867d7bbcc5c20774b6724eb8b272450cd0725`; hostile kernel verification `j2-r4-hostile-torsor-brauer-kernel-verification.json`, blob `32be9c1f272a4b12d032bbba00d9bbea1edf2622` | Geometric elliptic-K3/genus-one setting with relative Jacobian; the same exact cocycle is matched through the Brauer/HS/Ogg-Shafarevich dictionary; semilinear translation descent constructs the torsor; the integral kernel theorem applies with pairing conventions checked. | Q-descent; arbitrary genus-one curves; identifying an isogeny cover with the torsor; using equal j-invariants or rational Hodge isometry alone; theorem credit for the external dictionary itself. |
| Exact HS zero-survival matrix protocol | **2. Workflow candidate** | workflow under `PW01` | `33-05/result.md`; hostile replay canonical `4e9f20c1...` | Enumerate the whole invariant block, choose fixed tests whose restriction is certified to detect the obstruction, build an exact matrix, prove rank. | Sampling-based vanishing or testing only a preferred representative. |
| Absolute-H1 receiver construction protocol | **2. Workflow candidate** | workflow under `PW06` | `33-10/result.md`, blob `49bb309...` | Decompose the coefficient Galois module first; apply continuous Shapiro to induced blocks; use LES for quotient blocks; preserve nonsplit extensions. | A finite-group shortcut when the absolute Galois kernel contributes. |
| Torsor semantic-validation protocol | **2. Workflow candidate** | workflow under `PW07` | torsor canonical `ef72c438...`; hostile torsor-kernel blob `32be9c1...` | Check exact Jacobian, semilinear descent action and cocycle identity; then verify that the Brauer edge and torsor class are the same class before lattice/kernel use. | Calling a 2-isogeny homogeneous-space quartic the original Jacobian torsor merely because there is a degree-two map. |
| Connecting-map fail-closed / hostile-replay protocol | **2. Workflow candidate** | workflow only; do not promote the project-specific zero map | stale hostile negative evidence `stages/stage33/33-11/audit-state.json`, blob `dfb1072cae83618e281bfd555d7f6ef25f853fa4`; later closed prerequisite summarized in `stages/stage33/33-12/result.md`, blob `fc410a317d71362153aba8aa9489b005d1d3e45d`, canonical `233be042e92010be169206df1193f25375ee9fd768f7fb3eebb9eb696389632e` | Do not assume an equivariant lift. Compute actual Galois-difference/connecting columns and rerun hostile audit after repairing the representative. | Concluding a connecting map is zero from visible-boundary invariance, naturality, dimension counting, or a lift chosen to be fixed by construction. |
| Concrete J2/f2/Tr torsor equation and invariant functions | **3. Stage33-specific — no promotion** | provenance under `PW07` only | `j2-r4-correct-translation-torsor.json`, canonical `ef72c438...` | Locked cuboid K3 generic fiber and corrected J2 cocycle. | A universal torsor formula. |
| Concrete Kc invariant block `{J2,q1}`, its 2x2 test matrix and named test cycles | **3. Stage33-specific — no promotion** | example payload under `PW01` | `33-05/result.md`; canonical `4e9f20c1...` | Locked Kc Brauer block. | Other K3 surfaces or different invariant blocks. |
| Concrete proper-Br2 Galois-module multiplicities, `L=Q(i,sqrt(2))`, and finite H1 dimension 16 | **3. Stage33-specific — no promotion** | example payload under `PW06` | `33-10/result.md`, blob `49bb309...` | Locked Stage33 coefficient module. | Copying the decomposition or dimensions to another module. |
| `T(Kc)=diag(4,8)`, `T(X_J2)=diag(8,16)`, minimum norm 8, marked coordinate `[1,0]` | **3. Stage33-specific — no promotion** | provenance under `PW07` | hostile torsor-kernel verification blob `32be9c1...` | Corrected geometric J2 only. | A generic transcendental-lattice theorem or Q-defined descent. |
| Stage33-11 exact zero localization map and its 26 columns | **3. Stage33-specific — no promotion** | retain as closed prerequisite, not weapon theorem | `33-12/result.md`, blob `fc410a...`, canonical `233be042...` | Exact Stage33 residue/localization system only. | Predicting zero localization in another problem. |

### R03 overlap / integration decision

- `S33-PW01`, `PW02`, `PW03`, `PW04`, and `PW05` already cover reusable pieces touched by this band; do not create duplicates.
- `S33-PW06` is strengthened from a warning (“finite quotient H1 is not absolute H1”) into an exact receiver-construction recipe using Stage33-10. It remains one card.
- `S33-PW07` is genuinely new: existing cards do not connect an exact Brauer/HS cocycle to the corresponding genus-one torsor and then to an **integral** transcendental-kernel lattice under strict geometric hypotheses.
- Existing formal selectors in `docs/arsenal/index.json` do not duplicate these Brauer/HS/torsor/cohomology interfaces.
- `S33-PW05` and `PW07` are complementary: PW05 audits a finite Kummer/cohomology binding; PW07 validates the geometric Brauer↔torsor dictionary. Neither implies the other.

### R03 hostile / revoked exclusions

Do not promote or restore any of the following:

```text
C2 + C3 = h_J2
status=REVOKED_EXACT_DO_NOT_USE
revoking_canonical_sha256=463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229

attempt1_standard_Tr_isogeny_quartic_as_the_named_original-E_torsor
status=REVOKED_BY_CORRECT_TRANSLATION_DESCENT
reason=its Jacobian is the 2-isogenous comparison curve, not the original E torsor

visible_boundary_V4_fixed_or_chosen_fixed_global_lift_implies_connecting_map_zero
status=REJECTED_BY_33_11_HOSTILE_AUDIT
later_zero_map_requires_repaired_explicit_columns_and_hostile_pass

global_Q_residue_lift_inventory_from_old_33_07_closure
status=SUPERSEDED_BY_STAGE33_08_HOSTILE_REOPEN

corrected_J2_Q_defined_Brauer_preimage
status=false
```

## Targeted harvest R02 retained — Picard / Kummer / finite-module / coordinate adapters

R02 remains active and is not replaced by R03. Its integrated cards are `S33-PW02`, `S33-PW04`, and `S33-PW05`; workflow candidates are `SMITH_ROUNDTRIP`, `BASIS_ADJOINT_AUDIT`, and `V4_EQUIVARIANT_TRANSPORT_AUDIT`. Concrete Kc/J2 bases, Pic/2 coordinates, V4 matrices and project-specific ranks remain Stage33-specific.

## S33-PW01 — exact zero-survival HS classifier

**Type:** `ARITHMETIC_HS_CLASSIFIER`

```text
source_path=stages/stage33/33-05/result.md
source_blob_sha=d72bbaf1d7f3200754e0cf2791f53c94c25ad417
primary_path=stages/stage33/33-05/stage33-05-br2-zero-q-survival-after-j2-nogo.json
primary_blob_sha=55d952e89c7ca8b732e4ed23c5483642c7f9a88f
primary_canonical_sha256=a48386c523e8c98b1d2b22a7dc3d789e4cea1bfa4557e658fb150e3c6b85a585
hostile_path=stages/stage33/33-05/stage33-05-br2-zero-q-survival-hostile-replay.json
hostile_blob_sha=4836625b559d27599c885bb80b232e33ae1408a3
hostile_canonical_sha256=4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9
```

Reusable output: a complete finite invariant Brauer block may be discharged by an exact full-rank HS obstruction matrix, and **zero survival** is a valid interface.

```text
HYPOTHESES=complete invariant block; exact obstruction map; injective detection on tested subgroup
APPLICABILITY=finite arithmetic-HS classification of a source-locked invariant block
DO_NOT_USE_FOR=general K3 vanishing; Q-defined representative; incomplete-block inference
```

## S33-PW02 — finite residue module -> invariant-factor basis

**Type:** `FINITE_MODULE_REDUCTION`

```text
source_path=stages/stage33/33-07/result.md
source_blob_sha=2a5f84a1fd34be395c216b343079ed85a525fb14
invariant_basis_sha256=f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939
```

Reusable output: exact Smith/invariant-factor compression with mutually inverse integral coordinate witnesses.

```text
HYPOTHESES=exact presentation and unimodular witness transforms retained
APPLICABILITY=finite residue/localization modules before descent calculations
DO_NOT_USE_FOR=global Q lift; Bockstein recovery; absolute H1 identification
```

## S33-PW03 — quotient/raw Bockstein adapter

**Type:** `EXTENSION_WARNING_ADAPTER`

```text
source_path=stages/stage33/33-07/result.md
source_blob_sha=2a5f84a1fd34be395c216b343079ed85a525fb14
liftability_sha256=85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312
```

Reusable output: quotient exponent two does not imply raw representatives have order two; compute the double/Bockstein obstruction first.

```text
DO_NOT_USE_FOR=forcing quotient 2-torsion into raw squareclasses
```

## S33-PW04 — Picard-adjoint -> proper Brauer source coordinate

**Type:** `EXACT_SOURCE_ADAPTER`

```text
source_path=stages/stage33/33-12/j2-picard-adjoint-proper-br2.json
source_blob_sha=2e70dc274afbbd20aefbb0a87409d66d6ac183bc
canonical_sha256=066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8
```

```text
HYPOTHESES=locked marking; adjoint/dual convention; target basis; matrix direction; exact pairing verification
APPLICABILITY=source-coordinate construction before Brauer/Kummer/cohomology transport
DO_NOT_USE_FOR=target binding; unrelated Pic2 coefficient copying; changed marking
```

## S33-PW05 — finite module source/target reachability audit

**Type:** `COMPATIBILITY_AUDIT_METHOD`

```text
source_path=stages/stage33/33-12/j2-picard-adjoint-proper-br2.json
source_canonical_sha256=066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8
target_path=stages/stage33/33-12/full-surface-pic2-kummer-target.json
target_blob_sha=a29e560984034fdfdc38a8d12908efbe23e70ec1
target_canonical_sha256=384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890
audit_path=stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json
audit_blob_sha=40dc28e0bae28208fb1dda3fc1a1578b62606f13
audit_canonical_sha256=463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229
```

```text
HYPOTHESES=both modules/bases/actions explicit; exact compatible-extension or intertwiner calculation
APPLICABILITY=Kummer/descent/cohomology identities assembled from independently computed coordinates
DO_NOT_USE_FOR=dimension-only binding; generator-label semantics; revoked C2+C3 relation; absolute H1 identification
```

## S33-PW06 — absolute-H1 receiver / finite-quotient firewall

**Type:** `ABSOLUTE_COHOMOLOGY_RECEIVER_RECIPE`

Primary closed source:

```text
path=stages/stage33/33-10/result.md
blob_sha=49bb309f994742874572f485bd5e594fe4439ed4
closed_interface_canonical_sha256=4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f
supporting_reopened_path=stages/stage33/33-07/result.md
supporting_blob_sha=2a5f84a1fd34be395c216b343079ed85a525fb14
```

Reusable method:

```text
1. Compute the exact absolute Galois-module decomposition of K.
2. Use continuous Shapiro on induced/permutation summands.
3. For quotient-regular blocks, retain the long exact sequence and its kernel/cokernel terms.
4. Do not split residual extensions unless separately proved.
5. Only then define the arithmetic localization/HS receiver.
```

Stage33's concrete example has an `E_L` term fitting an exact short filtration; that concrete decomposition is not itself portable.

```text
HYPOTHESES=exact Galois-module decomposition and valid Shapiro/LES inputs
APPLICABILITY=absolute H1 receivers when a finite quotient describes the coefficient action but the kernel Galois group may contribute
DO_NOT_USE_FOR=H1(V4,K)=H1(G_Q,K); killing kernel terms; automatic localization values; unproved splitting
```

## S33-PW07 — Brauer / translation-torsor / integral-kernel adapter

**Type:** `TORSOR_BRAUER_INTEGRAL_KERNEL_ADAPTER`

Source locks:

```text
torsor_path=stages/stage33/33-05/j2-r4-correct-translation-torsor.json
torsor_blob_sha=5a0ac87e7afc7b048d6bbe9c12bea7fe91a0348b
torsor_canonical_sha256=ef72c43811428acb2d4c1ea58d4867d7bbcc5c20774b6724eb8b272450cd0725
hostile_kernel_path=stages/stage33/33-05/j2-r4-hostile-torsor-brauer-kernel-verification.json
hostile_kernel_blob_sha=32be9c1f272a4b12d032bbba00d9bbea1edf2622
repair_state_path=stages/stage33/33-05/j2-representative-repair-state.json
repair_state_blob_sha=612d5a9628084cb06cc722d40a1355a92926b742
```

Reusable contract:

```text
Brauer representative/class
 -> exact HS/cohomological cocycle
 -> semilinear translation descent using the SAME cocycle
 -> genus-one torsor with the intended relative Jacobian
 -> Ogg-Shafarevich/Brauer identification
 -> integral transcendental-kernel identification when the lattice/moduli hypotheses apply.
```

The crucial semantic check is that a standard isogeny homogeneous-space quartic may have the wrong Jacobian even when it maps to the intended curve. The torsor must be built/verified as the class represented by the same translation-valued cocycle. The hostile certificate additionally rejects a merely rational Hodge-isometry argument and checks the inherited integral pairing.

```text
HYPOTHESES=geometric elliptic-K3/genus-one setting; exact common cocycle; semilinear descent; valid Brauer/Ogg-Shafarevich edge dictionary; smooth projective model; integral-kernel theorem hypotheses
APPLICABILITY=geometric Brauer classes whose torsor class can be explicitly matched to a translation-valued cocycle and whose relative Jacobian/moduli interpretation is available
DO_NOT_USE_FOR=Q-defined descent; arbitrary genus-one curves; isogeny-cover substitution; same-j-invariant inference; rational Hodge isometry alone; external-theorem credit
```

## Promotion firewalls

- All `S33-PW*` entries remain provisional; none is a formal selector or theorem/receiver/endpoint credit.
- Stage33 source locks and hostile audits override this file.
- Stage33-07 is still reopened; only its explicitly retained finite-module/Bockstein prefix is harvested.
- Stage33-11's final zero connecting map is exact for Stage33 but remains project-specific; only its fail-closed computation/audit workflow is harvested.
- `S33-PW07` is geometric. It does not restore Q-defined descent credit.
- Concrete Picard markings, Pic/2 bases, V4 matrices, J2 coordinates, torsor coefficients, lattice Gram matrices and Stage33-specific ranks are provenance, not portable claims.
- At Stage33 close, rerun a hostile promotion audit and activate/revise/retire each card.

```text
PROVISIONAL_WEAPONS=S33-PW01,S33-PW02,S33-PW03,S33-PW04,S33-PW05,S33-PW06,S33-PW07
TARGETED_R02_NEW_CARD_COUNT=0
TARGETED_R02_INTEGRATED_CARDS=S33-PW02,S33-PW04,S33-PW05
TARGETED_R02_WORKFLOW_CANDIDATES=SMITH_ROUNDTRIP,BASIS_ADJOINT_AUDIT,V4_EQUIVARIANT_TRANSPORT_AUDIT
TARGETED_R03_NEW_CARD_COUNT=1
TARGETED_R03_NEW_CARD=S33-PW07
TARGETED_R03_EXTENDED_CARD=S33-PW06
TARGETED_R03_WORKFLOW_CANDIDATES=HS_ZERO_SURVIVAL_MATRIX,ABSOLUTE_H1_RECEIVER_DECOMPOSITION,TORSOR_SEMANTIC_VALIDATION,CONNECTING_MAP_FAIL_CLOSED
TARGETED_R03_STAGE33_SPECIFIC_DATA_PROMOTED=false
TARGETED_R03_REVOKED_CLAIMS_PROMOTED=false
ROUTEABLE_FOR_CANDIDATE_DISCOVERY=true
FORMAL_PROMOTION_ACTIVE=false
PERFECT_CUBOID_CONCLUSION=NONE
```
