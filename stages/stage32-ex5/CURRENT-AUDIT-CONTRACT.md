# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance.

## Consumed predecessor audit

PR #1776 BC2-26 hostile audit **PASS** was granted at exact head `34d6b030095b97c738f6faf6b9045f366622592c`, review `5177919212`. That PASS authorizes only the bounded BC2-27 generation and grants no Stage32 MAIN/FULL178/merge credit.

## BC2-27 retained boundary

BC2-27 is frozen on PR #1776. Exact compute head `21828bcf36ea33d1e6c26465eea74c646ba26901`; workflow run `34593864110`; integrity job `103245034147`; compute job `103245141239`; artifact `10262350002`; artifact ZIP digest `e42f8aba7ed0092e770051a732ac9c0733a9681064c7f600c9db3a7d45d6356b`.

Retained checkpoint canonical: `0f9278799809fd1a48c187f9a9668631422ab3136478cb3f9f64fd423df71462`; raw result canonical: `6537cdece0d03e80fb704e9ee8b95de240ec7dc043e872004ca78d4199a08fbd`.

Bounded result: 3 new parent UNSAT `[1066,1117,1133]`; `9` retained UNKNOWN parents; `13` UNKNOWN branches; `13` UNKNOWN p33 subbranches; `13` UNKNOWN p34 leaves; `13` p35 timeout UNKNOWN leaves; 0 SAT; known parent-UNSAT lower bound `7155`. The other `172` BC2-19 UNKNOWN identities remain uninferred.

## Latest hostile audit and required repair

The first BC2-27 hostile audit **FAIL** was recorded at exact head `43fce7733be95b47b2d2a4e4568300add7694224`, review `5179261378`. The computation, artifact receipt, target identity, boundary35 partition, retained accounting, transitive source-lock chain, and exact-head CI were accepted before two authority defects were found:

1. `MAIN-STATE.json` misspelled the mandatory `perfect_cuboid_existence_claim=false` firewall as `perfect_curboid_existence_claim`.
2. `claim_sync.existing_active_goal` used the non-authoritative claim ID `S32.FULL178.NUMERICAL.CENSUS.V1` instead of `S32.FULL178.NUMERICAL_CENSUS.V1`.

The repaired state must retain the exact canonical Perfect Cuboid existence/nonexistence firewall names and must source-check the FULL178 claim ID against the source-locked Stage32 MAIN authority projection. The source-locked Stage32 MAIN state blob is `9981889309c833a1834eaadddce73e52c0aa0176`, whose `current_exact_frontier.full178_goal_claim_id` is `S32.FULL178.NUMERICAL_CENSUS.V1`.

`stage32ex5-audit` must independently replay checkpoint canonical, exact run/artifact receipt, executed runkey/workflow identities, BC2-26 predecessor checkpoint and hostile-audit receipt, the transitive executable chain BC2-27 → BC2-26 → BC2-25 → BC2-24 → BC2-18 → `hperp_integral_adapter.py` / `pairing_prefix_engine.py`, and the repaired authority/firewall checks above. UNKNOWN/no-promotion firewalls must remain intact.

BC2-28 is blocked until a fresh BC2-27 hostile-audit PASS on the repaired exact head. Merge authorization remains false and independent. No whole-first-block, whole-stratum, FULL178, N350, Stage32 MAIN, theorem, effectivity, receiver, endpoint, Perfect Cuboid, or heavy-scaleout credit follows from BC2-27.
