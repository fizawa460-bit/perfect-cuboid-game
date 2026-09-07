# Stage36 literature-backed Arsenal strengthening

Status: **PROVISIONAL — hostile audit required; no Stage36 mathematical credit**

```text
LITERATURE_DELTA_STAGE=Stage36
LITERATURE_AUDIT_PR=1690
LITERATURE_AUDIT_EXACT_HEAD=f1a2d3074e802b0fd4555cb827e165c3de2bdfc9
IMPLEMENTATION_PR=1692
IMPLEMENTATION_BRANCH=arsenal-stage36-literature-strengthening-implementation
ARSENAL_BASE_MAIN=386b6a52d7bfec2e8903412c7ca56976b46c288b
IMPLEMENTATION_BASE_MAIN=e758e05953df2cf8cd4ab26ac1e9d72374e99760
STAGE36_ARSENAL_SOURCE_HEAD=2fc3f4b8afb28bb23765bd861cbd7c52aafd6563
STAGE36_HARVEST_SNAPSHOT_HEAD=07a465cb5025e7c0188fb63610bb40e4b54e7a84
STAGE36_DELTA_ONLY=true
PHASE3_MANIFEST_FROZEN=true
LITERATURE_POPULATION_EXPANDED=false
HOSTILE_AUDIT_REQUIRED_BEFORE_FORMAL_TREATMENT=true
```

Authority remains:

`active Stage36 authority > existing formal Arsenal > Stage36 provisional Arsenal > this literature-backed provisional extension`.

A published theorem and a repo adapter are separate proof layers. No cited theorem is represented as a theorem proved by Stage36.

## Credit firewall

```text
LITERATURE_ARSENAL_REGISTRATION_DOES_NOT_CHANGE_STAGE36_MATHEMATICAL_AUTHORITY=true
STAGE36_PROGRESS_INCREMENT=0
STAGE36_THEOREM_CREDIT_INCREMENT=0
RECEIVER_CLOSURE_INCREMENT=0
MW_CLOSURE_INCREMENT=0
LOCAL_GLOBAL_OBSTRUCTION_INCREMENT=0
ENDPOINT_CREDIT_INCREMENT=0
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
NOVEL=false
FIRST_PROOF=false
NEW_THEOREM=false
```

## Frozen Phase 4 manifest

- Stage36 literature-direct: `S36-PW02`, `S36-PW06`
- Stage36 literature-adapted: `S36-PW04`, `S36-PW07`
- Stage36 existing-card extension: `S36-PW03`
- Older-card extensions: `S30-W01 <- DISC-S36-B01`, `S31-W01 <- DISC-S36-B08`, `S34-W02 <- DISC-S36-B12`
- Source-anchor-only: `S36-PW01`, `S36-PW05`
- New literature weapons: none
- New provisional workflow: `LIT-WF02 GLOBAL_H1_LOCALIZATION_RECIPROCITY_APPLICABILITY_WORKFLOW`
- Research gap: `GLOBAL-HILBERT-SELMER-COMPATIBILITY-TERMINAL`

The seven hostile duplicate families remain inactive: reciprocal methods; finite-prime Weil completion; transvection/symplectic pruning; finite-group reconstruction; MW/local sieve; factor/squareclass linearization; Gaussian/norm lineage.

## S36-PW02 — PROVISIONAL_LITERATURE_EXTENSION

**Classification:** LITERATURE_DIRECT. `CURRENT_CORE` remains the Stage36 provisional contract; this section adds only an exact literature lock.

Reusable extension contract:

```text
STAGE36_SOURCE_RESULT
  exact V4 action/maps + quotient/full-group genera + differential independence
-> REPO_ADAPTER
  certify the exact subgroup relation and genus-zero full quotient over the stated field
-> LITERATURE_THEOREM
  Kani-Rosen Theorem B
-> STRENGTHENED_ARSENAL_OUTPUT
  theorem-locked Jacobian isogeny decomposition, with no rational-point converse
```

