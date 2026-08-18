# StructureRadar literature ledger — SR-SEARCH-01

SEARCH_ID=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-01-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-001,SR-STR-002,SR-STR-003,SR-STR-004,SR-STR-005,SR-STR-006
EVIDENCE_POLICY=primary sources only for external theorem claims
NOVELTY_BY_SEARCH_ABSENCE=false

This ledger checks the first six normalized structures against the existing repository
arsenal/q-literature record and a fresh primary-source literature search. `ACTIVE` below
means that the existing audited repo weapon remains reusable for an exact matching receiver;
it does **not** mean that an external paper independently proves every repo-local adapter,
height normalization, mask, or leading constant.

## SR-STR-001 — Primitive canonical cuboid population convention

- Repo object: positive edges projected to `0<a<b<c`, `gcd(a,b,c)=1`, under an explicitly declared height and face-mask convention.
- Existing exact weapon: `AR-001`, already `ACTIVE` in `docs/stage14-arsenal.md`.
- Primary-source check: Stoll--Testa, *The surface parametrizing cuboids*, arXiv:1009.0388 (v2, 2025), treats the projective rational-cuboid surface and hence the natural scaling equivalence of rational boxes.
- Exact theorem/result used: the perfect/rational cuboid problem is represented by rational points on a projective cuboid surface; their paper determines the Picard group of the desingularization and studies a K3 quotient. It does not prescribe the repo's ordered primitive integer representative or its exact face-mask bookkeeping.
- Variable dictionary: projective rational box coordinates -> scale orbit of integer edge/diagonal tuples; repo additionally chooses the unique positive primitive ordered edge triple once an integer representative exists.
- Quantitative loss: none; this is an exact normalization contract, not a density theorem.
- Transfer verdict: `ADJACENT_CONTEXT + REPO_EXACT_NORMAL_FORM`; no external theorem is needed to strengthen AR-001.
- Smallest transfer test: verify that scaling/permutation preserves the stated face and space square predicates, then prove the projection fiber/orientation factor used by the receiver.
- Stable source: https://arxiv.org/abs/1009.0388
- Arsenal decision: `ACTIVE` (existing AR-001; no new promotion).

## SR-STR-002 — Saunderson parametrization of primitive Euler bricks

- Repo object: for a primitive Pythagorean triple `(u,v,w)`,
  `A=u|4v^2-w^2|`, `B1=v|4u^2-w^2|`, `C=4uvw`; the generalized repo construction yields `M3(B) >>_epsilon B^(1/3-epsilon)`.
- Existing exact weapons: `S20-W02` and stronger `S26-W01`.
- Primary-source check 1: Djamel Himane, *Primitive Euler brick generator*, arXiv:2405.13061 (2024), records exactly the Saunderson edge formulas and face diagonals `w^3`, `u(4v^2+w^2)`, `v(4u^2+w^2)`.
- Primary-source check 2: René Peschmann, *A torsion-intersection proof of perfect-cuboid nonexistence on 1,072 explicit master-tuple fibers*, arXiv:2604.28072 (2026), gives a structural classification of primitive Euler bricks in its master-tuple framework and proves nonexistence only on 1,072 explicit fibers; it is not a global Euclidean-height count.
- Primary-source check 3: Peschmann, *Exponent-one blockers and a Mordell-Weil construction of Euler bricks*, arXiv:2605.00573 (2026), gives a large rigorous generator on elliptic fibers but its exponent-one blocker is empirical on fully factored records and it does not supply the repo's global height exponent.
- Variable dictionary: Himane `(a,b,c)` = repo Saunderson edge triple up to canonical sorting/scaling; repo `B` is real Euclidean cuboid height, not a parameter-box cutoff.
- Quantitative comparison: no searched primary source states the repo's `B^(1/3-epsilon)` generalized lower under the same primitive/canonical Euclidean height. Himane certifies the algebraic construction but not that counting exponent.
- Transfer verdict: `FORMULA_COLLISION + NO_STRONGER_HEIGHT_COUNT_FOUND`.
- Smallest transfer test: substitute a primitive Euclid triple, verify the three face-diagonal identities, primitive/canonical projection, then compare `R` with the parameter height and bound output multiplicity.
- Stable sources: https://arxiv.org/abs/2405.13061 ; https://arxiv.org/abs/2604.28072 ; https://arxiv.org/abs/2605.00573
- Arsenal decision: `ACTIVE` (existing S26-W01/S20-W02; no new promotion).

