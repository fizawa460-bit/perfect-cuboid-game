# Stage29 roadmap R2 — audit contract

This file records the intended semantic changes of the post-29-02 roadmap rewrite. The canonical roadmap change is on the same branch; the canonical controller is intentionally not rewritten before fresh audit.

## Why R2 exists

The original roadmap assumed that 29-06 and 29-07 would still need to discover/develop the global endpoint and joint-cover models. Audited 29-02 work already produced substantially more infrastructure than that assumption allowed, including the full endpoint surface, joint V4 model, F7 degree-64 sign/Kummer cover, F8 Campedelli quotient layer, Beauville/modular/L-function/Brauer routes, and the non-Fano/Hirzebruch recognition adapter.

R2 therefore changes Stage29 from

```text
find global model -> compare three entrances -> choose one route
```

to

```text
synthesize audited foundations
-> prove exact bridges
-> attack several serious routes in parallel
-> prune only with evidence
-> compress late
```

## Load-bearing policy changes

```text
ROADMAP_IS_LIVING=true
PREMATURE_SINGLE_ROUTE_SELECTION=false
MULTI_ROUTE_ATTACK_ALLOWED=true
PARALLEL_ROUTE_PORTFOLIO_DEFAULT=true
ROUTE_PRUNING_REQUIRES_EVIDENCE=true
FINAL_COMPRESSION_AT_29_16=true
```

Every GAP_SCAN is also a ROADMAP_REVIEW checkpoint.

## Critical firewall retained

R2 does not claim that Stage16–20 are already literal successive levels of the F7 degree-64 cover.

```text
FULL_ENDPOINT_IS_DEGREE64_SIGN_KUMMER_COVER=true
STAGE16_20_AS_LITERAL_SIGN_TOWER_LEVELS_PROVED=false
POPULATION_TRANSFER_TO_SIGN_TOWER_AUTOMATIC=false
```

29-03/04/07 must decide and prove the exact bridge scope.

## Renamed/reframed stages

```text
29-03 FOUNDATION_BACKFLOW_AND_ROADMAP_RATIFICATION
29-04 POPULATION_PREDICATE_AND_CONDITION_COST_MATRIX
29-05 DEPENDENCY_EQUIVALENCE_AND_DOUBLE_CHARGE_LEDGER
29-06 GLOBAL_FOUNDATION_SYNTHESIS
29-07 SIGN_TOWER_JOINT_V4_AND_POPULATION_BRIDGE
29-08 PARAMETRIZATION_FIBRATION_AND_COVERAGE_ATLAS
29-09 FULL_ENDPOINT_LOCAL_ARITHMETIC
29-10 GLOBAL_AND_K3_ATTACK_PORTFOLIO
29-11 QUOTIENT_DESCENT_AND_MODULAR_ATTACK_PORTFOLIO
29-12 JOINT_LOCAL_PARAMETRIC_AND_INTERACTION_ATTACK_PORTFOLIO
29-13 A2_METHOD_TRANSFER_ACROSS_SURVIVING_ROUTES
29-14 NATURAL_SLICE_QUOTIENT_AND_COVERAGE_TEST
29-15 ENDPOINT_ARSENAL_REMATCH
29-16 RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO
29-17 PERFECT_CUBOID_ATTACK_HANDOFF
```

## Audit questions

Fresh audit should attack at least:

1. Does R2 over-promote the F7 sign/Kummer cover to a universal organizer before KUM3A/B/KUM4 are proved?
2. Does any renamed stage silently assume population/height/primitivity transfer?
3. Are 29-10/11/12 genuinely nonredundant portfolios, or are some mechanisms double-counted?
4. Is 29-16 late enough for route compression, or does any earlier exact dependency force pruning sooner?
5. Does the living-roadmap rule risk loop/research drift, and are the materiality triggers restrictive enough?
6. Are `Q` versus `Q(i)` and Q-form/twist firewalls preserved throughout?
7. Does any current unresolved candidate, especially `R29-PESCH1`, get incorrectly classified as an existing adapter?
8. Is the controller-delta proposal metadata-preserving and consistent with the merged 29-02hd state?

## Submission state

```text
ROADMAP_R2_SUBMISSION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_AFTER_AUDIT_AND_MERGE=29-03_FOUNDATION_BACKFLOW_AND_ROADMAP_RATIFICATION
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