HYPOTHESES: smooth retained curve; exact V4 action/maps over the working field; quotient and full-group genera exact; Kani-Rosen subgroup/idempotent relation applicable; factor independence certified.

APPLICABILITY: exact Klein-four curve symmetry. DO_NOT_USE_FOR: source rational-point classification; quotient Mordell-Weil rank; combining arbitrary quotient points into a source point; extension-field points as base-field points.

Literature: Ernst Kani; Michael Rosen, “Idempotent relations and factors of Jacobians”, *Mathematische Annalen* 284 (1989), 307–328. DOI `10.1007/BF01442878`. Canonical URL: https://doi.org/10.1007/BF01442878. Locator: **Theorem B**. Conclusion used: the V4 idempotent relation gives the stated product isogeny; when the full quotient has genus zero its Jacobian factor is trivial. Source type: original peer-reviewed paper. Conditional assumptions: only the theorem/field/action hypotheses above.

Repo provenance: source PR `1642`; exact source head `be979251c6e3d7a2431fb56537520afd2596c7d9`; source/certificate `stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json`, blob `6a2678ebedba40e13277100441361039ee47ca28`; verifier `stages/stage36/verify_stage36_36_09O.py`, blob `ed0ae786505e3443226eaed6e61b7c78ee389191`; literature source-lock `stages/stage36/36-09O/kani-rosen-v4-jacobian-source-lock.md`, blob `5b5957843933b487bb9cae3acd22bb7737f37392`.

Strength delta: exact theorem provenance only; mathematical output remains the existing Jacobian isogeny contract.

## S36-PW03 — PROVISIONAL_LITERATURE_EXTENSION

**Classification:** EXTEND_STAGE36_EXISTING.

Reusable extension contract:

```text
receiver-forced independent anti-invariant quadratic-extension direction
-> exact twist/eigenspace identification
-> standard quadratic-twist rank decomposition
-> optional rank-jump theorem context ONLY after an exact family-hypothesis adapter passes
```

HYPOTHESES: explicit quadratic extension and twist isomorphism; Galois action exact; generic MW/Kummer baseline source-locked; receiver direction independent; every selected rank-jump theorem hypothesis verified before use. DO_NOT_USE_FOR: receiver existence from rank growth; full MW group from one witness; non-thin rank-jump claim before family hypotheses match.

Literature: Lilybelle Cowland Kellock; Vladimir Dokchitser, “Root numbers and parity phenomena”, *Bulletin of the London Mathematical Society* 55 (2023), 2557–2597, DOI `10.1112/blms.12931`, https://doi.org/10.1112/blms.12931, **Lemma 2.9** for quadratic-extension/twist rank decomposition. Joseph H. Silverman, “Heights and the specialization map for families of abelian varieties”, *J. reine angew. Math.* 342 (1983), 197–211, DOI `10.1515/crll.1983.342.197`, https://doi.org/10.1515/crll.1983.342.197, **Theorem C** specialization background. Daniel Loughran; Cecília Salgado, “Rank jumps on elliptic surfaces and the Hilbert property”, *Annales de l'Institut Fourier* 72 (2022), 617–638, DOI `10.5802/aif.3457`, https://doi.org/10.5802/aif.3457, **Theorems 1.1 and 1.2**. Source type: original peer-reviewed papers. Conditional assumption: Loughran–Salgado is inactive until the exact Stage36 family satisfies one cited theorem's hypotheses.

Repo provenance: source PR `1664`; exact source head `25229e7b0dfbbc5524266ce49e8edaf217841701`; source/certificate `stages/stage36/36-09U/qi-antiinvariant-rankjump-descent-preflight.json`, blob `a1f0c924d267ab4f45aaada6c9bcb3a5f544f284`; verifier `stages/stage36/verify_stage36_36_09U.py`, blob `21b3b1461195cfae1a1294832f8e77f09a09983b`.

Missing repo adapter for rank-jump use: `STAGE36_FAMILY_TO_RANK_JUMP_THEOREM_HYPOTHESES`. Until it exists, output is only the typed necessary twist-growth obligation already present in S36-PW03.

