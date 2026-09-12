# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance. PR #1776 remains open/draft/unmerged. BC2-30 hostile audit **PASS** is predecessor authority: exact head `38b60be7d0390ad5fa89ddb4dcd9511cfe36c57f`, review `5184226057`.

## BC2-31 fresh all-7336 replay candidate boundary

The historical attempt to recover the unretained 172 BC2-19 UNKNOWN identities was rejected: generation-2 replay run `34660585544` produced `7113 UNSAT / 223 UNKNOWN / 0 SAT`, raw canonical `f5ef75a81dcb3a952689a0bad14fcf8b122d2b321b4b63a469b3e761910d7f13`; the historical 2-second timeout status stream is not replay-stable, so no exact historical-172 identity claim is retained.

BC2-31 therefore executed a fresh all-7336 replay at exact compute head `d5ee384f0dc0675ce034969964e71ccfdae25459`, workflow `34665881779`, authorize job `103477546494`, compute job `103477565567`, artifact `10288804651`. The retained result is `7166 UNSAT / 170 UNKNOWN / 0 SAT`; every fresh UNKNOWN identity is explicit. Checkpoint canonical is `f2aec1d923ff43393d24364864be36e223d43674149e6655a920d3b3d5de3ae4`, checkpoint blob `188601efcb99d33fe00fc60dc3c2f40f51e65b20`, raw canonical `8929e6bdffca0297c3ebbf67032fa514bf4685590563df91c7db26f9570c8ad6`, status-stream sha256 `1ad123b746f30db4542171e45da72a0fb93a408d6b312925af76dbb02da616eb`, UNKNOWN-list sha256 `df7db2159df41d93ce64b7d2ccf230b9363711bbdf769280e1df0560cfbae1ae`.

The fresh generation-1 runkey is consumed/disarmed and the one-shot fresh executor is removed. Audit must verify predecessor receipt, producer/preflight locks, executed workflow/artifact receipt, exact checkpoint/canonical, explicit 170-UNKNOWN list, and the firewall that fresh run-specific statuses do not reconstruct the expired historical 172 set.

This candidate raises the local known parent-UNSAT lower bound to `7166` only. It does **not** prove the whole first block UNSAT, FULL178 closure, Stage32 MAIN/N350 promotion, theorem/effectivity/receiver/endpoint/Perfect Cuboid credit, or merge authorization. BC2-32 is blocked until a fresh `stage32ex5-audit` PASS on the final exact head.
