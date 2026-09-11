# Stage32EX5 — current role in Stage32

Stage32EX5 is an auxiliary `ATTACKS` / producer lane for Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Historical `stage32-ex5.md` remains source-locked provenance.

Canonical commands and ownership live in `stages/stage32/COMMANDS.md`. Ordinary research uses `stage32ex5-mainbatch`; `stage32ex5-audit` audits a frozen exact checkpoint.

## Audited predecessor BC2-25

PR #1776 BC2-25 hostile re-audit PASS is exact head `1d2e04486e170336ce02af144aabb08e4a80a31d`, review `5177354131`. It established 3 new parent UNSAT, leaving 16 parent UNKNOWN / 36 branch UNKNOWN / 38 p33-subbranch UNKNOWN, 0 SAT, and known parent-UNSAT lower bound `7148`. The other `172` BC2-19 UNKNOWN identities remain uninferred.

## Active BC2-26 retained audit boundary

BC2-26 executed the bounded exact boundary34 partition over those 38 p33 UNKNOWN subbranches, maximum 110 p34 leaves. It proves 4 additional parents `[1106,1119,1218,1224]` exact UNSAT and leaves `12` retained UNKNOWN parents, `20` UNKNOWN branches, `20` UNKNOWN p33 subbranches and `23` UNKNOWN p34 leaves, with 0 SAT. The known parent-UNSAT lower bound is now `7152`; all `172` unrelated identities remain uninferred.

BC2-26 checkpoint canonical is `b97d61c0d20cec1742831a07595429024cb9bb272d383cfb98d968278d8d330a`. The compute run was `34588771756` at exact compute head `7d5c35057b480ebe6bf3b0cdf047c0d7bdfde18f`.

This is a new hostile-audit boundary. BC2-27 is blocked until BC2-26 hostile-audit PASS. No whole-first-block, whole-stratum, FULL178, N350, Stage32 MAIN, theorem, effectivity, receiver, endpoint, Perfect Cuboid, heavy-scaleout, or merge credit is authorized.
