# Stage14-4ax — sparse linear dispersion transfer and determinant/norm frontier

## Result

Stage14-4aw left three local analytic pieces:

```text
Delta L2 dispersion
+ microscopic lower-dimensional blocks
+ sparse large-state moduli.
```

Merged Stage14-s5j now closes the **sparse discrepancy second moment for the six reciprocal edges among the four linear Euclid columns**

```text
m, n, m-n, m+n,
```

by reducing every collision to the determinant

```text
D(P,P') = m*n' - m'*n.
```

Stage14-4ax imports that theorem into the main `14-4` retainer chain, audits what it actually supplies to `E_loc`, removes the literal unit-modulus endpoint from the reciprocal ledger, and isolates the remaining medium linear and state-split norm problems.

## 1. Imported sparse linear theorem

For a primitive Euclid point `P=(m,n)`, each of the four linear columns is one projective slope modulo every odd prime:

```text
m       : [0:1]
n       : [1:0]
m-n     : [1:1]
m+n     : [-1:1].
```

For odd squarefree state moduli `u,v` on two distinct linear columns, CRT gives one projective class modulo

```text
q=uv.
```

If two primitive positive points `P,P'` occupy the same cell, merged s5j proves

```text
q | D(P,P').
```

Inside

```text
0<m,m'<=X,
0<n,n'<=Y,
```

we have `|D(P,P')|<2XY`, and `D=0` for primitive positive points implies `P=P'`. Therefore

```text
q>2XY
=> every sparse linear projective cell has occupancy at most 1.
```

Writing the s5i rank-one main term as `M(u,v)`, incidence as `W(u,v)`, and

```text
Delta(u,v)=W(u,v)-M(u,v),
```

merged s5j obtains for `Q=UV>2XY`

```text
boxed:
sum_{u~U,v~V}|Delta(u,v)|^2
  <<_epsilon N B^epsilon,
```

where `N` is the number of primitive opposite-parity Euclid points in the geometric box.

The scale `N` is the genuine same-point diagonal scale.

## 2. Main-track transfer audit: L2 closure is not yet rho_loc saving

The sparse theorem removes the possible large-modulus **dispersion blow-up**, but it must not be over-interpreted.

A bare Cauchy transfer gives

```text
|sum Delta(u,v)(u/v)|
<= (# cells)^(1/2) * (sum |Delta|^2)^(1/2)
<< (Q N)^(1/2) B^epsilon.
```

When `Q` is comparable to or larger than `N`, this is not a fixed-power saving below the base `N` scale. The stronger occupancy fact `W in {0,1}` gives the direct absolute estimate

```text
sum W(u,v) << N B^epsilon,
```

again base-scale rather than `N^(1-eta)`.

Thus the exact main-track conclusion is:

```text
sparse six-linear L2 is closed to its natural diagonal scale,
but sparse L2 alone does not instantiate a positive delta_loc.
```

This distinction matters in the 14-4as error ledger: a controlled second moment is a necessary analytic input, not automatically the final retainer exponent.

## 3. Medium six-linear remainder is one determinant problem

For

```text
Q<=2XY,
```

distinct points can collide. But every off-diagonal collision on all six linear reciprocal edges is supported on

```text
uv | D(P,P').
```

So the earlier arbitrary coefficient-matrix obstruction is gone. The medium second moment reduces to the structured divisor correlation

```text
sum_{P != P'}
#{u~U,v~V : uv | m*n'-m'*n,
               u,v satisfy the two fixed linear-column state conditions}.
```

The divisor multiplicity of one fixed nonzero determinant is only `B^o(1)`, but there are `N^2` point pairs. A genuine determinant-distribution / dispersion estimate is still required to extract a fixed power.

This is now the first unresolved object on the six-linear core.

## 4. Exact unit-modulus endpoint is lower-dimensional

The most singular microscopic case is exact, not analytic. If one reciprocal modulus is `1`, then

```text
(1/v)=1.
```

That edge is no longer a nonconstant reciprocal character. It belongs to the Fourier graph with that edge deleted and must be handled as a lower-dimensional mode.

Hence

```text
U=1 or V=1
```

is removed from the reciprocal off-diagonal error ledger.

This does **not** close the full microscopic interval `1<U<L^kappa`: a slowly growing small side can still fail to yield a fixed power from the quadratic large sieve. The correct next treatment is induction on active reciprocal edges and/or divisor switching for the small side.

