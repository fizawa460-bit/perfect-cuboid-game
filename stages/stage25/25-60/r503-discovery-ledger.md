# Stage25-60 R503 discovery ledger

```text
DISCOVERY_CHECKPOINT=Stage25-60-R503
ROUTE=R503
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS,PRIMARY_LITERATURE
SEARCHED_PATHS=stages/stage25/25-50/**;stages/stage25/25-60/**;stages/stage24/24-40/**;stages/stage24/24-50/**;docs/stage14-15-bound-attack-map.md;docs/stage14-15-bound-deep-review-queue.md;Yoshida arXiv:2407.09825;Naskrecki arXiv:1210.6933;Silverman arXiv:2402.14771;Wong arXiv:1409.3255
SEARCH_TERMS=Yoshida face cuboid elliptic curve;Pythagorean Frey plus family generic rank;geometric Mordell-Weil rank zero;positive-rank specialization;canonical height;small rational points;specialization map;varying-fiber uniform height;multisection;base change
STRUCTURAL_SIGNATURES=E_1s:y^2=x(x-4s^2)(x+(s^2-1)^2);a=2s;b=s^2-1;c=s^2+1;a^2+b^2=c^2;generic geometric rank0;Yoshida 32:1;fixed s=5/3 non-torsion orbit;Mobius alpha-to-t;Mobius alpha-to-sprime
DEPENDENCY_NEIGHBORS=Stage19;Stage24-40 moving-family gate;Stage24-50 C17;Stage25-R501;Stage25-R502;Stage14/15 Q03,Q05
CANDIDATES_FOUND=generic non-torsion section on original Yoshida surface;Yoshida fixed-fiber orbit;Yoshida transformed positive-rank s sequence;low-degree base-change multisection;quantitative exceptional-fiber theorem;uniform small-point theorem
CANDIDATES_ACCEPTED=generic-rank-zero obstruction;fixed-fiber height-sparsity certificate;positive-rank-s-sequence height-sparsity certificate;32:1 finite-multiplicity reuse;precise base-change/external theorem gate
CANDIDATES_REJECTED_WITH_REASON=direct generic-section route rejected because geometric generic rank is zero;Yoshida fixed-fiber orbit rejected as exponent-upgrade route because only O(sqrt(log B)) indices can occur below physical height B;positive-rank infinitude alone rejected because displayed parameter sequence is height-sparse and gives no polynomial varying-fiber count;Silverman function-field Lehmer lower bound rejected as population lower input because it does not count rational positive-rank specializations;Wong specialization result rejected because it does not provide the required one-parameter polynomial small-point population
POPULATION_ADAPTERS_PROVED=Yoshida 32:1 handles elliptic-data-to-face-cuboid similarity multiplicity;Stage19 exactly-two/primitive/canonical adapter remains required for any future new varying-fiber lower;current negative certificates do not use finite census as proof
DISCOVERY_LEDGER_STATUS=COMPLETE_R503_GATE_REFINEMENT
```

## Exact family identification

Yoshida's family is

\[
E_{1,s}:y^2=x(x-(2s)^2)(x+(s^2-1)^2).
\]

With `(a,b,c)=(2s,s^2-1,s^2+1)`, the Pythagorean identity is exact. Therefore Naskręcki's geometric generic-rank-zero statement for the plus-sign Pythagorean/Frey family applies directly to the original Yoshida surface.

```text
R503_FAMILY_IDENTIFICATION_ADAPTER=EXACT
R503_GENERIC_GEOMETRIC_MW_RANK=0
R503_GENERIC_NONTORSION_SECTION=false
```

## Fixed-fiber Yoshida orbit

At `s=5/3`, Yoshida uses a fixed infinite-order point and its multiples. The source map to the cuboid parameter is Möbius in the `x`-coordinate:

\[
t=15(9\alpha-32)/(81\alpha+800).
\]

The inverse is also Möbius. On a fixed elliptic curve,

\[
h(x([n]P))=2n^2\hat h(P)+O(1),
\]

so `h(t_n)=Theta(n^2)`.

The primitive cuboid contains the edge ratio

\[
2t/(t^2-1),
\]

a degree-two rational map. Height at most `B` for the primitive cuboid therefore forces `n=O(sqrt(log B))`.

```text
R503_FIXED_FIBER_ORBIT_COUNT_UPPER=O(sqrt(log B))
R503_FIXED_FIBER_ORBIT_POWER_UPGRADE=false
```

## Positive-rank parameter sequence

Yoshida's displayed transformation gives, at `s=5/3`,

\[
s'=4(27\alpha+40)/(27\alpha-640).
\]

Again this is Möbius with rational inverse, hence the displayed positive-rank parameters have `h(s'_n)=Theta(n^2)` and only `O(sqrt(log X))` terms of rational height at most `X`.

This is a statement about Yoshida's explicit sequence only. It does not claim that all positive-rank specializations are sparse.

## Stage14/15 reopen discipline

```text
S1415_ATTACKS_REVIEWED=Q03,Q05
S1415_Q03_RELEVANCE=MOVING_ELLIPTIC_SELMER_HEIGHT_UNIFORMITY
S1415_Q05_RELEVANCE=MOVING_GENUS_ONE_GLOBAL_AGGREGATION
NEW_INPUT_RELATIVE_TO_Q03_Q05=GENERIC_GEOMETRIC_RANK_ZERO_IDENTIFICATION_PLUS_YOSHIDA_HEIGHT_SPARSE_SEQUENCE
EXHAUSTED_ROUTE_REOPENED=false
```

The new input sharpens the receiver: the original Yoshida surface has no non-torsion generic section, so a successful continuation must use a genuine base change/multisection or a quantitative theorem on exceptional positive-rank fibers with small points.

## Bounded primary-literature recheck

The primary-literature pass searched the exact Yoshida family, Pythagorean/Frey rank results, canonical-height inputs and specialization-height results. It also checked for later exact face-cuboid followups in arXiv search.

No directly applicable primary result was identified that proves a polynomial lower count of rational `s` carrying suitably small non-torsion points in this exact family. This is recorded only as a bounded-search outcome.

```text
NO_EXHAUSTIVE_NO_KNOWN_THEOREM_CLAIM=true
R503_EXTERNAL_THEOREM_GATE_PRECISE=true
R503_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE
R503_DIRECT_GENERIC_SECTION_ROUTE=CLOSED
R503_BASE_CHANGE_MULTISECTION_ROUTE=OPEN_GATE
R503_QUANTITATIVE_EXCEPTIONAL_FIBER_ROUTE=OPEN_GATE
R503_UNIFORM_SMALL_POINT_ROUTE=OPEN_GATE
GLOBAL_LOWER_EXPONENT_ABOVE_QUARTER_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_REASON=R503 route is reclassified using an external geometric generic-rank-zero theorem and a new quantitative height-sparsity certificate
```
