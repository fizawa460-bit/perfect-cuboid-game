# Stage32EX4 hostile-audit contract

Invocation token: `stage32ex4-audit`.

This lane is independent from `stage32ex4-mainbatch`. It attacks the exact candidate as written and does not continue research or repair the branch while auditing.

## Audit startup

Read, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex4/AUDIT-CONTRACT.md`;
3. `stages/stage32-ex4/MAIN-STATE.json`;
4. exact target PR metadata, exact head, current `main`, and complete changed-file list;
5. only the changed files and exact source locks/verifiers needed to test the claims under audit.

If the user supplies a PR/head, that exact target controls. Otherwise use the unique active EX4 candidate identified by `MAIN-STATE.json`. If no unique candidate can be resolved, fail closed rather than guessing.

Do not treat mainbatch narrative as mathematical evidence. Do not preload unrelated Stage32 history or other EX lanes.

## Read-only hostile-audit discipline

During audit:

- do not push fixes;
- do not edit state to make the candidate pass;
- do not merge;
- do not grant Stage32 MAIN promotion;
- do not replace an absolute-marking claim with a weaker gauge/conjugacy claim after the fact;
- do not promote an unaudited/provisional source merely because the candidate depends on it.

A FAIL returns to `stage32ex4-mainbatch` for repair on the same lineage unless the user explicitly chooses otherwise. A moved head requires a new audit.

## Mandatory checks

### A. Exact Git/PR target

Record PR state, exact head, current main, freshness/divergence, draft/mergeability, changed-file scope, and exact-head CI status when applicable.

Freshness is a promotion gate, not a substitute for mathematical review.

### B. Startup/state/roadmap consistency

Verify that `MAIN-START-HERE.md`, `MAIN-STATE.json`, and `stage32-ex4.md` agree on:

- `stage32ex4-mainbatch` / `stage32ex4-audit` separation;
- current leaf and working set;
- exactly two allowed terminal outcomes: `ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED` and `FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE`;
- gauge choice, inner-conjugacy orbit, source-gap diagnosis, conditional residue, and partial source inventory are not terminal success;
- no automatic merge or Stage32 MAIN promotion.

Mutable state may route work but may not weaken the roadmap completion contract.

### C. Source authority and object typing

For every load-bearing arrow in the claimed marking chain, verify:

- exact source locator/blob/canonical where applicable;
- actual hostile-audit/authority status;
- exact mathematical object on both sides of the arrow;
- field/model/basis/ordering conventions;
- whether the arrow is source-proved, reconstructed, conditional, or merely an abstract isomorphism.

In particular, post1648 Cecotti trace/orientation material must not be self-promoted beyond its actual audited status.

A mismatch of `C0`, `J(C0)[2]`, retained F2^4 basis, torsor plane `W`, V4/H characters, branch-point labels, or generator conventions is FAIL for the affected credit.

### D. Absolute-versus-gauge marking test

Hostile-test the central claim:

- a chosen representative is not enough;
- a trace/order/group-presentation match is not enough;
- an inner-conjugacy orbit is not an explicit conjugating element;
- `delta_0inf in W` is not a unique W-line;
- finding one conjugator is insufficient if other admissible conjugators send `delta_0inf` to different W-lines.

For a positive terminal, require either uniqueness of the admissible conjugator at the needed level or proof that all admissible conjugators produce the same retained W-line.

### E. Curve-side and retained-side independence

Verify the source-side curve/Weierstrass action independently from the retained-side `J[2]`/lattice representation. Check that the same desired residue was not used to choose the conjugator that is then claimed to recover that residue.

Explicit source automorphisms must be converted to branch-point/J[2] action from their actual formulas or an exact source theorem. Named-generator identifications cannot be inferred from order/relations alone.

### F. Residue-selection adapter

For `ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED`, replay the complete chain:

`source marked datum -> source J2/branch marking -> admissible conjugator -> retained J2 basis -> delta_0inf W-line -> retained line-to-residue table`.

Verify that exactly one of `73,97,235` is selected and that allowed coordinate/model changes transport the marking coherently.

Then enforce the credit ceiling: `3 -> 1` is not `1 -> 0`. Selection alone does not exclude Q602/O210.

### G. Bounded obstruction terminal

For `FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE`, require:

- the frozen source package is named exactly;
- all admissible identifications under that package are exhaustively covered;
- the residual ambiguity subgroup is explicit;
- its orbit on the three nonzero W-lines is computed exactly;
- uniqueness truly fails;
- the minimal new datum/re-entry condition is named.

This result must remain bounded to that source package. Any claim of literature-wide or mathematical impossibility is FAIL.

### H. Cross-model/Galois/circularity checks

Where applicable verify that complex conjugation, Galois action, level-structure changes, hyperelliptic coordinate changes, ppav basis changes, or Stoll/Cecotti/FSM model isomorphisms do not produce an untracked alternative marking.

An imported other-stage marking must have a population/model-preserving adapter to the same Bolza/torsor/J2 target.

### I. Replay/verifier integrity

Replay leaf verifiers or inspect exact CI evidence. Check deterministic reconstruction, source hashes, canonical digests, and no hidden dependence on mutable narrative state.

Do not rerun heavy computation merely for audit unless separately authorized and necessary; prefer retained compact evidence.

### J. External authority firewall

Verify that EX4 assertion alone does not change Stage32 MAIN, exclude Q602/O210, authorize O212+, grant receiver/theorem/endpoint credit, or claim Perfect Cuboid existence/nonexistence.

A positive EX4 result may become a Stage32 MAIN residue-contraction candidate only through a separate current-target promotion adapter.

## Credit classification

Classify the strongest supported result by name:

- `NO_CREDIT`;
- `NECESSARY_CONDITION_ONLY`;
- `MARKING_AMBIGUITY_REDUCTION_ONLY`;
- `AUDIT_READY_FULL_TARGET_CLOSURE / ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED`;
- `AUDIT_READY_FULL_TARGET_CLOSURE / FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE`;
- after exact-head hostile-audit PASS, the corresponding `FULL_TARGET_CLOSURE` outcome.

Do not use roadmap step numbers as credit names.

## Required audit output

Return one unambiguous `PASS` or `FAIL`. Record exact head, current main, PR state, reviewed scope, exact-head CI status, strongest supported credit ceiling, terminal outcome if any, and every blocking finding.

When repository review posting is available, place one hostile-audit review/comment anchored to the exact candidate head.

`PASS` means only that the stated EX4 claim survives this contract at that exact head. It does not merge or auto-promote. `FAIL` must identify the smallest concrete repair or missing proof boundary and stop; implementation belongs to `stage32ex4-mainbatch`.
