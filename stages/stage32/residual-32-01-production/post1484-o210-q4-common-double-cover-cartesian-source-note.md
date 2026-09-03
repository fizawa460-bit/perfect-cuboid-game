# Stage32 post-1484 O=210 common-double-cover Cartesian identity

Scope: fixed recovered V6 class `g1-d186` only. This note corrects the active interpretation of the preceding Pic/2 reduction. The abstract Pic/2 reduction is algebraically valid for two arbitrary maps `z,w:N->X(4)`, but a genuine Stage32 carrier is not an arbitrary pair: it maps to the box quotient itself. The global subgroup quotient forces the two quadratic pullbacks to be the same Beauville double cover.

## Retained quotient data

Use the already source-locked modular quotient data only:

- `Z=X(8)`;
- `G=Gamma[4]/Gamma[8]`, order 8;
- `H=Gamma'[4]/Gamma[8] ~= V4`, order 4 and index 2 in `G`;
- `P=Z x Z`, with the relevant groups acting diagonally;
- `X=P/H_diag`, the Beauville cover surface;
- `B=P/G_diag`, the box quotient at the retained normal/open level;
- `C0=Z/H`, genus 2;
- `X(4)=Z/G`, genus 0;
- `X->B` and `C0->X(4)` both have generic degree 2.

The retained Beauville note source-locks `P->X` as the free degree-four `H` quotient and `X->B` as the residual degree-two cover. The V4 quotient certificate source-locks `Z->C0` as the free degree-four `H` quotient and `C0->X(4)` as the residual degree-two quotient. The post-1484 modular-factor source note source-locks the two maps `B->X(4)` induced from the two factors.

## Index-two quotient square

For either factor there is a natural commutative square

`X=P/H_diag  ->  C0=Z/H`

`   |                 |`

`   v                 v`

`B=P/G_diag  ->  X(4)=Z/G`.

On the generic free-action locus this square is Cartesian. Indeed, fix a generic diagonal `G`-orbit `[(x,y)]` in `B` and an `H`-orbit of the selected factor lying over its `G`-orbit in `X(4)`. The selected `H`-orbit determines one coset in `G/H`. Applying a representative of that coset diagonally to `(x,y)` determines exactly one `H_diag`-orbit in `P`. Conversely that `H_diag`-orbit maps to the prescribed two points. Thus the generic fiber product has exactly the same function field as `X`.

Since the relevant objects are taken with normalization when passing through the quotient singularities, the precise statement needed by Stage32 is:

`X is the normalization of B x_{X(4)} C0`

for either factor map `B->X(4)`.

This is only the elementary subgroup-lattice identity for an index-two normal subgroup, applied to the retained diagonal quotient geometry. No new receiver-specific existence assertion is imported.

## Consequence for a hypothetical carrier

Let `N` be the normalization of a hypothetical integral carrier mapping to `B`, and let `Y` be the normalization of its Beauville pullback `N x_B X`. Base-changing the normalized quotient square gives, for both factor maps `z,w:N->X(4)`,

`Y = normalization(N x_{z,X(4)} C0)`

and

`Y = normalization(N x_{w,X(4)} C0)`.

Hence both quadratic pullbacks have the same function field `K(Y)`.

If `K(C0)=K(X(4))(sqrt(F))`, then

`K(N)(sqrt(F(z))) = K(Y) = K(N)(sqrt(F(w)))`.

Therefore

`F(w)/F(z) in K(N)^{*2}`,

and the Pic/2 difference class introduced in the previous symbolic reduction is necessarily

`[ 1/2 div(F(w)/F(z)) ] = 0 in Pic^0(N)[2]`.

The zero class is conditional on the carrier mapping to `B`; it is not a newly computed invariant of the bare V6 numerical class. This distinction is important. The previous statement `current_retained_data_determines_D_class=false` was appropriate for an arbitrary pair of factor maps considered without the global `N->B` lift, but it is too weak for the actual carrier hypothesis.

## What this does and does not do

The Pic/2 class is therefore not a live exclusion route. Its vanishing is a compatibility identity already built into any genuine carrier. It does not prove that a carrier exists, and it does not make the provisional first-projection Hurwitz witness into a carrier.

The live question returns to simultaneous correspondence geometry on the same source:

- `Y->C0` degree 105 and etale;
- `Y->C0` degree 81 with ramification 48;
- both maps come from the same `N->B` / resolved V6 geometry.

Thus the next exact leaf is `O210_Q4_SIMULTANEOUS_105_81_CORRESPONDENCE_GEOMETRY`.

O=188 remains CLOSED_AUDITED. O=210 remains OPEN. FULL178 remains inactive. No receiver, route, theorem, endpoint, or perfect-cuboid credit follows. Promotion requires bounded hostile audit.
