# Research Arsenal literature strengthening promotion

Status: **PROVISIONAL — hostile audit required**

```text
LITERATURE_AUDIT_PR=1676
LITERATURE_AUDIT_EXACT_HEAD=44f635f364f9904c2048197bc84eea58938fdb16
ARSENAL_BASE_MAIN=9306238c7ada55e31311245019d6b7e474ad837f
IMPLEMENTATION_BASE_MAIN=24215fa27a631cd3cb370c0dfd76866dd2e916f1
STAGE35_PROVISIONAL_COMPARISON_HEAD=3fc684677ef1570a820420079088667f558e0983
STAGE36_EXCLUDED=true
LITERATURE_STRENGTHENING_ADDS_NO_STAGE_PROGRESS=true
LITERATURE_ARSENAL_REGISTRATION_DOES_NOT_CHANGE_STAGE_MATHEMATICAL_AUTHORITY=true
MATHEMATICAL_STAGE_CREDIT_INCREMENT=0
```

Authority: `active stage authority > formal Arsenal core > literature-backed provisional registration > historical discovery`.
Literature theorem provenance and repo adapter provenance are distinct. Published theorems do not make an unverified repo adapter FORMAL. No Stage theorem, active MAIN authority, endpoint, or perfect-cuboid claim changes.

Phase-6 accepted implementation: 9 existing-ID deltas; 6 adapted weapons; 9 new terminal weapons; 1 workflow; 2 source anchors. Rejected/gap items remain inactive. Stage36 is not consumed.

# New PROVISIONAL literature-backed weapons

## LIT-PW01

- Candidate / class / role: `MW_SIEVE_GENERAL_FINITE_QUOTIENT_EXTENSION` / **LITERATURE_ADAPTED** / `GENERAL_FINITE_QUOTIENT_MORDELL_WEIL_SIEVE`
- Maturity: **PROVISIONAL**
- Contract: Certified MW subgroup Gamma + exact finite quotient maps phi_i:Gamma->G_i + exact receiver-admissible subsets X_i + complete torsion/coset accounting -> if the exact inverse-image intersection is empty, no receiver-compatible rational point exists.
- HYPOTHESES: finitely generated MW subgroup with sufficient index/saturation control; exact finite quotient maps; exact receiver-to-local-image subsets; complete torsion/coset accounting
- APPLICABILITY: elliptic/Jacobian receiver problems over Q or a source-locked number-field extension
- DO_NOT_USE_FOR: nonempty sieve set as a rational point; uncontrolled finite-index subgroup as full MW; universal termination

### Literature provenance
- Authors: Nils Bruin; Michael Stoll
- Title: The Mordell-Weil sieve: proving non-existence of rational points on curves
- Year / journal-publisher: 2010 / LMS Journal of Computation and Mathematics 13, 272-306
- DOI: 10.1112/S1461157009000187
- Canonical URL: https://doi.org/10.1112/S1461157009000187
- Theorem/algorithm locator: Section 3 finite-quotient/finite-index formalism, including Definition 3.1; later local-information sections
- Theorem/algorithm summary: Finite-quotient Mordell-Weil sieve: exact homomorphisms to finite groups plus exact local admissible subsets can certify nonexistence when the compatible inverse-image intersection is empty.
- Conditional assumptions: none after exact finite data; no universal eventual-success theorem
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S34-W02 full-MW/torsion/good-prime CRT data
- Required adapter: RECEIVER_TO_LOCAL_IMAGE_SUBSET; LOCAL_MW_QUOTIENT_MATERIALIZER
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: stronger certified nonexistence sieve
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW02

- Candidate / class / role: `ELLIPTIC_CHABAUTY_EXTENSION_ADAPTER` / **LITERATURE_ADAPTED** / `REPO_QUOTIENT_TO_ELLIPTIC_CHABAUTY_ADAPTER`
- Maturity: **PROVISIONAL**
- Contract: Exact quotient/lift receiver -> elliptic curve over an extension + exact base-field image condition + controlled MW index + local elliptic-log matrix -> certified elliptic-Chabauty exclusion/uniqueness.
- HYPOTHESES: exact extension-field elliptic model; local dimension/rank criterion; finite-index control at selected p; local logarithm certificate
- APPLICABILITY: quotient/lift receivers whose rationality condition becomes a base-field condition on an elliptic curve over an extension
- DO_NOT_USE_FOR: Kummer-shaped equations without elliptic-cover identity; rank inequality alone; uncontrolled MW index

### Literature provenance
- Authors: Nils Bruin
- Title: Chabauty methods using elliptic curves
- Year / journal-publisher: 2003 / Journal für die reine und angewandte Mathematik 562, 27-49
- DOI: 10.1515/crll.2003.076
- Canonical URL: https://doi.org/10.1515/crll.2003.076
- Theorem/algorithm locator: Section 4, including Lemma 4.3
- Theorem/algorithm summary: Elliptic Chabauty uses local elliptic logarithms on an extension-field elliptic curve to enforce a base-field rationality condition when the local rank criterion is satisfied.
- Conditional assumptions: unconditional once local matrix/rank and index hypotheses are exact
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S35-PW02/S35-PW03 quotient/lift receivers and S34-W03 restricted intersections
- Required adapter: REPO_QUOTIENT_TO_ELLIPTIC_EXTENSION; BASE_FIELD_IMAGE_CONDITION; ELLIPTIC_LOCAL_LOG_CERTIFICATE
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: proof-capable p-adic terminal on eligible branches
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW03

- Candidate / class / role: `FINITE_BRANCH_TO_EXPLICIT_N_COVER` / **LITERATURE_ADAPTED** / `FINITE_BRANCH_TO_N_COVER_SELMER_ADAPTER`
- Maturity: **PROVISIONAL**
- Contract: Finite exact branch/square system + exact curve/Jacobian + explicit cover map -> prove torsor/Selmer identity and local data -> emit a genuine n-covering object with exhaustive semantics only where proved.
- HYPOTHESES: nonsingular genus-one/cover object; source-locked Jacobian; exact cover/torsor/Selmer class; exact local data
- APPLICABILITY: finite squareclass branches that can be identified with explicit 2/3/4-coverings or other n-coverings
- DO_NOT_USE_FOR: Selmer membership as rational point; Kummer-looking equations as cover identity; nonempty cover as closure

