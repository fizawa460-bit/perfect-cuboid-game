# Stage14-4bb — K4 graph escape and elimination of the intrinsic product-conductor obstruction

## Result

Stage14-4ba reduced the remaining linear multi-edge local-character problem to the nonempty `2`-cores of the reciprocity graph on

```text
A=m,
B=n,
C=m-n,
D=m+n.
```

The only core shapes were

```text
triangle, C4, diamond K4-e, K4.
```

Stage14-4bb closes that **intrinsic graph-assembly obstruction**.  The degree-two / degree-three product-conductor loss isolated in s5n is not a persistent resonance: it is an artifact of summing the wrong variable first.

The proof uses only already-established Stage14 inputs:

- the s5h separable quadratic-large-sieve edge bound;
- the s5n squarefree incomplete quadratic-character completion lemma;
- exact local centering and the fixed-conductor periodic bound from s5g/s5n;
- the finite K4 reduction from 14-4ba.

A parallel validated Stage14-s5o branch proves the same graph escape.  Stage14-4bb records the argument self-containedly on the 14-4 mainline and does not require s5o to be merged.

The remaining local obstruction is no longer K4 degree.  It is

```text
AUXILIARY_INCIDENCE_UNIFORMITY
+ STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY.
```

No complete `rho_loc / E_loc` pair is claimed yet.

## 1. K4 monomials and dyadic state sizes

After the fixed mod-4 reciprocity partition, a linear reciprocal monomial is

```text
K_H(u_A,u_B,u_C,u_D)
 = product_{{i,j} in E(H)} (u_i/u_j),
```

up to bounded one-variable mod-4/mod-8 characters, where

```text
H subseteq K4.
```

Let

```text
u_i ~ U_i.
```

Isolated vertices are separable mass and do not participate in reciprocal cancellation.

Fix

```text
eta = 1/100.
```

The graph-active variables are divided using the thresholds

```text
LONG:      U_i >= M^eta,
VERY_LONG: U_i >= M^(4 eta).
```

Every nonempty graph / size assignment falls into one of the three cases below.

## 2. Case A — one long-long edge

Suppose an active edge `{i,j}` satisfies

```text
U_i,U_j >= M^eta.
```

Freeze every variable except `u_i,u_j`.  Every other edge incident to `i` becomes a one-variable unit-modulus coefficient in `u_i`; every edge incident to `j` becomes a one-variable coefficient in `u_j`; edges among frozen vertices become constants.

Thus the moving pair has the form

```text
sum alpha(u_i) beta(u_j) (u_i/u_j).
```

The s5h quadratic-large-sieve bound gives, for bounded coefficients,

```text
|S_H|
 << B^epsilon (product_k U_k)
    sqrt(1/U_i + 1/U_j).
```

Hence

```text
|S_H| / trivial
 << M^(-eta/2+epsilon).
```

With `eta=1/100`,

```text
Case A saving = M^(-1/200+epsilon).
```

This estimate is independent of the degrees of `i,j`; triangle, C4, diamond and full K4 are all harmless whenever one edge has two long endpoints.

## 3. Case B — no long-long edge, but a very-long active vertex

Assume no active edge has both endpoints at least `M^eta`, but some active vertex `i` satisfies

```text
U_i >= M^(4 eta).
```

Then every neighbor of `i` has size `<M^eta`.  Since K4 has maximum degree three, the product neighbor conductor satisfies

```text
Q_i = product_{j~i} u_j
 << M^(3 eta).
```

After freezing all other variables,

```text
product_{j~i} (u_i/u_j)
 = (u_i/Q_i)
```

up to fixed reciprocity signs.

The s5n squarefree completion lemma gives

```text
sum_{u_i~U_i} mu(u_i)^2 (u_i/Q_i)
 << B^epsilon U_i^(1/2) Q_i^(1/4).
```

Relative to the trivial `U_i` bound,

```text
U_i^(-1/2) Q_i^(1/4)
 <= M^(-2 eta) M^(3 eta/4)
 = M^(-5 eta/4).
```

Thus, for `eta=1/100`,

```text
Case B saving = M^(-1/80+epsilon).
```

The same argument applies to the partial-summation `1/u_i` weights and the already-switched one-small-variable boundary operators.

## 4. Case C — all graph-active variables below M^(4 eta)

The only remaining case is

```text
U_i < M^(4 eta)
```

for every graph-active vertex.

There are at most four active variables, so the total fixed conductor is bounded by

```text
Q << M^(16 eta).
```

The number of possible modulus tuples is also crudely

```text
<< M^(16 eta).
```

For each fixed tuple, assemble the exact local means first.  The centered physical Euclid sum is periodic modulo `Q` with exact zero mean on primitive-compatible residue classes.  The s5n periodic estimate gives

```text
sum_{P in Omega} Psi_Q(P)
 << B^epsilon (P_Omega Q + Q^2).
```

Summing crudely over all short tuples yields

```text
<< B^epsilon [
   P_Omega M^(32 eta)
   + M^(48 eta)
].
```

On a regular Stage14 box

```text
P_Omega ~ M,
G ~ M^2,
```

so for `eta=1/100` the two powers are

```text
M^1.32,
M^0.48,
```

