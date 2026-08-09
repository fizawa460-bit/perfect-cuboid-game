# Stage14-4bc — auxiliary-progression uniformity and split-E top-strip reduction

## Result

Stage14-4bb left two reciprocal-local gates:

```text
AUXILIARY_INCIDENCE_UNIFORMITY
+ STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY.
```

Stage14-4bc closes the first gate and sharply reduces the second.

The main conclusions are:

1. the merged 14-4ay frozen-state linear discrepancy theorem already gives auxiliary-modulus uniformity for every linear-linear reciprocal edge;
2. the signed-root `E=m^2+n^2` lattice theorem from s5m remains valid after **arbitrarily many pairwise-coprime frozen odd state moduli** are imposed: the auxiliary lattice is a sublattice of the original signed-root lattice, so its shortest vector cannot decrease;
3. the `E` column is the `H` factor in the s5a factorization. Its odd primes split only into selected `23` and unselected pieces, and there is no reciprocal edge between those two pieces;
4. whole-kernel `E` identities let every reciprocal edge be transferred from one split `E` piece to the other at the cost of only a one-variable mod-8 character. Hence all `E` reciprocal edges may be placed on the **smaller** of the two split `E` pieces, whose size is at most `sqrt(rad_odd(E)) <= M` on a regular Euclid box of scale `M`;
5. after this transfer, all state-split `E` multi-edge bulk monomials are a `K_4` linear graph plus one extra `E` vertex. The s5o graph escape extends to this `K_5` bulk sector with the same conservative worst saving `M^(-1/200+epsilon)`;
6. the remaining discrepancy is power-saving everywhere except one explicit top strip: the active split-`E` modulus is of scale `M` and a linear neighbor is at least `M^(1/2-o(1))`.

Thus

```text
AUXILIARY_INCIDENCE_UNIFORMITY = CLOSED,
```

and the former generic `STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY` obstruction is reduced to

```text
BALANCED_SPLIT_E_TOP_STRIP_DISPERSION.
```

No complete `rho_loc/E_loc` pair is claimed yet.

## 1. Imported linear auxiliary uniformity

Merged 14-4ay already proves the full-frozen-state normal form for a linear-linear reciprocal edge. After all other state pieces are frozen, endpoint coordinates can be written

```text
x=a0*u*r,
y=b0*v*s,
```

and all remaining odd auxiliary local conditions CRT to a projective congruence

```text
r = c*s (mod R),
(c,R)=1,
(R,a0*b0*u*v)=1.
```

The polygon slicing error is uniform in `R`, giving

```text
|Delta_state(u,v)|
 <<_epsilon B^epsilon
    (1 + H_i/(a0*u) + H_j/(b0*v)).
```

Therefore the linear part of the s5o `AUXILIARY_INCIDENCE_UNIFORMITY` flag was already solved on the merged mainline.

## 2. Uniform auxiliary theorem for signed-root E lattices

Fix one linear column `L_i` from

```text
m, n, m-n, m+n,
```

odd squarefree coprime moving moduli `u,v`, and one signed root

```text
r^2 = -1 (mod v).
```

The s5m base lattice is

```text
Lambda_0(i;u,v,r)
 = {(m,n): L_i(m,n)=0 (mod u), m-r*n=0 (mod v)}.
```

It has

```text
det Lambda_0 = u*v
```

and

```text
lambda_1(Lambda_0)
 >= (1/sqrt(2))*K(u,v),
K(u,v)=max(sqrt(v),min(u,v)).
```

Now freeze any finite collection of additional odd state moduli

```text
q_1,...,q_t
```

with pairwise-disjoint prime support and coprime to `uv`. After root-sign refinement, every frozen `E` condition is a single projective linear congruence. Every frozen linear-factor condition is already linear. Let `Lambda_aux` be the intersection of `Lambda_0` with all of them.

Because all auxiliary moduli are coprime to `uv`, reduction of `Lambda_0` modulo each `q_j` is the full plane, and imposing one primitive projective condition has index exactly `q_j`. CRT therefore gives

```text
det Lambda_aux
 = u*v*Q_aux,
Q_aux=product q_j.
```

More importantly,

```text
Lambda_aux subseteq Lambda_0,
```

so

```text
lambda_1(Lambda_aux)
 >= lambda_1(Lambda_0)
 >= K(u,v)/sqrt(2).
```

The elementary convex-region lattice estimate therefore gives an error no worse than the original s5m error. Primitive Mobius inversion is performed exactly as in s5m; auxiliary primes are pre-imposed locally and the remaining Mobius variable is coprime to the full frozen modulus. Divisor multiplicity and root-sign refinement cost only `B^o(1)`.

Hence the **uniform frozen-state signed-root discrepancy theorem** is

```text
|Delta_{i,E,r}^{aux}(u,v)|
 <<_epsilon
 B^epsilon * (1 + P_Omega/K(u,v)),
```

uniformly in `Q_aux`.

