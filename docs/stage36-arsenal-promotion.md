# Stage36 Arsenal initial provisional harvest promotion

**PROVISIONAL ONLY — active Stage36 MAIN/controller/source-lock authority is higher.**

```text
SOURCE_STAGE=Stage36
INITIAL_HARVEST=true
DISCOVERY_PR=1673
DISCOVERY_EXACT_HEAD=0ad4a2fc78ebd3ee55c47d9bf5100d8e4cee3b66
IMPLEMENTATION_PR=1675
IMPLEMENTATION_BRANCH=stage36-arsenal-initial-provisional-harvest-promotion
STAGE36_CANONICAL_INCEPTION=62c26297ebeb159e9cdd1e6b9c2129dff6a4acdc
HARVEST_LOWER_BOUND=62c26297ebeb159e9cdd1e6b9c2129dff6a4acdc
HARVEST_UPPER_BOUND=07a465cb5025e7c0188fb63610bb40e4b54e7a84
RANGE_EXPANDED_AFTER_HARVEST1=false
INSPECTED_SCOPE=exactly the 36 Harvest1 candidates; PR #1670 / 36-09AB and later main movement excluded
ARSENAL_REGISTRATION_DOES_NOT_CHANGE_STAGE36_MATHEMATICAL_AUTHORITY=true
STAGE36_MATHEMATICAL_CREDIT_CHANGE=0
```

This document is the authoritative source for the Stage36 initial PROVISIONAL Arsenal harvest. It registers only Harvest3-accepted reusable contracts. It does not alter Stage36 progress, MAIN authority, current route, receiver closure, rank proof, Mordell–Weil closure, Hilbert-reciprocity endpoint credit, local-global obstruction credit, theorem closure, Stage36 closure/release, or any perfect-cuboid existence/nonexistence claim.

## Harvest 3 classification frozen for implementation

- NEW_WEAPON: DISC-S36-A01, DISC-S36-A05, DISC-S36-A06, DISC-S36-B03, DISC-S36-B10, DISC-S36-B11, DISC-S36-B14
- EXTEND_EXISTING: DISC-S36-B01, DISC-S36-B02, DISC-S36-B04, DISC-S36-B08, DISC-S36-B12
- NEW_WORKFLOW: none
- HISTORICAL_OR_NEGATIVE: DISC-S36-B07, DISC-S36-E01, DISC-S36-E02, DISC-S36-E03, DISC-S36-E04, DISC-S36-E05, DISC-S36-E06, DISC-S36-E07, DISC-S36-E08, DISC-S36-E09, DISC-S36-F01
- STAGE36_SPECIFIC: DISC-S36-D01, DISC-S36-D02
- REJECT_DUPLICATE: DISC-S36-A02, DISC-S36-A03, DISC-S36-A04, DISC-S36-A07, DISC-S36-B05, DISC-S36-B06, DISC-S36-B09, DISC-S36-B13, DISC-S36-C01, DISC-S36-C02, DISC-S36-C03

## S36-PW01 ELEMENTARY_ABELIAN_COVER_CHARACTER_QUOTIENT_GENUS_INVENTORY

**Maturity:** PROVISIONAL

**Kind:** weapon

**Harvest candidate:** `DISC-S36-A01`

Reusable contract:

```text
connected elementary-2 cover of a rational base + complete exact branch/inertia marking -> enumerate every nontrivial character quotient -> compute exact branch support/genus/invariants by inertia pairing and Riemann-Hurwitz -> complete structural quotient inventory on the audited generic open
```

**HYPOTHESES**

- characteristic != 2
- finite elementary abelian deck group
- connected source cover
- complete inertia including infinity
- branch collisions/singular parameter strata separated

**APPLICABILITY:** elementary-2 covers/fibrations where character-by-character quotient geometry must be inventoried before arithmetic closure

**DO_NOT_USE_FOR**

- rational-point classification
- Mordell-Weil computation
- receiver closure
- transferring Stage36 quotient counts

**Field restrictions:** marked cover/action must be defined over the working field; base change may increase rational quotient data and gives no descent of extension-field points

**Exceptional locus:** branch-collision, singular, disconnected and special-parameter strata are separate

**Forward/converse status:** structural forward construction only; no source-point converse

Source lock:

