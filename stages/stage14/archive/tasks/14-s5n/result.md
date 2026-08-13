# Stage14-s5n — one-small-variable boundary averaging and multi-edge conductor obstruction

## Purpose

Stage14-s5m reduced every large linear boundary strip to an exact complementary-divisor form with one small cofactor and a physical quadratic character. It also left explicit small-state strips. This stage proves that those **single-edge one-small-variable boundary operators** can be averaged with power saving, and then asks whether the resulting estimates assemble term-by-term across the full finite local character polynomial.

The answer is mixed:

- for each individual reciprocal edge among `A=m`, `B=n`, `C=m-n`, `D=m+n`, the small-state and switched-large boundary strips are now quantitatively controlled;
- a common regular-box cutoff `Z=M^(2/5)` is compatible with the earlier s5l/s5m central estimates and gives a positive power saving on every single-edge linear dyadic sector;
- however a monomial in the full local character polynomial can contain several reciprocal edges incident to the same state variable. Multiplying those characters multiplies their conductors. The elementary one-variable completion bound then sees the **product conductor**, and degree two or three can erase the single-edge saving.

Thus s5n isolates the first genuinely final-looking assembly obstruction: not Euclid incidence, not mixed-sign `E`, and not one-small-variable boundaries, but **multi-edge conductor pile-up at a common reciprocity vertex**.

No new external theorem is used. The only character-sum input is proved below from the elementary Gauss-sum completion bound.

## 1. Squarefree incomplete quadratic-character lemma

Let `q` be odd squarefree and let

```text
chi_q(n)=(n/q)
```

be the primitive real Jacobi character modulo `q`. For any interval `I` of length `T`,

```text
sum_{n in I} mu(n)^2 chi_q(n)
 << T^(1/2) q^(1/4) log(2q)^(1/2).
```

The same estimate holds after finitely many fixed coprimality or residue-class restrictions, at the cost of a `B^epsilon` factor in Stage14 ranges.

### Proof

The ordinary completion argument for a primitive character gives

```text
max_I |sum_{n in I} chi_q(n)|
 << sqrt(q) log(2q).
```

Indeed, expand the interval indicator into additive Fourier modes modulo `q`; the nonzero Fourier coefficients cost `sum_{h<=q} 1/h`, while every twisted complete character sum is a Gauss sum of absolute value `sqrt(q)`.

Now use

```text
mu(n)^2 = sum_{d^2|n} mu(d).
```

If `(d,q)>1`, the corresponding character term vanishes. Otherwise `chi_q(d^2)=1`, so

```text
S(I)=sum_d mu(d)
     sum_{m: d^2 m in I} chi_q(m).
```

Put

```text
A=sqrt(q) log(2q).
```

For `d<=D` use the completed bound `A`; for `d>D` use the trivial length `T/d^2`. Hence

```text
|S(I)| << D A + T/D.
```

Taking `D~sqrt(T/A)` when `T>=A`, and using the trivial bound when `T<A`, gives

```text
|S(I)| << sqrt(TA)
       << T^(1/2) q^(1/4) log(2q)^(1/2).
```

This is the boundary-operator input of s5n.

A partial-summation corollary used below is

```text
sum_{n~N} mu(n)^2 chi_q(n)/n
 << N^(-1/2) q^(1/4) B^epsilon.
```

## 2. Small-state linear boundary operator

Fix one linear reciprocal edge `(i,j)`. In the integral coordinates

```text
x=L_i(m,n),
y=L_j(m,n),
```

the determinant is `1` or `2`, so opposite parity contributes only a fixed lattice coset. Let the coordinate widths be `H_i,H_j`, and put

```text
G_ij=H_i H_j.
```

Consider a dyadic block

```text
u~U,
v~V,
```

with `u` the small state modulus on `x`, `v|y`, and kernel `(u/v)`. After primitive Möbius inversion and the fixed parity bookkeeping, the relevant sum has the same shape as

```text
sum_{u~U} sum_{x: u|x}
 sum_{v~V, v|y} mu(v)^2 (u/v),
```

up to `B^epsilon` divisor multiplicity and bounded state characters.

For fixed `u`, summing first over the physical `y`-coordinate gives

```text
sum_{v~V} mu(v)^2 (u/v) floor(H_j/v).
```

Write `floor(H_j/v)=H_j/v+O(1)`. The squarefree character lemma plus partial summation gives

```text
sum_{v~V} mu(v)^2 (u/v)/v
 << B^epsilon V^(-1/2) u^(1/4).
```

The `O(1)` remainder costs `O(V)`. There are `O(H_i/u)` admissible `x`-values. Summing `u~U` therefore gives the single-edge small-state boundary theorem