### Literature provenance
- Authors: J. E. Cremona; T. A. Fisher; C. O'Neil; D. Simon; M. Stoll
- Title: Explicit n-descent on elliptic curves, I. Algebra / II. Geometry
- Year / journal-publisher: 2008/2009 / Journal für die reine und angewandte Mathematik 615 / 632
- DOI: 10.1515/CRELLE.2008.012; 10.1515/CRELLE.2009.050
- Canonical URL: https://doi.org/10.1515/CRELLE.2008.012 ; https://doi.org/10.1515/CRELLE.2009.050
- Theorem/algorithm locator: paper-level n-Selmer/genus-one model constructions; no single top-level numbered theorem was frozen in Phase 6 (FORMAL promotion blocker until exact selected theorem/algorithm is locked)
- Theorem/algorithm summary: Explicit n-descent literature constructs geometric genus-one representatives of descent/Selmer elements once the actual covering class is identified.
- Conditional assumptions: none beyond exact descent data
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S34-W01 finite branches or S35-PW03 simultaneous-square receiver
- Required adapter: REPO_BRANCH_TO_COVER_CLASS; REPO_COVER_TO_SELMER_ELEMENT
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: typed genuine n-covering object; not rational-point closure
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW04

- Candidate / class / role: `STAGE33_BRAUER_ADELIC_EVALUATION_ADAPTER` / **LITERATURE_ADAPTED** / `SOURCE_BOUND_BRAUER_LOCAL_EVALUATION_ADAPTER`
- Maturity: **PROVISIONAL**
- Contract: Named source-bound Brauer representative + exact terminal variety/model + local point population -> compute evaluation in Br(k_v), normalized inv_v, and a complete local evaluation image/table.
- HYPOTHESES: valid Brauer representative on exact variety/open; local evaluation formula/model hypotheses; all relevant boundary strata covered
- APPLICABILITY: Stage33 classes already tied to literal/marked representatives
- DO_NOT_USE_FOR: nonzero class as obstruction; localization column as pointwise evaluation; incomplete local population as adelic set

### Literature provenance
- Authors: Martin Bright
- Title: Efficient evaluation of the Brauer-Manin obstruction
- Year / journal-publisher: 2007 / Mathematical Proceedings of the Cambridge Philosophical Society 142, 13-23
- DOI: 10.1017/S0305004106009844
- Canonical URL: https://doi.org/10.1017/S0305004106009844
- Theorem/algorithm locator: main result; exact internal theorem number was not recovered in Phase 6 (FORMAL promotion blocker until exact selected result is locked)
- Theorem/algorithm summary: Under suitable p-adic model/reduction hypotheses, local evaluation of a Brauer class can be reduced to finite/reduction data; the repo must still bind its literal class to the evaluation formula.
- Conditional assumptions: none once exact local model hypotheses hold
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S33-PW04/PW09 marked class binding plus S33-PW08/PW10 localization data
- Required adapter: MARKED_BRAUER_CLASS_TO_LOCAL_EVALUATION; GERSTEN_LOCALIZATION_TO_POINT_EVALUATION
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: certified local invariant images usable by a Brauer-Manin terminal
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW05

- Candidate / class / role: `KUMMER_2PRIMARY_BM_REDUCTION_GATE` / **LITERATURE_ADAPTED** / `KUMMER_2PRIMARY_BRAUER_RELEVANCE_GATE`
- Maturity: **PROVISIONAL**
- Contract: Prove the exact terminal object is a Kummer variety from a 2-covering; certify tested 2-primary Brauer coverage; then restrict Brauer-Manin obstruction search to 2-primary classes.
- HYPOTHESES: actual Kummer variety over a number field; exact 2-covering provenance; sufficient Br[2^infinity] subgroup coverage
- APPLICABILITY: only after a source-locked Kummer-variety identity
- DO_NOT_USE_FOR: Br[2] as automatically all 2-primary; Kummer terminology as geometry; missing adelic evaluations

### Literature provenance
- Authors: Brendan Creutz; Bianca Viray
- Title: Degree and the Brauer-Manin obstruction
- Year / journal-publisher: 2018 / Algebra & Number Theory 12, 2445-2480
- DOI: 10.2140/ant.2018.12.2445
- Canonical URL: https://doi.org/10.2140/ant.2018.12.2445
- Theorem/algorithm locator: Theorems 1.7, 1.9; Appendix Theorem A.1
- Theorem/algorithm summary: For Kummer varieties the relevant Brauer-Manin obstruction can be reduced to the 2-primary part under the cited BM_2 results.
- Conditional assumptions: none beyond the Kummer hypotheses of the cited results
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S33-PW09 named Br[2] H2(mu2) lift and S33-PW07 torsor semantics
- Required adapter: REPO_RECEIVER_TO_KUMMER_2COVERING; KUMMER_2PRIMARY_BRAUER_COVERAGE_CERTIFICATE
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: theorem-certified 2-primary relevance reduction; not an obstruction by itself
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW06

- Candidate / class / role: `BRAUER_GOOD_REDUCTION_FINITE_PLACE_REDUCER` / **LITERATURE_ADAPTED** / `BRAUER_RELEVANT_PLACE_CERTIFICATE`
- Maturity: **PROVISIONAL**
- Contract: Smooth proper model + torsion-free geometric Picard + finite transcendental Brauer group/order + exact bad-reduction set -> restrict Brauer evaluation to archimedean, bad-reduction, and order-dividing finite places.
- HYPOTHESES: smooth projective number-field variety; Pic(Xbar) torsion-free; finite Br(X)/Br1(X) with order control
- APPLICABILITY: proper Stage33 terminal objects satisfying the theorem exactly
- DO_NOT_USE_FOR: open receivers; unknown transcendental Brauer order; omission of local evaluation at retained places

### Literature provenance
- Authors: Jean-Louis Colliot-Thélène; Alexei N. Skorobogatov
- Title: Good reduction of the Brauer-Manin obstruction
- Year / journal-publisher: 2013 / Transactions of the American Mathematical Society 365, 579-590
- DOI: 10.1090/S0002-9947-2012-05556-5
- Canonical URL: https://doi.org/10.1090/S0002-9947-2012-05556-5
- Theorem/algorithm locator: main theorem as stated in the paper abstract/introduction; exact internal theorem number was not frozen in Phase 6 (FORMAL promotion blocker until locked)
- Theorem/algorithm summary: Under the stated smooth/proper Picard and finite transcendental-Brauer hypotheses, only archimedean, bad-reduction and order-dividing primes can affect the Brauer-Manin set.
- Conditional assumptions: none beyond theorem hypotheses
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S33-PW08/PW10 explicit residue/localization machinery
- Required adapter: PROPER_MODEL_AND_BAD_PLACE_CERTIFICATE; TRANSCENDENTAL_BRAUER_ORDER_CERTIFICATE
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: finite theorem-certified place panel for Brauer evaluation
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW07

