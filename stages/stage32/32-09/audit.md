# Stage32-09 hostile audit — exact cumulative <=256 high-mass tiers

```text
AUDITED_PR=1359
AUDITED_FUNCTIONAL_HEAD=74aa140dd4f4a34887ae6d8d70596a43b20a26cb
AUDIT_VERDICT=PASS_EXACT_TIER256_CUMULATIVE_EXPANSION
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
THEOREM_CREDIT=false
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

## Verdict

PASS at the claimed bounded numerical-tier scope. No mathematical repair was required.

PR #1359 changes only the Stage32-09 workflow and documentation. The exact materialized-cell solver `stages/stage32/32-08/run_materialized_parent_tier.py` is unchanged from the hostile-audited Stage32-08 predecessor. The production head workflow run `32685512985` completed successfully.

## Independent audit checks

### 1. Immutable profile -> selected-tier reconstruction

The Stage32-08 audited materialization profiles were independently rehashed and filtered by the literal branch-cost predicate `materialized_branch_count <= 256`.

```text
e8/a36 profile SHA  = 97608b176d7a91677f63cd293502f7042a9a9f6ad30904631260c9d560b7be17
selected             = 24/53 cells
scheduled branches   = 1161

e10/a30 profile SHA = 993d0005f60499b50b03b899153b60f93de757a74f53d942e5a2168830cc5123
selected             = 64/134 cells
scheduled branches   = 3344
```

The independently reconstructed selected cell IDs and cell indices match the new artifacts exactly for both parents.

### 2. Deterministic artifact hashes independently recomputed

Runtime-only fields were removed according to the solver's canonicalization rule and both tier hashes were independently recomputed from the downloaded artifacts.

```text
e8/a36 <=256
  deterministic SHA = e0e714271d192722ba43097818d0d4cabd1fadf08c25d7df4a610c5da95a3def

e10/a30 <=256
  deterministic SHA = 12dae92b3b7dab3834d81c3f1af552438a89c157bb2644a2e26b2e325c2da9b6
```

Both reproduce the submitted locks exactly.

### 3. Hostile-audited <=64 prefix reproduced exactly

The Stage32-08 predecessor artifacts from run `32682503895` were independently rehashed:

```text
e8/a36 <=64  = a58a6589633ef76a08bba420efabbd52d1b56c28eaaaa131c4ebb336666f13b0
e10/a30 <=64 = 383f2a2aa202aad1384ada1ef41041d0c731445e1ea7baff0ea895e91117a0e9
```

For both parents:

- predecessor selected cell IDs are the exact prefix of the cumulative <=256 IDs;
- predecessor selected cell indices are the exact prefix of the cumulative <=256 indices;
- every predecessor cell record equals the recomputed <=256 cell record after removal of runtime-only fields;
- no predecessor survivor disappears and no predecessor record changes.

Thus this is a cumulative exact extension, not a disconnected resample.

### 4. Complete branch and UNKNOWN accounting

Independent artifact accounting gives:

```text
e8/a36 <=256
  selected cells      = 24
  materialized branches = 1161
  executed branches   = 1161
  complete cells      = 24
  UNSAT cells         = 17
  SAT_EXHAUSTED cells = 7
  UNKNOWN cells       = 0
  numerical survivors = 57

e10/a30 <=256
  selected cells      = 64
  materialized branches = 3344
  executed branches   = 3344
  complete cells      = 64
  UNSAT cells         = 64
  SAT_EXHAUSTED cells = 0
  UNKNOWN cells       = 0
  numerical survivors = 0
```

All `4505` scheduled branches were executed. Every branch in every selected cell reports complete numerical enumeration; no node-budget UNKNOWN is promoted.

### 5. Increment over the audited <=64 checkpoint

Set-difference and per-cell accounting independently reproduce:

```text
e8/a36
  +3 cells
  +460 branches
  +1 UNSAT cell
  +2 SAT_EXHAUSTED cells
  +24 numerical survivors

new e8 cells:
  eac389c3d64878e92c39d92c : 140 branches, 8 survivors
  7131ec2d700a865f3f2bb5d3 : 160 branches, 16 survivors
  920bd92cfaef8f0a3326b919 : 160 branches, UNSAT

e10/a30
  +6 cells
  +1204 branches
  +6 UNSAT cells
  +0 survivors
```

The 57 cumulative e8 survivor basis-coordinate vectors are pairwise distinct. The predecessor 33 are a subset of them exactly, leaving 24 genuinely new numerical survivors in this tier.

### 6. Scope and duplicate-credit firewall

No orbit statement is accepted for the 24 new e8 survivors. No effectivity or actual-curve existence statement is accepted. The <=256 tier does not close either high-mass parent because only 24/53 and 64/134 immutable signature cells are included.

Therefore no full-d8, full Stage32 numerical, effectivity, multibranch, Stage29 receiver, route-color, theorem, endpoint, or perfect-cuboid credit follows.

## Accepted checkpoint

```text
D8_HIGHMASS_MATERIALIZED_EXACT_TIERS_LE256=AUDITED
E8_A36_LE256_SELECTED_CELLS=24/53
E8_A36_LE256_BRANCHES=1161
E8_A36_LE256_SURVIVORS=57
E8_A36_LE256_UNKNOWN=0
E10_A30_LE256_SELECTED_CELLS=64/134
E10_A30_LE256_BRANCHES=3344
E10_A30_LE256_SURVIVORS=0
E10_A30_LE256_UNKNOWN=0
```

## Next legal Class-2 work

The same exact leaf remains open. After merge, the next natural bounded cumulative checkpoint is `<=1024` using the unchanged exact solver and the same per-branch node budget, with the audited <=256 tier locked as its regression prefix.

```text
NEXT_ITEM=32-01-D8-HIGHMASS-MATERIALIZED-TIER-EXPANSION-LE1024
NEXT_EXPECTED_COMMAND=Stage32-main-batch
```
