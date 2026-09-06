# Stage36 initial Arsenal harvest — Harvest 1 / Full Discovery

**DISCOVERY_ONLY_NOT_ARSENAL_PROMOTION**

This file is a frozen discovery ledger only. It assigns no stable Arsenal IDs, changes no Stage36 authority, and grants no theorem/receiver/endpoint/perfect-cuboid credit.

## Frozen harvest boundary

- Stage36 canonical inception / lower bound: `62c26297ebeb159e9cdd1e6b9c2129dff6a4acdc` — merge of bootstrap PR #1535, the first authoritative Stage36 introduction on `main`.
- Harvest 1 upper bound: `07a465cb5025e7c0188fb63610bb40e4b54e7a84` — `main` observed at Harvest start. This value is frozen for Harvest 2/3/4.
- Later main movement does not widen this harvest. Open/later PR #1670 (36-09AB) is outside this range.

## Authority snapshot at the upper bound

- `MAIN-START-HERE.md` delegates mutable truth to `MAIN-STATE.json`.
- `MAIN-STATE.json` is at the 36-09AA batch hostile-audit checkpoint; U-AA have hostile-audit PASS provenance in PR #1664 but are not yet promoted in the mutable state at this frozen upper.
- `MAIN-BATCH-HANDOFF.md` is `EMPTY`.
- No separate Stage36 `controller.json` was found by the bounded search; the mutable authority used here is `MAIN-STATE.json`.

## Discovery method

The scan followed `AGENTS.md`: non-recursive Stage36 top-level/one-level indexing, then cluster-by-cluster certificate -> verifier -> source-lock -> hostile-audit provenance. Arsenal lookup was `docs/arsenal/index.json` first, then only semantic near-neighbor cards. Superseded leaves and negative blockers are retained as history but not promoted as positive weapons.

Near-neighbor cards inspected: `S30-W01`, `S30-W02`, `S30-WF02`, `S30-WF03`, `S31-W01`, `S34-W01`, `S34-W02`, `S34-W03`, `S34-WF01`, `S33-PW09`, `S35-PW01`, `S35-PW03`, `S35-PW04`, `S35-PW05`.

## Harvest 1 classification

- Total candidates: **36**
- A probable NEW_WEAPON: **7**
- B probable EXTEND_EXISTING: **14**
- C probable NEW_WORKFLOW: **3**
- D STAGE36_SPECIFIC: **2**
- E HISTORICAL_OR_NEGATIVE: **9**
- F unresolved: **1**

## A. probable NEW_WEAPON

- `DISC-S36-A01` — **ELEMENTARY_ABELIAN_CHARACTER_QUOTIENT_GENUS_INVENTORY** (36-09D). Output: complete genus inventory of every nontrivial character quotient plus exact quotient invariants Nearest: S30-W01, S31-W01.
- `DISC-S36-A02` — **PHYSICAL_LOCUS_TWIST_ABSORPTION_ELLIPTIC_RECEIVER_ADAPTER** (36-09E). Output: source-faithful normalized Legendre/elliptic paired receiver with source-forced twists absorbed Nearest: S31-W01, S35-PW03.
- `DISC-S36-A03` — **RECIPROCAL_INVOLUTION_TWO_LINEAR_RECEIVER_REDUCTION** (36-09I). Output: iff two-linear product-square receiver in X=x+1/x,Z=z+1/z plus X±2,Z±2 reconstruction squares Nearest: S35-PW04, S34-W01, S31-W01.
- `DISC-S36-A04` — **PHYSICAL_SQUARE_LIFT_CRITERION_ON_ELLIPTIC_QUOTIENT** (36-09O). Output: exact iff squareclass criterion (V+rho*U)/(V-rho*U) square for top-cover physical lift Nearest: S35-PW03, S34-W03.
- `DISC-S36-A05` — **V4_GENUS3_JACOBIAN_ELLIPTIC_QUOTIENT_DECOMPOSITION** (36-09O). Output: three explicit genus-one quotients + certified Kani-Rosen Jacobian isogeny, independently checked on differentials Nearest: S31-W01, S34-W03.
- `DISC-S36-A06` — **QUADRATIC_EXTENSION_ANTIINVARIANT_TWIST_DESCENT_RANKJUMP_GATE** (36-09T + 36-09U). Output: anti-invariant extension direction descended to rational twist plus strict rank/Kummer-image growth obligation Nearest: S30-W02, S34-W02.
- `DISC-S36-A07` — **SAME_X_TWIST_PAIR_RECEIVER_PRODUCT_SQUARE_ADAPTER** (36-09AA). Output: iff receiver compatibility by same-x intersection and normalized Z^2=(X^2-1)(X^2-k^4) auxiliary receiver Nearest: S34-W03, S35-PW04.