After summing the root signs,

```text
|Delta_{i,E}^{aux}(u,v)|
 <<_epsilon
 B^epsilon * (1 + P_Omega/K(u,v)),
```

and the same s5m L2 envelope remains valid:

```text
sum_{u~U,v~V} |Delta_{i,E}^{aux}(u,v)|^2
 <<_epsilon
 B^epsilon * UV * (1 + P_Omega^2/K(U,V)^2).
```

Therefore

```text
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true.
```

There is no additional exponent `delta_aux` to pay.

## 3. Exact structure of the split E column

From s5a,

```text
S=m^2-n^2,
X=2mn,
H=m^2+n^2.
```

Thus the fifth Euclid factor `E=m^2+n^2` is exactly the `H` factor.

The selected-prime routing from s5c forces

```text
p|H selected  => label 23=(0,1,1),
```

while s5d treats the alternative as an unselected `H` prime. Therefore the odd squarefree `E` kernel has only two state pieces:

```text
e = e_23 * e_0,
```

where `e_23` is selected and `e_0` is unselected.

### No E--E reciprocal edge

A second selected `H` prime has support vector `(0,1,1)`. In the selected-H rows the character exponents are `(0,1,1)` and `(1,0,0)`, so the same-factor interaction parities are

```text
(0,1,1) dot (0,1,1) = 0 mod 2,
(1,0,0) dot (0,1,1) = 0 mod 2.
```

An unselected H prime lies in none of `d1,d2,d3`. Conversely the unselected-H row is `chi(d1)=+1`, and selected label `23` is absent from `d1`.

Hence the two split E pieces never carry a genuine reciprocal edge between themselves:

```text
SPLIT_E_INTERNAL_RECIPROCAL_EDGE=false.
```

They can only couple reciprocally to linear-column state variables.

## 4. Whole-E transfer between the two split E pieces

Let

```text
e = rad_odd(E)=e_23*e_0.
```

Every prime of `e` is `1 mod 4`. For every odd divisor `u` of one of the four linear kernels, the whole-kernel identities from s5h hold already at divisor level:

```text
u|m       => (u/e)=1,
u|n       => (u/e)=1,
u|m-n     => (u/e)=(2/u),
u|m+n     => (u/e)=(2/u).
```

Indeed `E=e*t^2`, and modulo `m` or `n` the value `E` is a nonzero square, while modulo `m-n` or `m+n` it is twice a nonzero square.

Since `e=e_23*e_0`, Jacobi multiplicativity gives exactly

```text
(u/e_23) = (u/e) * (u/e_0),
(u/e_0)  = (u/e) * (u/e_23).
```

The factor `(u/e)` is only `1` or the one-variable mod-8 character `(2/u)`.

Therefore every reciprocal edge incident to one split E piece can be transferred to the other E piece at the cost of a bounded one-variable coefficient. If both pieces carried an edge to the same linear vertex, the two equal transferred Jacobi factors square to `1` and cancel.

Consequently a full E reciprocal monomial can be represented with **one reciprocal-active E vertex only**; the other E piece appears solely as an auxiliary incidence modulus.

On a regular Euclid box `m,n~M`,

```text
e <= E=m^2+n^2 << M^2.
```

Choose the reciprocal-active piece to be

```text
v=min(e_23,e_0).
```

Then

```text
v <= sqrt(e) << M.
```

This removes the apparent `M^2` E-modulus scale from the reciprocal graph.

## 5. K5 bulk graph escape

After the preceding transfer, the reciprocal graph has at most five active vertices:

```text
A,B,C,D,E_*.
```

There is no second active E vertex. Thus it is a subgraph of `K5`.

The s5i pure-incidence bulk remains rank one across all split state pieces. The s5o freeze-one-edge large-sieve argument is graph-size independent, so whenever an active edge has both endpoints at least `M^eta`, it gives

```text
M^(-eta/2+epsilon).
```

Take again

```text
eta=1/100.
```

If no long-long edge exists, all neighbors of a long vertex are `<M^eta`. Linear very-long vertices are handled exactly by s5o. For the E vertex, the rank-one E density is handled after root-sign summation; the root multiplicity is `B^o(1)` and does not alter the exponent bookkeeping. If every active variable is short, the fixed-modulus centered periodic argument has at most five active moduli and remains far below the `M^2` physical scale.

Thus the **rank-one / separable K5 bulk sector** inherits the same conservative bound

```text
E_bulk,K5(M)
 << M^(2-1/200+o(1)).
```

This statement does not by itself control the E incidence discrepancy; that is handled separately below.

## 6. E discrepancy exponent map after the transfer

The active E modulus now satisfies `V<=M`.

Write on a regular box

```text
U=M^a,
V=M^b,
0<=a,b<=1,
```

for one linear neighbor and the active split-E modulus. The uniform s5m pointwise/L2 transfer gives schematically

```text
E_Delta(U,V)
 << M^o(1) * UV * (1 + M/K(U,V)),
K(U,V)=max(V^(1/2),min(U,V)).
```

