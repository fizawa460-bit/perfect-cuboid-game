# Stage14-4ax — sparse linear dispersion and determinant collision boundary

## Result

Stage14-4aw reduced the local analytic remainder to three pieces:

```text
Delta L2 dispersion
+ microscopic lower-dimensional blocks
+ sparse large-state moduli.
```

Stage14-4ax closes the **sparse discrepancy problem for the six reciprocal edges among the four linear Euclid columns**

```text
m, n, m-n, m+n,
```

and identifies the correct second-moment diagonal. It also proves that the remaining medium-range linear discrepancy is supported on divisors of one determinant, while state-split pieces of `m^2+n^2` obey a different determinant/anti-determinant collision law.

This stage is self-contained on current `main`: it uses merged 14-4aw and s5i, and independently derives the projective collision reduction also found in the parallel s5j track.

## 1. Four linear columns are projective points

For a primitive pair `P=(m,n)` and an odd prime `p`, the four linear Euclid columns impose one projective slope in `P^1(F_p)`:

```text
m       : [m:n]=[0:1]
n       : [m:n]=[1:0]
m-n     : [m:n]=[1:1]
m+n     : [m:n]=[-1:1].
```

Let `u` and `v` be odd squarefree state moduli attached to two distinct linear columns. Their prime supports are disjoint on every primitive Euclid point, so `(u,v)=1`. By CRT the two divisibility conditions determine one projective class modulo

```text
q = u v.
```

For two primitive points

```text
P=(m,n),  P'=(m',n')
```

in the same cell, define

```text
D(P,P') = m*n' - m'*n.
```

At every prime dividing `q` the two points lie on the same projective slope, hence

```text
q | D(P,P').
```

For primitive positive integer pairs, `D(P,P')=0` implies `P=P'`.

## 2. Sparse collision threshold

Place the points in a rectangle

```text
0 < m,m' <= X,
0 < n,n' <= Y.
```

Then

```text
|D(P,P')| < 2XY.
```

Therefore

```text
q > 2XY
=> every linear-linear projective cell contains at most one primitive point.
```

This is an exact sparse-incidence theorem, not a heuristic density statement.

Let `W(u,v)` be the primitive opposite-parity incidence count in a fixed dyadic state cell. In the sparse linear range

```text
Q:=UV > 2XY
```

we have pointwise

```text
W(u,v) in {0,1}.
```

## 3. Sparse linear L2 discrepancy

Write the merged s5i rank-one main term as `M(u,v)` and

```text
Delta(u,v)=W(u,v)-M(u,v).
```

Let `N` be the number of primitive opposite-parity Euclid points in the geometric box. For a fixed point, the number of dyadic divisor pairs `(u,v)` attached to two fixed linear columns is `B^o(1)` by the divisor bound. Hence

```text
sum_{u~U,v~V} W(u,v)
  <<_epsilon N B^epsilon.
```

Because `W^2=W` in the sparse range,

```text
sum W(u,v)^2 <<_epsilon N B^epsilon.
```

The s5i main term satisfies schematically

```text
M(u,v) <<_epsilon N B^epsilon / Q,
```

and there are `O(Q)` dyadic modulus pairs, so

```text
sum M(u,v)^2
  <<_epsilon N^2 B^epsilon / Q
  <<_epsilon N B^epsilon
```

when `Q>2XY` and `N<=XY`.

Thus

```text
boxed:
sum_{u~U,v~V} |Delta(u,v)|^2
  <<_epsilon N B^epsilon
```

for every sparse linear-linear dyadic block.

This closes the uncontrolled **growth** of the sparse linear discrepancy: its second moment is at the natural same-point diagonal scale.

## 4. The N-scale diagonal is genuine

The `N` term is not an error that should be forced to `o(N)`. Expanding `sum W^2` produces a same-point contribution `P=P'`, and this diagonal is of order `N` up to divisor weights whenever points carry admissible divisor pairs.

The correct future dispersion target is therefore

```text
diagonal O(N B^epsilon)
+ off-diagonal power saving.
```

Two consequences must be kept separate:

1. the sparse linear `L2` problem is controlled to its sharp natural scale;
2. this **does not by itself provide a fixed-power local retainer saving**.

Indeed a naive Cauchy bound over all `O(Q)` cells gives `O(sqrt(QN) B^epsilon)`, which need not be smaller than `N` when `Q` is sparse. Directly using `W in {0,1}` gives an `O(N B^epsilon)` absolute bound, still only the base scale. Thus Stage14-4ax closes a dispersion blow-up, not the final `rho_loc` exponent.

