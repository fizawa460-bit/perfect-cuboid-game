# stage32ex5-e

Role: exact Magma enumeration-semantics investigation for `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`.

Startup:
1. `AGENTS.md`
2. `stages/stage32-ex5/MAIN-START-HERE.md`
3. `stages/stage32-ex5/MAIN-STATE.json`
4. `stages/stage32-ex5/parallel/BC2-01B-LANES.json`
5. this file
6. only exact Magma/Stoll/runtime sources discovered search-first

Task: isolate the semantics of the exact primitive behind Stoll's `pts := Points(SingularSubscheme(S))`. Determine whether the resulting 48-point enumeration has a documented or replayably deterministic ordering in the pinned runtime/toolchain, what representation/type owns that ordering, and whether repository evidence pins enough version/context to reproduce it. Trace only the enumeration primitive and its immediate callers; lane B keeps the broader repository exceptional-index provenance task.

Required deliverable: exact source/manual/runtime locators, object/type and enumeration semantics, version/pinning evidence, a replay procedure if ordering is recoverable, and a precise blocker proof if the numeric order is intentionally unspecified or unrecoverable. Distinguish deterministic-in-one-runtime from canonical/documented semantics.

Do not infer a formula ordering from the 48-count. Do not edit authority/state/claim files. No FULL178 span replay.