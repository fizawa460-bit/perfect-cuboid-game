# Stage14-s5l — linear dyadic synthesis and sparse state-split E root-energy bound

## Purpose

Stage14-s5h supplied the separable reciprocal quadratic-large-sieve estimate. Stage14-s5k supplied pointwise and dyadic `L^2` discrepancy bounds for the six reciprocal edges among

```text
A=m, B=n, C=m-n, D=m+n.
```

This stage combines those inputs into a master dyadic envelope, sums the entire central dyadic region with a power saving, and then returns to the state-split norm column

```text
E=m^2+n^2.
```

For `E`, the s5j mixed-sign `D*S` collision is bypassed in the sparse range by refining to exact projective roots before taking the second moment. This closes sparse `E`-linear incidence at diagonal scale. Medium `E` and the linear boundary strips remain open.

## 1. Linear master dyadic envelope

Fix one of the six edges `(i,j)` among `A,B,C,D`, and let

```text
u ~ U, v ~ V, Q=UV
```

with odd squarefree coprime support. Write

```text
W_ij(u,v)=M_ij(u,v)+Delta_ij(u,v),
M_ij(u,v)=c_Omega lambda(u)lambda(v),
lambda(q)=prod_{p|q}1/(p+1).
```

Bounded one-variable state characters and fixed mod-4/mod-8 factors may be absorbed into coefficients of modulus at most one.

For the reciprocal kernel `(u/v)`, s5h gives

```text
|Bulk_ij(U,V)|
 <<_epsilon
 c_Omega B^epsilon sqrt(U+V)
 ||lambda||_{2,U} ||lambda||_{2,V}.
```

Since `lambda(q)<=1/q`,

```text
||lambda||_{2,U}^2 << 1/U,
||lambda||_{2,V}^2 << 1/V,
```

and hence

```text
|Bulk_ij(U,V)|
 <<_epsilon
 c_Omega B^epsilon sqrt(1/U+1/V).
```

From s5k,

```text
sum |Delta_ij(u,v)|^2
 <<_epsilon
 B^epsilon (Q+H_i^2 V/U+H_j^2 U/V).
```

Cauchy-Schwarz against a unit-modulus reciprocal kernel gives

```text
|Err_ij(U,V)|
 <<_epsilon
 B^epsilon (Q+H_i V+H_j U).
```

Thus every linear reciprocal dyadic block satisfies

```text
|T_ij(U,V)|
 <<_epsilon B^epsilon [
   c_Omega sqrt(1/U+1/V)
   + Q + H_i V + H_j U
 ].
```

No new external theorem is introduced in s5l; the only external analytic input is the quadratic large sieve already contracted in s5h.

## 2. Central dyadic summation

Put

```text
G_ij=H_i H_j
```

and fix `Z>=2`. Define the central region by

```text
Z <= U <= H_i/Z,
Z <= V <= H_j/Z.
```

Then

```text
Q <= G_ij/Z^2,
H_i V <= G_ij/Z,
H_j U <= G_ij/Z,
sqrt(1/U+1/V) << Z^(-1/2).
```

Since `c_Omega << G_ij`,

```text
|T_ij(U,V)|
 <<_epsilon B^epsilon G_ij Z^(-1/2).
```

The `O(log^2 B)` dyadic multiplicity is absorbed into `B^epsilon`, so

```text
sum_central T_ij(U,V)
 <<_epsilon B^epsilon G_ij Z^(-1/2).
```

Summing six edges costs only an absolute constant. For `Z=B^theta`, the central six-edge sector therefore gains `B^{-theta/2+epsilon}` on the regular two-dimensional geometric scale.

## 3. Exact remaining linear boundary

The complement of the central region is exactly the union of

```text
U < Z,
V < Z,
U > H_i/Z,
V > H_j/Z.
```

Hence the six linear edges no longer have an unidentified medium-range obstruction. What remains is explicitly small state pieces and large state pieces with small complementary divisors.

If `u|L_i(m,n)` and `u>H_i/Z`, then its complementary divisor is `O(Z)`. This makes the large strips structurally divisor-switchable, but the reciprocal character must be rewritten inside the complete s5 state polynomial before the switch is globally legal. This stage does not claim those strips closed.

## 4. Root-pattern refinement of E

Let `v` be an odd squarefree divisor of `E=m^2+n^2` for a primitive Euclid pair. Every `p|v` satisfies `p=1 mod 4`. For each prime choose `r_p^2=-1 mod p`. Since `n` is invertible modulo every such `p`, a point with `p|E` has

```text
m/n == +r_p or -r_p mod p.
```

CRT gives exactly

```text
2^omega(v)
```

projective root patterns modulo `v`, equivalently the roots `r^2=-1 mod v`.

For a linear column `L_i`, odd squarefree `(u,v)=1`, and one root pattern `r`, define

```text
W_{i,E,r}(u,v)
 = #{P=(m,n) in Omega :
      primitive/opposite parity,
      u|L_i(P),
      v|E(P),
      m==r*n (mod v)}.
```