```text
source_pr=1590
source_exact_head=f22d67dda4183c3bfd39710ebb4083f5185f3f49
authoritative_source=stages/stage36/36-09D/q-defined-pencil-fibration-preflight.json
authoritative_source_blob_sha=7fb67b8bf5a37d16ef527aea6109eb0782d61201
certificate=stages/stage36/36-09D/q-defined-pencil-fibration-preflight.json
certificate_blob_sha=7fb67b8bf5a37d16ef527aea6109eb0782d61201
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_09D_audited.py
verifier_blob_sha=062b61e2625a5643e66523e829beb6a29e78d85e
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock=null
```

**Nearest existing card:** S30-W01, S31-W01

**Distinction:** S30-W01 identifies concrete finite actions but does not output the complete character-quotient branch/genus inventory of a marked elementary-2 cover; S31-W01 begins only after a genus-one quotient model is selected.

## S36-PW02 V4_CURVE_JACOBIAN_QUOTIENT_DECOMPOSITION

**Maturity:** PROVISIONAL

**Kind:** weapon

**Harvest candidate:** `DISC-S36-A05`

Reusable contract:

```text
smooth curve + exact faithful V4 action/maps + Kani-Rosen hypotheses + differential independence -> construct three involution quotients -> certify product map -> Jacobian isogeny decomposition into quotient Jacobians
```

**HYPOTHESES**

- compatible characteristic
- smooth retained source fiber
- exact three involutions and quotient maps
- quotient/full-group genera established
- Kani-Rosen hypotheses
- differential or equivalent independence certification

**APPLICABILITY:** curves with exact Klein-four symmetry where Jacobian decomposition routes arithmetic to lower-genus quotient factors

**DO_NOT_USE_FOR**

- pointwise source reconstruction
- source rational-point classification
- quotient rank determination
- combining arbitrary quotient points into a source point

**Field restrictions:** exact V4 action/maps and theorem hypotheses must hold over the stated field; base change may rationalize factors/points without giving source-point descent

**Exceptional locus:** singular source fibers, quotient-map degenerations and genus-pattern changes

**Forward/converse status:** structural isogeny decomposition, not an iff rational-point adapter

Source lock:

```text
source_pr=1642
source_exact_head=be979251c6e3d7a2431fb56537520afd2596c7d9
authoritative_source=stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json
authoritative_source_blob_sha=6a2678ebedba40e13277100441361039ee47ca28
certificate=stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json
certificate_blob_sha=6a2678ebedba40e13277100441361039ee47ca28
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_09O.py
verifier_blob_sha=ed0ae786505e3443226eaed6e61b7c78ee389191
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock={"blob_sha":"5b5957843933b487bb9cae3acd22bb7737f37392","path":"stages/stage36/36-09O/kani-rosen-v4-jacobian-source-lock.md"}
```

**Nearest existing card:** S31-W01, S34-W03

**Distinction:** S31-W01 is one genus-one birational adapter and S34-W03 is receiver-intersection exclusion; neither constructs a V4/Kani-Rosen Jacobian decomposition nor certifies quotient-factor independence.

## S36-PW03 QUADRATIC_EXTENSION_ANTIINVARIANT_TWIST_DESCENT_GROWTH_GATE

**Maturity:** PROVISIONAL

**Kind:** weapon

**Harvest candidate:** `DISC-S36-A06`

Reusable contract:

```text
elliptic curve/twist + explicit quadratic-extension isomorphism/Galois action + source-locked generic MW/Kummer baseline + receiver-forced independent anti-invariant extension direction -> decompose MW eigenspaces -> identify anti-invariant direction with a base-field twist point -> necessary twist rank/Kummer-image growth obligation
```

**HYPOTHESES**

- characteristic != 2
- explicit quadratic extension and twist isomorphism
- Galois action checked
- generic rank/Kummer baseline source-locked
- receiver implication supplies an independent anti-invariant direction

**APPLICABILITY:** quadratic-twist receiver problems where arithmetic evidence appears over a quadratic extension and must be translated to a base-field necessary condition

**DO_NOT_USE_FOR**

- receiver existence from rank growth
- receiver emptiness from missing known points
- full MW group from a rank-jump witness
- descent of arbitrary extension points

**Field restrictions:** quadratic L/K with explicit twist descent; new L-points do not automatically descend to E(K)

**Exceptional locus:** singular twists, torsion-only/degenerate fibers, bad specializations and receiver boundaries without certified independence

