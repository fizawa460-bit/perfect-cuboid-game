# Stage32EX5 — current role in Stage32

Stage32EX5 remains an auxiliary `ATTACKS` lane for Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Ordinary research uses `stage32ex5-mainbatch`; hostile audit uses `stage32ex5-audit`. PR #1776 remains the active work surface.

## Audited BC2-27 predecessor

BC2-27 hostile re-audit **PASS** is exact head `b70bc51909f5ed78641ee3b727a2258382ef950c`, review `5179488973`. The first BC2-27 audit FAIL remains provenance at `43fce7733be95b47b2d2a4e4568300add7694224`, review `5179261378`. Audited bounded credit is 3 new UNSAT parents `[1066,1117,1133]`, known parent-UNSAT lower bound `7155`, with 9 retained UNKNOWN parents, 13 UNKNOWN branches / p33 / p34 / p35 timeout leaves, 0 SAT, and the other `172` BC2-19 UNKNOWN identities uninferred.

## Active BC2-28 bounded route

BC2-28 targets exactly those 13 audited BC2-27 timeout p35 leaves. BC2-24 already proves the second-factor pack `[34,35,38,39,42,43]` has common fibre degree `n2`, so BC2-28 uses exact boundary38 partition `p38=0..floor(n2/2)`, equivalently `n2=2*p38+sum(incident exceptional pairings)`. The retained target has at most `42` p38 checks, timeout 2000 ms per leaf, concurrency 1, and no heavy scaleout.

BC2-29 is blocked until the BC2-28 result is retained and a new hostile-audit boundary is established. No Stage32 MAIN/N350, whole-first-block, whole-stratum, FULL178, theorem, effectivity, receiver, endpoint, Perfect Cuboid, heavy-scaleout, or merge credit is authorized.
