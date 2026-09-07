# Research Arsenal × Literature Strengthening Audit — Phase 6 Hostile Freeze

Status: **LITERATURE MAP + CATEGORY AUDITS + HOSTILE DEDUP COMPLETE**  
Implementation: **NOT YET PERFORMED**  
Stage36: **EXCLUDED**

## 1. Frozen boundary

This Phase 6 audit does not move the Phase 1 literature-comparison population.

```text
ARSENAL_BASE_MAIN=9306238c7ada55e31311245019d6b7e474ad837f
STAGE35_PROVISIONAL_COMPARISON_HEAD=3fc684677ef1570a820420079088667f558e0983
STAGE36_EXCLUDED=true
LITERATURE_COMPARISON_POPULATION_FROZEN=true
```

The live repository may advance independently. That does not expand this audit population, grant freshness to later Stage assets, or alter the authority rule that active Stage authority outranks a provisional Arsenal snapshot.

Phase 6 reads the Phase 1 map and the Phase 2–5 category audits as discovery evidence. Earlier multi-label classifications are not final credit. Every final candidate below receives exactly one Phase 6 class.

## 2. Candidate population and hostile counts

The frozen Phase 6 population contains 36 candidates:

- Phase 2 manifest: 8
- Phase 3 manifest: 8
- Phase 4 manifest: 9
- Phase 5 manifest: 9
- Phase 3 prerequisite-only Stage35 diagnostics: 2

Phase 1 was a routing/triage map. Route names that were not materialized by Phases 2–5 are not inflated into new Phase 6 candidates.

| Final class | Count |
|---|---:|
| `LITERATURE_DIRECT` | 0 |
| `LITERATURE_ADAPTED` | 6 |
| `EXTEND_EXISTING` | 9 |
| `NEW_LITERATURE_WEAPON` | 9 |
| `NEW_LITERATURE_WORKFLOW` | 1 |
| `SOURCE_ANCHOR_ONLY` | 2 |
| `REPO_SPECIFIC` | 0 |
| `NO_STRENGTHENING` | 0 |
| `NOT_APPLICABLE` | 2 |
| `REJECT_DUPLICATE` | 2 |
| `RESEARCH_GAP` | 5 |
| `POSSIBLY_NOVEL` | 0 |

The zero count for `LITERATURE_DIRECT` is deliberate. Under hostile comparison, every apparently direct strengthening either changes the admissible input interface, requires a repo-to-theorem adapter, or merely changes the algorithm/source provenance rather than the mathematical output.

## 3. Final architectural rule

The implementation boundary is:

```text
REPO_INPUT
-> REPO_SOURCE_ADAPTER
-> LITERATURE_THEOREM_OR_ALGORITHM
-> REPO_OUTPUT_CERTIFICATE
```

The literature theorem remains literature provenance. A repo adapter, source marking, local-image map, covering identity, Brauer evaluation, or reconstruction certificate remains repo-derived provenance. A formal theorem in the literature does not make a new repo adapter `FORMAL`.

All new literature-backed additions therefore start `PROVISIONAL`. A delta to an existing `FORMAL` card is also treated as a provisional delta until exact implementation, replay and hostile audit complete.

## 4. `LITERATURE_ADAPTED` — 6

### `MW_SIEVE_GENERAL_FINITE_QUOTIENT_EXTENSION` → `S34-W02`

Final verdict: **LITERATURE_ADAPTED**.

Bruin–Stoll, *The Mordell-Weil sieve: proving non-existence of rational points on curves*, LMS J. Comput. Math. 13 (2010), DOI `10.1112/S1461157009000187`, Section 3 including Definition 3.1, strictly generalizes the current good-prime CRT pattern to exact finite quotients and local admissible subsets. The frozen S34-W02 instance is a special case, but the general theorem cannot be imported without `RECEIVER_TO_LOCAL_IMAGE_SUBSET` and `LOCAL_MW_QUOTIENT_MATERIALIZER`.

Safe strength delta:

```text
current:
full MW + good-prime residue conditions + CRT

candidate:
controlled Gamma + exact phi_i: Gamma -> G_i
+ exact X_i subset G_i from receiver/local images
+ complete torsion/coset accounting
-> empty intersection certifies nonexistence
```

No nonempty sieve set is promoted to a rational point, and no uncontrolled finite-index subgroup is promoted to full MW.

