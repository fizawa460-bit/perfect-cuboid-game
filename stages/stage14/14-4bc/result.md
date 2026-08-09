# Stage14-4bc — import s5p auxiliary uniformity and reduce split-E tensor to one top strip

## Result

Merged Stage14-4bb reduced the complete reciprocal-local problem to

```text
AUXILIARY_INCIDENCE_UNIFORMITY
+ STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY.
```

Merged Stage14-s5p now closes the first gate at theorem level. In particular it proves:

```text
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true
AUXILIARY_PROGRESSION_MODULUS_LOSS_PERSISTS=false
E_SIGNED_ROOT_AUX_UNIFORMITY_PROVED=true
E_SPARSE_AUX_UNIFORMITY_PROVED=true
AUXILIARY_STATE_ENERGY_TRANSFER_PROVED=true
HILBERT_QUADRATIC_LARGE_SIEVE_LIFT_PROVED=true.
```

Stage14-4bc imports those results and advances the remaining split-`E` tensor.

The new structural reduction is:

1. `E=m^2+n^2` is the `H` factor, so its odd squareclass support has only a selected `23` piece and an unselected piece;
2. those two E pieces have **no reciprocal edge between themselves**;
3. whole-E Jacobi identities transfer every E-linear reciprocal edge from one split E piece to the other, at the cost of only a one-variable mod-8 character;
4. therefore every E reciprocal monomial may be represented with **one reciprocal-active E vertex**, chosen to be the smaller of the two E pieces; its size is at most the Euclid scale `M`, not `M^2`;
5. the separable/rank-one E graph is then a `K5` problem and is closed with the same conservative `M^(-1/200+o(1))` graph saving;
6. using the s5p auxiliary `ell^2` transfer, the E discrepancy tensor is power-saving outside one explicit top strip;
7. the only surviving E tensor obstruction is

```text
V_E >= M^(99/100),
U_linear >= M^(49/100),
```

for at least one active E-linear edge.

We name this final reciprocal-local obstruction

```text
BALANCED_SPLIT_E_TOP_STRIP_TENSOR.
```

Thus the 4bb conditional contract

```text
delta_rec=min(1/200,delta_aux,delta_E)
```

is sharpened to

```text
boxed:
delta_rec=min(1/200,delta_top).
```

No complete `rho_loc/E_loc` pair is claimed yet.

## 1. s5p removes the auxiliary progression gate

For a moving linear edge, s5p proves that all frozen odd states collapse in scaled edge coordinates to one modular graph. Its fixed-state discrepancy has no positive power of the auxiliary modulus, and the dyadic L2 estimate is auxiliary-uniform.

For a moving signed-root E edge, s5p observes exactly the sublattice mechanism needed here: adding frozen auxiliary congruences makes the new lattice a sublattice of the original s5m lattice, so the shortest vector cannot become shorter. Therefore both the medium and sparse E estimates remain uniform.

s5p also proves two assembly facts which are essential below:

- auxiliary state labels have only `B^o(1)` collision energy;
- the quadratic large sieve lifts to Hilbert-space-valued coefficients with the same operator norm.

Consequently auxiliary states may be carried as Hilbert coordinates rather than summed in absolute value.

Hence Stage14-4bc sets

```text
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true
AUXILIARY_PROGRESSION_MODULUS_EXPONENT_LOSS=0.
```

There is no longer a `delta_aux` parameter in the main-track exponent ledger.

## 2. The E column has exactly two odd state pieces

Stage14-s5a uses

```text
S=m^2-n^2,
X=2mn,
H=m^2+n^2.
```

Thus the fifth Euclid factor

```text
E=m^2+n^2
```

is exactly the `H` factor.

Stage14-s5c forces every selected odd `H` prime to support label

```text
23=(0,1,1),
```

while s5d gives the alternative unselected H row. Therefore the odd squareclass kernel of E decomposes into at most two coprime pieces:

```text
e = core_odd(E) = e_23 * e_0,
```

where `E/e` has square odd part, `e_23` is the selected-H piece, and `e_0` is the unselected-H piece.

