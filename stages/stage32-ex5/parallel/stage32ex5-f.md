# stage32ex5-f

Role: Picard-slot / intersection-signature reverse lookup for `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`.

Startup:
1. `AGENTS.md`
2. `stages/stage32-ex5/MAIN-START-HERE.md`
3. `stages/stage32-ex5/MAIN-STATE.json`
4. `stages/stage32-ex5/parallel/BC2-01B-LANES.json`
5. this file
6. only exact Picard/intersection/pairing artifacts discovered search-first

Task: work backwards from the runtime exceptional slots, especially the `92+k` convention and any retained Picard/intersection/pairing matrices, to construct an order-independent signature for each exceptional divisor. Determine whether those signatures can be matched exactly and injectively to the 48 source singular nodes using incidence with retained curves or other exact geometric data.

Required deliverable: exact artifact/source locators, definition of the signature, 48-count/uniqueness table, collision ledger, exact node-matching rule if successful, and verifier/replay procedure. If signatures are insufficient, identify the smallest missing datum rather than falling back to guessed runtime order.

Do not assume matrix row/column labels without proving their provenance. Do not edit authority/state/claim files. No FULL178 span replay.