## B. probable EXTEND_EXISTING

- `DISC-S36-B01` — **FINITE_KERNEL_SQUARECLASS_REPRESENTATIVE_INVENTORY** (36-02). Output: canonical kernels with stabilizer, radical, squareclass rank, orbit multiplicity and quotient degree; Q and Q(i) inventories separate Nearest: S30-W01, S30-W02.
- `DISC-S36-B02` — **PHYSICAL_OPEN_BOUNDARY_AND_ONE_WAY_QUOTIENT_PUSH_ADAPTER** (36-03). Output: stratified boundary certificate and exact one-way U(Q)->U_H(Q) push Nearest: S30-WF03, S34-W03.
- `DISC-S36-B03` — **POINTWISE_FINITE_H_TORSOR_LIFT_CLASS_CHART_ADAPTER** (36-04). Output: canonical chart squareclasses + explicit degree-|H| fiber equations with q_H^-1(P)(Q) nonempty iff delta_H(P)=1 Nearest: S35-PW03, S33-PW09.
- `DISC-S36-B04` — **S34_W03_PROOF_CAPABILITY_PREFLIGHT** (36-09B). Output: fail-closed decision whether genuinely simpler exhaustive B and exact joint B+K test exist before S34-W03 Nearest: S34-W03.
- `DISC-S36-B05` — **CHARACTER_PRODUCT_MATRIX_SUBRECEIVER_REDUCTION** (36-09F + 36-09G). Output: exact F2 row-space/kernel yielding proper intermediate receiver or endpoint-equivalence proof Nearest: S35-PW01, S34-W01.
- `DISC-S36-B06` — **FOUR_FACTOR_CONIC_PRODUCT_SQUARE_PREFLIGHT** (36-09H). Output: primitive four-factor model + valuation-support diagnostic deciding whether S34-W01 finite first layer is legal Nearest: S34-W01.
- `DISC-S36-B07` — **CHARACTER_LINEAR_NO_MIDDLE_LAYER_EXHAUSTION** (36-09I). Output: every legal extra row is redundant or raises to endpoint span, proving no strict intermediate character-linear receiver Nearest: S35-PW01, S34-W01.
- `DISC-S36-B08` — **RECIPROCAL_FIBER_COVER_TOWER_GENUS_STRATIFICATION** (36-09J). Output: certified genus 0->1->3 tower with discriminant and physical degeneration audit Nearest: S31-W01.
- `DISC-S36-B09` — **GENUS_ONE_QUARTIC_ELLIPTIC_EXACT_ADAPTER_INSTANCE** (36-09K). Output: Weierstrass model + forward/inverse maps + denominator/discriminant/projective exception audit Nearest: S31-W01.
- `DISC-S36-B10` — **FULL2_ROOT_SQUARECLASS_ORDER4_2ISOGENY_NORMALIZATION** (36-09L). Output: collapsed root-difference squareclasses, universal order-4 point and exact 2-isogenous quotient/open map Nearest: S31-W01, S34-W02.
- `DISC-S36-B11` — **RELATIVE_2ISOGENY_KUMMER_SPECIALIZATION_BASELINE** (36-09N). Output: generic rank/Kummer images via complete fixed-fiber isogeny descent and injective specialization Nearest: S34-W02, S31-W01.
- `DISC-S36-B12` — **GENERIC_MW_BASELINE_TO_RECEIVER_GROWTH_OBLIGATION** (36-09P + 36-09R). Output: every retained receiver-compatible specialization must exhibit strict MW growth beyond generic subgroup; may transport obligation to second quotient Nearest: S34-W02, S34-W03.
- `DISC-S36-B13` — **TORSION_GROWTH_EXCLUSION_BY_FIXED_AUXILIARY_CURVES** (36-09S). Output: uniform torsion-growth exclusion via fixed auxiliary curves with complete Q-point pullback + torsion classification Nearest: S31-W03, S34-W02.
- `DISC-S36-B14` — **DIRECTIONAL_SIX_RESERVOIR_LOCAL_CHARACTER_MATRIX** (36-09V + 36-09X + 36-09Y). Output: complete local character matrix at self/cross primes, Q2 and infinity, with automatic conditions and admissible classes Nearest: S35-PW01, S35-PW05.

## C. probable NEW_WORKFLOW

- `DISC-S36-C01` — **SOURCE_AUTHORITY_IMMUTABLE_REPLAY_WITH_CREDIT_FIREWALL** (36-01). Output: fail-closed path/blob lock + cheap independent reconstruction + explicit no-credit firewall Nearest: S30-WF02, S30-WF03.
- `DISC-S36-C02` — **RECEIVER_REPLACEMENT_BREADTH_GATE** (36-09). Output: fresh bounded candidate ledger after blind rediscovery and post-blind Arsenal comparison, with selected successor Nearest: S34-WF01, Research OS.
- `DISC-S36-C03` — **BLIND_SNAPSHOT_THEN_ARSENAL_COMPARISON_PROVENANCE_SPLIT** (36-09G + 36-09I). Output: immutable blind-only snapshot whose direct child first adds history/Arsenal mapping, with verifier content exclusions Nearest: Research OS blind rediscovery, S30-WF02.

