# Stage14-s5k — six-edge linear medium dispersion theorem

## Purpose

Stage14-s5j reduced every off-diagonal collision among the four linear Euclid columns

```text
A=m,
B=n,
C=m-n,
D=m+n
```

to divisors of the determinant `mn'-m'n`, and closed the sparse range `q>2XY` at the natural diagonal scale.  The remaining task was to obtain a genuine medium-range `L^2` estimate for the six reciprocal edges among `A,B,C,D`.

For these six edges one can do better than a generic determinant-divisor estimate.  Any two distinct linear columns form an integral coordinate system of determinant `±1` or `±2`.  Because all moving state moduli are odd and the Stage14 family is opposite-parity, the factor `2` causes only a fixed parity-lattice condition.  Primitive incidence can therefore be counted directly in the two selected linear coordinates by an elementary Möbius/lattice-point argument.

This stage proves a pointwise discrepancy estimate and sums it over every medium dyadic block.  No external analytic theorem is needed for this step.

## 1. Six linear coordinate pairs

For `L=(A,B,C,D)` the six ordered-unoriented pairs have coefficient determinants

```text
(A,B) :  1
(A,C) : -1
(A,D) :  1
(B,C) : -1
(B,D) : -1
(C,D) :  2.
```

Hence for every pair `i<j`,

```text
T_ij : (m,n) -> (x,y)=(L_i(m,n),L_j(m,n))
```

is an integral linear map of determinant `1` in absolute value except for `(C,D)`, where the determinant is `2`.

At odd primes the map is invertible in all six cases.  For `(C,D)`, opposite parity of `(m,n)` makes `C,D` odd, so the image is one fixed parity coset and the factor `2` remains completely fixed.

Moreover odd common divisors are preserved:

```text
gcd_odd(m,n)=gcd_odd(L_i(m,n),L_j(m,n))
```

for every one of the six pairs.  Since the Stage14 Euclid family is opposite-parity, primitiveness is therefore equivalent to

```text
gcd(x,y)=1
```

inside the appropriate fixed parity lattice.

This is the key simplification absent from a generic projective-incidence problem.

## 2. Primitive divisibility count in linear coordinates

Let `Omega` be a Stage14 dyadic Euclid box (or its intersection with `m>n`) and write

```text
A_Omega = area(Omega).
```

For a selected linear edge `(i,j)`, let `H_i,H_j` denote the coordinate widths of `T_ij(Omega)` in the `x=L_i` and `y=L_j` directions.  Thus in a rectangular box `0<m<=X, 0<n<=Y`, one may take

```text
H_A <= X,
H_B <= Y,
H_C,H_D <= X+Y.
```

Let `u,v` be odd squarefree moduli with `(u,v)=1`, placed on different linear columns, and define

```text
W_ij(u,v)
 = #{(m,n) in Omega :
      gcd(m,n)=1,
      m,n opposite parity,
      u | L_i(m,n),
      v | L_j(m,n)}.
```

Put

```text
lambda(q) = product_{p|q} 1/(p+1).
```

The primitive opposite-parity bulk is

```text
M_ij(u,v) = (4/pi^2) A_Omega lambda(u) lambda(v),
```

up to the fixed boundary convention of the dyadic box.  The same formula applies to polygonal sub-boxes by replacing the rectangular area with `A_Omega`.

### Local factor check

At an odd prime `p`, among primitive residue vectors `(m,n) != (0,0) mod p`, any one linear projective root has `p-1` vectors out of `p^2-1`.  Therefore

```text
Prob(p | L_i | primitive mod p) = 1/(p+1).
```

Distinct linear columns are distinct projective roots, so the same prime cannot occur in two different state columns of a primitive pair.  This is exactly the `lambda` factor inherited from s5i.

## 3. Pointwise discrepancy theorem

Define

```text
Delta_ij(u,v)=W_ij(u,v)-M_ij(u,v).
```

Then for every `epsilon>0`, uniformly for odd squarefree coprime `u,v`,

```text
|Delta_ij(u,v)|
  <<_epsilon B^epsilon
     (1 + H_i/u + H_j/v).
```

Here `B` is any fixed polynomial height dominating the Stage14 dyadic box and its linear factor values.

### Proof

Use the coordinates `(x,y)=(L_i,L_j)`.  The transformed region is a convex polygon with coordinate widths `H_i,H_j`, inside a fixed lattice/coset of covolume `1` or `2`.

Primitiveness is `gcd(x,y)=1`.  Apply Möbius inversion

```text
1_{gcd(x,y)=1} = sum_{d|x,y} mu(d).
```

Only odd `d` matter after the fixed opposite-parity condition.  Since `u,v` are coprime squarefree, split uniquely

```text
d = a*b*c,
a | u,
b | v,
(c,uv)=1.
```

Then

```text
lcm(u,d)=u*b*c,
lcm(v,d)=v*a*c.
```

For fixed `(a,b,c)`, lattice-point counting in the transformed polygon gives the area term plus boundary error

```text
O(
  H_i/(u*b*c)
 +H_j/(v*a*c)
 +1
).
```

Summing the area terms over `a,b,c` produces the Euler factors

```text
1-1/p^2        for p not dividing uv,
(1/p)(1-1/p)  for p dividing u or v,
```

and therefore, relative to primitive density,

```text
[(1/p)(1-1/p)]/(1-1/p^2)=1/(p+1).
```

This yields `(4/pi^2)A_Omega lambda(u)lambda(v)`.

