# Stage32EX5 MAINBATCH operations

This operational contract grants no mathematical, FULL178, Stage32 MAIN, N350, receiver, theorem, endpoint, effectivity, or Perfect Cuboid credit. PR #1776 remains active/open/draft/unmerged; merge is not authorized.

Ordinary `stage32ex5-mainbatch` first resolves the live Stage32 MAIN coordination PR and its `CROSS-LANE-DEMANDS.json`. The retained live coordination snapshot is MAIN PR #1800 at `9d4a24ef479d031e9c4b85001fe8f7a10198b17d`; zero OPEN EX5 producer demands are recorded and `mainbatch_stop_gate=NONE` permits bounded local EX5 research to continue. Any newer conflicting live coordination result preempts this retained snapshot.

BC2-39 hostile audit PASS is exact head `4b974550d9ad030973fec99e19a090f6785f8aa8`, review `5193423203`. Mainbatch consumes only the bounded EX5 result: audited known-parent UNSAT lower bound `7313`, with exactly 23 remaining UNKNOWN parents committed by hash `29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02`.

The active live state is V33: `STAGE32EX5_MAIN_COMPACT_STATE_V33_BC2_39_AUDIT_CONSUMED_BC2_40_PREFLIGHT`. BC2-40 preflight targets exactly those 23 hostile-audited UNKNOWN parents at `180000 ms` per parent. Its retained producer and preflight identities are source-locked by `MAIN-STATE.json` and `verify_main_state.py`.

BC2-40 heavy execution is currently **not authorized**. `dedicated_runkey=null`, `effective_heavy_concurrency=0`, `runkey_armed=false`, and heavy scaleout is false. The next gate is `BC2_40_FRESH_RUNKEY_AUTHORIZATION`. Before any heavy execution, mainbatch must create a fresh semantic runkey in the triggering commit range and extend/activate a fail-closed workflow gate that validates the exact audited-23 identity, producer/preflight source locks, `180000 ms` timeout, one-heavy-runner ceiling, and all no-credit/no-merge firewalls. Unrelated PR synchronization is cold and must not start compute.

Once a future authorized BC2-40 execution completes, mainbatch must retain an exact checkpoint plus artifact commitments, consume/disarm the runkey, retire the BC2-40 heavy executor, freeze the new state, and stop at `stage32ex5-audit`. Until such execution occurs, `stage32ex5-audit` is not the active route.

UNKNOWN must remain UNKNOWN. Any SAT result is Picard64-feasibility evidence only and must not be promoted to an actual effective/irreducible curve. No whole-first-block, whole-stratum, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid, heavy scaleout, or merge promotion is authorized.
