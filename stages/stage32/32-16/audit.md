# Stage32-16 hostile audit — PR #1374

Verdict: `PASS_EXACT_E20_A0_DELTA_AND_CUMULATIVE_LE65536_ZERO_TIER`

Audited functional head: `0893fb99699ae8b0f16b2041c484e5c2b31111c6`.
Authoritative workflow: `32733420941` (SUCCESS).
Final artifact: `stage32-16-e20-a0-le65536-exact-tier`, id `9529005890`, ZIP SHA256 `efd8b4403eb4557e0fa61d1ac2f894dac517d7f6e06aae2c1e2f506b8b7876a7`.
Final JSON SHA256: `f31b4e8222d3638e05ba8ee5dddc1ab1d3f1aef4ecb3d083fe29965c42aad558`.
Final canonical SHA256: `5e6a447f7df3a712d6b8c873bc7e912f58b74b44cf4f461dc4cecd800c9e516c`.

## 1. Independent source-lock and tier reconstruction

The audit independently downloaded and rehashed the Stage32-14 profile, Stage32-15 hostile-audited predecessor, Stage32-16 deterministic plan, final aggregate, and predecessor-neighbor regression artifacts.

The exact source-locked hashes independently reproduce:

- e20/a0 profile canonical SHA256: `e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5`;
- audited `<=16384` predecessor canonical SHA256: `593bb0fc5231222ab9ce79ae0bd5802d77311d02fd633152d665f869b095611f`;
- Stage32-16 plan canonical SHA256: `1f6f879d3f0e9eafd74dffc5afc4695e27f9758101fe32e23ecffcb16f07bdd6`.

Reapplying the threshold predicates directly to all 1,182 profile cells gives exactly:

- predecessor `<=16384`: 69 cells / 655,558 branches;
- delta `16384 < branches/cell <=65536`: 232 cells / 6,178,556 branches;
- cumulative `<=65536`: 301 cells / 6,834,114 branches.

The delta minimum is 17,664 branches/cell and maximum is 65,376 branches/cell. The plan's selected cell-key/branch-count map equals this independently reconstructed delta exactly.

## 2. Exact partition and execution architecture

The 232 delta cells are partitioned into 287 exact global-index modulo work items. Independent plan inspection verifies every cell has all shard indices `0..shard_count-1` exactly once and the expected modulo-shard counts sum exactly to each parent cell and to all 6,178,556 delta branches.

The 287 items are deterministically packed into 48 bundles with expected branch loads 111,648 through 129,376. This changes execution scheduling only. The runner imports the source-locked Stage32-08 exhaustive search, re-derives the same exact 140-cap certificate, preserves the 1,000,000-node per-branch limit, and retains exact global branch-index modulo semantics.

Raw branch evidence is verified before compaction. The compact verifier requires exact branch-index progression, complete numerical enumeration, `enumeration_exhausted=true`, `node_budget_exhausted=false`, an accepted exact solver result, and exact survivor consistency before emitting a certificate. Missing/duplicate work items, UNKNOWN, incomplete branches, or node-budget exhaustion therefore cannot receive UNSAT credit in the aggregate.

## 3. Independent final-artifact verification

The downloaded final ZIP independently hashes to

`efd8b4403eb4557e0fa61d1ac2f894dac517d7f6e06aae2c1e2f506b8b7876a7`,

and its sole `e20-tier65536.json` hashes to

`f31b4e8222d3638e05ba8ee5dddc1ab1d3f1aef4ecb3d083fe29965c42aad558`.

Removing only `canonical_sha256_without_this_field` and independently canonicalizing the parsed JSON reproduces exactly

`5e6a447f7df3a712d6b8c873bc7e912f58b74b44cf4f461dc4cecd800c9e516c`.

The final artifact contains exactly the 301 profile cell keys selected by the `<=65536` predicate. All 69 audited predecessor cell summaries are unchanged in the cumulative artifact. The independently isolated 232-cell delta sums to:

- 6,178,556 branches;
- 1,602,160 search nodes;
- UNKNOWN = 0;
- numerical survivors = 0;
- all 232 delta cells UNSAT.

The cumulative accepted tier is therefore:

- 301/301 selected cells complete;
- 6,834,114/6,834,114 branches complete;
- 1,881,870 search nodes;
- UNKNOWN = 0;
- numerical survivors = 0;
- all 301 selected cells UNSAT.

## 4. Replacement-runner regression

The regression artifact id `9523004366` independently rehashes to ZIP SHA256

`52802de9951110b6334987b51599ed579f81a51edb3270ddc79996566023dd0f`.

Its compact certificate and regression result canonical hashes independently verify. The replacement runner recomputed inherited cell 588 shard `s0of2` with exactly 2,448 branches, 48 search nodes, zero UNKNOWN, zero survivors, and reproduced the inherited branch-evidence-stream SHA256 exactly:

`8d258cf6ae672e497af3dcf4f32afe4f1dc4b35b41a7cebcec2501da5b424544`.

Regression result canonical SHA256:

`a6d319062c8d0e7045654b6f167f8425839edbee0bc73b98c476c15956a3c544`.

This supports execution equivalence for the scheduling/context-reuse redesign; it does not independently create broader theorem or effectivity credit.

## 5. Trigger repair, storage and performance claims

The two commits after the authoritative functional head alter only README/audit/execution-state material and the workflow's heavy-compute change gate; none of the six exact Python execution sources changed. The documentation-triggered run `32751922545` was cancelled and receives no certificate or aggregate credit.

Validation run `32752154788` completed SUCCESS with the change-gate job successful and every heavy plan/pilot/wave/aggregate job skipped. The trigger repair is therefore accepted as workflow-maintenance isolation and does not replace the authoritative run.

The reported incremental retained storage is consistent with the evidence: the conservative new-run bound is 22,540,000 bytes, while the authoritative final inventory reports 51 new artifacts totaling 553,651 compressed bytes. Historical artifacts are background context only and no authoritative historical evidence was deleted.

The reported performance ratios are arithmetic/resource measurements, not mathematical credit. The recorded baseline and current totals reproduce approximately 1.591727x runner-efficiency improvement and 1.714088x end-to-end throughput improvement.

## 6. Scope firewall and next boundary

This audit closes only the e20/a0 cumulative numerical tier through 65,536 materialized branches per cell.

It does **not** close the 1,182-cell e20/a0 parent. Exactly 881 profile cells remain outside this audited tier. It does not establish effectivity, actual curve existence, the full `d=8,g=0` row, the full `d<=176/d<=192` numerical census, any receiver discharge, or any perfect-cuboid existence/nonexistence result.

Mandatory retained state:

`E20_A0_PARENT_COMPLETE=false`
`STAGE32_01_COMPLETE=false`
`STAGE32_CLOSED=false`
`FULL_D8_G0_ROW_COMPLETE=false`
`FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false`
`R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false`
`R29_LG2=NOT_DISCHARGED`
`R29_LG2_EFF=NOT_DISCHARGED`
`R29_LG2_MB=NOT_DISCHARGED`
`G10_LOWGENUS_PICARD=AMBER`
`THEOREM_CREDIT=false`
`RECEIVER_CREDIT=false`

The next Stage32-main-batch may use this audited `<=65536` tier as its exact predecessor, but must design and preflight any larger execution envelope separately. No larger tier receives credit from this audit.
