# Stage32EX5 current roadmap

This mutable roadmap does not override `stages/stage32/MAIN-STATE.json`. PR #1776 remains active/open/draft/unmerged.

BC2-35 hostile audit **PASS** is consumed from exact head `8bea7a6be26e01db0deb138dbd8406f578447921`, review `5187359907`.

Audited current local result:

- BC2-35: `12 UNSAT / 52 UNKNOWN / 0 SAT`
- known parent-UNSAT lower bound: `7284`
- remaining UNKNOWN hash: `95743ba70ed11191bffa8ce8464ff190d5133cdcd0643d7b83f7756ed33f9818`

BC2-36 now targets exactly those 52 audited UNKNOWN parents at `100000 ms` per parent, one heavy runner, no scaleout. Its producer source-locks the hostile-audited BC2-35 checkpoint plus BC2-32/BC2-19/BC2-18 before reusing `build_parent_space()`.

Cold execution boundary:

- producer blob: `18f9c2146d5dc97400c4af1a8691560523cc03cf`
- preflight canonical: `b2cc1cd97fe8da4504da980aa1c470f1aa419f9417b3eea8b1533305382155b0`
- preflight blob: `aa9bf40cf3550cae33cdfe8669aa51a80acddcec`
- runkey generation: `0`
- runkey armed: `false`

The next operational step is exact-head cold CI, then a fresh generation-1 arm followed by the BC2-36 heavy replay. After a successful run, mainbatch must retain the compact artifact, disarm/consume the runkey, retire the BC2-36 heavy path, install a fail-closed retained verifier, and freeze a new hostile-audit boundary.

BC2-37 remains blocked until that future BC2-36 hostile-audit PASS. No timeout UNKNOWN is relabelled UNSAT and no Stage32 MAIN/FULL178/N350/theorem/effectivity/receiver/endpoint/Perfect Cuboid/merge credit follows automatically.