**Forward/converse status:** necessary-condition gate only; no converse from growth to receiver compatibility

Source lock:

```text
source_pr=1664
source_exact_head=25229e7b0dfbbc5524266ce49e8edaf217841701
authoritative_source=stages/stage36/36-09U/qi-antiinvariant-rankjump-descent-preflight.json
authoritative_source_blob_sha=a1f0c924d267ab4f45aaada6c9bcb3a5f544f284
certificate=stages/stage36/36-09U/qi-antiinvariant-rankjump-descent-preflight.json
certificate_blob_sha=a1f0c924d267ab4f45aaada6c9bcb3a5f544f284
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_09U.py
verifier_blob_sha=21b3b1461195cfae1a1294832f8e77f09a09983b
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock={"blob_sha":"a562d7053a6f04deff4473067777b7cfd538ea8a","path":"stages/stage36/36-09N/relative-2isogeny-specialization-source-lock.md"}
```

**Nearest existing card:** S30-W02, S34-W02

**Distinction:** S30-W02 is finite-action semilinear descent, not MW eigenspace/twist arithmetic. S34-W02 consumes a certified fixed-curve MW group for congruence exclusion and does not produce this family-level twist-growth gate.

## S36-PW04 POINTWISE_ELEMENTARY_2_TORSOR_LIFT_CLASS_CHART_ADAPTER

**Maturity:** PROVISIONAL

**Kind:** weapon

**Harvest candidate:** `DISC-S36-B03`

Reusable contract:

```text
finite elementary-2 torsor quotient + exact dual-character basis/charts and source open -> choose canonical nonvanishing charts -> evaluate pointwise H1 squareclass tuple -> materialize independent square-root fiber equations -> rational source fiber nonempty iff the pointwise class is trivial
```

**HYPOTHESES**

- characteristic != 2
- finite elementary abelian torsor and basis exact
- complete dual pairing
- chart supports avoid forbidden zero strata
- transition ratios invariant squares
- source open preserved by rational lifting

**APPLICABILITY:** elementary-2/sign-cover quotient receivers whose rational lift obstruction is several point-dependent squareclasses with possibly moving prime support

**DO_NOT_USE_FOR**

- fixed finite global twist-family credit
- quotient rational-point classification
- cohomological naming without character functions
- marked Brauer/H2(mu2) binding

**Field restrictions:** squareclasses may trivialize after extension; extension-field triviality does not imply base-field lift

**Exceptional locus:** forbidden zero strata, chart denominators, source boundary and unaudited quotient singularities

**Forward/converse status:** iff pointwise rational-lift adapter on the chart-covered open

Source lock:

```text
source_pr=1560
source_exact_head=dcdae282120f29a42679b654e21bd35f843e4cbf
authoritative_source=stages/stage36/36-04/h-torsor-lift-class.json
authoritative_source_blob_sha=a06e201a9b554da71c5e75d8f8541e7284f8d020
certificate=stages/stage36/36-04/h-torsor-lift-class.json
certificate_blob_sha=a06e201a9b554da71c5e75d8f8541e7284f8d020
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_04.py
verifier_blob_sha=35d288d8a18adee95830caa6ee9d6b0d8ebe9e53
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock=null
```

**Nearest existing card:** S35-PW03, S33-PW09

**Distinction:** S35-PW03 gives algebraic rational-source lift-square normalization but not finite-H dual-character/chart construction of a pointwise H1 torsor class. S33-PW09 binds marked Brauer/H2(mu2) data and has different objects/semantics.

## S36-PW05 SPLIT_FULL2_ORDER4_HALF_AND_2ISOGENY_NORMALIZATION

**Maturity:** PROVISIONAL

**Kind:** weapon

**Harvest candidate:** `DISC-S36-B10`

Reusable contract:

```text
elliptic curve y^2=x(x+a^2)(x+b^2) with chosen rational 2-torsion kernel -> construct (ab,ab(a+b)) -> verify doubling to the kernel point -> form standard 2-isogenous quotient/open map -> certified uniform order-4 subgroup plus normalized 2-isogeny interface
```

**HYPOTHESES**

- characteristic != 2
- a,b nonzero
- roots distinct
- chosen 2-torsion kernel rational
- split-square root-difference presentation exact

**APPLICABILITY:** split-full-2 elliptic families requiring a uniform order-4 half and explicit 2-isogeny normalization before descent

