# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` remains historical source-locked provenance.

## Consumed BC2-25 audit

PR #1776 BC2-25 hostile re-audit **PASS** was granted at exact head `1d2e04486e170336ce02af144aabb08e4a80a31d`, review `5177354131`. The prior FAIL at `9bbc491cfde0f8a7f48d9742dad8ff368e4837b2`, review `5176133548`, remains retained provenance.

The PASS covers the bounded BC2-25 result: 3 new parent UNSAT / 16 UNKNOWN / 0 SAT; 24/36/0 branch UNSAT/UNKNOWN/SAT; 128/38/0 p33-subbranch UNSAT/UNKNOWN/SAT; known parent-UNSAT lower bound `7148`; the other `172` BC2-19 UNKNOWN identities remain uninferred. It grants no Stage32 MAIN, FULL178, N350, theorem, effectivity, receiver, endpoint, Perfect Cuboid, or merge credit.

Merge-ready freshness at PASS was PENDING because current main `c31684fb5f63d8a025eb298c91861d4c979b0e28` was two reviewed non-load-bearing commits ahead. Merge remains separately unauthorized.

## BC2-26 execution boundary

The consumed PASS authorizes only the bounded BC2-26 exact partition over the 38 audited residual p33 UNKNOWN subbranches on 16 parents / 36 branches. Partition by label 34 with `p34=0..floor(n2/2)` and `n2=2*p34+sum(incident exceptional pairings)`. Maximum `110` p34 leaves, concurrency 1; `172` other identities remain uninferred.

After BC2-26 output is frozen into a retained checkpoint, a **new audit boundary exists** and `stage32ex5-audit` must run before BC2-27. The new verifier must lock the BC2-26 source plus the full retained executable chain. Merge authorization remains independent and false.
