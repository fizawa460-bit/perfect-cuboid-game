# Stage14-4az — linear endpoint normal form and finite edge-deletion closure

## Result

Stage14-4ay closed the full frozen-state six-linear **interior** mode family, but left two linear endpoint interfaces:

```text
LOWER_DIMENSIONAL_BULK_MODE_INDUCTION
UPPER_COMPLEMENTARY_STATE_FOURIER_SWITCH.
```

Merged Stage14-s5m subsequently proved the exact complementary-divisor switch on every large linear strip. Stage14-4az imports that theorem into the full 14-4 Fourier expansion and closes the remaining **structural** linear endpoint recursion.

The conclusion is:

```text
all six-linear endpoint modes
  -> finite edge deletion / central saved block / one-small-variable boundary operator.
```

There is no longer any unresolved large-large linear reciprocal kernel. The surviving analytic problem is the average of the one-small-variable boundary operators together with their physical quadratic characters. That average is not proved here.

## 1. Linear reciprocity graph has finite complexity

The four linear Euclid columns are

```text
A=m,
B=n,
C=m-n,
D=m+n.
```

Their genuine whole-kernel reciprocity graph has exactly six possible linear-linear edges. For a fixed local support/Fourier monomial, let

```text
c_lin = number of active linear-linear reciprocal Jacobi edges.
```

Then

```text
0 <= c_lin <= 6.
```

All frozen support pieces, Q2 branches, mod-4/mod-8 characters, and root-sign refinements of the norm column are coefficients for this complexity count; they do not create new linear-linear edges.

## 2. Exact deletion of a unit endpoint

For an oriented reciprocal edge with moving pieces `u,v`, if one endpoint is the unit piece, then

```text
(1/v)=1,
(u/1)=1.
```

Therefore the edge factor disappears exactly from the Fourier monomial. No error term is introduced and no new reciprocal edge is created.

Hence every exact unit-side reduction satisfies

```text
c_lin -> c_lin-1.
```

Iterating can occur at most six times. This closes the termination question left open in 14-4ay: the lower-dimensional recursion cannot cycle or generate increasing reciprocity complexity.

The terminal `c_lin=0` object is not automatically small. It is a lower-dimensional local-character coefficient containing only one-variable local characters, fixed residue conditions, and possibly physical quadratic characters created by the complementary switch below. Its **analytic average** remains a separate task.

## 3. Central / small / large trichotomy for each linear edge

Choose a cutoff `Z` with

```text
1 < Z < min(H_i,H_j).
```

For one dyadic linear-linear edge `(u,v)` with `u|L_i(P)`, `v|L_j(P)`, exactly one of the following applies to each side:

```text
small:   u<Z,
central: Z<=u<=H_i/Z,
large:   u>H_i/Z,
```

and analogously for `v`.

If both sides are central, merged s5l plus 14-4ay provide the saved six-linear full-mode bound. Thus only a small side or a large side requires endpoint reduction.

## 4. Exact complementary-state switch on a large linear side

Import the Stage14-s5m theorem. Suppose

```text
u > H_i/Z,
u | x,
x=L_i(P),
|x|<=H_i.
```

Define the complementary cofactor

```text
k=|x|/u.
```

Then exactly

```text
k<Z.
```

The map

```text
(P,u) <-> (P,k),
u=|L_i(P)|/k
```

is a bijection once the original squarefree/support-state predicate is retained on the reconstructed `u`.

For a primitive Euclid pair, distinct linear columns are odd-coprime. Hence for a reciprocal partner `v|L_j(P)`,

```text
(x,v)=1.
```

Jacobi multiplicativity gives the exact rewrite

```text
(u/v) = (|x|/v) (k/v).
```

If the sign of `x` varies, the sign correction is `(-1/v)` and is absorbed into the already allowed mod-4 character. If the original edge orientation is `(v/u)`, partitioning by residue classes mod 4 and using quadratic reciprocity reduces to the same switched form, exactly as in s5m.

Thus a large endpoint is not a new large-modulus problem. It becomes

```text
small cofactor k<Z
* physical quadratic character chi_v(L_i(P))
* small Jacobi factor (k/v)
* the unchanged bounded frozen-state coefficient.
```

## 5. Stability inside a full Fourier monomial

The complementary switch acts on one Jacobi edge only. Every other factor in the fixed Fourier monomial is carried along unchanged, except for the explicit mod-4 sign character already present in the finite character algebra.

Therefore, after freezing all other support pieces, the switch is an identity of the complete summand, not merely an identity after summation.

In particular:

```text
FULL_FOURIER_MONOMIAL_COMPLEMENT_SWITCH_EXACT=true.
```

No independence assumption is used. The reconstructed `u` continues to satisfy the original selected/unselected/state predicate by definition of the switched summation domain.

## 6. Finite endpoint reduction algorithm

For each active linear-linear reciprocal edge, apply the following deterministic reduction.