### `ELLIPTIC_CHABAUTY_EXTENSION_ADAPTER`

Final verdict: **LITERATURE_ADAPTED**.

Bruin, *Chabauty methods using elliptic curves*, J. reine angew. Math. 562 (2003), DOI `10.1515/crll.2003.076`, Section 4 including Lemma 4.3. S35 quotient/lift receivers require a new exact extension-field elliptic model, base-field image condition, MW-index control and local elliptic-log certificate before the theorem applies.

### `FINITE_BRANCH_TO_EXPLICIT_N_COVER`

Final verdict: **LITERATURE_ADAPTED**.

Cremona–Fisher–O'Neil–Simon–Stoll, *Explicit n-descent on elliptic curves I/II*, DOI `10.1515/CRELLE.2008.012` and `10.1515/CRELLE.2009.050`. A finite squareclass branch or simultaneous-square system is not a Selmer element merely because it resembles a covering equation. The new adapter must prove the exact curve/Jacobian, covering map, torsor/Selmer identity and local data.

### `STAGE33_BRAUER_ADELIC_EVALUATION_ADAPTER`

Final verdict: **LITERATURE_ADAPTED**.

Bright, *Efficient evaluation of the Brauer-Manin obstruction*, Math. Proc. Camb. Phil. Soc. 142 (2007), DOI `10.1017/S0305004106009844`. The exact numbered theorem was not recovered in Phase 4 and remains a promotion-blocking source-lock item.

This is the most important Stage33 bridge:

```text
literal/marked source-bound Brauer class
-> actual local point evaluation in Br(k_v)
-> normalized inv_v
-> complete local evaluation image
```

PW08 localization data are not themselves pointwise evaluations.

### `KUMMER_2PRIMARY_BM_REDUCTION_GATE`

Final verdict: **LITERATURE_ADAPTED**.

Creutz–Viray, *Degree and the Brauer-Manin obstruction*, Algebra & Number Theory 12 (2018), DOI `10.2140/ant.2018.12.2445`, Theorem 1.7; Theorem 1.8; Appendix Theorem A.1. Before using the 2-primary reduction, the repo must prove an actual Kummer variety from a 2-covering and certify the relevant `Br[2^infinity]` coverage. `PW09`'s named `Br[2]` class is not automatically the full 2-primary layer.

### `BRAUER_GOOD_REDUCTION_FINITE_PLACE_REDUCER`

Final verdict: **LITERATURE_ADAPTED**.

Colliot-Thélène–Skorobogatov, *Good reduction of the Brauer-Manin obstruction*, Trans. AMS 365 (2013), DOI `10.1090/S0002-9947-2012-05556-5`. Application requires a smooth proper model, torsion-free geometric Picard group, finite transcendental Brauer group with order control, and exact bad-reduction set. It is not an open-receiver theorem.

## 5. Strongest `EXTEND_EXISTING` candidates — 9

These should not become independent stable weapon IDs unless implementation reveals a genuine new semantic interface.

### P0

`MW_CONTROLLED_FINITE_INDEX_INTERFACE` extends `S31-WF01`/`S34-W02` to export `full_group_proved`, subgroup generators, known index bounds and prime-saturation facts separately. It never relabels a finite-index subgroup as the full MW group.

`S34W01_TERMINAL_EQUATION_ROUTER_EXTENSION` extends `S34-W01` with typed outputs such as `FIXED_S_UNIT`, `FIXED_THUE`, `FIXED_THUE_MAHLER`, and `EXPLICIT_COVER`. It does not change the current finite squareclass-branch credit.

`F2_SYMPLECTIC_TRANSVECTION_DIRECTION_NORMAL_FORM` extends `S32-PW06`. For exact nondegenerate symplectic `(V,B)` over `F2`, a nonidentity symplectic `T` with `rank(T-I)=1` has a unique nonzero direction `v` and

```text
T(x)=x+B(x,v)v.
```

Thus `im(T-I)<=W` becomes `v in W-{0}`, replacing arbitrary-operator enumeration by direction enumeration. Pollatsek 1976 is a characteristic-two transvection source anchor, but the rank-one normal form itself should be proved directly in the repo adapter. No absolute source line is obtained.

