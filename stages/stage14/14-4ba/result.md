# Stage14-4ba — K4 2-core reduction of the local assembly obstruction

## Result

Stage14-4az reduced every six-linear endpoint mode to a finite normal form. Merged Stage14-s5n then proved the remaining one-small-variable operators for every **single** linear reciprocal edge and obtained, on a regular box of linear scale `M`, a common cutoff

```text
Z=M^(2/5)
```

with worst single-edge saving

```text
M^(-1/20+epsilon).
```

However s5n also showed that the full local Fourier polynomial cannot be assembled by applying this estimate independently at every edge. If a single state variable `u` is incident to `d` reciprocal neighbors, then

```text
prod_j (u/v_j) = (u / prod_j v_j),
```

so one-variable completion sees the **product conductor**. At regular scale this gives

```text
d=1 : power saving,
d=2 : no power saving,
d=3 : trivial bound wins.
```

Stage14-4ba identifies exactly which linear reciprocity monomials genuinely contain this obstruction. The four linear columns form the complete graph `K4`. Repeatedly remove vertices of current degree `0` or `1`. Degree-one variables are controlled by s5n before the remaining variables are summed, while degree-zero variables carry no reciprocal edge. Therefore every nonempty monomial with empty graph-theoretic `2-core` reduces to the already-proved single-edge theory.

The only unresolved linear assembly monomials are those whose `K4` edge set has a nonempty `2-core`.

Exact enumeration of all `2^6=64` edge subsets gives

```text
empty 2-core                         38 subsets
triangle 2-core C3                   16 subsets
four-cycle 2-core C4                  3 subsets
diamond 2-core K4 minus one edge      6 subsets
complete 2-core K4                    1 subset
```

Thus the s5n product-conductor problem is reduced from an unspecified degree-two/degree-three failure to **26 explicitly classified 2-core configurations**. The other 38 possible linear edge sets are peelable by the existing single-edge theorem.

This is a structural assembly advance, not yet a complete local retainer theorem. No positive complete `delta_loc` is declared because the four nonempty core types and the state-split `E` boundary assembly remain uncontrolled.

## 1. Inputs imported from 14-4az and s5n

From 14-4az:

```text
LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_CLOSED=true
UPPER_COMPLEMENTARY_STATE_FOURIER_SWITCH_CLOSED=true
ALL_LINEAR_ENDPOINT_MODES_REDUCED_TO_CENTRAL_OR_ONE_SMALL_VARIABLE=true
```

From s5n:

```text
SINGLE_LINEAR_EDGE_FULL_DYADIC_SUMMATION_PROVED=true
ALL_SIX_LINEAR_EDGES_INDIVIDUALLY_CLOSED=true
MULTI_EDGE_PRODUCT_CONDUCTOR_OBSTRUCTION_ISOLATED=true
```

The s5n regular-box exponent ledger gives the worst single-edge boundary saving `M^(-1/20+epsilon)`.

## 2. Reciprocity graph and leaf-peeling operation

Write the four linear state vertices as

```text
A=m,
B=n,
C=m-n,
D=m+n.
```

A fixed Fourier monomial selects an edge subset

```text
G <= K4.
```

Suppose a vertex, say `A`, has degree exactly one, with unique reciprocal neighbor `B`. After all other state variables are fixed, the only reciprocal dependence on the moving `A`-state variable is the single factor

```text
(u_A/u_B)
```

or its reciprocity-equivalent orientation. All remaining dependence on `u_A` consists of one-variable local characters, support predicates, residue classes, and the exact complementary-switch physical character already allowed in the s5n single-edge theorem.

Therefore the s5n boundary estimate may be applied in `u_A` with the rest frozen. Removing vertex `A` and its unique edge leaves a lower-complexity monomial on the remaining vertices. No new reciprocal edge is created.

A degree-zero vertex is even simpler: it has no reciprocal edge and belongs to the local-density/one-variable coefficient algebra.