```text
1. If an endpoint equals 1: delete the edge.
2. Else if an endpoint is <Z: mark ONE_SMALL_VARIABLE and stop reducing that edge.
3. Else if an endpoint is >H/Z: complementary-switch it to k<Z and mark SWITCHED_ONE_SMALL_VARIABLE.
4. Else both endpoints lie in the central corridor: mark CENTRAL_SAVED.
```

If step 1 occurs, repeat on the remaining graph. Since `c_lin<=6`, deletion terminates after at most six iterations.

Steps 2 and 3 terminate the edge in a one-small-variable operator; step 4 is already controlled by the central six-linear theorem.

Hence every linear endpoint monomial reaches, after finitely many exact transformations, a product of:

```text
CENTRAL_SAVED factors,
ONE_SMALL_VARIABLE boundary factors,
SWITCHED_ONE_SMALL_VARIABLE factors,
fixed one-variable/Q2/root-sign coefficients,
with no unresolved large-large linear reciprocal edge.
```

This is the precise closure of the lower-dimensional induction requested by 14-4ay.

## 7. What remains analytically

The finite reduction is structural, not yet a complete local power-saving theorem.

A typical unswitched boundary operator has one small state modulus `k<Z` and one large character variable. A switched operator additionally carries the physical character

```text
chi_v(L_i(P)).
```

The remaining task is to average these one-small-variable operators uniformly through the full finite local character polynomial without losing the exponent already won in the central region.

Merged s5m records this same frontier as

```text
SMALL_LINEAR_STATE_STRIPS_CLOSED=false
SWITCHED_PHYSICAL_CHARACTER_SUMS_AVERAGED=false.
```

Therefore 14-4az does **not** claim

```text
FULL_LINEAR_SIX_DYADIC_SUMMATION_PROVED=true
```

or an explicit nontrivial `(rho_loc,E_loc)`.

## 8. Relation to the norm sector

The linear endpoint recursion is now separated cleanly from reciprocal modes whose moving variable is a state-split piece of

```text
E=m^2+n^2.
```

Merged s5l/s5m already control sparse E-root energy and a central medium E-linear corridor by signed-root lattices. Their remaining E-boundary assembly is not solved by the linear complementary switch unless the moving large piece lies on a linear column.

Thus the active local frontier becomes

```text
ONE_SMALL_VARIABLE_LINEAR_BOUNDARY_AVERAGING
+ STATE_SPLIT_E_BOUNDARY_ASSEMBLY.
```

This is narrower than the 14-4ay frontier: the finite induction and the exact upper linear switch are no longer open problems.

## Deterministic audit

The accompanying audit checks:

- all six linear edges and the bound `c_lin<=6`;
- exact unit-edge deletion;
- exact partition of representative dyadic sizes into small/central/large strips;
- exact complementary bijection `u <-> k=|L_i|/u` on finite primitive Euclid states;
- exact Jacobi rewrite `(u/v)=(|L_i|/v)(k/v)` whenever the linear-edge coprimality hypotheses hold;
- repeated edge deletion terminates in at most six steps;
- imported 14-4ay and s5m boundary flags remain consistent.

Finite computation is regression evidence only. The structural theorem is carried by the finite six-edge graph, Jacobi multiplicativity, and the exact s5m complementary-divisor bijection.

## Boundary

```text
STAGE14_4AZ=LINEAR_ENDPOINT_FINITE_REDUCTION_AND_COMPLEMENT_SWITCH_CLOSED
S5M_LINEAR_LARGE_BOUNDARY_SWITCH_IMPORTED=true
LINEAR_RECIPROCITY_COMPLEXITY_MAX=6
UNIT_ENDPOINT_EDGE_DELETION_EXACT=true
LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_CLOSED=true
FULL_FOURIER_MONOMIAL_COMPLEMENT_SWITCH_EXACT=true
UPPER_COMPLEMENTARY_STATE_FOURIER_SWITCH_CLOSED=true
ALL_LINEAR_ENDPOINT_MODES_REDUCED_TO_CENTRAL_OR_ONE_SMALL_VARIABLE=true
UNRESOLVED_LARGE_LARGE_LINEAR_RECIPROCAL_EDGE=false
ONE_SMALL_VARIABLE_LINEAR_BOUNDARY_AVERAGED=false
SWITCHED_PHYSICAL_CHARACTER_SUMS_AVERAGED=false
FULL_LINEAR_SIX_DYADIC_SUMMATION_PROVED=false
STATE_SPLIT_E_BOUNDARY_ASSEMBLY_CLOSED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

The phrase `LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_CLOSED=true` means the **finite exact reduction/termination theorem** is closed. It does not mean the terminal one-small-variable operators have been analytically averaged.

```text
NEXT=Stage14-4ba import the s5n one-small-variable boundary estimate when available, assemble the linear boundary normal forms with the central six-linear saving, and determine the first explicit complete local rho_loc/E_loc pair or isolate the remaining E-boundary loss
```
