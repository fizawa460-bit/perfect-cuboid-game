# Stage36 36-09EQ — Legendre graph leaf-pivot maximal-rank criterion

## Purpose

36-09EP proves that for every primitive positive parameter `p=a/b`, `a!=b`, the full-2 Selmer matrix for the rho quotient is determined exactly by the labelled radical Legendre datum

```text
R(a,b)=(S_P,S_Q,S_D; q mod 8; epsilon_2; pairwise Legendre symbols),
```

and that, with `n=1+|S_f|`,

```text
Sel2_dim=2
iff
rank_F2 M_R(R(a,b))=2n-2.
```

The present leaf extracts a purely graph-theoretic sufficient condition for the maximal rank `2n-2`. It uses no local point search, no valuation exponents, and no F2 Gaussian elimination as part of the criterion itself.

## Bipartite Legendre support graph

Let `M=M_R(R(a,b))` be the exact 0/1 matrix from 36-09EP. Define a bipartite graph

```text
B_R=(V_row disjoint_union V_col,E)
```

with one row vertex for each row of `M`, one column vertex for each ambient squareclass coordinate of `M`, and an edge `(r,c)` exactly when

```text
M[r,c]=1.
```

Because 36-09EP reconstructs `M` from `R(a,b)` alone, `B_R` is also determined by the labelled radical Legendre datum alone.

## Leaf-pivot operation

On an active induced row/column subgraph, a **leaf pivot** is either

1. a row vertex of degree one together with its unique adjacent column, or
2. a column vertex of degree one together with its unique adjacent row.

After choosing a leaf pivot `(r,c)`, delete both `r` and `c` and repeat on the remaining active graph.

A **deficiency-two complete leaf-pivot certificate** is a sequence of exactly

```text
2n-2
```

such pivots.

The certificate is finite and directly checkable from the Legendre graph.

## Maximal-rank theorem

Suppose `B_R` admits a deficiency-two complete leaf-pivot certificate

```text
(r_1,c_1),...,(r_{2n-2},c_{2n-2}).
```

Reverse the pivot order. At the moment `(r_i,c_i)` was removed, one endpoint had degree one in the active graph, so in the square submatrix selected by the pivoted rows and columns the corresponding pivot entry is `1` and has no competing active entry in that row or column.

Repeated Laplace expansion along these leaf pivots gives

```text
det_F2 M[pivot_rows,pivot_cols]=1.
```

Hence

```text
rank_F2 M >= 2n-2.
```

But the rational full 2-torsion already forces

```text
dim Sel^2(E_rho,p/Q) >= 2,
```

so the 36-09EP dimension formula gives the universal upper bound

```text
rank_F2 M <= 2n-2.
```

Therefore

```text
rank_F2 M = 2n-2
```

and consequently

```text
Sel2_dim=2.
```

Thus the leaf-pivot condition is an exact sufficient arithmetic condition for the Selmer condition used by 36-09EH.

## Deterministic certificate convention

The verifier uses the following deterministic peeling rule only to make certificates reproducible:

1. scan active rows in canonical order and take the first degree-one row if one exists;
2. otherwise scan active columns in canonical order and take the first degree-one column;
3. delete the chosen row and column;
4. repeat.

The theorem itself only requires existence of a valid leaf-pivot sequence. The deterministic rule is a concrete sufficient subcriterion and is what is replayed below.

## Exact EO 50-box replay

On all `1546` ordered primitive rows with

```text
1<=a,b<=50,
gcd(a,b)=1,
a!=b,
```

the deterministic leaf-pivot rule reaches `2n-2` pivots on exactly `20` rows. Every one of those rows has exact `Sel2_dim=2`, and there are no false positives.

The 20 certified rows are

```text
(1,2),(1,3),(1,5),
(2,1),(2,3),(2,7),(2,9),
(3,1),(3,2),
(5,1),(5,9),
(6,43),
(7,2),(7,11),
(9,2),(9,5),
(11,7),
(37,49),(43,6),(49,37).
```

They are exactly five of the six dimension-two literal/rho orbits already identified by 36-09EO:

```text
O(2),
O(1/5),
O(2/7),
O(2/9),
O(6/43).
```

Thus five of the six known maximal-rank orbits can now be recognized without Gaussian elimination: a graph peeling certificate suffices.

## Exact obstruction to necessity

The remaining dimension-two orbit

```text
O(3/47)={3/47,22/25,25/22,47/3}
```

is an exact counterexample to necessity of leaf-peelability.

All four rows have

```text
n=10,
rank M_R=18=2n-2,
Sel2_dim=2,
```

but the deterministic leaf peeling stops early:

```text
(3,47):  12 pivots,
(22,25): 12 pivots,
(25,22): 10 pivots,
(47,3):  10 pivots.
```

For `(3,47)` and `(22,25)`, after 12 pivots the active residual is `8 x 8` with rank `6`; for `(25,22)` and `(47,3)`, after 10 pivots the active residual is `10 x 10` with rank `8`.

So the missing phenomenon is not another local Kummer formula. It is a cyclic Legendre-core parity phenomenon inside the already closed support graph.

This identifies the next exact leaf:

```text
36-09ER_RHO_LEGENDRE_CORE_PARITY_PREFLIGHT.
```

The intended task is to certify maximal rank on non-leaf-peelable cores by a small odd-minor / perfect-matching-parity condition, with `O(3/47)` as the first exact test case.

## Credit firewall

This leaf proves a sufficient graph criterion and diagnoses its exact non-necessity. It adds no fixed-p exclusion beyond the already exact 24-value EO registry.

The following remain false:

```text
uniform_Sel2_dimension_2_theorem,
candidate_parameter_set_shrunk,
receiver_emptiness_proved,
R29_CAMP2_closed,
Q11_CAMPEDELLI_closed,
endpoint_closed,
perfect_cuboid_nonexistence_claim.
```
