# Research Arsenal × Literature Strengthening Audit — Phase 2 Elliptic / Mordell–Weil / Rational-Point Methods

```text
ARSENAL_BASE_MAIN=9306238c7ada55e31311245019d6b7e474ad837f
STAGE36_EXCLUDED=true
STAGE35_PROVISIONAL_COMPARISON_HEAD=3fc684677ef1570a820420079088667f558e0983
LITERATURE_DISCOVERY_ONLY=true
ARSENAL_AUTHORITY_CHANGED=false
STABLE_ID_CREATED=false
```

This phase compares the frozen Phase-1 Arsenal contracts to original peer-reviewed literature where available. It does not promote a theorem, weaken a card, infer novelty from a search miss, or change Stage authority. Stage35 cards remain below active Stage35 authority.

## 1. Reviewed Arsenal surface

Primary: `S31-W01`, `S31-W02`, `S31-W03`, `S31-WF01`, `S34-W02`, `S34-W03`, `S35-PW02`, `S35-PW03`, `S35-PW04`.

Phase-1 routed bridge checks: `S34-W01`, `S35-PW01`, `S35-PW05`. `S35-PW05` is retained only to record that its Hasse–Weil exceptional-prime interface is outside the elliptic/MW theorem family studied here.

## 2. Literature families reviewed

### L2-MW01 — general Mordell–Weil sieve

Nils Bruin and Michael Stoll, *The Mordell–Weil sieve: proving non-existence of rational points on curves*, LMS Journal of Computation and Mathematics **13** (2010), 272–306. DOI `10.1112/S1461157009000187`. Relevant locator: §3 finite-quotient/finite-index formalism (including Definition 3.1), plus the later local-information sections.

Literature interface: a finitely generated Mordell–Weil group or controlled finite-index subgroup `Gamma`, exact homomorphisms to finite abelian quotients `phi_i: Gamma -> G_i`, and exact admissible subsets `X_i <= G_i` arising from the local image of the curve/receiver. Empty intersection of the inverse images certifies nonexistence. The local quotients need not be only `J(F_p)` at good primes: the paper explicitly develops information beyond good-prime mod-`p`, including bad-reduction and deeper local information in its genus-two implementation.

Classification for `S34-W02`: **DIRECT_STRENGTHENING + ADAPTER_STRENGTHENING**.

Direct strengthening available without changing the semantic output:

```text
current:
full MW lattice + good-prime residue predicates + generalized CRT
-> empty residue set => no receiver-compatible Q-point

literature-generalized:
controlled MW lattice/subgroup Gamma
+ arbitrary exact finite quotients phi_i: Gamma -> G_i
+ exact local admissible subsets X_i
-> intersection_i phi_i^-1(X_i)=empty
=> no receiver-compatible Q-point
```

This strictly generalizes the rank-one/cyclic-coordinate CRT presentation to arbitrary MW rank and arbitrary finite abelian quotient data. It also permits a full-rank finite-index subgroup instead of a proved full group when the index is explicitly controlled relative to the local quotients; that is a hypothesis-management strengthening, not permission to call an unsaturated subgroup the full Mordell–Weil group.

Missing repo adapters for the stronger interface:

1. `RECEIVER_TO_LOCAL_IMAGE_SUBSET`: evaluate the exact parent/receiver predicates on the chosen local quotient and produce a conservative exact `X_i`, including poles, zeros and degeneracies.
2. `LOCAL_MW_QUOTIENT_MATERIALIZER`: source-lock good-prime reduction, bad-prime component/Néron data, or deeper `p^n`/kernel-of-reduction quotient data.
3. `FINITE_INDEX_MW_CONTROL`: expose a proved index bound and/or the primes at which the known subgroup is saturated so all missing cosets are accounted for.
4. For a general higher-genus curve rather than the current elliptic quotient, `RECEIVER_CURVE_TO_JACOBIAN`: exact curve/Jacobian embedding and source-population adapter.

The current Stage34 instance already supplies a valid special case of the abstract sieve because its good-prime congruence classes are finite quotient preimages. The bad/deep/general-Jacobian upgrades are not automatic from the frozen card.

### L2-CH01 — Chabauty–Coleman

