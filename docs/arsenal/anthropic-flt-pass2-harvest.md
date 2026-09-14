# Anthropic FLT second-pass internal-lemma harvest

Date: 2026-09-14. Status: PROVISIONAL_SOURCE_INSPECTION_ONLY.
External commit: `aa2d8b34692b16c70f699536de0d8e75b9a3e9ef`. Extends the three cards from [pass one](anthropic-flt-provisional-harvest.md); no previous card is upgraded.
Registry baseline for this pass: `e1a7d3459e8afea76bd64e4e8e751a395fddb280`.

## Scope, evidence and dedup

The second pass searched the already obtained nonrecursive theorem metadata by arithmetic, torsion/reduction, Selmer, norm, Riemann-Roch/gluing and descent symbols. Eleven selected public theorem statements were inspected. Selected proof bodies/dependencies were inspected only in bounded excerpts (the short norm, 3/5 classification and torsion-injectivity proofs were read fully). No transitive proof audit, Lean build, comparator or independent-kernel replay was run.

[Machine-readable source locks](anthropic-flt-pass2-source-locks.json) pin each chosen statement and proof blob; screening decisions are recorded below. These hashes are provenance, not proof acceptance. A source name, source-reported successful build or registry PASS is not a local mathematical audit.

Dedup used the canonical registry and relevant source sections for S30-W02, S31-W01/WF01, S32-PW09, S33-PW09, S34-W01, S36-PW05/PW06 and LIT-PW03/PW04/PW06. Six new contracts have distinct inputs/outputs; no claim of exhaustive branch-history novelty. Speculative consumer suggestions below do not alter any live Stage assignment or authorize re-opening a stopped route.

All cards retain zero Stage pruning, receiver, effectivity, theorem and endpoint credit. Each requires exact receiver/model/field adapters and independent validation before authoritative use. No mathematical computation or heavy workflow was launched. No upstream code is vendored; see the pinned upstream LICENSE/NOTICE/ATTRIBUTION linked in pass one.

## FLT-PW03 — UNRAMIFIED_LOCAL_NORM_VALUATION_GATE

Maturity: PROVISIONAL. Source-inspected contract, not locally kernel-verified.

Input: number fields E -> M, a finite place v of E and a specified place w above it; ramification index e(w/v)=1; a nonzero element x of E_v. Let f be the residue degree. Output: x is a norm from M_w exactly when its normalized valuation is divisible by f. The Lean version states multiplicative valuation = exp(f*k), k in Z, so the valuation sign/normalization must be matched explicitly.

Cuboid application (conditional): once a squareclass/norm receiver has an exact equation N(y)=x over the same fields, a valuation failing the test excludes that local branch. For an unramified quadratic local field extension (f=2), this is a parity gate. A failed necessary local condition may exclude a global branch through a proved forward map; passing it does not prove a global norm or rational point.

Required adapter: pin E,M,v,w,e,f, the normalized valuation and the receiver-to-norm map. Handle x=0 separately. For a global tensor-product norm, account for every place above v and the product of local norms; do not substitute a single factor test unless justified. Ramified places, split algebras and archimedean places are not automatically covered.

Distinctness: LIT-PW04/LIT-PW06 concern Brauer evaluation/place selection; this is an explicit norm-image equivalence, not a Brauer invariant calculation. Existing congruence/squareclass filters may already encode the same restriction: no double charge. No local-global norm theorem is claimed.

Source: [exact Lean statement](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Theorems/Thm_LanglandsTunnell_TateLocal_mem_range_unitsMap_norm_iff_inertiaDeg_dvd_of_ramificationIdx_eq_one.lean), Git blob `29b8f980585d118dd7b4aba6cb53546cd6f4f4b4` (1123 bytes); [proof implementation](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/P2M/Sol/S_LanglandsTunnell_TateLocal_mem_range_unitsMap_norm_iff_inertiaDeg_dvd_of_ramificationIdx_eq_one.lean), Git blob `7d983be19ae1e1f6779fbe434d117543d36212e7` (2975 bytes). The named theorem and all definition/typeclass hypotheses take precedence over this prose.

Activation gate: identify the exact receiver and source dependency closure; validate the adapter and theorem in the chosen toolchain; freeze and independently audit the resulting boundary under its Stage rules. No current authority or credit is changed by registration.

## FLT-PW04 — FINITE_S_SUPPORTED_POWERCLASS_UNIVERSE

