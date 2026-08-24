# Stage32-15 hostile audit — PR #1372

Verdict: `PASS_EXACT_E20_A0_DELTA_AND_CUMULATIVE_LE16384_ZERO_TIER`

Audited functional head: `649c7673256734cf9acbbf3e75616ebf72d5b1e9`.
Authoritative workflow: `32726279718` (SUCCESS).
Final artifact: `stage32-15-e20-a0-le16384-exact-tier`, id `9520584453`, ZIP SHA256 `92d6f8ea549d3cf6df8522baad55e87d4ecb1395c6630d34e6148c39da892e11`.

## 1. Locked predecessor and exact delta

Stage32-15 does not silently recompute or weaken the audited Stage32-14 checkpoint. It downloads the exact Stage32-14 profile and predecessor artifact from workflow `32725113188`, verifies the predecessor canonical SHA

`88d3d7d12217626e8af80e3d6c3886b47a6416b498500de94bc1032c25407cb5`,

and verifies the e20/a0 profile canonical SHA

`e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5`.

From that profile it reconstructs the cumulative sets independently:

- predecessor `<=4096`: 16 cells / 48,790 branches;
- target `<=16384`: 69 cells / 655,558 branches;
- exact delta `4096 < branches/cell <=16384`: 53 cells / 606,768 branches.

The predecessor cell-key set is checked exactly against the profile, and the 53-cell delta is selected by predicate rather than by a hand-picked list.

## 2. Exact delta execution

Every delta cell is split into two exact global-branch-index modulo shards. The final aggregate requires exactly the 106 expected shard certificates, rejects duplicates/missing shards, checks certificate canonical hashes, checks exact modulo coverage, requires complete numerical enumeration, and requires `unknown_branch_count=0`.

Accepted delta result:

- 53/53 delta cells complete;
- 606,768/606,768 delta branches complete;
- 106/106 modulo shards represented;
- UNKNOWN = 0;
- numerical survivors = 0;
- all 53 delta cells UNSAT;
- delta search nodes = 258,424.

The solver, cap semantics and per-branch node limit remain the source-locked Stage32-08/11r exact path. Compact evidence is generated only after raw branch-row verification and preserves raw deterministic and branch-evidence-stream commitments.

## 3. Cumulative <=16384 tier

The final artifact combines the exact Stage32-14 predecessor with the exact Stage32-15 delta and independently checks that the resulting cell-key set equals *all* e20/a0 profile cells with materialized branch count at most 16,384.

Accepted cumulative result:

- 69/69 selected cells complete;
- 655,558/655,558 selected materialized branches;
- UNKNOWN = 0;
- numerical survivors = 0;
- all 69 selected cells UNSAT;
- total search nodes = 279,710.

Final cumulative canonical SHA256 was independently recomputed from the downloaded artifact and matches exactly:

`593bb0fc5231222ab9ce79ae0bd5802d77311d02fd633152d665f869b095611f`.

The downloaded ZIP SHA256 also matches the GitHub artifact digest exactly:

`92d6f8ea549d3cf6df8522baad55e87d4ecb1395c6630d34e6148c39da892e11`.

## 4. Scope firewall

This closes only the cumulative e20/a0 numerical tier `materialized branches/cell <= 16384`.

It does **not** close the e20/a0 parent. The exact profile still contains 1,182 cells total, so 1,113 cells remain outside the audited tier. It does not prove effectivity, actual curve existence, the full d=8,g=0 row, the d<=176/d<=192 census, receiver discharge, or any perfect-cuboid existence/nonexistence statement.

The next declared profile wall is `<=65536`: 301 cumulative cells / 6,834,114 cumulative branches, i.e. a further delta of 232 cells / 6,178,556 branches. That is a new execution-design boundary and receives no automatic credit from this audit.

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

## 5. Stacked-branch controller handling

PR #1372 branched before the audited Stage32-14 controller promotion reached main. Its branch-local `stages/stage32/controller.json` is therefore stale but is not part of the PR diff. The audit deliberately does not modify that stale controller inside #1372.

Controller promotion and these audit records are isolated on a main-based controller/audit branch. Intended merge order is **#1372 first, then the controller/audit synchronization PR**. This prevents Stage32-15 from overwriting the already-audited Stage32-14 controller state and avoids retriggering the expensive Stage32-15 workflow merely by writing audit files into the stacked execution branch.
