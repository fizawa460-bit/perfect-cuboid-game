# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads `AGENTS.md`, `stages/stage32/COMMANDS.md`, current `stages/stage32/MAIN-STATE.json`, then this EX5 startup/operations/state surface. Historical Cycle1 files remain source-locked provenance.

## Active work surface

PR #1776 is the active EX5 work/audit surface. BC2-25 is hostile-audited PASS at exact head `1d2e04486e170336ce02af144aabb08e4a80a31d`, review `5177354131`.

BC2-26 has now been executed and frozen. It adds 4 exact-UNSAT parents `[1106,1119,1218,1224]`, advances the known parent-UNSAT lower bound to `7152`, and leaves `12` retained UNKNOWN parents, `20` UNKNOWN branches, `20` UNKNOWN p33 subbranches and `23` UNKNOWN p34 leaves, with 0 SAT. The other `172` BC2-19 UNKNOWN identities remain uninferred.

Checkpoint canonical: `b97d61c0d20cec1742831a07595429024cb9bb272d383cfb98d968278d8d330a`. Compute run: `34588771756`; exact compute head: `7d5c35057b480ebe6bf3b0cdf047c0d7bdfde18f`.

## Startup route

On `stage32ex5-mainbatch`, replay the retained BC2-25 and BC2-26 verifiers, preserve every UNKNOWN and the `172` uninferred identities, and maintain the frozen BC2-26 hostile-audit boundary. BC2-27 is blocked until `stage32ex5-audit` grants PASS on BC2-26.

No broad/heavy scale-out, merge, Stage32 MAIN/N350 promotion, FULL178 closure, theorem, receiver, effectivity, endpoint, or Perfect Cuboid credit is authorized.
