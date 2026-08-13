# Stage14-4bb — import K4 graph escape and update the complete-local exponent gate

## Result

Merged Stage14-4ba reduced the unresolved linear multi-edge local-character problem to the nonempty `2`-cores of the reciprocity graph on

```text
A=m,
B=n,
C=m-n,
D=m+n.
```

The exact 2-core ledger was

```text
triangle: 16,
C4:        3,
diamond:   6,
K4:        1,
```

for `26` nonempty 2-core edge subsets in total.

Merged Stage14-s5o now closes this **intrinsic K4 product-conductor obstruction**.  The degree-two / degree-three conductor pile-up found at s5n is not a persistent resonance; it is an artifact of summing a common vertex first.

Stage14-4bb imports the s5o graph theorem into the 14-4 mainline and updates the exact local exponent contract.

The result is:

```text
K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR = CLOSED,
```

with a conservative graph-assembly saving

```text
delta_K4 = 1/200.
```

The first remaining reciprocal-local gates are now

```text
AUXILIARY_INCIDENCE_UNIFORMITY
+ STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY.
```

No complete `rho_loc / E_loc` pair is claimed yet.

## 1. Imported s5o graph theorem

For a nonempty linear reciprocal graph `H subseteq K4`, let the active squarefree state variables satisfy

```text
u_i ~ U_i.
```

s5o chooses

```text
eta = 1/100
```

and proves an exhaustive three-case escape.

### Case A — a long-long edge exists

If some active edge `{i,j}` satisfies

```text
U_i,U_j >= M^eta,
```

freeze the remaining state variables.  All other reciprocal factors become one-variable unit-modulus coefficients, leaving one genuine Jacobi edge

```text
sum alpha(u_i) beta(u_j) (u_i/u_j).
```

The s5h quadratic-large-sieve bound gives relative saving

```text
M^(-eta/2+epsilon)
 = M^(-1/200+epsilon).
```

### Case B — no long-long edge, but a very-long active vertex exists

If no active edge has two endpoints at least `M^eta`, but some active vertex satisfies

```text
U_i >= M^(4eta),
```

then every neighbor of `i` has size `<M^eta`.  Since the K4 degree is at most three, the product conductor at `i` is

```text
Q_i << M^(3eta).
```

The s5n squarefree completion lemma then gives relative saving

```text
M^(-5eta/4+epsilon)
 = M^(-1/80+epsilon).
```

### Case C — all graph-active variables are below M^(4eta)

If every active state size satisfies

```text
U_i < M^(4eta),
```

then the total conductor and the number of modulus tuples are both bounded by `M^(16eta)`.  Exact local centering followed by the fixed-conductor periodic estimate gives the crude total

```text
B^epsilon [ M^(1+32eta) + M^(48eta) ].
```

For `eta=1/100`, this is

```text
M^1.32 + M^0.48,
```

well below the regular physical scale `M^2`.

Hence the worst of the three cases is Case A, and

```text
boxed:
delta_K4 = 1/200.
```

## 2. Consequence for the 14-4ba 2-core ledger

Stage14-4ba had separated `38` empty-2-core edge subsets from `26` nonempty-2-core subsets.

The empty-2-core family was already reducible by leaf peeling to the single-edge theory.

Merged s5o now controls every nonempty K4 graph as well.  In particular the four core isomorphism types

```text
triangle,
C4,
diamond K4-e,
K4
```

all fall under the same exhaustive graph escape.

Therefore

```text
K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR_CLOSED=true
```

and no residual `delta_core` parameter is needed in the main-track exponent ledger.

## 3. What exactly is averaged

The s5o theorem applies to the interfaces already put in separable / one-small-variable form:

1. the s5i rank-one Euclid-incidence bulk;
2. the s5m/s5n one-small-variable linear boundary operators;
3. finite mod-4/mod-8 and `Q_2` coefficient splittings.

Thus

```text
SEPARABLE_K4_MULTI_EDGE_MONOMIALS_AVERAGED=true
ONE_SMALL_VARIABLE_K4_BOUNDARY_ASSEMBLY_PROVED=true.
```

The K4 graph itself is no longer an analytic obstruction.

## 4. What remains: auxiliary incidence uniformity

The complete local Fourier polynomial also contains discrepancy pieces after several other Euclid state moduli have been frozen simultaneously.

In those terms, a physical one-variable or two-variable sum is restricted to an auxiliary progression whose modulus contains other moving/frozen state pieces.

