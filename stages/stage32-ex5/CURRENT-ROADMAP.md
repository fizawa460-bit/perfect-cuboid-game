# Stage32EX5 current roadmap

This is the mutable current roadmap. `stage32-ex5.md` remains the historical Cycle1 source-locked roadmap.

## Stage32 synchronization

PR #1765 is synchronized onto current `main` `6bad01a45b3c57d8697df79c1790bd2f30af68de`. Stage32 MAIN #1753 is merged. N355 remains the consumed pruning authority; N356 is `AUDIT_REQUIRED`, deferred, and grants zero new MAIN pruning credit. FULL178 remains active/incomplete. The retained e=4 local exact UNSAT prefix is `0..797`.

## Current Stage32EX5 checkpoint

BC2-24 is retained and is the stopping point for this PR. Starting from the BC2-19 `7100 UNSAT / 236 UNKNOWN / 0 SAT` partition of 7336 mod8 parents, BC2-20..23 narrowed a retained slice to 23 UNKNOWN parents. BC2-24's exact fibre-degree partition proves 4 of those UNSAT and leaves `19` retained UNKNOWN, `0` SAT, with known parent-UNSAT lower bound `7145`. The other `172` BC2-19 UNKNOWN identities are deliberately uninferred.

This does not prove the e=8 first block UNSAT, does not close the stratum, and does not close FULL178.

## Merge-first route

1. Repair the historical retained-state schema replay and current BC2-24 state projection.
2. Retire the branch-local BC2-24 automatic workflow from the merge surface; retain its checkpoint, source, run key and GitHub run provenance.
3. Require Stage32EX5 main integrity and repository claim/frontier lifecycle integrity to pass at the exact frozen head.
4. Hostile re-audit that exact head.
5. Merge PR #1765.
6. Only after merge may a fresh PR consider BC2-25.

BC2-25 is therefore deferred. No heavy scale-out, Stage32 MAIN promotion, N350 registration, theorem/effectivity/receiver/endpoint credit, or Perfect Cuboid conclusion is authorized before merge.
