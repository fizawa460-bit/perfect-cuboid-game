# stage32ex5-d

Role: permutation-invariant canonicalization and hostile ambiguity analysis for `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`.

Startup:
1. `AGENTS.md`
2. `stages/stage32-ex5/MAIN-START-HERE.md`
3. `stages/stage32-ex5/MAIN-STATE.json`
4. `stages/stage32-ex5/parallel/BC2-01B-LANES.json`
5. this file
6. only directly required coordinate/action/runtime paths

Task: design an exact projective-node canonicalization that is stable under the relevant permutation/action conventions, then attack it. Check projective scale/sign normalization, zero-coordinate edge cases, orbit representatives, duplicate/collision risks, convention dependence, and whether runtime relabeling changes the resulting node identity.

Required deliverable: canonicalization definition, exact invariance obligations, adversarial test matrix, collision/ambiguity results, and a PASS/BLOCKED result. If full permutation invariance is stronger than the source/runtime semantics justify, identify the exact maximal justified invariance instead of silently weakening the requirement.

This is an independent check, not a rubber stamp of lane C. Do not edit authority/state/claim files. Do not run FULL178 span replay.