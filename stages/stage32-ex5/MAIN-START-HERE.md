# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order:

1. `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. `stages/stage32/MAIN-STATE.json` for current Stage32 routing;
4. `stages/stage32-ex5/README.md`;
5. this file;
6. `MAINBATCH-OPERATIONS.md`;
7. `MAIN-STATE.json`;
8. only the active EX5 working set.

Historical Cycle1 files remain source-locked provenance.

## Current authority

PR #1765 is merged at `98c5710dad4ca9a006e93b273ecf5259733e03aa`; it is not an active working PR. There is no ordinary EX5 active PR encoded at this startup boundary. Current Stage32 routing must be read from `stages/stage32/MAIN-STATE.json` rather than from the old #1765 base SHA.

N355 remains the latest consumed pruning authority recorded by current Stage32 compact state and N356 remains retained `AUDIT_REQUIRED` with zero new MAIN pruning credit. The e=4 EX5 local exact prefix remains `0..797`.

## Retained boundary

BC2-24 remains the latest retained EX5 result: 4 newly UNSAT parents, `19` retained UNKNOWN, 0 SAT; known parent-UNSAT lower bound `7145`; `172` other BC2-19 UNKNOWN identities remain uninferred. The whole first block, whole stratum, and FULL178 remain open.

The retained BC2-24 files remain the startup replay set until a new BC2-25 checkpoint is created.

## Executable post-merge boundary

The old merge-first stop rule is complete. On a new `stage32ex5-mainbatch` invocation:

1. synchronize current main and Stage32 MAIN routing;
2. replay/validate the retained BC2-24 state and firewalls;
3. search for duplicate/obsolete routes;
4. if still useful, open only the bounded `BC2_25_POST_MERGE_UNKNOWN_REFINEMENT_PREFLIGHT` continuation on a fresh work surface;
5. do not rerun BC2-20..24 and do not launch broad/heavy scale-out by default.

UNKNOWN must not be relabelled UNSAT. No Stage32 MAIN, N350, theorem, receiver, effectivity, endpoint, or Perfect Cuboid credit follows automatically.