Ignoring the already-smaller `UV` term, the exponent is

```text
D(a,b)
 = a+b+1-max(a,b/2).
```

Two cases give an exact elementary ledger.

If `a>=b/2`, then

```text
D(a,b)=1+b.
```

If `a<b/2`, then

```text
D(a,b)=1+a+b/2.
```

Hence for every fixed `kappa>0`, one gets a power saving outside

```text
b > 1-kappa
and
a > 1/2-kappa.
```

For the concrete bookkeeping choice

```text
kappa=1/100,
```

all E-linear discrepancy blocks outside

```text
V >= M^(99/100),
U >= M^(49/100)
```

satisfy

```text
E_Delta(U,V)
 << M^(2-1/100+o(1)).
```

The K5 bulk is therefore still the slower closed exponent `1/200` on every such block.

## 7. The final E obstruction is a top strip, not generic multi-edge coupling

The only region not supplied a fixed saving by the preceding uniform discrepancy ledger is

```text
V >= M^(99/100),
U >= M^(49/100)
```

for at least one linear neighbor of the reciprocal-active E piece.

Because the active E piece was chosen to be the smaller of `e_23,e_0`, this top strip forces both split E pieces to be of order `M^(1-o(1))`, so the whole odd E kernel is of order `M^(2-o(1))`.

This is much narrower than the former `STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY` gate. It is a specific near-diagonal energy problem in which the natural E-lattice second moment is at the physical diagonal scale and Cauchy-Schwarz alone gives no fixed power saving.

Define the surviving obstruction as

```text
BALANCED_SPLIT_E_TOP_STRIP_DISPERSION.
```

It should be attacked by a two-copy signed-root determinant/anti-determinant energy estimate which keeps both E state pieces visible, rather than by another generic graph-conductor argument.

## 8. Updated reciprocal exponent contract

Stage14-4bb had

```text
delta_rec=min(1/200,delta_aux,delta_E).
```

Stage14-4bc proves that `delta_aux` is not a loss and closes all E sectors outside the balanced top strip with at least `1/100` discrepancy saving. Therefore the only remaining parameter is

```text
delta_top > 0
```

for the balanced split-E top strip.

The exact updated contract is

```text
boxed:
delta_rec=min(1/200,delta_top).
```

Equivalently, once the top strip is closed,

```text
E_rec(M)
 << M^(2-delta_rec+o(1)).
```

Since the global Stage14 height parameter satisfies `B~M^2` on regular Euclid boxes, the already-closed reciprocal sectors have

```text
E_rec,closed(B)
 << B^(1-1/400+o(1)).
```

No full reciprocal exponent is declared until `delta_top>0` is proved.

## 9. Why rho_loc is still unavailable

As in 14-4bb,

```text
S_W <= D_loc + E_rec.
```

`D_loc` is the constant/diagonal local-density contribution from 14-4au. Stage14-4bc only advances `E_rec`. Therefore it remains invalid to identify the reciprocal saving with `rho_loc`.

A complete

```text
S_W <= rho_loc A_W + E_loc
```

still requires a separate assignment of `D_loc` relative to `A_W` after the reciprocal top strip is closed.

## Boundary

```text
STAGE14_4BC=AUXILIARY_UNIFORMITY_CLOSED_AND_SPLIT_E_TOP_STRIP_ISOLATED
LINEAR_AUXILIARY_UNIFORMITY_IMPORTED_FROM_4AY=true
E_SIGNED_ROOT_AUXILIARY_SUBLATTICE_THEOREM_PROVED=true
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true
AUXILIARY_PROGRESSION_MODULUS_EXPONENT_LOSS=0
E_COLUMN_IS_H_FACTOR=true
E_ODD_STATE_PIECE_COUNT_MAX=2
SPLIT_E_INTERNAL_RECIPROCAL_EDGE=false
WHOLE_E_SPLIT_EDGE_TRANSFER_EXACT=true
RECIPROCAL_ACTIVE_E_PIECE_CAN_BE_CHOSEN_LE_M=true
K5_SEPARABLE_E_GRAPH_BULK_ASSEMBLED=true
K5_BULK_SAVING_EXPONENT=1/200
E_DISCREPANCY_OUTSIDE_TOP_STRIP_SAVING_EXPONENT=1/100
BALANCED_SPLIT_E_TOP_STRIP_DISPERSION_PROVED=false
STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_REDUCED_TO_TOP_STRIP=true
CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA=min(1/200,delta_top)
CLOSED_RECIPROCAL_B_SCALE_EXPONENT=1-1/400
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_COMPLETE_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

```text
NEXT=Stage14-4bd attack the balanced split-E top strip by a two-copy signed-root determinant/anti-determinant energy estimate, keeping both E state pieces visible; if a fixed saving is obtained, freeze the first complete reciprocal E_rec exponent and then return to the diagonal D_loc/rho_loc assignment
```