**DO_NOT_USE_FOR**

- full torsion subgroup
- absence of order 8 without a separate halving gate
- Selmer group
- Mordell-Weil group
- receiver closure

**Field restrictions:** a,b and chosen kernel must be rational over the base; higher 2-power divisibility may increase after extension

**Exceptional locus:** root collisions, zero a/b, degenerate half and affine isogeny denominators

**Forward/converse status:** explicit construction; standard isogeny-level finite-kernel relation only, not pointwise receiver equivalence

Source lock:

```text
source_pr=1632
source_exact_head=98d057a47fc37a897fb14e904cdf9d52913f082b
authoritative_source=stages/stage36/36-09L/physical-base-full2-descent-preflight.json
authoritative_source_blob_sha=56fd432a3ae6046bc4643b56bf562660af49fe89
certificate=stages/stage36/36-09L/physical-base-full2-descent-preflight.json
certificate_blob_sha=56fd432a3ae6046bc4643b56bf562660af49fe89
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_09L.py
verifier_blob_sha=d59215520dd5c5ef265672b60681df65ef7b0292
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock=null
```

**Nearest existing card:** S31-W01, S34-W02

**Distinction:** Neither existing card supplies split-full-2 root-difference normalization, the explicit uniform order-4 half or the 2-isogeny construction; the Stage36 source itself records no existing formal card for this interface.

## S36-PW06 RELATIVE_2ISOGENY_KUMMER_SPECIALIZATION_BASELINE

**Maturity:** PROVISIONAL

**Kind:** weapon

**Harvest candidate:** `DISC-S36-B11`

Reusable contract:

```text
explicit 2-isogenous elliptic family over a rational function field + visible generic Kummer classes/sections + one injective specialization + complete fixed-fiber 2-isogeny descent -> pin specialized Kummer images -> bound generic rank by injectivity -> combine visible lower bounds and isogeny index formula -> exact generic rank/Kummer baseline
```

**HYPOTHESES**

- exact isogenous pair and Kummer maps
- visible generic sections/classes
- proved specialization injectivity criterion
- complete fixed-fiber isogeny descent
- torsion/nontorsion certified

**APPLICABILITY:** elliptic families where an exact generic rank/Kummer baseline is needed before exceptional specialization growth analysis

**DO_NOT_USE_FOR**

- uniform rank of all fibers
- exclusion of rank jumps
- full generic MW group unless separately proved
- receiver closure

**Field restrictions:** function-field family with specialization to the base field; rank/Kummer images can increase under specialization or extension

**Exceptional locus:** singular fibers, bad specializations and injectivity-criterion failures

**Forward/converse status:** generic arithmetic baseline method; no pointwise source converse and no converse from one specialization

Source lock:

```text
source_pr=1640
source_exact_head=8ca23e42a057af260c7051c20dd8f608067efefd
authoritative_source=stages/stage36/36-09N/relative-2isogeny-kummer-image-rank1-preflight.json
authoritative_source_blob_sha=02a14439d94d7f6e5ac2f65e995e8acfb6845788
certificate=stages/stage36/36-09N/relative-2isogeny-kummer-image-rank1-preflight.json
certificate_blob_sha=02a14439d94d7f6e5ac2f65e995e8acfb6845788
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_09N.py
verifier_blob_sha=e7effbe9ee6106505db013f326ec653627885054
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock={"harvest_upper_corrected_blob_sha":"a562d7053a6f04deff4473067777b7cfd538ea8a","path":"stages/stage36/36-09N/relative-2isogeny-specialization-source-lock.md","source_head_blob_sha":"e7c98981fbb1d523fd7db54478dc09aa87b547e8"}
```

**Nearest existing card:** S34-W02, S31-WF01, S31-W01

**Distinction:** S34-W02 assumes a certified full MW group for a fixed quotient, while S31-WF01 governs MW proof semantics; neither derives exact generic rank and Kummer images for a family from one injective specialization plus complete fixed-fiber isogeny descent.

## S36-PW07 DIRECTIONAL_PRIME_RESERVOIR_LOCAL_CHARACTER_MATRIX

**Maturity:** PROVISIONAL

**Kind:** weapon

**Harvest candidate:** `DISC-S36-B14`

Reusable contract:

