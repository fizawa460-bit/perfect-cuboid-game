# stage32ex5-b

Role: repository/runtime reconstruction for `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`.

Startup:
1. `AGENTS.md`
2. `stages/stage32-ex5/MAIN-START-HERE.md`
3. `stages/stage32-ex5/MAIN-STATE.json`
4. `stages/stage32-ex5/parallel/BC2-01B-LANES.json`
5. this file
6. only exact code/artifact paths discovered search-first

Task: determine exactly what runtime exceptional indices `0..47` mean in the Stoll/runtime ordering already reached by BC2-01A. Trace their construction path, ordering, pair/support semantics, permutation conventions, and any normalization. Produce a deterministic way to regenerate the 48 runtime objects and identify what data each index carries.

Required deliverable: (a) exact repository locators, (b) construction/order algorithm, (c) 48-count and uniqueness checks, (d) any existing coordinate-bearing data attached to each runtime object, (e) ambiguity or information-loss ledger, and (f) the minimal missing adapter from runtime object to projective node.

Do not assume an index is a coordinate label merely because counts match. Do not edit authority/state/claim files. Do not run FULL178 span replay.