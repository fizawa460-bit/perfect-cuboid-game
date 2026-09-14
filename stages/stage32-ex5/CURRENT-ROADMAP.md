# Stage32EX5 current roadmap

PR #1776 remains open/draft/unmerged. Merge is not authorized. This roadmap is operational and does not override Stage32 MAIN authority.

## Live authority

BC2-39 hostile audit is **PASS** at exact head `4b974550d9ad030973fec99e19a090f6785f8aa8`, review `5193423203`: exactly `7 UNSAT / 23 UNKNOWN / 0 SAT`, so the audited EX5 mathematical lower bound is `7313`. The 23 UNKNOWN hash is `29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02`.

The live `MAIN-STATE.json` intentionally remains the hostile-audited V32 compatibility boundary. A direct V33 activation was rejected by existing historical-schema / synchronized-MAIN integrity gates, so no live-state consumption marker is retained. This preserves fail-closed Research OS behavior.

## Staged next unit: BC2-40

A source-locked bounded producer and preflight are staged for exactly the 23 audited UNKNOWN parents. Timeout is `180000 ms / parent`, intended heavy concurrency is one, scaleout is forbidden, and no runkey is armed. The preflight status is `PREFLIGHT_STAGED_LIVE_AUTHORITY_NOT_ACTIVATED`.

The next exact unit is therefore **not heavy execution**. First extend and verify the live EX5 schema migration so historical EX5 replay, Stage32 synchronized MAIN authority, claim frontier, and startup authority all accept the new state. Only after that migration is green may a fresh semantic BC2-40 runkey be armed.

No whole-first-block, whole-stratum, FULL178, Stage32 MAIN/N350, effectivity/actual-curve, receiver, theorem, endpoint, Perfect Cuboid, or merge credit. No merge.