## S36-PW04 — PROVISIONAL_LITERATURE_EXTENSION

**Classification:** LITERATURE_ADAPTED.

Typed handoff:

```text
STAGE36_SOURCE_RESULT
  canonical pointwise elementary-2 lift charts and squareclass tuple
-> REPO_ADAPTER
  POINTWISE_CHART_TUPLE_TO_GLOBAL_KUMMER_OR_TORSOR_CLASS
-> LITERATURE_THEOREM / EXISTING ARSENAL
  explicit descent / LIT-PW03
-> STRENGTHENED_ARSENAL_OUTPUT
  genuine global n-cover/Selmer input semantics only where the adapter is proved
```

HYPOTHESES: exact elementary-2 torsor/basis/charts; transition ratios invariant squares; one named global finite module/class identified; exact cover/Jacobian and localization maps. DO_NOT_USE_FOR: Kummer-shaped equations as a covering identity; Selmer membership as a rational point; marked Brauer/H2 import without its own source binding.

Literature: Edward F. Schaefer, “2-Descent on the Jacobians of Hyperelliptic Curves”, *Journal of Number Theory* 51 (1995), 219–232, DOI `10.1006/jnth.1995.1044`, https://doi.org/10.1006/jnth.1995.1044; Edward F. Schaefer, “Computing a Selmer group of a Jacobian using functions on the curve”, *Mathematische Annalen* 310 (1998), 447–471, DOI `10.1007/s002080050156`, https://doi.org/10.1007/s002080050156; J. E. Cremona, T. A. Fisher, C. O'Neil, D. Simon, M. Stoll, “Explicit n-descent on elliptic curves, II. Geometry”, *J. reine angew. Math.* 632 (2009), 63–84, DOI `10.1515/CRELLE.2009.050`, https://doi.org/10.1515/CRELLE.2009.050. Exact selected internal theorem/algorithm locator was not frozen by Phase 3; therefore no theorem-output credit is registered here. The adapter remains fail-closed and routes to existing provisional `LIT-PW03`. Source type: original peer-reviewed papers.

Repo provenance: source PR `1560`; exact source head `dcdae282120f29a42679b654e21bd35f843e4cbf`; source/certificate `stages/stage36/36-04/h-torsor-lift-class.json`, blob `a06e201a9b554da71c5e75d8f8541e7284f8d020`; verifier `stages/stage36/verify_stage36_36_04.py`, blob `35d288d8a18adee95830caa6ee9d6b0d8ebe9e53`.

## S36-PW06 — PROVISIONAL_LITERATURE_EXTENSION

**Classification:** LITERATURE_DIRECT.

Reusable extension contract:

```text
split-full-2 elliptic family over Q(t)
+ visible generic sections/classes
+ exact q0 specialization criterion replay
+ complete specialized 2-isogeny descent
-> Gusic-Tadic Theorem 1.1 injectivity
-> exact generic rank/Kummer baseline already certified by the Stage36 adapter
```

HYPOTHESES: nonconstant `E/Q(t): y^2=(x-e1)(x-e2)(x-e3)` with `ei in Z[t]`; good specialization `t0`; every required nonconstant square-free divisor evaluates to a nonsquare; complete fixed-fiber descent; torsion/nontorsion certified. DO_NOT_USE_FOR: uniform rank of all fibers; rank-jump exclusion; full generic MW group without basis/index proof; receiver closure.

Literature: Ivica Gusić; Petra Tadić, “A remark on the injectivity of the specialization homomorphism”, *Glasnik Matematicki* 47 (2012), 265–275. DOI `10.3336/gm.47.2.03`. Canonical URL: https://doi.org/10.3336/gm.47.2.03. Locator: **Theorem 1.1**. Conclusion used: the stated square-free-divisor criterion is sufficient for injective specialization. Source type: original peer-reviewed paper. Conditional assumptions: exactly the theorem and good-specialization hypotheses above.