```text
source-derived coprime prime reservoirs + selected Kummer/isogeny squareclasses + exact local cover equations -> partition support by reservoir/direction -> derive self-prime, cross-prime, dyadic and real quadratic-character/Hilbert conditions -> complete local necessary-condition matrix including automatic rows and explicit locally admissible classes
```

**HYPOTHESES**

- exact primitive reservoir factorization and odd disjointness
- selected Kummer classes with controlled support
- exact local covers
- self/cross-prime reductions proved
- 2-adic and real cases handled separately

**APPLICABILITY:** dynamic-support descent systems with several source-derived prime reservoirs and class-dependent local solvability

**DO_NOT_USE_FOR**

- global rational points
- Selmer membership from local admissibility
- receiver emptiness
- finite exceptional-prime classification
- fixed finite squareclass family
- calling standard Hilbert reciprocity new mathematics

**Field restrictions:** source reservoirs and local rows are tied to the stated global field/completions; prime splitting and squareclasses can change after extension

**Exceptional locus:** prime 2, infinity, shared/forbidden support boundaries, zero factors and bad reduction are explicit separate cases

**Forward/converse status:** place-by-place iff only where proved; globally the matrix is a necessary-condition interface

Source lock:

```text
source_pr=1664
source_exact_head=25229e7b0dfbbc5524266ce49e8edaf217841701
authoritative_source=stages/stage36/36-09Y/kummer-complement-prime-2adic-hilbert-preflight.json
authoritative_source_blob_sha=20c6d782e59bff820392731ec81653d15b2d1921
certificate=stages/stage36/36-09Y/kummer-complement-prime-2adic-hilbert-preflight.json
certificate_blob_sha=20c6d782e59bff820392731ec81653d15b2d1921
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_09Y.py
verifier_blob_sha=63b4cc43e91c18a8ff295b288995e23395de8539
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock={"blob_sha":"89f3847397b5a2b8e4df2fb4762a3dfb5f362616","path":"stages/stage36/36-09X/quadratic-character-supplement-source-lock.md"}
```

**Nearest existing card:** S35-PW01, S35-PW05, S33-PW07

**Distinction:** S35-PW01 solves a global parametric squareclass graph but not place-by-place local rows. S35-PW05 produces a finite all-prime exceptional set by census+Weil, while this contract allows unbounded reservoirs and stops at a local matrix. S33-PW07 supplies torsor/Brauer semantics, not reservoir-to-local-character construction.

## PROVISIONAL extensions to existing IDs

### DISC-S36-B01 -> S30-W01 — S30-W01_FIELD_SEPARATED_KERNEL_INVARIANT_INVENTORY_EXTENSION

**Maturity:** PROVISIONAL extension; no new stable ID.

Reusable contract: complete finite source-labelled population under exact symmetry -> compute source-defined kernels plus stabilizer/radical/squareclass-rank/orbit metadata -> canonicalize deterministically -> repeat after an explicit field extension while keeping base-field and extension-field equivalence relations separate

HYPOTHESES: complete finite population; exact symmetry action/canonicalization; source-derived kernel semantics; exact stabilizer/radical/squareclass invariants; base and extension equivalence relations not conflated

APPLICABILITY: extension of S30-W01 for finite kernel inventories carrying arithmetic invariants and field-change bookkeeping

DO_NOT_USE_FOR: arithmetic existence/nonexistence; semantic kernel identity from abstract group type; descending extension-field orbit mergers; transferring Stage36 counts

Field restrictions: extension can merge orbits/add symmetries without implying base-field equivalence

Exceptional locus: degenerate/radical kernel types remain explicit inventory strata

Forward/converse status: complete finite classification only for the exact enumerated population

```text
source_pr=1541
source_exact_head=3a78f9ff156b53f509625d353df48d1b3e02b836
authoritative_source=stages/stage36/36-02/representative-inventory.json
authoritative_source_blob_sha=88130b9380a677a191f91c24df87618e65be0a2f
certificate=stages/stage36/36-02/representative-inventory.json
certificate_blob_sha=88130b9380a677a191f91c24df87618e65be0a2f
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_02_audited.py
verifier_blob_sha=97dd2e3834365e8b013f9ff076b1b05595362aee
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock=null
```

Nearest existing card: S30-W01, S30-W02

