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
7. only changed files and exact source locks/verifiers needed for the claims under audit.

If the user supplies a PR/head, that exact target controls. Otherwise resolve the active EX5 PR from `MAIN-STATE.json`. Fail closed if no unique target exists. Do not rely on chat summary as mathematical evidence.

## Current authority

Stage32 MAIN authority is `FULL178_AND_FINAL_MILESTONE_CHAIN`, with `32-01 FULL178` primary incomplete. Observed MAIN authority head is `b07bfc2b206d960e6e95d36cb9c50198720f7dce`; observed repository main for this continuation is `5ca6acba4b591d9e2d40057241c850598c1fa1df`.

N350 remains the current production-leaf certificate/producer-registration boundary, pending its own fresh hostile audit with an empty producer registry. EX5 therefore has zero N350/N104/FULL178 production-coverage credit unless later hostile-audited MAIN authority explicitly registers an EX5 producer.

V6/O210/Q602 and `[73,97,235]` are historical/formal provenance only. Old no-O210/Q602-credit statements are a historical-credit firewall, not current-frontier descriptions.

## Current audit target and claim family

Current continuation target is Draft PR #1764, branch `stage32ex5-mainbatch-bc2-12`. Merge remains unauthorized.

The retained local exact UNSAT prefix is ranks `0..398` of `(g1-d008,e=4)`. BC2-11 structurally rederived ranks `399..531`, canonical `b7c3d16f415623dabd6356a2ed94794c96da51de39c7118a7b4ec706b7b81f0d`.

BC2-12 then derives fixed/residual exceptional mass `3/1` from that exact terminal and evaluates the complete 20-parent symbolic-x4 Picard64 partition. Retained result:

- 17 exact UNSAT;
- 3 UNKNOWN;
- 0 SAT;
- UNKNOWN parent IDs `1,6,8`;
- selected one-based labels `135,125,120`;
- exactly one full-exceptional refinement subcase per UNKNOWN parent;
- retained evidence canonical `67c48b8230c36567384e68ee413756074462de134a2d2451ca3dc3c034f642d7`.

UNKNOWN is never UNSAT. Therefore ranks `399..531` are not yet Picard64-closed and the exact UNSAT prefix remains `0..398`.

Current next leaf is `BC2_13_OUTER_RANK3_UNKNOWN_PARENT_FULL_EXCEPTIONAL_REFINEMENT`.

## Mandatory checks

### A. Exact Git/PR target and freshness

Record PR number/state, exact candidate head, current `main`, Stage32 MAIN #1753 head, freshness/divergence, draft/mergeability, changed-file scope, and exact-head CI. A moved head invalidates the previous audit.

### B. Startup/state/roadmap consistency

Check README, startup, `MAIN-STATE.json`, `CURRENT-ROADMAP.md`, PR body, and verifier agree on Stage32 mode, primary incomplete `32-01 FULL178`, BC2-12 `17 UNSAT / 3 UNKNOWN / 0 SAT`, exact prefix `0..398`, BC2-13 three-subcase routing, N350 firewall, and separate merge/MAIN promotion actions.

Historical `stage32-ex5.md` and `AUDIT-CONTRACT.md` remain source-locked historical artifacts.

### C. Prior exact evidence preservation

Retained local locks are:

- ranks `0..132`, BC2-05 canonical `cc62959ccf8c2939ff4024dc3a1e4ba59fdea38b7d33fd94817161b732c5284e`;
- ranks `133..265`, BC2-08 canonical `af197e67d3f56a6775f99f49aae59a14bc99bfa8c1b9b1d113749df3f1aa162c`;
- ranks `266..398`, BC2-10 canonical `1abeb2bd5299ed217840d028eb99ed961d98238cdec75b5286b05b7f066a752b`;
- ranks `399..531` structural BC2-11 canonical `b7c3d16f415623dabd6356a2ed94794c96da51de39c7118a7b4ec706b7b81f0d`.

Any canonical mismatch is FAIL. Semantic synchronization must not rewrite retained evidence.

### D. BC2-11 replay

Re-run `bc2_11_next_exceptional_terminal_block_preflight.py` against locked BC2-10 and compare byte-for-byte with retained BC2-11. Confirm ranks `399..531`, width `133`, outer rank `3`, base terminal `[0,1,0,0,0,0,1,0,0,0,1]`, exact rank/unrank and source `terminal_predicate` replay, and no solver/Picard64 credit.

### E. BC2-12 retained evidence

Recompute the canonical digest of `bc2-12-outer-rank3-parent-preflight-evidence.json`. Confirm source locks bind BC2-11 canonical/replay stream, selected64/all140 Picard model, manifest/prefix/adapter locks, and Z3 version.

Confirm the mass split `3/1` is derived from the BC2-11 terminal rather than inherited from another outer-rank pattern. Confirm complete parent count `20`, exact result `17 UNSAT / 3 UNKNOWN / 0 SAT`, UNKNOWN IDs `1,6,8`, labels `135,125,120`, and total exact refinement size `3`. Confirm `rank_399_to_531_block_exact_unsat_authorized=false` and `rank_399_to_531_block_picard64_closed=false`.

The timed parent run need not be rerun merely for audit; retained compact evidence and exact source-lock/replay structure are the authority unless a fresh run is separately authorized.

### F. BC2-13 routing ceiling

The next research unit may refine only the three retained UNKNOWN subcases. It must not rerun or reopen the 17 exact-UNSAT parents and must not widen beyond ranks `399..531` without a new explicit route. Any remaining UNKNOWN keeps the block open; any SAT routes only to the exact witness/node-support interface.

### G. FULL178 / N350 promotion firewall

A finite EX5 block is not population-wide FULL178 completion. Until N350 itself passes hostile audit and MAIN explicitly registers an exact source-locked producer, EX5 output has zero N350/N104 production-coverage credit. Picard64 SAT alone is not a full project-native production leaf.

### H. Historical/formal provenance

Cycle1, early BC2, V6/O210/Q602, and formal Q602 residues may be cited only at retained historical scopes. The historical-credit firewall forbids silently reopening or claiming new credit for that line.

### I. Merge and endpoint firewall

Merge is unauthorized unless explicitly requested by the user. No EX5 local result alone grants Stage32 final-milestone, theorem, endpoint, or Perfect Cuboid existence/nonexistence credit.

## Credit ceiling

The strongest new BC2-12 credit is `LOCAL_EXACT_INTERFACE_PARENT_PREFLIGHT / ranks 399..531 / 17 parent branches UNSAT, 3 parent branches UNKNOWN`. It is not `LOCAL_EXACT_PICARD64_BLOCK_UNSAT` for ranks `399..531`.

## Required audit output

Return one unambiguous `PASS` or `FAIL`. Record exact head, current main, Stage32 MAIN #1753 authority head, reviewed delta/scope, CI/replay status, BC2-12 canonical/result, strongest supported credit ceiling, N350 compatibility finding, historical-provenance findings, and every blocker.

`PASS` does not merge and does not automatically promote anything into Stage32 MAIN. `FAIL` states the smallest concrete repair or missing proof boundary and stops; implementation belongs to `stage32ex5-mainbatch`.