both power-saving against the `M^2` physical scale.

## 5. Exhaustive graph dichotomy

For every nonempty subgraph `H subseteq K4` and every dyadic size assignment, exactly one of the following applies:

```text
A: H contains a long-long edge;
B: no long-long edge, but some active vertex is VERY_LONG;
C: all active vertices are below M^(4 eta).
```

There is no fourth case.

The deterministic audit checks all

```text
63 nonempty K4 subgraphs
x 3^4 abstract size assignments
= 5103 configurations.
```

The exact classification counts are

```text
Case A: 3568
Case B: 840
Case C: 695
```

with zero unclassified configurations.

The 26 nonempty 2-core configurations isolated in 14-4ba are therefore all absorbed by the same trichotomy.  No triangle/C4/diamond/K4 resonance survives.

## 6. Quantitative graph-assembly exponent

The three guaranteed relative savings are

```text
Case A: eta/2,
Case B: 5 eta/4,
Case C: at least min(1-32 eta, 2-48 eta)
        relative to the M^2 scale.
```

For `eta=1/100`, the worst is Case A:

```text
boxed:
delta_K4 = 1/200.
```

Thus the **separable / one-small-variable linear graph sector** satisfies

```text
E_K4(M)
 << M^(2-1/200+epsilon).
```

This improves the logical interface from 14-4ba:

```text
K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR
```

is no longer an intrinsic obstruction.

## 7. Why this still does not prove the complete local theorem

The graph escape applies directly to:

1. the s5i rank-one Euclid-incidence bulk;
2. the s5m/s5n one-small-variable linear boundary operators;
3. finite mod-4/mod-8 and Q2 coefficient splittings.

However, the complete local Fourier polynomial also contains discrepancy pieces after several auxiliary Euclid state moduli are frozen simultaneously.

For those terms, a physical one-variable sum can be restricted to an auxiliary progression whose modulus contains other state pieces.  The s5k linear discrepancy and the s5m signed-root E lattice discrepancy have not yet been proved uniformly through all such simultaneous progression moduli at only `B^epsilon` cost.

Likewise, moving state-split pieces of

```text
E=m^2+n^2
```

have their own signed-root lattice graph and are not covered by the pure linear K4 theorem.

Therefore the new main-track frontier is

```text
AUXILIARY_INCIDENCE_UNIFORMITY
+ STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY.
```

## 8. Updated local exponent contract

The previously proved single-edge boundary exponent `1/20` is no longer the limiting linear graph exponent.  The conservative full K4 assembly gives `1/200`.

If the remaining auxiliary-progression discrepancy sector admits a saving `delta_aux>0`, and the complete state-split E multi-edge sector admits a saving `delta_E>0`, then the reciprocal nonconstant-mode error has the conditional exponent

```text
delta_rec
 = min(1/200, delta_aux, delta_E).
```

Equivalently,

```text
E_rec(M)
 << M^(2-delta_rec+o(1)).
```

This is still only the **nonconstant reciprocal-mode error** contract.  The local-density / constant-mode term remains separate, so it is still invalid to declare

```text
rho_loc = M^(-1/200)
```

without a corresponding diagonal/local-density theorem.

## 9. Status

Proved at 14-4bb:

```text
all empty-2-core monomials reducible                         true
all nonempty K4 2-core graph shapes escape                  true
degree-2 product conductor intrinsic obstruction            false
degree-3 product conductor intrinsic obstruction            false
persistent resonant K4 subgraph                             false
separable K4 multi-edge monomials averaged                  true
one-small-variable K4 boundary assembly                     true
conservative linear graph saving exponent                   1/200
```

Still open:

```text
uniform auxiliary-incidence discrepancy                     open
state-split E multi-edge assembly                            open
full local character polynomial averaged                    open
explicit nontrivial rho_loc                                  open
complete E_loc                                               open
positive global saving exponent                              open
positive height saving exponent                              open
sqrt(B) active-vertex asymptotic                             open
```

## Boundary

```text
STAGE14_4BB=K4_GRAPH_ESCAPE_AND_INTRINSIC_PRODUCT_CONDUCTOR_OBSTRUCTION_CLOSED
K4_2CORE_TYPES_CONTROLLED=true
K4_FREEZE_ONE_EDGE_ESCAPE_PROVED=true
K4_VERY_LONG_VERTEX_ESCAPE_PROVED=true
K4_ALL_SHORT_PERIODIC_ESCAPE_PROVED=true
K4_GRAPH_DICHOTOMY_EXHAUSTIVE=true
K4_GRAPH_ASSEMBLY_SAVING_EXPONENT=1/200
DEGREE_2_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION=false
DEGREE_3_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION=false
PERSISTENT_RESONANT_K4_SUBGRAPH_FOUND=false
SEPARABLE_K4_MULTI_EDGE_MONOMIALS_AVERAGED=true
ONE_SMALL_VARIABLE_K4_BOUNDARY_ASSEMBLY_PROVED=true
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=false
STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_PROVED=false
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

```text
NEXT=Stage14-4bc prove uniform auxiliary-progression versions of the linear and signed-root E discrepancy estimates, then insert the K4 escape into the complete finite local polynomial and attempt the first explicit reciprocal E_loc exponent
```
