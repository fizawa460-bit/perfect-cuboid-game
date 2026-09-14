# Stage32EX5 MAINBATCH operations

This operational contract grants no mathematical, FULL178, Stage32 MAIN, N350, receiver, theorem, endpoint, effectivity, or Perfect Cuboid credit. PR #1776 remains active/open/draft/unmerged; merge is not authorized.

Ordinary `stage32ex5-mainbatch` first resolves the live Stage32 MAIN coordination PR and its `CROSS-LANE-DEMANDS.json`. Current live coordination is MAIN PR #1800 at `9d4a24ef479d031e9c4b85001fe8f7a10198b17d`; zero OPEN EX5 producer demands are recorded and `mainbatch_stop_gate=NONE` permits bounded FULL178/final-chain research to resume.

BC2-38 hostile re-audit **PASS** is exact head `5e1d07e4c92fbecff9bfa89b0bfb65cdaf564a71`, review `5190676180`. Mainbatch consumes only the bounded EX5 result: audited known-parent UNSAT lower bound `7306`, with exactly 30 remaining UNKNOWN parents committed by hash `d60d873c4fc66ebb6cda0530d4137e5fd195fe1b601b0a21e91f873c1df28fb7`.

The active local leaf is BC2-39. It may replay exactly those 30 audited UNKNOWN parents at `160000 ms` per parent with one heavy runner. Heavy scaleout is not authorized. The dedicated runkey must advance freshly in the triggering commit range; unrelated PR synchronization is cold. Persist only the compact verified result artifact, at most 524288 bytes, retention 2 days.

After BC2-39 executes, mainbatch must retain its exact checkpoint and artifact commitments, consume/disarm the runkey, retire the BC2-39 heavy executor, freeze the state, and stop at `stage32ex5-audit`. BC2-40 is blocked until that hostile audit passes.

UNKNOWN must remain UNKNOWN. Any SAT result is Picard64-feasibility evidence only and must not be promoted to an actual effective/irreducible curve. No whole-first-block, whole-stratum, FULL178, Stage32 MAIN/N350, theorem/effectivity/receiver/endpoint/Perfect Cuboid, or merge promotion is authorized.