Distinction: The finite reconstruction, symmetry quotient, kernel/image/stabilizer checks and canonicalization already belong to S30-W01. Stage36 adds field-separated radical/squareclass-rank/orbit-degree metadata but no independent terminal operation, so S30-W01 should be strengthened rather than duplicated.

### DISC-S36-B02 -> S35-PW02 — S35-PW02_ONE_WAY_BOUNDARY_PREFLIGHT_EXTENSION

**Maturity:** PROVISIONAL extension; no new stable ID.

Reusable contract: distinguished source open/population + exact finite quotient + classified branch/exceptional divisor -> certify exact one-way source-to-quotient push and boundary dictionary -> withhold quotient-to-source/receiver-equivalence credit until a separate lift class or converse reconstruction exists

HYPOTHESES: exact source and quotient opens; finite quotient defined on retained locus; branch/exceptional strata classified; distinguished arithmetic population separated from ambient geometric open

APPLICABILITY: preflight for S35-PW02 when the forward quotient is certified but converse lift remains separate

DO_NOT_USE_FOR: quotient Q-point => source Q-point; ambient-open population => distinguished source population; receiver emptiness from boundary classification

Field restrictions: extra quotient points or split boundaries after base change do not imply base-field source lifts

Exceptional locus: branch divisor, quotient singularities/resolution exceptions and source boundaries

Forward/converse status: one-way source-to-quotient push; converse explicitly unavailable until separately proved

```text
source_pr=1553
source_exact_head=5fd7af75ede4cd2eceb70f9f21bd2b98ec5453a6
authoritative_source=stages/stage36/36-03/physical-open-boundary.json
authoritative_source_blob_sha=fc1947b2de08f7d8a104bdc91902b20e88635349
certificate=stages/stage36/36-03/physical-open-boundary.json
certificate_blob_sha=fc1947b2de08f7d8a104bdc91902b20e88635349
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_03_audited.py
verifier_blob_sha=56dcab68f90ae3a21e6f1716c3f79f4e17c7e391
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock=null
```

Nearest existing card: S35-PW02, S30-WF03

Distinction: S35-PW02 already owns exact full-receiver involution quotient plus converse reconstruction. Stage36 adds a reusable fail-closed intermediate state: forward population push and full boundary audit with converse credit deliberately withheld.

### DISC-S36-B04 -> S34-W03 — S34-W03_PROOF_CAPABILITY_PREFLIGHT_EXTENSION

**Maturity:** PROVISIONAL extension; no new stable ID.

Reusable contract: exact receiver K + proposed auxiliary branch B -> before S34-W03, certify that B is genuinely information-reducing, exhaustive for the target population and equipped with an exact proof-capable joint B+K test -> otherwise fail closed on that proposed B only

HYPOTHESES: receiver K exact; B source-derived and exhaustive; B not merely original lift equations renamed; joint B+K test proof-capable; boundary/degenerate strata included

APPLICABILITY: branch-selection preflight for S34-W03

DO_NOT_USE_FOR: claiming S34-W03 globally unavailable from one failed B; receiver closure; restating source equations as a new branch

Field restrictions: same field/population as the proposed S34-W03 application; extension-field tests do not close a base-field receiver without exact population implication

Exceptional locus: boundary handling is part of the proof-capability check

Forward/converse status: applicability/preflight gate only; no closure by itself

```text
source_pr=1584
source_exact_head=fd7b5d9dfef272bee2b6676797e6d12d8b07bde0
authoritative_source=stages/stage36/36-09B/receiver-restricted-branch-intersection-preflight.json
authoritative_source_blob_sha=da9143e587506522ed966d380d9980ff1875db0d
certificate=stages/stage36/36-09B/receiver-restricted-branch-intersection-preflight.json
certificate_blob_sha=da9143e587506522ed966d380d9980ff1875db0d
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_09B_audited.py
verifier_blob_sha=ed2be37b568120b7b7d7a7f3cfbd6d16243366d5
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock=null
```

Nearest existing card: S34-W03

Distinction: The candidate changes no mathematical output beyond S34-W03. It tightens S34-W03 applicability by rejecting vacuous/non-proof-capable auxiliary branches, so it is an extension rather than a new workflow ID.

### DISC-S36-B08 -> S31-W01 — S31-W01_SUCCESSIVE_COVER_GENUS_PREFLIGHT_EXTENSION

**Maturity:** PROVISIONAL extension; no new stable ID.