The existing s5k linear discrepancy theorem and s5m signed-root E lattice theorem are not yet uniform in all such auxiliary progression moduli at only `B^epsilon` cost.

This is now a distinct named gate:

```text
AUXILIARY_INCIDENCE_UNIFORMITY.
```

It is not the old arbitrary-matrix obstruction and it is not a K4 product-conductor obstruction.

## 5. State-split E multi-edge assembly remains separate

Sparse and central-medium E-linear incidence are already controlled by s5l/s5m, including signed-root lattice dispersion.

What remains is the complete simultaneous assembly when a moving reciprocal variable is itself a state-split piece of

```text
E=m^2+n^2.
```

Thus the second remaining reciprocal-local gate is

```text
STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY.
```

The K4 linear graph theorem does not by itself prove this E-sector theorem.

## 6. Updated reciprocal error decomposition

Write the nonconstant reciprocal-mode error schematically as

```text
E_rec
 = E_K4
 + E_aux
 + E_E,
```

where

```text
E_K4 : separable / one-small-variable linear K4 sector,
E_aux: auxiliary-incidence discrepancy sector,
E_E  : state-split E multi-edge sector.
```

Merged s5o gives

```text
E_K4(M)
 << M^(2-1/200+o(1)).
```

Suppose future stages prove

```text
E_aux(M) << M^(2-delta_aux+o(1)),
E_E(M)   << M^(2-delta_E+o(1))
```

for some positive `delta_aux,delta_E`.  Then

```text
boxed:
delta_rec
 = min(1/200, delta_aux, delta_E),
```

and

```text
E_rec(M)
 << M^(2-delta_rec+o(1)).
```

This replaces the 14-4ba provisional contract

```text
min(1/20,delta_core,delta_E).
```

The single-edge `1/20` saving remains true but is no longer the conservative graph-assembly bottleneck.

## 7. Why rho_loc is still not available

The local domination from 14-4au has the form

```text
S_W
 <= D_loc + E_rec,
```

where `D_loc` is the constant/diagonal local-density contribution and `E_rec` is the nonconstant reciprocal error.

The graph theorem controls only a component of `E_rec`.  It does not identify the asymptotic size of `D_loc` relative to `A_W`.

Therefore it remains invalid to declare

```text
rho_loc = M^(-1/200)
```

or any other positive local retainer exponent from the K4 saving alone.

A genuine complete pair

```text
S_W <= rho_loc A_W + E_loc
```

requires both:

1. closure of `E_aux` and `E_E`;
2. a complete diagonal/local-density assignment for `D_loc`.

## 8. Main-track frontier after 14-4bb

The local analytic ledger is now

```text
rank-one local bulk                              proved
single-edge linear full dyadic range             proved
linear endpoint finite reduction                 proved
empty K4 2-core monomials                        proved/reducible
nonempty K4 2-core product-conductor obstruction proved closed
separable K4 multi-edge assembly                 proved
one-small-variable K4 boundary assembly          proved
auxiliary-incidence discrepancy uniformity       open
state-split E multi-edge assembly                open
full local character polynomial averaged         open
explicit rho_loc / E_loc                         open
```

Thus the first remaining reciprocal-local obstruction is exactly

```text
AUXILIARY_INCIDENCE_UNIFORMITY
+ STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY.
```

## Boundary

```text
STAGE14_4BB=K4_GRAPH_ESCAPE_IMPORTED_AND_LOCAL_EXPONENT_GATE_UPDATED
S5O_K4_GRAPH_ESCAPE_IMPORTED=true
K4_2CORE_TYPES_CONTROLLED=true
K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR_CLOSED=true
K4_GRAPH_ASSEMBLY_SAVING_EXPONENT=1/200
DEGREE_2_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION=false
DEGREE_3_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION=false
PERSISTENT_RESONANT_K4_SUBGRAPH_FOUND=false
SEPARABLE_K4_MULTI_EDGE_MONOMIALS_AVERAGED=true
ONE_SMALL_VARIABLE_K4_BOUNDARY_ASSEMBLY_PROVED=true
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=false
STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_PROVED=false
CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA=min(1/200,delta_aux,delta_E)
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

```text
NEXT=Stage14-4bc import Stage14-s5p if available; prove auxiliary-progression-uniform linear/E discrepancy estimates, assemble the remaining E sector, and attempt the first explicit complete reciprocal E_loc exponent
```
