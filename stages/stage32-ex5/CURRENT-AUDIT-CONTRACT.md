# Stage32EX5 current hostile-audit contract

Invocation token: `stage32ex5-audit`.

This is the mutable current audit contract. `AUDIT-CONTRACT.md` is a historical Cycle1 source-locked contract and must remain byte-identical for retained evidence replay.

The audit lane is independent from `stage32ex5-mainbatch`. It attacks the exact candidate as written; it does not continue research, repair the branch, merge, or promote EX5 into Stage32 MAIN.

## Audit startup

Read, in this order:

1. `AGENTS.md`;
2. `stages/stage32-ex5/README.md`;
3. `stages/stage32-ex5/CURRENT-AUDIT-CONTRACT.md`;
4. `stages/stage32-ex5/MAIN-STATE.json`;
5. `stages/stage32-ex5/CURRENT-ROADMAP.md`;
6. exact target PR metadata/head, current `main`, Stage32 MAIN PR #1753 current authority, and complete changed-file list;
7. only the changed files and exact source locks/verifiers needed for the claims under audit.

If the user supplies a PR/head, that exact target controls. Otherwise resolve the active EX5 PR from `MAIN-STATE.json`. Fail closed if no unique target exists. Do not rely on chat summary as mathematical evidence.

## Current authority that the audit must enforce

Current Stage32 MAIN authority is `FULL178_AND_FINAL_MILESTONE_CHAIN`, with `32-01 FULL178` as the primary incomplete requirement. Current observed MAIN head is `a2cacaeb9b61eca34399952a7daaf5288ff3b826`.

N350 is the current Stage32 production-leaf certificate/producer-registration boundary, but its meta-contract is still pending its own fresh hostile audit and currently has an empty producer registry. Therefore current EX5 work receives zero N350/N104/FULL178 production coverage credit unless a later audited MAIN authority explicitly registers an EX5 producer.

Current-facing EX5 claims must keep V6/O210/Q602 and `[73,97,235]` as historical/formal provenance only. Old no-O210/Q602-credit statements are a historical-credit firewall, not current-frontier descriptions.

## Predecessor audit release

The long-lived predecessor PR #1742 hit the 100-commit freeze and then passed the required intermediate hostile audit on exact head `a5e59bab3f7fe5a31e356c5a78edcbd741b093a6`, review `5161068590`. It was merged to `main` at `bf2890ec0b8168f70db803de876024aa6b6d1f6d`. The freeze is released for current continuation, but the audited scope and credit ceilings remain binding.

Current continuation target is Draft PR #1762, branch `impl/stage32ex5-bc2-11-continuation`. Merge remains unauthorized.

## Current EX5 claim family

The active BC2 line is a FULL178 Picard64 / node-support interface and obstruction producer:

`compressed terminal/pairings -> exact Picard64 completion -> 59D witness when SAT -> canonical 48-node support interface`.

The retained exact local UNSAT prefix is ranks `0..398` of `(g1-d008,e=4)`. BC2-11 additionally rederives ranks `399..531` structurally, but grants no Picard64 closure credit. Its checkpoint canonical is `b7c3d16f415623dabd6356a2ed94794c96da51de39c7118a7b4ec706b7b81f0d`.

Current next leaf is `BC2_12_OUTER_RANK3_SYMBOLIC_X4_PARENT_PREFLIGHT`.

## Mandatory checks

### A. Exact Git/PR target and freshness

Record PR number/state, exact candidate head, current `main`, Stage32 MAIN #1753 head, freshness/divergence, draft/mergeability, changed-file scope, and exact-head CI. A moved head invalidates the previous audit.

### B. Startup/state/roadmap authority consistency

Check README, startup, `MAIN-STATE.json`, `CURRENT-ROADMAP.md`, PR body, and next-step agree that Stage32 mode is `FULL178_AND_FINAL_MILESTONE_CHAIN`, primary incomplete is `32-01 FULL178`, EX5 is auxiliary, BC2-11 is structural-only for ranks `399..531`, BC2-12 is current, and merge/MAIN promotion are separate explicit actions.

Historical `stage32-ex5.md` and `AUDIT-CONTRACT.md` remain source-locked historical artifacts.

