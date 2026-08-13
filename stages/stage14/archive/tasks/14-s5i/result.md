# Stage14-s5i — Euclid-incidence rank-one bulk and discrepancy boundary

## Purpose

Stage14-s5h proved the first separable reciprocal Jacobi bilinear estimate, but the actual local-indicator expansion still carried a two-variable Euclid incidence weight

```text
W(u,v)=#{(m,n): u|F_i(m,n), v|F_j(m,n), ...}.
```

The unresolved question was whether this weight is genuinely arbitrary, in which case the quadratic large sieve cannot be inserted, or whether the Euclid geometry forces a low-rank main structure.

This stage resolves that question for the **pure local divisibility incidence**. After primitive/opposite-parity conditions are included, its bulk density is multiplicative across the five Euclid columns and therefore separable across all state-split squarefree pieces. Thus the s5h arbitrary-matrix obstruction is reduced to one explicit remainder: finite-box / primitive-Mobius discrepancy. A uniform second-moment estimate for that discrepancy is not yet proved.

## 1. Five Euclid columns and local primitive residue counts

Write

```text
A=m,
B=n,
C=m-n,
D=m+n,
E=m^2+n^2.
```

For primitive opposite-parity `(m,n)`, odd prime support is pairwise disjoint across these five columns.

Let `p` be odd. Impose local primitivity, i.e. exclude `(m,n)=(0,0) mod p`.

For any linear column `A,B,C,D`, the congruence

```text
p | L(m,n)
```

is one nonzero line through the origin. It therefore has exactly

```text
p-1
```

primitive-compatible residue pairs modulo `p`.

For the norm column `E`,

```text
m^2+n^2=0 mod p
```

has no primitive-compatible solution when `p=3 mod 4`, while for `p=1 mod 4` it is the union of the two lines

```text
m=+r n,
m=-r n,
r^2=-1 mod p,
```

and hence has exactly

```text
2(p-1)
```

primitive-compatible residue pairs.

Relative to the unconstrained primitive local population `p^2-1`, the conditional factors are therefore

```text
linear column : (p-1)/(p^2-1)   = 1/(p+1),
norm column   : 2(p-1)/(p^2-1) = 2/(p+1)  for p=1 mod 4,
                0                         for p=3 mod 4.
```

Define for odd squarefree `q`

```text
lambda_L(q) = product_{p|q} 1/(p+1),
lambda_E(q) = product_{p|q} 2/(p+1),
```

with `lambda_E(q)=0` if any `p|q` is `3 mod 4`.

## 2. CRT makes the pure incidence bulk exactly multiplicative

Let the odd squarefree state moduli assigned to the five columns be

```text
q_A, q_B, q_C, q_D, q_E,
```

with pairwise disjoint prime support, as forced by the Euclid factorization. Put

```text
Q=q_A q_B q_C q_D q_E.
```

At each `p|Q`, exactly one column condition is active. Chinese remaindering therefore multiplies the primitive-compatible local residue counts with no cross-column correction.

If

```text
rho(Q)=phi(Q) * 2^omega(q_E),
```

then the admissible primitive-compatible residue set modulo `Q` has exactly `rho(Q)` elements. The factor `2^omega(q_E)` is present only because every split norm prime contributes two nonzero isotropic lines.

The opposite-parity condition contributes exactly two residue classes modulo `2` and is independent of all odd state moduli.

Consequently, before the remaining global gcd condition at primes outside `2Q` is imposed, the complete local residue density is already a product over state pieces.

## 3. Primitive Mobius completion gives a rank-one bulk

Now count in a rectangular Euclid box

```text
R < m <= R+X,
S < n <= S+Y,
```

chosen inside `m>n>0`. Let `W_R(q_A,...,q_E)` denote the number of pairs in the box which

- are primitive;
- have opposite parity;
- satisfy `q_A|A`, ..., `q_E|E`.

For a common divisor `d` coprime to `2Q`, scaling by `d` permutes the admissible classes modulo `2Q`. Mobius inversion at the primes outside `2Q` therefore contributes

```text
product_{p not| 2Q} (1-1/p^2).
```

Combining this with the local residue count gives the bulk identity

```text
W_R(q_A,...,q_E)
 = (4/pi^2) X Y
   * lambda_L(q_A)
   * lambda_L(q_B)
   * lambda_L(q_C)
   * lambda_L(q_D)
   * lambda_E(q_E)
   + Delta_R(q_A,...,q_E).
```

The constant `4/pi^2` is exactly the density of primitive opposite-parity integer pairs.

This is the key s5i advance: the main Euclid incidence coefficient is **rank one across the state moduli**. If a whole column is split into several coprime selected/unselected/state pieces, `lambda_L` and `lambda_E` multiply over those pieces, so the rank-one bulk survives the actual finite state splitting used by the s5 local character polynomial.

Thus the state-split `E` column can reintroduce reciprocal Jacobi symbols, as s5h warned, but it does **not** reintroduce an arbitrary two-variable divisibility weight at main-term level.

## 4. Explicit Mobius-truncation discrepancy decomposition