Reusable contract: receiver reconstructed by successive quadratic covers -> compute exact branch divisors/discriminants and generic genus layer-by-layer -> separate degeneration parameters -> route the first genus-one layer to an exact S31-W01 birational adapter when available

HYPOTHESES: exact successive-cover equations; branch/discriminant data computable; generic smoothness; degenerate parameter strata separated

APPLICABILITY: preflight before genus-one quartic/elliptic routing in reconstruction towers

DO_NOT_USE_FOR: rational-point classification from genus; automatic elliptic birational map; generic genus as classification of degenerate fibers

Field restrictions: geometric genus survives separable base change; rationality of branch/quotient points may increase without descent

Exceptional locus: discriminant-zero parameters, branch collisions and reconstruction boundaries

Forward/converse status: forward structural tower/genus audit; no point converse/completeness

```text
source_pr=1624
source_exact_head=6ede28751914a881a5ddaca7691538a8a3e4780c
authoritative_source=stages/stage36/36-09J/reciprocal-involution-two-linear-cover-preflight.json
authoritative_source_blob_sha=72e9ca86f726f2ff286c983138d9381acdd97e62
certificate=stages/stage36/36-09J/reciprocal-involution-two-linear-cover-preflight.json
certificate_blob_sha=72e9ca86f726f2ff286c983138d9381acdd97e62
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_09J.py
verifier_blob_sha=b5357a344ffab51118f4f1ec92904367c79c6541
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock=null
```

Nearest existing card: S31-W01

Distinction: The terminal reusable operation remains S31-W01 once a genus-one layer is reached. Stage36 supplies an upstream exact cover-tower/genus/degeneration preflight, not a second birational-adapter species.

### DISC-S36-B12 -> S34-W02 — S34-W02_GENERIC_SUBGROUP_SPECIALIZATION_GROWTH_PREFLIGHT_EXTENSION

**Maturity:** PROVISIONAL extension; no new stable ID.

Reusable contract: elliptic family + certified generic MW subgroup/torsion + exact receiver predicate -> specialize and exhaustively test the generic subgroup against the receiver -> if none is compatible, every compatible specialization must arise from separately classified enlargement: rank, saturation/index or torsion growth

HYPOTHESES: generic subgroup/torsion proved to claimed level; all relevant specialized generic points checked; receiver adapter exact; bad/boundary specializations classified; growth species not collapsed to rank only

APPLICABILITY: family-level preflight before MW-based exclusion of exceptional specialization growth

DO_NOT_USE_FOR: empty growth locus; receiver existence from growth; full MW group from generic subgroup; ignoring saturation/torsion enlargement

Field restrictions: rank/torsion/saturation can grow after specialization or extension without producing a receiver point

Exceptional locus: bad specializations, boundary generic points and fibers where generic-subgroup comparison is invalid

Forward/converse status: necessary specialization-growth obligation only

```text
source_pr=1655
source_exact_head=f48184e2ab7fabe6fd07b553aa1cda507874569d
authoritative_source=stages/stage36/36-09R/etau-rankjump-receiver-esigmatau-growth-preflight.json
authoritative_source_blob_sha=b55d042ede01032ff8c8b0d872510a53cb857969
certificate=stages/stage36/36-09R/etau-rankjump-receiver-esigmatau-growth-preflight.json
certificate_blob_sha=b55d042ede01032ff8c8b0d872510a53cb857969
certificate_canonical_sha256=null
verifier=stages/stage36/verify_stage36_36_09R.py
verifier_blob_sha=62707dc5126e9ea6caad5fd41834cab488b29945
verifier_ref=07a465cb5025e7c0188fb63610bb40e4b54e7a84
source_lock={"blob_sha":"a562d7053a6f04deff4473067777b7cfd538ea8a","path":"stages/stage36/36-09N/relative-2isogeny-specialization-source-lock.md"}
```

Nearest existing card: S34-W02, S34-W03

Distinction: S34-W02 is downstream global exclusion once a full fixed-fiber MW group is certified. Stage36 adds a family-specialization preflight showing receiver compatibility requires strict enlargement beyond the generic subgroup, but it does not close that growth locus.

## Historical / negative exclusions