## D. STAGE36_SPECIFIC

- `DISC-S36-D01` — **STAGE36_ALL_PLACE_LOCAL_POINT_FAMILY** (36-09C). Output: explicit local receiver points at every relevant place, killing single-place obstruction route Nearest: S34-W03.
- `DISC-S36-D02` — **STAGE36_TO_STAGE14_SECOND_PYTHAGOREAN_BASECHANGE_TRANSFER** (36-09Q). Output: exact Stage36 p-line = second-Pythagorean base-change locus, transferring Stage14 fiberwise torsion theorem Nearest: Stage14 lineage, S31-W01.

## E. HISTORICAL_OR_NEGATIVE

- `DISC-S36-E01` — **MOVING_RAMIFICATION_SUPPORT_BLOCKS_FIXED_S_DESCENT** (36-05). Output: fixed function support does not imply one finite arithmetic S for all specializations Nearest: S34-W01.
- `DISC-S36-E02` — **BRAUER_COMPATIBILITY_ROUTE_BLOCKED_BY_UPSTREAM_SOURCE_GAPS** (36-09A). Output: ordered blocker: explicit 2-primary reps and local evaluation maps are not source-closed upstream Nearest: S33-PW07, S33-PW08, S30-WF03.
- `DISC-S36-E03` — **PAIRED_CHARACTER_RECEIVER_COLLAPSES_TO_FULL_ENDPOINT** (36-09F). Output: exact endpoint equivalence, hence no proper receiver gain Nearest: S35-PW01, S34-W01.
- `DISC-S36-E04` — **UNBOUNDED_SHARED_PRIME_SUPPORT_BLOCKS_FIXED_S_FULL2_OR_FACTOR_DESCENT** (36-09H + 36-09L). Output: arbitrary-prime valuation witnesses show no fixed finite S follows Nearest: S34-W01.
- `DISC-S36-E05` — **NAIVE_MULTIPLE_BY_MULTIPLE_LIFT_SEARCH_BLOCKED_BY_GENUS_GROWTH** (36-09O). Output: 2P lift locus already squarefree degree 16 genus 7, blocking naive unbounded multiple-by-multiple strategy Nearest: S34-W02.
- `DISC-S36-E06` — **PARAMETER_ONLY_HILBERT_PRODUCT_FORMULA_NOT_A_RECEIVER_OBSTRUCTION** (36-09W). Output: global product checksum is automatic and not a receiver obstruction Nearest: S33-PW07.
- `DISC-S36-E07` — **LOCALLY_ADMISSIBLE_KUMMER_CLASSES_BLOCK_PURE_LOCAL_UNIFORM_CLOSURE** (36-09Y). Output: explicit classes satisfying every tested local condition, so those filters alone cannot uniformly contradict Nearest: S35-PW01, S33-PW07.
- `DISC-S36-E08` — **EXPLICIT_RANKJUMP_WITNESSES_BLOCK_RANKJUMP_LOCUS_EMPTINESS** (36-09Z). Output: explicit rational MW/Kummer witnesses prove rankjump locus nonempty Nearest: S34-W02.
- `DISC-S36-E09` — **RANKJUMP_WITNESS_NONLIFT_DOES_NOT_PROVE_RECEIVER_FIBER_EMPTY** (36-09AA). Output: known witnesses fail receiver lift, while no fiber-emptiness inference is allowed Nearest: S34-W03.

## F. unresolved

- `DISC-S36-F01` — **UNIVERSAL_ORDER4_2PRIMARY_TORSION_GATE_WITH_FIXED_C8_ADAPTER** (36-09M). Output: candidate gate reducing k or -k square to fixed quartic C8 and fixed rank-0 elliptic curve, deriving exact 2-primary torsion Nearest: S31-W01, S34-W02.

## Strongest Harvest 2 abstraction targets

