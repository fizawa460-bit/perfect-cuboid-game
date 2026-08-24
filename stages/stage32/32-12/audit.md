# Stage32 combined hostile audit — PR #1364 -> #1365 -> #1366

Verdict: `PASS_CHAIN_AFTER_EXACT_RESOURCE_WALL_REPAIR_AND_E8_PARENT_RECONSTRUCTION`

Audited functional heads and runs:

- PR #1364 `2c4aa1ccb16d809c48bdb081b8f17a787eb8b0f9`, run `32689063120`.
- PR #1365 `8f9724b341faec3ac3d8acac63d185a89e859afe`, run `32694939071`.
- PR #1366 `7b491b5ffc259a3947264e142aa4c748f8e7a798`, run `32699046660`.

## 1. PR #1364 — exact partial evidence with a measured resource wall

The matrix schedules exactly the nine e8/a36 cells outside the audited `<=65536` prefix and exactly the 28 e10/a30 cells satisfying `4096 < materialized_branch_count <= 700000`. Every job locks the audited materialization profile and re-derives the exact 140 cap certificate before calling the unchanged Stage32-08 one-cell exhaustive solver with node limit `1000000`.

Run `32689063120` produced 34 successful exact cell artifacts. Exactly three jobs were externally cancelled during the exhaustive step at the approximately 90-minute Actions wall:

- e8/a36 cell 39 `ceb88a2b425fb743669aa33e`, 529480 branches;
- e10/a30 cell 27 `2719e0ba39bfa79944906bf5`, 639840 branches;
- e10/a30 cell 37 `3af4cf3d535a93607ef8b5bb`, 605120 branches.

Independent inspection of all three logs confirms: profile/cap locking completed, the exact solver started, GitHub cancelled the process at the job wall, no solver failure or `UNKNOWN_NODE_BUDGET` was reported, and no finalized `cell.json` existed. Therefore these three jobs receive no result credit from #1364; #1364 is accepted only as exact partial evidence plus a measured resource-wall witness.

## 2. PR #1365 — exact shard replacement

The repair changes only outer scheduling. It reconstructs the identical global branch order and selects branches by `branch_index mod 4`; each selected branch is passed to the unchanged Stage32-08 `search_exhaustive` backend with the same source lock, cap semantics, qtail12 context, and per-branch node limit.

All 12 shard artifacts were independently inspected by streaming their branch records rather than trusting the aggregate. For each repaired cell the four shards are exact residue progressions `0,4,8,...`, `1,5,9,...`, `2,6,10,...`, `3,7,11,...`, terminating at the correct final indices. Their union covers every branch index exactly once with no gap or duplicate. Across all 12 shards: incomplete branch count = 0 and node-budget-exhausted count = 0.

Exact repaired cells:

- e8/a36 cell 39: 529480 branches, 240 numerical survivors, 976608 search nodes;
- e10/a30 cell 27: 639840 branches, 16 numerical survivors, 1041632 search nodes;
- e10/a30 cell 37: 605120 branches, 16 numerical survivors, 929280 search nodes.

Total repaired branches = 1774440; total repaired survivors = 272. The aggregate canonical SHA independently reproduces
`7550900e558a47d07c41164dcb1547901b2849ba53e72f4882b7d15d4ce62384`.

Thus #1365 exactly replaces, rather than supplements or guesses, the three no-output jobs from #1364.

## 3. PR #1366 — independent e8/a36 parent reconstruction

The final artifact ZIP digest independently matches
`3bcc9788f652785b568633754f5ba047d1ae74298885f49f212148b0e5db9e8c`.

The e8/a36 parent was independently reconstructed from three disjoint evidence blocks:

1. audited Stage32-10 `<=65536` predecessor: 44 cells, 122906 branches, 330 survivors;
2. eight direct successful e8 tail cells from #1364: 1131565 branches and 459 survivors;
3. repaired cell 39 from #1365: 529480 branches and 240 survivors.

