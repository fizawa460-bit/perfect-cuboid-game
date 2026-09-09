# stage32ex5-a

Role: source-side reconstruction for `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`.

Startup:
1. `AGENTS.md`
2. `stages/stage32-ex5/MAIN-START-HERE.md`
3. `stages/stage32-ex5/MAIN-STATE.json`
4. `stages/stage32-ex5/parallel/BC2-01B-LANES.json`
5. this file
6. only source/leaf paths directly required by the task

Task: reconstruct the exact BTVA-side 48 singular-node target used by the audited BC2 route. Pin the projective coordinate convention, labeling convention, equivalence under projective scaling/sign, and any permutation/action convention. Distinguish statements proved by the external source from repository-side adapters or inference.

Required deliverable: a compact result containing (a) exact source locator(s), (b) a deterministic representation or formula for all 48 target nodes, (c) uniqueness/count check, (d) convention/ambiguity ledger, and (e) explicit statement of what remains unbridged to runtime indices.

Do not attempt Stage32 authority promotion. Do not edit `MAIN-STATE.json` or claim/frontier files. Do not run FULL178 span replay. If an exact 48-node target cannot be recovered, return a precise blocker rather than filling gaps.