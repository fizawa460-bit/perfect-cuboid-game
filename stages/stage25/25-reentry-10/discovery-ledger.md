# Stage25-reentry-10 discovery ledger

```text
TASK_ID=Stage25-um-r001a
DISCOVERY_PHASE=25-reentry-10
DISCOVERY_CHECKPOINT=PRE_STAGE
DISCOVERY_LEDGER_STATUS=COMPLETE
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
```

## Search evidence

```text
SEARCHED_PATHS=docs/stage14-arsenal.md;docs/stage14-arsenal-index.md;docs/stage14-num-reuse-index.md;docs/stage14-15-bound-attack-map.md;docs/stage14-15-bound-attack-ledger/part-*.jsonl;docs/stage14-15-bound-deep-review-queue.md;stages/stage16*;stages/stage17;stages/stage18;stages/stage19;stages/stage20;stages/stage21;stages/stage22;stages/stage23;stages/stage24;stages/stage25;docs/stage20-arsenal.md;docs/stage21-arsenal.md;docs/stage22-arsenal-promotion.md;docs/stage23-arsenal-promotion.md;docs/stage24-arsenal-promotion.md;docs/stage25-arsenal-promotion.md;PRs_950_957_966_979_984_999_1000_1001
SEARCH_TERMS=exactly-one;exactly-two;three faces;Euler;integral space;quarter-power;half-power;moving family;common core;Kummer;Prym;Selmer;small point;fixed-prime;growing modulus;reconstruction;Pell;directional;shared edge;shared hypotenuse
STRUCTURAL_SIGNATURES=PYTHAGOREAN_FACE,INTEGRAL_SPACE_DIAGONAL,EXACTLY_TWO_FACES,THREE_FACES_EULER,PAIRED_NORMS,COMMON_CORE,MOVING_MODULUS,DIRECTIONAL_CHAMBER,OVERLAP_INTERSECTION,K3_SURFACE_COVER,ELLIPTIC_GENUS_ONE
DEPENDENCY_NEIGHBORS=Stage16,Stage16S,Stage17,Stage18,Stage19,Stage20,Stage21,Stage22,Stage23,Stage24,Stage25,Stage14-e8/e10/e11,Stage15-6,Q01-Q11,S20-W01-W03,S21-W01-W02,S25-W01-W04
```

The five JSONL shards match their manifest hashes and contain all 824 indexed Stage14/15 results. This phase did not pretend that all 380 `review_required` records received a new theorem audit. It performed a full machine inventory plus source-level reading of the route clusters and terminal artifacts that match the current receivers.

## Accepted Stage14/15 attack components

| IDs | Accepted use | Receiver boundary |
|---|---|---|
| `S1415-ATTACK-0215`, `S1415-ATTACK-0216`, `S1415-ATTACK-0217`, `S1415-ATTACK-0224` | two-face toric height, Euler K3 cover, exact local blocker law, explicit `eta<1/46` upper | phase60; e10's fixed-prime result is causal, e11 is the quantitative upper |
| `S1415-ATTACK-0259`, `S1415-ATTACK-0260`, `S1415-ATTACK-0261` | full-2-torsion/Selmer architecture and the genuine first-small-point height gate | phases20/30; positive rank alone never counts physical points |
| `S1415-ATTACK-0204`, `S1415-ATTACK-0522`, `S1415-ATTACK-0544`, `S1415-ATTACK-0583` | rank-one/Pluecker, discriminant, two-conic and twisted-Kummer normal-form collision checks | phases20/30; no global count transfers automatically |
| `S1415-ATTACK-0724`, `S1415-ATTACK-0728`, `S1415-ATTACK-0729`, `S1415-ATTACK-0731` | exact moving genus-one receiver and fixed-core reductions | phase20 as an external-uniformity boundary, not a ready global theorem |
| `S1415-ATTACK-0748` | admissible physical-diagonal support receiver `Y^2=F1F2`, `Y<=2B` | phase20; required global support theorem remains unproved |
| `S1415-ATTACK-0791`, `S1415-ATTACK-0793`, `S1415-ATTACK-0794`, `S1415-ATTACK-0796`, `S1415-ATTACK-0800` | exact survivor reconstruction, divisor-many core list and Pell completion | phase20; vertical `B^o(1)` multiplicity is not horizontal density saving |
| `S1415-ATTACK-0818`, `S1415-ATTACK-0819`, `S1415-ATTACK-0820` | same-measure local squareclass law, fixed-finite-prime refined count and qualitative zero density | phase20; no fixed power without effective growing-modulus uniformity |

## Rejected or fenced candidates

