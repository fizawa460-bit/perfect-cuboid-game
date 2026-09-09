# stage32ex5-c

Role: independent end-to-end bridge construction for `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`.

Startup:
1. `AGENTS.md`
2. `stages/stage32-ex5/MAIN-START-HERE.md`
3. `stages/stage32-ex5/MAIN-STATE.json`
4. `stages/stage32-ex5/parallel/BC2-01B-LANES.json`
5. this file
6. only directly required BC2/source/runtime paths

Task: independently attempt a complete exact map from runtime exceptional indices `0..47` to projective singular-node coordinates. Do not wait for A/B conclusions; use the audited BC2 checkpoint and exact repository/source evidence to derive an end-to-end candidate bridge.

Acceptance target: 48 runtime indices, 48 exact projective nodes, injective and surjective correspondence after the declared projective canonicalization, deterministic replay, and no hidden dependence on incidental runtime enumeration order.

Required deliverable: candidate mapping representation, verifier or exact replay procedure, collision/missing-index report, assumptions ledger, and a PASS/BLOCKED result scoped only to this bridge.

Do not promote scratch output to EX5 or Stage32 authority. Do not edit `MAIN-STATE.json`/claim/frontier files. No FULL178 span replay.