The prime `2` remains in the already finite Q2 state table and is not part of this moving odd graph.

## 3. There is no reciprocal E--E edge

At a selected H prime the two s5c row exponents are

```text
(0,1,1)
and
(1,0,0).
```

A second selected H prime has support vector `(0,1,1)`. Their interaction parities are

```text
(0,1,1) dot (0,1,1) = 0 mod 2,
(1,0,0) dot (0,1,1) = 0 mod 2.
```

Thus two selected H primes do not create a reciprocal symbol.

An unselected H prime lies in none of `d1,d2,d3`. Conversely the unselected-H row is `chi(d1)=+1`, and label `23` has zero first coordinate. Hence selected/unselected and unselected/unselected pairs also create no internal E reciprocity.

Therefore

```text
SPLIT_E_INTERNAL_RECIPROCAL_EDGE=false.
```

The two E state pieces can couple reciprocally only to the four linear factor columns.

## 4. Whole-E edge transfer is exact

Let

```text
e=core_odd(E)=e_23 e_0.
```

Every odd prime dividing `e` is `1 mod 4`. For every odd state divisor `u` of a linear factor, the s5h whole-E identities hold at divisor level because `E/e` is a square in odd squareclass:

```text
u|m       => (u/e)=1,
u|n       => (u/e)=1,
u|m-n     => (u/e)=(2/u),
u|m+n     => (u/e)=(2/u).
```

Since `e=e_23 e_0`, Jacobi multiplicativity gives

```text
(u/e_23)=(u/e)*(u/e_0),
(u/e_0) =(u/e)*(u/e_23).
```

The factor `(u/e)` is only `1` or the one-variable mod-8 character `(2/u)`.

Thus an edge incident to `e_23` may be moved to `e_0`, or conversely, without introducing a new moving conductor. If both E pieces carry an edge to the same linear vertex, after transfer the two identical Jacobi factors square to `1` and cancel.

Therefore every full E reciprocal monomial has an equivalent representation with exactly one reciprocal-active E piece. The other E piece remains only as an auxiliary incidence modulus, which s5p now handles uniformly.

## 5. Choose the smaller E piece as the reciprocal vertex

On a regular Euclid box

```text
m,n ~ M,
E=m^2+n^2 << M^2.
```

Choose

```text
v=min(e_23,e_0)
```

as the reciprocal-active E piece. Since

```text
e_23 e_0=e<=E,
```

we have

```text
v<=sqrt(e)<=sqrt(E)<<M.
```

Hence the reciprocal graph has at most the five vertices

```text
A,B,C,D,E_*
```

with every active modulus on the same `<=M` scale.

This is the crucial split-E reduction: the apparent `M^2` norm-factor scale is removed from the reciprocal graph before any large-sieve or tensor contraction is attempted.

## 6. Split-E density completion for a very-long E bulk vertex

The s5o graph escape needs a one-variable completion when there is no long-long edge but one active vertex is very long. For the E vertex, the rank-one density is

```text
lambda_E(n)=product_{p|n} 2/(p+1)
```

on split odd squarefree `n`.

Stage14-4bc proves the needed weighted completion in the accompanying supplement. Define

```text
b(n)=mu(n)^2 * 1_{p|n => p=1 mod 4}
     * product_{p|n} (2p/(p+1)).
```

Then for a primitive real character `chi` of odd conductor `q`,

```text
sum_{n<=x} b(n)chi(n)
 <<_epsilon (xq)^(1/2) (xq)^epsilon
```

uniformly for `x>=q`.

The proof uses the coefficient-level factorization

```text
sum b(n)chi(n)n^(-s)
 = L(s,chi)L(s,chi*chi_4)G(s),
```

where `G` is absolutely convergent for `Re(s)>1/2+epsilon`, followed by Dirichlet hyperbola and Pólya--Vinogradov.

Since `lambda_E(n)=b(n)/n`, partial summation gives

