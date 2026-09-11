# Stage32EX5 — current role in Stage32

Stage32EX5 remains an auxiliary `ATTACKS` lane for Stage32 `FULL178_AND_FINAL_MILESTONE_CHAIN`; `32-01 FULL178` remains primary/incomplete. Ordinary research uses `stage32ex5-mainbatch`; hostile audit uses `stage32ex5-audit`. PR #1776 remains active. BC2-29 hostile audit **PASS** is exact head `ca8e0ea7209b898d24d5f647dcce11be1aff03b2`, review `5183342658`.

BC2-30 boundary42 executed exactly once at compute head `53be207f91cfd6b13ee8533efcf0af64bdccf3d6`, workflow `34647160641`, compute job `103420643305`, artifact `10283165917`. All four p42 leaves are UNSAT: `4 UNSAT / 0 UNKNOWN / 0 SAT`; parent `1064` is newly UNSAT. The retained BC2-25..30 path therefore has **retained UNKNOWN=0** and the known parent-UNSAT lower bound is `7164`.

This does **not** close the whole first block: the separate `172` BC2-19 UNKNOWN identities remain uninferred. The BC2-30 runkey is consumed/disarmed, the one-shot executor is removed, and the retained checkpoint/verifier are source-locked to the exact compute/artifact receipt. BC2-31 is blocked until a fresh `stage32ex5-audit` PASS. No Stage32 MAIN/N350, whole-first-block, whole-stratum, FULL178, theorem, effectivity, receiver, endpoint, Perfect Cuboid, heavy-scaleout, or merge credit is authorized.
