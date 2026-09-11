# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain source-locked provenance.

## Consumed predecessor audit

PR #1776 BC2-25 hostile re-audit **PASS** was granted at exact head `1d2e04486e170336ce02af144aabb08e4a80a31d`, review `5177354131`. The prior FAIL at `9bbc491cfde0f8a7f48d9742dad8ff368e4837b2`, review `5176133548`, remains provenance. BC2-25 credit stops at known parent-UNSAT lower bound 7148 with 16 retained UNKNOWN parents; it grants no Stage32 MAIN/FULL178/merge credit.

## New BC2-26 hostile-audit boundary

BC2-26 has executed and is frozen on PR #1776. Exact compute head: `7d5c35057b480ebe6bf3b0cdf047c0d7bdfde18f`; workflow run `34588771756`; compute job `103229111936`; artifact `10194988584`; artifact ZIP digest `6844041386ce9ebf198e2dd7c88c545bca8ce524a9f2659e7f81351b2aa23465`.

Retained checkpoint canonical: `b97d61c0d20cec1742831a07595429024cb9bb272d383cfb98d968278d8d330a`; raw result canonical: `f61f60804829c63b2090b42e142824411120f4d1a80d04ea323e04127e94e831`.

The bounded result is: 4 new parent UNSAT `[1106,1119,1218,1224]`; `12` retained UNKNOWN parents; `20` UNKNOWN branches; `20` UNKNOWN p33 subbranches; `23` UNKNOWN p34 leaves; 0 SAT; known parent-UNSAT lower bound `7152`. The other `172` BC2-19 UNKNOWN identities remain uninferred.

`stage32ex5-audit` must independently verify checkpoint canonical replay, the exact run/artifact receipt, the executed runkey identity, the executed workflow identity, predecessor BC2-25 lock, and the transitive executable chain through BC2-25 → BC2-24 → BC2-18 → `hperp_integral_adapter.py` / `pairing_prefix_engine.py`. UNKNOWN/no-promotion firewalls must remain intact.

BC2-27 is blocked until BC2-26 hostile-audit PASS. Merge authorization remains independent and false. No whole-first-block, whole-stratum, FULL178, N350, Stage32 MAIN, theorem, effectivity, receiver, endpoint, Perfect Cuboid, or heavy-scaleout credit follows from BC2-26.