### C. Exact evidence preservation

Retained local closures are source-locked:

- ranks `0..132`, BC2-05 canonical `cc62959ccf8c2939ff4024dc3a1e4ba59fdea38b7d33fd94817161b732c5284e`;
- ranks `133..265`, BC2-08 canonical `af197e67d3f56a6775f99f49aae59a14bc99bfa8c1b9b1d113749df3f1aa162c`;
- ranks `266..398`, BC2-10 canonical `1abeb2bd5299ed217840d028eb99ed961d98238cdec75b5286b05b7f066a752b`;
- ranks `399..531` structural BC2-11 canonical `b7c3d16f415623dabd6356a2ed94794c96da51de39c7118a7b4ec706b7b81f0d`.

Any canonical mismatch is FAIL for the associated claim. Semantic synchronization must not rewrite retained evidence merely to modernize terminology.

### D. BC2-11 structural replay

Re-run `bc2_11_next_exceptional_terminal_block_preflight.py` against the locked BC2-10 checkpoint and compare byte-for-byte with the retained BC2-11 checkpoint. Confirm ranks `399..531`, block width `133`, outer rank `3`, base terminal `[0,1,0,0,0,0,1,0,0,0,1]`, constant exceptional signature, exact rank/unrank round trips, and source `terminal_predicate` replay. Confirm solver/heavy compute was not invoked and no Picard64 closure was granted.

### E. BC2-12 interpretation

If BC2-12 is present, derive fixed/residual exceptional mass from the exact BC2-11 terminal signature rather than assuming a prior outer-rank pattern. Any parent partition, solver result, UNKNOWN refinement, or SAT witness must be replayable under the retained selected64/all140 Picard model. UNKNOWN is never UNSAT.

### F. FULL178 / N350 promotion firewall

A finite EX5 block is not population-wide FULL178 completion. N350 currently accepts production coverage only from a registered exact producer with a source-locked replay verifier and hostile-audit PASS. Until current Stage32 MAIN's N350 contract itself passes hostile audit and explicitly registers such a producer, EX5 output has zero N350/N104 production-coverage credit. Picard64 SAT alone is explicitly not a full project-native production leaf.

### G. UNSAT and SAT scope

UNSAT may receive local obstruction credit only for its exact certified terminal/block/model. SAT must reconstruct the exact Picard64/59D witness when claimed, but is not by itself an effective curve, actual carrier, rational point, production leaf, FULL178 completion, or final milestone.

### H. Historical/formal provenance

Cycle1, early BC2, V6/O210/Q602, and formal Q602 residues may be cited only at retained historical scopes. The historical-credit firewall forbids silently reopening or claiming new credit for that line unless current Stage32 MAIN explicitly requires it.

### I. Computational/replay integrity

Replay compact evidence/verifiers. Heavy computation must not be rerun merely for audit unless separately authorized by a fresh run key. Sample/finite evidence cannot be widened without completeness.

### J. Merge and endpoint firewall

Merge is unauthorized unless explicitly requested by the user. No EX5 local result alone grants Stage32 final-milestone, theorem, endpoint, or Perfect Cuboid existence/nonexistence credit.

## Credit ceiling

Use precise scopes such as `LOCAL_EXACT_INTERFACE_PREFLIGHT`, `LOCAL_EXACT_PICARD64_BLOCK_UNSAT / <rank interval>`, or `EXACT_PICARD64_WITNESS_INTERFACE / <terminal>`. `N350_REGISTERABLE_EXACT_PRODUCER_CANDIDATE` is permitted only after a complete source-locked producer adapter/verifier exists; it still grants no N350 coverage until MAIN-side hostile-audited registration.

## Required audit output

Return one unambiguous `PASS` or `FAIL`. Record exact head, current main, Stage32 MAIN #1753 authority head, reviewed delta/scope, CI/replay status, strongest supported credit ceiling, N350 compatibility finding, historical-provenance findings, and every blocker.

`PASS` does not merge and does not automatically promote anything into Stage32 MAIN. `FAIL` states the smallest concrete repair or missing proof boundary and stops; implementation belongs to `stage32ex5-mainbatch`.
