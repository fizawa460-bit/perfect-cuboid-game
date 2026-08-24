# Stage32-09 — audited-prefix exact <=256 tier expansion

This unit continues the audited Stage32-08 Class-2 leaf `L32-01-D8-HIGHMASS-MATERIALIZED-TIER-EXPANSION` after hostile audit verdict `PASS_AFTER_CONTROLLER_AND_REPO_LOCAL_EVIDENCE_REPAIR` on PR #1354.

The accepted predecessor is the exact cumulative `<=64` materialized signature-cell checkpoint:

```text
e8/a36  : 21/53 cells,  701 branches, 0 UNKNOWN, 33 numerical survivors
           deterministic SHA a58a6589633ef76a08bba420efabbd52d1b56c28eaaaa131c4ebb336666f13b0

e10/a30 : 58/134 cells, 2140 branches, 0 UNKNOWN, 0 numerical survivors
           deterministic SHA 383f2a2aa202aad1384ada1ef41041d0c731445e1ea7baff0ea895e91117a0e9
```

## Bounded target

The immutable materialization profiles audited in Stage32-08 give the next natural cumulative tier:

```text
e8/a36 <=256  : 24/53 cells, 1161 scheduled materialized branches
e10/a30 <=256 : 64/134 cells, 3344 scheduled materialized branches
```

Stage32-09 uses the unchanged exact Stage32-08 runner `run_materialized_parent_tier.py` with the same `1,000,000` node budget per materialized branch. No solver timeout or node-budget extension is introduced.

## Predecessor regression lock

Workflow `.github/workflows/stage32-09-tier256.yml` downloads the audited run `32682503895` predecessor artifacts before execution. For each parent it requires:

1. the predecessor deterministic SHA to match the hostile-audited lock;
2. the `<=64` selected cell IDs and indices to be the exact prefix of the `<=256` tier;
3. every recomputed predecessor cell, after removing runtime-only fields, to equal the audited `<=64` cell record exactly;
4. all exact branch, lattice, cap and UNKNOWN firewalls to remain unchanged.

Thus the expansion is cumulative and regression-locked rather than a disconnected new sample.

## Hostile-audited production result

Authoritative audit: `stages/stage32/32-09/audit.md`.

```text
AUDIT_VERDICT=PASS_EXACT_TIER256_CUMULATIVE_EXPANSION
AUDITED_FUNCTIONAL_HEAD=74aa140dd4f4a34887ae6d8d70596a43b20a26cb
WORKFLOW_RUN=32685512985

E8_A36_LE256_SELECTED_CELLS=24/53
E8_A36_LE256_BRANCHES=1161
E8_A36_LE256_UNSAT_CELLS=17
E8_A36_LE256_SAT_CELLS=7
E8_A36_LE256_SURVIVORS=57
E8_A36_LE256_UNKNOWN=0
E8_A36_LE256_SHA=e0e714271d192722ba43097818d0d4cabd1fadf08c25d7df4a610c5da95a3def

E10_A30_LE256_SELECTED_CELLS=64/134
E10_A30_LE256_BRANCHES=3344
E10_A30_LE256_UNSAT_CELLS=64
E10_A30_LE256_SAT_CELLS=0
E10_A30_LE256_SURVIVORS=0
E10_A30_LE256_UNKNOWN=0
E10_A30_LE256_SHA=12dae92b3b7dab3834d81c3f1af552438a89c157bb2644a2e26b2e325c2da9b6
```

The audit independently reconstructed the <=256 selected-cell sets from the locked Stage32-08 profiles, recomputed both deterministic hashes, verified all `4505` branch records, and compared every hostile-audited <=64 predecessor cell against the cumulative <=256 artifact after removing runtime-only fields.

Relative to the audited <=64 checkpoint:

```text
e8/a36 : +3 cells, +460 branches, +1 UNSAT, +2 SAT_EXHAUSTED, +24 numerical survivors
e10/a30: +6 cells, +1204 branches, +6 UNSAT, +0 numerical survivors
```

No orbit/effectivity interpretation is assigned to the 24 new e8 survivors.

## Credit boundary

The audited `<=256` result is still only a selected immutable-signature-cell numerical tier. It does not complete either parent, the full `d=8,g=0` row, the Stage32 numerical census, effectivity, multibranch analysis, or any Stage29 receiver.

```text
THEOREM_CREDIT=false
AUDIT_STATUS=PASS_EXACT_TIER256_CUMULATIVE_EXPANSION
RECEIVER_CREDIT=false
FULL_D8_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Next checkpoint

After merge, the same Class-2 leaf remains open. The next natural bounded cumulative tier is `<=1024`, using the unchanged exact solver, unchanged per-branch node budget, and the audited <=256 artifacts as the next regression prefix.

```text
NEXT_ITEM=32-01-D8-HIGHMASS-MATERIALIZED-TIER-EXPANSION-LE1024
NEXT_EXPECTED_COMMAND=Stage32-main-batch
```