Hence the exact graph reduction is

```text
current degree <=1
    -> sum that vertex by existing one-edge/one-variable theory
    -> delete the vertex and incident edge if present.
```

Repeat until every remaining vertex has degree at least two or the graph is empty. This terminal graph is the ordinary graph-theoretic `2-core`.

## 3. Empty 2-core monomials are analytically reducible

If the 2-core is empty and the monomial contains at least one reciprocal edge, repeated leaf peeling eventually removes every reciprocal edge. At the first nontrivial leaf step, s5n supplies a regular-box power saving of at least

```text
M^(-1/20+epsilon)
```

relative to the corresponding area-scale single-edge contribution. Subsequent leaf eliminations cost only the previously permitted `B^epsilon` divisor/state factors and do not recreate a product conductor at the eliminated vertex.

Accordingly, within the purely linear reciprocal sector and with the nonmoving `E`/Q2 state frozen as in 14-4ay,

```text
EMPTY_LINEAR_2CORE_MONOMIALS_REDUCE_TO_SINGLE_EDGE_THEORY=true.
```

This statement does **not** assert that the full local polynomial already has a global `M^(-1/20)` error: nonempty 2-core monomials and moving state-split `E` reciprocal modes still contribute.

## 4. Exact K4 2-core classification

There are six possible linear reciprocal edges, hence 64 edge subsets. Exhaustive exact graph enumeration gives four nonempty 2-core isomorphism types.

### 4.1 Triangle core

```text
C3
```

Each core vertex has degree two. There is no leaf variable on which the single-edge estimate can be applied without seeing a second incident reciprocal conductor. Across all K4 edge subsets, 16 have triangle 2-core.

### 4.2 Four-cycle core

```text
C4
```

Every vertex again has degree two. Exactly 3 K4 edge subsets have this 2-core.

### 4.3 Diamond core

```text
K4 minus one edge
```

The degree profile is

```text
(3,3,2,2).
```

Exactly 6 edge subsets have this 2-core.

### 4.4 Complete K4 core

```text
K4
```

All four vertices have degree three. Exactly 1 edge subset has this core.

The complete ledger is therefore

```text
38 peelable edge subsets
26 nonempty-2-core edge subsets.
```

The counts sum to 64 exactly.

## 5. Why the 2-core is the correct conductor frontier

The s5n failure mechanism is vertex-local. If `u` sees neighbors `v_1,...,v_d`, elementary completion combines them into

```text
V_*=prod_j v_j.
```

A degree-one vertex has `d=1` and is already controlled. A nonempty 2-core is precisely a subgraph in which every surviving vertex has `d>=2`, so **no first single-edge peeling step exists**.

Thus the K4 2-core is not merely a convenient graph statistic: it is exactly the minimal residual object on which the s5n product-conductor loss can persist after all proven degree-one reductions are exhausted.

This sharpens the obstruction from

```text
MULTI_EDGE_PRODUCT_CONDUCTOR
```

to

```text
K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR.
```

## 6. Exponent ledger and why rho_loc is still not available

The elementary one-variable completion scale from s5n is

```text
T^(1/2) Q^(1/4).
```

For a regular long variable `T~M` and `d` neighbors each of scale `M`, this is

```text
d=1 : M^(3/4),
d=2 : M,
d=3 : M^(5/4), truncated by the trivial M bound.
```

Hence the degree-two vertices in `C3` and `C4` already sit exactly at the no-saving threshold. The diamond and K4 additionally contain degree-three vertices.

Therefore no valid argument presently upgrades the single-edge `1/20` exponent to all nonconstant Fourier monomials. In the 14-4au notation, the reciprocal error term

```text
sum |B_omega|
```

is not yet bounded by a fixed-power-saving `E_rec` for the complete local polynomial.

Consequently

```text
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false.
```

It would be incorrect to set `rho_loc=M^(-1/20)` from s5n alone.

