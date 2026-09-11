# Stage32EX5 current roadmap

This is the mutable current roadmap. `stage32-ex5.md` remains the historical Cycle1 source-locked roadmap.

## Stage32 synchronization

PR #1765 is merged into main at `98c5710dad4ca9a006e93b273ecf5259733e03aa`. N355 remains the latest consumed pruning authority recorded by current Stage32 compact state; N356 remains retained `AUDIT_REQUIRED` with zero new MAIN pruning credit. FULL178 remains active/incomplete. The retained e=4 local exact UNSAT prefix is `0..797`.

At each new EX5 batch, current Stage32 routing must be re-read from `stages/stage32/MAIN-STATE.json`; this roadmap does not override it.

## Current retained checkpoint

BC2-24 is merged retained evidence. Starting from the BC2-19 `7100 UNSAT / 236 UNKNOWN / 0 SAT` partition of 7336 mod8 parents, BC2-20..23 narrowed a retained slice to 23 UNKNOWN parents. BC2-24's exact fibre-degree partition proves 4 of those UNSAT and leaves `19` retained UNKNOWN, `0` SAT, with known parent-UNSAT lower bound `7145`. The other `172` BC2-19 UNKNOWN identities are deliberately uninferred.

This does not prove the e=8 first block UNSAT, does not close the stratum, and does not close FULL178.

## Post-merge route

1. Synchronize current main, `stages/stage32/COMMANDS.md`, and current Stage32 `MAIN-STATE.json`.
2. Replay the retained BC2-24 checkpoint and UNKNOWN firewalls.
3. Search for already-retained MAIN/178/EX5 results that dominate or duplicate the next idea.
4. If still live, open `BC2_25_POST_MERGE_UNKNOWN_REFINEMENT_PREFLIGHT` as the smallest bounded next unit.
5. Freeze a coherent checkpoint before hostile audit or any larger scale-out.

No automatic heavy scale-out, Stage32 MAIN promotion, N350 registration, theorem/effectivity/receiver/endpoint credit, or Perfect Cuboid conclusion is authorized by this roadmap.
