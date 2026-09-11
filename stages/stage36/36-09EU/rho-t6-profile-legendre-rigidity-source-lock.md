# Stage36 36-09EU — T6-profile Legendre rigidity

## Purpose

36-09ET isolates a single coarse labelled/mod-8 profile with five new near-miss orbits. On that profile the exact 36-09EP support matrix has rank either 18 or 16 in the observed realizations. This leaf removes the parameter-specific hashes and derives an exact symbolic rank criterion valid for **every** realization of the same coarse profile.

Entry authority is V274, with 36-09ET exact-green and the fixed-p exclusion registry at 36 values.

## Fixed coarse profile

After the global P/Q swap allowed by 36-09ES and permutations inside equal labelled/mod-8 classes, order the eight odd support vertices as

```text
D0 : (D,3)
D1 : (D,3)
D2 : (D,5)
D3 : (D,7)
P  : (P,1)
R  : (P,7)
Q0 : (Q,1)
Q1 : (Q,1)
```

and retain the shallow dyadic branch. Directed Legendre bits satisfy quadratic reciprocity, so one upper-triangular bit for each unordered pair determines the full directed datum.

Let

```text
b_iP  = (P / D_i) bit,
b_i0  = (Q0 / D_i) bit,
b_i1  = (Q1 / D_i) bit
```

in the retained 0/1 convention (`0` for +1, `1` for -1). Form the 4 x 3 matrix

```text
B =
[ b_0P b_00 b_01 ]
[ b_1P b_10 b_11 ]
[ b_2P b_20 b_21 ]
[ b_3P b_30 b_31 ].
```

Swapping the two `(Q,1)` vertices only permutes the last two columns, so `rank_F2(B)` is canonical.

## Exact constant-pivot reduction

Construct the full 20 x 20 36-09EP Selmer support matrix symbolically from the coarse profile, with all unordered Legendre bits left as independent F2 variables and reverse directed bits imposed by quadratic reciprocity.

There is a fixed sequence of twelve pivots whose pivot entries are identically `1`, independent of every Legendre variable. Exact invertible row and column operations reduce the matrix to

```text
I_12  (+)  R_8,
```

where `R_8` has one identically zero row and one identically zero column. Removing those gives the 7 x 7 alternating core

```text
K = [ 0_4   B ]
    [ B^T   C ],
```

with

```text
C =
[ 0    e_PQ1 e_PQ0 ]
[ e_PQ1   0     0   ]
[ e_PQ0   0     0   ].
```

Here `e_PQ0,e_PQ1` are two further Legendre bits. All other Legendre variables disappear from the rank problem, including the P7 interactions and the Q0-Q1 bit.

Therefore

```text
rank(M_Sel2) = 12 + rank(K).
```

## Alternating-core theorem

Because `K` is alternating of odd size seven, its rank is even and at most six.

For each `i=0,1,2,3`, delete the `D_i` row and column. The resulting 6 x 6 alternating matrix has Pfaffian equal to the determinant of the 3 x 3 matrix obtained from `B` by deleting row `i`. The three special-vertex deletions have identically zero Pfaffian.

Hence the seven principal 6 x 6 Pfaffians are exactly

```text
det(B without row 0),
det(B without row 1),
det(B without row 2),
det(B without row 3),
0,0,0.
```

Thus

```text
rank(K)=6
iff at least one 3 x 3 minor of B is nonzero
iff rank_F2(B)=3.
```

If `rank(B)<=2`, all principal 6 x 6 Pfaffians vanish, so the alternating core has rank at most four.

Combining with the universal full rational 2-torsion upper bound from 36-09EP gives the exact equivalence

```text
rank_F2 M_Sel2 = 18
iff rank_F2 B = 3
iff dim_F2 Sel^2(E_rho,p/Q)=2.
```

This is a necessary-and-sufficient criterion on the entire fixed coarse profile, not merely on the ET 1..2000 diagnostic domain.

## Explicit Pfaffian parities

Writing the three columns of B as `P,Q0,Q1`, the four decisive cubic parities are

```text
Delta_i = det_F2(B with row i deleted),  i=0,1,2,3.
```

Equivalently each `Delta_i` is the parity of the six perfect matchings of the corresponding 3 x 3 bipartite graph. The criterion is

```text
Sel2_dim=2  iff  (Delta_0,Delta_1,Delta_2,Delta_3) != (0,0,0,0).
```

No other Legendre bit enters this decision.

## Replay on the six ET profile patterns

Using one common coarse-profile orientation:

```text
T6  seed 3/47:     rank(B)=3
T7  seed 1/277:    rank(B)=3
T8  seed 1/333:    rank(B)=3
T9  seed 134/863:  rank(B)=3
N1  seed 1/1323:   rank(B)=2
N2  seed 81/317:   rank(B)=2
```

so the exact symbolic criterion separates all four rank-18 patterns from both retained rank-16 negative controls.

## Consequence and next leaf

The hash-level distinction T6/T7/T8/T9 is unnecessary for Sel2 rank on this coarse profile. They are all instances of one arithmetic family cut out by the single rank condition `rank(B)=3`.

The next leaf is

```text
36-09EV_RHO_T6_PROFILE_RANK3_REALIZATION_PREFLIGHT
```

which should search directly for new primitive realizations of this coarse profile with `rank(B)=3`, rather than exact hash matches, and then independently apply the 36-09EH no-4/no-3 torsion checks.

## Credit firewall

This leaf adds no new fixed-p exclusion by itself. It does not prove that the T6 coarse profile is the only possible maximal-rank profile, nor that all positive rational parameters satisfy the criterion.

The following remain false:

```text
all maximal-rank profiles classified,
uniform Sel2 dimension two,
all positive rational p excluded,
candidate parameter set shrunk,
receiver emptiness,
R29-CAMP2 closure,
Q11-CAMPEDELLI closure,
endpoint closure,
Perfect Cuboid nonexistence.
```
