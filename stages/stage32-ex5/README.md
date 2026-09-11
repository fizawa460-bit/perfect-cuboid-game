# Stage32EX5 — current role in Stage32

Stage32EX5 is an auxiliary `ATTACKS` / producer lane for Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Historical `stage32-ex5.md` is the Cycle1 source-locked roadmap and is not rewritten.

Canonical commands and ownership live in `stages/stage32/COMMANDS.md`. Ordinary EX5 research uses `stage32ex5-mainbatch`; `stage32ex5-audit` is used only after a new exact retained checkpoint is frozen.

## Current Stage32 authority observation

N355 remains the latest consumed hostile-audited pruning authority in the current compact Stage32 state: `17,128` strata and `66,462,870,551,188,628,549,910` terminals remain. N356 is retained `AUDIT_REQUIRED` with zero new MAIN pruning credit. V6/O210/Q602 are historical/formal provenance only; `[73,97,235]` is not the current Stage32 survivor population.

EX5 must re-read current `stages/stage32/MAIN-STATE.json` at startup rather than treating this observation as routing authority.

## Merged BC2-24 checkpoint

PR #1765 is merged at `98c5710dad4ca9a006e93b273ecf5259733e03aa`. Its BC2-24 result remains retained evidence:

- e=4 local exact UNSAT prefix `0..797`;
- e=8 first block BC2-19: `7100 UNSAT / 236 UNKNOWN / 0 SAT` among 7336 mod8 parents;
- retained BC2-20..23 slice: 23 UNKNOWN parents;
- BC2-24: 4 newly UNSAT, `19` retained UNKNOWN, `0` SAT;
- known parent-UNSAT lower bound `7145`;
- `172` other BC2-19 UNKNOWN identities remain uninferred.

This is not whole-first-block, whole-stratum, FULL178, N350, theorem, effectivity, receiver, endpoint, or Perfect Cuboid closure.

## Post-merge continuation

The old merge-first stop rule is complete and must not block ordinary startup. A fresh `stage32ex5-mainbatch` invocation starts from current main, synchronizes current Stage32 authority, replays BC2-24 as retained evidence, and may open the bounded `BC2_25_POST_MERGE_UNKNOWN_REFINEMENT_PREFLIGHT` leaf if still useful.

Do not rerun BC2-20..24 and do not broaden into heavy scale-out without a new retained route/authorization. UNKNOWN remains UNKNOWN. EX5 does not self-promote Stage32 MAIN credit.
