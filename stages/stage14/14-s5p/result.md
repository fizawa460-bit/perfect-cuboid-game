# Stage14-s5p — auxiliary progression uniformity and tensor-energy reduction

## Purpose

Stage14-s5o removed the apparent degree-2/degree-3 product-conductor obstruction in the linear `K4` reciprocity graph, but it deliberately froze all remaining Euclid state pieces. The unresolved question was whether the s5k linear discrepancy theorem, the s5m signed-root `E=m^2+n^2` lattice theorem, and the s5n one-small-variable boundary estimates survive **uniformly** when those frozen state pieces impose additional arithmetic progressions.

This stage proves that they do.

The main points are:

1. after two moving state moduli are chosen, every collection of frozen odd state constraints is one additional projective progression modulo the product auxiliary modulus;
2. for a linear-linear moving edge, this auxiliary progression causes **no loss in its modulus**: the pointwise error is controlled by the shorter of the two scaled coordinate lengths;
3. for a linear-`E` moving edge with a fixed norm root, adding auxiliary state congruences only restricts the s5m lattice, so its shortest vector cannot decrease;
4. the s5n squarefree incomplete quadratic-character lemma remains valid inside an arbitrary coprime auxiliary arithmetic progression, with the expected `A^{-1/2}` gain from the reduced interval length;
5. summing auxiliary labels at the second-moment level costs only `B^epsilon`, because each physical Euclid point carries only divisor-many compatible state labels;
6. the quadratic large sieve lifts verbatim to Hilbert-space-valued coefficients.

Therefore the **progression modulus itself is no longer an obstruction**. The remaining assembly problem is narrower: contract the resulting Hilbert/tensor discrepancy energies through several simultaneously active reciprocal edges, especially when a state-split `E` edge is active. This stage does not claim that final tensor contraction.

No new external theorem is used. The only external analytic input remains the quadratic large sieve already contracted in s5h; its Hilbert-space lift is formal.

## 1. State columns and pairwise odd support

Use the five Euclid factors

```text
A=m,
B=n,
C=m-n,
D=m+n,
E=m^2+n^2.
```

For a primitive opposite-parity Euclid pair, odd prime support of these five factors is pairwise disjoint. Every odd prime in an `E` state is `1 mod 4`.

Write the four linear forms as

```text
L_A=m,
L_B=n,
L_C=m-n,
L_D=m+n.
```

Every pair of distinct linear coefficient vectors has determinant `±1` or `±2`. Hence every such determinant is a unit modulo every moving odd state prime.

For a split `E` prime `p`, a fixed root state is

```text
m == r_p n (mod p),
r_p^2 == -1 (mod p).
```

The projective root `r_p` is distinct from the four linear roots `0,infinity,+1,-1` modulo every odd prime. Thus an `E` root congruence is also transverse to every linear column.

## 2. Projective CRT for frozen auxiliary states

Fix two distinct moving linear columns `i,j`. Put

```text
x=L_i(m,n),
y=L_j(m,n).
```

The integral change `(m,n)->(x,y)` has determinant `±1` or `±2`, so after the fixed opposite-parity coset is recorded it is invertible at every odd state prime.

Let `u|x`, `v|y` be the moving odd squarefree state moduli, and freeze any collection of state moduli on the remaining columns. If a frozen `E` piece is present, fix one of its signed roots first. Let `A_aux` be the product of all frozen odd moduli. Pairwise support disjointness gives `gcd(A_aux,uv)=1`.

Write `x=u*r`, `y=v*s`. Every frozen linear state has, in `(x,y)` coordinates, the form

```text
alpha*x + beta*y == 0 (mod a),
```

with both `alpha,beta` units modulo every prime of `a`, because the auxiliary projective root is distinct from the two moving roots. The same is true for a fixed signed `E` root. Therefore each frozen state determines

```text
s == c_a r (mod a).
```

CRT combines all frozen states into exactly one progression

```text
s == c r (mod A_aux).
```

Thus arbitrarily many frozen state pieces do not create a higher-dimensional congruence object. They create one modular graph in the two scaled moving coordinates.

## 3. Uniform linear-linear auxiliary discrepancy

Let `Omega` be a convex Stage14 Euclid box. In `(x,y)` coordinates let the two coordinate widths be `H_i,H_j`.

For fixed auxiliary data `sigma=(A_aux,c,2-adic state,root labels)` define `W^sigma_ij(u,v)` to count primitive opposite-parity points in `Omega` satisfying `u|L_i`, `v|L_j`, and all frozen auxiliary state constraints `sigma`.

