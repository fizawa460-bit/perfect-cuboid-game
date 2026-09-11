# Stage32 MB102 — local branch / delta / genus correction ledger

Status: **RETAINED CHECKPOINT / NO RECEIVER CREDIT**

## Input

MB101 fixes the exact nodewise branch profile. For each box node `i`, the strict transform `D` on the smooth resolution has normalization branches with FSM data `(A_ij,B_ij)`, exceptional multiplicities `m_ij=min(A_ij,B_ij)`, and resolved landing points on `E_i`.

MB102 adds exactly the singularity data needed to pass from that normalization profile to genus accounting. It does not infer delta from exceptional mass or branch count.

## Resolved-point local ledger

Fix a resolved point `P` of `D` lying on an exceptional curve. Let the reduced local branches of `D` through `P` be

```text
beta_1,...,beta_s.
```

On the smooth surface `S`, the standard reduced plane-curve delta decomposition is

```text
delta_P(D)
  = sum_a delta(beta_a)
    + sum_{a<b} I_P(beta_a,beta_b).
```

Thus the exact exceptional-locus contribution is

```text
Delta_exc
  = sum_{P in D cap (union_i E_i)} delta_P(D).
```

Branches landing at different resolved points have no pairwise local intersection term at the exceptional locus. In particular, the MB101 minimal `(A,B)=(1,1)` branches with pairwise distinct `lambda` values may contribute zero exceptional-locus delta even when they came from the same singular box node.

Consequently none of the following identities is valid without extra data:

```text
Delta_exc = M,
Delta_exc = R,
Delta_exc = R-N,
delta at node i = M_i-r_i,
delta at node i = choose(r_i,2).
```

The exact ledger must retain, for every resolved landing point:

1. the list of MB101 branch ids landing there;
2. each intrinsic branch delta `delta(beta_a)`;
3. each pairwise intersection multiplicity `I_P(beta_a,beta_b)`.

## Off-exceptional singularities

Let

```text
Delta_off = sum_{P in Sing(D), P notin union_i E_i} delta_P(D).
```

Then

```text
Delta_total = Delta_exc + Delta_off.
```

MB101 node data places no a priori upper bound on `Delta_off`. The retained V6 feasibility wall gives an explicit example of this separation: the complete exceptional profile can be locally compatible with zero exceptional-locus delta while the remaining genus defect is placed at a smooth ambient point away from the exceptional curves.

## Global genus correction

The resolved surface satisfies `H=K_S`. For the strict transform `D`, write

```text
d = H.D,
g = genus(normalization(D)).
```

Adjunction on the smooth surface gives

```text
p_a(D) = 1 + (D^2 + d)/2.
```

For a reduced integral curve,

```text
p_a(D) - g = Delta_total.
```

Therefore the exact global correction identity is

```text
D^2 + d = 2g - 2 + 2*Delta_total.
```

For the Stage32 low-genus receiver:

```text
g=0: D^2 = -d - 2 + 2*Delta_total,
g=1: D^2 = -d     + 2*Delta_total.
```

This identity is exact, but by itself it is not a degree bound: `Delta_total` is nonnegative and may grow. MB104 therefore still needs an independent population-wide restriction coupling degree/intersection data to the multibranch profile.

## Nodewise bookkeeping contract

For each box node `i`, retain

```text
r_i  = number of normalization branches,
M_i  = sum_j m_ij,
L_i  = partition of those branches by resolved landing point,
Delta_i_exc = sum_{P in L_i} [sum intrinsic deltas + sum pairwise intersections].
```

The exact global bookkeeping is

```text
R = sum_i r_i,
M = sum_i M_i,
Delta_exc = sum_i Delta_i_exc,
Delta_total = Delta_exc + Delta_off.
```

Only `r_i`, `M_i`, and `L_i` are supplied by the MB101 profile. The delta entries are new MB102 data and cannot be synthesized from the counts alone.

## Decision

```text
MB102_LOCAL_DELTA_LEDGER=RETAINED
MB102_GLOBAL_GENUS_CORRECTION=RETAINED
DELTA_INFERRED_FROM_EXCEPTIONAL_MASS=false
DELTA_INFERRED_FROM_BRANCH_COUNT=false
OFF_EXCEPTIONAL_DELTA_FORCED_ZERO=false
FINITE_DEGREE_WINDOW_PROVED=false
FINITE_PICARD_ENUMERATION_RELEASED=false
R29_LG2_MB_DISCHARGED=false
RECEIVER_CREDIT=false
NEXT_NODE=MB103
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
MERGE_AUTHORIZED=false
```

## Source locks

- MB101 certificate, blob `282fc94d8d5feb0221cf6bf096ed4b0030883563`.
- `stages/stage29/29-02c-LG2/result.md`, blob `820ed4e1b1a53db14085678de6f186b59ae0ea48` — `H=K_S`, adjunction setup, and low-genus receiver semantics.
- `stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`, blob `512fcc70afb1acf16956fd4b7a2b9b935a052150` — standard delta decomposition, exact branch landing adapter, and explicit exceptional/off-exceptional separation wall.