## SR-STR-003 — Degree-two K3 cover of the two-face toric Euler-brick host

- Repo object: on `u^2=e^2+x^2`, `v^2=e^2+y^2`, adjoin `z^2=x^2+y^2`; after normalization/minimal resolution the third-face cover is K3.
- Existing exact weapon: `S20-W01` / `S26-W03`, with the explicit firewall that its saving is not multiplied with the independent local-blocker route.
- Primary-source check 1: David McKinnon, *Counting Rational Points on K3 Surfaces*, arXiv:math/9903013; J. Number Theory 84 (2000), 49--62, computes counts for Kummer surfaces associated to products of elliptic curves and exhibits accumulating curves.
- Primary-source check 2: Stoll--Testa, arXiv:1009.0388, studies the full cuboid surface and a K3 quotient, but this is not automatically the same physical Euler-brick K3 cover or the same height.
- Primary-source check 3: Zhizhong Huang, *Equidistribution of rational points and the geometric sieve for toric varieties*, arXiv:2111.01509, proves effective Manin--Peyre equidistribution and geometric-sieve estimates for smooth projective split toric varieties. In the repo this is used on the toric host/fibration image through an audited adapter, not as a generic K3 point-count theorem.
- Variable dictionary: repo two-face host -> split toric base; third-face square -> degree-two cover/image condition. McKinnon's `V` requires a verified product-Kummer model and its own ample height; that hypothesis has not been identified for this physical count.
- Quantitative comparison: generic K3 counting results found here do not give the repo's same-height Euler-brick envelope directly. The quantitative upper remains the audited S20-W01 adapter, not a free Picard-rank/K3 transfer.
- Transfer verdict: `REUSABLE_CONTEXT + EXACT_HEIGHT/VARIETY_FIREWALL`; no stronger direct collision.
- Smallest transfer test: prove an explicit birational/model identification, compare the physical Euclidean height with the theorem height uniformly, remove accumulating curves/exceptional divisors, and preserve primitive/canonical masks before importing any K3 exponent.
- Stable sources: https://arxiv.org/abs/math/9903013 ; https://arxiv.org/abs/1009.0388 ; https://arxiv.org/abs/2111.01509
- Arsenal decision: `ACTIVE` only through the already-audited S20-W01/S26-W03 interface.

## SR-STR-004 — Space-diagonal one-face transition asymptotic

- Repo theorem: for matched primitive canonical `R<=B` populations,
  `N1(B)/M1(B) ~ (kappa*pi/18)(log B)^2/B`.
- Existing exact weapon: `S21-W02` (`ACTIVE`).
- Primary-source check 1: Takumi Yoshida, *The relationship between face cuboids and elliptic curves*, arXiv:2407.09825 (2024), gives a 32:1 surjection from suitable non-torsion points on `E_{1,s}` to equivalence classes of rational face cuboids (two face diagonals plus the space diagonal) and proves infinitely many such classes.
- Primary-source check 2: Stoll--Testa, arXiv:1009.0388, gives the algebraic surface for the full rational cuboid problem, not this matched one-face transition count.
- Variable dictionary: Yoshida's face-cuboid target is an at-least-two-face-plus-space rational population modulo equivalence; repo `N1/M1` compares exactly-one-face integer primitive canonical populations under Euclidean height. These populations and measures are not interchangeable.
- Quantitative comparison: neither source states a bounded-height asymptotic for the matched `N1/M1` ratio or the constant `kappa*pi/18`.
- Transfer verdict: `ADJACENT_ELLIPTIC_STRUCTURE + NO_DIRECT_TRANSITION_COLLISION`.
- Smallest transfer test: rebuild the map on the exact `M1/N1` face mask, prove finite fiber multiplicity under the repo canonicalization, and compare the elliptic/projective height to `R` before using it quantitatively.
- Stable sources: https://arxiv.org/abs/2407.09825 ; https://arxiv.org/abs/1009.0388
- Arsenal decision: `ACTIVE` (existing S21-W02; no new promotion).

## SR-STR-005 — No-space one-face to two-face transition asymptotic

- Repo theorem: for matched primitive canonical `R<=B` populations,
  `M2(B)/M1(B) ~ (4*pi^2*C_M2/3)(log B)^4/B`.
