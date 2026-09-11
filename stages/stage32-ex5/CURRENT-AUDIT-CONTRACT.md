# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance.

## Consumed predecessor audit

PR #1776 BC2-26 hostile audit **PASS** was granted at exact head `34d6b030095b97c738f6faf6b9045f366622592c`, review `5177919212`. That PASS authorizes only the bounded BC2-27 generation and grants no Stage32 MAIN/FULL178/merge credit.

## New BC2-27 hostile-audit boundary

BC2-27 is frozen on PR #1776. Exact compute head `21828bcf36ea33d1e6c26465eea74c646ba26901`; workflow run `34593864110`; integrity job `103245034147`; compute job `103245141239`; artifact `10262350002`; artifact ZIP digest `e42f8aba7ed0092e770051a732ac9c0733a9681064c7f600c9db3a7d45d6356b`.

Retained checkpoint canonical: `0f9278799809fd1a48c187f9a9668631422ab3136478cb3f9f64fd423df71462`; raw result canonical: `6537cdece0d03e80fb704e9ee8b95de240ec7dc043e872004ca78d4199a08fbd`.

Bounded result: 3 new parent UNSAT `[1066,1117,1133]`; `9` retained UNKNOWN parents; `13` UNKNOWN branches; `13` UNKNOWN p33 subbranches; `13` UNKNOWN p34 leaves; `13` p35 timeout UNKNOWN leaves; 0 SAT; known parent-UNSAT lower bound `7155`. The other `172` BC2-19 UNKNOWN identities remain uninferred.

`stage32ex5-audit` must independently replay checkpoint canonical, exact run/artifact receipt, executed runkey/workflow identities, BC2-26 predecessor checkpoint and hostile-audit receipt, and the transitive executable chain BC2-27 → BC2-26 → BC2-25 → BC2-24 → BC2-18 → `hperp_integral_adapter.py` / `pairing_prefix_engine.py`. UNKNOWN/no-promotion firewalls must remain intact.

BC2-28 is blocked until BC2-27 hostile-audit PASS. Merge authorization remains false and independent. No whole-first-block, whole-stratum, FULL178, N350, Stage32 MAIN, theorem, effectivity, receiver, endpoint, Perfect Cuboid, or heavy-scaleout credit follows from BC2-27.
