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

## Active work surface

PR #1776 is the active EX5 work/audit surface. BC2-25 is retained: 3 newly exact-UNSAT parents, `16` retained UNKNOWN parents, 0 SAT; known parent-UNSAT lower bound `7148`; the other `172` BC2-19 UNKNOWN identities remain uninferred. Whole-first-block, whole-stratum and FULL178 closure remain false.

The first hostile audit failed at exact head `9bbc491cfde0f8a7f48d9742dad8ff368e4837b2`, review `5176133548`, because retained-verifier/state synchronization and transitive source-locking were incomplete. The compute itself remains retained.

## Startup route

On `stage32ex5-mainbatch`:

1. synchronize current Stage32 authority;
2. replay the retained BC2-25 verifier and its transitive executable source locks;
3. preserve all `16` retained UNKNOWN parents and `172` uninferred identities as UNKNOWN;
4. require exact-head CI PASS and re-run `stage32ex5-audit` on #1776;
5. do not start BC2-26 before hostile-audit PASS.

BC2-26 is blocked until BC2-25 hostile-audit PASS. No heavy scale-out, merge, Stage32 MAIN/N350 promotion, theorem, receiver, effectivity, endpoint, or Perfect Cuboid credit is authorized.