Maturity: PROVISIONAL. Source-inspected contract, not locally kernel-verified.

Input: a Dedekind domain R, fraction field K, n>0, a finite set S of height-one primes, finite class group and finitely generated unit group. Output: the multiplicative n-Selmer group of K relative to R and S is finite: n-th-power classes whose valuations away from S vanish modulo n.

Cuboid application (conditional): after proving that an exact family of square/norm branches has valuations divisible by n outside one fixed finite S, its image lies in a finite powerclass universe. This supplies a finiteness premise before constructing an exhaustive covering collection. It is NOT itself an elliptic-curve n-Selmer computation.

Required adapter: derive the fixed S from the same receiver's denominators, discriminants and bad places, prove all outside-S conditions, and provide the unit/class-group inputs. If S or K changes with the parameter, a pointwise finite result does not establish a uniformly finite global universe. A concrete representative list and completeness proof remain separate work.

Distinctness: LIT-PW03 starts with finite branches and builds genuine n-covers; this card can justify a missing arithmetic finiteness premise. S34-W01 performs exact factor-squareclass descent; it does not alone establish this general Dedekind-domain finite universe. Finiteness is not an effective bound, executable enumeration, rational solvability or receiver closure.

Source: [exact Lean statement](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Theorems/Thm_IsDedekindDomain_selmerGroup_finite_of_finite_classGroup_of_fg_units.lean), Git blob `131553625b947d216a9b1c27fbdd2671ebb6f664` (718 bytes); [proof implementation](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/P2M/Sol/S_IsDedekindDomain_selmerGroup_finite_of_finite_classGroup_of_fg_units.lean), Git blob `72b9375416577dbb8fc8d48d883ac2f6a45a64ee` (14532 bytes). The named theorem and all definition/typeclass hypotheses take precedence over this prose.

Activation gate: identify the exact receiver and source dependency closure; validate the adapter and theorem in the chosen toolchain; freeze and independently audit the resulting boundary under its Stage rules. No current authority or credit is changed by registration.

## FLT-PW05 — SIMULTANEOUS_MOD3_MOD5_REDUCIBILITY_J_FILTER

Maturity: PROVISIONAL. Source-inspected contract, not locally kernel-verified.

Input: an integral Weierstrass model W with nonzero discriminant, and proofs that BOTH its mod-3 and mod-5 Galois representations are not irreducible (the precise upstream ModRepIsIrreducible predicate). Output: j=c4^3/Delta belongs to exactly the stated candidate set:
{-25/2, -349938025/8, -121945/32, 46969655/32768}.

Cuboid application (conditional): if an associated elliptic receiver forces both reducibilities, its j-map must land in this finite set. For a rational-function j(t), solve each equation with denominator and singular loci tracked. Conversely, j outside the set implies at least one of the two irreducibility predicates by contraposition, not which one.

Required adapter: exhibit W and prove both representation conditions on the same object, or deliberately use only the contrapositive. Visible rational 2-torsion does NOT imply mod-3 or mod-5 reducibility. The theorem name is not permission to replace these exact hypotheses by an unchecked claim about a 15-isogeny.

Distinctness: S36-PW05 treats split full-2 torsion/order-4 halves and 2-isogenies. This is a mod-3/mod-5 j-invariant restriction. Four possible j-values do not mean four curves or four points: twists and possibly positive-dimensional fibers remain. No general rational-isogeny or torsion classification is imported.

Source: [exact Lean statement](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Theorems/Thm_WeierstrassCurve_fifteenIsogenyClassification.lean), Git blob `34a6c0d3db44168d720f92d3f51ebdb79259de51` (2095 bytes); [proof implementation](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/P2M/Sol/S_WeierstrassCurve_fifteenIsogenyClassification.lean), Git blob `7a0bf854a2ca238d7ec1fd9184048af2bde00367` (2660 bytes). The named theorem and all definition/typeclass hypotheses take precedence over this prose.

Activation gate: identify the exact receiver and source dependency closure; validate the adapter and theorem in the chosen toolchain; freeze and independently audit the resulting boundary under its Stage rules. No current authority or credit is changed by registration.

## FLT-PW06 — PRIME_TO_RESIDUE_CHARACTERISTIC_TORSION_REDUCTION_INJECTION

Maturity: PROVISIONAL. Source-inspected contract, not locally kernel-verified.

