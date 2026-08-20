# Stage28-20/30 repository-wide reuse preflight

```text
DISCOVERY_CHECKPOINT=Stage28-20,Stage28-30
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS,STAGE14_15_BOUND_ATTACK_MAP
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS_FOR_CURRENT_FINITE_PANEL_AND_DERIVED_CORRIDOR
STRONGER_PRIOR_RESULT_FOUND=true
NEW_RESEARCH_JUSTIFIED=NOT_REQUIRED_AT_CHECKPOINT20_OR_30
```

## Search evidence

```text
SEARCHED_PATHS=
  docs/stage16-29-population-roadmap.md;
  docs/stage14-num-reuse-index.md;
  docs/research-arsenal-index.md;
  docs/stage14-15-bound-attack-map.md;
  docs/stage14-15-bound-deep-review-queue.md;
  stages/stage20/final.md;
  stages/stage26/26-70/self-contained-bundle.md;
  stages/stage27/27-20/result.md;
  stages/stage27/final.md;
  stages/stage28/28-10/result.md
SEARCH_TERMS=N2 M3 common cutoff; Stage19 Stage20 bridge ratio; exactly-two space; Euler cuboid; M3/N2; H_ge2 host share
STRUCTURAL_SIGNATURES=INTEGRAL_SPACE_DIAGONAL; EXACTLY_TWO_FACES; THREE_FACES_EULER; COMMON_EUCLIDEAN_CUTOFF; OVERLAP_INTERSECTION; AT_LEAST_TWO_FACE_HOST
DEPENDENCY_NEIGHBORS=Stage19,Stage20,Stage24,Stage26,Stage27
DISCOVERY_LEDGER_STATUS=COMPLETE
```

## Numerical reuse

The exact common-cutoff finite baseline is already present in audited sources. No new enumerator run is needed.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R05;Stage27-20;Stage20-final
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=DERIVED_EXACT_FINITE
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

Accepted finite interfaces:

- `Stage27-20` for exact `N2` values at `B=10k,50k,200k,1m`;
- `Stage20 final` / compatible Stage14-e exact census for exact `M3` values at the same cutoffs;
- only matched common cutoffs are used in the bridge panel.

Rejected numerical shortcuts:

- `N2(500m)=3495` is not paired with an exact reused `M3(500m)` count here, so it is not used for a Stage28 ratio point;
- finite `T=0` in the integral-space census is not a perfect-cuboid nonexistence theorem;
- finite effective exponents are not asymptotic exponents.

## Theorem reuse for checkpoint30

Accepted current theorem interfaces:

```text
N2_LOWER=S25-W01 / Stage27: N2(B)>>B^(1/4)
N2_UPPER=AR-006 / Stage27: N2(B)<<_epsilon B^(1/2+epsilon)
M3_LOWER=S26-W01: M3(B)>>_epsilon B^(1/3-epsilon)
M3_UPPER=S26-W03: M3(B)<<_eta B(log B)^(5-eta), 0<eta<1/46
HOST_SHARE=S26-W02 / Stage26: Phi20=o((log B)^(-delta)), 0<delta<1/46
N2_HOST_SHARE=Stage27+Stage18: B^(-3/4)(log B)^(-5)<<Sigma19<<_epsilon B^(-1/2+epsilon)(log B)^(-5)
```

The Stage20 historical one-parameter `B^(1/6)` lower is rejected as superseded by `S26-W01`.

## Stage14/15 bound-attack rematch

The Stage14/15 discovery map and curated queue were checked before claiming the current derived corridor. No older attack is promoted as a stronger direct Stage28 bridge theorem.

Representative rejected/non-direct attack clusters:

```text
CANDIDATES_REJECTED_WITH_REASON=
  S1415-ATTACK-0215,0216,0710: ambient/toric components; population mismatch for direct N2-vs-M3 bridge theorem;
  S1415-ATTACK-0724,0728,0729,0731: moving genus-one support receiver; external future theorem species, no completed bridge bound;
  S1415-ATTACK-0748: exact Kummer support receiver, but no completed support-size theorem stronger than the current N2 upper;
  S1415-ATTACK-0791,0793,0794,0796,0800: survivor reconstruction cluster exhausted internally absent materially new input;
  S1415-ATTACK-0771,0772: pointwise gcd-product route negatively certified;
  S1415-ATTACK-0804,0807,0809,0811: reconstructed-graph dispersion lacks same-measure cancellation adapter;
  S1415-ATTACK-0812,0814,0816,0817: Pell/ideal/residual-switch cluster exhausted absent new average theorem;
  S1415-ATTACK-0818,0819,0820: fixed-prime local overlap gives qualitative obstruction, not a stronger fixed-power bridge theorem
CANDIDATES_ACCEPTED=NONE_AS_NEW_DIRECT_BRIDGE_THEOREM
POPULATION_ADAPTERS_PROVED=Stage28 checkpoint10 H_ge2 common-host adapter
```

These rejections do not assert that no new theorem exists. They only show that the already-indexed Stage14/15 routes do not improve the checkpoint30 bridge corridor without new input.

## Result

The strongest legal checkpoint30 bridge corridor derivable from current audited project inputs is

\[
\mathcal R_{28}(B)=M_3(B)/N_2(B)\gg_\zeta B^{-1/6-\zeta}
\]

for every fixed `zeta>0`, and

\[
\mathcal R_{28}(B)=o(B^{3/4}(\log B)^{5-\delta})
\]

for every fixed `0<delta<1/46`.

No direct prior bridge theorem found in the checked repository surfaces resolves the asymptotic ordering.
