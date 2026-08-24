# Stage32-13 hostile audit — PR #1367

Verdict: `PASS_COMPLETE_E10_A30_PARENT_AND_FULL_AUT_NUMERICAL_ORBIT_CENSUS`

Audited functional head: `d0cd94aebff5b5f1f5c3ae599226ce7f898144cc`.
Successful authoritative workflow: `32706948355`, attempt 2.
Final artifact: `stage32-13-e10-a30-full-parent-aut-orbit-census`, id `9517128001`, ZIP SHA256 `17318d4757a7978aedd2e7a41d6982e9111cfce0de8b03855bc59de4177431fc`.

## 1. Cancelled run receives no credit

The first Stage32-13 execution `32702148657` was manually cancelled for artifact-storage safety. It is not used in any closure inference. The accepted run recomputes all four giant cells from the frozen Stage32-08/11r solver path.

## 2. Compact evidence is post-verification only

Each shard first materializes the full raw exact branch report. `compact_shard_certificate.py` then verifies the exact global-index modulo partition, branch-by-branch completion, `enumeration_exhausted=true`, `node_budget_exhausted=false`, branch-derived/top-level survivor equality, survivor uniqueness, and all receiver/theorem firewalls before raw rows are deleted. The compact certificate commits both the deterministic raw-report SHA and a canonical per-branch evidence-stream SHA. Thus compaction changes persistence only; it does not change the search or replace UNKNOWN branches by summaries.

## 3. Exact giant-tail result

The accepted aggregate independently verifies all 48 shards and exact disjoint/full coverage:

- cell 43 `42ee1ca9ffc49798d5c927a6`: 1,095,920 branches, UNSAT, 0 survivors, 1,013,336 search nodes;
- cell 64 `65bd86aef2d39bf5e13aa268`: 1,179,360 branches, SAT_EXHAUSTED, 32 survivors, 1,181,816 nodes;
- cell 100 `cb01d3f2aed50c00b72d69e9`: 2,534,560 branches, UNSAT, 0 survivors, 2,433,848 nodes;
- cell 108 `d6c2af90f25f4a5940eb3dd1`: 2,596,160 branches, SAT_EXHAUSTED, 64 survivors, 2,558,184 nodes.

Total giant tail: 7,406,000 branches, 96 numerical survivors, 7,187,184 nodes, UNKNOWN=0.
Canonical giant-tail SHA256 independently recomputed: `c6fb1e742619e6027d3fdd5d85736608a54b5fbcce144b6089e82fbce9dc0918`.

## 4. Exact e10/a30 parent reconstruction

The parent assembler consumes four disjoint frozen evidence blocks: Stage32-10 <=4096 tier (102 cells), Stage32-11 direct tail (26 cells), Stage32-11r timeout repair (2 cells), and Stage32-13 giant tail (4 cells). The union is exactly 134/134 immutable signature cells and exactly 11,205,888/11,205,888 materialized branches.

Exact result:

- 126 UNSAT cells;
- 8 SAT_EXHAUSTED cells;
- 192 distinct numerical survivors;
- every survivor has `C^2=-10`;
- UNKNOWN=0.

Parent inventory SHA256: `c2e028af43afda9cce1e82139c09ba56be72c087b5d957b40e8bda70e3a96afd`.
Parent canonical SHA256 independently recomputed: `8dec6825542e80f7c6568506e8fb7773599faa48158811cb105d8b829b69340d`.

## 5. Independent Aut(S) orbit partition

The source-locked nine automorphism generators preserve the hyperplane class and all 140 pairings and close to order 1536. The 64-row recovery matrix has determinant `274877906944=2^38`, so intersection images recover uniquely to integral Picard-basis vectors.

The 192 a=30 survivors partition into exactly two pairwise-disjoint full numerical Aut(S) orbits. Each has:

- full orbit size 192;
- stabilizer order 8;
- 96 members returning to the a=30 slice;
- full a-distribution `{28:64,29:32,30:96}`.

The two full orbits have union size 384. Every a=30 orbit member is present in the completed parent, every recovered orbit image is an integral Picard class, and none is one of the frozen known 140 classes.

Orbit canonical SHA256 independently recomputed: `fa83bd1bfb627b8c94f63810adaf89460dc60a843f6f353bd1f95f6941c01292`.

## 6. Functional-head and current-head boundary

The mathematical run is source-locked at `d0cd94a...`. The four commits after that head through pre-audit PR head `dcb1a9eb...` modify only repository operating-policy documentation and do not change Stage32 solver, workflow, evidence, source locks, or mathematical code. They do not invalidate the successful run.

## 7. Credit firewall

Accepted result is exactly the complete e10/a30 numerical parent and its full Aut(S) numerical orbit partition. It does not prove effectivity, actual curve existence, the full d=8,g=0 row, the d<=176/d<=192 census, or receiver discharge.

The following remain false/open:

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

Stage32-01 remains in progress under the roadmap close criterion requiring every even degree in the G0/G1 windows. The next production command remains `Stage32-main-batch`; it must continue from this newly audited e10/a30 parent checkpoint rather than treating this internal sub-parent as completion of the 183-row numerical census.