# Stage36 36-09ER — cyclic Legendre-core odd matching parity criterion

## Purpose

36-09EQ proves a graph-only sufficient condition for

```text
rank_F2 M_R(R(a,b))=2n-2
```

by leaf-pivoting the Legendre support graph. That criterion recognizes five of the six exact maximal-rank orbits in the 36-09EO diagnostic box, but the orbit

```text
O(3/47)={3/47,22/25,25/22,47/3}
```

has a nontrivial cyclic residual core.

This leaf closes that exact graph-theoretic gap by replacing complete leaf-peelability with a leaf-plus-odd-core certificate.

## Odd matching parity on an F2 minor

For a finite square 0/1 matrix `H`, view `H` as the bipartite adjacency matrix between its row and column vertices. The determinant expansion is

```text
det(H)=sum_{sigma} sign(sigma) product_i H[i,sigma(i)].
```

Over `F2`, `+1=-1`, so the signs disappear. Therefore

```text
det_F2(H)
=
(number of perfect matchings of the bipartite graph of H) mod 2.
```

Hence an odd number of perfect matchings implies

```text
det_F2(H)=1.
```

This is the only parity fact used below.

## Leaf-plus-core maximal-rank criterion

Let `M=M_R(R(a,b))`, and let `n` be the EP ambient half-dimension. Perform any valid sequence of `k` leaf pivots as in 36-09EQ.

Suppose the residual active graph contains a square submatrix `H` of size

```text
m=2n-2-k
```

whose bipartite graph has an odd number of perfect matchings.

Select the `k` pivot rows/columns together with the `m` rows/columns of `H`. Reverse the leaf-pivot order. The selected `(2n-2) x (2n-2)` minor is block-triangular under that order: every leaf pivot contributes a diagonal `1`, and the final diagonal block is `H`. Therefore

```text
det_F2(selected minor)=det_F2(H)=1.
```

Thus

```text
rank_F2 M >= 2n-2.
```

As in 36-09EQ, rational full 2-torsion forces the universal upper bound `rank M<=2n-2`. Hence

```text
rank_F2 M=2n-2
```

and therefore

```text
Sel2_dim=2.
```

This criterion includes complete leaf peeling as the special case `m=0`.

## Exact O(3/47) core: p=3/47 and p=22/25

For both ordered representatives `(a,b)=(3,47)` and `(22,25)`, the deterministic 36-09EQ peeling performs

```text
k=12
```

pivots. Since `n=10`, the remaining certificate size is

```text
m=18-12=6.
```

Using the canonical residual row/column labels, select rows

```text
(3,1),(5,1),(11,1),(17,1),(73,1),(137,1)
```

and columns

```text
x[17],x[73],x[137],y[3],y[5],y[11].
```

The resulting `6 x 6` core minor is

```text
1 0 1 | 0 0 0
1 1 1 | 0 0 0
1 1 0 | 0 0 0
------+------
0 0 0 | 1 1 1
0 0 0 | 0 1 1
0 0 0 | 1 1 0
```

The first `3 x 3` block has exactly three perfect matchings, and the second `3 x 3` block also has exactly three. Thus the full core minor has

```text
3*3=9
```

perfect matchings, which is odd. Therefore its determinant is `1` in `F2` and the full support matrix has rank `18`.

## Exact inverse representatives: p=25/22 and p=47/3

For `(25,22)` and `(47,3)`, deterministic peeling performs

```text
k=10,
m=18-10=8.
```

Select residual rows

```text
(3,1),(5,1),(11,1),(17,0),(17,1),(73,0),(73,1),(137,1)
```

and residual columns

```text
x[17],x[73],x[137],y[3],y[5],y[11],y[17],y[73].
```

The resulting `8 x 8` core minor is

```text
1 0 1 0 0 0 0 0
1 1 1 0 0 0 0 0
1 1 0 0 0 0 0 0
1 0 0 0 0 0 1 0
0 1 0 1 1 1 0 1
0 1 0 0 0 0 0 1
1 0 0 0 1 1 1 0
0 0 0 1 1 0 0 0
```

It has exactly

```text
9
```

perfect matchings. Hence its determinant is again `1` in `F2`, giving rank `18` and `Sel2_dim=2`.

## EO box consequence

36-09EQ already gives complete leaf-pivot certificates for exactly `20` of the `24` exact `Sel2_dim=2` rows in the EO `1<=a,b<=50` box.

The four rows of `O(3/47)` now have leaf-plus-odd-core certificates. Therefore all

```text
24 / 24
```

exact maximal-rank rows in that box admit explicit Legendre-graph certificates, with zero false positives.

This does **not** make the finite box exhaustive. It shows that the observed maximal-rank phenomenon is entirely visible in the finite labelled Legendre graph: either by leaf pivots alone or by leaf pivots plus a small odd-matching core.

## Structural conclusion

The previously unresolved cyclic core is not a new arithmetic local condition. It is parity of perfect matchings in a small residual Legendre graph.

A natural next leaf is therefore to translate the two graph certificate mechanisms into direct arithmetic conditions on labelled prime support and Legendre-symbol patterns, rather than searching larger boxes:

```text
36-09ES_RHO_LEGENDRE_PATTERN_CLASSIFICATION_PREFLIGHT.
```

## Credit firewall

This leaf adds no new fixed-p values beyond the exact 24-value registry already promoted by 36-09EO. The EO box remains diagnostic, not exhaustive.

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
