# Stage14-s5j — projective collision dispersion and sparse-regime closure

## Purpose

Stage14-s5i reduced the Euclid divisibility weight to a separable rank-one bulk plus a discrepancy `Delta`. The next question is whether the discrepancy has an `L^2` dispersion bound strong enough to be paired with the s5h quadratic-large-sieve estimate.

This stage proves the sharp sparse-regime `L^2` bound for the four linear Euclid columns, identifies the unavoidable diagonal scale, and isolates the only new obstruction created by state-split pieces of `m^2+n^2`.

## 1. Projective roots of the five Euclid columns

For a primitive pair `P=(m,n)` and an odd prime `p`, the four linear columns correspond to one projective point of `P^1(F_p)`:

```text
A=m       : [m:n]=[0:1]
B=n       : [m:n]=[1:0]
C=m-n     : [m:n]=[1:1]
D=m+n     : [m:n]=[-1:1].
```

The norm column

```text
E=m^2+n^2
```

has no primitive projective root for `p=3 mod 4`, and exactly two roots

```text
[m:n]=[r:1], [-r:1],  r^2=-1 mod p
```

for `p=1 mod 4`.

Thus for pairwise-coprime squarefree state moduli on the four linear columns, CRT gives exactly one projective class modulo

```text
q=q_A q_B q_C q_D.
```

This is stronger than the arbitrary two-variable incidence picture left at s5h.

## 2. Collision determinant for the linear-four core

For two integer pairs

```text
P=(m,n),  P'=(m',n')
```

define

```text
D(P,P') = m*n' - m'*n.
```

If both points occupy the same projective class modulo an odd modulus `q`, then

```text
q | D(P,P').
```

For primitive positive pairs, `D(P,P')=0` implies `P=P'`: two primitive positive integer vectors on the same rational ray are identical.

Now place the points in a rectangle

```text
0 < m,m' <= X,
0 < n,n' <= Y.
```

Then

```text
|D(P,P')| < 2XY.
```

Therefore:

```text
q > 2XY
=> no two distinct primitive points can occupy the same linear-four CRT projective class mod q.
```

Equivalently, every such sparse projective cell contains at most one primitive Euclid point.

## 3. Sparse dyadic `L^2` dispersion bound

Fix a reciprocal edge between two distinct linear columns, and let `u~U`, `v~V` be odd squarefree state moduli on those two columns, with `(u,v)=1` and

```text
Q=UV > 2XY.
```

Let `W(u,v)` be the primitive Euclid incidence count in the fixed rectangle, and let `M(u,v)` be the separable s5i rank-one bulk. Put

```text
Delta(u,v)=W(u,v)-M(u,v).
```

The collision lemma gives

```text
W(u,v) in {0,1}
```

throughout this sparse range.

For a fixed primitive point `P`, the number of dyadic pairs `(u,v)` for which

```text
u | F_i(P),
v | F_j(P)
```

is bounded by the divisor function of the two factor values. Uniformly on a polynomial-height Stage14 box this is

```text
<<_epsilon B^epsilon.
```

Hence, with `N` the number of primitive points in the box,

```text
sum_{u~U}^* sum_{v~V}^* W(u,v)
  <<_epsilon N B^epsilon.
```

The s5i bulk has size

```text
M(u,v) <<_epsilon N B^epsilon / Q,
```

and there are `O(Q)` dyadic modulus pairs. Therefore

```text
sum M(u,v)^2
  <<_epsilon N^2 B^epsilon / Q
  <<_epsilon N B^epsilon
```

when `Q>2XY` and `N<=XY`.

Using `(a-b)^2<=2a^2+2b^2` and `W^2=W`, we obtain the sparse dispersion theorem

```text
sum_{u~U}^* sum_{v~V}^* |Delta(u,v)|^2
  <<_epsilon N B^epsilon.
```

This is exactly the natural diagonal scale and is sufficient for Cauchy-Schwarz without losing a positive power in the sparse linear-four regime.

## 4. The diagonal scale is genuine

The `N` term is not an artifact of the proof. In the second-moment expansion

```text
sum_{u,v} W(u,v)^2
```

the contribution `P=P'` is precisely the same-point diagonal. Whenever a positive proportion of points has at least one admissible dyadic divisor pair, this contribution is of order `N` up to divisor weights.

