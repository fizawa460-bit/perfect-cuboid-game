# MB104 Z41B — exact line-bundle descent and canonical index three — 2026-09-19

Status: **PRE-AUDIT EXACT DESCENT / INDEX-THREE UPGRADE / NO CREDIT**

## Input

For each surviving balanced support, the Birkar contraction

```text
phi:S -> Y
```

contracts exactly the complete P-null locus, where

```text
P = 7H - 4 sum_(i in Sigma) E_i,
P^2=336,
K_S=H.
```

Z41 gives the divisor identities

```text
size-48:
P = 3K_S + 4(Q1+Q2+Q3+Q4+E_a+E_b),

size-768:
P = 3K_S + 8A+8B+4E_A+4E_B.
```

The retained formal-null calculations prove that `O_S(P)` is compatibly trivial on every finite
infinitesimal neighborhood of every complete exceptional fiber.

## 1. Exact descent of O_S(P)

Put

```text
L = O_S(P),
M = phi_* L.
```

Since `phi` is proper birational and `Y` is normal,

```text
phi_* O_S = O_Y.
```

For a contracted point `y`, the theorem on formal functions identifies the completed stalks with
inverse limits over a cofinal system of infinitesimal neighborhoods of the exceptional fiber
`N_y`:

```text
M_y^hat
 ~= inverse_limit H^0(nN_y,L|nN_y),

O_(Y,y)^hat
 ~= inverse_limit H^0(nN_y,O_nN_y).
```

The compatible triviality

```text
L|nN_y ~= O_nN_y
```

for every finite `n` therefore gives

```text
M_y^hat ~= O_(Y,y)^hat.
```

Completion of a Noetherian local ring is faithfully flat. Hence `M_y` is free of rank one.

Away from the exceptional locus, `phi` is an isomorphism. Therefore

```text
A := phi_* O_S(P)
```

is a line bundle on all of `Y`.

The adjunction map

```text
phi^* A -> O_S(P)
```

is an isomorphism off the exceptional locus and after completion along every exceptional fiber.
Hence it is an isomorphism globally:

```text
O_S(P) ~= phi^* A.                              (Z41B-1)
```

A positive power of `P` defines `phi) with an ample polarization downstairs, so a positive
power of `A` is ample; therefore `A` is ample.

## 2. Exact tricanonical descent

On the common open set where `phi` is an isomorphism, the Z41 identities imply

```text
A|Y_reg ~= O_Y(3K_Y)|Y_reg.
```

Both sides extend uniquely as rank-one reflexive sheaves over the normal surface `Y`, while
`A` is invertible. Therefore

```text
A ~= O_Y(3K_Y)
```

as reflexive sheaves.

Consequently

```text
3K_Y is Cartier and ample,
O_S(P) ~= phi^* O_Y(3K_Y).                     (Z41B-2)
```

Thus the global canonical index divides three.

## 3. Exact local index at the nonrational contraction points

The exact discrepancy vectors are:

```text
size-48 Q-E-Q:
(-4/3,-4/3,-4/3);

size-768:
(-8/3,-8/3,-4/3,-4/3).
```

If `K_Y` were Cartier at one of these points, then `K_S` and `phi^*K_Y` would both be integral
Cartier divisors on `S`, so their difference would have integral exceptional coefficients. The
displayed nonintegral discrepancies contradict this.

Therefore the local index is not one. Since `3K_Y` is Cartier,

```text
local canonical index = 3
```

at every nonrational contracted point.

The isolated A1 contractions are crepant and index one.

Hence

```text
global canonical index(Y)=3.
```

## 4. Numerical invariants and carrier reformulation

The exact identities are now

```text
(3K_Y)^2 = P^2 = 336,
K_Y^2 = 112/3,
e(Y_reg)=16.
```

A hypothetical irreducible carrier is disjoint from the exceptional locus and descends unchanged
to the smooth locus:

```text
C_Y in |3l K_Y|,
normalization genus(C_Y)=1.
```

## Next leaf

The canonical-cover route is now precise:

```text
MB104-Z43-INDEX-THREE-CANONICAL-COVER-PREFLIGHT
```

At each nonrational contraction point, study the degree-three canonical index-one cover and decide
whether the retained cuboid contraction data determine its analytic model sufficiently for
Gorenstein/local-Chern methods.

## Firewalls

```text
P_exactly_descends_as_line_bundle=true
three_KY_Cartier=true
global_canonical_index=3
canonical_cover_analytic_type_classified=false
surviving_orbits_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
