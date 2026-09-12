# Stage32EX5 current roadmap

This mutable roadmap does not override `stages/stage32/MAIN-STATE.json`. PR #1776 remains active/open/draft/unmerged.

BC2-34 hostile re-audit **PASS** is consumed from exact head `cdb455860849cfd064e3ab8c83d6d4993fb5ff1b`, review `5186516652`.

Audited current local result:

- BC2-34: `17 UNSAT / 64 UNKNOWN / 0 SAT`
- known parent-UNSAT lower bound: `7272`
- remaining UNKNOWN hash: `00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b`

BC2-35 now targets exactly those 64 audited UNKNOWN parents at `80000 ms` per parent, one heavy runner, no scaleout. Its producer source-locks BC2-32/BC2-19/BC2-18 before reusing `build_parent_space()`.

Cold execution boundary:

- producer blob: `40111bb7619113d1c9c766089026bcf59d6bdb01`
- preflight canonical: `e74e6c15050187d06c472c2eff6156c66837f8f9c9de3d2cfca7629b431dadb4`
- preflight blob: `bf2f4b1125925a27c820dfdc49ad796e69b268b4`
- runkey generation: `0`
- runkey armed: `false`

The next operational step is a fresh generation-1 arm followed by the exact-head BC2-35 heavy replay. After a successful run, mainbatch must retain the compact artifact, disarm/consume the runkey, retire the BC2-35 heavy path, install a fail-closed retained verifier, and freeze a new hostile-audit boundary.

BC2-36 remains blocked until that future BC2-35 hostile-audit PASS. No timeout UNKNOWN is relabelled UNSAT and no Stage32 MAIN/FULL178/N350/theorem/effectivity/receiver/endpoint/Perfect Cuboid/merge credit follows automatically.