Let `rho(sigma)` be the exact odd local density of the frozen root cells. For one fixed projective root at a prime `p` the primitive relative density is `1/(p+1)`. Hence

```text
M^sigma_ij(u,v)
 = c_Omega * rho(sigma) * lambda(u)*lambda(v),

lambda(q)=prod_{p|q} 1/(p+1).
```

Define `Delta^sigma_ij=W^sigma_ij-M^sigma_ij`.

### Theorem 3.1 — fixed-auxiliary pointwise bound

Uniformly in the size of `A_aux`,

```text
|Delta^sigma_ij(u,v)|
 <<_epsilon B^epsilon [1+min(H_i/u,H_j/v)].
```

After the moving divisibilities are removed, the frozen conditions are `s==c r (mod A_aux)` inside a convex region whose widths are `H_i/u` and `H_j/v`. Slice first by `r`: every admissible `r` sees one residue class in the `s`-interval, producing error `O(1+H_i/u)`. Slice instead by `s`; since `c` is a unit modulo `A_aux`, this gives `O(1+H_j/v)`. Take the smaller bound.

Apply the same rational Möbius inversion as in s5k to impose primitiveness. Coprime Möbius factors dilate the scaled region; factors meeting state moduli contribute divisor multiplicity. Harmonic sums and the finite parity/root cases are absorbed into `B^epsilon`. The area terms reproduce the exact product of projective local densities.

The important feature is the absence of any positive power of `A_aux`.

### Corollary 3.2 — dyadic L2

For `u~U`, `v~V`,

```text
sum |Delta^sigma_ij(u,v)|^2
 <<_epsilon B^epsilon UV
 [1+min(H_i/U,H_j/V)^2].
```

Against a unit-modulus reciprocal kernel, Cauchy-Schwarz gives

```text
|sum Delta^sigma_ij(u,v)(u/v)|
 <<_epsilon B^epsilon UV
 [1+min(H_i/U,H_j/V)].
```

The estimate is uniform in every frozen auxiliary modulus and root pattern.

## 4. Full fixed state tuple is one projective lattice

Let `q_A,q_B,q_C,q_D,e` be pairwise odd-coprime squarefree state moduli, with `e` split, and fix one signed root modulo `e`. At each prime the state condition selects one projective line in `P^1(F_p)`. CRT therefore gives one primitive projective class modulo

```text
Q=q_A q_B q_C q_D e.
```

The corresponding lattice `Lambda_sigma` has index `Q`.

Let `q_(2)` denote the second largest of `q_A,q_B,q_C,q_D`, with missing state moduli interpreted as `1`. Every nonzero vector lies on the exact kernel of at most one of the four distinct linear forms. Hence at least one of the two largest linear moduli divides a nonzero linear form value, giving `|z| >> q_(2)`.

The signed `E` root gives `e|m^2+n^2`, so `|z|>=sqrt(e)`. Therefore

```text
lambda_1(Lambda_sigma)
 >> max(q_(2),sqrt(e)).
```

This explains geometrically why auxiliary state congruences cannot manufacture new short vectors except along one exact linear kernel, and the second-largest linear modulus rules out that exception.

## 5. Uniform auxiliary version of the s5m signed-root E theorem

Keep one moving linear modulus `u` and one moving signed `E` modulus `v` with root `r^2==-1 (mod v)`. Freeze arbitrary additional state congruences `sigma` on the remaining columns, all coprime to `uv`.

Before auxiliary constraints are added, s5m uses

```text
Lambda(i;u,v,r)
 = {L_i(m,n)==0 mod u,
    m-rn==0 mod v}
```

with

```text
det Lambda=uv,
lambda_1(Lambda)>=(1/sqrt(2))*K(u,v),
K(u,v)=max(sqrt(v),min(u,v)).
```

Adding frozen congruences replaces this by a sublattice, so the shortest nonzero vector cannot decrease. Therefore

```text
|Delta^sigma_{i,E,r}(u,v)|
 <<_epsilon B^epsilon [1+P_Omega/K(u,v)].
```

Summing the `2^omega(v)` signed roots costs only `B^epsilon`, hence

```text
sum_{u~U,v~V}|Delta^sigma_{i,E}(u,v)|^2
 <<_epsilon B^epsilon UV
 [1+P_Omega^2/K(U,V)^2],

K(U,V)=max(V^(1/2),min(U,V)).
```

