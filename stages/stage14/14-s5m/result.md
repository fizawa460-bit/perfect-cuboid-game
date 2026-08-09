# Stage14-s5m — medium E-linear lattice dispersion and exact linear boundary switching

## Purpose

Stage14-s5l closed the sparse `E=m^2+n^2` range by keeping each square-root pattern of `-1` visible until after the second moment, and isolated four linear dyadic boundary strips. This stage pushes both interfaces one step further.

The key observation is that a **fixed norm-root pattern is linear**. If `r^2 == -1 (mod v)`, then the state-split norm condition is

```text
m == r*n (mod v),
```

not a genuinely quadratic condition. Intersecting this with one linear Euclid state condition gives a rank-two lattice of determinant `uv`. Its shortest vector admits an elementary lower bound which is strong enough to give a medium-range `L^2` discrepancy theorem.

For the linear boundary strips, a large state divisor `u|L_i(m,n)` is replaced exactly by its small complementary cofactor `k=|L_i|/u`; the reciprocal symbol is rewritten without approximation. This reduces every large linear strip to a one-small-variable character-sum interface. The remaining small-state strips and the switched physical character sums are not yet globally averaged.

No new external analytic theorem is used in this stage.

## 1. Fixed E-root pattern gives a lattice of determinant uv

Let

```text
L_A=m,
L_B=n,
L_C=m-n,
L_D=m+n.
```

Fix one linear column `L_i`, odd squarefree coprime moduli `u,v`, and assume every prime of `v` is `1 mod 4`. Fix a root

```text
r^2 == -1 (mod v).
```

Define

```text
Lambda(i;u,v,r)
 = {(m,n) in Z^2 :
      L_i(m,n) == 0 (mod u),
      m-r*n       == 0 (mod v)}.
```

Each congruence is a primitive linear congruence. Since `(u,v)=1`, CRT makes the two indices independent, hence

```text
[Z^2 : Lambda(i;u,v,r)] = u*v.
```

Equivalently,

```text
det Lambda = uv.
```

## 2. Shortest-vector lower bound

Write `lambda_1(Lambda)` for the Euclidean length of the shortest nonzero vector of `Lambda`.

Every `z=(m,n)` in `Lambda` satisfies

```text
v | m^2+n^2,
```

because `m == r*n (mod v)` and `r^2 == -1 (mod v)`. Thus every nonzero lattice vector has

```text
|z| >= sqrt(v).
```

If `L_i(z) != 0`, then `u | L_i(z)`, while every one of the four coefficient vectors has Euclidean norm at most `sqrt(2)`. Hence

```text
|z| >= u/sqrt(2).
```

If `L_i(z)=0`, then `z` lies on one of

```text
m=0,
n=0,
m=n,
m=-n.
```

Combining that line with `m-rn == 0 (mod v)` forces its scalar parameter to be divisible by `v`: `r`, `1-r`, and `1+r` are units modulo every odd prime divisor of `v`. Therefore

```text
|z| >= v/sqrt(2)
```

in the zero-linear-form case.

Consequently

```text
lambda_1(Lambda(i;u,v,r))
  >= (1/sqrt(2)) * K(u,v),

K(u,v) = max(sqrt(v), min(u,v)).
```

uniformly in all four linear columns and all norm-root patterns.

## 3. Signed-root primitive incidence

Let `Omega` be one fixed Stage14 convex dyadic Euclid box, with area scale `A_Omega` and perimeter scale `P_Omega`. Let

```text
W_{i,E,r}(u,v)
```

count primitive opposite-parity points of `Omega` lying in `Lambda(i;u,v,r)`.

At an odd prime, a fixed projective root has primitive local density `1/(p+1)`. Put

```text
lambda(q)=prod_{p|q} 1/(p+1),
M_{i,E,r}(u,v)=c_Omega * lambda(u)*lambda(v),
```

where `c_Omega` is the primitive opposite-parity area constant used in s5i--s5l. Define

```text
Delta_{i,E,r}(u,v)
 = W_{i,E,r}(u,v)-M_{i,E,r}(u,v).
```

### Theorem: signed-root pointwise discrepancy

For every `epsilon>0`,

```text
|Delta_{i,E,r}(u,v)|
 <<_epsilon
 B^epsilon * (1 + P_Omega/K(u,v)).
```

