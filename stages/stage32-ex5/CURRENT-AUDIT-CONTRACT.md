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

If the user supplies a PR/head, that exact target controls. Otherwise resolve the active EX5 PR from `MAIN-STATE.json`. Fail closed if no unique target exists.

Do not rely on chat summary as mathematical evidence. Do not preload unrelated Stage32 history or other EX lanes.

## Current authority that the audit must enforce

Current Stage32 MAIN authority is `FULL178_AND_FINAL_MILESTONE_CHAIN`, with `32-01 FULL178` as the primary incomplete requirement.

Current-facing EX5 claims must therefore satisfy all of the following:

- V6 is not described as the current attack target;
- O210 is not described as the current attack target;
- Q602 is not described as the current attack target;
- `[73,97,235]` is not described as the current survivor population;
- if `[73,97,235]` appears, it is explicitly historical/formal Q602 provenance;
- old no-O210/Q602-credit statements are treated as historical-credit firewalls rather than current-frontier descriptions.

Historical retained artifacts may retain their original vocabulary and source locks. Audit must distinguish immutable proof/evidence provenance from mutable current-state prose.

## Current EX5 claim family

The active BC2 line is a FULL178 Picard64 / node-support interface and obstruction producer:

`compressed terminal/pairings -> exact Picard64 completion -> 59D witness when SAT -> canonical 48-node support interface`.

The Stage32 MAIN consumption boundary is `32-01-178/N150` or its audited successor. EX5 does not grant MAIN credit by asserting compatibility; a current-target population adapter and MAIN-side acceptance are required.

## Mandatory checks

### A. Exact Git/PR target and freshness

Record PR number/state, exact candidate head, current `main`, Stage32 MAIN #1753 head, freshness/divergence, draft/mergeability, changed-file scope, and exact-head CI when applicable. A moved head invalidates the previous audit.

For long-lived PR #1742, also apply `docs/research-os/policies/hostile-audit-and-freshness.md`. At the 100-commit retained checkpoint, freeze the exact head and perform an intermediate delta-bounded hostile audit before further substantive retained research.

### B. Startup/state/roadmap authority consistency

Check that README, startup, `MAIN-STATE.json`, `CURRENT-ROADMAP.md`, PR body, and next-step agree that:

- Stage32 mode is `FULL178_AND_FINAL_MILESTONE_CHAIN`;
- primary incomplete is `32-01 FULL178`;
- EX5 is an auxiliary interface/obstruction research surface for that chain;
- current EX5 exact frontier matches the latest retained BC2 checkpoint;
- V6/O210/Q602 and `[73,97,235]` are not presented as live current targets/survivors;
- merge and MAIN promotion are separate explicit actions.

Also verify that historical `stage32-ex5.md` and `AUDIT-CONTRACT.md` remain source-locked historical artifacts rather than mutable current prose.

### C. Exact evidence preservation

Semantic synchronization must not rewrite retained mathematical evidence merely to modernize terminology.

Current retained local closures include:

- ranks `0..132`, BC2-05 checkpoint canonical `cc62959ccf8c2939ff4024dc3a1e4ba59fdea38b7d33fd94817161b732c5284e`;
- ranks `133..265`, BC2-08 checkpoint canonical `af197e67d3f56a6775f99f49aae59a14bc99bfa8c1b9b1d113749df3f1aa162c`;
- ranks `266..398`, BC2-10 checkpoint canonical `1abeb2bd5299ed217840d028eb99ed961d98238cdec75b5286b05b7f066a752b`.

Any canonical mismatch is FAIL for the associated exact claim.

### D. FULL178 population/interface adapter

For any claim intended for Stage32 MAIN consumption, verify exact population semantics: FULL178 row/terminal identity; degree/exceptional-mass and assignment-order semantics; terminal-rank/pairing adapter; selected64/all140 Picard64 model; witness reconstruction when SAT; 48-node support mapping when consumed; and quantifier scope of any finite block or population claim.

A finite block obstruction is not population-wide FULL178 completion without exhaustive coverage or another exact compression/adapter.

### E. UNSAT interpretation

An exact UNSAT result may receive local obstruction credit only for its certified terminal/block/model. Reject promotion to whole stratum, FULL178, effectivity, final milestone, theorem, endpoint, or Perfect Cuboid nonexistence unless separately proved.

### F. SAT interpretation

A SAT result must reconstruct the exact Picard64/59D witness and pass the retained node-support consumer when that interface is claimed. SAT is not by itself an effective curve, actual carrier, rational point, FULL178 completion, or final-milestone proof.

### G. Historical/formal provenance

Cycle1, early BC2, V6/O210/Q602, and formal Q602 residues may be audited as historical retained authority at their original scopes. Do not require old immutable evidence files to use current terminology. Current-facing prose/state must label them correctly.

The historical-credit firewall means EX5 cannot silently recompute, reopen, mutate, or claim new V6/O210/Q602 credit unless current Stage32 MAIN explicitly reopens that line.

### H. Claim promotion and N150 boundary

Check the current Stage32 MAIN `N150` external-consumption gate before any EX5-to-MAIN promotion. Newer EX5 progress than the N150 snapshot is local EX5 authority only until MAIN explicitly consumes it. An EX5 PR update, hostile-audit PASS, or local checkpoint does not automatically advance N150, `32-01`, or any final milestone.

### I. Computational/replay integrity

Replay exact compact evidence/verifiers as appropriate. Heavy computation must not be rerun merely for audit unless separately authorized by a fresh run key. UNKNOWN cannot be promoted to UNSAT. Sample or finite evidence cannot be widened without completeness.

### J. Merge and endpoint firewall

Verify merge is unauthorized unless the user explicitly authorizes it; no Stage32 final-milestone credit is inferred from EX5 alone; and no Perfect Cuboid existence/nonexistence claim is made from EX5 local evidence.

## Credit ceiling

Use precise current scope, for example:

- `NO_CREDIT`;
- `LOCAL_EXACT_INTERFACE_PREFLIGHT`;
- `LOCAL_EXACT_PICARD64_BLOCK_UNSAT / <rank interval>`;
- `EXACT_PICARD64_WITNESS_INTERFACE / <terminal>`;
- `MAIN_CONSUMABLE_FULL178_ADAPTER_CANDIDATE` only when the current-target adapter is complete and audit-ready.

None automatically means `32-01 FULL178` complete or Stage32 closure.

## Required audit output

Return one unambiguous `PASS` or `FAIL`. Record exact head, current main, Stage32 MAIN #1753 authority head, reviewed delta/scope, CI/replay status, strongest supported credit ceiling, historical-provenance findings, and every blocker.

`PASS` does not merge and does not automatically promote anything into Stage32 MAIN. `FAIL` states the smallest concrete repair or missing proof boundary and stops; implementation belongs to `stage32ex5-mainbatch`.