The sparse root-pattern occupancy theorem from s5l is also uniform: extra auxiliary congruences only remove points from each signed projective cell.

Thus the s5m/s5l `E` incidence geometry suffers zero auxiliary progression-modulus loss.

## 6. Squarefree quadratic completion inside an auxiliary progression

Let `q,A` be odd and coprime, with `q` squarefree, and let `chi_q(n)=(n/q)`. Let `(a,A)=1`. For an interval `I` of physical length `T`, consider

```text
S(I;A,a,q)
 = sum_{n in I, n==a (mod A)}
   mu(n)^2 chi_q(n).
```

### Theorem 6.1 — auxiliary progression completion

```text
S(I;A,a,q)
 <<_epsilon B^epsilon (T/A)^(1/2) q^(1/4).
```

The harmless logarithm from character completion is absorbed into `B^epsilon`.

Write `n=a+A t`. The `t` interval has length `O(T/A+1)`. Expand `mu(n)^2=sum_{d^2|n}mu(d)`. If `(d,A)>1`, there are no solutions because `(a,A)=1`. If `(d,q)>1`, the Jacobi character vanishes. Thus only `(d,Aq)=1` matters.

For each such `d`, the condition `d^2|a+A t` places `t` in one residue class modulo `d^2`. Writing `t=t_d+d^2 s`, the character is `chi_q(c_d+A d^2 s)`, whose linear coefficient is a unit modulo `q`. Ordinary Gauss completion gives `O(sqrt(q)log(2q))`.

Split at `D`. The small-`d` contribution is `D sqrt(q)log(2q)` and the large-`d` contribution is `(T/A)/D`. Optimizing proves the theorem.

For `n~N`, partial summation gives

```text
sum_{n~N,n==a mod A}
 mu(n)^2 chi_q(n)/n
 <<_epsilon B^epsilon
 N^(-1/2) A^(-1/2) q^(1/4).
```

Thus an auxiliary progression helps rather than hurts the s5n boundary completion estimate.

## 7. Switched one-small-variable boundaries remain uniform

In the s5m complementary switch, a large state divisor `u|L_i(P)` is replaced by

```text
k=|L_i(P)|/u < Z.
```

After the other state pieces are frozen, transversality and pairwise odd support place the reconstructed long variable `u` in a residue class modulo an auxiliary modulus `A_aux` coprime to the active quadratic conductor. Also `(k,A_aux)=1`, because odd primes in the other Euclid factors do not divide `L_i(P)`.

Therefore Theorem 6.1 applies directly. Every s5n one-small-variable estimate survives with an additional `A_aux^(-1/2)` factor at the character-completion step.

```text
AUXILIARY_PROGRESSION_MODULUS_LOSS = none.
```

## 8. Auxiliary state energy transfer

Let `Sigma(P)` be the set of compatible frozen auxiliary state labels carried by one physical Euclid point `P`. Because every label is assembled from squarefree divisors of only finitely many factor values,

```text
#Sigma(P) <<_epsilon B^epsilon.
```

For a fixed moving cell `(u,v)`, let `W_sigma(u,v)` count points carrying auxiliary label `sigma`, and let `W_base(u,v)` ignore auxiliary labels. Then

```text
sum_sigma W_sigma(u,v)^2
 = sum_{P,P' in base cell}
   #{sigma : sigma in Sigma(P) intersect Sigma(P')}
 <<_epsilon B^epsilon W_base(u,v)^2.
```

This is an exact collision-energy argument; there is no modulus-range factor.

The local main densities satisfy the analogous square-summability bound. Since `lambda(q)<=1/q`, and signed `E` root multiplicity `2^omega(e)` is dominated by the square decay,

```text
sum_sigma rho(sigma)^2 <<_epsilon B^epsilon.
```

Consequently auxiliary labels can be carried as an `ell^2(Sigma)` coordinate at only `B^epsilon` energy cost.

## 9. Hilbert-space lift of the quadratic large sieve

Let `H` be any Hilbert space and `beta_v in H`. The scalar quadratic-large-sieve operator from s5h satisfies

```text
sum_u |sum_v b_v (v/u)|^2
 <<_epsilon (UV)^epsilon (U+V)
 sum_v |b_v|^2.
```

Choose an orthonormal basis of `H`, apply the scalar inequality to every coordinate, and sum. Therefore

