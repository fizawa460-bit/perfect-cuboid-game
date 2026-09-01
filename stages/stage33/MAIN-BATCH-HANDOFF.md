# Stage33 MAIN transient handoff

status: UNPROMOTED_DELTA
base_main_state_canonical_sha256: 7d52c93a517fc96050b2f78583ae05e5e4ff4f983c2533c673ca008060bd0226

durable_gap_artifact: `stages/stage33/33-12/j2-indlist-magma-picard-bridge-source-lock-gap.json`
durable_gap_canonical_sha256: `85c3e0811bb9e9b5391772ae35e569f4aa0fd12940ca6c2db1b4be59b635ae2c`
durable_gap_commit: `9fa968143ac65b9674bfe43a79a0f7d5c051644d`

## Exact narrowing from this batch

The current retained data do not source-lock the actual 64x64 INDLIST-to-historical-Magma Picard-basis bridge. A corrected exact local backtracking search found two distinct full bridge witnesses satisfying all presently retained constraints simultaneously:

- unimodular determinant `-1`;
- exact historical Gram transport;
- exact intertwining of named `cc`, `ct`, and all seven coordinate signs.

Witness 1 (1-based known-curve indices in historical basis-row order):
`[1,42,22,21,4,77,80,79,68,34,53,39,30,90,32,92,93,94,47,96,97,98,99,100,105,106,54,108,101,48,29,104,109,15,111,112,113,114,115,116,121,122,67,26,24,118,2,120,125,126,127,128,129,130,7,132,135,136,133,134,139,140,137,138]`

Witness 2:
`[8,43,19,20,5,77,80,79,66,35,60,39,30,91,32,89,99,100,52,98,95,96,93,94,108,107,59,105,104,51,29,101,114,15,116,115,110,109,112,111,118,117,65,26,17,121,7,123,125,126,127,128,129,130,2,132,140,139,138,137,136,135,134,133]`

The induced actual `swap12` Picard actions differ:
- witness 1 SHA-256: `75458313bb6d3cd666952d0cbb6d17351bb10228eb82528f5b16057f0efe62c7`
- witness 2 SHA-256: `edc04fc389562ca89f3903db51ae489975e7f903d63944f9ce6156f1a3499aa6`

Their `swap13` actions agree in this pair (SHA-256 `924e9a38a19a54a18216f764fe1a06fbcebc41d81ae5f10f63701d38f9c6648d`), but one differing swap is already sufficient: Gram + named V4 + seven signs do not determine the actual marking. Neither witness is authoritative; they are non-uniqueness witnesses only.

The intended source-locked bridge already has repository adapters:
- producer: `stages/stage33/33-07/extract_indlist_to_magma_picard_basis.py`
- expected retained output: `stages/stage33/33-07/indlist-to-magma-picard-basis.json`
- verifier/transport: `stages/stage33/33-07/certify_marked_picard_basis_bridge.py`
- manual producer workflow: `.github/workflows/stage33-07-marked-picard-basis-bridge-producer.yml`

No prior producer workflow run/artifact was found. An attempted public external-Magma route was stopped because submitting locally assembled source-derived inputs to a third party was not authorized. Do not retry or dispatch the manual workflow without explicit authorization.

## Refined next exact leaf

`SOURCE_LOCK_ACTUAL_INDLIST_TO_HISTORICAL_MAGMA_PICARD_BASIS_64x64_QPIC_BRIDGE_OR_EQUIVALENT_RETAINED_SMITH_COMPOSITE_THEN_DESCEND_ACTUAL_SWAPS_AND_TEST_THE_ORDER4_AFFINE_SLICE`

Acquire the exact source-authorized `indlist-to-magma-picard-basis.json` (or an equivalent retained Smith composite), run `certify_marked_picard_basis_bridge.py`, replay the historical common Smith transport, and only then test literal swap fixedness on the four candidate masks `{4,5,6,7}`. Before using the result, source-lock that the swaps descend to and fix the named Kc J2.

Do not:
- treat either local witness above as the actual bridge;
- reuse non-unique retained-basis swap transports as actual actions;
- use the 20 Kc `preimsinPic` rows as full-surface known-curve qPic bridge rows;
- repeat the seven-sign filter or infer the label from historical mask 6.

No MAIN-STATE/controller progress, source coordinate, Kummer column, closure, receiver, theorem, endpoint, or release credit is added.
