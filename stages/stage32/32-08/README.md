# Stage32-08 — high-mass signature-cell Class-2 attack

Stage32-07 closed the audited numerical orbit slice `(d,g,e)=(8,0,2)` but exposed the higher-mass signature-cell wall. This unit tests exact parent-preserving symmetry and then pivots to a lattice-aware materialized-cell backend where symmetry alone does not solve the wall.

## Exact symmetry used here

The source-locked nine geometric generators of `Aut(S)` close to order `1536` on the 140 known classes. The artificial Stage32 parent coordinate

```text
a = sum_{i=1}^{46} (K_i . C)
```

is not preserved by the full group. Therefore full-Aut canonicality is **not** legal inside one fixed `(e,a)` parent.

Instead Stage32-08 independently closes the subgroup

```text
H_a = { g in Aut(S) : g preserves {K_1,...,K_46} setwise }.
```

For the locked action its exact order is `64`. The full Aut action preserves the 48 exceptional divisors, hence `H_a` acts on the selected exceptional intersection coordinates by a permutation. The benchmark imposes lexicographic minimality of the 48-vector under every element of `H_a`.

This symmetry-breaking is exact **for the union of all signature cells in one fixed `(d,g,e,a)` parent**. A group element may move a class from one signature cell to another, so an individual symmetry-reduced cell becoming UNSAT is not interpreted as original-cell emptiness. Parent closure is legal only if every signature cell has been searched under the same global canonicality rule and no canonical survivor remains.

## Paired deterministic A/B result

Workflow run `32676167623` benchmarked the same first 16 immutable cells in each hard parent, with seed 0, one thread and a 3-second per-cell limit.

```text
parent      mode                 UNKNOWN  UNSAT  solver seconds
----------------------------------------------------------------
e8/a36      baseline                 15      1       47.603500
e8/a36      H_a symmetry             10      6       37.976102

e10/a30     baseline                 13      3       41.704205
e10/a30     H_a symmetry             13      3       86.878605
```

Verdict:

- `e8/a36`: exact symmetry is useful as a reducer; UNKNOWN falls `15 -> 10` and runtime also falls.
- `e10/a30`: exact symmetry does **not** improve the solved-cell count and roughly doubles runtime.
- Therefore symmetry is **not** promoted as the general higher-mass solver. In particular, do not run the full `e10/a30` parent merely with longer SMT timeouts or the same 63 lex constraints.
- A full-parent symmetry pass for `e8/a36` may be used later as a reducer/checkpoint, but the 16-cell benchmark itself has no closure credit.

## Exact materialized-cell backend

The successor materializes the exact exceptional assignment set represented by one immutable signature cell and all bounded q-head assignments. This fixes the first 52 selected intersection coordinates. The resulting exact integral affine lattice has kernel dimension `12`; the remaining q-tail is exhausted inside the negative-definite Picard slice with all 140 lower/upper intersection caps active.

The fixed-52 construction also rechecks the exact parent identities for degree, exceptional mass, `a`-mass and total normal mass. No congruence-only or floating-point acceptance is used.

Representative final-head workflow evidence:

```text
functional head = aa10009fa43aeaeaf6f89e234831f89e74db5e9a

e8/a36 cell 0451bcae...
  complete materialization : 1 branch
  qtail kernel dimension   : 12
  search nodes             : 38
  result                   : SAT_WITNESS

e10/a30 cell 02066d9e...
  complete materialization : 16 branches
  qtail kernel dimension   : 12
  search nodes total       : 40
  result                   : exact UNSAT for this signature cell
```

The e8 witness is a **numerical Picard class only**:

```text
degree                    = 8
self-intersection         = 0
exceptional mass          = 8
a-mass                    = 36
normal intersections      = 28x0, 16x1, 48x2
exceptional intersections = 40x0, 8x1
known-140 exact match      = none
```

Its independently verified full `Aut(S)` orbit has size `6` and stabilizer order `256`, with artificial-parent distribution `a=36` (5) and `a=32` (1). This is not effectivity or actual-curve evidence.

## Exact materialization-cost profile

The exact branch cost of a signature cell is

```text
branches(cell)
 = left_assignment_count
 * right_assignment_count
 * qhead_assignment_count(t).
```

Final audited profiles:

