# Stage32EX5 MAIN startup

Ordinary `stage32ex5-mainbatch` reads, in order:

1. `AGENTS.md`;
2. `stages/stage32-ex5/README.md`;
3. this file;
4. `stages/stage32-ex5/MAIN-STATE.json`;
5. only `MAIN-STATE.json.current_leaf_working_set`.

Do not preload unrelated Stage32 history, other EX lanes, Research OS, or large retained payloads unless the active leaf explicitly triggers them.

## Current authority

Stage32 remains in `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` is the primary incomplete requirement. Observed MAIN PR #1753 head is `c2c1041298ae34a593fcb48d04c0e0a20dc9c37a`.

MAIN has progressed through N353. N353 hostile audit PASS is consumed at review `5163144778`, exact head `0f8cee995e5c982cdb7ceceae14d69f91e65588d`. The current MAIN stop gate is N354 hostile audit: N354 RESULT canonical `9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4`, candidate head `ab0ce28876dbba306985343c104b02b69cec89fb`, handoff canonical `350afe8c3fbda418a888feff4e8c8233acc44b6472e825cf9d758c22d69065f6`. N354 is `AUDIT_REQUIRED` and grants no MAIN pruning credit yet.

Freshness is reset to the audited N353 head; current MAIN distance is `9 ahead / 0 behind`, so there is no freshness freeze. N350 remains the separate fail-closed production-registration boundary.

V6/O210/Q602 and `[73,97,235]` are historical/formal provenance only. EX5 does not reopen them.

## Current frontier

The retained local `(g1-d008,e=4)` exact Picard64 UNSAT prefix is **`0..797`**, consisting of six consecutive 133-rank blocks.

BC2-16 exactly closed ranks `665..797`: outer exceptional rank `5`, base terminal `[0,1,0,0,0,0,2,0,0,0,1]`, fixed exceptional mass `4`, residual mass `0`, complete parent count `1`, exact result `1/1 UNSAT`, `UNKNOWN=0`, `SAT=0`.

Evidence canonical: `47278e00902f049e354227f02fe891b199025129a8fd3387a0249ad3b5c5ac9c`.
Checkpoint canonical: `8cfe535fbd486b32e21c9e2cbb7c2289f2880420e5aa4cf3fc98db5f7d310a20`.
Claim-sync canonical: `ddb8841a798ee491fd6322fcb5a25ac7ff64cc33fa1b82d7d5e717e13e3ea4fd`.

The whole stratum is still open. FULL178 is still incomplete. No N350, receiver, effectivity, theorem, endpoint, or Stage32 MAIN credit follows from EX5.

## Current unit

`BC2_17_NEXT_EXCEPTIONAL_TERMINAL_BLOCK_PREFLIGHT`.

BC2-17 must rederive the next complete 133-rank exceptional block after rank `797` using source `CompressedTerminalIndexer`, exact rank/unrank round trips, and source `terminal_predicate` replay. Stop at the structural checkpoint; do not assume the next exceptional signature or mass split, and do not invoke a Picard64 solver in this unit.

## Claim-DAG and execution contract

BC2-16 retained consolidation leaves EX5 in role `ATTACKS` on `S32.FULL178.NUMERICAL_CENSUS.V1`. No ACTIVE-FRONTIER remap or MAIN promotion occurred. Required claim-DAG integrity and active-frontier verifiers remain part of the EX5 main workflow.

Each `stage32ex5-mainbatch` executes one bounded unit, retains exact evidence with source locks and firewalls, synchronizes current routing, and stops. Heavy/artifact-producing work requires a dedicated fresh run-key authorization. Historical `stage32-ex5.md` and `AUDIT-CONTRACT.md` are immutable source-locked Cycle1 records.

Do not merge without explicit user authorization. Current working PR #1765 remains a separate audit/merge surface.
