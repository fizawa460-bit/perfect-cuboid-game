# Stage32EX5 current roadmap

PR #1776 remains open/draft/unmerged. Merge is not authorized. This roadmap is operational and does not override Stage32 MAIN authority.

## Live MAIN / cross-lane synchronization

The live MAIN coordination PR is #1800 at exact head `9d4a24ef479d031e9c4b85001fe8f7a10198b17d`. Its V24 authority has `mainbatch_stop_gate=NONE`; bounded FULL178/final-chain research may resume. The reviewed V24 mathematical boundary is `3c5915dee248660a2821f2ebe9c24e20b0ad1647`, hostile-audit review `5191916561`.

Current MAIN authority projection remains **17,128 strata** and **26,876,434,389,242,951,089,388 certified remaining-terminal upper bound**, with semantics `CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET`. FULL178 remains incomplete.

The live cross-lane registry has zero OPEN EX5 producer demands. CUT192 and HPADJ FULL178→Picard64 demands remain SATISFIED. Existing terminal→Picard64 handoff work must not be reopened.

## BC2-38 consumed

BC2-38 hostile re-audit is **PASS** at exact head `5e1d07e4c92fbecff9bfa89b0bfb65cdaf564a71`, review `5190676180`. The exact retained result is `4 UNSAT / 30 UNKNOWN / 0 SAT`; therefore the bounded EX5 audited known-parent UNSAT lower bound advances from `7302` to `7306`.

The exact remaining UNKNOWN set is `[1048,1050,1056,1103,1206,1216,1218,1243,1251,1703,1706,1717,1719,1733,1798,2092,2122,2187,2407,2634,2651,2819,3205,3375,3635,3885,3901,3915,3980,4200]`, hash `d60d873c4fc66ebb6cda0530d4137e5fd195fe1b601b0a21e91f873c1df28fb7`.

This is EX5-local audited progress only. It grants no Stage32 MAIN pruning, whole-block/whole-stratum, FULL178, effectivity, receiver, theorem, endpoint, Perfect Cuboid, or merge credit.

## Active leaf: BC2-39

BC2-39 targets exactly the audited remaining 30 UNKNOWN parents. The retained producer is `breadth-cycle-2/bc2_39_replay_explicit_fresh_unknown30.py`; preflight canonical is `7bda94c5869c988892c979873f13a1c311debedbbe9fcc670a253e339fb5e435`.

Execution contract:

- one heavy runner only;
- `160000 ms` per parent;
- no heavy scaleout;
- compact result artifact only, retention 2 days;
- dedicated runkey `runkeys/bc2-39-fresh-unknown30-replay.json` must advance freshly to generation 1 in the triggering commit range;
- UNKNOWN remains UNKNOWN and SAT, if any, is only Picard64-feasibility evidence, not curve existence.

After BC2-39 executes, freeze its exact result and require `stage32ex5-audit` before BC2-40 or any credit promotion.

No merge.
