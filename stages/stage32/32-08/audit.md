# Stage32-08 hostile audit — high-mass materialized tiers

## Verdict

```text
AUDITED_PR=1354
AUDITED_FUNCTIONAL_HEAD=aa10009fa43aeaeaf6f89e234831f89e74db5e9a
AUDIT_VERDICT=PASS_AFTER_CONTROLLER_AND_REPO_LOCAL_EVIDENCE_REPAIR
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
```

The numerical/computational claims on the submitted functional head pass hostile audit at their declared bounded scope. Two repository-state defects were repaired before merge: `32-08/README.md` only documented the early symmetry/coset pilot rather than the later exact materialized tiers, and `stages/stage32/controller.json` was still frozen at the much older 32-01 polytail/graded-slice state. These were evidence/handoff defects, not mathematical defects in the accepted bounded computations.

## 1. Final-head workflow evidence

The audited functional head is

```text
aa10009fa43aeaeaf6f89e234831f89e74db5e9a
```

The relevant PR-triggered Stage32 workflows on that head all completed successfully, including:

```text
32682503822  affine-coset hard-cell pilot                     SUCCESS
32682503823  exhaustive low-branch parent tiers              SUCCESS
32682503826  e8 cell0 exhaustive numerical census            SUCCESS
32682503832  materialization schedule profile                SUCCESS
32682503840  verify e8 numerical Aut orbit                   SUCCESS
32682503844  cached materialized regression                  SUCCESS
32682503855  high-mass symmetry-cell benchmark               SUCCESS
32682503865  verify e8 low-tier Aut orbit partition          SUCCESS
32682503893  materialized signature-cell qtail pilot         SUCCESS
32682503895  exact <=64-branch parent tiers                  SUCCESS
```

The Stage32-07 bounded-signature regression also succeeded on this head. Green workflow state alone was not treated as proof; the audit independently inspected the generated artifacts and code paths below.

## 2. Signature-cell and materialization semantics

The accepted Stage32-07 predecessor already source-locks the rank-64 Picard representation, the exact degree-8 caps

```text
92 nonexceptional coordinates : 0..4
48 exceptional coordinates    : 0..2
```

and the exact bounded-multiplicity signature-cell compression.

Stage32-08 does not infer an individual cell to be empty from parent-preserving symmetry. The `H_a` symmetry benchmark is only a reducer and correctly records that full `Aut(S)` does not preserve the artificial fixed-parent coordinate `a`.

The materialized successor is exact at the branch level:

1. each signature cell's left/right exceptional assignments are reconstructed from the exact mod-8 signature and bounded multiplicity counts;
2. the left and right column sets are disjoint, and the implementation asserts that combining them produces exactly the Cartesian-product number of exceptional vectors;
3. all bounded q-head assignments with the required total are materialized;
4. the 48 exceptional plus 4 q-head coordinates fix the first 52 selected coordinates;
5. the fixed equations plus redundant exact parent locks have independent rank 52 in the 64-dimensional Picard basis, leaving an exact integral kernel of dimension 12;
6. each branch is searched in that 12D negative-definite slice with exact rational LDL data and all 140 lower/upper caps active;
7. node-budget exhaustion is represented as UNKNOWN and receives no UNSAT credit.

The exhaustive production path does not stop on the first witness: `run_materialized_cell_exhaustive.py` enumerates every lattice point satisfying the completed square bound for a branch unless the explicit node budget is exhausted, rechecks the original 140 intersections, degree/mass identities, signature, and cell multiplicity identities at every retained leaf, and returns `SAT_EXHAUSTED`, `UNSAT`, or `UNKNOWN_NODE_BUDGET` accordingly.

## 3. Independent artifact/hash checks

The audit downloaded the final-head profile and tier artifacts and recomputed the canonical JSON hashes rather than trusting the embedded hash fields.

Verified profile hashes:

```text
e8/a36  97608b176d7a91677f63cd293502f7042a9a9f6ad30904631260c9d560b7be17
e10/a30 993d0005f60499b50b03b899153b60f93de757a74f53d942e5a2168830cc5123
```

Verified tier hashes:

```text
e8/a36 <=4   b14f7e70ea962fe00bb8bbe6e459090a1c166414070fa5a875673dc31e22268d
e8/a36 <=64  a58a6589633ef76a08bba420efabbd52d1b56c28eaaaa131c4ebb336666f13b0
e10/a30 <=64 383f2a2aa202aad1384ada1ef41041d0c731445e1ea7baff0ea895e91117a0e9
```