```text
e8/a36: 53 cells, 95,973 exceptional assignments
  <=1     :  1 cells /    1 branches
  <=4     :  5 cells /   17 branches
  <=64    : 21 cells /  701 branches
  <=256   : 24 cells / 1161 branches
  <=1024  : 30 cells / 6038 branches
  profile SHA = 97608b176d7a91677f63cd293502f7042a9a9f6ad30904631260c9d560b7be17

e10/a30: 134 cells, 703,688 exceptional assignments
  <=16    : 14 cells /  156 branches
  <=64    : 58 cells / 2140 branches
  <=256   : 64 cells / 3344 branches
  <=1024  : 88 cells / 16232 branches
  profile SHA = 993d0005f60499b50b03b899153b60f93de757a74f53d942e5a2168830cc5123
```

These are cost profiles only. A threshold tier is exact only after every selected cell and every scheduled materialized branch has completed without UNKNOWN.

## Audited exact low-cost tiers

Hostile audit of PR `#1354` accepts the following bounded numerical tiers.

First locked tier:

```text
e8/a36 <=4 branches/cell
  selected cells : 5/53
  exact branches : 17
  UNKNOWN        : 0
  UNSAT cells    : 2
  SAT cells      : 3
  exact numerical survivors : 17
  deterministic SHA : b14f7e70ea962fe00bb8bbe6e459090a1c166414070fa5a875673dc31e22268d

e10/a30 <=16 branches/cell
  selected cells : 14/134
  exact branches : 156
  UNKNOWN        : 0
  UNSAT cells    : 14
  numerical survivors : 0
  deterministic SHA : 8a4609ff2a34e903a9d2314a8df863c860ba68b3b9b4e101d18807b036b87437
```

The 17 e8 survivors partition exactly into two pairwise-disjoint full `Aut(S)` numerical orbits:

```text
input survivors  full orbit  C^2   stabilizer  a-distribution
----------------------------------------------------------------
1                6            0      256         {32:1, 36:5}
16               192         -4        8         {34:64, 36:128}
```

Aut partition verifier SHA:
`eedee71a6becd97d3dced086379ac57d98dabcbb8e669f01deebb0688836c7af`.

Expanded exact `<=64` tier:

```text
e8/a36 <=64
  selected cells : 21/53
  exact branches : 701
  complete cells : 21
  UNSAT cells    : 16
  SAT cells      : 5
  exact numerical survivors : 33
  UNKNOWN        : 0
  deterministic SHA : a58a6589633ef76a08bba420efabbd52d1b56c28eaaaa131c4ebb336666f13b0

e10/a30 <=64
  selected cells : 58/134
  exact branches : 2140
  complete cells : 58
  UNSAT cells    : 58
  SAT cells      : 0
  numerical survivors : 0
  UNKNOWN        : 0
  deterministic SHA : 383f2a2aa202aad1384ada1ef41041d0c731445e1ea7baff0ea895e91117a0e9
```

The hostile audit independently re-read the final-head artifacts, recomputed their canonical hashes, checked that the tier-selected cell IDs/indices are exactly the profile cells with materialized branch cost `<=64`, and checked branch/count/UNKNOWN/survivor accounting. The 33 e8 survivors are **not** promoted here to a new full-orbit classification beyond the independently verified 17-survivor locked tier.

## Audited scope and next Class-2 leaf

Stage32-08 is accepted as an exact bounded **numerical infrastructure checkpoint**, not as a complete parent, degree row, low-genus census, effectivity result or Stage29 receiver discharge.

The next legal continuation remains inside `32-01`: expand the exact high-mass materialized tiers in cost order and/or add another independently complete reducer, preserving immutable-cell inventories and exact branch coverage. The profile shows `<=256` as the next natural bounded tier, but no threshold receives credit until it is fully executed and audited.

Do not infer parent coverage percentages from selected-cell counts alone: the tier is defined by immutable signature cells satisfying the declared branch-cost threshold, not by a probabilistic sample of exceptional assignments.

## Firewalls

```text
THEOREM_CREDIT=false
AUDIT_STATUS=PASS_AFTER_CONTROLLER_AND_REPO_LOCAL_EVIDENCE_REPAIR
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

This unit is Class-2 numerical infrastructure only.