- Existing exact weapons: `S22-W01` and geometric ledger `S25-W06` (`ACTIVE`).
- Primary-source check 1: Victor Batyrev and Yuri Tschinkel, *Manin's conjecture for toric varieties*, arXiv:alg-geom/9510014; J. Algebraic Geom. 7 (1998), 15--53, proves Manin's anticanonical asymptotic for smooth projective toric varieties over number fields.
- Primary-source check 2: Huang, arXiv:2111.01509, strengthens the split-toric input with effective asymptotics in adelic neighbourhoods and a geometric sieve.
- Variable dictionary: repo two-face host -> a specific split toric compactification after the repo-local gluing/height identification; `R<=B` -> an anticanonical height only after bounded metric comparison; primitive/canonical/exactly-two masks -> local/chamber conditions plus repo projection bookkeeping.
- Quantitative comparison: the general toric papers provide the theorem species and analytic counting engine, but do not state the cuboid-language ratio or its exact leading constant. Those require the repo-specific model, chamber, metric and multiplicity calculation.
- Transfer verdict: `THEOREM_LEVEL_INPUT + REPO_SPECIFIC_ADAPTER`; this is a genuine literature collision at the general Manin mechanism level, not at the final cuboid formula level.
- Smallest transfer test: verify smooth split toric model, anticanonical height equivalence, positive adelic chamber/mask, Picard rank, and primitive/canonical multiplicity; then recompute the Peyre/local constant in repo normalization.
- Stable sources: https://arxiv.org/abs/alg-geom/9510014 ; https://arxiv.org/abs/2111.01509
- Arsenal decision: `ACTIVE` (existing S22-W01/S25-W06; no new promotion).

## SR-STR-006 — Space-diagonal two-face versus one-face zero-density transition

- Repo theorem: for matched primitive canonical space-diagonal populations under `R<=B`, `N2(B)/N1(B) -> 0`.
- Existing exact weapon: `S23-W01` (`ACTIVE`).
- Primary-source check 1: Yoshida, arXiv:2407.09825, proves infinitude and an elliptic-curve parametrization for rational face cuboids with two face diagonals plus the space diagonal; it does not compare this population with an exactly-one-face host by bounded height.
- Primary-source check 2: Peschmann, *Quartic reductions and elliptic obstructions for perfect Euler bricks*, arXiv:2604.09328 (2026), gives unconditional reductions/obstructions for adding the remaining face conditions toward a perfect cuboid but explicitly leaves global nonexistence open.
- Primary-source check 3: Peschmann arXiv:2604.28072 proves nonexistence only on 1,072 explicit master-tuple fibers. These are fiberwise obstruction results, not a whole-population `N2/N1` density theorem.
- Variable dictionary: Yoshida face cuboids correspond to a rational at-least-two-face+space population; Peschmann begins from Euler-brick/master-tuple structures when testing the remaining space/face obstruction; repo `N2/N1` is an exactly-two versus exactly-one matched integer primitive canonical ratio with space already charged in both.
- Quantitative comparison: no searched primary source states `N2(B)/N1(B)->0` under the repo's exact masks and Euclidean height.
- Transfer verdict: `ADJACENT_STRUCTURAL_RESULTS + NO_DIRECT_ZERO_DENSITY_COLLISION`.
- Smallest transfer test: construct a measure-preserving finite-to-one adapter into the exact `N2` population and a matched `N1` denominator under `R<=B`; fiberwise nonexistence or infinitude alone is insufficient.
- Stable sources: https://arxiv.org/abs/2407.09825 ; https://arxiv.org/abs/2604.09328 ; https://arxiv.org/abs/2604.28072
- Arsenal decision: `ACTIVE` (existing S23-W01; no new promotion).

## Batch decision

SEARCHES_COMPLETED=6
ARSENAL_DECISIONS=6
NEW_EXTERNAL_ACTIVE_WEAPONS=0
EXISTING_ACTIVE_WEAPONS_CONFIRMED=6
DIRECT_STRONGER_COLLISIONS=0
NOVELTY_BY_SEARCH_ABSENCE=false
PERFECT_CUBOID_EXISTENCE_PROMOTED=false
PERFECT_CUBOID_NONEXISTENCE_PROMOTED=false

The fresh search therefore closes `SR-SEARCH-01` without adding a new external
weapon. It does, however, sharpen the firewalls: generic K3 counts, elliptic
face-cuboid infinitude, finite-fiber obstruction results, and toric Manin theorems
must only enter through an exact population/height/multiplicity adapter.