`FINITE_ACTION_STABILIZER_TRANSPORTER_EQUIVARIANT_MATCHER` extends `S30-W01` using Seress's stabilizer/transporter machinery instead of raw equivariant relabeling enumeration. The common/source semantic anchor remains mandatory.

`GENERATOR_COMPLETE_SEMILINEAR_COMPATIBILITY_VERIFIER` extends `S30-W02`: once both sides are certified homomorphisms from the same generated/presented group, generator/relator equality replaces a full all-element scan. `sigma`, `theta`, the cocycle/deck element and the source action remain source-derived.

### P1/P2

`REVERSIBLE_INTEGER_MODULE_NORMAL_FORM_ADAPTER` factors the common HNF/SNF-with-unimodular-transforms layer across `S32-PW03`, `S32-PW04`, and `S33-PW02`. Primary source: Kannan–Bachem 1979, DOI `10.1137/0208040`.

`FINITE_LATTICE_QUOTIENT_SATURATION_ADAPTER` generalizes exact image/saturation/quotient calculations but does not turn the ambient SNF quotient into the reachable subgroup and does not upgrade PW04's lower bound to exact CVP.

`FINITE_MODULE_INTERTWINER_ISOMORPHISM_SOLVER` extends `S33-PW05` using constructive module-isomorphism algorithms such as Chistov–Ivanyos–Karpinski 1997, DOI `10.1145/258726.258751`. An invertible intertwiner is still not a marked geometric adapter.

`ORBITAL_DOUBLE_COSET_RECONSTRUCTION_ENGINE` extends `S32-PW05`/`S30-W03` by computing orbital representatives before propagation. Complete coverage, conflict checks and source semantics remain unchanged.

## 6. `NEW_LITERATURE_WEAPON` — 9

These have independent reusable theorem/algorithm interfaces and should begin as new `PROVISIONAL` literature-backed candidates.

1. `ELLIPTIC_LOG_SINTEGRAL_TERMINAL` — von Känel–Matschke 2023, Memoirs AMS 286(1419), DOI `10.1090/memo/1419`, especially Algorithm 11.19. Requires an exact S-integral Weierstrass dictionary, MW basis and explicit initial height bound.
2. `CHABAUTY_TERMINAL_ROUTER` — Siksek 2013, Algebra & Number Theory 7(4), DOI `10.2140/ant.2013.7.765`, Theorem 2 and Section 5; classical Coleman hypotheses remain visible.
3. `QUADRATIC_CHABAUTY_TERMINAL` — Balakrishnan–Besser–Müller 2017, Math. Comp. 86, DOI `10.1090/mcom/3130`. Rank/Néron-Severi/p-adic-height/model hypotheses and final finite-survivor cleanup are load-bearing.
4. `COVERING_COLLECTION_TERMINAL_ADAPTER` — Flynn–Wetherell 2001, Acta Arith. 98(2), DOI `10.4064/aa98-2-9`. Exhaustive coverage must be proved; a nonempty covering family is not a solved rational-point problem.
5. `FIXED_THUE_MAHLER_TERMINAL` — Gherga–Siksek 2025, Algebra & Number Theory 19(4), DOI `10.2140/ant.2025.19.667`, Algorithm 2.6, Proposition 2.7, Proposition 3.1, Propositions 10.2–10.3 and Procedure 10.4.
6. `FIXED_S_UNIT_TERMINAL` — von Känel–Matschke 2023, including Algorithm 3.14 in the audited equation classes. Fixed finite `S` is mandatory.
7. `FIXED_THUE_TERMINAL` — Tzanakis–de Weger 1989, J. Number Theory 31(2), DOI `10.1016/0022-314X(89)90014-0`. The Phase 3 audit did not recover a single top-level numbered Algorithm; source-lock must preserve that limitation.
8. `BRAUER_MANIN_EMPTY_ADELIC_SET_TERMINAL` — Bright–Swinnerton-Dyer 2004, DOI `10.1017/S0305004104007571`, together with exact local-evaluation coverage. Empty certified BM adelic set gives nonexistence; a nonzero class alone does not.
9. `OPEN_DESCENT_ETALE_BRAUER_TERMINAL` — Cao–Demarche–Xu 2019, Trans. AMS 371, DOI `10.1090/tran/7567`, Theorem 1.5 = Theorem 7.5. The theorem identifies descent and étale-Brauer adelic sets for the stated smooth quasi-projective geometrically integral varieties; emptiness must still be computed.