- `DISC-S36-B07` — finite no-middle-layer exhaustion only for the enumerated character-linear class; anti-loop evidence, not a positive weapon
- `DISC-S36-E01` — moving specialization support blocks unjustified fixed-S descent
- `DISC-S36-E02` — Brauer route blocked by upstream source-lock gaps; no compatibility theorem
- `DISC-S36-E03` — proposed character receiver is endpoint-equivalent
- `DISC-S36-E04` — arbitrary shared-prime support blocks fixed finite-S inference
- `DISC-S36-E05` — tested multiple-lift route quickly enters high genus but does not prove all multiples impossible
- `DISC-S36-E06` — parameter-only Hilbert product formula is an automatic reciprocity checksum, not a receiver obstruction
- `DISC-S36-E07` — locally admissible Kummer classes block pure-local uniform closure, without global-point credit
- `DISC-S36-E08` — rank-growth witnesses refute an empty rank-jump locus but do not imply receiver compatibility/full MW
- `DISC-S36-E09` — known growth witnesses do not lift, but samples do not prove whole-fiber emptiness
- `DISC-S36-F01` — positive adoption blocked by unresolved hostile verifier-coverage maturity; later user-pass repair is not hostile re-audit credit

## Stage36-specific exclusions

- `DISC-S36-D01` — explicit all-place local points depend essentially on the exact Stage36 receiver/charts
- `DISC-S36-D02` — transfer depends essentially on the concrete Stage36-to-Stage14 parameter/isomorphism and second-Pythagorean locus

## Rejected duplicates

- `DISC-S36-A02` — REJECT_DUPLICATE: source-locus twist absorption is naturally represented by S35-PW03 source-lift square normalization; S31-W01 handles separate model birationality.
- `DISC-S36-A03` — REJECT_DUPLICATE: distinct from S35-PW04 common-factor compression, but abstractly it is the broader S35-PW02 exact full-receiver involution quotient with boundary/fixed-locus audit and converse reconstruction.
- `DISC-S36-A04` — REJECT_DUPLICATE: one rational lift squarefunction is a direct S35-PW03 specialization.
- `DISC-S36-A07` — REJECT_DUPLICATE: same-coordinate second-twist square is missing source-lift square data covered by S35-PW03; S34-W03 covers downstream joint-intersection exclusion.
- `DISC-S36-B05` — REJECT_DUPLICATE: exact F2 row-span/kernel/rank manipulation is ordinary squareclass linear algebra inside S35-PW01/S34-W01.
- `DISC-S36-B06` — REJECT_DUPLICATE: Stage35 already supplied the dynamic-reservoir/fixed-finite-support preflight for S34-W01 and S35-PW01 permits live unbounded reservoirs.
- `DISC-S36-B09` — REJECT_DUPLICATE: exact S31-W01 contract match.
- `DISC-S36-B13` — REJECT_DUPLICATE: complete fixed-auxiliary point sets pulled back to family parameters are S31-W03; torsion species are source-specific side data.
- `DISC-S36-C01` — REJECT_DUPLICATE: S30-WF02 + S30-WF03 already provide immutable replay and credit firewalls.
- `DISC-S36-C02` — REJECT_DUPLICATE: Research OS Cycle Exploration Safety Protocol already provides candidate ledger, breadth triggers, blind rediscovery, Arsenal comparison, anti-loop and parking discipline.
- `DISC-S36-C03` — REJECT_DUPLICATE: Research OS BLIND_REDISCOVERY + S30-WF02 already provide blind/history separation and immutable provenance; Stage36 commit ordering is implementation detail.

## Credit firewall

```text
ARSENAL_REGISTRATION_DOES_NOT_CHANGE_STAGE36_MATHEMATICAL_AUTHORITY=true
STAGE36_PROGRESS_INCREMENT=0
STAGE36_MAIN_AUTHORITY_CHANGE=false
STAGE36_CURRENT_ROUTE_CREDIT_CHANGE=0
RECEIVER_CLOSURE_ADDED=false
RANK_PROOF_ADDED=false
MORDELL_WEIL_CLOSURE_ADDED=false
HILBERT_RECIPROCITY_ENDPOINT_CREDIT_ADDED=false
LOCAL_GLOBAL_OBSTRUCTION_CREDIT_ADDED=false
THEOREM_CLOSURE_ADDED=false
STAGE36_CLOSURE_OR_RELEASE_ADDED=false
PERFECT_CUBOID_EXISTENCE_CLAIM_ADDED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM_ADDED=false
```
