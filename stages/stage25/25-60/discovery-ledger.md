# Stage25-60 discovery ledger

```text
DISCOVERY_CHECKPOINT=Stage25-60
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS,PRIMARY_LITERATURE
SEARCHED_PATHS=stages/stage25/25-50/**;stages/stage23/post-stage25-r01/result.md;stages/stage24/post-stage25-r01/result.md;stages/stage21/final.md;stages/stage22/22-controller.json;docs/stage14-15-bound-attack-map.md;docs/stage14-15-bound-deep-review-queue.md;docs/cycle-exploration-safety-protocol.md;Meskhishvili arXiv:1502.02375;Yoshida arXiv:2407.09825
SEARCH_TERMS=causal interaction;cross ratio;order of conditions;independence correction;primitive gcd;parametric height rigidity;uniform varying-fiber height;moving elliptic surface;symmetric k;common core;common leg space
STRUCTURAL_SIGNATURES=M1~B^2logB;M2~Blog^5;N1~Blog^3;N2>>B^1/4;N2<<B^1/2+epsilon;interaction cross ratio;degree8 parametric family;moving elliptic fibers
DEPENDENCY_NEIGHBORS=Stage16;Stage16S;Stage17;Stage18;Stage19;Stage21;Stage22;Stage23;Stage24;Stage25-50;Stage14/15 Q03-Q11
CANDIDATES_FOUND=R501 audited positive-power family;R502 Meskhishvili third parametrization;R503 Yoshida uniform varying-fiber height;R504 symmetric-k aggregation;R505 common squarefree-core;R506 common-leg plus space;R507 R501 primitive-height rigidity
CANDIDATES_ACCEPTED=R507 exact primitive-height rigidity;R504 generic non-torsion moving section as structural progress;exact causal cross-ratio I as checkpoint60 synthesis theorem
CANDIDATES_REJECTED_WITH_REASON=R502 no exponent upgrade from same degree8 rational-height mechanism;R503 not rejected and remains live but load-bearing uniform varying-fiber height count is not proved;R504 current certified section height too costly for exponent upgrade;R505 no closed independent dimension/height count;R506 no closed independent dimension/height count
POPULATION_ADAPTERS_PROVED=all global causal ratios use previously audited common Stage16/17/18/19 cutoff/population adapters;R501 primitive reduction changes height only by bounded factor;R504 is retained as a structural route and is not promoted to a Stage19 global count
DISCOVERY_LEDGER_STATUS=COMPLETE
```

## Persistent route-name registry

The route names were already allocated at checkpoint50 and remain stable through checkpoint60 and later audits:

```text
R501=Meskhishvili_first_positive_power_family
R502=Meskhishvili_third_parametrization_fallback
R503=Yoshida_uniform_varying_fiber_height
R504=symmetric_k_aggregation
R505=common_squarefree_core
R506=common_leg_plus_space
R507=R501_primitive_height_rigidity
ROUTE_IDS_PERSIST_ACROSS_CHECKPOINTS=true
ROUTE_IDS_ARE_NOT_AUDIT_ROUND_NUMBERS=true
```

A refinement keeps its route ID. Only a genuinely new mathematically distinct route receives the next unused ID (`R508`, `R509`, ...).

## Causal decomposition

With

`F=M2/M1`, `S=N1/M1`, `A=N2/M2`, `T=N2/N1`,

the exact cross-ratio is

\[
I=A/S=T/F=N_2M_1/(M_2N_1).
\]

The audited post-checkpoint50 lower gives

\[
I(B)\gg B^{1/4}(\log B)^{-7}\to\infty.
\]

This is the correction to the naive product `F*S`; it is not an independence claim.

## R507 — primitive-height rigidity of R501

For reduced parameters in the fixed physical cone, the exact primitive gcd is

\[
g=2^{7[m,n\text{ both odd}]}3^{4[3\mid m]}\le10368.
\]

Therefore primitive reduction cannot lower the degree-eight height by an unbounded polynomial factor. Combining the checkpoint50 lower with the reverse parameter count gives

\[
N_{R501}(B)=\Theta(B^{1/4}).
\]

This closes the hidden-gcd route to an exponent upgrade for R501.

## R503 — Yoshida varying-fiber route

Status: `LIVE_HIGH_VALUE_EXTERNAL_THEOREM_GATE`.

Yoshida supplies a finite-to-one elliptic-data description and infinitely many positive-rank parameters, but Stage25 still lacks a uniform theorem counting suitable rational points with controlled physical height while the elliptic fiber varies. The required input must respect the exact primitive/canonical Stage19 measure and cannot be replaced by positive-rank infinitude alone.

Stage14/15 Q03 and Q05 show the same theorem species was historically missing for nearby moving-elliptic/genus-one receivers. Thus another algebraic rephrasing is not enough; the live receiver needs a genuinely uniform height/count input.

## R504 — symmetric-k aggregation

A generic non-torsion moving section is established by specialization at `k=2`, with an explicit `3P` rational section checked against the elliptic group law. This is real structural progress and keeps R504 live. However the presently certified rational functions have height growth too large to improve the global `1/4` exponent after summing the available parameter dimensions.

Status: `LIVE_STRUCTURAL_NO_EXPONENT_UPGRADE_YET`.

## R505 / R506

Both remain live structural receivers. Neither currently has a certified independent parameter dimension plus physical-height estimate sufficient to produce a new polynomial lower. They are not marked dead.

## Stage14/15 route audit

```text
S1415_ATTACKS_REVIEWED=Q03,Q05,Q07,Q08,Q09,Q10,Q11
S1415_Q03_RELEVANCE=MOVING_ELLIPTIC_HEIGHT_UNIFORMITY_GATE
S1415_Q05_RELEVANCE=MOVING_GENUS_ONE_GLOBAL_AGGREGATION_GATE
S1415_Q07_Q10_RELEVANCE=RECONSTRUCTION_DISPERSION_PELL_INTERNAL_ROUTES_EXHAUSTED_WITHOUT_NEW_INPUT
S1415_Q11_RELEVANCE=QUALITATIVE_LOCAL_SIEVE_NOT_A_LOWER_COUNT
```

No exhausted route is reopened without the required materially new input.

## Continuation / stopping discipline

Checkpoint60 is not single-shot. Audit PASS on one submission certifies those claims but does not close checkpoint60 while assigned high-value routes remain actionable.

```text
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
LIVE_ROUTE_CANDIDATES=R503,R504,R505,R506
SUBLANES_OPENED=R507
SUBLANES_REJECTED=NONE_GLOBALLY
SUBLANE_BUDGET=CONTINUE_AFTER_AUDITED_MERGE
NEXT_CHECKPOINT_AFTER_THIS_AUDIT_IF_LIVE_ROUTES_REMAIN=60
STAGE70_ALLOWED=false
```

Checkpoint60 may advance to70 only after each live route is proved, negatively certified for upgrade, or reduced to a precise external theorem gate, and after no repo-native mutation satisfying the Stage14/15 reopen rules remains unexecuted.

```text
FORMULA_SUBSTITUTION_ONLY=false
FINITE_DATA_USED_AS_PROOF=false
EXPLORATION_EVIDENCE_COMPLETE=true
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_REASON=checkpoint60 adds causal interaction classification,R501 Theta-growth rigidity,and generic R504 moving-section theorem
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=REGRESSION_ONLY_NO_NEW_CENSUS
NUM_NEW_COMPUTATION_JUSTIFIED=TARGETED_GCD_AND_SECTION_IDENTITY_REGRESSION_ONLY
```