### Proof

Apply rational Möbius inversion to the primitive condition. Split the Möbius variable into the factors supported on `u`, on `v`, and coprime to `uv`, exactly as in the s5k linear-coordinate proof. The supported factors contribute only divisor multiplicity. For the coprime part `d`, the relevant congruence lattice is the dilation by `d` of `Lambda(i;u,v,r)`, so its determinant is `d^2uv` and its shortest vector is at least

```text
d*K(u,v)/sqrt(2).
```

For a convex planar region the elementary lattice-point estimate

```text
#(Omega intersect Lambda)
 = area(Omega)/det(Lambda)
   + O(1 + P_Omega/lambda_1(Lambda))
```

applies. The area terms reproduce the primitive Euler product and hence `lambda(u)lambda(v)`. The boundary terms contribute

```text
sum_d P_Omega/(d*K) << B^epsilon P_Omega/K,
```

and the number of nonempty dilations contributes at the same scale. This proves the pointwise bound.

## 4. Sum over all E-root patterns

For split squarefree `v`, the roots of `r^2 == -1 (mod v)` are exactly

```text
2^omega(v)
```

in number. The unsplit incidence and main term are

```text
W_{i,E}(u,v)=sum_r W_{i,E,r}(u,v),
M_{i,E}(u,v)=sum_r M_{i,E,r}(u,v)
            =c_Omega*lambda(u)*lambda_E(v),

lambda_E(v)=prod_{p|v} 2/(p+1).
```

Hence

```text
Delta_{i,E}(u,v)=sum_r Delta_{i,E,r}(u,v).
```

Since `2^omega(v) <<_epsilon B^epsilon`, root multiplicity is harmless at the `B^epsilon` level and

```text
|Delta_{i,E}(u,v)|
 <<_epsilon
 B^epsilon * (1 + P_Omega/K(u,v)).
```

Thus the mixed-sign `D*S` representation is not required for a pointwise medium estimate: retain signed roots, apply the lattice estimate, then sum the root patterns.

## 5. Medium E-linear L2 dispersion theorem

Let

```text
u ~ U,
v ~ V,
Q=UV,
```

with `u` odd squarefree, `v` odd split squarefree, and `(u,v)=1`. On a dyadic block define

```text
K(U,V)=max(V^(1/2), min(U,V)).
```

The pointwise theorem gives

```text
sum_{u~U} sum_{v~V}
 |Delta_{i,E}(u,v)|^2

<<_epsilon
 B^epsilon * Q *
 (1 + P_Omega^2/K(U,V)^2).
```

This is the first full medium-range `E`-linear signed-root dispersion envelope. It is valid below the s5l sparse threshold as well as above it; s5l remains sharper for `UV>2XY`, where the second moment collapses to the natural same-point diagonal scale.

Against any unit-modulus reciprocal kernel, Cauchy--Schwarz yields

```text
|sum Delta_{i,E}(u,v) * (u/v)|

<<_epsilon
 B^epsilon * Q *
 (1 + P_Omega/K(U,V)).
```

The same bound holds after inserting bounded one-variable mod-4/mod-8 state characters.

## 6. Central E-linear power-saving corridor

The separable main term still satisfies the s5h quadratic-large-sieve envelope. Since

```text
lambda(u) << 1/u,
lambda_E(v) <<_epsilon B^epsilon/v,
```

one obtains

```text
|Bulk_{i,E}(U,V)|
 <<_epsilon
 c_Omega B^epsilon sqrt(1/U+1/V).
```

Let `G` denote the regular two-dimensional geometric scale (comparable to area) and let `P` dominate `P_Omega`. If a dyadic block satisfies

```text
U >= Z,
V >= Z,
UV <= G/Z^2,
```

then `K(U,V)>=Z` and

```text
|Err_{i,E}(U,V)|
 <<_epsilon
 B^epsilon * (G/Z^2) * (1+P/Z).
```

Thus whenever

```text
Z^3 >= P * B^eta
```

for some fixed `eta>0`, the discrepancy has a power saving on the central E-linear region. The bulk simultaneously saves by `Z^(-1/2)`.

The medium norm-root problem is therefore no longer an unstructured `D*S` obstruction. Its central dyadic region is controlled by a signed-root lattice theorem; only boundary corridors remain quantitatively delicate.

