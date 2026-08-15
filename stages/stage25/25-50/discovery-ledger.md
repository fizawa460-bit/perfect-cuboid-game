# Stage25-50 discovery ledger

```text
DISCOVERY_CHECKPOINT=Stage25-50
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS,PRIMARY_LITERATURE
SEARCHED_PATHS=stages/stage25/25-controller.json;stages/stage24/24-50/result.md;stages/stage24/24-50/fresh-lower-surgeon.md;stages/stage24/24-50/u19-r501a-quartic-family.md;stages/stage24/24-50/literature-recheck.md;stages/stage23/post-stage24-r01/**;stages/stage21/**;stages/stage22/**;Stage14 NUM reuse index and NUM-R01/R02/R03;Meskhishvili arXiv:1502.02375;Yoshida arXiv:2407.09825
SEARCH_TERMS=positive-power lower;nearly-perfect cuboid;face cuboid;one-parameter rational parametrization;C17;quartic family;common squarefree core;shared-edge plus space;primitive canonical adapter;height growth;third-face square;hyperelliptic exception;bounded similarity multiplicity
STRUCTURAL_SIGNATURES=N2>>sqrt(logB);one-parameter rational NPC;homogeneous degree8 family;two rational parameter heights;degree16 third-face square curve;M1~B^2logB;M2~Blog^5;N1~Blog^3
DEPENDENCY_NEIGHBORS=Stage14 NUM;Stage15-2 explicit families;Stage16 source;Stage16S ambient baseline;Stage17/N1;Stage18/M2;Stage19/N2;Stage21;Stage22;Stage23 post-Stage24;Stage24 checkpoints50/60/70
CANDIDATES_FOUND=L50-A C17 audited logarithmic lower;L50-B Meskhishvili first one-parameter rational NPC family;L50-C Meskhishvili third one-parameter family;L50-D Meskhishvili second family;L50-E Yoshida elliptic face-cuboid surface;L50-F Stage24 symmetric multiplier k-family;L50-G common squarefree-core slices;L50-H common-leg divisor plus space receiver
CANDIDATES_ACCEPTED=L50-A as audited baseline;L50-B as new positive-power theorem candidate
CANDIDATES_REJECTED_WITH_REASON=L50-C:same homogeneous degree8 so no immediate exponent improvement beyond lane B and redundant before audit;L50-D:highest homogeneous degree12 in displayed family gives at best weaker naive rational-height exponent;L50-E:infinite rational face-cuboid classes and infinitely many positive-rank parameters are relevant but no repo-native uniform height count over the elliptic surface has yet been proved;L50-F:k=2 is C17 and no uniform rank/count theorem in k is currently certified;L50-G:correct squareclass target but no globally injective polynomial-height primitive family closed;L50-H:successful low-dimensional specialization already represented by C17 and no independent bulk count closed
POPULATION_ADAPTERS_PROVED=L50-B homogenizes to integer edges/two integer face diagonals/integer space diagonal;fixed cone 7/2<t<4 fixes canonical ordering;division by gcd preserves all required integer diagonals;third-face rational exceptions lie on genus7 curve and are finite;similarity fibers bounded by degree8 invariant;common Stage19 cutoff is the integer space diagonal D after primitive reduction
DISCOVERY_LEDGER_STATUS=COMPLETE
```

## Strongest-known / supersession check

Entering theorem:

```text
ENTERING_LOWER=N2(B)>>sqrt(log B)
ENTERING_LOWER_SOURCE=Stage24-50 audited C17 family
ENTERING_POSITIVE_POWER_STATUS=false
```

New lane B gives the candidate

```text
NEW_STRONGER_RESULT_FOUND=true
NEW_LOWER_CANDIDATE=N2(B)>>B^(1/4)
NEW_RESULT_SOURCE=Stage25-r501 parametric rational-height family
STRONGEST_KNOWN_CHECK=PASS_NEW_CANDIDATE_STRICTLY_STRONGER
```

No repository artifact found a previously audited positive-power lower for the exact Stage19 primitive/canonical population. The primary literature establishes adjacent rational face-cuboid parametrizations/infinitude but does not by itself provide the exact Stage19 counting theorem used here.

## Candidate mechanics

### L50-A — C17

Accepted audited baseline. Positive-rank elliptic height gives only `sqrt(log B)` because multiples have exponential coordinate height. Reused as a correctness baseline and as evidence that exactly-two infinitude is already settled.

### L50-B — Meskhishvili first parametrization

Accepted as the main new lane. After `t=m/n` and multiplying by `n^8`, all required rational lengths become homogeneous degree-eight integers. Reduced rational parameters in a fixed cone occur with density `gg T^2`, while space height is `O(T^8)`. The missing-face-square condition is a degree-16 squarefree hyperelliptic curve, genus seven, so only finitely many rational parameter exceptions survive. Similarity fibers are bounded by eight.

Candidate consequence: `N2(B)>>B^(1/4)`.

### L50-C — Meskhishvili third parametrization

