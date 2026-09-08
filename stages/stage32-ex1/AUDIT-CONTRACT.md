# Stage32EX1 hostile-audit contract

Invocation token: `stage32ex1-audit`.

This lane is independent from `stage32ex1-mainbatch`. Its job is to attack the exact candidate as written, not to continue the research or repair the branch while auditing.

## Audit startup

Read, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex1/AUDIT-CONTRACT.md`;
3. `stages/stage32-ex1/MAIN-STATE.json`;
4. exact target PR metadata, exact head, current `main`, and the complete changed-file list;
5. only the changed files and exact source locks/verifiers needed to test the claims under audit.

If the user supplies a PR number/head, that exact target controls. Otherwise use `MAIN-STATE.json.audit.exact_head` / the active Stage32EX1 work PR when they identify one unambiguously. If no unique candidate can be resolved, fail closed rather than auditing a guessed branch.

### Retained-audit projection exception

A retained consolidation may deliberately leave `MAIN-STATE.json` unchanged because that mutable resume projection is itself source-locked by existing claims. In that case startup/state consistency may be satisfied only through the fail-closed overlay `stages/stage32-ex1/RETAINED-AUDIT-PROJECTION.json`.

The overlay is valid only when all of the following hold: the exact target PR equals the projection's declared PR; the live head branch equals its declared branch; the exact head is refetched from PR metadata at audit time; the declared retained manifest exists at that exact head; the overlay preserves both terminal outcomes and points back to the unchanged roadmap completion contract; and every no-credit/no-merge firewall in the projection remains false. Any missing file, PR/branch mismatch, moved-head ambiguity, or attempt to use the overlay as mathematical authority is FAIL.

When this exception applies, `MAIN-STATE.json` remains the ordinary mainbatch resume projection and is not required to pretend that the retained audit candidate is its current mathematical leaf. For audit routing only, the projection's `audit_routing_overlay.current_leaf` and `working_set` replace the mutable current-leaf/working-set fields in `MAIN-STATE.json`. All fixed completion semantics, authority firewalls, and audited predecessor facts must still agree with `MAIN-START-HERE.md`, `MAIN-STATE.json`, and `stage32-ex1.md`. This exception cannot weaken the completion contract, alter a prior hostile-audit result, grant credit, or avoid re-audit after a moved head.

Do not rely on a mainbatch chat summary as mathematical evidence. Do not preload unrelated Stage32 history or other Stage32EX lanes.

## Read-only hostile-audit discipline

During the audit:

- do not push fixes to the candidate branch;
- do not change `MAIN-STATE.json` to make the candidate pass;
- do not merge;
- do not grant Stage32 MAIN promotion;
- do not reinterpret a narrower claim as a stronger one.

A FAIL is returned to `stage32ex1-mainbatch` for repair on the same working lineage unless the user explicitly chooses otherwise. A moved head invalidates the previous audit; audit the new exact head again.

## Mandatory checks

### A. Exact Git/PR target

Record:

- PR number and state;
- exact candidate head SHA;
- current `main` SHA;
- base/head freshness or divergence;
- draft/mergeability status;
- changed-file scope;
- exact-head CI/workflow status when applicable.

Freshness is a promotion gate, not a substitute for mathematical review. Docs-only absence of a relevant workflow is reported as such rather than fabricated as CI success.

### B. Startup/state consistency

Check that `MAIN-START-HERE.md`, `MAIN-STATE.json`, and `stage32-ex1.md` agree on:

- the `stage32ex1-mainbatch` / `stage32ex1-audit` separation;
- the current leaf and working set, except when the exact retained-audit projection exception above is valid and supplies the audit-only leaf/working set;
- `FULL_TARGET_CLOSURE` as an umbrella decision state with exactly two allowed terminal outcomes: `ALL_V6_GENUS1_CARRIERS_EXCLUDED` and `GENUINE_SURVIVING_CARRIER_ESTABLISHED`;
- the fact that finite ledger, data-gap diagnosis, one-branch exclusion, and a merely formal/effective divisor class are not terminal success;
- no automatic merge or Stage32 MAIN promotion.

Mutable state may route work but may not silently weaken the roadmap completion contract or delete either terminal outcome from the state machine. A retained-audit overlay may route an exact audit candidate but may not mutate or reinterpret ordinary `MAIN-STATE.json` source locks.

### C. Source and population lock

For every promoted mathematical statement, verify the exact population, field, Picard class, integrality/irreducibility assumptions, resolution convention, and source locators. A source-lock mismatch, population change without adapter, or use of an unaudited mutable candidate as theorem authority is FAIL for the affected credit.

### D. Normalization-location exhaustiveness

Hostile-test the central scope boundary on the exclusion route:

- normalization non-bijectivity must not be localized to the `47` met surface nodes without proof;
- the surface-node multibranch branch and smooth-ambient curve-singularity branch must remain distinct until an exhaustive adapter joins them;
- any further locus required by the exact resolution model must be accounted for;
- a globally non-bijective normalization statement alone does not choose a local branch.

Premature localization is FAIL.

These population-wide exhaustiveness requirements are required for the exclusion terminal, not for a positive terminal backed by one fully verified actual target member.

### E. Delta/contact bookkeeping

Verify locally and globally that:

- required total delta `472` comes from the fixed genus/arithmetic-genus relation under the exact source lock;
- exceptional support count `47` and exceptional total mass `266` retain their actual geometric meaning;
- `266` is not substituted for or subtracted from `472` without an exact local/global identity or inequality justifying the operation;
- local delta, conductor, branch multiplicity, exceptional intersection, and support count are not conflated;
- overlapping local/global restrictions are not double-counted.

Any unsupported `266 -> delta` identification is FAIL.

### F. Credit ceiling and terminal-decision adapter

Classify the strongest supported result by name, not roadmap number:

- `NO_CREDIT`;
- `NECESSARY_CONDITION_ONLY`;
- `BRANCH_EXCLUSION`;
- `AUDIT_READY_FULL_TARGET_CLOSURE` with one declared terminal outcome;
- `FULL_TARGET_CLOSURE / ALL_V6_GENUS1_CARRIERS_EXCLUDED` only after exact-head hostile-audit PASS of the complete exclusion/exhaustiveness certificate;
- `FULL_TARGET_CLOSURE / GENUINE_SURVIVING_CARRIER_ESTABLISHED` only after exact-head hostile-audit PASS of a complete positive witness certificate.

A finite table, sample zero-hit, missing-data diagnosis, blocked route, or formal divisor/class cannot be promoted to full closure.

For `ALL_V6_GENUS1_CARRIERS_EXCLUDED`, verify that every integral irreducible V6 genus-1 carrier in the fixed target is covered and every residual configuration is disposed.

For `GENUINE_SURVIVING_CARRIER_ESTABLISHED`, verify one actual target member end-to-end: exact construction or identification, Picard class V6, field, integrality, irreducibility, geometric genus `1`, and the target-membership adapter. Population-wide disposal of unrelated residual configurations is **not** required for this positive terminal. A formal V6 divisor, Riemann--Roch effectivity statement, reducible member, nonintegral scheme, wrong-field member, or genus not exactly `1` is insufficient.

If `FULL_TARGET_CLOSURE` is asserted without exactly one valid terminal outcome, FAIL.

### G. Replay/verifier integrity

When a leaf has a verifier/certificate, replay the verifier or inspect exact CI evidence as appropriate. Check digest/source locks and deterministic reconstruction. Heavy computation must not be rerun merely to perform an audit unless separately authorized and required; use retained compact evidence when valid.

### H. External authority firewall

Verify that the candidate does not, by Stage32EX1 assertion alone, change Stage32 MAIN, Q602/O210, survivors `[73,97,235]`, receiver/theorem/endpoint credit, or Perfect Cuboid existence/nonexistence claims. Such promotion requires its own current-target adapter and authority gate.

## Required audit output

Return one unambiguous result: `PASS` or `FAIL`. Record the exact head, current main, PR state, reviewed scope, exact-head CI status, strongest supported credit ceiling, the selected terminal outcome if any, and every blocking finding. When repository review posting is available, place one hostile-audit review/comment anchored to the exact candidate head.

`PASS` means only that the stated Stage32EX1 claim survives this contract at that exact head. It does not merge and does not automatically promote to Stage32 MAIN. `FAIL` must state the smallest concrete repair or missing proof boundary and then stop; implementation belongs to `stage32ex1-mainbatch`.