## 5. Medium linear range becomes one determinant-divisor problem

When

```text
Q <= 2XY,
```

distinct points may share a cell. But every off-diagonal collision on any of the six linear-linear reciprocal edges still satisfies

```text
u v | D(P,P').
```

Hence the entire medium off-diagonal second moment is supported on divisors of

```text
D(P,P') = m*n' - m'*n.
```

The arbitrary-matrix obstruction has disappeared. What remains is a structured determinant-dispersion problem:

```text
sum_{P != P'}
#{u~U,v~V : uv | D(P,P'),
               u,v satisfy the two fixed linear-column state conditions}.
```

A divisor bound for each fixed nonzero determinant is only `B^o(1)`, but summing over all point pairs still has `N^2` scale. A genuine distribution/dispersion estimate for determinant values is therefore still required.

## 6. Exact unit-side reclassification

The most singular microscopic endpoint is now separated cleanly. If one reciprocal modulus is exactly `1`, then

```text
(1/v)=1,
```

so that edge is not a nonconstant reciprocal character at all. It must be reclassified into the Fourier graph with that edge deleted.

Therefore the exact `U=1` or `V=1` endpoint is a **lower-dimensional mode**, not a failed quadratic-large-sieve block. This removes the literal constant-character endpoint from the reciprocal-error ledger.

It does not close the full microscopic range `1<U<L^kappa`; slowly growing small sides can still fail to yield a fixed power of `L` and require an induction/switching argument.

## 7. State-split norm column has a D/S collision law

For a split odd prime `p|m^2+n^2`, choose `r^2=-1 mod p`. The norm projective roots are

```text
[m:n]=[+r:1], [-r:1].
```

For two points `P,P'`:

- if the same root sign is chosen at `p`, then `p | D(P,P')`;
- if opposite root signs are chosen, then

```text
p | S(P,P'),
S(P,P') = m*n' + m'*n.
```

Thus a state-split norm modulus factors as

```text
q_E = q_same q_opp,
q_same | D(P,P'),
q_opp  | S(P,P').
```

and only

```text
q_E | D(P,P') S(P,P')
```

is forced in general.

Since both `|D|` and `|S|` are `O(XY)`, a mixed-sign norm state can support modulus as large as `O((XY)^2)`. Consequently the linear sparse threshold `q>2XY` does **not** close the state-split `E` contribution.

This is the principal new sparse obstruction after the six linear edges are controlled.

## 8. Updated local ledger

The local path now reads

```text
14-4av : bare/interior linear reciprocal power saving
14-4aw : full-state bulk separable; Delta + endpoints isolated
14-4ax : sparse six-linear L2 = natural diagonal scale
          medium six-linear off-diagonal -> uv | determinant
          unit modulus -> lower-dimensional mode
          state-split E -> mixed determinant/anti-determinant D*S.
```

Thus the previous

```text
DISCREPANCY_L2_PLUS_MICROSCOPIC_DIAGONAL_PLUS_SPARSE_SWITCHING
```

is replaced by the sharper frontier

```text
MEDIUM_DETERMINANT_DISPERSION
+ MICROSCOPIC_SMALL-SIDE_INDUCTION
+ NORM_MIXED_SIGN_D_TIMES_S_DISPERSION.
```

## Boundary

```text
STAGE14_4AX=SPARSE_LINEAR_L2_CLOSED_AND_DETERMINANT_NORM_OBSTRUCTIONS_ISOLATED
SIX_LINEAR_RECIPROCAL_EDGES_PROJECTIVE=true
LINEAR_COLLISION_DIVIDES_DETERMINANT=true
SPARSE_LINEAR_THRESHOLD_Q_GT_2XY=true
SPARSE_LINEAR_DISCREPANCY_L2_DIAGONAL_SCALE_PROVED=true
SPARSE_LINEAR_L2_BOUND=O_epsilon(N*B^epsilon)
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

No `N`-scale diagonal is mislabeled as a removable error. No sparse linear `L2` estimate is promoted to a fixed-power local retainer. No norm mixed-sign closure or medium determinant dispersion theorem is claimed.

```text
NEXT=Stage14-4ay prove a medium-range determinant-dispersion estimate for the six linear reciprocal edges and organize the remaining microscopic small-side modes inductively, then isolate the state-split E mixed-sign D*S kernel as a separate norm problem
```
