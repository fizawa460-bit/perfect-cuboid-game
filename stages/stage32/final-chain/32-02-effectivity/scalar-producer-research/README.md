# 32-02 scalar producer research

## Scope
Produce a fail-closed, source-locked record `{row_id,d,negative_hperp_square_N}` for a concrete 32-01 terminal/Picard witness, for consumption by the existing 32-02 RR gate.

## Non-goals
No FULL178 enumeration, CUT/EX5/MB computation, MAIN authority mutation, pruning credit, irreducibility/genus claim, or merge authorization.

## Success ladder
1. Replay a supplied integral Picard witness to exact `N=-y^2`.
2. Bind `d`, divisibility `m=16/gcd(d,16)`, and the RR inequality to that witness.
3. State precisely the missing producer fields needed for every final survivor.

## Audit repair (review 5184048998)

The canonical record is `STAGE32_32_02_SCALAR_PRODUCER_V1`, with
`picard64_coordinates`, `selected64_pairings`, terminal identity and witness
source locks. Both actual producers return this protocol; `scalar_producer.py`
is only the legacy scalar arithmetic illustration, not a witness producer and
not accepted by the protocol.

`source_locked_known_curve_scalar.load()` snapshots all four retained repository
dependencies, verifies every blob before executing any dependency, and executes
only those verified bytes. Preloaded module names cannot substitute different
code. Standard-library and SymPy installations remain runtime dependencies.

Run `python -B stages/stage32/final-chain/32-02-effectivity/scalar-producer-research/verify_scalar_e2e.py`.
It exercises actual known-curve producer -> common protocol -> independent
matrix/coordinate/C2/N replay -> source-locked existing RR consumer. Negative
tests cover each retained dependency drifting before execution, cached-module
substitution, missing fields, noninteger inputs, modified coordinates/pairings,
commitments and internally consistent but forged C2/N.

This replay deliberately passes `source_affirmed=False`: retained matrix locks
are not a replacement for the separate surface/source audit. Expected RR status
is `RR_INCONCLUSIVE_SOURCE_NOT_AFFIRMED`; effectivity and all production credits
remain zero. Local tests are not a hostile-audit PASS or exact-head CI receipt.