- Candidate / class / role: `ELLIPTIC_LOG_SINTEGRAL_TERMINAL` / **NEW_LITERATURE_WEAPON** / `COMPLETE_ELLIPTIC_S_INTEGRAL_POINT_TERMINAL`
- Maturity: **PROVISIONAL**
- Contract: Integral Weierstrass E/Q + fixed finite S + certified MW basis + explicit initial height bound + exact repo S-integrality dictionary -> elliptic-logarithm sieves -> complete S-integral point set.
- HYPOTHESES: exact integral Weierstrass model; fixed finite S; MW basis; explicit initial canonical-height bound; exact local/global logarithm data
- APPLICABILITY: receiver branches exactly equivalent to S-integral elliptic points over Q
- DO_NOT_USE_FOR: birational integrality without iff adapter; missing initial height bound; incomplete MW basis

### Literature provenance
- Authors: Rafael von Känel; Benjamin Matschke
- Title: Solving S-Unit, Mordell, Thue, Thue-Mahler and Generalized Ramanujan-Nagell Equations via the Shimura-Taniyama Conjecture
- Year / journal-publisher: 2023 / Memoirs of the American Mathematical Society 286(1419)
- DOI: 10.1090/memo/1419
- Canonical URL: https://doi.org/10.1090/memo/1419
- Theorem/algorithm locator: Algorithm 11.19
- Theorem/algorithm summary: Algorithm 11.19 gives a complete S-integral elliptic-point algorithm from explicit Mordell-Weil and height-bound input.
- Conditional assumptions: unconditional given the required effective inputs
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S31-W02 exact integral-transfer surface or S34-W03 receiver intersection
- Required adapter: REPO_TO_S_INTEGRAL_WEIERSTRASS; EXPLICIT_INITIAL_HEIGHT_BOUND
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: complete S-integral point set
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW08

- Candidate / class / role: `CHABAUTY_TERMINAL_ROUTER` / **NEW_LITERATURE_WEAPON** / `EXPLICIT_CHABAUTY_POINT_COMPLETENESS_TERMINAL`
- Maturity: **PROVISIONAL**
- Contract: Exact smooth projective genus>=2 curve + Jacobian MW/index data + source-locked p-adic criterion -> certify completeness/uniqueness of rational points in all relevant residue classes, optionally with MW-sieve cleanup.
- HYPOTHESES: genus>=2; suitable rank/dimension criterion; exact local p-adic matrix/integration data; controlled MW/index information
- APPLICABILITY: receiver intersections materialized as eligible curves over Q/number fields
- DO_NOT_USE_FOR: genus-one quotient; rank inequality alone; unknown exceptional/open points

### Literature provenance
- Authors: Samir Siksek
- Title: Explicit Chabauty over number fields
- Year / journal-publisher: 2013 / Algebra & Number Theory 7(4), 765-793
- DOI: 10.2140/ant.2013.7.765
- Canonical URL: https://doi.org/10.2140/ant.2013.7.765
- Theorem/algorithm locator: Theorem 2 and Section 5
- Theorem/algorithm summary: Theorem 2 gives explicit residue-ball uniqueness under the required full-rank local matrix criterion, with finite-index Mordell-Weil control entering the computation.
- Conditional assumptions: unconditional after exact matrix/index hypotheses
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S34-W03 method-agnostic receiver and S31-W03 pullback
- Required adapter: RECEIVER_TO_GENUS_GE2_CURVE; JACOBIAN_MW_CERTIFICATE; LOCAL_CHABAUTY_MATRIX_CERTIFICATE
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: complete rational-point terminal for eligible branches
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW09

- Candidate / class / role: `QUADRATIC_CHABAUTY_TERMINAL` / **NEW_LITERATURE_WEAPON** / `QUADRATIC_CHABAUTY_INTEGRAL_POINT_TERMINAL`
- Maturity: **PROVISIONAL**
- Contract: Eligible odd-degree hyperelliptic/open curve + rank=genus data + rational MW basis + p-adic height/local data + exact MW-sieve survivor cleanup -> complete certified integral point set.
- HYPOTHESES: paper-specific odd-degree hyperelliptic setup; rank equals genus in the audited complete algorithm; sufficient MW basis and p-adic height data; exact sieve cleanup
- APPLICABILITY: branches where classical rank<genus Chabauty fails but the audited quadratic-Chabauty algorithm applies
- DO_NOT_USE_FOR: rank condition alone; missing p-adic height data; finite p-adic superset as complete point set

### Literature provenance
- Authors: Jennifer S. Balakrishnan; Amnon Besser; J. Steffen Müller
- Title: Computing integral points on hyperelliptic curves using quadratic Chabauty
- Year / journal-publisher: 2017 / Mathematics of Computation 86(305), 1403-1434
- DOI: 10.1090/mcom/3130
- Canonical URL: https://doi.org/10.1090/mcom/3130
- Theorem/algorithm locator: paper main algorithm combining quadratic Chabauty with the Mordell-Weil sieve; exact numbered algorithm was not frozen in Phase 6 (FORMAL promotion blocker until locked)
- Theorem/algorithm summary: The paper gives a complete integral-point computation in its rank=genus odd-degree hyperelliptic setting by combining quadratic Chabauty and Mordell-Weil sieve cleanup.
- Conditional assumptions: unconditional once the computational hypotheses are exact
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: future compatible S31/S34 hyperelliptic receiver
- Required adapter: INTEGRAL_RECEIVER_TO_ODD_HYPERELLIPTIC; QC_PLUS_MW_SIEVE_CERTIFICATE
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: complete integral-point set
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW10

- Candidate / class / role: `COVERING_COLLECTION_TERMINAL_ADAPTER` / **NEW_LITERATURE_WEAPON** / `EXHAUSTIVE_COVERING_COLLECTION_TERMINAL`
- Maturity: **PROVISIONAL**
- Contract: Exact source curve/receiver + exhaustive finite covering collection whose rational points cover every source rational point + exact local pruning and terminal solvers on retained covers -> complete source point classification; an empty exhaustive cover set proves nonexistence.
- HYPOTHESES: proved exhaustive finite cover family and exact maps; every retained cover closed by a proof-capable terminal
- APPLICABILITY: high-rank/awkward source problems admitting smaller cover/quotient arithmetic
- DO_NOT_USE_FOR: nonempty cover family as solved source; unproved cover exhaustiveness; local solubility as global point

