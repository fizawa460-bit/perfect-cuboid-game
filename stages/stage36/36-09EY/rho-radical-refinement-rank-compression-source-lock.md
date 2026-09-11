# Stage36 36-09EY — radical-refinement leaf-core nullity compression

## Purpose

36-09EX enlarged the exact sufficient-template library from `T1..T9` to `T1..T17` by allowing controlled radical splitting. The new patterns have support sizes ranging up to `n=16`, so continuing by full pattern hashes would scale poorly. This leaf extracts the invariant that survives the splitting.

Entry authority is V282, exact head `fce8877acde317f1215c1804a9d93033209c8df0`, CI `34412114871 / 102668682937`.

## Exact leaf-core rank identity

Let `M` be any square Stage36 36-09EP support matrix of size `2n x 2n`. Apply the deterministic 36-09EQ leaf-pivot procedure. Each step chooses a current row or column containing exactly one `1` and deletes that pivot row and pivot column. After `k` legal leaf pivots, let the residual square matrix be `H`, of size

```text
m = 2n-k.
```

A leaf row can be permuted to the first row with its unique `1` in the first column; elementary row operations clear the rest of that column. Thus

```text
rank(M_current) = 1 + rank(M_next).
```

The same argument applies to a leaf column. Induction over the complete deterministic peel gives the exact identity

```text
rank_F2(M) = k + rank_F2(H).
```

By 36-09EP,

```text
dim_F2 Sel^2(E_rho,p/Q) = 2n - rank_F2(M).
```

Therefore

```text
dim_F2 Sel^2(E_rho,p/Q)
 = (2n-k) - rank_F2(H)
 = nullity_F2(H).
```

This is an equality, not only a sufficient criterion. In particular,

```text
Sel2_dim = 2  iff  nullity_F2(H)=2.
```

EQ is the special case `H=0_2`; ER is the case where a deficiency-two residual core contains a nonsingular minor of size `m-2`.

## Radical-refinement invariance

A useful corollary is exact leaf-extension invariance. If a controlled radical refinement enlarges the support matrix by pairs that are eliminated by legal leaf pivots before reaching the old residual core, the Selmer dimension is unchanged. The extra radical vertices contribute rank one per leaf pair and disappear from the residual nullity.

This does not say every factor split is harmless. A split that changes the residual core can change its nullity and must still be checked. The theorem identifies precisely where that dependence lives.

## Replay on the exact template library

Replay the deterministic EQ peel on the exact matrix representation used by the verifier: T1..T9 use their exact arithmetic representatives, while T10..T17 use the canonical 36-09ES abstract pattern matrices promoted by 36-09EX. In every case the residual core has nullity exactly two.

```text
id   n   leaf pivots k   residual size m   rank(H)   nullity(H)
T1   4        6               2              0          2
T2   6       10               2              0          2
T3   7       12               2              0          2
T4   7       12               2              0          2
T5   9       16               2              0          2
T6  10       12               8              6          2
T7  10       18               2              0          2
T8  10       18               2              0          2
T9  10       10              10              8          2
T10 14       26               2              0          2
T11 14       26               2              0          2
T12 12       15               9              7          2
T13 15       16              14             12          2
T14 14       26               2              0          2
T15 14       14              14             12          2
T16 12       15               9              7          2
T17 16       18              14             12          2
```

The V283 first attempt recorded the T17 peel on the raw arithmetic matrix as `k=17, m=15, rank(H)=13`. That raw replay is also correct and has the same nullity two, but it is not the canonical pattern representation used for T10..T17 by the retained verifier. V283R1 therefore source-locks the canonical T17 row above; no rank, Selmer, template, fixed-parameter, receiver, or endpoint claim changes.

Thus ten templates are leaf-only after compression (`H=0_2`), while seven retain a genuine core. All seventeen are described by the single exact condition `nullity(H)=2`; the hash labels are no longer mathematically load-bearing for rank once the labelled support matrix has been built.

## Consequence for the next search

Future controlled-radical searches need not compute or classify the full support rank first. They may:

1. build the exact labelled-radical support matrix;
2. perform deterministic leaf peeling;
3. evaluate only the residual core nullity;
4. accept a Sel2 candidate exactly when that nullity is two;
5. separately apply the EH no-4/no-3 conditions before fixed-p exclusion credit.

This is an exact reduction, not a heuristic filter.

The next leaf is

```text
36-09EZ_RHO_CORE_NULLITY_CONTROLLED_RADICAL_SEARCH_PREFLIGHT.
```

Its purpose is to use the nullity-two criterion to search broader controlled-radical refinements without accumulating new full-pattern hashes unless a genuinely new residual-core type appears.

## Credit firewall

This leaf adds no new fixed-p parameter by itself. It does not prove every radical refinement has nullity two, does not classify all possible residual cores, does not establish infinitely many hits or a uniform Sel2 theorem, does not shrink the parent candidate ledger, and does not prove receiver/R29/Q11/endpoint/Perfect Cuboid closure.
