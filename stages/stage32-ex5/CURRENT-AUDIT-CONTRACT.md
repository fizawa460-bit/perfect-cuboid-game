# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance. PR #1776 remains open/draft/unmerged.

## Predecessor authority

BC2-31 hostile audit **PASS** is the direct predecessor authority: exact head `72118efafdd25ca3b08d408463db46e2800e22df`, review `5184996992`. Its bounded result was a fresh all-7336 replay with `7166 UNSAT / 170 UNKNOWN / 0 SAT`; the 170 current UNKNOWN identities are explicit and hash to `df7db2159df41d93ce64b7d2ccf230b9363711bbdf769280e1df0560cfbae1ae`. The rejected historical 172-identity reconstruction remains rejected and must not be revived.

## BC2-32 targeted replay candidate boundary

BC2-32 replayed exactly those hostile-audited 170 UNKNOWN parent identities with a 20,000 ms per-parent limit, one heavy runner, and no heavy scaleout. Compute head: `5272a3b0d0835f9b970250adefada2c9868cecc9`. Workflow run: `34672718019`. Authorization job: `103497019707`. Compute job: `103497078073`. Artifact: `10292081214`.

Retained result: `63 UNSAT / 107 UNKNOWN / 0 SAT`. The known parent-UNSAT lower bound therefore rises from `7166` to `7229`. The remaining 107 UNKNOWN identities are all explicit; their canonical list hash is `e617578c83e604866c22de5d38d62d93fe4453886b0d46ddce609bce87308492`. Result canonical: `905b416477b23199c794a1267e143158e0dac7baaaa9f809d9cd8528e8e4aa6c`. Status-stream sha256: `bdbd63978e0fdd34687661cf2b60e74553e7108e93fc7c773dd3e3406fdaf320`. Raw JSON sha256: `1d62550f3008d96be10b2f3e91e836181c6dbd3b774f7c017feef4734e14e89f`. Artifact ZIP sha256: `ba7a4314dcc7082c75dc18fa583b11a03f8e88d09d01526fa197c235d2717f6f`.

The retained checkpoint is `stages/stage32-ex5/breadth-cycle-2/bc2-32-fresh-unknown170-replay-checkpoint.json`, canonical `905b416477b23199c794a1267e143158e0dac7baaaa9f809d9cd8528e8e4aa6c`, blob `d21a3ddd3c2e06dd5523777aa3141ff41392a467`. The generation-1 runkey is consumed/disarmed. BC2-33 is blocked until this boundary passes hostile audit.

## Audit obligations

Audit must independently verify the BC2-31 PASS receipt, exact BC2-31 170-UNKNOWN target identity set, BC2-32 source/preflight/checkpoint locks, fresh commit-range runkey authorization, workflow/job/artifact provenance, the exact `63/107/0` partition, explicit 107-UNKNOWN list, and the resulting lower bound `7229`.

The following must remain false: whole-first-block UNSAT, whole-stratum closure, FULL178 completion, Stage32 MAIN pruning credit, N350 registration, effectivity/actual-curve credit, theorem/endpoint credit, Perfect Cuboid existence/nonexistence claim, merge authorization. UNKNOWN may not be relabelled UNSAT. No BC2-33 execution before hostile-audit PASS.