### Literature provenance
- Authors: E. Victor Flynn; Joseph L. Wetherell
- Title: Covering collections and a challenge problem of Serre
- Year / journal-publisher: 2001 / Acta Arithmetica 98(2), 197-205
- DOI: 10.4064/aa98-2-9
- Canonical URL: https://doi.org/10.4064/aa98-2-9
- Theorem/algorithm locator: paper-level covering-collection plus Chabauty method; no single numbered theorem was frozen in Phase 6
- Theorem/algorithm summary: Covering collections can transport a rational-point problem to cover components where terminal Chabauty or other methods become effective, provided cover exhaustiveness is proved.
- Conditional assumptions: terminal-specific
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S34-W01 finite branches or S35-PW03 square receivers after genuine cover identification
- Required adapter: REPO_BRANCHES_TO_EXHAUSTIVE_COVERING_COLLECTION; COVER_TERMINAL_ROUTING
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: independent closure method for exact receivers
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW11

- Candidate / class / role: `FIXED_THUE_MAHLER_TERMINAL` / **NEW_LITERATURE_WEAPON** / `COMPLETE_FIXED_THUE_MAHLER_TERMINAL`
- Maturity: **PROVISIONAL**
- Contract: Fixed irreducible homogeneous F of degree>=3 + fixed nonzero a + fixed finite rational-prime support + exact gcd/content normalization + exact repo forward/converse dictionary -> complete Thue-Mahler solution set with replay.
- HYPOTHESES: fixed coefficients/support; gcd(X,Y)=1 or exact finite normalization; exact number-field arithmetic and solver prerequisites
- APPLICABILITY: S34-W01 branches normalized to a fixed Thue-Mahler equation
- DO_NOT_USE_FOR: parameter-dependent support; reducible/degree<3 form without separate reduction; height bound without enumeration

### Literature provenance
- Authors: Adela Gherga; Samir Siksek
- Title: Efficient resolution of Thue-Mahler equations
- Year / journal-publisher: 2025 / Algebra & Number Theory 19(4), 667-714
- DOI: 10.2140/ant.2025.19.667
- Canonical URL: https://doi.org/10.2140/ant.2025.19.667
- Theorem/algorithm locator: Algorithm 2.6; Proposition 2.7; Proposition 3.1; Propositions 10.2-10.3; Procedure 10.4
- Theorem/algorithm summary: The cited algorithmic chain gives a complete solver for normalized fixed-support Thue-Mahler equations using ideal covering, lattice reduction/local sieves and exact final enumeration.
- Conditional assumptions: unconditional for normalized solver input
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S34-W01 finite exhaustive squareclass branch
- Required adapter: FINITE_SQUARECLASS_BRANCH_TO_THUE_MAHLER
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: complete integer solution set for the exact branch
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW12

- Candidate / class / role: `FIXED_S_UNIT_TERMINAL` / **NEW_LITERATURE_WEAPON** / `COMPLETE_FIXED_S_UNIT_TERMINAL`
- Maturity: **PROVISIONAL**
- Contract: Fixed coefficient field + fixed finite S + exact unit-group/normalization data + repo forward/converse map -> effective S-unit solver -> complete branch solution set.
- HYPOTHESES: fixed finite S; exact coefficients/field; algorithm-specific height/unit data
- APPLICABILITY: branches normalizing to the audited fixed-support S-unit equation species
- DO_NOT_USE_FOR: S-unit finiteness as enumeration; variable S; missing unit data

### Literature provenance
- Authors: Rafael von Känel; Benjamin Matschke
- Title: Solving S-Unit, Mordell, Thue, Thue-Mahler and Generalized Ramanujan-Nagell Equations via the Shimura-Taniyama Conjecture
- Year / journal-publisher: 2023 / Memoirs of the American Mathematical Society 286(1419)
- DOI: 10.1090/memo/1419
- Canonical URL: https://doi.org/10.1090/memo/1419
- Theorem/algorithm locator: Algorithm 3.14
- Theorem/algorithm summary: The audited algorithm gives complete fixed-support S-unit solving in its Q-oriented framework from explicit effective input.
- Conditional assumptions: algorithm inputs must be explicit
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S34-W01 typed fixed-S branch or exact integral receiver
- Required adapter: FIXED_S_UNIT_EQUATION_NORMALIZER
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: complete S-unit solutions plus exact repo pullback
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW13

- Candidate / class / role: `FIXED_THUE_TERMINAL` / **NEW_LITERATURE_WEAPON** / `COMPLETE_FIXED_THUE_TERMINAL`
- Maturity: **PROVISIONAL**
- Contract: Fixed irreducible binary F in Z[X,Y] degree>=3 + fixed nonzero RHS + exact primitive/content normalization + repo forward/converse map -> complete integral solution enumeration.
- HYPOTHESES: irreducible fixed binary form degree>=3; fixed nonzero RHS; exact primitive/content normalization
- APPLICABILITY: finite branches normalized to a fixed Thue equation
- DO_NOT_USE_FOR: variable coefficients; bound-only citation; omitted exceptional/zero branches

### Literature provenance
- Authors: N. Tzanakis; B. M. M. de Weger
- Title: On the practical solution of the Thue equation
- Year / journal-publisher: 1989 / Journal of Number Theory 31(2), 99-132
- DOI: 10.1016/0022-314X(89)90014-0
- Canonical URL: https://doi.org/10.1016/0022-314X(89)90014-0
- Theorem/algorithm locator: paper-level general complete algorithm; no single top-level numbered Algorithm was located in Phase 6
- Theorem/algorithm summary: The method combines Baker bounds with computational Diophantine approximation to determine all integral solutions of a fixed irreducible Thue equation.
- Conditional assumptions: none beyond exact algorithm input
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S34-W01 fixed branch or S31 integral model
- Required adapter: FINITE_SQUARECLASS_BRANCH_TO_THUE
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: complete integral solutions for the exact branch
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW14

- Candidate / class / role: `BRAUER_MANIN_EMPTY_ADELIC_SET_TERMINAL` / **NEW_LITERATURE_WEAPON** / `BRAUER_MANIN_ADELIC_EMPTYNESS_TERMINAL`
- Maturity: **PROVISIONAL**
- Contract: Exact terminal variety/open + source-bound Brauer subgroup + complete local point/evaluation images at every required place -> compute invariant-sum compatibility; if the resulting Brauer-Manin adelic set is empty, certify no rational point.
- HYPOTHESES: valid global Brauer classes; complete relevant local populations/evaluation images; correct global reciprocity normalization
- APPLICABILITY: Stage33 classes after a certified local-evaluation adapter
- DO_NOT_USE_FOR: nonzero class alone; one local evaluation alone; incomplete place coverage; empty tested cell without exhaustive coverage

