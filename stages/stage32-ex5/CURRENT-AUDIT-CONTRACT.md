# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance. PR #1776 remains open/draft/unmerged.

## Predecessor authority

BC2-32 hostile audit **PASS** is the direct predecessor authority: exact head `5c68ed03d77d6443c54340c90d457e80441fe414`, review `5185434136`. It certified the targeted replay of the hostile-audited BC2-31 170-UNKNOWN set: `63 UNSAT / 107 UNKNOWN / 0 SAT`, known parent-UNSAT lower bound `7229`. The 107 current UNKNOWN identities are explicit and hash to `e617578c83e604866c22de5d38d62d93fe4453886b0d46ddce609bce87308492`. The rejected historical 172-identity reconstruction remains rejected and must not be revived.

## BC2-33 bounded execution authority

BC2-33 may replay exactly those hostile-audited 107 UNKNOWN parent identities with a 40,000 ms per-parent limit, one heavy runner, effective heavy concurrency 1, and no heavy scaleout. It must use `bc2_33_replay_explicit_fresh_unknown107.py`, preflight `bc2-33-fresh-unknown107-replay-preflight.json`, and the generation-gated runkey `runkeys/bc2-33-fresh-unknown107-replay.json`.

The cold runkey is not execution authority. BC2-33 compute may start only after the exact cold head passes EX5 main integrity, Stage32 claim-frontier integrity, and stale-run sweeper, followed by a fresh semantic runkey generation advance. The runkey gate must source-lock the producer/preflight and consume the BC2-32 PASS receipt above.

## Execution and retention obligations

Every result must partition exactly 107 audited targets into UNSAT / UNKNOWN / SAT. Every remaining UNKNOWN identity must be retained explicitly; timeout UNKNOWN may not be relabelled UNSAT. Any SAT result is only a Picard64 feasibility witness and must retain its coordinates/pairings without actual-curve or effectivity promotion. The known parent-UNSAT lower bound may increase only by newly exact UNSAT parents from the audited 107-target set.

After successful compute, mainbatch must retain the compact artifact and exact workflow/job/artifact receipt, disarm/consume the runkey, remove the BC2-33 heavy execution path, install a fail-closed retained verifier/state projection, freeze a new BC2-33 hostile-audit boundary, and stop for `stage32ex5-audit`. BC2-34 is blocked until that audit returns PASS.

The following remain false: whole-first-block authoritative UNSAT, whole-stratum closure, FULL178 completion, Stage32 MAIN pruning credit, N350 registration, effectivity/actual-curve credit, theorem/endpoint credit, Perfect Cuboid existence/nonexistence claim, heavy scaleout, and merge authorization.