```text
|Small_ij(U,V)|
 <<_epsilon B^epsilon [
      G_ij U^(1/4) V^(-1/2)
      + H_i V
   ].
```

The symmetric estimate holds with `i,j` and `U,V` interchanged.

### Consequence

If

```text
U<=Z,
Z<=V<=H_j/Z,
```

then

```text
|Small_ij(U,V)|
 <<_epsilon B^epsilon G_ij
    [ Z^(-1/4)+Z^(-1) ].
```

Thus a small state modulus is not itself an obstruction once the other side is outside the microscopic range.

## 3. Switched large-state boundary operator

Now suppose the original `u|x` lies on the large strip

```text
u>H_i/Z.
```

By s5m write exactly

```text
x=k*u,
0<k<Z,
```

and rewrite

```text
(u/v)=(|x|/v)(k/v).
```

Since `x=ku`, the two factors reduce, up to the fixed sign character, to the quadratic character of the reconstructed squarefree state `u` modulo `v`. Thus after switching the oscillatory variable is again the long variable `u`, but the geometric cofactor `k` is short.

For a dyadic cofactor block `k~K`, fixed `k,v`, the physical `u`-interval has length `O(H_i/K)`. The squarefree character lemma gives

```text
sum_u mu(u)^2 (u/v)
 <<_epsilon
 B^epsilon (H_i/K)^(1/2) V^(1/4).
```

The other coordinate has `O(H_j/V)` multiples of `v`. Summing `k~K` and `v~V` yields

```text
|Switch_ij(K,V)|
 <<_epsilon B^epsilon
 H_j H_i^(1/2) K^(1/2) V^(1/4).
```

The symmetric estimate holds for a large `v` strip.

On a regular box `H_i,H_j~M`, with `K<=Z` and `V<=M`,

```text
|Switch_ij|/G_ij
 <<_epsilon B^epsilon
 Z^(1/2) M^(-1/4).
```

Hence any choice

```text
Z<=M^(1/2-delta)
```

gives a power saving.

## 4. The small/large corner after switching the other side

Suppose `u` is small but `v` lies on the large `y`-strip. Write

```text
y=l*v,
0<l<Z.
```

Quadratic reciprocity on fixed mod-4 classes gives

```text
(u/v)=fixed_sign*(v/u)
     =fixed_sign*(y/u)*(l/u).
```

Since `y=lv`, this again reduces to a squarefree quadratic character in the reconstructed long variable `v` modulo the small modulus `u`.

For dyadic `u~U`, `l~L`, the squarefree character lemma gives

```text
|Corner_ij(U,L)|
 <<_epsilon B^epsilon
 H_i H_j^(1/2) U^(1/4) L^(1/2).
```

Thus on a regular box

```text
|Corner_ij|/G_ij
 <<_epsilon B^epsilon
 Z^(3/4) M^(-1/2).
```

This saves whenever `Z<<M^(2/3)`.

## 5. A common cutoff closes every single-edge linear boundary sector

Take a regular Stage14 Euclid box with

```text
H_A,H_B,H_C,H_D ~ M,
G~M^2,
P~M.
```

Choose

```text
Z=M^(2/5).
```

This one cutoff is simultaneously compatible with all earlier interfaces:

1. s5l linear central blocks save `Z^(-1/2)=M^(-1/5)`;
2. s5m central `E` condition `Z^3>P*B^eta` is compatible because `Z^3=M^(6/5)`;
3. switched large linear strips save
   `Z^(1/2)M^(-1/4)=M^(-1/20)`;
4. small-state/medium strips save at least `Z^(-1/4)=M^(-1/10)`;
5. small/large switched corners save
   `Z^(3/4)M^(-1/2)=M^(-1/5)`.

So the worst **single linear reciprocal edge** boundary exponent furnished by this elementary synthesis is

```text
M^(-1/20+epsilon).
```

## 6. Microscopic two-small blocks are locally centered, not resonant

The preceding small-state estimate gives a power saving once the larger dyadic side tends to infinity. A finite microscopic block still needs the local centering introduced at s5g.

Let `Psi_q(m,n)` be one centered local row after expanding raw characters as

```text
raw trace = centered trace + exact local mean.
```

For a fixed odd squarefree modulus `q`, CRT makes `Psi_q` periodic modulo `q`, and its exact mean over primitive-compatible nonvanishing residue classes is zero.

For a convex box `Omega` with perimeter `P`, complete `q x q` residue cells cancel exactly. After Möbius inversion for global primitiveness, only boundary cells remain. One obtains the fixed-conductor periodic estimate

```text
sum_{P in Omega primitive/opposite parity} Psi_q(P)
 <<_epsilon B^epsilon (P q + q^2).
```

Therefore truly microscopic centered blocks carry boundary size rather than area size. They are not a hidden recurrence of the raw resonances seen in s5g.

