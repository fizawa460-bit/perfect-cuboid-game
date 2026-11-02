# Stage32 MB101 — exact multibranch population / normalization-profile adapter

Status: **RETAINED CHECKPOINT / NO RECEIVER CREDIT**

## Scope

This node instantiates the first load-bearing `R29-LG2-MB` object without importing the Freitag--Salvati Manni unibranch degree cap. It only fixes the population semantics and the exact nodewise normalization profile needed by MB102--MB104.

Let `X` be the singular box surface, `pi:S->X` its minimal resolution, and `E_i` (`i=0,...,47`) the exceptional curves over the 48 box nodes. Let `C subset X` be a nonexceptional integral low-genus carrier and `D subset S` its strict transform. The normalization of `D` is also the normalization object used for `C` under the birational strict-transform map.

`R29-LG2-MB` means the part of the low-genus carrier population outside the **bijective-normalization** hypothesis because at least one box node has at least two normalization branches. No degree upper bound is asserted here.

## Exact branch record at one box node

For every normalization branch of `C` through a box node, retain the FSM cusp exponents

```text
A=a1/4 > 0,
B=a2/4 > 0,
A+B even.
```

The source-locked A1-resolution adapter gives, on the resolved surface,

```text
m = min(A,B),
```

where `m` is the intersection multiplicity of that strict-transform branch with the exceptional curve.

The landing semantics are also exact:

- `A<B`: the branch lands at the distinguished point on the `x`-chart;
- `A>B`: symmetrically it lands at the distinguished point on the `z`-chart;
- `A=B`: it lands at a nonzero exceptional coordinate `lambda` determined by the leading unit ratio.

The exponents alone do not identify two `A=B` branches: distinct `lambda` values give distinct resolved landing points.

## Exact node profile

For node `i`, let the normalization branches be `b_(i,1),...,b_(i,r_i)`. For each branch retain `(A_ij,B_ij,m_ij,landing_kind,landing_key)` with

```text
m_ij = min(A_ij,B_ij) >= 1.
```

Define the node exceptional contact mass

```text
M_i = D.E_i = sum_j m_ij.
```

Hence, whenever `M_i>0`,

```text
1 <= r_i <= M_i.
```

Moreover:

```text
node i is multibranch  <=>  r_i >= 2,
normalization-preimage count over node i = r_i,
exceptional contact mass at node i = M_i.
```

These quantities are not interchangeable. Equality `r_i=M_i` holds exactly when every branch has `m_ij=1`.

For the full 48-node profile, define

```text
R = sum_i r_i,
M = sum_i M_i,
N = #{i : r_i>0},
N_MB = #{i : r_i>=2}.
```

Then the population-wide necessary identities/inequalities are

```text
N <= R <= M,
N_MB <= N,
R-N = sum_{i:r_i>0}(r_i-1).
```

The last quantity is the exact normalization branch-excess over the met node support. It is not a delta invariant.

## Delta / genus firewall for MB102

The node profile above intentionally does **not** assign local delta from `M_i`, `r_i`, or branch excess. Existing exact local evidence shows that several minimal `(A,B)=(1,1)` branches over one box node may have distinct `lambda` values and become pairwise disjoint after resolution, contributing no pairwise local delta there.

Therefore MB102 must retain the resolved landing partition and, at any resolved point supporting more than one branch or a singular branch, separately account for intrinsic branch delta and pairwise intersection multiplicities. The scalar genus-defect ledger may only be formed after that local adapter is explicit.

## Population adapter verdict

The exact MB101 record for a candidate is therefore:

```text
(g, d, D-class if known,
 node_profile[48] = multisets of branch records,
 R, M, N, N_MB)
```

with `N_MB>=1` for `R29-LG2-MB` and **no imported 176/192 cap**.

This is enough to distinguish the multibranch receiver from the unibranch finite-Picard receiver and to hand the exact local objects to MB102/MB103. It is not enough to start finite Picard enumeration or claim a finite degree window.

## Source locks

- `stages/stage29/29-02c-LG2/result.md`, blob `820ed4e1b1a53db14085678de6f186b59ae0ea48` — receiver split and multibranch firewall.
- `stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`, blob `512fcc70afb1acf16956fd4b7a2b9b935a052150` — exact branch exponents, A1 resolution, `m=min(A,B)`, landing semantics, and the delta-separation wall.
- `stages/stage32/final-chain/32-03-multibranch/PREFLIGHT.json`, blob `f625c14b665af668d9ce6b6e78d0b05a2a27bd27` — MB mission boundary and anti-loop contract.

## Decision

```text
MB101_EXACT_POPULATION_ADAPTER=RETAINED
MB101_NORMALIZATION_PROFILE_ADAPTER=RETAINED
UNIBRANCH_176_192_CAP_IMPORTED=false
NODE_PREIMAGE_COUNT_EQUALS_EXCEPTIONAL_MASS=false
NODE_BRANCH_EXCESS_EQUALS_DELTA=false
FINITE_DEGREE_WINDOW_PROVED=false
FINITE_PICARD_ENUMERATION_RELEASED=false
R29_LG2_MB_DISCHARGED=false
RECEIVER_CREDIT=false
NEXT_NODE=MB102
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
MERGE_AUTHORIZED=false
```