```text
sum_u ||sum_v beta_v (v/u)||_H^2
 <<_epsilon (UV)^epsilon (U+V)
 sum_v ||beta_v||_H^2.
```

Equivalently, the scalar quadratic-large-sieve matrix has the same operator norm after tensoring with the identity on `H`.

Taking `H=ell^2(auxiliary state labels)` shows that the K4 freeze-one-edge mechanism of s5o is compatible with auxiliary state energy. The auxiliary coordinates do not create a new large-sieve constant.

## 10. What s5p does and does not assemble

The following interfaces are now uniform in arbitrary frozen odd state data:

1. linear-linear central/medium discrepancy;
2. signed-root linear-`E` medium discrepancy;
3. sparse signed-root `E` occupancy;
4. one-small-variable squarefree completion;
5. complementary-divisor switched boundary sums;
6. quadratic-large-sieve operator norms after carrying auxiliary labels in `ell^2`.

Therefore the auxiliary progression-modulus loss isolated in s5o is eliminated.

What remains is not another progression theorem. It is a tensor-contraction question. A full local monomial can have several simultaneously active reciprocal edges. The incidence discrepancy is then a tensor indexed by several state variables. s5p provides

```text
uniform edgewise discrepancy norms
+ auxiliary ell^2 energy transfer
+ Hilbert-valued large-sieve operator bounds.
```

To declare the complete local character polynomial averaged, one still must choose an order of Cauchy-Schwarz / large-sieve contractions that preserves a positive power saving through all active discrepancy tensors. This is particularly delicate when a state-split `E` edge is active, because the s5m estimate is a lattice `L^2` envelope rather than a separable coefficient identity.

Accordingly this stage does not claim `FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true`.

The remaining obstruction is exactly

```text
multi-edge discrepancy tensor contraction,
with active state-split E pieces as the hardest case.
```

There is no longer an unidentified auxiliary progression modulus loss.

## Deterministic audit

The accompanying audit checks:

- pairwise determinants of the four linear columns are `±1,±2`;
- every tested frozen auxiliary state becomes one modular graph in moving linear coordinates;
- exact CRT projective-cell product-index bookkeeping and the second-largest-linear / `sqrt(E)` shortest-vector barrier;
- direct finite modular-graph incidence against the uniform `1+min(R,S)` shape;
- signed-root `E` auxiliary cells remain subsets of the original s5m lattices;
- squarefree Jacobi sums in coprime arithmetic progressions against the `(T/A)^(1/2)q^(1/4)` shape;
- the weighted `1/n` progression corollary;
- auxiliary collision-energy transfer on finite primitive Euclid boxes;
- the Hilbert lift identity by comparing coordinatewise and vector-valued quadratic forms.

Finite checks are regression evidence only. The theorems are carried by projective CRT, two-direction slicing, Möbius inversion, the s5m shortest-vector argument, Gauss completion, divisor multiplicity, and Hilbert-space tensoring.

## Boundary

```text
STAGE14_S5P=COMPLETE_AUXILIARY_PROGRESSION_UNIFORMITY_AND_TENSOR_ENERGY_REDUCTION
AUX_PROJECTIVE_CRT_CELL_EXACT=true
LINEAR_AUX_FIXED_POINTWISE_DISCREPANCY_PROVED=true
LINEAR_AUX_DYADIC_L2_PROVED=true
FULL_STATE_CELL_INDEX_PRODUCT_PROVED=true
FULL_STATE_CELL_SECOND_LARGEST_SHORTEST_BARRIER_PROVED=true
E_SIGNED_ROOT_AUX_UNIFORMITY_PROVED=true
E_SPARSE_AUX_UNIFORMITY_PROVED=true
AUX_PROGRESSIONS_SQUAREFREE_COMPLETION_PROVED=true
SWITCHED_BOUNDARY_AUX_UNIFORMITY_PROVED=true
AUXILIARY_STATE_ENERGY_TRANSFER_PROVED=true
HILBERT_QUADRATIC_LARGE_SIEVE_LIFT_PROVED=true
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true
AUXILIARY_PROGRESSION_MODULUS_LOSS_PERSISTS=false
MULTI_EDGE_DISCREPANCY_TENSOR_CONTRACTION_PROVED=false
STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_PROVED=false
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5q contract the auxiliary Hilbert discrepancy tensors along the s5o graph escape, treating active state-split E edges first, and either close the full finite local character polynomial or isolate the final tensor-norm loss
```