Robert F. Coleman, *Effective Chabauty*, Duke Mathematical Journal **52** (1985), 765–770. DOI `10.1215/S0012-7094-85-05240-8`.

For a smooth projective curve over `Q` of genus `g>=2` with `rank J(Q)<g`, Coleman gives an effective `p`-adic method; at good primes `p>2g` the standard Coleman bound is `#C(Q) <= #C(F_p)+2g-2`.

Classification: **NEW_TERMINAL_METHOD** for `S34-W03` / upstream `S31-W03`, conditional on an exact receiver-to-curve adapter and the rank hypothesis. **NOT_APPLICABLE** as a direct strengthening of the genus-one `S34-W02` elliptic quotient interface: classical Chabauty requires genus at least two and the relevant rank inequality.

### L2-CH02 — elliptic Chabauty

Nils Bruin, *Chabauty methods using elliptic curves*, Journal für die reine und angewandte Mathematik **562** (2003), 27–49. DOI `10.1515/crll.2003.076`. Relevant local criterion: §4, including Lemma 4.3.

The method studies a curve over a base field through an elliptic curve over an extension and imposes a base-field rationality condition on the elliptic image. The usable dimension condition is local: enough completions over a rational prime must provide more independent local conditions than the rank of the known Mordell–Weil subgroup; a finite-index subgroup prime-to-the residue characteristic can suffice.

Classification: **NEW_TERMINAL_METHOD + ADAPTER_STRENGTHENING** for `S35-PW02`, `S35-PW03`, or `S34-W03` only when an exact quotient/cover produces the required elliptic-over-extension plus base-field image condition. Merely having an elliptic quotient over `Q` does not meet this hypothesis.

### L2-CH03 — explicit Chabauty over number fields

Samir Siksek, *Explicit Chabauty over number fields*, Algebra & Number Theory **7** (2013), 765–793. DOI `10.2140/ant.2013.7.765`. Relevant locator: Theorem 2 and §5.

Input: smooth projective absolutely irreducible `C/K`, genus `g>=2`, `d=[K:Q]`, rank `r`; the practical criterion is dimensionally favorable around `r<=d(g-1)`, but this inequality alone is not a termination theorem. Theorem 2 gives a local uniqueness criterion by a full-rank matrix condition. The method can work with a finite-index Mordell–Weil subgroup while tracking index/saturation information.

Classification: **NEW_TERMINAL_METHOD** for number-field receiver curves, and **ADAPTER_STRENGTHENING** for `S31-W03`/`S34-W03`. It also supports a Phase-6 finite-index-control extension adjacent to `S31-WF01` without weakening that workflow's meaning of “full MW group”.

### L2-QC01 — quadratic Chabauty for integral hyperelliptic points

Jennifer S. Balakrishnan, Amnon Besser and J. Steffen Müller, *Quadratic Chabauty: p-adic heights and integral points on hyperelliptic curves*, Journal für die reine und angewandte Mathematik **720** (2016), 51–79. DOI `10.1515/crelle-2014-0048`.

For the hyperelliptic setup in the paper, when the Mordell–Weil rank equals the genus, the method gives `p`-adic approximations/bounds for `p`-integral points and only requires a basis of `J(Q) tensor Q`, rather than a certified integral full basis.

Jennifer S. Balakrishnan, Amnon Besser and J. Steffen Müller, *Computing integral points on hyperelliptic curves using quadratic Chabauty*, Mathematics of Computation **86** (2017), 1403–1434. DOI `10.1090/mcom/3130`. For odd-degree hyperelliptic curves over `Q` with genus equal to the Jacobian rank, it combines the quadratic-Chabauty `p`-adic approximation with the Mordell–Weil sieve to determine integral points.

Classification: **NEW_TERMINAL_METHOD** downstream of `S31-W02` if the exact auxiliary/source object is put into the required odd-degree hyperelliptic/integral model and the MW/p-adic data are certified. It strengthens the terminal solver, not `S31-W02`'s iff integral-transfer lemma itself.

### L2-QC02 — quadratic Chabauty for rational points

Jennifer S. Balakrishnan and Netan Dogra, *Quadratic Chabauty and rational points, I: p-adic heights*, Duke Mathematical Journal **167** (2018), 1981–2038. DOI `10.1215/00127094-2018-0013`.