| IDs / cluster | Classification | Reason |
|---|---|---|
| `0709`, `0710` / Q01 | `ALREADY_CONSUMED` | Stage25 already supersedes the older ambient-family attack; not a new route |
| Q02 population-mismatched uses | `ADAPTER_REQUIRED` | toric coordinates and subtraction discipline transfer, ambient mass does not become an `N2` lower |
| `0724`, `0728`, `0729`, `0731` / Q05 as a direct theorem | `EXTERNAL_FUTURE_GATE` | same-measure uniform moving-curve aggregation is missing |
| `0748` / Q06 as a proved bound | `EXTERNAL_FUTURE_GATE` | support count `<<B^(1/2+o(1))` is a target, not a theorem |
| `0771`, `0772` / Q08 | `P3_EXHAUSTED_INTERNAL` | pointwise gcd-product domination was tested and blocked in the current normal form |
| `0796`, `0804`, `0807`, `0809`, `0811` / Q09 | `P3_EXHAUSTED_INTERNAL` | positive support cannot replace centered dispersion; no legal same-measure large-sieve adapter |
| `0811`, `0812`, `0814`, `0816`, `0817` / Q10 | `P3_EXHAUSTED_INTERNAL` | Pell/residual switch was executed and proved exponent-neutral with current inputs |
| `0216` as a fixed-power sieve | `SUPERSEDED_OR_INSUFFICIENT` | fixed-prime ordered limits prove qualitative zero density only; e11 supplies the certified log saving |
| `NUM-R01` finite `N3=0` rows | `FINITE_ONLY` | cannot imply perfect-cuboid nonexistence |

No P3 cluster is reopened. A future reopen must name a new equation, height monotonicity, same-measure spectral estimate, or external theorem as required by the deep-review queue.

## Current-stage and PR reconciliation

The merged closeouts #950, #957, #966, #979, #1000 and reentry unlock #1001 override historical `CANDIDATE_PENDING_*` or `CLOSED_PENDING_MERGE` strings inside submitted artifacts. The Stage25 checkpoint50 hostile-audited PR #984 supersedes the historical Stage19/23/24 lower interfaces. Phase10 records this precedence in `interface-registry.json` instead of rewriting historical submission files.

## Compatibility map

| Reuse class | Population | Cutoff | Multiplicity | Measure | Quantifier | Decision |
|---|---|---|---|---|---|---|
| Stage25 quarter-power backflow to Stage19/23/24 | exact | exact | exact | exact | exact | accept |
| Stage14-num to Stage19 target census | exact after mask selection | exact `d=R` | exact | exact finite objects | finite only | accept as regression |
| Stage14-num to Stage18 ambient denominator | no direct match | exact cutoff only | adapter required | mismatch | finite only | reject direct use |
| Stage20 Euler weapons to phase60 | target exact | exact | phase60 adapter required | phase60 adapter required | uniformity varies by weapon | queue as receiver input |
| Stage15 fixed-prime sieve to phase20 | target exact | exact | exact labeled physical states | exact | fixed-set then `B`, then primes | accept qualitative only |
| moving genus-one/Prym/common-core gates | target-compatible subfamilies | mixed | mixed | no global adapter | external uniformity missing | external boundary |

## Numerical preflight

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,NUM-R05,NUM-R06,NUM-R07,NUM-R08
NUM_POPULATION_MATCH=MIXED_WITH_NAMED_ADAPTERS
NUM_EVIDENCE_LEVEL=EXACT_FINITE_OR_FINITE_DIAGNOSTIC_ONLY
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED_FOR_PHASE10
FINITE_DATA_PROMOTED_TO_THEOREM=false
```

## Completion markers

```text
CANDIDATES_FOUND=S1415_Q01_Q11;AR001_AR039;NUM_R01_R08;S20_W01_W03;S21_W01_W02;STAGE22_24_PROMOTIONS;S25_W01_W04
CANDIDATES_ACCEPTED=SEE_ACCEPTED_TABLE
CANDIDATES_REJECTED_WITH_REASON=SEE_REJECTED_TABLE
POPULATION_ADAPTERS_PROVED=POST_STAGE25_BACKFLOW_EXACT;NUM_R01_STAGE19_MASK_EXACT
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true
NEW_RESEARCH_JUSTIFIED=PHASE10_RECEIVER_AND_LIFECYCLE_SYNCHRONIZATION
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_REASON=STRONGEST_INTERFACE_AND_OPEN_GATE_CLASSIFICATION
DISCOVERY_AUDITOR=Stage25-reentry-audit
DISCOVERY_AUDIT_VERDICT=PENDING
```