Input: a valued field L with valuation subring A; a Weierstrass equation over A whose reduction has nonzero discriminant; an integer N whose residue-field image is nonzero; two generic-fiber points P,Q killed by N. Output: equal reductions imply P=Q. Thus reduction is injective on this N-torsion.

Cuboid application (conditional): certify prime-to-residue-characteristic torsion distinctions in an elliptic receiver and reject impossible torsion requirements. With a finite residue field and a proved rational embedding/reduction dictionary, an N-torsion subgroup embeds into the finite reduced group; finite group computations must still be exact and matched to this model.

Required adapter: certify good reduction, N invertible in the residue field, the chosen reduction homomorphism, and actual N-torsion rather than numerical torsion guesses. This injectivity statement does not require the algebraically closed residue-field and Henselian hypotheses used by the stronger bijectivity theorem also inspected.

Distinctness: S36-PW06 is specialization of generic rank/Kummer data in an elliptic family. This card is local reduction of torsion, not injectivity on the full Mordell-Weil group. No nontorsion rank bound, bad-reduction case, residue-characteristic-primary torsion claim or converse lift is granted.

Source: [exact Lean statement](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Theorems/Thm_WeierstrassCurve_eq_of_reduceHom_eq_of_nsmul_eq_zero.lean), Git blob `c3eab9ae8dcd31de8756bf3360b94a0336760a9c` (698 bytes); [proof implementation](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/P2M/Sol/S_WeierstrassCurve_eq_of_reduceHom_eq_of_nsmul_eq_zero.lean), Git blob `78c76d3eabe79e1b6f6d90caae5296142dd57ae1` (1092 bytes). The named theorem and all definition/typeclass hypotheses take precedence over this prose.

Activation gate: identify the exact receiver and source dependency closure; validate the adapter and theorem in the chosen toolchain; freeze and independently audit the resulting boundary under its Stage rules. No current authority or credit is changed by registration.

## FLT-PW07 — NODAL_VALUE_AND_LEADING_TERM_RR_DIMENSION_BOUND

Maturity: PROVISIONAL. Source-inspected contract, not locally kernel-verified.

Input: an algebraically closed field K and a function field F with the upstream IsCurveOver instance; divisors Kc,D1,D2 and genus parameter g with the Riemann-Roch identity for ALL divisors. Choose a nonempty finite set SS of ordered pairs of places, injective in the first coordinate, a distinguished pair s, order-one parameters x,y there, nonnegative integers m,k and u in K. Require D1(t.first)=0 and D2(t.second)=0 at the relevant places, deg D1 >= 2g+m+|SS| and deg D2 >= 2g+k+|SS|.

Let P be a K-linear subspace of pairs (h0,h1) from this SAME F. Require h0 in L(D1-m*s.first), h1 in L(D2-k*s.second), equal regular values at every other pair, and leading values at s satisfying lead(h0)=u*lead(h1). Output: P is finite-dimensional and
dim P <= (deg D1-m)+(deg D2-k)+2-2g-|SS|.

Cuboid application (conditional): model sheet/branch matching as an actual evaluation-and-leading-coefficient map, then bound the compatible section space. This is a possible source lemma for normalization/gluing investigations, not a supplied MB104 solution.

Required adapter: construct the function field/divisors/place pairs and prove all conditions plus the exact image of the receiver's section space. Matching places and regular values are load-bearing: the upstream evalAt defaults to zero outside its domain, so use the HasValue regularity premises and do not count poles as zero-valued matches. For different components/function fields, an additional generalization is necessary. Distinct first-coordinate places cannot be replaced by repeated copies of the same landing.

Distinctness: S32-PW09 couples discriminant/conductor degrees; this theorem bounds a specifically defined linear space. Its proof constructs the matching linear map and establishes the required rank, rather than assuming one independent saving per node. The displayed upper bound alone is not a finite degree cap or an R8 bound. A contradiction requires an independently proved incompatible dimension lower bound; no double counting of existing conditions.

Source: [exact Lean statement](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Theorems/Thm_AlgebraicCurve_RROpens_finrank_le_of_forall_mem_riemannRochSpace_sub_and_hasValue_nodes_and_hasValue_leading.lean), Git blob `2414782a8cc732a5c07edf011f95f1b6e528a4ad` (2122 bytes); [proof implementation](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/P2M/Sol/S_AlgebraicCurve_RROpens_finrank_le_of_forall_mem_riemannRochSpace_sub_and_hasValue_nodes_and_hasValue_leading.lean), Git blob `9bc8394a9c71e8f3be60bb2339f2f7db41ec1eac` (15000 bytes). The named theorem and all definition/typeclass hypotheses take precedence over this prose.

