# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order:

1. `AGENTS.md`;
2. `stages/stage32-ex5/README.md`;
3. this file;
4. `stages/stage32-ex5/MAIN-STATE.json`;
5. only `MAIN-STATE.json.current_leaf_working_set`.

Do not preload unrelated Stage32 history, other EX lanes, Research OS, or large retained payloads unless the active leaf explicitly triggers them.

## Current authority

Stage32 remains in `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is the primary incomplete requirement. Observed MAIN PR #1753 head is `0f8cee995e5c982cdb7ceceae14d69f91e65588d`.

The latest retained MAIN checkpoint is N353, RESULT canonical `afd873201ed0deea149c502d681729508face43942df085af91db3e95fbf371b`. N353 is audit-candidate only and grants no MAIN pruning credit. MAIN is freshness-frozen at `98 ahead / 0 behind` from hostile-audited head `b56a832e6c194321916fe4ef63eef0d673b8ff9a` until fresh hostile-audit credit is consumed. N350 remains the separate fail-closed production-registration boundary.

V6/O210/Q602 and `[73,97,235]` are historical/formal provenance only. EX5 does not reopen them.

## Current frontier

The retained local `(g1-d008,e=4)` exact Picard64 UNSAT prefix is **`0..797`**, consisting of six consecutive 133-rank blocks.

BC2-16 exactly closed ranks `665..797`: outer exceptional rank `5`, base terminal `[0,1,0,0,0,0,2,0,0,0,1]`, fixed exceptional mass `4`, residual mass `0`, complete parent count `1`, exact result `1/1 UNSAT`, `UNKNOWN=0`, `SAT=0`.

Evidence canonical: `47278e00902f049e354227f02fe891b199025129a8fd3387a0249ad3b5c5ac9c`.
Checkpoint canonical: `8cfe535fbd486b32e21c9e2cbb7c2289f2880420e5aa4cf3fc98db5f7d310a20`.
Claim-sync canonical: `ddb8841a798ee491fd6322fcb5a25ac7ff64cc33fa1b82d7d5e717e13e3ea4fd`.

The whole stratum is still open. FULL178 is still incomplete. No N350, receiver, effectivity, theorem, endpoint, or Stage32 MAIN credit follows.

## Current unit

`BC2_17_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`.

BC2-17 must rederive the next complete 133-rank exceptional block after rank `797` using source `CompressedTerminalIndexer`, exact rank/unrank round trips, and source `terminal_predicate` replay. Stop at the structural checkpoint; do not assume the next exceptional signature or mass split, and do not invoke a Picard64 solver in this unit.

## Claim-DAG and execution contract

BC2-16 retained consolidation leaves EX5 in role `ATTACKS` on `S32.FULL178.NUMERICAL_CENSUS.V1`. No ACTIVE-FRONTIER remap or MAIN promotion occurred. Required claim-DAG integrity and active-frontier verifiers remain part of the EX5 main workflow.

Each `stage32ex5-mainbatch` executes one bounded unit, retains exact evidence with source locks and firewalls, synchronizes current routing, and stops. Heavy/artifact-producing work requires a dedicated fresh run-key authorization. Historical `stage32-ex5.md` and `AUDIT-CONTRACT.md` are immutable source-locked Cycle1 records.

Do not merge without explicit user authorization. Current working PR #1765 remains a separate audit/merge surface.