## 7. Conditional local assembly contract

Stage14-4ba records the precise theorem still sufficient to finish the linear assembly.

Suppose every nonempty linear 2-core monomial satisfies, on regular boxes,

```text
|CoreMode_G(M)| << M^(2-delta_core+epsilon)
```

for one uniform `delta_core>0`, after the same frozen-state normalization used in 14-4ay. Suppose also the remaining moving state-split `E` boundary sector satisfies

```text
|EBoundary(M)| << M^(2-delta_E+epsilon)
```

for `delta_E>0`.

Then the nonconstant local Fourier error is controlled with exponent

```text
delta_rec = min(1/20, delta_core, delta_E).
```

The finite number of edge subsets, Q2 states, root-sign refinements, and dyadic boxes contributes only `B^o(1)`.

This contract is exact at the exponent-bookkeeping level; it does not assume independence between local modes.

The diagonal/local-density contribution `D_loc` from 14-4au remains a separate term in the eventual `rho_loc` assignment. Thus even after the reciprocal error is closed, the final `rho_loc` must be read from the complete diagonal/support calculation rather than invented from the reciprocal exponent.

## 8. Relation to the E sector

Merged s5l and s5m already prove:

```text
FULL_STATE_SPLIT_E_SPARSE_REGIME_CLOSED=true
MEDIUM_E_LINEAR_DISPERSION_PROVED=true
E_CENTRAL_MEDIUM_POWER_SAVING_PROVED=true.
```

What is not yet assembled is every E-boundary mode simultaneously with the full multi-edge linear character polynomial. Therefore the E frontier is retained as

```text
STATE_SPLIT_E_BOUNDARY_ASSEMBLY.
```

The linear K4 2-core classification and the E-boundary problem are now independent named interfaces. Future stages should not conflate them.

## 9. Main-track frontier after 14-4ba

The local chain is now

```text
rank-one local bulk                         proved
six-linear central modes                    proved
single-edge linear boundaries               proved
linear endpoint finite reduction            proved
empty-2-core multi-edge monomials           reducible by leaf peeling
nonempty K4 2-core monomials                 open
E sparse and central-medium dispersion       proved
E boundary/full-polynomial assembly          open
```

Thus the first complete-local obstruction is

```text
K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR
+ STATE_SPLIT_E_BOUNDARY_ASSEMBLY.
```

No complete positive local saving exponent is claimed yet.

## Boundary

```text
STAGE14_4BA=K4_2CORE_ASSEMBLY_REDUCTION_AND_LOCAL_EXPONENT_GATE
S5N_ONE_SMALL_BOUNDARY_AVERAGING_IMPORTED=true
SINGLE_LINEAR_EDGE_WORST_SAVING_EXPONENT=1/20
LINEAR_RECIPROCITY_GRAPH=K4
LINEAR_EDGE_SUBSET_COUNT=64
EMPTY_2CORE_EDGE_SUBSET_COUNT=38
NONEMPTY_2CORE_EDGE_SUBSET_COUNT=26
TRIANGLE_2CORE_SUBSET_COUNT=16
C4_2CORE_SUBSET_COUNT=3
DIAMOND_2CORE_SUBSET_COUNT=6
K4_2CORE_SUBSET_COUNT=1
DEGREE_ONE_LEAF_PEELING_VALID=true
EMPTY_LINEAR_2CORE_MONOMIALS_REDUCE_TO_SINGLE_EDGE_THEORY=true
K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR_CLOSED=false
STATE_SPLIT_E_BOUNDARY_ASSEMBLY_CLOSED=false
CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA=min(1/20,delta_core,delta_E)
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

```text
NEXT=Stage14-4bb import Stage14-s5o if available and control the four nonempty K4 2-core types by graph-oriented or iterated quadratic-large-sieve bounds; in parallel keep the state-split E boundary assembly as a separate exponent gate
```