The broad finiteness inequality is controlled by Mordell–Weil rank and Néron–Severi rank (in the standard form `r < g + rho - 1`); the paper gives explicit rank-equals-genus examples under extra Néron–Severi/p-adic-height structure. Exact use requires the relevant cycles/heights and local calculations, not just the numerical inequality.

Classification: **NEW_TERMINAL_METHOD / RESEARCH_GAP** for `S34-W03` and Stage35-derived genus-`>=2` receivers. No frozen repo card by itself establishes the Néron–Severi and `p`-adic height input needed for automatic use.

### L2-EL01 — elliptic-logarithm / S-integral closure

Attila Pethő, Horst G. Zimmer, Josef Gebel and Emanuel Herrmann, *Computing all S-integral points on elliptic curves*, Mathematical Proceedings of the Cambridge Philosophical Society **127** (1999), 383–402. DOI `10.1017/S0305004199003916`. The paper gives an algorithm for all `S`-integral points on rational Weierstrass elliptic curves by combining Siegel–Baker–Coates and Lang–Zagier/elliptic-logarithm techniques.

Rafael von Känel and Benjamin Matschke, *Solving S-Unit, Mordell, Thue, Thue–Mahler and Generalized Ramanujan–Nagell Equations via the Shimura–Taniyama Conjecture*, Memoirs of the AMS **286**, no. 1419 (2023). DOI `10.1090/memo/1419`. Algorithm 11.19 gives a particularly explicit modern interface: integral Weierstrass model, finite `S`, a basis of the free part of `E(Q)`, and an explicit initial canonical-height bound for every `S`-integral point; output is the complete `S`-integral point set.

Classification: **NEW_TERMINAL_METHOD** for `S31-W02` (and potentially `S35-PW03`) after an exact `repo receiver -> S-integral Weierstrass point` adapter. Missing load-bearing input is not just the MW basis: the required integrality/S-integrality dictionary and explicit initial height bound must be source-locked. This method is complementary to `S34-W02`: it can enumerate all `S`-integral points with a height bound, while MW-sieve exclusion can be globally empty without a height cutoff.

### L2-COV01 — covering collections / two-cover descent

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic curves*, Mathematics of Computation **78** (2009), 2347–2370. DOI `10.1090/S0025-5718-09-02255-8`. The algorithm returns a set of unramified covers through which every rational point lifts; an empty returned set proves that the curve has no rational points.

E. Victor Flynn and Joseph L. Wetherell, *Covering collections and a challenge problem of Serre*, Acta Arithmetica **98** (2001), 197–205. DOI `10.4064/aa98-2-9`. This is a concrete covering-collection plus Chabauty realization.

Classification: **NEW_TERMINAL_METHOD + ADAPTER_STRENGTHENING** for `S34-W01`, `S34-W03`, and especially `S35-PW03`. The Stage35 simultaneous-square normal form is not yet a literature-certified 2-cover/Selmer object merely because it looks Kummer-like. A source-locked covering map / torsor class / local-solubility adapter is required.

### L2-DESC01 — explicit 2/3/4 descent and genus-one models

J. E. Cremona, T. A. Fisher, C. O'Neil, D. Simon and M. Stoll, *Explicit n-descent on elliptic curves, I. Algebra*, J. Reine Angew. Math. **615** (2008), 121–155. DOI `10.1515/CRELLE.2008.012`.

Same authors, *Explicit n-descent on elliptic curves, II. Geometry*, J. Reine Angew. Math. **632** (2009), 63–84. DOI `10.1515/CRELLE.2009.050`.

J. E. Cremona, T. A. Fisher and M. Stoll, *Minimisation and reduction of 2-, 3- and 4-coverings of elliptic curves*, Algebra & Number Theory **4** (2010), 763–820. DOI `10.2140/ant.2010.4.763`.

These papers identify and realize Selmer elements as explicit genus-one covering models and provide minimisation/reduction algorithms for degrees 2, 3 and 4.