### Literature provenance
- Authors: Martin Bright; Peter Swinnerton-Dyer
- Title: Computing the Brauer-Manin obstructions
- Year / journal-publisher: 2004 / Mathematical Proceedings of the Cambridge Philosophical Society 137, 1-16
- DOI: 10.1017/S0305004104007571
- Canonical URL: https://doi.org/10.1017/S0305004104007571
- Theorem/algorithm locator: paper-level effective procedure; exact numbered theorem was not frozen in Phase 6
- Theorem/algorithm summary: The effective Brauer-Manin framework combines exact Brauer classes and local evaluations; emptiness of the exact Brauer-Manin adelic set obstructs rational points.
- Conditional assumptions: none once the exact Brauer-Manin set is computed
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: Stage33 marked/literal classes plus certified local evaluation tables
- Required adapter: LIT-PW04 SOURCE_BOUND_BRAUER_LOCAL_EVALUATION_ADAPTER
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: rational-point nonexistence when the certified Brauer-Manin set is empty
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

## LIT-PW15

- Candidate / class / role: `OPEN_DESCENT_ETALE_BRAUER_TERMINAL` / **NEW_LITERATURE_WEAPON** / `OPEN_VARIETY_DESCENT_ETALE_BRAUER_TERMINAL`
- Maturity: **PROVISIONAL**
- Contract: Smooth quasi-projective geometrically integral X/k + exact torsor/twist family + complete adelic descent/Brauer computation -> use X(A_k)^desc = X(A_k)^{et,Br}; emptiness gives a rational-point obstruction.
- HYPOTHESES: number field; smooth quasi-projective geometrically integral X; exact torsor/twist species and complete adelic computation
- APPLICABILITY: open Stage33 receivers for which proper descent theorems would be invalid
- DO_NOT_USE_FOR: unproved smooth/open model; equality theorem as emptiness; incomplete twist family

### Literature provenance
- Authors: Yang Cao; Cyril Demarche; Fei Xu
- Title: Comparing descent obstruction and Brauer-Manin obstruction for open varieties
- Year / journal-publisher: 2019 / Transactions of the American Mathematical Society 371, 8625-8650
- DOI: 10.1090/tran/7567
- Canonical URL: https://doi.org/10.1090/tran/7567
- Theorem/algorithm locator: Theorem 1.5 = Theorem 7.5
- Theorem/algorithm summary: The theorem identifies the descent adelic set with the étale-Brauer adelic set for the stated smooth quasi-projective geometrically integral varieties.
- Conditional assumptions: none beyond theorem hypotheses
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: S33-PW06/PW07 torsor/H1 semantics and S33-PW08 localization infrastructure
- Required adapter: OPEN_RECEIVER_DESCENT_ADAPTER; EXACT_TWIST_ADELIC_COMPUTATION
- Repo adapter source: this section plus named target cards; no Stage certificate is modified.
- Repo adapter verifier: registry/generator checks only in Phase 7; method-specific mathematical replay is still required.
- Expected output: descent/étale-Brauer rational-point obstruction terminal for open receivers
- Recommendation: remain **PROVISIONAL** until exact theorem locator where unresolved, repo adapter, and certificate are hostile-audited.

# New PROVISIONAL workflow

## LIT-WF01

- Candidate / class / role: `CERTIFIED_BAKER_LLL_REDUCTION_ENUMERATION` / **NEW_LITERATURE_WORKFLOW** / `BOUND_REDUCTION_ENUMERATION_REPLAY_WORKFLOW`
- Maturity: **PROVISIONAL**
- Contract: Separate proved initial height/exponent bound -> exact real/p-adic approximation lattice -> certified LLL/reduction -> exact finite enumeration region -> independent replay and repo pullback.
- HYPOTHESES: exact proved initial bound; exact approximation lattice; reproducible reduction; exact final enumeration
- APPLICABILITY: Thue/Thue-Mahler/S-unit/elliptic-log terminal implementations using very large initial bounds
- DO_NOT_USE_FOR: LLL output as theorem; reduced bound without final enumeration; S32-PW04 lower bound as exact CVP

### Literature provenance
- Authors: N. Tzanakis; B. M. M. de Weger
- Title: How to explicitly solve a Thue-Mahler equation
- Year / journal-publisher: 1992 / Compositio Mathematica 84(3), 223-288
- DOI: none
- Canonical URL: https://www.numdam.org/item/CM_1992__84_3_223_0/
- Theorem/algorithm locator: paper-level complete algorithm: logarithmic bounds -> real/p-adic reduction -> finite enumeration; corrigendum Compositio 89 (1993), 241-242
- Theorem/algorithm summary: The classical algorithm separates proof of huge bounds, real/p-adic lattice reduction, and exact finite enumeration; the workflow registers that certificate architecture, not a new Diophantine theorem.
- Conditional assumptions: solver-specific
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and output
- Repo input: future literature terminal implementation plus exact lattice infrastructure
- Required adapter: workflow/provenance layer only
- Repo adapter source: this section.
- Repo adapter verifier: generator/registry validation only; solver-specific mathematical replay remains required.
- Expected output: auditable complete-solver certificate chain

# PROVISIONAL extensions to existing IDs

## EXTENSION MW_CONTROLLED_FINITE_INDEX_INTERFACE

- Targets / role / maturity: `S31-WF01`, `S34-W02` / `CONTROLLED_FINITE_INDEX_MW_EXPORT` / **PROVISIONAL_DELTA**
- New stable ID: none
- Contract: Extend MW certification metadata to distinguish full_group_proved, subgroup generators, known index bounds and p-saturation; each downstream method must prove its quotient computation is insensitive to unresolved index.
- HYPOTHESES: exact generated subgroup plus certified index/saturation facts
- APPLICABILITY: MW sieve/Chabauty methods accepting controlled finite-index subgroups
- DO_NOT_USE_FOR: calling a finite-index subgroup the full MW group; reusing index claims at untested primes

### Literature provenance
- Authors: Nils Bruin; Michael Stoll
- Title: The Mordell-Weil sieve: proving non-existence of rational points on curves
- Year / journal-publisher: 2010 / LMS Journal of Computation and Mathematics 13, 272-306
- DOI: 10.1112/S1461157009000187
- Canonical URL: https://doi.org/10.1112/S1461157009000187
- Theorem/algorithm locator: Section 3 finite-index/finite-quotient formalism including Definition 3.1
- Theorem/algorithm summary: selected sieve operations can use a finite-index MW subgroup when the unresolved index is controlled relative to the finite quotients
- Conditional assumptions: method-specific index condition
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and delta
- Repo input: S31-WF01 strict full-group workflow; S34-W02 full-MW consumer
- Required adapter/change: existing ID metadata extension only; no new ID
- Repo adapter source: this section; target card core remains unchanged.
- Repo adapter verifier: no new mathematical verifier from registration; per-use replay required.
- Expected output / strength delta: typed finite-index/saturation export without weakening full-group credit
- Recommendation: keep target ID; only this **PROVISIONAL_DELTA** is registered.

