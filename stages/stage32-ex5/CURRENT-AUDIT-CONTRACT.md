# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance. PR #1776 remains open/draft/unmerged.

## Predecessor authority

BC2-32 hostile audit **PASS** is the direct predecessor authority: exact head `5c68ed03d77d6443c54340c90d457e80441fe414`, review `5185434136`. It certified `63 UNSAT / 107 UNKNOWN / 0 SAT` from the audited BC2-31 170-UNKNOWN target, with known parent-UNSAT lower bound `7229`. The 107 current UNKNOWN identities are explicit and hash to `e617578c83e604866c22de5d38d62d93fe4453886b0d46ddce609bce87308492`.

## BC2-33 execution recovery

BC2-33 remains bounded to exactly those 107 audited UNKNOWN parents, `40000 ms` per parent, one heavy runner, effective concurrency 1, no scaleout. Generation 1 at head `75760777934825de9851811c708871412d99ab0e` passed its semantic runkey gate, but workflow `34681403712` compute job `103520625439` was cancelled by the stale-head sweeper during solver execution. Validation and artifact upload were skipped. Therefore generation 1 has no retained solver result and no mathematical credit.

The runkey records that cancelled generation-1 receipt with `accepted_for_mathematical_credit=false` and is disarmed. The active gate is generation-2-only. A generation-2 run may start only after the repaired exact cold head passes EX5 main integrity, Stage32 claim-frontier integrity, and stale-run sweeper, followed by a fresh runkey advance from generation 1 to generation 2.

## Execution and retention obligations

Every successful result must partition exactly 107 audited targets into UNSAT / UNKNOWN / SAT. Every remaining UNKNOWN identity must be retained explicitly; timeout UNKNOWN may not be relabelled UNSAT. Any SAT result is only a Picard64 feasibility witness and must retain its coordinates/pairings without actual-curve or effectivity promotion. The known parent-UNSAT lower bound may increase only by newly exact UNSAT parents from a completed authorized run.

After successful generation-2 compute, mainbatch must retain the compact artifact and exact workflow/job/artifact receipt, disarm/consume the runkey, remove the BC2-33 heavy execution path, install a fail-closed retained verifier/state projection, freeze a new BC2-33 hostile-audit boundary, and stop for `stage32ex5-audit`. BC2-34 is blocked until that audit returns PASS.

The following remain false: whole-first-block authoritative UNSAT, whole-stratum closure, FULL178 completion, Stage32 MAIN pruning credit, N350 registration, effectivity/actual-curve credit, theorem/endpoint credit, Perfect Cuboid existence/nonexistence claim, heavy scaleout, and merge authorization.