Classification for `S31-W01`: **SOURCE_ANCHOR_ONLY + ADAPTER_STRENGTHENING**. The general literature strongly anchors quartic/genus-one-to-Jacobian model theory, but it does not replace the repo's exact forward/inverse map, denominator and exceptional-locus certificate. Classification for `S35-PW03`: **ADAPTER_STRENGTHENING / RESEARCH_GAP** until the exact simultaneous-square receiver is proved to be the claimed covering/Selmer object.

### L2-MW02 — saturation / finite-index control

Samir Siksek, *Infinite Descent on Elliptic Curves*, Rocky Mountain Journal of Mathematics **25** (1995), 1501–1538. DOI `10.1216/rmjm/1181072159`, together with later descent/saturation implementations, supplies literature support for proving/controling finite index and saturation rather than conflating found generators with a full Mordell–Weil group.

Classification for `S31-WF01`: **SOURCE_ANCHOR_ONLY** for the existing full-group workflow. Phase 2 separately identifies an **ADAPTER_STRENGTHENING** opportunity: expose `known_index_bound`, `saturated_at_primes`, and `index_coprimality_conditions` so downstream MW-sieve/Chabauty methods can legally use a finite-index subgroup without changing the meaning of `full_group_proved`.

## 3. Card-by-card hostile classification

| Arsenal card | Verdict | Exact Phase-2 conclusion |
|---|---|---|
| `S31-W01` | SOURCE_ANCHOR_ONLY / ADAPTER_STRENGTHENING | Explicit n-descent literature canonicalizes genus-one/cover models, but the repo exact rational maps and exceptional loci remain indispensable. |
| `S31-W02` | NEW_TERMINAL_METHOD downstream | Elliptic-log and quadratic-Chabauty algorithms can replace/augment the complete auxiliary solver only after exact integral/S-integral model and height/MW hypotheses are built. The transfer lemma itself is already the right interface. |
| `S31-W03` | DUPLICATE_OF_EXISTING as pullback discipline; NEW_TERMINAL_METHOD upstream | Literature solvers can supply the complete auxiliary point set; exhaustive source reconstruction remains repo-specific and should not be replaced. |
| `S31-WF01` | SOURCE_ANCHOR_ONLY + ADAPTER_STRENGTHENING | Preserve strict full-group semantics; add a separate controlled-finite-index output interface for methods that only need saturation/index conditions. |
| `S34-W01` | ADAPTER_STRENGTHENING | Finite squareclass branches can feed covering collections/descent, but each branch needs an exact cover/torsor identification. |
| `S34-W02` | DIRECT_STRENGTHENING + ADAPTER_STRENGTHENING | Generalize from good-prime coefficient CRT to arbitrary finite MW quotients/local admissible subsets, arbitrary rank, controlled finite-index subgroups, bad/deep local information. |
| `S34-W03` | NEW_TERMINAL_METHOD router | Chabauty, elliptic Chabauty, quadratic Chabauty, MW sieve, or two-cover descent can certify the joint receiver intersection when their exact curve/field/rank hypotheses are met. |
| `S35-PW01` | RESEARCH_GAP | Live parameter-dependent reservoirs are not a fixed finite-support descent/covering collection. A finite-support theorem is required before the reviewed terminal methods become applicable. |
| `S35-PW02` | ADAPTER_STRENGTHENING | Exact involution quotient is a good preterminal adapter; elliptic/number-field Chabauty requires a further exact curve/extension/rationality dictionary. |
| `S35-PW03` | ADAPTER_STRENGTHENING / RESEARCH_GAP | Strong candidate to identify with an explicit 2-covering/covering collection, but Kummer-style square equations alone do not establish a Selmer/torsor covering class. |
| `S35-PW04` | DUPLICATE_OF_EXISTING for algebraic compression / SOURCE_ANCHOR_ONLY | Literature birational simplification does not improve the exact iff compression contract; use the smaller receiver as input to a terminal method. |
| `S35-PW05` | NOT_APPLICABLE in Phase 2 | Its theorem family is finite-field point counting / Hasse–Weil, not elliptic MW/rational-point closure; retain Phase-1 routing to the separate local/counting audit. |

## 4. Exact proposed strengthening boundary for S34-W02

Phase-6 candidate contract, not yet an Arsenal change:

