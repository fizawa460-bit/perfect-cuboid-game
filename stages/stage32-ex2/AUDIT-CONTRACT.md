# Stage32EX2 hostile-audit contract

Invocation token: `stage32ex2-audit`.

This lane is independent from `stage32ex2-mainbatch`. It attacks the exact candidate as written; it does not continue research or push repairs while auditing.

## Audit startup

Read, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex2/AUDIT-CONTRACT.md`;
3. `stages/stage32-ex2/MAIN-STATE.json`;
4. exact target PR metadata, exact head, current `main`, and complete changed-file list;
5. only the changed files and exact source locks/verifiers needed for the claims under audit.

If the user supplies a PR/head, that exact target controls. Otherwise use the unique active EX2 candidate identified by state. If no unique candidate exists, fail closed rather than auditing a guessed lineage.

Do not use a mainbatch chat summary as mathematical evidence. Do not preload unrelated Stage32 history or other EX lanes.

## Read-only audit discipline

During hostile audit:

- do not push fixes;
- do not mutate state to make the candidate pass;
- do not merge;
- do not grant Stage32 MAIN promotion;
- do not strengthen a narrower reconstruction/decomposition result.

A moved head requires a new audit. FAIL returns to `stage32ex2-mainbatch` for repair on the same lineage unless the user explicitly chooses otherwise.

## Mandatory checks

### A. Exact Git/PR target

Record PR number/state, exact head, current main, freshness/divergence, draft/mergeability, changed-file scope, and relevant exact-head CI status. Freshness is a promotion gate, not a substitute for mathematical review.

### B. Startup/state/roadmap consistency

Check that `MAIN-START-HERE.md`, `MAIN-STATE.json`, and `stage32-ex2.md` agree on:

- separation of `stage32ex2-mainbatch` and `stage32ex2-audit`;
- current leaf and working set;
- `FULL_TARGET_CLOSURE` as a decision state with exactly two allowed terminal outcomes:
  - `GENUINE_V6_GENUS1_MEMBER_ESTABLISHED`;
  - `NO_INTEGRAL_IRREDUCIBLE_V6_GENUS1_MEMBER_IN_LINEAR_SYSTEM`;
- source-gap diagnosis, finite search miss, one reducible member, one fixed-component lemma, and one certified subspace are not terminal success;
- no automatic merge or Stage32 MAIN promotion.

Mutable state may route work but cannot weaken the completion contract.

### C. Object typing and source lock

For each claim, verify the exact object and model:

- Picard class / line bundle `L=O(D)`;
- actual section in `H^0(L)`;
- divisor scheme of the section;
- fixed and moving parts;
- strict transform / blow-down image;
- normalization / geometric component;
- field of definition.

Every transition between Picard64, known-curve labels, modular/theta coordinates, projective box coordinates, graded/ideal coordinates, or quotient/cover models requires an explicit source-bound adapter. Formal class equality alone is insufficient to identify an actual member.

### D. Fixed-component and linear-system scope

Hostile-test every fixed/moving statement:

- a component occurring in one known effective decomposition is not automatically fixed;
- negative intersection may force a component only under the exact effective/irreducible hypotheses used;
- a scan over retained known curves is not an exhaustive classification of all possible negative curves unless proved;
- a result for one symmetry eigenspace, finite ansatz, degree cutoff, or certified subspace is not a result for the complete linear system unless a spanning/exhaustiveness adapter is proved.

Any subspace-to-complete-system scope jump is FAIL for the stronger credit.

### E. Positive member verification

For `GENUINE_V6_GENUS1_MEMBER_ESTABLISHED`, verify one target member end-to-end:

1. explicit equation/section/ideal or equally replayable construction;
2. nonzero actual section on the exact surface/model;
3. exact Picard class V6 including fixed/exceptional corrections;
4. field recorded correctly;
5. actual member scheme materialized;
6. reducedness/integrality/irreducibility as required;
7. normalization/geometric genus exactly 1;
8. no hidden model, strict-transform, or population mismatch.

Riemann--Roch effectivity, `h^0>=294`, a reducible V6 divisor, a formal divisor class, a candidate polynomial, or a wrong-genus member is insufficient.

One fully verified positive member is enough for the positive EX2 terminal; unrelated members need not be classified.

### F. Negative linear-system verification

For `NO_INTEGRAL_IRREDUCIBLE_V6_GENUS1_MEMBER_IN_LINEAR_SYSTEM`, verify population-wide exhaustiveness. The proof must control every integral irreducible V6 member, for example by a complete section-space description, exhaustive fixed/moving decomposition, complete residual parameter space, or theorem applying to all members.

A solver miss, finite zero-hit, bounded sample, one coordinate ansatz, one eigenspace, one reducible member, or inability to materialize a section is never negative terminal evidence.

If a residual family or unclassified section space remains, `FULL_TARGET_CLOSURE` must be false.

### G. Genus/singularity bookkeeping

If genus is used, verify it belongs to the same explicit member. Distinguish arithmetic genus from geometric genus, and distinguish local curve singularities, ambient-surface singularities, exceptional intersection multiplicity, conductor, and delta. Do not identify unrelated masses/contacts with total delta without an exact adapter.

### H. Replay / verifier integrity

Replay compact verifiers or inspect exact CI evidence as appropriate. Check source hashes/digests and deterministic reconstruction. Do not rerun heavy computation merely for audit unless separately authorized; retained exact certificates are preferred.

### I. External authority firewall

EX2 does not by assertion change Stage32 MAIN, Q602/O210, survivors `[73,97,235]`, receiver/theorem/endpoint credit, or Perfect Cuboid claims. Any transfer requires its own current-target adapter and promotion gate.

## Credit ceiling

Classify the strongest supported result by name:

- `NO_CREDIT`;
- `NECESSARY_CONDITION_ONLY`;
- `BRANCH_EXCLUSION`;
- `EXPLICIT_MEMBER_CANDIDATE_UNVERIFIED`;
- `VERIFIED_V6_MEMBER_NONTERMINAL`;
- `AUDIT_READY_FULL_TARGET_CLOSURE` with exactly one terminal outcome;
- audited `FULL_TARGET_CLOSURE / GENUINE_V6_GENUS1_MEMBER_ESTABLISHED`;
- audited `FULL_TARGET_CLOSURE / NO_INTEGRAL_IRREDUCIBLE_V6_GENUS1_MEMBER_IN_LINEAR_SYSTEM`.

If `FULL_TARGET_CLOSURE` is claimed without exactly one valid terminal outcome, FAIL.

## Required audit output

Return one unambiguous `PASS` or `FAIL`, with exact head, current main, PR state, reviewed scope, exact-head CI status, strongest supported credit ceiling, selected terminal outcome if any, and every blocking finding.

PASS means only that the stated EX2 claim survives this contract at that exact head. It does not merge or automatically promote Stage32 MAIN. FAIL states the smallest concrete repair or missing proof boundary and stops; implementation belongs to `stage32ex2-mainbatch`.