## 7. `NEW_LITERATURE_WORKFLOW` — 1

`CERTIFIED_BAKER_LLL_REDUCTION_ENUMERATION` is a reusable proof workflow rather than a new Diophantine theorem:

```text
proved initial height/exponent bound
-> exact real/p-adic approximation lattice
-> certified LLL/reduction
-> exact finite enumeration region
-> independent replay
-> exact repo pullback
```

Primary source pattern: Tzanakis–de Weger, *How to explicitly solve a Thue-Mahler equation*, Compositio 84 (1992), NUMDAM `CM_1992__84_3_223_0`, with corrigendum. The workflow must not turn LLL or a reduced bound into completeness without the final exact enumeration.

## 8. `SOURCE_ANCHOR_ONLY` — 2

`GENUS_ONE_NDESCENT_SOURCE_ANCHOR` strengthens source provenance for `S31-W01` via the Cremona–Fisher–O'Neil–Simon–Stoll explicit n-descent series. It does not replace the repo's exact rational maps, denominator opens, exceptional loci or integrality firewall.

`GERSTEN_PURITY_THEOREM_ANCHOR` strengthens `S33-PW08/PW10` provenance via Bloch–Ogus 1974, DOI `10.24033/asens.1266`. It does not identify repo height-one primes, exceptional divisors or literal purity corrections.

## 9. Rejected / blocked

### `REJECT_DUPLICATE`

- `DISC-S35-A02` — dynamic-reservoir preflight: prerequisite/diagnostic only; absorbed by the finite-support gap.
- `DISC-S35-A09` — primitive pair-gcd skeleton: normalization prerequisite only; absorbed by the same gate and fixed-equation adapters.

### `NOT_APPLICABLE`

`KUMMER_TRANSCENDENTAL_BRAUER_COMPARISON_ADAPTER`: the strongest audited Skorobogatov–Zarhin comparison is an odd-`n` isomorphism on an actual `Kum(A)`. The frozen target is 2-primary and lacks the required marked abelian-surface/Kummer pullback. No odd-to-2 extrapolation is allowed.

`CLASSICAL_GROUP_CONSTRUCTIVE_RECOGNITION_GATE`: the frozen instances do not present the whole claimed classical group in the natural finite-field representation required by constructive-recognition algorithms. In any case, recognition would not remove the source-marking gate.

### `RESEARCH_GAP`

1. `PARAMETRIC_RESERVOIR_FINITE_SUPPORT_CERTIFICATE`: no proof yet that the live parameter-dependent reservoir becomes a fixed finite `S` or finitely many fixed `S_i`. Until this is proved, no fixed-S theorem applies.
2. `NORM_FORM_BOUND_AND_TERMINAL_ADAPTER`: Bugeaud–Győry gives explicit norm/Thue/Thue-Mahler bounds, but the exact repo norm-form normalizer plus a complete enumerator for the relevant number-field/S class is absent.
3. `KUMMER_SECOND_DESCENT_ADAPTER`: the frozen repo does not yet provide the exact abelian variety, `H^1(k,A[2])` 2-covering identity, Galois/polarization package, local Selmer/Cassels–Tate data, or explicit Sha conditionality required by the reviewed second-descent theorems.
4. `CURVE_FINITE_ABELIAN_DESCENT_TERMINAL`: no exact curve receiver satisfying Stoll's strong curve/abelian/Sha hypotheses has been source-locked from Stage33 surface data.
5. `TRANSVECTION_GENERATED_SUBGROUP_CLASSIFIER`: PW06 supplies a source-derived transvection constraint, not a source-locked irreducible group generated by multiple transvections. Pollatsek's exact theorem-number source lock is also still missing.

## 10. Possible novelty

No Phase 6 candidate is classified `POSSIBLY_NOVEL`.

The bounded-search novelty firewall remains:

```text
POSSIBLY_NOVEL
= NO_DIRECT_MATCH_FOUND_IN_THIS_BOUNDED_LITERATURE_SEARCH
!= novelty claim
```

No search miss in Phases 1–5 establishes novelty, priority or publication-level originality.

## 11. Phase 7 implementation manifest

### Extensions