Then

```text
W_{i,E}(u,v)=sum_{r^2=-1 mod v} W_{i,E,r}(u,v)
```

is a disjoint sum.

## 5. A fixed root pattern is one projective class

If two points `P=(m,n)` and `P'=(m',n')` lie in the same `W_{i,E,r}(u,v)`, the linear condition gives the same projective root modulo `u` and the signed norm condition gives the same root modulo `v`. Therefore, with

```text
D(P,P')=m*n'-m'*n,
Q=uv,
```

one has

```text
Q | D(P,P').
```

In `0<m,m'<=X`, `0<n,n'<=Y`,

```text
|D(P,P')|<2XY.
```

For primitive positive points `D=0` implies equality. Hence

```text
Q>2XY
=> W_{i,E,r}(u,v) in {0,1}.
```

The opposite-sign `D*S` law from s5j occurs only after distinct root patterns are mixed. Keeping the root pattern visible restores the single determinant law before the second moment is formed.

## 6. Sparse root-energy theorem

Cauchy-Schwarz over the `2^omega(v)` root patterns gives

```text
W_{i,E}(u,v)^2
 <= 2^omega(v) sum_r W_{i,E,r}(u,v)^2.
```

For `UV>2XY`, every signed cell has occupancy at most one, so

```text
sum_r W_{i,E,r}(u,v)^2=W_{i,E}(u,v),
```

and therefore

```text
W_{i,E}(u,v)^2
 <= 2^omega(v) W_{i,E}(u,v).
```

Using `2^omega(v)<<_epsilon v^epsilon` and the divisor bound point-by-point,

```text
sum_{u~U,v~V} W_{i,E}(u,v)^2
 <<_epsilon N_Omega B^epsilon
```

uniformly for `UV>2XY`.

The norm local factor is

```text
lambda_E(v)=prod_{p|v}2/(p+1)
            <<_epsilon B^epsilon/v.
```

Thus, for

```text
M_{i,E}(u,v)=c_Omega lambda(u)lambda_E(v),
```

one has

```text
sum M_{i,E}(u,v)^2
 <<_epsilon c_Omega^2 B^epsilon/(UV).
```

Consequently

```text
sum_{u~U,v~V}|Delta_{i,E}(u,v)|^2
 <<_epsilon
 B^epsilon [N_Omega+c_Omega^2/(UV)]
```

for `UV>2XY`.

On regular Stage14 boxes this is the natural diagonal scale. Thus the sparse state-split `E`-linear obstruction is closed without pretending that opposite root signs disappear algebraically.

## 7. Status after s5l

The analytic interfaces are now:

1. six linear edges, central dyadic region: full dyadic summation with power saving proved;
2. six linear edges, boundary strips: small pieces / small complementary divisors remain;
3. four `E`-linear edges, sparse `UV>2XY`: diagonal-scale `L^2` proved by root-pattern energy;
4. four `E`-linear edges, medium `UV<=2XY`: signed-root dispersion remains;
5. simultaneous multi-edge assembly of the complete local character polynomial remains open.

The old arbitrary two-variable incidence obstruction has therefore been reduced to two explicit interfaces: **linear boundary strips** and **medium norm-root dispersion**.

## Deterministic audit

The accompanying audit checks:

- exact central/boundary partition for all six linear edges;
- `lambda(q)<=1/q` on odd squarefree moduli;
- `#{r mod v:r^2=-1}=2^omega(v)` on tested split squarefree moduli;
- exact root-pattern partition of points with `v|m^2+n^2`;
- determinant divisibility for same-root collisions;
- occupancy at most one in every tested sparse signed `E`-linear cell;
- the finite root-energy inequality.

The finite audit is regression evidence only. The central theorem follows from s5h+s5k; the sparse `E` theorem follows from root refinement, determinant geometry, Cauchy-Schwarz and divisor bounds.

## Boundary

```text
STAGE14_S5L=COMPLETE_LINEAR_CENTRAL_DYADIC_SYNTHESIS_AND_E_SPARSE_ROOT_ENERGY_BOUND
LINEAR_MASTER_DYADIC_ENVELOPE_PROVED=true
LINEAR_CENTRAL_DYADIC_SUMMATION_PROVED=true
LINEAR_CENTRAL_POWER_SAVING_PROVED=true
LINEAR_BOUNDARY_STRIPS_ISOLATED=true
FULL_LINEAR_SIX_DYADIC_SUMMATION_PROVED=false
E_ROOT_PATTERN_PARTITION_EXACT=true
E_LINEAR_SPARSE_ROOT_PATTERN_OCCUPANCY_LE_1=true
E_LINEAR_SPARSE_L2_DISPERSION_PROVED=true
FULL_STATE_SPLIT_E_SPARSE_REGIME_CLOSED=true
MEDIUM_E_LINEAR_DISPERSION_PROVED=false
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5m prove medium E-linear signed-root dispersion and reduce the four linear boundary strips by complementary-divisor switching inside the full state polynomial
```
