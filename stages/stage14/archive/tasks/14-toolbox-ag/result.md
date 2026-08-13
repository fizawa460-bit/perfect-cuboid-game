# Stage14-toolbox-ag — odd kernel edge packet and full-radical incidence

## Purpose

Package the merged Stage14 global-witness squarefree support and radical-incidence results into a stable reusable interface for both the main and s routes.

This stage owns no new Stage14 theorem. Canonical sources are merged PR #345 (`s6-01`), merged PR #349 (`4bi-L`), merged PR #352 (`4bi-S`), and merged PR #355 (`4bj`).

## Canonical cards added

```text
TB-FORMULA-signed-kernel-edge-packet
TB-DICTIONARY-kernel-five-column-refinement
TB-LEMMA-composite-squarefree-line-cover
TB-LEMMA-full-leg-radical-modulus
TB-BOUND-radical-poor-hypotenuse-family
TB-RECIPE-radical-incidence-small-D-dichotomy
TB-WARNING-radical-incidence-quantifier-boundary
```

## Reusable chain

The integral witness factors have signed squarefree kernels

```text
d0=tau0*a*b
d1=tau1*a*c
d2=tau2*b*c
```

with exactly 16 sign/2-primary packets and

```text
a|rad_odd(S)
b|rad_odd(X)
c|rad_odd(H).
```

The selected kernels refine uniquely to the same five Euclid columns as the local descent system.

For any odd squarefree modulus `q` and unit quadratic ratio, the solution set is covered by at most `2^omega(q)` CRT projective lines, each a rank-two lattice of index `q`, giving

```text
N_q(U,V) <<_eps B^eps*(U*V/q + min(U,V) + 1).
```

Merged 4bi-S strengthens the selected edge modulus to the full odd leg radicals

```text
R_S=rad_odd(S)
R_X=rad_odd(X)
R_H=rad_odd(H),
```

with exact congruences

```text
tau0*b*u0^2 == tau1*c*u1^2 (mod R_S)
tau2*c*u2^2 == tau0*a*u0^2 (mod R_X)
tau2*b*u2^2 == tau1*a*u1^2 (mod R_H).
```

Thus neither a large-prime factor nor a large selected kernel is required for a useful modulus.

## Global versus coordinate statements

The radical-poor hypotenuse family has the genuine supported base/class bound

```text
R_H<=B^rho -> O(B^(rho+epsilon)).
```

By contrast, the radical-rich rectangle estimate is a coordinate-density statement. If

```text
R_H>=B^rho
U_*=max(|u1|,|u2|)>=B^nu,
```

then the fixed witness layer gains

```text
B^(-min(rho,nu)+epsilon).
```

If `U_*<B^nu`, the exact equation forces

```text
D<2B^nu.
```

At the merged main-track critical choice

```text
rho=1/2
nu=10/21,
```

the radical-poor base/classes are at square-root scale and the long-coordinate layer contains the full missing `10/21` coordinate exponent. The quantifier transfer to an unweighted packet-existence saving remains separate.

## Hard warnings

Do not identify

```text
selected kernel a,b,c
with
full radical R_S,R_X,R_H.
```

Do not restore an obsolete largest-prime condition after the composite/full-radical modulus theorems.

Do not multiply the `B^(41/42)` packet count by a coordinate-density factor without an existence/occupancy theorem.

## Boundary

```text
STAGE14_TOOLBOX_AG=COMPLETE_ODD_KERNEL_EDGE_PACKET_AND_FULL_RADICAL_INCIDENCE
CANONICAL_NEW_CARD_COUNT=7
CANONICAL_TOTAL_CARD_COUNT=38
SIGNED_KERNEL_EDGE_PACKET_FROZEN=true
TAU_PACKET_COUNT=16
KERNEL_FIVE_COLUMN_REFINEMENT_FROZEN=true
COMPOSITE_SQUAREFREE_LINE_COVER_FROZEN=true
FULL_ODD_LEG_RADICAL_MODULUS_FROZEN=true
RADICAL_POOR_BASE_CLASS_BOUND_FROZEN=true
RADICAL_RICH_LONG_OR_SMALL_D_RECIPE_FROZEN=true
LARGEST_PRIME_REQUIRED_FOR_INCIDENCE=false
SMALL_SELECTED_KERNEL_INTRINSIC_MODULUS_OBSTRUCTION=false
COORDINATE_DENSITY_IMPLIES_PACKET_EXISTENCE_SAVING=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-ah two-quadrics and genus-one geometry
```
