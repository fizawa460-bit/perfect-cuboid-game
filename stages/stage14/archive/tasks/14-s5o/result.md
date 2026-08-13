# Stage14-s5o — K4 graph escape from multi-edge product conductors

## Purpose

Stage14-s5n closed every single linear reciprocal edge, but a naive assembly of the full linear reciprocity graph produced a product-conductor loss.  If one state variable `u` is incident to several neighbors,

```text
prod_j (u/v_j) = (u / prod_j v_j),
```

and summing `u` first pays the quarter-power of the product conductor.  On a regular box this erases the single-edge saving at degree two and is worse than trivial at degree three.

This stage shows that this is **not an intrinsic K4 resonance**.  It is an artifact of choosing the wrong summation order.  The four linear columns

```text
A=m,
B=n,
C=m-n,
D=m+n
```

give a reciprocity graph contained in `K4`.  For every nonempty graph monomial there is an escape route:

1. if one edge has two genuinely long endpoints, freeze every other variable and apply the s5h quadratic large sieve to that one edge;
2. if no long-long edge exists but an incident vertex is very long, all of its neighbors are short, so the product conductor at that vertex is itself short and the s5n squarefree completion lemma saves;
3. if every graph-active variable is short, exact s5g centering plus periodic completion controls the whole finite-conductor block.

Therefore no degree-two or degree-three K4 subgraph is persistently resonant in the **separable / one-small-variable linear sector** already reduced by s5i and s5n.  What remains is to lift this graph escape uniformly through the simultaneous Euclid-incidence discrepancy and the state-split `E` pieces.

No new external theorem is used.  The only analytic inputs are the s5h quadratic large sieve and the s5n squarefree completion lemma.

## 1. K4 reciprocity monomials

Let the four odd pairwise-coprime squarefree state variables be

```text
u_A, u_B, u_C, u_D.
```

After the fixed mod-4 reciprocity partition, every linear reciprocal monomial has the form

```text
K_H(u_A,u_B,u_C,u_D)
 = prod_{ {i,j} in E(H) } (u_i/u_j),
```

up to one-variable mod-4/mod-8 characters of modulus one, where `H` is a subgraph of `K4`.

The orientation of an edge is irrelevant analytically: reversing `(u_i/u_j)` changes only the fixed quadratic-reciprocity sign on a chosen mod-4 class pair.

Let

```text
u_i ~ U_i.
```

The graph-active vertices are those incident to at least one edge of `H`.  Isolated state variables contribute only separable mass and play no role in the reciprocity cancellation.

## 2. Freeze-one-edge lemma

Fix an edge `{i,j}` of `H` and freeze every variable except `u_i,u_j`.

Every remaining edge incident to `i` becomes a one-variable unit-modulus factor in `u_i`; every remaining edge incident to `j` becomes a one-variable unit-modulus factor in `u_j`; all edges joining frozen vertices become constants.  Therefore the two moving variables have exactly the form

```text
sum_{u_i~U_i} sum_{u_j~U_j}
 alpha_{u_i} beta_{u_j} (u_i/u_j),
```

with the frozen graph factors absorbed into `alpha,beta` without changing their absolute values.

The s5h quadratic-large-sieve bound therefore gives

```text
|S_H|
 <<_epsilon B^epsilon
 sqrt(U_i+U_j)
 ||alpha||_2 ||beta||_2
 prod_{k notin {i,j}} ||a_k||_1.
```

For bounded coefficients on full dyadic supports this is

```text
|S_H|
 <<_epsilon B^epsilon
 (prod_k U_k)
 sqrt(1/U_i + 1/U_j).
```

Hence if

```text
U_i, U_j >= M^eta,
```

one obtains the uniform relative saving

```text
M^(-eta/2+epsilon).
```

This estimate is independent of the degrees of `i` and `j`.  In particular a triangle, a 3-star, or the full `K4` is harmless as soon as one of its edges has two long endpoints.

This is the first escape mechanism and already removes the balanced degree-two/degree-three product-conductor loss isolated at s5n.

## 3. No long-long edge implies the long vertices form an independent set

Fix a threshold

```text
S=M^eta.
```

Assume `H` has no edge whose two endpoints both have dyadic sizes at least `S`.

Then the set

```text
L={i : U_i >= S}
```

is an independent set in `H`.