For a single reciprocal edge with `U,V<=W`, the combined conductor is `q<<W^2`, so choosing, for example,

```text
W=M^(1/10)
```

gives

```text
Pq+q^2 << M^(6/5)+M^(2/5)=o(M^2).
```

Together with the previous estimates, this proves full dyadic power saving for every **individual** linear reciprocal edge.

## 7. What fails when the full local polynomial is assembled naively

The full s5 local character polynomial is a finite sum of monomials in reciprocal edges. A state variable can be incident to several edges at once.

Suppose one long squarefree variable `u` is incident to pairwise-coprime neighbor moduli

```text
v_1,...,v_d.
```

Then multiplicativity gives exactly

```text
product_{j=1}^d (u/v_j)
 = (u/V_*),
V_*=product_j v_j.
```

Thus the one-variable squarefree completion lemma sees the **product conductor** `V_*`, not the individual conductors. Its bound is

```text
T^(1/2) V_*^(1/4) B^epsilon.
```

For one edge (`d=1`) this is precisely the saving used above. But on a regular scale with `T~M` and each `v_j~M`,

```text
d=1:  M^(1/2) M^(1/4) = M^(3/4)  (saving),
d=2:  M^(1/2) M^(1/2) = M        (no power saving),
d=3:  M^(1/2) M^(3/4) > M        (trivial bound wins).
```

The linear reciprocity graph on `A,B,C,D` is `K_4`, so degree two and degree three monomials are structurally possible in a naive edgewise expansion. This is the first precise exponent loss that prevents s5n from declaring the full local character polynomial averaged.

Crucially, this is **not** a return of the old arbitrary-matrix obstruction. The incidence and every one-edge boundary operator are controlled. What remains is a graph-assembly problem: exploit the simultaneous reciprocity graph (for example by iterated quadratic large sieve, graph orientation, or a higher-rank mean-value inequality) without paying the product conductor at one vertex.

## 8. Status after s5n

What is now proved:

- all six linear reciprocal edges have central dyadic saving from s5l;
- all six linear reciprocal edges have single-edge small-state boundary saving;
- all six linear reciprocal edges have exact switched-large boundary saving;
- microscopic fixed-conductor rows are controlled after exact s5g centering;
- for regular boxes, `Z=M^(2/5)` gives a uniform positive single-edge exponent, worst case `M^(-1/20+epsilon)`;
- medium and sparse `E` incidence are already structurally controlled by s5l/s5m.

What remains:

- simultaneous products of two or three reciprocal edges sharing one state variable;
- the associated product-conductor loss in the squarefree physical character sum;
- final assembly with state-split `E` terms and the finite `Q_2` cases;
- only after that can a genuine family large-sieve theorem be claimed.

## Deterministic audit

The accompanying audit checks:

- exact Jacobi multiplicativity for one, two, and three neighbor conductors;
- squarefree incomplete quadratic-character sums against the `T^(1/2)q^(1/4)` envelope on representative primitive Jacobi characters;
- weighted dyadic `1/n` corollaries numerically;
- exact large-divisor/complement switch identities on primitive Euclid points;
- finite small-state and switched-boundary ledgers against the theorem shapes;
- the exponent ledger for the common cutoff `Z=M^(2/5)`;
- explicit conductor pile-up factors for degrees one, two, and three.

Finite computation is regression evidence only. The analytic statements are carried by Gauss completion, the squarefree sieve identity, coordinate counting, and the exact switch from s5m.

## Boundary

```text
STAGE14_S5N=COMPLETE_ONE_SMALL_VARIABLE_BOUNDARY_AVERAGING_AND_MULTI_EDGE_CONDUCTOR_OBSTRUCTION
SQUAREFREE_QUADRATIC_COMPLETION_LEMMA_PROVED=true
SINGLE_EDGE_SMALL_STATE_BOUNDARY_AVERAGED=true
SINGLE_EDGE_SWITCHED_PHYSICAL_CHARACTER_AVERAGED=true
SINGLE_EDGE_SMALL_LARGE_CORNER_AVERAGED=true
MICROSCOPIC_CENTERED_PERIODIC_BOUND_PROVED=true
REGULAR_BOX_COMMON_CUTOFF_Z_EQ_M_2_5_VALID=true
SINGLE_LINEAR_EDGE_FULL_DYADIC_SUMMATION_PROVED=true
ALL_SIX_LINEAR_EDGES_INDIVIDUALLY_CLOSED=true
MULTI_EDGE_PRODUCT_CONDUCTOR_OBSTRUCTION_ISOLATED=true
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5o exploit the K4 reciprocity-graph structure with an iterated quadratic-large-sieve/graph-orientation argument to control degree-2 and degree-3 product conductors, or exhibit a persistent resonant subgraph
```