- `DISC-S36-A03` — **RECIPROCAL_INVOLUTION_TWO_LINEAR_RECEIVER_REDUCTION**: reciprocal-symmetric four-factor square receiver in nonzero x,z + physical source constraints -> iff two-linear product-square receiver in X=x+1/x,Z=z+1/z plus X±2,Z±2 reconstruction squares
- `DISC-S36-A06` — **QUADRATIC_EXTENSION_ANTIINVARIANT_TWIST_DESCENT_RANKJUMP_GATE**: quadratic-twist pair + invariant generic section + receiver point over quadratic extension -> anti-invariant extension direction descended to rational twist plus strict rank/Kummer-image growth obligation
- `DISC-S36-A07` — **SAME_X_TWIST_PAIR_RECEIVER_PRODUCT_SQUARE_ADAPTER**: non-torsion point on one twist + exact inverse source adapter + same-x square condition on other twist -> iff receiver compatibility by same-x intersection and normalized Z^2=(X^2-1)(X^2-k^4) auxiliary receiver
- `DISC-S36-A05` — **V4_GENUS3_JACOBIAN_ELLIPTIC_QUOTIENT_DECOMPOSITION**: genus-3 curve with exact Klein-four involutions -> three explicit genus-one quotients + certified Kani-Rosen Jacobian isogeny, independently checked on differentials
- `DISC-S36-A04` — **PHYSICAL_SQUARE_LIFT_CRITERION_ON_ELLIPTIC_QUOTIENT**: retained elliptic point (U,V) + physical parameter rho -> exact iff squareclass criterion (V+rho*U)/(V-rho*U) square for top-cover physical lift
- `DISC-S36-A01` — **ELEMENTARY_ABELIAN_CHARACTER_QUOTIENT_GENUS_INVENTORY**: connected elementary-2 cover of P1 with complete branch/inertia data -> complete genus inventory of every nontrivial character quotient plus exact quotient invariants
- `DISC-S36-B03` — **POINTWISE_FINITE_H_TORSOR_LIFT_CLASS_CHART_ADAPTER**: Q-defined finite H-torsor quotient point + exact H-dual character/chart data -> canonical chart squareclasses + explicit degree-|H| fiber equations with q_H^-1(P)(Q) nonempty iff delta_H(P)=1
- `DISC-S36-B11` — **RELATIVE_2ISOGENY_KUMMER_SPECIALIZATION_BASELINE**: explicit 2-isogenous family over Q(t) + Kummer classes + one exact specialization -> generic rank/Kummer images via complete fixed-fiber isogeny descent and injective specialization
- `DISC-S36-B14` — **DIRECTIONAL_SIX_RESERVOIR_LOCAL_CHARACTER_MATRIX**: Gaussian/directional factorization with six odd-disjoint prime reservoirs + selected Kummer classes -> complete local character matrix at self/cross primes, Q2 and infinity, with automatic conditions and admissible classes

Key hostile-dedup warnings:

- `DISC-S36-A03` must be compared semantically with Stage35 `S35-PW04`; the shared word “reciprocal” is not enough either to merge or separate them.
- `DISC-S36-B09` is already an exact `S31-W01` type match and should not become a new weapon merely because Stage36 has new coefficients.
- `DISC-S36-B14` is a dynamic six-reservoir local character matrix, not Stage35 `S35-PW05` finite exceptional-prime classification.
- `DISC-S36-F01` remains unresolved because hostile audit found a verifier-coverage defect even though the mathematics recheck passed; later user-pass repair is not hostile re-audit credit.

## Negative-result firewall

The E-records are anti-loop/history assets. In particular: moving specialization support blocks fixed-S descent; parameter-only Hilbert product formula is not a receiver obstruction; locally admissible Kummer classes block pure-local uniform closure; explicit rank-jump witnesses prove the rank-jump locus is nonempty but do not imply receiver existence; known witnesses failing the receiver do not prove receiver-fiber emptiness.

## Harvest 2 exact handoff

1. Keep lower `62c26297ebeb159e9cdd1e6b9c2129dff6a4acdc` and upper `07a465cb5025e7c0188fb63610bb40e4b54e7a84` fixed.
2. Do not include #1670 / 36-09AB or later main movement.
3. Abstract only the 36 records in `stage36-initial-discovery.json`; strip Stage36 coefficients/payload and write exact reusable `input -> operation -> output` contracts.
4. Hostile-compare the priority overlap pairs listed in the JSON handoff; Stage34 and Stage35 overlap must be treated strictly.
5. Keep `DISC-S36-F01` audit-maturity unresolved until the repaired verifier is hostile re-audited or otherwise receives equivalent authority.
6. Do not assign stable IDs or modify Arsenal registry/cards/catalog in Harvest 2.

## Provenance notes

- Canonical inception basis: PR #1535 first authoritative Stage36 merge, not an older working branch/SOURCE_HEAD.
- Upper bound basis: `main` exactly at Harvest-start observation.
- U-AA source candidates use PR #1664 hostile-audited batch head `25229e7b0dfbbc5524266ce49e8edaf217841701`; their mutable promotion remains outside the frozen upper-state authority.
- Candidate-level source PR/head/path/blob, certificate blob, verifier/source-lock, audit status, field, quantifiers, exceptions and credit boundaries are in the JSON companion.