## EXTENSION S34W01_TERMINAL_EQUATION_ROUTER_EXTENSION

- Targets / role / maturity: `S34-W01` / `TYPED_FIXED_EQUATION_BRANCH_ROUTER` / **PROVISIONAL_DELTA**
- New stable ID: none
- Contract: After the current finite exhaustive squareclass reduction, optionally emit a typed fixed equation species: S-unit, Thue, Thue-Mahler, or exact cover, with fixed coefficients/support, primitive normalization, boundary accounting and converse reconstruction.
- HYPOTHESES: current S34-W01 finite branch proof plus exact normalizer to a fixed equation species
- APPLICABILITY: surviving finite branches with fixed coefficients/support after normalization
- DO_NOT_USE_FOR: variable support; finite branch as solved equation; one-way normalization

### Literature provenance
- Authors: Adela Gherga; Samir Siksek
- Title: Efficient resolution of Thue-Mahler equations
- Year / journal-publisher: 2025 / Algebra & Number Theory 19(4), 667-714
- DOI: 10.2140/ant.2025.19.667
- Canonical URL: https://doi.org/10.2140/ant.2025.19.667
- Theorem/algorithm locator: Algorithm 2.6; Proposition 2.7; Proposition 3.1; Propositions 10.2-10.3; Procedure 10.4
- Theorem/algorithm summary: modern complete Thue-Mahler solving makes a fixed equation-species handoff materially more reusable than an undifferentiated low-genus handoff
- Conditional assumptions: solver-specific after routing
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and delta
- Repo input: S34-W01 exact finite branches
- Required adapter/change: existing S34-W01 output-schema extension only
- Repo adapter source: this section; target card core remains unchanged.
- Repo adapter verifier: no new mathematical verifier from registration; per-use replay required.
- Expected output / strength delta: typed fixed-equation terminal routing
- Recommendation: keep target ID; only this **PROVISIONAL_DELTA** is registered.

## EXTENSION F2_SYMPLECTIC_TRANSVECTION_DIRECTION_NORMAL_FORM

- Targets / role / maturity: `S32-PW06` / `F2_TRANSVECTION_DIRECTION_PARAMETERIZATION` / **PROVISIONAL_DELTA**
- New stable ID: none
- Contract: For nondegenerate symplectic (V,B) over F2, if T is symplectic, T!=I and rank(T-I)=1, directly prove the unique nonzero v with T(x)=x+B(x,v)v; im(T-I)<=W becomes v in W-{0}.
- HYPOTHESES: exact nondegenerate F2 symplectic form and exact operator satisfying the current PW06 predicate
- APPLICABILITY: S32-PW06 finite candidate pruning
- DO_NOT_USE_FOR: absolute source W-line identification; transvection-generated subgroup classification; geometric-action identity without source lock

### Literature provenance
- Authors: Harriet S. Pollatsek
- Title: Irreducible groups generated by transvections over finite fields of characteristic two
- Year / journal-publisher: 1976 / Journal of Algebra 39, 328-333
- DOI: 10.1016/0021-8693(76)90080-6
- Canonical URL: https://doi.org/10.1016/0021-8693(76)90080-6
- Theorem/algorithm locator: main characteristic-two transvection classification; exact theorem number not frozen and NOT used as proof of the elementary rank-one normal form
- Theorem/algorithm summary: literature provides the transvection structural setting; the specific rank-one normal form used here must be directly replayed in the repo adapter
- Conditional assumptions: none for the elementary normal form
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and delta
- Repo input: S32-PW06 rank-one symplectic predicate
- Required adapter/change: existing PW06 algorithm extension; source marking remains untouched
- Repo adapter source: this section; target card core remains unchanged.
- Repo adapter verifier: no new mathematical verifier from registration; per-use replay required.
- Expected output / strength delta: operator enumeration -> nonzero direction enumeration
- Recommendation: keep target ID; only this **PROVISIONAL_DELTA** is registered.

## EXTENSION FINITE_ACTION_STABILIZER_TRANSPORTER_EQUIVARIANT_MATCHER

- Targets / role / maturity: `S30-W01` / `STABILIZER_TRANSPORTER_EQUIVARIANT_MATCHER` / **PROVISIONAL_DELTA**
- New stable ID: none
- Contract: Decompose exact G-sets into orbits, compare stabilizers up to conjugacy and compute transporters/equivariant maps using strong-generating-set infrastructure; then retain the existing common/source semantic anchor gate.
- HYPOTHESES: same exact acting group and exact actions; complete orbit/stabilizer/transporter computation
- APPLICABILITY: finite action matching in S30-W01
- DO_NOT_USE_FOR: abstract G-set equivalence as semantic source identity

### Literature provenance
- Authors: Ákos Seress
- Title: Permutation Group Algorithms
- Year / journal-publisher: 2003 / Cambridge Tracts in Mathematics 152
- DOI: 10.1017/CBO9780511546549
- Canonical URL: https://doi.org/10.1017/CBO9780511546549
- Theorem/algorithm locator: Chapters 4-6 and 9
- Theorem/algorithm summary: standard permutation-group algorithms replace raw relabeling search with structured orbit/stabilizer/transporter computation
- Conditional assumptions: algorithmic only
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and delta
- Repo input: S30-W01 exact source/target actions
- Required adapter/change: retain common/source anchor and existing semantic checks
- Repo adapter source: this section; target card core remains unchanged.
- Repo adapter verifier: no new mathematical verifier from registration; per-use replay required.
- Expected output / strength delta: same adapter credit with smaller candidate search
- Recommendation: keep target ID; only this **PROVISIONAL_DELTA** is registered.

## EXTENSION GENERATOR_COMPLETE_SEMILINEAR_COMPATIBILITY_VERIFIER

- Targets / role / maturity: `S30-W02` / `GENERATOR_RELATOR_SEMILINEAR_VERIFIER` / **PROVISIONAL_DELTA**
- New stable ID: none
- Contract: Once both sides of the semilinear compatibility equation are certified homomorphisms from the same generated/presented group, verify equality on generators plus relators instead of rescanning every group element.
- HYPOTHESES: certified homomorphisms; exact presentation/generators; exact sigma, theta and cocycle/deck element
- APPLICABILITY: finite semilinear descent with separately proved homomorphism structure
- DO_NOT_USE_FOR: generator spot checks before homomorphism certification; copied cocycle/sign data

