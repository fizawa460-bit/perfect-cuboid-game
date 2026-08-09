# Stage14-s5h — reciprocal off-diagonal reduction and first dyadic bilinear bound

## Purpose

Stage14-s5g showed that raw prime-level character sums must be locally centered before any family cancellation statement can be true. The next task is to expand the actual s5 local indicator far enough to expose the reciprocal Jacobi-symbol interactions between squarefree pieces, then determine exactly where a quadratic large sieve can and cannot be applied.

This stage proves the first **separable dyadic reciprocal bilinear bound** and identifies the remaining obstruction: the Euclid divisibility incidence produces a genuinely two-variable coefficient matrix, so the quadratic large sieve cannot yet be inserted into the full Stage14 family sum without an additional dispersion / low-rank decomposition.

## 1. Local rows are finite character polynomials

Write `x in {+1,-1}` for the relevant odd-prime reciprocity character bit and

```text
s = chi_p(-1) in {+1,-1}.
```

After the global product-square relation is used, the selected rows from s5c/4an and the unselected rows from s5d have the exact indicator formulas

```text
selected S or H   : (1+x)/2
selected X        : (1+s)(1+x)/4
unselected S or H : (1+x)/2
unselected X      : (3+x-s+s*x)/4.
```

The last identity is the exact polynomial form of

```text
s=-1  => automatic,
s=+1  => require x=+1.
```

Hence every odd local row is a finite linear combination of monomials in reciprocity bits and the one-prime mod-4 bit. The fixed `Q_2` eight-state table from s5f only creates finitely many additional coefficient cases; it introduces no moving odd modulus.

After squarefree state splitting and expansion, every odd term therefore has the schematic form

```text
coefficient
* product of one-variable mod-4/mod-8 characters
* product over reciprocal edges (u_alpha / u_beta),
```

where the `u_alpha` are pairwise-coprime odd squarefree pieces cut from the five Euclid factors.

## 2. Whole-kernel `m^2+n^2` column collapses

For a primitive opposite-parity Euclid pair put

```text
a = odd squarefree kernel of m
b = odd squarefree kernel of n
c = odd squarefree kernel of m-n
d = odd squarefree kernel of m+n
e = odd squarefree kernel of m^2+n^2.
```

Every odd prime dividing `e` is `1 mod 4`. Moreover

```text
(a/e) = 1,
(b/e) = 1,
(c/e) = (2/c),
(d/e) = (2/d).
```

Proof: if `q | m^2+n^2` is odd, primitiveness rules out `q=3 mod 4`, so all prime divisors of `e` are `1 mod 4`. Modulo any odd divisor of `m` or `n`, `m^2+n^2` is a nonzero square, giving `(e/a)=(e/b)=1`; quadratic reciprocity has no sign because every prime of `e` is `1 mod 4`. Modulo `m-n` and `m+n` one has

```text
m^2+n^2 == 2n^2,
```

so `(e/c)=(2/c)` and `(e/d)=(2/d)`, again with sign-free reciprocity against `e`.

Thus at the level of the five **whole squarefree kernels**, the four apparent edges incident to `e` are not genuine two-variable reciprocal interactions:

```text
m -- e       constant 1
n -- e       constant 1
m-n -- e     one-variable mod-8 character (2/c)
m+n -- e     one-variable mod-8 character (2/d).
```

The ten edges of the naive `K_5` reciprocity graph reduce to six genuine whole-kernel reciprocal edges among

```text
m, n, m-n, m+n.
```

Important boundary: the actual local-indicator expansion splits a whole kernel into selected/unselected/state pieces. Individual `e`-pieces need not satisfy the whole-product identities separately. Therefore the collapse is an exact structural simplification and consistency relation, but it does **not** justify deleting every state-split `e` bilinear term.

## 3. First dyadic reciprocal bilinear bound

Consider one reciprocal edge after all other variables have been fixed. Let `u` and `v` range over odd squarefree integers in dyadic intervals

```text
u ~ U,  v ~ V,
```

and let `alpha_u`, `beta_v` be arbitrary complex coefficients. Define

```text
B(U,V) = sum_u^* sum_v^* alpha_u beta_v (u/v),
```

where `*` denotes odd squarefree support.

The quadratic large sieve for real characters gives, for every `epsilon>0`,

