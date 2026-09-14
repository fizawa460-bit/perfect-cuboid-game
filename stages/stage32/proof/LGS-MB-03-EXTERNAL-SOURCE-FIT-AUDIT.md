# Stage32 LGS-MB-03 — external theorem / source-fit audit

Status: `SOURCE_DISCOVERY_COMPLETE_NO_SOURCE_FIT_CLOSURE`

This is the bounded follow-up named by `LGS-MB-02-REPO-ARCHAEOLOGY.md`:

`LGS_MB_03_EXTERNAL_THEOREM_AND_SOURCE_DISCOVERY_FOR_JET_OR_DELTA_OFF_BOUND`.

It audits only the two nonduplicate directions retained there:

1. `POPULATION_WIDE_TANGENT_JET_OR_LANDING_CONSTRAINT`;
2. `POPULATION_WIDE_GLOBAL_SINGULARITY_OR_DELTA_OFF_BOUND`.

No AN--AU computation is rerun. No FULL178 enumeration, EX5/CUT replay, heavy compute, MAIN authority mutation, receiver exclusion, or merge credit is performed. MB104 conductor/monodromy work is outside this leaf and is not entered.

## Refetched PR boundary before source audit

PR `#1807` was refetched at exact head

`0a3490436f126af0e3815d4ad6d3361e849969ae`.

The pull-request-triggered runs attached to that exact head were:

- `Stage32 stale-run sweeper` run `34798337492`: `SUCCESS`;
- `Stage32 claim frontier integrity` run `34798337491`: `SUCCESS`.

The PR was Draft / Open / unmerged at that boundary.

## Receiver/source locks used without recomputation

The exact attacked population remains `R29-LG2-MB`. MB101/MB102 source-lock the multibranch semantics and the exact local/global delta ledger, but explicitly leave intrinsic branch delta ranges, pairwise local intersection ranges, and `Delta_off` uncontrolled.

The retained archaeology already rules out replaying scalar branch counts, factor-Hurwitz budgets without member-level landings, cusp multiplicity alone, conductor identities without an upper bound, residual involution action without member-level landings/jets, and weighted Bezout from retained cusp multiplicities.

### Retained geometric input

- post1648AS source-locks the local cusp inertia action on an exceptional coordinate as `lambda -> -lambda`, while explicitly recording that retained data do not force an opposite pair or determine first jets.
- post1648AT leaves the missing input as member-level landing/jet information or an independent global restriction on singularities of the intermediate/image curves.
- Arsenal `S34-W03` is only a receiver-restricted intersection-exclusion routing method. It requires an exact extra condition `K`; it does not supply the missing `K`, landing theorem, local-defect range, or `Delta_off` bound.

## Direction A — tangent-jet / landing constraint

### Candidate A1: Freitag--Salvati Manni, box-variety curve bound

Source:

E. Freitag and R. Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675--691, DOI `10.1307/mmj/1480734014`, arXiv `1303.6495`.

Their Theorem 3.1 assumes for an irreducible box-variety curve `C` that the normalization map `Cbar -> C` is bijective. In the proof, the upper bound on exceptional poles uses this hypothesis directly: bijectivity implies that `Cbar` meets each of the 48 exceptional curves at most once. The same proof uses the cusp/curve-lemma expansion to constrain the positive translation exponents, but it does not source-lock the member-level finite nonzero exceptional landing parameter or first jet needed by post1648AS.

### Population adapter check

`R29-LG2-MB` is the multibranch receiver: at least one attacked node has `r_i >= 2`. At such a point the normalization has at least two preimages, so the global bijectivity hypothesis required by Theorem 3.1 fails exactly on the population for which a landing-collision bound is needed.

The useful statement “at most one meeting per exceptional curve” therefore cannot be imported population-wide. Removing the bijectivity hypothesis or replacing it by an `r_i`-weighted pole/jet statement would be a new theorem/adapter, not source reuse. The cusp expansion alone likewise does not force a relation among the finite nonzero `lambda` values retained by AS.

Verdict:

`NEAR_FIT__LOAD_BEARING_BIJECTIVITY_HYPOTHESIS_FAILS`.

No population-wide tangent/landing constraint is source-fitted.

## Direction B — global singularity / Delta_off bound

