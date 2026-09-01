# Stage33 MAIN transient handoff

status: UNPROMOTED_DELTA
base_main_state_canonical_sha256: 7d52c93a517fc96050b2f78583ae05e5e4ff4f983c2533c673ca008060bd0226

## Exact narrowing from this batch

New certificate:
- `stages/stage33/33-12/j2-marked-order4-geometric-sign-indistinguishability.json`
- verifier: `stages/stage33/33-12/verify_j2_marked_order4_geometric_sign_indistinguishability.py`

The four source-side order-4 candidates retained in the preceding exact gap remain masks `{4,5,6,7}` after all seven safe geometric coordinate-sign fixedness tests. The locked semantic `u1` A_T[2] row and all four proper-Br2 candidate rows are fixed by all seven signs. Thus the safe sign family adds rank 0 and cannot select the named J2 row.

The four candidates form the exact affine plane
`mask4 + span_F2(e0,e1)`
in retained10 coordinates. The remaining label ambiguity therefore has dimension 2. Any positive cross-marking route must provide two independent binary constraints on this slice, or directly materialize the actual proper14 evaluation row / marked order-4 lift.

The existing exact coordinate-swap route was also replayed. The intrinsic 14-dimensional swap pair is exact (`actual-coordinate-swap-at2-actions.json`, canonical SHA-256 `bf44ad79107c3b6ee6b8c14fd6d7dbb67da132956a644e44da32b8bfad98ec3f`), but transport to the retained basis is still non-unique after the named `cc/ct` marking and all seven signs (`intrinsic-to-retained-at2-swap-transport-named-v4.json`, canonical SHA-256 `3f932640dd6ebf04c5c5c148664348b0c2e4a70df12f8d740ea85432323e14ba`). Therefore no retained-basis swap fixedness test is source-locked, and swaps cannot select among masks `{4,5,6,7}` at this leaf.

## Refined next exact leaf

`SOURCE_LOCK_RANK2_CROSS_MARKING_ON_THE_FOUR_ROW_ORDER4_AFFINE_SLICE_OR_DIRECTLY_MATERIALIZE_THE_ACTUAL_U1_PROPER14_ROW_THEN_REPEAT_FOR_U2`

Seek an actual primitive-H2 / marked `NS<->T` anti-isometry datum, or an actual labeled order-512 glue, that evaluates nontrivially on the two remaining affine directions. Do not repeat the seven-sign filter and do not use raw-75D/V4 compatibility, masks 742/736, or historical mask 6 to choose the label.

Do not reuse either witness swap pair emitted by the non-unique transport solvers as though it were the actual retained-basis pair. A further exact Picard/Smith marking invariant would be required before swap naturality is admissible.

No source coordinate, Kummer column, closure, receiver, theorem, endpoint, or release credit is added.