Displayed formulas also have maximal homogeneous degree eight, so the same raw rational-height mechanism could at best reproduce exponent `1/4` without an extra cancellation or lower-degree invariant. Kept as an independent fallback family, not stacked before lane B audit.

### L50-D — Meskhishvili second parametrization

Displayed space height has degree twelve after homogenization. A two-dimensional rational-height count would naively give exponent `2/12=1/6`, weaker than lane B. No reason to prioritize it before lane B audit.

### L50-E — Yoshida elliptic face-cuboid structure

Yoshida constructs a finite-to-one map from elliptic data to rational face-cuboid similarity classes and proves infinitely many classes, plus infinitely many `s` with positive rank. This is potentially higher-dimensional input, but converting it into a polynomial-height lower for exact primitive Stage19 objects requires a uniform height/count theorem over varying fibers. That theorem is not yet supplied by the paper excerpt or repo.

Status: `OPEN_DEEPER_LANE`, potentially important for exponent `>1/4`.

### L50-F — symmetric multiplier k-family

Stage24 identified

`e=2kpq`, `x=k^2p^2-q^2`, `y=k^2q^2-p^2`

with space receiver `p^4+q^4=(k^4+1)Z^2`. `k=2` is C17. Aggregating many `k` could in principle create another parameter dimension, but no uniform rank/physical-cone/exactly-two theorem in `k` is proved.

Status: `OPEN_DEEPER_LANE`.

### L50-G/H — core/divisor receivers

Retained as structural lower receivers but no new polynomial-height family was closed in this batch.

## New deduction backflow ledger

If lane B passes fresh audit:

```text
BACKFLOW_STAGE24_N2_OVER_M2_LOWER=B^(-3/4)(log B)^(-5)
BACKFLOW_STAGE23_N2_OVER_N1_LOWER=B^(-3/4)(log B)^(-3)
BACKFLOW_STAGE25_N2_OVER_M1_LOWER=B^(-7/4)(log B)^(-1)
BACKFLOW_STAGE24_J2_LOWER=B^(1/4)(log B)^(-5)->infinity
BACKFLOW_CROSS_RATIO_I_LOWER=B^(1/4)(log B)^(-7)->infinity
PREVIOUS_GLOBAL_INTERACTION_SIGN=UNRESOLVED
NEW_INTERACTION_SIGN_CANDIDATE=POSITIVE_DIVERGENT
PREVIOUS_SECOND_ORDER_SIGN=UNRESOLVED
NEW_SECOND_ORDER_SIGN_CANDIDATE=POSITIVE_DIVERGENT
HISTORY_SUPERSESSION_BACKFLOW_REQUIRED_AFTER_AUDIT_PASS=true
```

No upstream frozen file is rewritten before audit.

## Sublane decision ledger

```text
LIVE_ROUTE_CANDIDATES=parametric-degree8;elliptic-surface-uniform-count;symmetric-k-aggregation;common-core;common-leg-space
SUBLANES_OPENED=Stage25-r501-parametric-positive-power
SUBLANES_DEFERRED=Stage25-r502-third-parametrization-cross-check;Stage25-r503-Yoshida-uniform-height;Stage25-r504-symmetric-k-aggregation;Stage25-r505-core-slices;Stage25-r506-common-leg-space
SUBLANE_DEFER_REASON=lane r501 already changes theorem class and should receive fresh hostile audit before stronger unreviewed counting claims are stacked;deferred lanes remain explicitly live for later deep batches
DEEP_RESEARCH_MODE=true
```

## Mandatory exploration layers

1. strongest source/target interfaces: `PASS`.
2. exact transition law: `PASS` via Stage25 endpoint semantics.
3. lower/construction search: `BREAKTHROUGH_CANDIDATE`.
4. alternate construction paths: `SEARCHED_6_PLUS_BASELINE`.
5. exact primitive/canonical adapter: `PROVED_CANDIDATE`.
6. third-face exactly-two control: `GENUS7_FALTINGS_CANDIDATE`.
7. bounded multiplicity: `DEGREE8_FIBER_BOUND_CANDIDATE`.
8. rational-height counting: `T^2_PARAMETERS_AT_T^8_HEIGHT`.
9. targeted computation: `EXACT_IDENTITY_REGRESSION_PLUS_MOD5_BEZOUT_ONLY`.
10. literature exploration: `PRIMARY_SOURCES_FOUND_AND_NOT_USED_AS_POPULATION_BLACK_BOX`.
11. new causal deductions: `RECORDED_AS_BACKFLOW_CANDIDATES`.
12. portable weapons: `DEFER_STAGE70_AFTER_AUDIT`.

```text
FORMULA_SUBSTITUTION_ONLY=false
FINITE_DATA_USED_AS_PROOF=false
EXPLORATION_EVIDENCE_COMPLETE=true
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_REASON=new strongest-certified positive-power theorem candidate and cross-stage supersession claims require fresh hostile audit
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=REGRESSION_ONLY_FOR_NEW_PARAMETRIC_THEOREM
NUM_NEW_COMPUTATION_JUSTIFIED=TARGETED_EXACT_IDENTITY_AND_SQUAREFREE_CERTIFICATE_ONLY
```