For the boundary terms, summation over `a|u,b|v` costs only divisor factors `B^epsilon`; the harmonic `c`-sum contributes a logarithm absorbed into `B^epsilon`.  The accumulated `+1` terms are bounded by the available transformed side lengths,

```text
min(H_i/(u*b), H_j/(v*a))
 <= H_i/(u*b)+H_j/(v*a),
```

so they do not create a new large term.  Hence

```text
Delta_ij(u,v)
 <<_epsilon B^epsilon(1+H_i/u+H_j/v).
```

This proves the pointwise theorem.

## 4. Medium dyadic `L^2` dispersion

Let

```text
u ~ U,
v ~ V,
Q=UV,
```

with odd squarefree coprime support.  Squaring the pointwise bound and summing over the `O(UV)` dyadic modulus pairs gives

```text
sum_{u~U}^* sum_{v~V}^*
  |Delta_ij(u,v)|^2

<<_epsilon B^epsilon
  ( Q
   + H_i^2 V/U
   + H_j^2 U/V ).
```

This is the first full medium-range dispersion theorem for all six linear-four reciprocal edges.  It is valid on both sides of the s5j sparse threshold; s5j remains sharper in the very sparse range because there the second moment collapses exactly to the same-point diagonal.

### Balanced corridor

If the dyadic aspect ratio matches the geometric aspect ratio,

```text
U/V ~ H_i/H_j,
```

then

```text
H_i^2 V/U + H_j^2 U/V << H_i H_j,
```

so

```text
sum |Delta_ij|^2
 <<_epsilon B^epsilon (Q + H_i H_j).
```

For a Stage14 box with `H_i H_j` on the physical point-count scale, this is the desired diagonal-size dispersion throughout the balanced medium range.

## 5. Direct reciprocal-error corollary

For any unit-modulus reciprocal kernel, in particular `(u/v)`, Cauchy-Schwarz gives

```text
| sum_{u~U} sum_{v~V} Delta_ij(u,v) (u/v) |

<= Q^(1/2) (sum |Delta_ij(u,v)|^2)^(1/2)

<<_epsilon B^epsilon
   ( Q + H_i V + H_j U ).
```

In the balanced corridor this becomes schematically

```text
<<_epsilon B^epsilon
   ( Q + sqrt(H_i H_j Q) ).
```

Thus for `Q=o(H_i H_j)` the discrepancy part itself has a power saving against the physical `H_iH_j` scale.  The transition `Q~H_iH_j` naturally returns to diagonal size; s5j showed that this diagonal is genuine rather than a proof artifact.

This corollary is independent of the s5h quadratic large sieve.  The large sieve is still used on the separable rank-one bulk; s5k controls the nonseparable finite-box discrepancy directly.

## 6. What remains after the six linear edges

The six reciprocal edges among `A,B,C,D` no longer have an unidentified medium-range incidence obstruction.  Their pure Euclid divisibility discrepancy now has:

1. the s5j exact sparse bound;
2. the s5k pointwise boundary estimate;
3. the s5k medium dyadic `L^2` estimate;
4. a direct reciprocal-error bound in every dyadic block.

Two tasks remain before a family large-sieve theorem can be claimed.

First, the full s5 character polynomial contains several simultaneous state pieces, so the six one-edge bounds must be summed with the rank-one large-sieve bulk without losing the target exponent through dyadic multiplicity or imbalanced blocks.

Second, state-split pieces of

```text
E=m^2+n^2
```

still have the mixed-sign collision law from s5j:

```text
q_same | D(P,P'),
q_opp  | S(P,P')=mn'+m'n.
```

The linear coordinate argument above does not turn `E` into an integral linear coordinate, so it does not close that `D*S` kernel.

## 7. Deterministic audit

The accompanying audit checks:

- all six linear coefficient determinants are `±1` or `±2`;
- odd gcd preservation for all six coordinate pairs on a finite opposite-parity box;
- exact equivalence between direct primitive incidence and the finite Möbius formula in transformed coordinates;
- the `1/(p+1)` primitive local factor by exact finite-field enumeration;
- finite dyadic discrepancy ledgers for all six edges;
- empirical `L^2` values against the proved envelope
  `Q + H_i^2 V/U + H_j^2 U/V`.

The finite ledger is regression evidence only.  The theorem is the elementary Möbius/lattice-point argument above.

## Boundary

```text
STAGE14_S5K=COMPLETE_SIX_LINEAR_MEDIUM_DISPERSION_THEOREM
LINEAR_SIX_COORDINATE_DETERMINANTS_ABS_LE_2=true
LINEAR_SIX_ODD_GCD_PRESERVED=true
LINEAR_SIX_POINTWISE_DISCREPANCY_PROVED=true
MEDIUM_LINEAR_L2_DISPERSION_PROVED=true
BALANCED_LINEAR_MEDIUM_DIAGONAL_SCALE_PROVED=true
LINEAR_RECIPROCAL_DISCREPANCY_BOUND_PROVED=true
FULL_LINEAR_SIX_DYADIC_SUMMATION_PROVED=false
STATE_SPLIT_E_MIXED_SIGN_OBSTRUCTION_PERSISTS=true
FULL_STATE_SPLIT_E_SPARSE_REGIME_CLOSED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5l combine the s5h rank-one quadratic-large-sieve bulk with the s5k six-edge discrepancy bounds across all dyadic blocks, then isolate the first quantitative bound for the state-split E mixed-sign D*S kernel
```
