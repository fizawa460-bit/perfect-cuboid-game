# Stage14-4bc — s5p auxiliary uniformity and split-E top-strip reduction

## Result

Merged Stage14-4bb left

```text
AUXILIARY_INCIDENCE_UNIFORMITY
+ STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY.
```

Merged Stage14-s5p now closes the first gate and supplies the tensor-energy interface required for the second:

```text
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true
AUXILIARY_PROGRESSION_MODULUS_LOSS_PERSISTS=false
E_SIGNED_ROOT_AUX_UNIFORMITY_PROVED=true
AUXILIARY_STATE_ENERGY_TRANSFER_PROVED=true
HILBERT_QUADRATIC_LARGE_SIEVE_LIFT_PROVED=true.
```

Stage14-4bc imports s5p and reduces the remaining split-`E` tensor to one explicit top strip.

The conclusion is

```text
all closed reciprocal sectors:
E_rec,closed(M) << M^(2-1/200+o(1)),

only remaining reciprocal-local sector:
BALANCED_SPLIT_E_TOP_STRIP_TENSOR.
```

The updated conditional reciprocal exponent is

```text
boxed:
delta_rec=min(1/200,delta_top).
```

No complete `rho_loc/E_loc` pair is claimed.

## 1. Auxiliary progression loss is gone

Stage14-s5p proves the full auxiliary-modulus version of the linear and signed-root E incidence estimates. Frozen odd state conditions combine into projective CRT cells; adding auxiliary E/linear congruences makes the signed-root lattice a sublattice and cannot decrease its shortest vector.

It also proves:

- squarefree quadratic completion in coprime progressions;
- auxiliary state collision energy costs only `B^o(1)`;
- the quadratic large sieve lifts to Hilbert-space-valued coefficients with the same operator norm.

Therefore auxiliary labels may remain as Hilbert coordinates rather than being summed in absolute value. In the 14-4 main-track ledger,

```text
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true
AUXILIARY_PROGRESSION_MODULUS_EXPONENT_LOSS=0.
```

The parameter `delta_aux` is removed.

## 2. The E column has at most two odd state pieces

The Euclid factors are

```text
S=m^2-n^2,
X=2mn,
H=m^2+n^2.
```

Thus the fifth factor `E=m^2+n^2` is exactly `H`.

By s5c, every selected odd H prime has support label

```text
23=(0,1,1).
```

By s5d, the alternative is an unselected H prime. Hence the odd squareclass kernel has at most two coprime state pieces:

```text
e=core_odd(E)=e_23*e_0,
```

where `E/e` has square odd part.

## 3. There is no reciprocal edge between the two E pieces

At a selected H prime, the two character-row exponent vectors are

```text
(0,1,1),
(1,0,0).
```

A second selected H prime has support `(0,1,1)`, so both dot products are `0 mod 2`. An unselected H prime lies in none of `d1,d2,d3`, while its row is `chi(d1)=+1`; selected label `23` has zero first coordinate.

Thus selected-selected, selected-unselected, and unselected-unselected H pairs create no internal reciprocal symbol:

```text
SPLIT_E_INTERNAL_RECIPROCAL_EDGE=false.
```

The split E pieces couple reciprocally only to linear columns.

## 4. Whole-E transfer puts all reciprocal E edges on one piece

Let

```text
e=e_23 e_0=core_odd(E).
```

Every odd prime of `e` is `1 mod 4`. For an odd state divisor `u` of a linear factor, the whole-E identities give

```text
u|m       => (u/e)=1,
u|n       => (u/e)=1,
u|m-n     => (u/e)=(2/u),
u|m+n     => (u/e)=(2/u).
```

Because `e=e_23e_0`,

```text
(u/e_23)=(u/e)(u/e_0),
(u/e_0) =(u/e)(u/e_23).
```

The factor `(u/e)` is only a constant or the one-variable mod-8 character `(2/u)`. Therefore every E-linear reciprocal edge can be transferred from one E piece to the other without a new moving conductor. If both pieces carry an edge to the same linear vertex, the transferred Jacobi factors square to `1` and cancel.

Hence every E reciprocal monomial has a representation with one reciprocal-active E vertex; the other E piece is only an auxiliary incidence coordinate, already uniform by s5p.

## 5. The reciprocal-active E piece has scale at most M

On a regular Euclid box `m,n~M`,

```text
E=m^2+n^2 << M^2.
```

Choose

```text
v=min(e_23,e_0).
```

Then

```text
v<=sqrt(e)<=sqrt(E)<<M.
```

Thus the reciprocal graph has at most five vertices

```text
A,B,C,D,E_*,
```

all with moving modulus scale `<=M`.

This removes the apparent `M^2` norm-factor modulus from the reciprocal graph.

## 6. K5 rank-one bulk is closed

