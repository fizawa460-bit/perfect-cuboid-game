# Stage32-14 — e20/a0 storage-safe cumulative exact tier

Stage32-13 completed and hostile-audited the `e10/a30` parent. The next accepted Class-2 wall inside the still-incomplete degree-8 genus-0 row is the high-mass parent

```text
(d,g,e,a) = (8,0,20,0).
```

The audited Stage32-07 compression inventory is

```text
signature cells                         = 1,182
exceptional assignments after quotient = 1,032,477,716
```

This unit **does not** materialize that billion-state parent globally and does not claim full `e20/a0` closure merely from a profile.

## Execution contract

1. Re-derive the exact 1,182 signature cells from the source-locked Picard core and exact dual-cap certificate.
2. Compute the exact materialized branch count of every signature cell without materializing all exceptional assignments.
3. Select the largest **cumulative** branch threshold satisfying all predeclared hard bounds:

```text
selected cells                  <= 24
selected materialized branches  <= 1,000,000
branches in any selected cell   <= 65,536
shards per selected cell         = 2
compact artifacts               <= 48
compact artifact bytes each     <= 100,000
bulk max-parallel                = 8
```

Selection is never by an arbitrary hand-picked list: every signature cell at or below the chosen materialized-branch threshold is included.

4. Run one representative shard first. It must complete exact enumeration with no node-budget exhaustion, survive post-verification compaction, delete the raw branch rows on-runner, and produce a compact certificate of at most 100 KB.
5. Only after that gate passes may the remaining exact shards fan out.
6. Every bulk shard applies the same 100 KB pre-upload gate. Raw branch rows are never Actions artifacts.
7. Aggregate only when every planned modulo shard is present and exact; verify the cumulative threshold directly against the independently regenerated profile.

The shard-artifact storage envelope is therefore bounded **before compute** by

```text
48 * 100,000 bytes = 4,800,000 bytes.
```

The profile/plan is separately limited to 2 MB and the final aggregate to 5 MB. A size violation is a resource STOP, not a mathematical result.

## Exact solver

This is not a new relaxed solver. Each shard reuses the source-locked Stage32-11r wrapper around the Stage32-08 exhaustive fixed-52/qtail-12 search with node budget `1,000,000` per branch. `UNKNOWN_NODE_BUDGET`, job timeout, missing shard, or failed compaction receives no closure credit.

## Scope

A successful unit certifies only the cumulative selected `e20/a0` tier. Unless all 1,182 cells happen to satisfy the hard envelope, it does not complete the parent and does not complete the degree-8 row.

Mandatory firewalls:

```text
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

If no nonempty cumulative tier fits the fixed envelope, the profile itself isolates a precise Class-2 materialization wall and bulk compute is skipped. If the tier completes with `UNKNOWN=0`, its aggregate becomes the next hostile-audit boundary before widening the threshold or changing the algorithm.
