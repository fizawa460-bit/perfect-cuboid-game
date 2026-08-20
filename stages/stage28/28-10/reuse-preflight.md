# Stage28-10 repository-wide reuse preflight

```text
DISCOVERY_CHECKPOINT=Stage28-10
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS_FOR_CONTRACT_INPUTS
STRONGER_PRIOR_RESULT_FOUND=true
NEW_RESEARCH_JUSTIFIED=NOT_REQUIRED_AT_CHECKPOINT10
```

## Purpose

Checkpoint10 is a comparison-contract checkpoint, not a new theorem or exponent attack. The reuse search therefore targets the exact Stage19/Stage20 population definitions, their strongest currently certified incoming theorem surfaces, and an already-audited common-host adapter.

## Searched paths and signatures

```text
SEARCHED_PATHS=
  docs/stage16-29-population-roadmap.md;
  docs/research-arsenal-index.md;
  stages/stage19/final.md;
  stages/stage20/final.md;
  stages/stage26/26-70/self-contained-bundle.md;
  stages/stage27/final.md;
  docs/stage27-arsenal-promotion.md;
  repository code search for Stage19/Stage20 bridge and N2/M3 comparisons

SEARCH_TERMS=Stage19 Stage20 bridge comparison; N2 M3 M2 ratio; integral space diagonal; exactly two faces; exactly three faces
STRUCTURAL_SIGNATURES=EXACTLY_TWO_FACES+INTEGRAL_SPACE_DIAGONAL; THREE_FACES_EULER; COMMON_EUCLIDEAN_CUTOFF; AT_LEAST_TWO_FACE_HOST
DEPENDENCY_NEIGHBORS=Stage18,Stage19,Stage20,Stage24,Stage26,Stage27
```

## Accepted candidates

### A. Canonical roadmap contract

`docs/stage16-29-population-roadmap.md` is authoritative:

- Stage28 compares Stage19 to Stage20;
- the comparison is not a literal subset transition;
- checkpoint10 must freeze exact comparison semantics and any host/intersection adapter before causal interpretation.

```text
CANDIDATE=ROADMAP_STAGE28_CONTRACT
ACCEPTED=true
POPULATION_MATCH=EXACT
CUTOFF_MATCH=EXACT
MULTIPLICITY_MATCH=EXACT
MEASURE_MATCH=EXACT
QUANTIFIER_MATCH=EXACT
```

### B. Stage19 source population

The Stage19 frozen interface defines

\[
N_2(B)=\#\{0<a<b<c,\gcd(a,b,c)=1,R\le B,\text{ exactly two integral face diagonals},R\in\mathbf Z\}.
\]

Later audited/promoted work strengthens the historical Stage19 lower-side metadata. The strongest currently certified source corridor consumed by Stage28 is

\[
B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

```text
CANDIDATE=Stage19+S25-W01+AR-006+Stage27
ACCEPTED=true
POPULATION_MATCH=EXACT
CUTOFF_MATCH=EXACT
MULTIPLICITY_MATCH=EXACT
MEASURE_MATCH=EXACT
QUANTIFIER_MATCH=EXACT
```

### C. Stage20 target population

Stage20 defines the primitive/canonical Euler population

\[
M_3(B)=\#\{0<a<b<c,\gcd(a,b,c)=1,R\le B,\text{ all three face diagonals integral}\},
\]

with no requirement that `R` be integral.

The Stage20 final bundle contains the historical `B^(1/6)` lower, but the project-wide arsenal explicitly supersedes that selector by Stage26 `S26-W01`. Stage28 therefore consumes the strongest current target envelope

\[
B^{1/3-\varepsilon}\ll_\varepsilon M_3(B)
\ll_\eta B(\log B)^{5-\eta},\qquad 0<\eta<1/46.
\]

```text
CANDIDATE=Stage20+S26-W01+S26-W03
ACCEPTED=true
POPULATION_MATCH=EXACT
CUTOFF_MATCH=EXACT
MULTIPLICITY_MATCH=EXACT
MEASURE_MATCH=EXACT
QUANTIFIER_MATCH=EXACT_WITH_FIXED_EPSILON_ETA
STRONGER_PRIOR_RESULT_FOUND=true
SUPERSEDED_SELECTOR=Stage20_B^(1/6)_LOWER
CURRENT_SELECTOR=S26-W01_B^(1/3-epsilon)_LOWER
```

### D. Common-host adapter

Stage26 already certifies the literal no-space at-least-two-face physical host

\[
H_{\ge2}(B)=M_2(B)+M_3(B),
\]

where `M2` is exactly-two-face and `M3` is exactly-three-face. These strata are disjoint and use the same primitive/canonical Euclidean cutoff.

Because Stage19 satisfies `N2 subset M2`, Stage28 can place both endpoint populations inside the same audited host:

\[
N_2\subset M_2\subset H_{\ge2},\qquad M_3\subset H_{\ge2}.
\]

This yields legal common-host shares

\[
\Sigma_{19}(B)=\frac{N_2(B)}{H_{\ge2}(B)},\qquad
\Phi_{20}(B)=\frac{M_3(B)}{H_{\ge2}(B)}.
\]

For sufficiently large `B`,

\[
\frac{\Phi_{20}(B)}{\Sigma_{19}(B)}=\frac{M_3(B)}{N_2(B)}.
\]

```text
CANDIDATE=S26-W02 / Stage26 H_ge2 adapter
ACCEPTED=true
POPULATION_MATCH=ADAPTER_PROVED
CUTOFF_MATCH=EXACT
MULTIPLICITY_MATCH=EXACT_PHYSICAL_OBJECTS
MEASURE_MATCH=EXACT
QUANTIFIER_MATCH=EXACT
POPULATION_ADAPTER=Stage19 N2 subset of Stage18 M2 inside Stage26 H_ge2=M2+M3
```

## Rejected / non-direct candidates

1. Treating Stage19 as a subset of Stage20: rejected because Stage19 has exactly two integral faces while Stage20 has exactly three. Their intersection as stage populations is empty by face multiplicity.
2. Treating Stage20 as a subset of Stage19: rejected for the same reason, and Stage20 does not require an integral space diagonal.
3. Using `M3/N2` as a survival probability: rejected. It is a matched population-size ratio, equivalently a ratio of two shares of the same `H_ge2` host.
4. Using the Stage20 historical `B^(1/6)` lower as current strongest input: rejected as superseded by `S26-W01`.
5. Treating the Stage27 finite/effective exponent near `0.42` as the Stage19 asymptotic exponent: rejected; it is computed diagnostic evidence only.
6. Using `S27-W01/W02/W03` as authoritative project-wide selectors: not required for checkpoint10; their file still carries pending-audit promotion metadata, so Stage28 relies on already-audited underlying Stage21/25/26 interfaces for any load-bearing claim.
7. Inferring perfect-cuboid existence/nonexistence from the Stage28 bridge: rejected. Stage20 permits either integral or nonintegral space diagonal, while Stage19 excludes three-face objects by definition.

```text
CANDIDATES_ACCEPTED=ROADMAP_STAGE28_CONTRACT;Stage19+S25-W01+AR-006;Stage20+S26-W01+S26-W03;S26-W02_H_GE2_ADAPTER
CANDIDATES_REJECTED_WITH_REASON=literal_subset_semantics;survival_probability_semantics;superseded_Stage20_lower;finite_N2_point_exponent;pending_Stage27_promotion_as_load_bearing_selector;perfect_cuboid_endpoint_inference
DISCOVERY_LEDGER_STATUS=COMPLETE_FOR_CHECKPOINT10
```