```text
MW_CONTROLLED_FINITE_INDEX_INTERFACE
S34W01_TERMINAL_EQUATION_ROUTER_EXTENSION
F2_SYMPLECTIC_TRANSVECTION_DIRECTION_NORMAL_FORM
FINITE_ACTION_STABILIZER_TRANSPORTER_EQUIVARIANT_MATCHER
GENERATOR_COMPLETE_SEMILINEAR_COMPATIBILITY_VERIFIER
REVERSIBLE_INTEGER_MODULE_NORMAL_FORM_ADAPTER
FINITE_LATTICE_QUOTIENT_SATURATION_ADAPTER
FINITE_MODULE_INTERTWINER_ISOMORPHISM_SOLVER
ORBITAL_DOUBLE_COSET_RECONSTRUCTION_ENGINE
```

### Literature-adapted candidates

```text
MW_SIEVE_GENERAL_FINITE_QUOTIENT_EXTENSION
ELLIPTIC_CHABAUTY_EXTENSION_ADAPTER
FINITE_BRANCH_TO_EXPLICIT_N_COVER
STAGE33_BRAUER_ADELIC_EVALUATION_ADAPTER
KUMMER_2PRIMARY_BM_REDUCTION_GATE
BRAUER_GOOD_REDUCTION_FINITE_PLACE_REDUCER
```

### New weapon candidates

```text
ELLIPTIC_LOG_SINTEGRAL_TERMINAL
CHABAUTY_TERMINAL_ROUTER
QUADRATIC_CHABAUTY_TERMINAL
COVERING_COLLECTION_TERMINAL_ADAPTER
FIXED_THUE_MAHLER_TERMINAL
FIXED_S_UNIT_TERMINAL
FIXED_THUE_TERMINAL
BRAUER_MANIN_EMPTY_ADELIC_SET_TERMINAL
OPEN_DESCENT_ETALE_BRAUER_TERMINAL
```

### New workflow candidates

```text
CERTIFIED_BAKER_LLL_REDUCTION_ENUMERATION
```

### Source-anchor-only changes

```text
GENUS_ONE_NDESCENT_SOURCE_ANCHOR
GERSTEN_PURITY_THEOREM_ANCHOR
```

### Do not implement as weapons in Phase 7

```text
REJECT_DUPLICATE:
  DISC-S35-A02
  DISC-S35-A09

NOT_APPLICABLE:
  KUMMER_TRANSCENDENTAL_BRAUER_COMPARISON_ADAPTER
  CLASSICAL_GROUP_CONSTRUCTIVE_RECOGNITION_GATE

RESEARCH_GAP:
  PARAMETRIC_RESERVOIR_FINITE_SUPPORT_CERTIFICATE
  NORM_FORM_BOUND_AND_TERMINAL_ADAPTER
  KUMMER_SECOND_DESCENT_ADAPTER
  CURVE_FINITE_ABELIAN_DESCENT_TERMINAL
  TRANSVECTION_GENERATED_SUBGROUP_CLASSIFIER
```

### Implementation order

P0 is the smallest high-value set:

```text
MW_SIEVE_GENERAL_FINITE_QUOTIENT_EXTENSION
MW_CONTROLLED_FINITE_INDEX_INTERFACE
S34W01_TERMINAL_EQUATION_ROUTER_EXTENSION
FIXED_THUE_MAHLER_TERMINAL
STAGE33_BRAUER_ADELIC_EVALUATION_ADAPTER
BRAUER_MANIN_EMPTY_ADELIC_SET_TERMINAL
F2_SYMPLECTIC_TRANSVECTION_DIRECTION_NORMAL_FORM
FINITE_ACTION_STABILIZER_TRANSPORTER_EQUIVARIANT_MATCHER
GENERATOR_COMPLETE_SEMILINEAR_COMPATIBILITY_VERIFIER
```

P1 contains the remaining immediately implementable adapters/terminals and reusable integer/module infrastructure. P2 contains quadratic Chabauty, orbital reconstruction and source-only literature anchors. Research gaps remain frozen and fail closed.

## 12. Stop boundary

No `docs/arsenal/index.json` change.  
No generated-card/catalog change.  
No stable ID creation.  
No Stage authority change.  
No Stage36 read/credit.  
No merge.

**Phase 6 closes discovery/dedup only. Phase 7 is the first implementation phase.**