Consequently every neighbor of a vertex `i in L` has size strictly below `S`.  Since `K4` has maximum degree three, the product of all neighbor moduli of `i` satisfies

```text
Q_i = prod_{j~i} u_j
     << M^(3 eta).
```

After freezing the other variables, multiplicativity gives exactly

```text
prod_{j~i} (u_i/u_j)
 = (u_i/Q_i)
```

up to the already-fixed reciprocity signs.

The important point is that the product conductor is now small **because graph orientation has forced every neighbor to be short**.

## 4. Very-long isolated vertex completion

Set a second threshold

```text
L_0=M^(4 eta).
```

Continue to assume that there is no long-long edge.  Suppose a graph-active vertex `i` satisfies

```text
U_i >= L_0.
```

Every neighbor is below `S`, so

```text
Q_i << M^(3 eta).
```

The one-variable weight in the s5n boundary operators is squarefree, with only finitely many fixed coprimality/residue restrictions.  The s5n squarefree completion lemma therefore gives, on an interval of length `T~U_i`,

```text
sum_{u_i~U_i} mu(u_i)^2 (u_i/Q_i)
 <<_epsilon
 B^epsilon U_i^(1/2) Q_i^(1/4).
```

Relative to the trivial `U_i` bound this is

```text
U_i^(-1/2) Q_i^(1/4)
 <= M^(-2 eta) M^(3 eta/4)
 = M^(-5 eta/4).
```

Thus a very-long vertex with only short neighbors has **more** saving than the long-edge case.

The same argument applies to the weighted `1/u_i` versions by partial summation, and to the switched one-small-cofactor operators of s5m/s5n after the already-proved exact Jacobi rewrite.

## 5. All graph-active variables short: centered periodic escape

The only remaining case is

```text
U_i < M^(4 eta)
```

for every graph-active vertex.

There are at most four graph-active variables, so for a fixed dyadic block

```text
Q = prod_{i active} u_i
  << M^(16 eta).
```

The number of possible modulus tuples in the block is also crudely

```text
<< M^(16 eta).
```

For each fixed tuple, assemble the exact local means before summing over the physical Euclid box, as required by s5g.  The moving part is then periodic modulo `Q` with exact zero mean over the primitive-compatible residue classes.  The s5n microscopic periodic estimate gives

```text
sum_{P in Omega} Psi_Q(P)
 <<_epsilon
 B^epsilon (P_Omega Q + Q^2).
```

Summing this bound crudely over all modulus tuples yields

```text
<<_epsilon B^epsilon [
  P_Omega M^(32 eta)
  + M^(48 eta)
].
```

On a regular Stage14 box

```text
P_Omega ~ M,
G ~ M^2.
```

Hence this is power-saving whenever

```text
eta < 1/32.
```

For the concrete conservative choice

```text
eta = 1/100,
```

the two exponents are

```text
M^(1.32),
M^(0.48),
```

both far below the physical `M^2` scale.

This third escape mechanism closes the graph sector in which every active modulus is short.

## 6. Exhaustive K4 graph dichotomy

Every nonempty subgraph `H subseteq K4` and every dyadic size assignment falls into exactly one of the following analytic cases:

### Case A — long-long edge

There exists `{i,j} in E(H)` with

```text
U_i,U_j >= M^eta.
```

Apply the freeze-one-edge quadratic large sieve.

### Case B — no long-long edge, but a very-long active vertex

There is no Case A edge, but some graph-active `i` has

```text
U_i >= M^(4 eta).
```

All neighbors of `i` are below `M^eta`; combine them into the small conductor `Q_i` and apply squarefree completion in `u_i`.

### Case C — all graph-active variables below `M^(4 eta)`

Use exact local centering and the periodic fixed-conductor estimate, summed over the short modulus tuples.

There is no fourth case.

For `eta=1/100`, the worst guaranteed graph-assembly saving supplied by these three mechanisms is the Case A exponent

```text
M^(-1/200+epsilon).
```

This is deliberately conservative; optimization is unnecessary for the Stage14 logical interface.

## 7. Degree-two and degree-three product conductors are not intrinsic obstructions

The s5n loss came from summing a common vertex first:

```text
(u/v_1)(u/v_2)(u/v_3)
 = (u/(v_1 v_2 v_3)).
```

If all four variables are on the regular scale, the product conductor is indeed too large for the one-variable completion lemma.

