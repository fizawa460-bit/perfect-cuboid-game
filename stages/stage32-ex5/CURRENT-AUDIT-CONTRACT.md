# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` remains the historical Cycle1 source-locked contract.

## Audit target

Audit PR #1765 only at the exact frozen BC2-24 merge-checkpoint head. N355 is the latest consumed Stage32 MAIN pruning authority; N356 remains `AUDIT_REQUIRED` and deferred with zero MAIN pruning credit. The e=4 local exact UNSAT prefix is `0..797`.

The retained BC2-24 result must replay exactly: source retained UNKNOWN count 23; new parent UNSAT 4; retained UNKNOWN `19`; SAT 0; branch partition `147 UNSAT / 60 UNKNOWN / 0 SAT`; known parent-UNSAT lower bound `7145`; `172` other BC2-19 UNKNOWN identities uninferred. BC2-24 must not be interpreted as whole-first-block, whole-stratum, or FULL178 closure.

## Required hostile checks

1. Historical Cycle1 authority provenance remains explicit in `MAIN-STATE.json`: `EX5_BREADTH_CYCLE_1`, audited status, `EX5_BREADTH_CYCLE_1_ONLY`, and the early-BC2 claim id are preserved. This repairs the prior `KeyError: breadth_cycle` integrity failure without weakening historical source locks.
2. `verify_main_state.py` replays the BC2-24 canonical checkpoint and source/run-key locks, checks 4/19/0 parent accounting, 147/60/0 branch accounting, 7145 lower bound, and the 172-uninferred firewall.
3. `Stage32EX5 main integrity` passes through the retained historical chain, BC2-12/14/16 exact checkpoints, current EX5 firewalls, Stage32 claim DAG, and active frontier.
4. Repository claim/frontier integrity passes its repo-wide workflow lifecycle verifier. The branch-local BC2-24 automatic workflow must not remain on the merge surface; its successful run provenance is retained in the checkpoint instead.
5. PR #1765 is based on current `main` and is not behind it at the audited head.
6. BC2-25 is not opened on this PR. No new heavy research unit is authorized before merge.
7. UNKNOWN remains UNKNOWN. No Stage32 MAIN/N350/receiver/effectivity/theorem/endpoint/Perfect Cuboid credit is promoted.

## PASS boundary

A PASS authorizes this retained Stage32EX5 checkpoint for merge only because the user explicitly requested merge priority for PR #1765. It does not authorize BC2-25 mathematics or any Stage32 MAIN promotion. If either active integrity gate is red, re-audit fails closed and merge must not proceed.
