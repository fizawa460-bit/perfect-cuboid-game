# Stage32EX5 hostile-audit contract

Invocation token: `stage32ex5-audit`.

This lane is independent from `stage32ex5-mainbatch`. Its job is to attack the exact candidate as written, not to continue research or repair the branch while auditing.

## Audit startup

Read, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex5/AUDIT-CONTRACT.md`;
3. `stages/stage32-ex5/MAIN-STATE.json`;
4. exact target PR metadata, exact head, current `main`, and complete changed-file list;
5. only the changed files and exact source locks/verifiers needed for the claims under audit.

If the user supplies a PR/head, that exact target controls. Otherwise resolve the unique candidate from `MAIN-STATE.json.audit` / active EX5 work PR. Fail closed if no unique candidate exists.

Do not rely on a chat summary as mathematical evidence. Do not preload unrelated Stage32 history or other EX lanes.

## Read-only discipline

During audit:

- do not push fixes;
- do not mutate state to make the candidate pass;
- do not merge;
- do not grant Stage32 MAIN promotion;
- do not widen a bounded EX5 claim into a Stage32 theorem.

A moved head invalidates the previous audit.

## Mandatory checks

### A. Exact Git/PR target

Record PR number/state, exact candidate head, current main, freshness/divergence, draft/mergeability, changed-file scope, and exact-head CI when applicable.

### B. Startup/state/roadmap consistency

Check that startup, state, and roadmap agree on:

- `stage32ex5-mainbatch` / `stage32ex5-audit` separation;
- current breadth cycle, leaf, and working set;
- `EX5_ROUTE_DECISION_CLOSURE` as a local route-decision state, not Stage32 closure;
- exactly two terminal outcomes:
  - `QUALIFIED_INDEPENDENT_STAGE32_ROUTE_ESTABLISHED`;
  - `FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE`;
- no automatic merge or Stage32 promotion.

### C. Receiver population and coverage lock

Hostile-test the load-bearing EX5 quantifier. Every receiver ledger row and any coverage/exhaustion claim must be traceable to the frozen Stage29 -> Stage32 authority chain with exact population semantics.

Check genus/branch/multibranch, field/model, degree/mask/height domain when relevant, numerical-vs-geometric status, and effectivity/existence distinctions.

A receiver ledger that omits an authority-required population, silently changes a mask/field/quantifier, or infers exhaustiveness from repository search is FAIL for breadth/exhaustion credit.

### D. Current-status provenance

For each ledger status (`CLOSED`, `OPEN`, `UNKNOWN`, `CONDITIONAL`, `OUT_OF_SCOPE`), verify the exact evidence/source and semantic adapter. Mutable state assertions alone do not close rows.

V6/O210/Q602 must not be treated as the definition of all Stage32 receivers unless the frozen authority explicitly proves such a reduction.

### E. Clean-room and asset-dedup discipline

Check that clean-room candidate generation precedes existing-asset solution lookup for the frozen cycle, and that EX5-04 uses the repository asset-discovery chain.

A keyword/theorem/card match is not applicability. Verify object, field, population, and quantifier compatibility for every imported asset.

### F. Route qualification

A positive terminal requires all eight roadmap qualification items:

1. exact receiver target;
2. population adapter;
3. exact new input;
4. forward implication;
5. reverse-scope firewall;
6. falsifiable execution unit;
7. retained nontrivial receiver effect;
8. replay path.

A route score, idea list, literature suggestion, missing-adapter diagnosis, sample result, or preflight-only predicate is insufficient.

The retained effect must be exact on its declared population: an exclusion, strict necessary-condition shrinkage of an exhaustive set, population-preserving reduction, or exact bridge to an audited external weapon.

### G. Bounded exhaustion

A negative terminal is valid only for an explicitly frozen receiver ledger and candidate universe. Verify every frozen candidate is classified as disproved, duplicate/dominated, inapplicable, blocked with named re-entry condition, or qualified.

`FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE` must never be phrased as "no other route exists" or literature-wide/mathematics-wide exhaustion.

### H. Independence and cross-stage imports

For a claimed independent route, verify it is not merely MAIN/EX1-EX4 under different wording. Cooperation is allowed, but duplicate decisive predicates do not count as independent breadth discovery.

Any imported Stage33/35/36 or other-EX result must have exact authority status plus object/model/field/population adapter. Provisional evidence may be explored but cannot support terminal credit.

### I. Computational/replay integrity

When an artifact/verifier exists, replay or inspect exact CI evidence as appropriate. Heavy computation must not be rerun merely for audit unless separately authorized. Finite/sample evidence cannot be widened without a completeness certificate.

### J. External authority firewall

Verify the candidate does not by EX5 assertion alone change Stage32 MAIN, Q602/O210, survivors `[73,97,235]`, O212+, FULL178, receiver/theorem/endpoint credit, or Perfect Cuboid existence/nonexistence claims.

## Credit ceiling

Classify the strongest supported result as one of:

- `NO_CREDIT`;
- `NECESSARY_CONDITION_ONLY`;
- `BRANCH_EXCLUSION` for an explicitly named receiver branch;
- `AUDIT_READY_EX5_ROUTE_DECISION_CLOSURE / <terminal outcome>`;
- `EX5_ROUTE_DECISION_CLOSURE / QUALIFIED_INDEPENDENT_STAGE32_ROUTE_ESTABLISHED` only after exact-head hostile-audit PASS of the complete positive route certificate;
- `EX5_ROUTE_DECISION_CLOSURE / FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE` only after exact-head hostile-audit PASS of the complete bounded-exhaustion certificate.

None of these labels automatically means Stage32 `FULL_TARGET_CLOSURE`.

## Required audit output

Return one unambiguous `PASS` or `FAIL`. Record exact head, current main, PR state, reviewed scope, exact-head CI status, strongest supported credit ceiling, selected terminal outcome if any, and every blocking finding.

`PASS` does not merge and does not automatically promote anything into Stage32 MAIN. `FAIL` states the smallest concrete repair or missing proof boundary and stops; implementation belongs to `stage32ex5-mainbatch`.