Verified independent Aut-partition hash:

```text
eedee71a6becd97d3dced086379ac57d98dabcbb8e669f01deebb0688836c7af
```

For both `<=64` tiers, the audit independently selected from the profile exactly the cells with

```text
materialized_branch_count <= 64
```

and compared their ordered immutable cell IDs and indices with the production tier artifacts. They match exactly.

The complete checked accounting is:

```text
e8/a36 <=64:
  profile cells                    = 53
  selected cells                   = 21
  scheduled/executed branches      = 701 / 701
  final qtail kernel dimension     = 12 on every branch
  complete cells                   = 21
  UNSAT cells                      = 16
  SAT_EXHAUSTED cells              = 5
  exact numerical survivors        = 33
  UNKNOWN cells                    = 0
  node-budget-exhausted branches   = 0

e10/a30 <=64:
  profile cells                    = 134
  selected cells                   = 58
  scheduled/executed branches      = 2140 / 2140
  final qtail kernel dimension     = 12 on every branch
  complete cells                   = 58
  UNSAT cells                      = 58
  SAT cells                        = 0
  exact numerical survivors        = 0
  UNKNOWN cells                    = 0
  node-budget-exhausted branches   = 0
```

Thus all `2841` scheduled branches in the accepted `<=64` tiers are accounted for without UNKNOWN.

## 4. Locked 17-survivor Aut(S) partition

The exact `e8/a36 <=4` tier has 17 numerical survivors. The independent verifier does not infer the group from those survivors. It source-locks the same upstream nine geometric generators used by the accepted Stage32-07 audit, rechecks their action on the 140 known classes, and independently closes the permutation group to order `1536`.

The 140-intersection representation is injective on Picard classes through the selected 64-row matrix of determinant

```text
2^38 = 274877906944.
```

The 17 inputs partition into exactly two pairwise-disjoint full numerical `Aut(S)` orbits:

```text
input survivors  full orbit  C^2   stabilizer  a-distribution
----------------------------------------------------------------
1                6            0      256         {32:1, 36:5}
16               192         -4        8         {34:64, 36:128}
```

Every recovered orbit member is an integral Picard class, has degree 8 and exceptional mass 8, satisfies the audited numerical caps, and is distinct from the frozen known 140 classes.

This is **numerical Picard-orbit classification only**. No effectivity or actual-curve conclusion is promoted.

The larger `e8/a36 <=64` tier contains 33 numerical survivors. Stage32-08 does not promote those 33 to a complete new orbit inventory; that remains legal future bookkeeping if useful.

## 5. Scope/firewall audit

The submitted firewalls are mathematically necessary and pass audit:

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

In particular:

- selected-cell tier completeness is not parent completeness;
- a cell count fraction is not a density theorem or a probability statement about exceptional assignments;
- numerical Picard classes are not effective curves;
- the degree-8 row is still incomplete;
- the frozen `d<=176/192` numerical census is still incomplete;
- effectivity and multibranch receivers remain open.

## 6. Bounded repository-state repair

Two nonmathematical defects were material for reproducibility/handoff:

1. `stages/stage32/32-08/README.md` stopped at the initial symmetry/coset successor plan and omitted the later materialized backend, exact profile/tier hashes and accepted bounded results.
2. `stages/stage32/controller.json` still reported the old 32-01 polytail/graded-slice state and did not know that Stage32-07 was audited or that Stage32-08 was awaiting hostile audit.

The audit repairs those records only. No Stage32-08 computational script, theorem adapter, numerical survivor set, branch result, or orbit calculation is changed by the audit.

## 7. Next legal state

Stage32 remains inside roadmap unit `32-01`; there is no roadmap-unit closure yet.

```text
32_01_COMPLETE=false
CURRENT_ACCEPTED_CHECKPOINT=D8_HIGHMASS_MATERIALIZED_EXACT_TIERS_LE64
SMALLER_CLASS2_LEAF=L32-01-D8-HIGHMASS-MATERIALIZED-TIER-EXPANSION
AUDIT_REQUIRED=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=32-01-D8-HIGHMASS-MATERIALIZED-TIER-EXPANSION
NEXT_EXPECTED_COMMAND=Stage32-main-batch
```

The profile makes `<=256` a natural next bounded expansion, but this is an execution priority rather than mathematical credit. Full parent expansion, effectivity, higher degree and the complete Stage29 receiver remain outside this audit.