Repo provenance: source PR `1640`; exact source head `8ca23e42a057af260c7051c20dd8f608067efefd`; source/certificate `stages/stage36/36-09N/relative-2isogeny-kummer-image-rank1-preflight.json`, blob `02a14439d94d7f6e5ac2f65e995e8acfb6845788`; verifier `stages/stage36/verify_stage36_36_09N.py`, blob `e7effbe9ee6106505db013f326ec653627885054`; corrected literature source-lock `stages/stage36/36-09N/relative-2isogeny-specialization-source-lock.md`, blob `a562d7053a6f04deff4473067777b7cfd538ea8a`.

Strength delta: exact theorem lock only. The `q0=6` divisor replay, fixed-fiber descent, visible-section lower bound, torsion checks and Kummer synthesis are repo work; theorem citation alone gives no full-MW upgrade.

## S36-PW07 — PROVISIONAL_LITERATURE_EXTENSION

**Classification:** LITERATURE_ADAPTED.

Typed handoff:

```text
STAGE36_SOURCE_RESULT
  source-derived self/cross/dyadic/real local character matrix
-> REPO_ADAPTER
  DYNAMIC_RESERVOIR_ROWS_TO_GLOBAL_KUMMER_LOCALIZATION_SYSTEM
-> LITERATURE_THEOREM
  Hilbert reciprocity / global realizability; Poitou-Tate only for a fixed finite global module
-> STRENGTHENED_ARSENAL_OUTPUT
  global compatibility/orthogonality data, not automatically a contradiction
```

HYPOTHESES: exact reservoirs/classes; one fixed global squareclass or finite Galois module; complete localization maps; 2-adic and real normalization; all required places accounted. DO_NOT_USE_FOR: product formula as contradiction; local admissibility as a global point; dynamic support as a fixed Selmer problem without proof.

Literature: Jean-Pierre Serre, *A Course in Arithmetic*, Springer GTM 7 (1973), DOI `10.1007/978-1-4684-9884-4`, https://doi.org/10.1007/978-1-4684-9884-4, Chapter III **Theorems 2–4**; J. S. Milne, *Arithmetic Duality Theorems*, 2nd ed. (2006), author edition https://www.jmilne.org/math/Books/ADTnot.pdf, **Theorem I.4.10**. Source type: authoritative monographs. Conditional assumption: Poitou–Tate use requires a genuine fixed global finite module and exact local conditions.

Repo provenance: source PR `1664`; exact source head `25229e7b0dfbbc5524266ce49e8edaf217841701`; source/certificate `stages/stage36/36-09Y/kummer-complement-prime-2adic-hilbert-preflight.json`, blob `20c6d782e59bff820392731ec81653d15b2d1921`; verifier `stages/stage36/verify_stage36_36_09Y.py`, blob `63b4cc43e91c18a8ff295b288995e23395de8539`; quadratic-character source-lock `stages/stage36/36-09X/quadratic-character-supplement-source-lock.md`, blob `89f3847397b5a2b8e4df2fb4762a3dfb5f362616`.

The global-localization adapter is missing. Therefore `LOCAL_GLOBAL_OBSTRUCTION_INCREMENT=0` and the global terminal remains a research gap.

## S30-W01 — PROVISIONAL_LITERATURE_EXTENSION_FROM_STAGE36

**Classification:** EXTEND_OLDER_EXISTING. No new Stage36 ID.

Contract: source-labelled finite kernels with exact form/radical -> compute radical, nondegenerate quotient and Arf/Witt-type structural invariants -> use structural compression only where the **actual source acting subgroup** realizes the theorem equivalence; keep base-field and extension-field orbit relations separate.

DO_NOT_USE_FOR: replacing source-labelled orbits by full `O/Sp` orbits without subgroup proof; semantic kernel identity from abstract type; creating a second transvection weapon. Transvection pruning remains `S32-PW06`.

Literature: Cahit Arf, “Untersuchungen über quadratische Formen in Körpern der Charakteristik 2. I”, *J. reine angew. Math.* 183 (1941), 148–167, DOI `10.1515/crll.1941.183.148`, https://doi.org/10.1515/crll.1941.183.148; Donald E. Taylor, *The Geometry of the Classical Groups*, Heldermann (1992), **Theorem 8.5** for symplectic generation by transvections. The Arf paper is a structural source anchor; exact internal classification locator is not promoted beyond what Phase 3 froze. Source types: original peer-reviewed paper; authoritative monograph.