```text
sum_{n~N} lambda_E(n)chi(n)
 <<_epsilon N^(-1/2)q^(1/2)(Nq)^epsilon,
N>=q.
```

This is weaker in the conductor than the s5n squarefree lemma, but it is sufficient for the E vertex.

## 7. K5 rank-one bulk is closed

Take

```text
eta=1/100.
```

For a nonempty reciprocal graph on `A,B,C,D,E_*`:

### Case A: a long-long edge exists

If both endpoints of some edge are at least `M^eta`, freeze all other state variables. The s5p Hilbert-valued lift of the s5h quadratic large sieve gives

```text
M^(-eta/2+o(1))=M^(-1/200+o(1)).
```

### Case B1: no long-long edge, a linear vertex is very long

This is exactly the s5o one-variable completion case and is already stronger than `1/200`.

### Case B2: no long-long edge, the E vertex is very long

The E vertex has degree at most four, so all neighbor product conductors satisfy

```text
q<=M^(4eta).
```

Use the threshold

```text
V>=M^(6eta).
```

The split-E density completion above gives relative saving

```text
V^(-1/2)q^(1/2)
 <= M^(-3eta)M^(2eta)
 = M^(-eta)
 = M^(-1/100).
```

### Case C: everything remaining is short

If no linear active variable reaches `M^(4eta)` and the E variable is below `M^(6eta)`, the product of all five active moduli is at most

```text
M^(4*4eta+6eta)=M^(22eta).
```

The number of modulus tuples has the same crude exponent, while root-sign and auxiliary Hilbert multiplicity cost only `B^o(1)` by s5p. Exact local centering plus the periodic box estimate therefore gives

```text
M^(1+44eta+o(1)) + M^(66eta+o(1))
 = M^(1.44+o(1)) + M^(0.66+o(1)),
```

well below `M^2`.

Thus

```text
K5_SEPARABLE_E_GRAPH_BULK_ASSEMBLED=true
K5_BULK_SAVING_EXPONENT=1/200.
```

## 8. Hilbert-valued E discrepancy tensor outside the top strip

The remaining issue is the incidence discrepancy, not the rank-one bulk.

By merged s5p, the signed-root E discrepancy estimate is auxiliary-uniform and auxiliary state labels may be retained as Hilbert coordinates at only `B^o(1)` energy cost. Therefore the scalar s5m dyadic envelope transfers to the Hilbert norm before contraction against the remaining graph characters.

Write

```text
U=M^a,
V=M^b,
0<=a,b<=1,
```

where `U` is one active linear neighbor and `V` is the reciprocal-active E piece. Because `V<=M`, the full range is `b<=1`.

The s5m bound uses

```text
K(U,V)=max(V^(1/2),min(U,V)).
```

and gives, after Cauchy/Hilbert transfer, the schematic exponent

```text
D(a,b)=a+b+1-max(a,b/2).
```

If `a>=b/2`, then

```text
D(a,b)=1+b.
```

If `a<b/2`, then

```text
D(a,b)=1+a+b/2.
```

Take

```text
kappa=1/100.
```

Outside the strip

```text
b>99/100
and
a>49/100,
```

one always has

```text
D(a,b)<=2-1/100.
```

The proof is elementary:

- in the first case `a>=b/2`, if `b>99/100` then automatically `a>99/200>49/100`, so being outside the strip forces `b<=99/100`;
- in the second case, either `a<=49/100`, giving `D<=1+49/100+1/2=199/100`, or `a>49/100`, which outside the strip forces `b<=99/100` and then `a<b/2<=99/200`, again giving `D<199/100`.

Thus the active-E discrepancy tensor has at least `M^(-1/100+o(1))` saving on every dyadic block outside the declared top strip. The other graph contractions do not reintroduce an auxiliary modulus loss because s5p supplies the Hilbert energy transfer.

## 9. The surviving top strip

The only E tensor regime not assigned a fixed saving is

```text
V >= M^(99/100),
U >= M^(49/100)
```

for at least one active E-linear edge.

Because the reciprocal-active E piece is the smaller of `e_23,e_0`, this also forces both split E pieces to have scale `M^(1-o(1))`; hence