The s5i pure-incidence bulk remains rank one across all state pieces. The s5p Hilbert lift allows the s5o freeze-one-edge graph escape to be applied with auxiliary states retained as Hilbert coordinates.

Take

```text
eta=1/100.
```

If a long-long edge exists, one genuine Jacobi edge gives the s5h/s5o saving

```text
M^(-eta/2+o(1))=M^(-1/200+o(1)).
```

If there is no long-long edge and a linear vertex is very long, s5o squarefree completion applies.

For a very-long E vertex, Stage14-4bc proves the supplementary split-E density lemma. On split odd squarefree support,

```text
lambda_E(n)=product_{p|n}2/(p+1).
```

Writing

```text
b(n)=mu(n)^2*1_{p|n=>p=1 mod4}*product_{p|n}(2p/(p+1)),
```

the Dirichlet series satisfies

```text
sum b(n)chi(n)n^(-s)
=L(s,chi)L(s,chi*chi_4)G(s),
```

with `G` absolutely convergent for `Re(s)>1/2+epsilon`. Dirichlet hyperbola and Pólya--Vinogradov give

```text
sum_{n~N}lambda_E(n)chi(n)
<<_epsilon N^(-1/2)q^(1/2)(Nq)^epsilon.
```

With no long-long edge the E vertex has at most four neighbors `<M^eta`, so `q<=M^(4eta)`. If `V>=M^(6eta)`, this gives relative saving `M^(-eta)=M^(-1/100)`.

If all four linear variables are `<M^(4eta)` and E is `<M^(6eta)`, the total active modulus product is at most `M^(22eta)`. Exact centering and the periodic estimate give

```text
M^(1+44eta+o(1))+M^(66eta+o(1))
=M^(1.44+o(1))+M^(0.66+o(1)),
```

below `M^2`.

Therefore

```text
K5_SEPARABLE_E_GRAPH_BULK_ASSEMBLED=true
K5_BULK_SAVING_EXPONENT=1/200.
```

## 7. E discrepancy tensor outside the top strip

By s5p, the signed-root E discrepancy is auxiliary-uniform and the auxiliary state labels have `ell^2` energy `B^o(1)`. Hence the scalar s5m dyadic envelope transfers to Hilbert norm before contraction against the remaining graph characters.

Write

```text
U=M^a,
V=M^b,
0<=a,b<=1,
```

for one active linear neighbor and the reciprocal-active E piece. The signed-root shortest-vector scale is

```text
K(U,V)=max(V^(1/2),min(U,V)).
```

The resulting discrepancy exponent is

```text
D(a,b)=a+b+1-max(a,b/2).
```

If `a>=b/2`, then `D=1+b`; if `a<b/2`, then `D=1+a+b/2`.

Take `kappa=1/100`. Outside

```text
b>99/100
and
a>49/100,
```

one has

```text
D(a,b)<=2-1/100.
```

Thus every E discrepancy tensor block outside the top strip saves at least

```text
M^(-1/100+o(1)).
```

This is stronger than the conservative K5 bulk bottleneck `1/200`.

## 8. Final reciprocal-local obstruction

The only E tensor regime not assigned a positive power saving is

```text
V>=M^(99/100),
U>=M^(49/100)
```

for at least one E-linear reciprocal edge.

Since the reciprocal-active E piece was chosen to be the smaller of `e_23,e_0`, both E pieces are then `M^(1-o(1))`, so

```text
core_odd(E)=e_23e_0=M^(2-o(1)).
```

Here the signed-root lattice second moment sits at the natural physical diagonal scale. s5p transports the tensor correctly but does not supply a fixed saving. The generic state-split E assembly problem is therefore reduced to

```text
BALANCED_SPLIT_E_TOP_STRIP_TENSOR.
```

The next attack should keep both E state pieces visible and exploit two-copy signed-root determinant/anti-determinant collisions.

## 9. Updated reciprocal exponent contract

Stage14-4bb had

```text
delta_rec=min(1/200,delta_aux,delta_E).
```

Merged s5p removes `delta_aux`, and Stage14-4bc closes all E sectors except the balanced top strip. Thus

```text
boxed:
delta_rec=min(1/200,delta_top).
```

All closed reciprocal sectors satisfy

```text
E_rec,closed(M)<<M^(2-1/200+o(1)).
```

Since `B~M^2`, equivalently

```text
E_rec,closed(B)<<B^(399/400+o(1)).
```

This is not yet the complete reciprocal error theorem because `delta_top>0` is not proved.

## 10. rho_loc remains separate

The local domination remains

```text
S_W<=D_loc+E_rec.
```

`D_loc` is the constant/diagonal local-density contribution. Even after the top strip is closed, `D_loc` must be assigned against `A_W` before a genuine `rho_loc/E_loc` pair is available.

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