### Literature provenance
- Authors: Jean-Pierre Serre
- Title: Galois Cohomology
- Year / journal-publisher: 1997 / Springer Monographs in Mathematics
- DOI: none
- Canonical URL: https://link.springer.com/book/9783540619901
- Theorem/algorithm locator: nonabelian cocycle/descent framework; equality-on-generators is elementary and has no separate theorem number
- Theorem/algorithm summary: standard nonabelian descent supplies the cocycle framework; equality of homomorphisms on generators is elementary once homomorphism certification is complete
- Conditional assumptions: none
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and delta
- Repo input: S30-W02 all-element semilinear certificate
- Required adapter/change: existing verifier-mode extension; source cocycle semantics unchanged
- Repo adapter source: this section; target card core remains unchanged.
- Repo adapter verifier: no new mathematical verifier from registration; per-use replay required.
- Expected output / strength delta: all-element scan -> generator/relator replay
- Recommendation: keep target ID; only this **PROVISIONAL_DELTA** is registered.

## EXTENSION REVERSIBLE_INTEGER_MODULE_NORMAL_FORM_ADAPTER

- Targets / role / maturity: `S32-PW03`, `S32-PW04`, `S33-PW02` / `REVERSIBLE_HNF_SNF_COORDINATE_LAYER` / **PROVISIONAL_DELTA**
- New stable ID: none
- Contract: Given an exact integer matrix/presentation, compute HNF/SNF together with unimodular multiplier matrices and explicit forward/inverse coordinate transforms; expose image membership, invariant factors and reversible coordinates.
- HYPOTHESES: exact integer matrix and locked source/target bases
- APPLICABILITY: lattice image gates, finite quotient presentations and finite-module normal forms
- DO_NOT_USE_FOR: changed marking without adapter; quotient reachability without exact map; theorem/endpoint credit from normal form

### Literature provenance
- Authors: Ravindran Kannan; Achim Bachem
- Title: Polynomial Algorithms for Computing the Smith and Hermite Normal Forms of an Integer Matrix
- Year / journal-publisher: 1979 / SIAM Journal on Computing 8(4), 499-507
- DOI: 10.1137/0208040
- Canonical URL: https://doi.org/10.1137/0208040
- Theorem/algorithm locator: paper-level HNF/SNF algorithms with multiplier matrices; no single numbered theorem frozen in Phase 6
- Theorem/algorithm summary: the algorithms provide exact HNF/SNF with reversible transformation information and polynomial bit-complexity guarantees
- Conditional assumptions: none
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and delta
- Repo input: existing exact integer matrices/presentations
- Required adapter/change: factor common exact-normal-form layer; no semantic credit change
- Repo adapter source: this section; target card core remains unchanged.
- Repo adapter verifier: no new mathematical verifier from registration; per-use replay required.
- Expected output / strength delta: one reusable reversible integer-module interface
- Recommendation: keep target ID; only this **PROVISIONAL_DELTA** is registered.

## EXTENSION FINITE_LATTICE_QUOTIENT_SATURATION_ADAPTER

- Targets / role / maturity: `S32-PW03`, `S32-PW04` / `EXACT_LATTICE_IMAGE_QUOTIENT_SATURATION_LAYER` / **PROVISIONAL_DELTA**
- New stable ID: none
- Contract: Exact lattice homomorphism + HNF/SNF transforms -> compute image, saturation/index, finite quotient invariant factors and exact reachable subgroup before any classwise bound.
- HYPOTHESES: exact integer lattices/maps and locked bases
- APPLICABILITY: finite quotient/class reachability problems underlying PW03/PW04
- DO_NOT_USE_FOR: ambient quotient as reachable image; lower bound as exact CVP; floating saturation

### Literature provenance
- Authors: Costas S. Iliopoulos; Ravindran Kannan; Achim Bachem
- Title: Worst-Case Complexity Bounds on Algorithms for Computing the Canonical Structure of Finite Abelian Groups and the Hermite and Smith Normal Forms of an Integer Matrix / Polynomial Algorithms for Computing the Smith and Hermite Normal Forms of an Integer Matrix
- Year / journal-publisher: 1989/1979 / SIAM Journal on Computing 18(4) / 8(4)
- DOI: 10.1137/0218045; 10.1137/0208040
- Canonical URL: https://doi.org/10.1137/0218045 ; https://doi.org/10.1137/0208040
- Theorem/algorithm locator: paper-level canonical finite-abelian-group/HNF/SNF algorithms; exact numbered theorem not frozen
- Theorem/algorithm summary: canonical normal-form algorithms support exact quotient structure; the reachable-image proof remains repo-specific data
- Conditional assumptions: none
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and delta
- Repo input: S32-PW03 image gate and S32-PW04 Smith-reduced reachable classes
- Required adapter/change: existing lattice-card extension only
- Repo adapter source: this section; target card core remains unchanged.
- Repo adapter verifier: no new mathematical verifier from registration; per-use replay required.
- Expected output / strength delta: instance-specific quotient reduction -> reusable canonical quotient/saturation layer
- Recommendation: keep target ID; only this **PROVISIONAL_DELTA** is registered.

## EXTENSION FINITE_MODULE_INTERTWINER_ISOMORPHISM_SOLVER

- Targets / role / maturity: `S33-PW05` / `CONSTRUCTIVE_FINITE_MODULE_INTERTWINER_SOLVER` / **PROVISIONAL_DELTA**
- New stable ID: none
- Contract: Given exact module generator matrices over a fixed field, decide module isomorphism/compatibility and construct an invertible intertwiner when it exists; apply the existing marked/source semantic gate separately.
- HYPOTHESES: finite-dimensional modules over the same finite-dimensional algebra/field with exact matrices
- APPLICABILITY: future S33 source-target module compatibility systems
- DO_NOT_USE_FOR: intertwiner as geometric identification; dimension-only binding; changed marking