### Candidate B1: Simon--Weimann discriminant identities on P1 x P1

Source:

D. Simon and M. Weimann, *Plane Curves With Minimal Discriminant*, Journal of Commutative Algebra 10 (2018), 559--598, arXiv `1507.01091`.

For a bihomogeneous form `F` with no factor in the base coordinate, Proposition 2.3 gives the exact fibrewise identity

`ord_alpha Delta_Y(F) = r_alpha + 2 delta_alpha`.

For an irreducible curve of fixed bidegree and geometric genus, Proposition 2.4 also gives a one-fibre upper bound on `ord_alpha Delta_Y(F)`, with equality characterized by all singularity defect being concentrated over that fibre and a unique place there.

### Object adapter check

post1648AP already supplies an integral factor-pair image `D` in `P1 x P1` and its birational normalization data, so the geometric object type is a genuine fit for these propositions.

The closure quantity is not. The propositions turn local delta/ramification data into discriminant valuations, but the retained LGS/MB surface does not source-lock a population-wide discriminant factorization, off-exception fibre valuation bound, or projection-contact restriction that is independent of the already retained genus/Hurwitz ledger. Consequently:

- Proposition 2.3 is an exact translator, not an independent upper bound for `Delta_off`;
- Proposition 2.4 bounds a single projection fibre, not the total off-exceptional defect required by MB102;
- summing the fibrewise identity without new valuation/contact input returns the same kind of global genus/ramification accounting already retained, rather than separating `Delta_exc` from `Delta_off`.

Using this source to obtain closure would therefore require one genuinely new input: a source-locked restriction on the discriminant valuations/contact pattern of the attacked population. That input is not present in the retained LGS/MB archaeology audited here.

Verdict:

`OBJECT_FIT__NO_INDEPENDENT_DELTA_OFF_BOUND`.

### Candidate B2: logarithmic Miyaoka/BMY-style singularity bounds

Standard logarithmic Miyaoka--Yau applications found in the literature impose positivity and/or smooth/semi-stable/simple-normal-crossing hypotheses after resolution. The directly available ruled-surface formulations do not give a population-complete bound on arbitrary intrinsic branch delta plus pairwise intersection contributions for the present `P1 x P1` image. Applying a plane-curve singularity inequality after a birational transformation would additionally require a new population-complete transformation/defect adapter.

Verdict:

`HYPOTHESIS_OR_MODEL_ADAPTER_GAP`.

No independent global singularity inequality is source-fitted from this family.

## Arsenal source-fit result

The retained archaeology names `S34-W03` as the relevant formal routing pattern. Its exact contract can consume a proved joint receiver condition, but it does not create the missing tangent/jet condition or `Delta_off` bound. A bounded Arsenal lookup under the repository asset-discovery policy produced no additional exact-fit retained weapon for either missing object. This is not a repository-wide mathematical absence claim.

## Deduplicated decision

Neither permitted direction currently supplies a theorem whose hypotheses, object, population semantics, and conclusion all fit `R29-LG2-MB` strongly enough to close the MB102 defect ledger.

- tangent/landing: `NO_SOURCE_FIT_CLOSURE` because the closest box-variety theorem uses normalization bijectivity, which the multibranch receiver violates;
- global singularity/`Delta_off`: `NO_SOURCE_FIT_CLOSURE`; the discriminant identity is object-compatible but requires new projection-specific valuation/contact information before it becomes an independent bound.

Therefore the blocker remains

`LGS_MB_MISSING_EXHAUSTIVE_LOCAL_DEFECT_RANGE_AND_DELTA_OFF_CONTROL`.

No finite-exception reduction, receiver exclusion, effectivity exclusion, MAIN credit, theorem credit, endpoint credit, or merge authorization follows.

## Bounded continuation hooks

If this LGS leaf is continued later without entering MB104, the only justified new inputs exposed by this audit are:

1. a genuine multibranch-compatible modular cusp theorem controlling finite nonzero exceptional landing parameters / first jets, not merely translation exponents; or
2. a population-wide projection/discriminant valuation or contact theorem that turns Simon--Weimann's fibrewise identity into an independent `Delta_off` restriction.

Absent one of those inputs, replaying AN--AU arithmetic or rephrasing MB102 through discriminants is an anti-loop violation.