Activation gate: identify the exact receiver and source dependency closure; validate the adapter and theorem in the chosen toolchain; freeze and independently audit the resulting boundary under its Stage rules. No current authority or credit is changed by registration.

## FLT-PW08 — ALGEBRAICALLY_CLOSED_CONSTANT_FIELD_TORSION_DESCENT

Maturity: PROVISIONAL. Source-inspected contract, not locally kernel-verified.

Input: compatible field towers K -> F, K' -> F', K -> K', F -> F'; K and K' algebraically closed with K characteristic zero; F and F' one-variable finite-type function fields with the stated IsCurveOver instances, and F' generated over K' by the image of F. For n>0 let D' be a divisor with nD'=div(g') for a nonzero g'.

Output: a divisor D over K with nD principal, together with a nonzero correcting function h' over F', such that D' agrees with the extension of D up to div(h') at restricting places, and is principal at the remaining places. This concerns torsion divisor classes, not literal equality of chosen divisor representatives.

Cuboid application (conditional): compare geometric torsion-class data after extending algebraically closed constants, e.g. Qbar to C when the exact tower hypotheses are established. It can help separate constant-extension artifacts from genuine geometric torsion.

Required adapter: prove both function-field models, tower compatibilities/generation and the principal multiple; retain the correcting function and place restriction semantics. This DOES NOT descend from Qbar or C to Q: Q is not algebraically closed. Arithmetic descent, a Galois-invariant representative, effectiveness and rational point existence remain separate.

Distinctness: S30-W02 is quadratic semilinear finite-action descent; S33-PW09 binds marked Kummer lifts. This is geometric constant-field invariance of torsion divisor classes. Lower-priority infrastructure candidate, not a new endpoint obstruction.

Source: [exact Lean statement](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/Theorems/Thm_AlgebraicCurve_Divisor_exists_torsion_descent_of_constantFieldExtension.lean), Git blob `fe07c2915cd195cbc78754ce8d940e1c99f7881e` (8372 bytes); [proof implementation](https://github.com/anthropics/fermats-last-theorem/blob/aa2d8b34692b16c70f699536de0d8e75b9a3e9ef/P2M/Sol/S_AlgebraicCurve_Divisor_exists_torsion_descent_of_constantFieldExtension.lean), Git blob `c3c131594edd1110988b8710422cea98b46383e9` (46340 bytes). The named theorem and all definition/typeclass hypotheses take precedence over this prose.

Activation gate: identify the exact receiver and source dependency closure; validate the adapter and theorem in the chosen toolchain; freeze and independently audit the resulting boundary under its Stage rules. No current authority or credit is changed by registration.

## Screened but not separately registered

- KummerCover.finrank_eq: a prime-degree Kummer extension degree lemma under primitive-root/non-power hypotheses; useful supporting provenance, but no newly justified independent-squareclass tower or receiver adapter was supplied beyond existing descent routes.
- continuousH2Map_kummerRep_injective_and_range_iff_smul_eq_zero: includes a specific representation map to the absolute Galois group of Q and two finite-level compatibility hypotheses; no shortcut to the repository's Brauer/Kummer receiver or general field statement was established.
- finite-dimensional Selmer representation invariant formula: includes normality and a prime-to-p index condition; not an unconditional Selmer rank or global H1 bound. Kept as a possible refinement of FLT-PW04, not another overlapping card.
- bijective_reduceHom_restrict_torsion: stronger than the chosen injection but needs Henselian and algebraically closed residue-field hypotheses. FLT-PW06 uses the more directly applicable injection theorem; no duplicate bijection card.
- finite/etale Kummer normalization with special-fiber section: requires proper normal models, invertible exponent, local unit/trivialization and cocycle conditions, plus a special-fiber connectedness premise. A special-fiber section is not a rational lift. No additional card without a concrete model match.

## Practical ordering

When an actual norm or finite-powerclass receiver exists, FLT-PW03/PW04 are the first candidates to evaluate. FLT-PW06 is a local torsion-certification tool. FLT-PW07 is a targeted geometric-section-space candidate, with substantial model-matching work. FLT-PW05 only applies if the two reducibility premises or its contrapositive are genuinely needed. FLT-PW08 is geometric infrastructure and must never be mistaken for arithmetic descent to Q. This is advisory ordering, not a live P0/P1/P2 reassignment.
