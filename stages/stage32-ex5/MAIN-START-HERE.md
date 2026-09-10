# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order:

1. `AGENTS.md`;
2. `stages/stage32-ex5/README.md`;
3. this file;
4. `stages/stage32-ex5/MAIN-STATE.json`;
5. only `MAIN-STATE.json.current_leaf_working_set`.

Do not preload unrelated Stage32 history, other EX lanes, Research OS, or large retained payloads unless the active leaf explicitly triggers them.

## Current authority

Stage32 remains `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is primary/incomplete. Observed MAIN PR #1753 head is `b1d44137e0dd87cd3a604221715596d9b3574bc5`. N349C hostile-audit handoff is the latest observed MAIN attack checkpoint; N350 remains the separate fail-closed production-registration boundary. V6/O210/Q602 and `[73,97,235]` are historical/formal provenance only.

## Current frontier

The retained local `(g1-d008,e=4)` exact Picard64 UNSAT prefix is `0..664`.

BC2-15 has additionally rederived ranks `665..797` structurally: outer exceptional rank `5`, base terminal `[0,1,0,0,0,0,2,0,0,0,1]`, exceptional signature `[0,1,0,0,0,2,0,0,0,1]`, `133/133` rank/unrank replay exact, `133/133` source `terminal_predicate` replay exact, replay SHA `6655d249aa6d51cea8fe9bd7108c315c523b5ee1725d36dd1a1a537e11d4724f`, checkpoint canonical `f88ebe53c4300c01fc0a4870cc0dca75a0a091b60c95c8da7e00926bcee43182`.

No solver/heavy compute was used by BC2-15. No Picard64 UNSAT credit is granted for `665..797`; exact closure remains `0..664`.

## Current unit

`BC2_16_OUTER_RANK5_SYMBOLIC_X4_PARENT_PREFLIGHT`.

BC2-16 may construct the exact symbolic-x4 selected-exceptional parent partition only for ranks `665..797`, deriving fixed/residual exceptional mass from the retained BC2-15 terminal signature. Heavy/artifact-producing execution requires its own dedicated fresh run-key authorization.

## Claim-DAG state

BC2-15 is structural-only, so the last synchronization remains BC2-14 retained consolidation. EX5 continues to attack `S32.FULL178.NUMERICAL_CENSUS.V1`; no ACTIVE-FRONTIER remap, claim-core mutation, or MAIN promotion occurs here.

Each invocation executes one bounded unit and stops at a coherent checkpoint. Historical `stage32-ex5.md` and `AUDIT-CONTRACT.md` remain immutable source-locked Cycle1 records. Do not merge without explicit user authorization; Draft PR #1765 remains the working surface.