Thus a generic target `o(N)` for the full incidence second moment is false or at least misaligned with the actual combinatorics. The correct objective is

```text
L2 dispersion = diagonal O(N B^epsilon)
                + off-diagonal power-saving/error.
```

s5j therefore fixes the diagonal scale rather than trying to remove it.

## 5. Medium range becomes a determinant-divisor problem

For `Q<=2XY`, distinct points may collide. For a linear-linear edge every off-diagonal collision necessarily satisfies

```text
u*v | D(P,P').
```

Hence the off-diagonal second moment is supported on divisors of one bilinear determinant. Schematically,

```text
OffDiag(U,V)
<= sum_{P != P'}
   #{u~U, v~V : uv | D(P,P'),
                    u|F_i(P)F_i(P'),
                    v|F_j(P)F_j(P')}.
```

The divisor multiplicity of a fixed nonzero determinant is only `B^epsilon`, but summing over all point pairs still requires cancellation or distribution of the determinant values. This is now a much narrower problem than an arbitrary matrix `W(u,v)`.

The next medium-range analytic target is a determinant-dispersion estimate, equivalently a two-dimensional large-sieve / divisor-switching bound for

```text
D(P,P') = m*n' - m'*n.
```

## 6. Why the norm column has a different collision law

At a split prime `p|m^2+n^2`, choose a square root `r^2=-1 mod p`. If two points use the same root sign, then

```text
p | D(P,P').
```

If they use opposite root signs, then instead

```text
p | S(P,P'),
S(P,P') = m*n' + m'*n.
```

Therefore a state-split norm modulus `q_E` decomposes as

```text
q_E = q_same * q_opp,
q_same | D(P,P'),
q_opp  | S(P,P').
```

so only

```text
q_E | D(P,P') S(P,P')
```

is forced in general.

Since both `|D|` and `|S|` are `O(XY)`, mixed root signs can support moduli as large as `O((XY)^2)`. Thus the linear-four sparse closure at `Q>2XY` does **not** automatically close state-split `E` pieces.

This is the persistent obstruction isolated by s5j. It is consistent with s5h: the whole `E` kernel collapses, but individual state-split `E` pieces can reintroduce bilinearity.

## 7. Deterministic audit

The accompanying standard-library audit checks:

- the four unique projective linear roots for every odd prime tested;
- split/inert root count of `m^2+n^2`;
- the determinant collision identity for every linear-column pair;
- the exact same-sign / opposite-sign `E` collision dichotomy;
- for finite primitive boxes, the maximal common linear-linear squarefree modulus for any distinct point pair never exceeds `|D(P,P')|<2XY`;
- no sparse linear-four projective cell above the determinant threshold contains two distinct primitive points;
- finite second-moment ledgers separate same-point diagonal from off-diagonal collisions.

The finite audit is consistency evidence only. The sparse `L^2` theorem is carried by the determinant collision lemma plus divisor bounds and the s5i rank-one bulk estimate.

## Boundary

```text
STAGE14_S5J=COMPLETE_PROJECTIVE_COLLISION_REDUCTION_AND_SPARSE_LINEAR_L2_BOUND
LINEAR_FOUR_CRT_CLASS_UNIQUE=true
LINEAR_COLLISION_DIVIDES_DETERMINANT=true
SPARSE_LINEAR_REGIME_THRESHOLD=q>2XY
SPARSE_LINEAR_L2_DISPERSION=O_epsilon(N*B^epsilon)
N_SCALE_DIAGONAL_UNAVOIDABLE=true
MEDIUM_LINEAR_OFFDIAGONAL_REDUCED_TO_DETERMINANT_DIVISORS=true
NORM_SAME_SIGN_COLLISION_DIVIDES_DETERMINANT=true
NORM_OPPOSITE_SIGN_COLLISION_DIVIDES_ANTIDETERMINANT=true
STATE_SPLIT_E_MIXED_SIGN_OBSTRUCTION_PERSISTS=true
MEDIUM_RANGE_L2_DISPERSION_PROVED=false
FULL_STATE_SPLIT_E_SPARSE_REGIME_CLOSED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5k prove the medium-range determinant-dispersion estimate for the six linear-four reciprocal edges, then treat the state-split E mixed-sign D*S kernel separately
```