Repo provenance: Stage36 candidate `DISC-S36-B01`; source PR `1541`; exact source head `3a78f9ff156b53f509625d353df48d1b3e02b836`; source/certificate `stages/stage36/36-02/representative-inventory.json`, blob `88130b9380a677a191f91c24df87618e65be0a2f`; verifier `stages/stage36/verify_stage36_36_02_audited.py`, blob `97dd2e3834365e8b013f9ff076b1b05595362aee`.

## S31-W01 — PROVISIONAL_LITERATURE_EXTENSION_FROM_STAGE36

**Classification:** EXTEND_OLDER_EXISTING. No new Stage36 ID.

Contract: exact successive double covers -> exact branch/discriminant data -> generic genus layer-by-layer by standard cover theory/Riemann–Hurwitz -> separate degenerations -> route the first genus-one layer to the existing S31-W01 birational adapter. No point-set conclusion follows from genus alone.

Literature: Rita Pardini, “Abelian covers of algebraic varieties”, *J. reine angew. Math.* 417 (1991), 191–214, DOI `10.1515/crll.1991.417.191`, https://doi.org/10.1515/crll.1991.417.191, **Theorem 2.1** building-data framework; ordinary Riemann–Hurwitz supplies the curve-genus computation. Source type: original peer-reviewed paper.

Repo provenance: Stage36 candidate `DISC-S36-B08`; source PR `1624`; exact source head `6ede28751914a881a5ddaca7691538a8a3e4780c`; source/certificate `stages/stage36/36-09J/reciprocal-involution-two-linear-cover-preflight.json`, blob `72e9ca86f726f2ff286c983138d9381acdd97e62`; verifier `stages/stage36/verify_stage36_36_09J.py`, blob `b5357a344ffab51118f4f1ec92904367c79c6541`.

## S34-W02 — PROVISIONAL_LITERATURE_EXTENSION_FROM_STAGE36

**Classification:** EXTEND_OLDER_EXISTING. No new Stage36 ID.

Contract: elliptic family + certified generic MW subgroup/torsion + exact receiver predicate -> exhaust specialized generic subgroup against the receiver -> if no member is compatible, any compatible specialization must arise from separately classified rank, saturation/index or torsion enlargement; rank-jump theorems may characterize a growth locus only after exact family hypotheses pass.

DO_NOT_USE_FOR: empty growth locus; receiver existence from growth; full MW group from generic subgroup; collapsing all enlargement to rank.

Literature: Silverman 1983, DOI `10.1515/crll.1983.342.197`, **Theorem C**; Loughran–Salgado 2022, DOI `10.5802/aif.3457`, **Theorems 1.1 and 1.2**. Conditional assumption: Loughran–Salgado is inactive until the exact Stage36 family satisfies one theorem's hypotheses.

Repo provenance: Stage36 candidate `DISC-S36-B12`; source PR `1655`; exact source head `f48184e2ab7fabe6fd07b553aa1cda507874569d`; source/certificate `stages/stage36/36-09R/etau-rankjump-receiver-esigmatau-growth-preflight.json`, blob `b55d042ede01032ff8c8b0d872510a53cb857969`; verifier `stages/stage36/verify_stage36_36_09R.py`, blob `62707dc5126e9ea6caad5fd41834cab488b29945`; specialization source-lock `stages/stage36/36-09N/relative-2isogeny-specialization-source-lock.md`, blob `a562d7053a6f04deff4473067777b7cfd538ea8a`.

## S36-PW01 — SOURCE_ANCHOR_ONLY

No mathematical output increment. Pardini 1991, **Theorem 2.1**, DOI `10.1515/crll.1991.417.191`, supplies a standard abelian-cover building-data envelope; Stage36 remains responsible for exact deck-character labels, complete inertia including infinity, generic-open separation and deterministic quotient inventory.