The remaining matrix is the discrepancy `Delta_R`.

Fix a truncation parameter `D>=1`. Pre-impose local primitivity at every prime dividing `2Q`, and apply Mobius inversion only with `(d,2Q)=1`. For `d<=D`, each admissible residue class modulo `2Q` contributes its rectangular area term plus endpoint errors. This gives

```text
Delta_R
 = Delta_small(D) + Delta_tail(D),
```

with the elementary bounds

```text
Delta_small(D)
 << rho(Q) * ((X+Y)/Q * log(2D) + D),

Delta_tail(D)
 << XY/D + (X+Y) log(2M) + M,
```

where `M=max(R+X,S+Y,2)`.

The tail bound follows by discarding the congruence conditions and summing the common-divisor majorant over `d>D`.

Optimizing the two terms `rho(Q)D` and `XY/D` gives, in the nonempty range, the useful schematic form

```text
Delta_R
 <<_epsilon Q^epsilon *
    ((X+Y) log(2M) + sqrt(Q X Y) + Q).
```

No claim is made that this pointwise estimate is sharp. Its purpose is structural: it isolates the only part of the pure Euclid incidence matrix that is not already separable.

## 5. Consequence for the s5h quadratic-large-sieve block

Take one reciprocal edge with state variables `u~U`, `v~V`, after all other pieces are fixed. The pure Euclid incidence weight now has the form

```text
W(u,v)=A_R * alpha_u * beta_v + Delta(u,v),
```

where `alpha_u` and `beta_v` include the corresponding `lambda_L` or `lambda_E` factors, one-variable mod-4/mod-8 characters, and fixed state coefficients.

Therefore the **bulk** reciprocal sum is exactly of the separable type treated in s5h:

```text
sum_u sum_v A_R alpha_u beta_v (u/v),
```

and inherits the first dyadic quadratic-large-sieve saving.

The arbitrary-matrix counterexample from s5h can no longer occur in the pure incidence bulk. Any failure of cancellation must live in

```text
sum_u sum_v Delta(u,v) (u/v),
```

or in weights which are not part of the local Euclid incidence at all, notably global-solubility/Sha and the physical first-small-point window.

## 6. Persistent obstruction: a discrepancy second moment is still missing

A pointwise bound for `Delta(u,v)` is not enough. Summing it trivially over all dyadic `u,v` loses the character cancellation that s5h gained. What is needed next is a dispersion estimate such as

```text
sum_{u~U} sum_{v~V} |Delta(u,v)|^2
```

with enough saving to feed Cauchy-Schwarz / quadratic large sieve.

There is also a genuinely sparse large-modulus regime. When the combined modulus `Q` is comparable to or larger than the geometric box area `XY`, the rank-one bulk is smaller than the endpoint/Mobius discrepancy and the pointwise expansion is not useful. Those blocks require divisor switching, complementary divisors, or a separate sparse-incidence argument.

This is now a much narrower obstruction than at s5h:

```text
s5h obstruction : arbitrary two-variable incidence matrix W(u,v)
s5i obstruction : centered discrepancy Delta(u,v) + sparse large-modulus blocks
```

## 7. Deterministic audit

The s5i audit checks exactly:

- for every tested odd prime, each linear column has `p-1` primitive-compatible roots;
- the norm column has `0` roots for `p=3 mod 4` and `2(p-1)` for `p=1 mod 4`;
- CRT joint residue counts for distinct state moduli equal the product of local root counts;
- the conditional factors are exactly `1/(p+1)` and `2/(p+1)`;
- finite rectangular primitive/opposite-parity incidence matrices are compared with the rank-one bulk `(4/pi^2)XY lambda_i(u)lambda_j(v)` on representative linear-linear and linear-norm edges.

The finite box comparison is diagnostic only. The rank-one bulk formula is carried by the local residue count, CRT, and Mobius inversion argument above.

## Boundary

```text
STAGE14_S5I=COMPLETE_EUCLID_INCIDENCE_RANK_ONE_BULK_AND_DISCREPANCY_REDUCTION
LINEAR_COLUMN_PRIMITIVE_LOCAL_FACTOR=1/(p+1)
NORM_COLUMN_PRIMITIVE_LOCAL_FACTOR=2/(p+1)_for_p_eq_1_mod4_else_0
PURE_EUCLID_DIVISIBILITY_BULK_SEPARABLE=true
STATE_SPLIT_MODULI_PRESERVE_BULK_FACTORIZATION=true
EUCLID_INCIDENCE_ARBITRARY_MATRIX_OBSTRUCTION_REDUCED=true
MOBIUS_TRUNCATION_DISCREPANCY_DECOMPOSITION_PROVED=true
FIRST_SEPARABLE_DYADIC_BILINEAR_BOUND_RETAINED=true
DISCREPANCY_SECOND_MOMENT_PROVED=false
SPARSE_LARGE_MODULUS_BLOCKS_CLOSED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5j prove an L2 dispersion bound for Delta on balanced/medium dyadic blocks and close the sparse Q>=XY regime by divisor switching or isolate its persistent diagonal
```
