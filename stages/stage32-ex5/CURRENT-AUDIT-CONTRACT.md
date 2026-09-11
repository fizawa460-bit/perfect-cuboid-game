# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. `AUDIT-CONTRACT.md` remains historical source-locked provenance.

## Active audit target

PR #1776 is the active Stage32EX5 audit surface. BC2-25 is retained at the boundary33 partition checkpoint: 3 newly exact-UNSAT parents, 16 retained UNKNOWN parents, 0 SAT; 24/36/0 branch UNSAT/UNKNOWN/SAT; 128/38/0 subbranch UNSAT/UNKNOWN/SAT; known parent-UNSAT lower bound 7148. The other 172 BC2-19 UNKNOWN identities remain uninferred. This grants no Stage32 MAIN, FULL178, N350, theorem, effectivity, receiver, endpoint, or Perfect Cuboid credit.

The first hostile audit of #1776 failed at exact head `9bbc491cfde0f8a7f48d9742dad8ff368e4837b2`, review `5176133548`. The compute run itself (`34574409241`) was accepted as successful; repair is required because the retained verifier/state still described BC2-24 and because the BC2-18 executable dependency identities for `hperp_integral_adapter.py` and `pairing_prefix_engine.py` were not fail-closed.

## Repair/re-audit requirements

The repaired exact head must verify the BC2-25 checkpoint canonical, predecessor chain, compute/artifact identity, UNKNOWN accounting, and executable source chain `BC2-25 -> BC2-24 -> BC2-18 -> hperp_integral_adapter / pairing_prefix_engine`. The current dependency blob locks are `fb1eb380ca786e42a6b00c5ef454b0e79fdba771` and `c8e87c6598fa1cd7ba1675fc35fa83bea983c94b` respectively.

`stage32ex5-audit` must be re-run on the repaired exact head. BC2-26 is blocked until that audit passes. Merge remains unauthorized and separate from hostile-audit PASS.
