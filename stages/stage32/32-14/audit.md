# Stage32-14 hostile audit — PR #1371

Verdict: `PASS_EXACT_E20_A0_PROFILE_AND_CUMULATIVE_LE4096_ZERO_TIER`

Audited functional head: `1595112d16a8cefdff0469e19c2b3ba7afaef30c`.
Authoritative workflow: `32725113188` SUCCESS.
Final artifact: `stage32-14-e20-a0-storage-safe-exact-tier`, id `9519460554`, ZIP SHA256 `347eb49158a3c8914dcfe1f2cf30afb47426e6583cd5b7d02d79759964256e3c`.

## 1. Exact compressed e20/a0 parent profile

The source-locked Stage32-08 materialization profiler was rerun from the frozen Picard core after re-deriving all 140 exact dual caps. The profile log gives exactly:

- signature cells: 1,182;
- exceptional assignments after qtail quotient: 1,032,477,716;
- qhead-inclusive total materialized branches: 7,806,762,328;
- minimum cell branch count: 1,094;
- maximum cell branch count: 920,344,320;
- profile canonical SHA256: `e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5`.

The billion-state parent was not globally materialized. This is an exact compressed scheduling/profile count, not a claim that 7.8 billion candidate curves were explicitly enumerated.

Cumulative profile landmarks are:

- <=1,024: 0 cells;
- <=4,096: 16 cells, 48,790 scheduled materialized branches;
- <=16,384: 69 cells, 655,558 branches;
- <=65,536: 301 cells, 6,834,114 branches.

Under the predeclared threshold ladder and hard envelope (<=24 cells, <=1,000,000 total branches, <=65,536 branches/cell), <=4,096 is the largest admissible cumulative tier. The next declared threshold <=16,384 fails the 24-cell gate. This is an execution-envelope boundary, not a mathematical impossibility theorem.

## 2. Storage-safe evidence gate

The representative pilot shard completed exact enumeration before fanout. Post-verification compaction produced a 1,281-byte compact artifact, below the fixed 100,000-byte gate.

The selected tier has exactly 16 cells x 2 modulo shards = 32 compact shard artifacts. Raw branch rows were verified on-runner, committed by deterministic/evidence-stream hashes, deleted before upload, and never used as persistent Actions artifacts. The selected-tier shard storage upper bound was fixed before compute at 3.2 MB (4.8 MB absolute envelope).

## 3. Exact cumulative <=4096 tier

The final aggregate was independently downloaded and rehashed during hostile audit. Its canonical SHA256 reproduces exactly:

`88d3d7d12217626e8af80e3d6c3886b47a6416b498500de94bc1032c25407cb5`.

Accepted exact result:

- chosen cumulative threshold: 4,096;
- selected cells: 16/16;
- selected materialized branches: 48,790/48,790;
- exact modulo shards: 32/32;
- total exact search nodes: 21,286;
- numerical survivors: 0;
- UNKNOWN branches: 0;
- all 16 selected cells: UNSAT.

The exact selected cell branch counts sum to 48,790 and every cell is individually complete under the unchanged Stage32-11r / Stage32-08 exhaustive solver with the same 1,000,000 node budget per branch.

## 4. Scope firewall

This audit closes only the cumulative `e20/a0` signature-cell tier with materialized branch count <=4,096. It does not close the remaining 1,166 e20/a0 cells, the e20/a0 parent, the d8/g0 row, the full d<=176/d<=192 numerical census, effectivity, the multibranch ledger, or any Stage29 receiver.

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
`STAGE32_CLOSED=false`
`STAGE32_01_COMPLETE=false`

The next exact Class-2 production target is to widen/repartition the e20/a0 cumulative tier from the audited <=4,096 checkpoint while preserving the storage/execution firewalls. No theorem or perfect-cuboid existence/nonexistence credit is authorized.