## 7. Exact complementary-divisor switching on large linear strips

Return to one of the six linear-linear reciprocal edges. Put

```text
x=L_i(m,n),
y=L_j(m,n),
```

and let `u|x`, `v|y` be the odd squarefree state pieces. On a large-`u` strip assume

```text
u > H_i/Z,
|x| <= H_i.
```

Define

```text
k = |x|/u.
```

Then exactly

```text
k < Z.
```

The map

```text
(P,u) <-> (P,k),
u=|L_i(P)|/k
```

is a bijection after retaining the original squarefree/state predicate on the reconstructed `u`.

Because distinct linear columns are odd-coprime on a primitive Euclid pair, `(x,v)=1`. Therefore

```text
(u/v)
 = (|x|/v) * (k/v).
```

If the sign of `x` is not fixed by the chosen box, the missing sign is only `(-1/v)` and is absorbed into the allowed mod-4 state character. After the standard mod-4 reciprocity partition, the same rewrite applies to an edge originally oriented as `(v/u)`.

Hence every large linear boundary strip is converted exactly to

```text
small cofactor k < Z
x physical quadratic character chi_v(L_i(P))
x small Jacobi factor (k/v)
x bounded remaining state-polynomial weight.
```

The analogous statement holds for a large `v` strip. Consequently the four linear boundary strips from s5l reduce to only two analytic types:

```text
small state modulus < Z,
or
small complementary cofactor < Z plus a physical incomplete character sum.
```

## 8. What is and is not closed

After s5m:

1. six linear edges, central dyadic blocks: power saving from s5l;
2. six linear edges, large boundary strips: exact complementary-divisor switching proved;
3. six linear edges, small boundary strips: explicit small-state-modulus interface remains;
4. four E-linear edges, sparse range: diagonal-scale L2 from s5l;
5. four E-linear edges, medium range: signed-root lattice L2 envelope proved here;
6. four E-linear edges, central medium corridor: power saving follows for a cutoff with `Z^3` larger than the perimeter scale by a fixed power;
7. switched boundary physical character sums are not yet averaged inside the complete multi-edge state polynomial.

So the remaining obstruction is an **assembly/boundary problem**: one small state/cofactor variable must be combined with physical quadratic-character sums and the simultaneous finite state-polynomial expansion without losing the target exponent.

## Deterministic audit

The accompanying audit checks:

- exact root count `#{r mod v:r^2=-1}=2^omega(v)` for tested split squarefree `v`;
- exact index `uv` of every tested fixed-root/linear congruence lattice;
- the shortest-vector lower bound against all nonzero lattice vectors in a finite search window;
- direct verification that every fixed-root lattice vector has `v|m^2+n^2`;
- finite signed-root and root-summed discrepancy ledgers against the new `K(U,V)` envelope;
- exact large-divisor/complementary-cofactor bijection;
- exact Jacobi rewrite `(u/v)=(|L_i|/v)(k/v)` on tested primitive linear-edge states.

The finite checks are regression evidence only. The medium theorem is carried by the lattice-index/shortest-vector argument and Möbius inversion.

## Boundary

```text
STAGE14_S5M=COMPLETE_MEDIUM_E_SIGNED_ROOT_LATTICE_DISPERSION_AND_LINEAR_BOUNDARY_SWITCH
E_FIXED_ROOT_LATTICE_DETERMINANT_UV=true
E_FIXED_ROOT_SHORTEST_VECTOR_BOUND_PROVED=true
MEDIUM_E_LINEAR_DISPERSION_PROVED=true
E_CENTRAL_MEDIUM_POWER_SAVING_PROVED=true
LINEAR_LARGE_BOUNDARY_COMPLEMENT_SWITCH_EXACT=true
LINEAR_BOUNDARY_REDUCED_TO_ONE_SMALL_VARIABLE=true
FULL_LINEAR_SIX_DYADIC_SUMMATION_PROVED=false
SMALL_LINEAR_STATE_STRIPS_CLOSED=false
SWITCHED_PHYSICAL_CHARACTER_SUMS_AVERAGED=false
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5n average the one-small-variable boundary operators (small state modulus and switched cofactor) together with the physical quadratic characters, then assemble the finite local character polynomial or isolate the final exponent loss
```