Repo provenance: source PR `1590`; exact source head `f22d67dda4183c3bfd39710ebb4083f5185f3f49`; source/certificate `stages/stage36/36-09D/q-defined-pencil-fibration-preflight.json`, blob `7fb67b8bf5a37d16ef527aea6109eb0782d61201`; verifier `stages/stage36/verify_stage36_36_09D_audited.py`, blob `062b61e2625a5643e66523e829beb6a29e78d85e`.

## S36-PW05 — SOURCE_ANCHOR_ONLY

No mathematical output increment. Michael Stoll, “Descent on elliptic curves”, *Panoramas et Synthèses* 36 (2012), 151–179; author manuscript https://arxiv.org/abs/math/0611694, supplies standard Kummer/descent context. `Miller–Stoll 2013` is **NOT_APPLICABLE** as the direct source for this 2-isogeny normalization because its principal prime-degree setup is for `l>3`.

Repo provenance: source PR `1632`; exact source head `98d057a47fc37a897fb14e904cdf9d52913f082b`; source/certificate `stages/stage36/36-09L/physical-base-full2-descent-preflight.json`, blob `56fd432a3ae6046bc4643b56bf562660af49fe89`; verifier `stages/stage36/verify_stage36_36_09L.py`, blob `d59215520dd5c5ef265672b60681df65ef7b0292`.

## LIT-WF02 GLOBAL_H1_LOCALIZATION_RECIPROCITY_APPLICABILITY_WORKFLOW

**Maturity recommendation:** PROVISIONAL. **Kind:** workflow, not a theorem or selector.

Reusable workflow contract:

```text
repo local rows/charts
-> identify a single fixed global H1/Kummer module/class system
-> prove every retained local row/chart is its exact localization/evaluation
-> certify field, support, dyadic, real and exceptional-place normalization
-> bind the exact literature theorem inputs
-> emit PASS typed global-local package or FAIL_CLOSED with the first missing obligation
```

HYPOTHESES: named global finite module/class; exact localization maps; complete relevant-place panel; source-bound local rows; field-change semantics explicit. APPLICABILITY: any repo branch attempting to upgrade local character/Kummer data to reciprocity, Selmer or global-duality input. DO_NOT_USE_FOR: constructing a missing global class; treating Hilbert reciprocity as a contradiction; converting local admissibility into a rational point; granting theorem/receiver/endpoint credit.

Literature anchors: Serre, *A Course in Arithmetic*, Chapter III Theorems 2–4, DOI `10.1007/978-1-4684-9884-4`; Milne, *Arithmetic Duality Theorems*, Theorem I.4.10, https://www.jmilne.org/math/Books/ADTnot.pdf; standard Kummer/Selmer local-condition semantics as routed through existing provisional `LIT-PW03`.

Stage36 seed input: `S36-PW04` chart tuple and `S36-PW07` local-character matrix. Repo adapter output is only a typed theorem-input package. Adapter source/verifier: **not yet present**; the workflow itself is the fail-closed applicability procedure and carries zero mathematical credit.

## Rejected duplicates and research gap

No new literature weapon is created.

- reciprocal methods -> `S35-PW02/PW03/PW04` (and `S31-W01` when genus-one birationality is the actual interface)
- finite-prime Weil completion -> `S35-PW05`
- transvection/symplectic pruning -> `S32-PW06`
- finite-group reconstruction -> `S30-W01/S32-PW05`
- MW/local sieve -> `S34-W02/LIT-PW01/LIT-PW02`
- factor/squareclass linearization -> `S34-W01/S35-PW01`
- Gaussian/norm lineage -> Stage14 `AR-017/AR-018` plus Stage35 extensions

`GLOBAL-HILBERT-SELMER-COMPATIBILITY-TERMINAL` remains **RESEARCH_GAP**. Required missing adapter: `DYNAMIC_RESERVOIR_ROWS_TO_GLOBAL_KUMMER_LOCALIZATION_SYSTEM`. No `POSSIBLY_NOVEL` item is activated; the Phase3 novelty flag list is empty.