The independent union gives exactly 53/53 immutable signature cells, exactly 1783951/1783951 profile branches, and exactly 1029 distinct numerical Picard survivors. It agrees cell-for-cell and survivor-for-survivor with the #1366 parent artifact. The self-intersection distribution is exactly:

- `C^2 = 0`: 5;
- `C^2 = -4`: 128;
- `C^2 = -8`: 896.

The independently recomputed parent canonical SHA is
`5c9cf74481108f1d8360e9bcbebe3c875a043be230c6a7e5814ab9728b64fc76`.

## 4. Independent Aut(S) orbit verification

The source-locked 9 automorphism generators were rechecked against the Picard pairing and hyperplane class. Their generated group closes to order 1536. The selected 64-row recovery matrix has determinant `274877906944 = 2^38`.

All 1029 parent survivors were independently converted to their 140-intersection vectors and partitioned under the full group. The result is exactly eight pairwise-disjoint full numerical orbits. Sorted full orbit sizes are
`[6, 96, 96, 192, 192, 384, 384, 384]`, with full-orbit union size 1734. All 1734 orbit images recover to integral Picard-basis vectors, reproduce all 140 pairings exactly, and none is one of the frozen known 140 classes. Every orbit member returning to the a=36 slice is present in the completed parent.

Regression orbits remain exact:

- square 0: orbit size 6, stabilizer 256, a-distribution `{32:1,36:5}`;
- square -4: orbit size 192, stabilizer 8, a-distribution `{34:64,36:128}`.

The independently recomputed orbit-manifest SHA is
`e05b4b3a18cfc14e84c92318aeb2534f10c82d31a965a82f478a0fd641ca5c7a`.

## 5. e10/a30 progress inherited from the same chain

The audited predecessor covers 102/134 cells. PR #1364 supplies 26 exact successful new e10 cells and PR #1365 exactly repairs its two e10 timeouts. Therefore exact completed coverage is now 130/134 cells. The four intentionally unexecuted giant cells remain:

- cell 43 `42ee1ca9ffc49798d5c927a6`: 1095920 branches;
- cell 64 `65bd86aef2d39bf5e13aa268`: 1179360 branches;
- cell 100 `cb01d3f2aed50c00b72d69e9`: 2534560 branches;
- cell 108 `d6c2af90f25f4a5940eb3dd1`: 2596160 branches.

No complete e10 parent claim is made.

## 6. Credit firewall and closure verdict

Accepted scope is numerical Picard census/orbit data only. Numerical class existence does not certify effectivity or an actual curve. The e8/a36 sub-parent is numerically complete, but the full Stage32-01 numerical census is not complete because e10/a30 still has four cells and other Stage32-01 obligations remain.

The following remain unchanged:

`FULL_D8_G0_ROW_COMPLETE=false`
`FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false`
`R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false`
`R29_LG2=NOT_DISCHARGED`
`R29_LG2_EFF=NOT_DISCHARGED`
`R29_LG2_MB=NOT_DISCHARGED`
`G10_LOWGENUS_PICARD=AMBER`
`THEOREM_CREDIT=false`
`RECEIVER_CREDIT=false`

Hostile-audit verdicts:

- #1364: `ACCEPTED_PARTIAL_EVIDENCE_RESOURCE_WALL_THREE_CELLS`;
- #1365: `PASS_EXACT_MOD4_TIMEOUT_SHARD_REPAIR`;
- #1366: `PASS_COMPLETE_E8_A36_PARENT_AND_FULL_AUT_NUMERICAL_ORBIT_CENSUS`;
- combined chain: `PASS_CHAIN_AFTER_EXACT_RESOURCE_WALL_REPAIR_AND_E8_PARENT_RECONSTRUCTION`.

Merge order #1364 -> #1365 -> #1366 is audit-authorized, subject to final-head mergeability/CI checks. Stage32 remains open; the next bounded production target is the four remaining e10/a30 giant cells, preferably partitioned from the outset rather than repeating the measured single-job wall.