```text
INPUT:
  finitely generated MW lattice/subgroup Gamma in E(Q) or J(Q)
  + exact finite-index/saturation status sufficient for all chosen quotients
  + exact finite quotient maps phi_i: Gamma -> G_i
  + exact receiver-local admissible subsets X_i subset G_i
  + complete torsion/coset accounting required by the chosen Gamma

ALLOWED LOCAL SOURCES:
  good-prime reduction
  bad-prime component/Neron information when explicitly materialized
  deeper p-adic / p^n quotient information when explicitly materialized
  multiple primes and non-cyclic finite quotients

OUTPUT:
  if intersection_i phi_i^-1(X_i) is empty after all required cosets,
  then there is no rational point compatible with the exact receiver.

NO CREDIT:
  nonempty sieve set => rational point
  uncontrolled finite-index subgroup => full MW coverage
  abstract local quotient => receiver predicate adapter
  eventual MW-sieve success without a proved termination theorem
```

Thus the strongest safe statement is not “replace S34-W02 by the Mordell–Weil sieve.” It is: **S34-W02 is a formal rank-one/good-prime specialization of a broader finite-quotient MW-sieve interface; the broader interface needs three concrete new adapters (receiver-local subsets, local quotient materialization, finite-index control), and a fourth curve-to-Jacobian adapter for general higher-genus use.**

## 5. Phase-6 candidate manifest

| Candidate | Targets | Class | Gate before promotion |
|---|---|---|---|
| `MW_SIEVE_GENERAL_FINITE_QUOTIENT_EXTENSION` | `S34-W02` | DIRECT_STRENGTHENING + ADAPTER_STRENGTHENING | Implement exact `phi_i/G_i/X_i`, coset/index accounting, and hostile examples for good/bad/deep local data. |
| `MW_CONTROLLED_FINITE_INDEX_INTERFACE` | `S31-WF01`, `S34-W02` | ADAPTER_STRENGTHENING | Separate `full_group_proved` from `known_index_bound` / `p_saturated`; prove downstream sufficiency per method. |
| `ELLIPTIC_LOG_SINTEGRAL_TERMINAL` | `S31-W02`, `S34-W03` | NEW_TERMINAL_METHOD | Exact Weierstrass/S-integral dictionary, MW basis, explicit initial height bound, complete algorithm certificate. |
| `CHABAUTY_TERMINAL_ROUTER` | `S34-W03`, `S31-W03` | NEW_TERMINAL_METHOD | Exact genus>=2 curve, Jacobian/MW data, field/rank inequality, p-adic local criterion and survivor elimination. |
| `ELLIPTIC_CHABAUTY_EXTENSION_ADAPTER` | `S35-PW02`, `S35-PW03`, `S34-W03` | ADAPTER_STRENGTHENING + NEW_TERMINAL_METHOD | Produce elliptic curve over extension + base-field image condition + rank/index/local-log certificate. |
| `QUADRATIC_CHABAUTY_TERMINAL` | `S31-W02`, `S34-W03` | NEW_TERMINAL_METHOD / RESEARCH_GAP | Hyperelliptic or general QC hypotheses, rank/NS data, p-adic heights/local contributions, exact finite survivor cleanup. |
| `COVERING_COLLECTION_TERMINAL_ADAPTER` | `S34-W01`, `S35-PW03`, `S34-W03` | ADAPTER_STRENGTHENING + NEW_TERMINAL_METHOD | Prove explicit cover/torsor/Selmer identity; local solubility and exhaustive cover family; then apply Chabauty/MW sieve as needed. |
| `GENUS_ONE_NDESCENT_SOURCE_ANCHOR` | `S31-W01` | SOURCE_ANCHOR_ONLY | Add literature source locks only; do not remove repo forward/inverse/exceptional-locus checks. |

## 6. Stop boundary

No existing Arsenal contract is weakened. No literature method is claimed applicable solely from equation shape, genus-one labels, matching `j`, Kummer-looking squares, rank, or a CAS generator list. `NO_DIRECT_MATCH_FOUND_IN_THIS_SEARCH` is not a novelty statement. Phase 2 ends with routing/strengthening candidates only; promotion, stable IDs and Arsenal edits are reserved for later phases.