```text
sum_u^* | sum_v^* beta_v (v/u) |^2
  <<_epsilon (UV)^epsilon (U+V) ||beta||_2^2.
```

Partitioning `u` and `v` by their residue classes modulo `4` makes the quadratic-reciprocity sign constant on each of the four class pairs. That sign can be absorbed into the coefficients. Cauchy-Schwarz therefore yields

```text
|B(U,V)|
  <<_epsilon
  (UV)^epsilon sqrt(U+V) ||alpha||_2 ||beta||_2.
```

In particular, if `|alpha_u|,|beta_v|<=1`, then

```text
|B(U,V)|
  <<_epsilon
  (UV)^epsilon sqrt(UV(U+V)).
```

Against the trivial `UV` bound, the ratio before the harmless `(UV)^epsilon` factor is

```text
sqrt(1/U + 1/V).
```

Hence a balanced block `U~V~L` gains a factor `L^(-1/2+epsilon)`. This is the first unconditional dyadic cancellation estimate in the s5 reciprocal off-diagonal program.

External input: the quadratic large sieve in the squarefree-odd form of Heath-Brown's real-character mean-value theorem; an explicit modern formulation is Zihao Liu, *Explicit quadratic large sieve inequality*, Theorem 1 / equation (10), Acta Arithmetica 223 (2026), 227–252, arXiv:2505.09637.

## 4. Why this does not yet prove the Stage14 family estimate

The actual s5 expansion does not naturally produce a separable coefficient `alpha_u beta_v`. After fixing the remaining squarefree pieces, the common Euclid pair `(m,n)` imposes simultaneous divisibility conditions such as

```text
u | F_i(m,n),
v | F_j(m,n),
F=(m,n,m-n,m+n,m^2+n^2),
```

together with primitiveness, parity, local-state labels, and eventually the physical small-point weight.

After summing over `(m,n)`, a dyadic reciprocal block has the form

```text
sum_{u~U}^* sum_{v~V}^* W(u,v) (u/v),
```

with a two-variable incidence weight `W(u,v)`. The quadratic large sieve controls one-variable coefficients inside the character sum; it does not give cancellation for an arbitrary matrix `W(u,v)`.

This distinction is logically necessary. For a completely arbitrary matrix one could choose

```text
W(u,v) = (u/v),
```

making every summand nonnegative and destroying all character cancellation. Thus a theorem about the **structure of the Euclid incidence weight** is required before the separable bilinear estimate can be transferred to the full s5 family.

There is a second boundary: if one dyadic side remains `O(1)`, the bound above is not a uniform power saving over the trivial estimate. Small-side blocks must be removed by a separate divisor/dispersion argument or shown to have sufficiently small total mass.

## 5. Deterministic audit

The s5h audit checks:

- the exact four truth tables for the local character-polynomial identities;
- odd pairwise coprimality and quadratic reciprocity for all ten whole-kernel edges;
- every odd prime of `m^2+n^2` is `1 mod 4`;
- the four exact whole-kernel `e`-column identities above;
- finite dyadic ratios corresponding to the proved separable bilinear estimate.

At `m^2+n^2<=20,000` there are `3,186` primitive opposite-parity Euclid pairs, giving

```text
31,860 whole-kernel reciprocity checks
12,744 exact e-column identity checks
0 failures.
```

These finite checks are consistency evidence only. The dyadic bilinear inequality is carried by the quadratic-large-sieve theorem plus Cauchy-Schwarz, not by finite computation.

## Boundary

```text
STAGE14_S5H=COMPLETE_RECIPROCAL_OFFDIAGONAL_REDUCTION_AND_FIRST_DYADIC_BILINEAR_BOUND
LOCAL_ROWS_FINITE_CHARACTER_POLYNOMIAL=true
WHOLE_KERNEL_E_COLUMN_COLLAPSES=true
WHOLE_KERNEL_GENUINE_RECIPROCAL_EDGE_COUNT=6
STATE_SPLIT_E_PIECES_CAN_REINTRODUCE_BILINEARITY=true
FIRST_SEPARABLE_DYADIC_BILINEAR_BOUND_PROVED=true
EUCLID_INCIDENCE_SEPARABILITY_PROVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5i derive a dyadic Euclid-incidence dispersion/low-rank decomposition that converts the two-variable divisor weight into large-sieve-admissible coefficients, or isolate a persistent diagonal obstruction
```