### Literature provenance
- Authors: Alexander Chistov; Gábor Ivanyos; Marek Karpinski
- Title: Polynomial time algorithms for modules over finite dimensional algebras
- Year / journal-publisher: 1997 / ISSAC 1997 Proceedings, 68-74
- DOI: 10.1145/258726.258751
- Canonical URL: https://doi.org/10.1145/258726.258751
- Theorem/algorithm locator: constructive module-isomorphism algorithm; exact numbered item not frozen in Phase 6
- Theorem/algorithm summary: constructive polynomial-time module-isomorphism algorithms can replace brute search for invertible intertwiners in the supported module model
- Conditional assumptions: algorithm-model assumptions
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and delta
- Repo input: S33-PW05 exact compatibility equations
- Required adapter/change: semantic S33-PW04/source lock remains mandatory
- Repo adapter source: this section; target card core remains unchanged.
- Repo adapter verifier: no new mathematical verifier from registration; per-use replay required.
- Expected output / strength delta: generic constructive intertwiner solver
- Recommendation: keep target ID; only this **PROVISIONAL_DELTA** is registered.

## EXTENSION ORBITAL_DOUBLE_COSET_RECONSTRUCTION_ENGINE

- Targets / role / maturity: `S32-PW05`, `S30-W03` / `ORBITAL_DOUBLE_COSET_FINITE_RECONSTRUCTION` / **PROVISIONAL_DELTA**
- New stable ID: none
- Contract: Use strong generating sets, point stabilizers and orbitals/double-coset representatives to identify required pair/state orbits; propagate only from certified representatives while retaining complete coverage/conflict checks.
- HYPOTHESES: validated finite action and exact invariant relation
- APPLICABILITY: large finite relation-table reconstruction and marked finite-state transport
- DO_NOT_USE_FOR: orbit representative as semantic label; incomplete orbital coverage; skipped conflict checks

### Literature provenance
- Authors: Ákos Seress
- Title: Permutation Group Algorithms
- Year / journal-publisher: 2003 / Cambridge Tracts in Mathematics 152
- DOI: 10.1017/CBO9780511546549
- Canonical URL: https://doi.org/10.1017/CBO9780511546549
- Theorem/algorithm locator: Chapters 4-6 and 9
- Theorem/algorithm summary: standard orbit/stabilizer infrastructure computes pair orbitals without materializing all pairs during orbit discovery
- Conditional assumptions: algorithmic only
- Source type: original peer-reviewed work or authoritative monograph as identified above

### Repo provenance and delta
- Repo input: S32-PW05 relation reconstruction and S30-W03 finite transport
- Required adapter/change: existing validated action/invariance and source semantics remain required
- Repo adapter source: this section; target card core remains unchanged.
- Repo adapter verifier: no new mathematical verifier from registration; per-use replay required.
- Expected output / strength delta: full pair/state scan -> orbital representative engine
- Recommendation: keep target ID; only this **PROVISIONAL_DELTA** is registered.

# SOURCE_ANCHOR_ONLY

## SOURCE ANCHOR GENUS_ONE_NDESCENT_SOURCE_ANCHOR

- Targets / class / new ID: `S31-W01` / **SOURCE_ANCHOR_ONLY** / none
- Authors: J. E. Cremona; T. A. Fisher; C. O'Neil; D. Simon; M. Stoll
- Title: Explicit n-descent on elliptic curves, I. Algebra / II. Geometry
- Year / journal: 2008/2009 / Journal für die reine und angewandte Mathematik
- DOI: 10.1515/CRELLE.2008.012; 10.1515/CRELLE.2009.050
- Canonical URL: https://doi.org/10.1515/CRELLE.2008.012 ; https://doi.org/10.1515/CRELLE.2009.050
- Theorem/algorithm locator: paper-level n-descent/genus-one model constructions; exact selected theorem number must be locked before any formal literature extension
- Exact use: source provenance only; exact repo forward/inverse maps, exceptional loci and integrality firewall are unchanged
- Conditionality: exact theorem/coefficient/model hypotheses must match before theorem use.
- Repo adapter source/verifier: existing target source and verifier; unchanged.
- DO_NOT_USE_FOR: output strengthening, stage credit, or replacement of repo marking/valuation/exceptional-locus data.

## SOURCE ANCHOR GERSTEN_PURITY_THEOREM_ANCHOR

- Targets / class / new ID: `S33-PW08`, `S33-PW10` / **SOURCE_ANCHOR_ONLY** / none
- Authors: Spencer Bloch; Arthur Ogus
- Title: Gersten's conjecture and the homology of schemes
- Year / journal: 1974 / Annales scientifiques de l'École Normale Supérieure 7, 181-201
- DOI: 10.24033/asens.1266
- Canonical URL: https://doi.org/10.24033/asens.1266
- Theorem/algorithm locator: Gersten/coniveau exactness results; exact coefficient-setting theorem must match the repo implementation
- Exact use: source provenance only; repo valuation attachment, exceptional divisors and literal purity correction remain unchanged
- Conditionality: exact theorem/coefficient/model hypotheses must match before theorem use.
- Repo adapter source/verifier: existing target source and verifier; unchanged.
- DO_NOT_USE_FOR: output strengthening, stage credit, or replacement of repo marking/valuation/exceptional-locus data.

# Inactive Phase-6 items

- REJECT_DUPLICATE: `DISC-S35-A02`, `DISC-S35-A09`.
- NOT_APPLICABLE: `KUMMER_TRANSCENDENTAL_BRAUER_COMPARISON_ADAPTER`, `CLASSICAL_GROUP_CONSTRUCTIVE_RECOGNITION_GATE`.
- RESEARCH_GAP: `PARAMETRIC_RESERVOIR_FINITE_SUPPORT_CERTIFICATE`, `NORM_FORM_BOUND_AND_TERMINAL_ADAPTER`, `KUMMER_SECOND_DESCENT_ADAPTER`, `CURVE_FINITE_ABELIAN_DESCENT_TERMINAL`, `TRANSVECTION_GENERATED_SUBGROUP_CLASSIFIER`.
- POSSIBLY_NOVEL: none.

Search misses never set `NOVEL=true`, `FIRST_PROOF=true`, or `NEW_THEOREM=true`.

# Credit firewall

```text
LITERATURE_ARSENAL_REGISTRATION_DOES_NOT_CHANGE_STAGE_MATHEMATICAL_AUTHORITY=true
STAGE30_PROGRESS_INCREMENT=0
STAGE31_PROGRESS_INCREMENT=0
STAGE32_PROGRESS_INCREMENT=0
STAGE33_PROGRESS_INCREMENT=0
STAGE34_PROGRESS_INCREMENT=0
STAGE35_PROGRESS_INCREMENT=0
STAGE35_EX_PROGRESS_INCREMENT=0
STAGE36_EXCLUDED=true
ENDPOINT_CREDIT_ADDED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

This is the authoritative literature-strengthening source. Cards/catalog are generated derivatives. No literature-backed registration is FORMAL before hostile audit.