```text
core_odd(E)=e_23 e_0 = M^(2-o(1)).
```

In this band the signed-root lattice L2 energy is at its natural physical diagonal scale. The s5p Hilbert lift transports that diagonal correctly but does not itself produce a positive power saving. This is exactly why s5p left

```text
MULTI_EDGE_DISCREPANCY_TENSOR_CONTRACTION_PROVED=false.
```

After the reductions above, that general tensor obstruction is no longer spread over all E ranges. It is concentrated in the explicit near-diagonal band

```text
BALANCED_SPLIT_E_TOP_STRIP_TENSOR.
```

The correct next attack is a two-copy signed-root energy argument which keeps **both** E state pieces visible and exploits the simultaneous determinant / anti-determinant divisibility, rather than another generic conductor bound.

## 10. Updated reciprocal exponent contract

Stage14-4bb recorded

```text
delta_rec=min(1/200,delta_aux,delta_E).
```

Merged s5p removes `delta_aux`. Stage14-4bc closes the E rank-one graph and all E discrepancy blocks outside the top strip. Therefore the only remaining reciprocal parameter is

```text
delta_top>0.
```

The exact new contract is

```text
boxed:
delta_rec=min(1/200,delta_top).
```

All already-closed reciprocal sectors satisfy

```text
E_rec,closed(M)
 << M^(2-1/200+o(1)).
```

Since the Stage14 Euclid scale has `B~M^2`, this is

```text
E_rec,closed(B)
 << B^(399/400+o(1)).
```

This is **not** yet the complete reciprocal error theorem because the top strip remains open.

## 11. rho_loc remains a separate diagonal problem

The local domination remains

```text
S_W <= D_loc + E_rec.
```

Even after the top strip is closed, the constant/diagonal term `D_loc` must be assigned against `A_W` before a genuine

```text
S_W <= rho_loc A_W + E_loc
```

can be stated.

Therefore Stage14-4bc does not identify the reciprocal `1/200` saving with `rho_loc`.

## Boundary

```text
STAGE14_4BC=S5P_AUXILIARY_UNIFORMITY_IMPORTED_AND_SPLIT_E_TOP_STRIP_ISOLATED
S5P_AUXILIARY_UNIFORMITY_IMPORTED=true
S5P_AUXILIARY_STATE_ENERGY_TRANSFER_IMPORTED=true
S5P_HILBERT_QUADRATIC_LARGE_SIEVE_LIFT_IMPORTED=true
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true
AUXILIARY_PROGRESSION_MODULUS_EXPONENT_LOSS=0
E_COLUMN_IS_H_FACTOR=true
E_ODD_STATE_PIECE_COUNT_MAX=2
SPLIT_E_INTERNAL_RECIPROCAL_EDGE=false
WHOLE_E_SPLIT_EDGE_TRANSFER_EXACT=true
RECIPROCAL_ACTIVE_E_PIECE_CAN_BE_CHOSEN_LE_M=true
SPLIT_E_DENSITY_COMPLETION_LEMMA_PROVED=true
K5_SEPARABLE_E_GRAPH_BULK_ASSEMBLED=true
K5_BULK_SAVING_EXPONENT=1/200
E_DISCREPANCY_TENSOR_OUTSIDE_TOP_STRIP_SAVING_EXPONENT=1/100
BALANCED_SPLIT_E_TOP_STRIP_TENSOR_PROVED=false
STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_REDUCED_TO_TOP_STRIP=true
CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA=min(1/200,delta_top)
CLOSED_RECIPROCAL_B_SCALE_ERROR_EXPONENT=399/400
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
EXPLICIT_COMPLETE_RECIPROCAL_E_REC_PROVED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_COMPLETE_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

```text
NEXT=Stage14-4bd prove a positive-power two-copy energy bound in the balanced split-E top strip, using both E state pieces and signed-root determinant/anti-determinant collisions; then freeze the first complete E_rec exponent and return to the D_loc/rho_loc diagonal assignment
```
