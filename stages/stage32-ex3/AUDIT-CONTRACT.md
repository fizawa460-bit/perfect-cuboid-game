# Stage32EX3 hostile-audit contract

Invocation token: `stage32ex3-audit`.

This lane is independent from `stage32ex3-mainbatch`. Its job is to attack the exact candidate as written, not to continue the research or repair the candidate while auditing.

## Audit startup

Read, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex3/AUDIT-CONTRACT.md`;
3. `stages/stage32-ex3/MAIN-STATE.json`;
4. exact target PR metadata, exact head, current `main`, and complete changed-file list;
5. only changed files plus exact source locks/verifiers needed for the claims under audit.

If the user supplies a PR/head, that exact target controls. Otherwise resolve the unique candidate from `MAIN-STATE.json.audit` / active work PR. If no unique exact candidate is available, fail closed rather than guessing.

Do not rely on a mainbatch chat summary as mathematical evidence. Do not preload unrelated Stage32 history or other EX lanes.

## Read-only hostile-audit discipline

During audit:

- do not push fixes;
- do not edit state to make a candidate pass;
- do not merge;
- do not grant Stage32 MAIN promotion;
- do not silently strengthen a narrow monodromy or cover claim.

A FAIL returns to `stage32ex3-mainbatch` for repair on the same working lineage unless the user explicitly chooses otherwise. A moved head requires a new audit.

## Mandatory checks

### A. Exact Git/PR target

Record PR number/state, exact candidate head, current `main`, freshness/divergence, draft/mergeability status, changed-file scope, and exact-head CI status when applicable. Freshness is a promotion gate, not a substitute for mathematical review.

### B. Startup/state consistency

Check that `MAIN-START-HERE.md`, `MAIN-STATE.json`, and `stage32-ex3.md` agree on:

- command split `stage32ex3-mainbatch` / `stage32ex3-audit`;
- current leaf and working set;
- `FULL_TARGET_CLOSURE` as a decision state with exactly two allowed terminal outcomes: `O210_COVER_GEOMETRY_EXCLUDED` and `GENUINE_O210_COVER_CONFIGURATION_ESTABLISHED`;
- finite monodromy ledgers, abstract Nielsen classes, source gaps, and residue pruning as intermediate only;
- no automatic merge or Stage32 MAIN promotion.

### C. Exact object/type lock

For every load-bearing statement identify the exact object and map. Hostile-test confusion among:

- carrier and normalization `N`;
- Beauville/common-cover normalization `Y`;
- further product-cover component `D`;
- targets `X(4)`, `X(8)`, `C0`;
- first and second projection maps;
- V4/G quotient maps;
- correspondence `Gamma` and Jacobian operator `T`.

A degree or ramification total moved from one map/model to another without an exact adapter is FAIL for that credit.

### D. Numerical cover boundary

Verify source/provenance and scope for every claimed fixed value, including as applicable:

- degrees `(105,81)`;
- `q'=4`;
- `O=210`;
- first-projection ramification `0` / étale statement;
- second-projection ramification `192` before the appropriate descent and `48` only on the exact descended map;
- genus `106` where derived on the correct source curve;
- contact histogram `210 x m1 + 28 x m2`;
- `Q(T)=602` only through the retained correspondence/Rosati adapter.

Unsupported mixing of `192` and `48`, or of N-level and Y/D-level degrees, is FAIL.

### E. Contact-to-ramification semantics

Hostile-test any use of O210 contact data. The audit must reject:

- `one contact = one ramification point` unless locally proved;
- exceptional multiplicity identified with ramification index without a local model;
- cusp-fiber multiplicity promoted to interior branch data;
- aggregated contact mass substituted for Riemann--Hurwitz ramification without a proved summation identity.

Every local species must retain its exact quantification domain.

### F. Monodromy / Nielsen exhaustiveness

For any finite group or branch-cycle claim verify:

- correct degree and target base/orbifold;
- connectedness/transitivity assumptions;
- inertia conjugacy classes and total ramification;
- product-one/generation conditions where required;
- simultaneous compatibility of the two projections rather than two unrelated cover searches;
- all allowed imprimitivity/intermediate-cover branches;
- the quotient/equivalence relation used to deduplicate tuples;
- exhaustiveness of the enumeration before a zero-hit is used for exclusion.

A finite sample or bounded candidate list without an exhaustiveness proof is not O210 exclusion.

### G. Geometric realizability adapter

An abstract permutation tuple or Nielsen class is not automatically a modular/algebraic cover with the required marked geometry. If realizability is claimed, verify the theorem/construction applies to the correct base curve, marked cusps, local ramification, common-cover tower, and field.

For the positive terminal outcome, additionally verify attachment to the **same actual V6 carrier**. A standalone cover, even if algebraically realizable, is insufficient.

### H. Common-cover/V4 scope

Check that the retained common-cover identity is used at its exact scope. If it is automatic for a genuine carrier, it cannot be promoted into a contradiction merely by restating it. Any new pruning requires an additional independent predicate with a source-bound adapter.

### I. Correspondence / Q602 adapter

Any claimed downstream effect on `Gamma`, `T`, `Q=602`, or residues `[73,97,235]` must identify the exact same correspondence orientation, retained basis/marking, and population. Abstract conjugacy or unmarked monodromy does not select a W-line or decimal residue.

A residue reduction may be valid intermediate credit while O210 remains open. Do not promote it to EX3 terminal exclusion without the full carrier-to-cover argument.

### J. Credit ceiling and terminal decision

Classify the strongest supported result by name:

- `NO_CREDIT`;
- `NECESSARY_CONDITION_ONLY`;
- `BRANCH_EXCLUSION`;
- `AUDIT_READY_FULL_TARGET_CLOSURE` with exactly one declared terminal outcome;
- `FULL_TARGET_CLOSURE / O210_COVER_GEOMETRY_EXCLUDED` only after exact-head hostile-audit PASS of a complete population-preserving exclusion/exhaustiveness certificate;
- `FULL_TARGET_CLOSURE / GENUINE_O210_COVER_CONFIGURATION_ESTABLISHED` only after exact-head hostile-audit PASS of a complete actual-carrier-attached positive cover certificate.

For exclusion, every admissible residual cover/monodromy/geometric-realization case must be disposed. For the positive terminal, one end-to-end carrier-attached configuration suffices; unrelated residual cases need not be eliminated.

### K. Replay/verifier integrity

Replay compact verifiers/certificates or inspect exact CI evidence as appropriate. Check digests/source locks and deterministic reconstruction. Heavy computation is not automatically rerun for audit; use retained exact compact evidence unless separate authorization is necessary.

### L. External authority firewall

A Stage32EX3 assertion alone must not alter Stage32 MAIN, Q602/O210, survivors `[73,97,235]`, O212+ progression, receiver/theorem/endpoint credit, or Perfect Cuboid conclusions. Such promotion requires a separate current-target authority step.

## Required audit output

Return one unambiguous `PASS` or `FAIL`. Record exact head, current main, PR state, reviewed scope, exact-head CI status, strongest supported credit ceiling, selected terminal outcome if any, and every blocking finding.

`PASS` means only that the stated Stage32EX3 claim survives this contract at that exact head. It does not merge and does not automatically promote to Stage32 MAIN. `FAIL` should identify the smallest concrete repair or missing proof boundary and stop; implementation belongs to `stage32ex3-mainbatch`.