But in that same balanced situation **every edge is a long-long edge**, so Case A applies before any product conductor is formed.  Freeze the other variables and use one reciprocal edge directly.

Conversely, if the graph is oriented so that a vertex must absorb a product conductor, then the absence of a long-long edge forces all of its neighbors to be short, and Case B shows that the product conductor is harmless.

Therefore:

```text
degree 2 product conductor != persistent obstruction,
degree 3 product conductor != persistent obstruction.
```

The K4 graph has no resonant subgraph caused solely by reciprocal degree.

## 8. Scope of the theorem

The graph escape theorem applies to the two interfaces already reduced to one-variable/separable form:

1. the rank-one Euclid-incidence bulk from s5i;
2. the one-small-variable linear boundary operators from s5m/s5n.

It also applies after finite mod-4/mod-8 and `Q_2` coefficient splitting, since those factors are bounded and introduce no moving odd conductor.

What is **not** proved here is uniformity of the s5k/s5m discrepancy estimates after several additional state moduli are frozen simultaneously.  In the full local polynomial, auxiliary divisibility conditions from the other Euclid columns can turn a physical one-variable sum into a progression whose modulus contains frozen state pieces.  The freeze-one-edge large-sieve lemma tolerates one-variable coefficient twists, but the one-vertex completion and lattice discrepancy estimates have not yet been proved uniformly in those auxiliary progression moduli.

Likewise, state-split `E=m^2+n^2` terms have their own signed-root lattice structure from s5l/s5m and are not promoted here to a complete multi-edge graph theorem.

Thus s5o removes the **intrinsic K4 product-conductor obstruction** but does not yet declare the full local character polynomial averaged.

## 9. What remains after s5o

The remaining analytic interface is now narrower:

```text
not: single-edge boundary cancellation,
not: balanced K4 reciprocal degree,
not: degree-2/3 product conductors,
not: sparse/medium single E-linear incidence,

but:
uniform multi-edge discrepancy under auxiliary Euclid-incidence progressions,
and its assembly with state-split E root lattices.
```

A natural next step is to prove that the s5k linear-coordinate discrepancy and the s5m signed-root lattice discrepancy remain valid, with controlled loss, after fixing the other pairwise-coprime state moduli.  If that uniform auxiliary-modulus theorem holds at `B^epsilon` cost, the K4 graph escape established here can be inserted term-by-term into the complete finite local character polynomial.

## Deterministic audit

The accompanying audit checks:

- all 63 nonempty subgraphs of `K4`;
- all `3^4` assignments of the abstract size classes `SHORT`, `MEDIUM`, `HUGE` to the four vertices;
- exhaustive coverage by the three graph escape cases;
- no unclassified degree-two, degree-three, triangle, star, cycle, or complete-K4 pattern;
- exact Jacobi factorization when one edge is frozen and all other graph factors are absorbed into one-variable coefficients;
- exact product-conductor identity at vertices of degrees one, two, and three;
- the exponent ledger for `eta=1/100`.

The finite audit is combinatorial regression evidence.  The analytic estimates are carried by the s5h quadratic large sieve, the s5n squarefree completion lemma, exact local centering, and the periodic box estimate.

## Boundary

```text
STAGE14_S5O=COMPLETE_K4_GRAPH_ESCAPE_AND_PRODUCT_CONDUCTOR_ELIMINATION
K4_FREEZE_ONE_EDGE_LARGE_SIEVE_ESCAPE_PROVED=true
K4_NO_LONG_EDGE_LONG_VERTICES_INDEPENDENT=true
K4_VERY_LONG_VERTEX_SMALL_PRODUCT_CONDUCTOR_PROVED=true
K4_ALL_SHORT_CENTERED_PERIODIC_ESCAPE_PROVED=true
K4_GRAPH_DICHOTOMY_EXHAUSTIVE=true
DEGREE_2_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION=false
DEGREE_3_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION=false
PERSISTENT_RESONANT_K4_SUBGRAPH_FOUND=false
SEPARABLE_K4_MULTI_EDGE_MONOMIALS_AVERAGED=true
ONE_SMALL_VARIABLE_K4_BOUNDARY_ASSEMBLY_PROVED=true
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=false
STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_PROVED=false
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5p prove uniform auxiliary-modulus versions of the s5k linear discrepancy and s5m signed-root E lattice estimates, then insert the K4 graph escape into the complete finite local character polynomial or isolate the final progression-modulus loss
```
