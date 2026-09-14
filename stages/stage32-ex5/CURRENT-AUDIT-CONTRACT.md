# Stage32EX5 current hostile-audit contract

PR #1776 remains open/draft/unmerged. Merge is not authorized.

## Consumed predecessor boundary

BC2-38 hostile re-audit **PASS** is consumed from exact head `5e1d07e4c92fbecff9bfa89b0bfb65cdaf564a71`, review `5190676180`.

The audited retained BC2-38 result is:

- exact target: 34 previously audited UNKNOWN parents;
- result: `4 UNSAT / 30 UNKNOWN / 0 SAT`;
- new UNSAT IDs: `[1014,1133,1910,2817]`;
- remaining UNKNOWN hash: `d60d873c4fc66ebb6cda0530d4137e5fd195fe1b601b0a21e91f873c1df28fb7`;
- checkpoint blob: `91eca02054cd2dbf702dd4a7635398ef76ee832f`;
- checkpoint canonical: `88b41680df6bb78f8b7f8ca00cde121d909a39e7b3c29eef765edb77b2c022ba`;
- retained audited verifier blob: `934f19363549d652c18b02934c1f963a19204664`;
- audited known-parent UNSAT lower bound: `7306`.

The current EX5 state must preserve that BC2-38 is audited and consumed locally, with no Stage32 MAIN/FULL178/effectivity/receiver/theorem/endpoint/Perfect Cuboid/merge promotion.

## Active execution boundary: BC2-39

BC2-39 may execute exactly once from a fresh generation-1 runkey against the exact BC2-38 remaining 30 UNKNOWN set. The producer blob is `e322029cfc4476ce8cf3685ca04f35b58e2ce9f2`; preflight blob `e3dab72865d734f2420fb71ddf3c29115f9df68e`, canonical `7bda94c5869c988892c979873f13a1c311debedbbe9fcc670a253e339fb5e435`.

Execution is bounded to one runner, `160000 ms` per parent, no scaleout, compact artifact only, two-day retention. The runkey must be newly advanced in the triggering `before..head` commit range; unrelated synchronization must not authorize compute.

The live MAIN coordination source is PR #1800 head `9d4a24ef479d031e9c4b85001fe8f7a10198b17d`, retained in `LIVE-MAIN-COORDINATION-SYNC-20260914.json`. It records zero OPEN EX5 producer demands and `mainbatch_stop_gate=NONE`. This routing synchronization is not mathematical credit.

## Next hostile audit

After BC2-39 executes, mainbatch must retain the exact artifact/result commitments, consume/disarm the runkey, remove the active BC2-39 heavy path, and freeze the state with `new_audit_boundary_exists=true`, `re_audit_required=true`, and BC2-40 blocked.

`stage32ex5-audit` must then independently verify the exact 30-parent target identity, solver/result partition, UNKNOWN preservation, SAT witness semantics if any, artifact/raw commitments, source locks, fresh-runkey authorization, heavy-path retirement, current MAIN/cross-lane synchronization, and all broad-credit firewalls.

A PASS may only advance bounded EX5-local audited progress. It does not automatically grant whole-block, whole-stratum, FULL178, Stage32 MAIN/N350, effectivity, receiver, theorem, endpoint, Perfect Cuboid, or merge credit.