## 5. State-split norm column has a different collision law

Merged s5j also identifies why the norm column

```text
E=m^2+n^2
```

survives the linear sparse closure.

For `p=1 mod 4`, choose `r^2=-1 mod p`. The two norm roots are

```text
[+r:1], [-r:1].
```

For two points:

- same root sign implies `p | D(P,P')`;
- opposite root signs imply

```text
p | S(P,P'),
S(P,P')=m*n'+m'*n.
```

Thus a state-split norm modulus decomposes as

```text
q_E=q_same*q_opp,
q_same | D(P,P'),
q_opp  | S(P,P').
```

and only

```text
q_E | D(P,P') S(P,P')
```

is forced in general.

Because both `D` and `S` are `O(XY)`, mixed-sign norm pieces can support moduli up to `O((XY)^2)`. Therefore the threshold `q>2XY` that closes the linear-four sparse cells does not close the full state-split `E` contribution.

## 6. Updated local decomposition

Combining 14-4av, 14-4aw, merged s5i, and merged s5j gives

```text
local support expansion
 -> rank-one full-state bulk + Delta
 -> interior bulk: fixed-power saving proved
 -> sparse six-linear Delta: L2 diagonal scale proved
 -> exact unit modulus: lower-dimensional reclassification
 -> medium six-linear Delta: uv | determinant, power saving missing
 -> state-split E: q_same | D, q_opp | S, mixed-sign dispersion missing
 -> slowly microscopic sides: induction/switching missing.
```

The previous frontier

```text
DISCREPANCY_L2_PLUS_MICROSCOPIC_DIAGONAL_PLUS_SPARSE_SWITCHING
```

is therefore sharpened to

```text
MEDIUM_DETERMINANT_DISPERSION
+ MICROSCOPIC_SMALL_SIDE_INDUCTION
+ NORM_MIXED_SIGN_D_TIMES_S_DISPERSION.
```

## 7. Consequence for the end-to-end retainer budget

14-4as requires an explicit local estimate

```text
S_Q <= rho_loc A_Q + E_loc
```

on the same nonnegative family used downstream.

After 4ax, the sparse six-linear second moment is no longer an uncontrolled source of `E_loc`. However:

- the genuine `N` diagonal still has to be assigned to a main/lower-dimensional term or canceled by additional structure;
- the medium determinant off-diagonal has no fixed-power theorem yet;
- state-split norm mixed-sign blocks remain open;
- the non-unit microscopic small-side range remains open.

Therefore no positive `delta_loc` is yet promoted to the end-to-end exponent budget.

## Boundary

```text
STAGE14_4AX=SPARSE_LINEAR_L2_IMPORTED_AND_MAIN_TRACK_FRONTIER_SHARPENED
S5J_SPARSE_LINEAR_L2_IMPORTED=true
SIX_LINEAR_RECIPROCAL_EDGES_PROJECTIVE=true
LINEAR_COLLISION_DIVIDES_DETERMINANT=true
SPARSE_LINEAR_THRESHOLD_Q_GT_2XY=true
SPARSE_LINEAR_DISCREPANCY_L2_DIAGONAL_SCALE_PROVED=true
N_SCALE_DIAGONAL_GENUINE=true
SPARSE_LINEAR_FIXED_POWER_RETAINER_SAVING_PROVED=false
MEDIUM_LINEAR_OFFDIAGONAL_REDUCED_TO_DETERMINANT=true
MEDIUM_LINEAR_L2_POWER_SAVING_PROVED=false
UNIT_MODULUS_RECIPROCAL_EDGE_RECLASSIFIED=true
FULL_MICROSCOPIC_SMALL_SIDE_CLOSED=false
NORM_SAME_SIGN_COLLISION_DIVIDES_DETERMINANT=true
NORM_OPPOSITE_SIGN_COLLISION_DIVIDES_ANTIDETERMINANT=true
FULL_STATE_SPLIT_E_SPARSE_REGIME_CLOSED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No `N`-scale diagonal is mislabeled as a removable error. No sparse L2 theorem is promoted to a fixed-power retainer. No medium determinant or norm mixed-sign theorem is claimed.

```text
NEXT=Stage14-4ay prove a medium-range determinant-dispersion estimate for the six linear reciprocal edges and organize the remaining microscopic small-side modes inductively, then isolate the state-split E mixed-sign D*S kernel as a separate norm problem
```
