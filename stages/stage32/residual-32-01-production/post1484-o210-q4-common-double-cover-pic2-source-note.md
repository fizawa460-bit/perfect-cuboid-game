# Stage32 post-1484 O=210 common-double-cover Pic/2 reduction

Scope: fixed recovered V6 class `g1-d186` only. This is a symbolic reduction of the current common-cover compatibility problem. It does not compute the resulting `Pic^0(N)[2]` class and therefore does not exclude O=210.

## Quadratic pullback formulation

The retained V4 quotient certificate gives a genus-two double cover

`C0 -> X(4)=P1`

branched at the six quotient cusps / Weierstrass points. Over the complex function field choose a rational coordinate `u` on `P1` and a representative `F(u)` for that quadratic extension, so

`K(C0)=C(u)(sqrt(F(u)))`.

We may choose the representative so that its six finite branch values occur with odd valuation and its pole divisor is even; a degree-six branch polynomial is the standard model after moving the branch values away from infinity.

Let `z,w:N->X(4)` be the two modular factor maps, of audited degrees 105 and 81. Pulling the same quadratic cover back along the two maps gives

`K_z = K(N)(sqrt(F(z)))`,

`K_w = K(N)(sqrt(F(w)))`.

For a field of characteristic not two and nontrivial quadratic extensions, the elementary identity

`K(sqrt(a)) = K(sqrt(b))  <=>  a/b in K^{*2}`

shows that the two pullbacks define the same double cover of `N` exactly when

`q := F(w)/F(z)`

is a square in `K(N)^*`.

This is the correct common-cover condition. Constructing an unrelated degree-81 cover on another genus-one source would not address it.

## Why local parity is already equal

At every exceptional contact the retained cusp adapter has local modular degrees `A_z,A_w` of the same parity, and that parity is the parity of the exceptional multiplicity `m`.

At the audited O=210 extremal profile all contacts have `m=1` or `m=2`:

- each of the 210 `m=1` contacts gives odd valuation for both `F(z)` and `F(w)`;
- each of the 28 `m=2` contacts gives even valuation for both.

A strict-boundary contribution to an `X(4)` cusp fiber has local degree `2*l`, hence contributes even valuation. The chosen pole divisor of `F` is even, so poles also contribute even valuation after pullback.

Therefore every valuation of `q=F(w)/F(z)` is even. Equivalently,

`div(q)=2D`

for an integral degree-zero divisor `D` on the smooth genus-one normalization `N`. The common odd branch support of the two quadratic pullbacks is precisely the 210 `m=1` exceptional contacts.

## The remaining obstruction is Picard 2-torsion

Because `div(q)=2D` is principal, the divisor class `[D]` satisfies

`2[D]=0` in `Pic^0(N)`.

Thus the difference between the two quadratic pullbacks is an unramified quadratic twist represented by

`[D] in Pic^0(N)[2]`.

For a complex genus-one curve,

`Pic^0(N)[2] ~= (Z/2)^2`,

so there are exactly four possible classes. Moreover

`q is a square  <=>  [D]=0`.

Hence the common Beauville double-cover condition has been reduced from an unconstrained degree-81-map problem to a four-state `Pic/2` test. The local parity data proves only that the obstruction is unramified; it does **not** decide which of the four classes occurs.

Equivalent topological form: the difference of the two pullback quadratic characters is an unramified `Z/2` character of `N`, hence an element of `H^1(N,F2)` with four possibilities. Equality of the two double covers means the zero character.

## Current exact blocker

Materialize

`[D] = [ 1/2 div(F(w)/F(z)) ] in Pic^0(N)[2]`

from source-locked V6 / modular divisor data, or compute the equivalent difference character on a basis of `H_1(N,F2)`.

- If the class is forced nonzero, O=210 is excluded at this layer (still subject to hostile audit).
- If the class is zero, the common double-cover condition survives and the next obstruction is the simultaneous degree-81 / full-V4 geometry.

No existing retained histogram, node-capacity count, or first-projection Hurwitz witness determines this class by itself. Do not infer zero merely from equality of branch parity.

O=188 remains CLOSED_AUDITED. FULL178 remains inactive. No receiver, route, theorem, endpoint, or perfect-cuboid credit follows. Promotion requires bounded hostile audit.
