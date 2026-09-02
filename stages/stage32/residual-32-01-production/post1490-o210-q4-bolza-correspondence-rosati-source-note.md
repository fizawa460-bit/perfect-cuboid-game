# Stage32 post-1490 O210 q'=4 Bolza correspondence / Rosati frontier

Scope: fixed recovered V6 class only, target `g1-d186`, `d=186`, `e=266`,
`z=(-15,62,-44,26,32)`, at the retained extremal profile `O=210`, `q'=4`.
This note does not construct or exclude a carrier. It replaces the exhausted
Abel--Jacobi-zero loop by an independent correspondence invariant on the fixed
genus-two quotient.

## Retained Stage32 input

The retained V4 quotient certificate fixes

`C0 = X(8)/(Gamma'[4]/Gamma[8])`

as a genus-two curve, with `X(8)->C0` finite etale of degree four and
`C0->X(4)` a degree-two hyperelliptic map whose six fixed points are the six
quotient cusps.

For a hypothetical O210 carrier, the common-cover Cartesian identity fixes one
connected curve `Y` and two maps

`f1,f2 : Y -> C0`

coming from the two modular factors. The exact bidegree/ramification certificate
gives

`deg(f1)=105`, `deg(R_f1)=0`,
`deg(f2)=81`, `deg(R_f2)=48`.

Thus both Riemann--Hurwitz computations give

`2g(Y)-2 = 105*(2*2-2) = 210`

and

`2g(Y)-2 = 81*(2*2-2)+48 = 210`,

so `g(Y)=106`.

## Exact identification of the genus-two target in the cuboid example

Beauville, *A tale of two surfaces*, arXiv:1303.1910v2, Section 2, starts with
a genus-five curve `C` carrying the free even-sign Klein four subgroup
`Gamma ~= (Z/2)^2`; its quotient `B=C/Gamma` is genus two and is the double
cover of `P1` branched at the six zeros of the three quadratic forms.
For the cuboid example

`u^2=xy`, `v^2=x^2-y^2`, `w^2=x^2+y^2`,

the six branch values are `{0,infinity,+/-1,+/-i}` and Beauville gives

`B : s^2 = x(x^4-1) = x^5-x`.

The same example produces the cuboid surface. Combined with the retained
Freitag--Salvati Manni identification of the genus-five modular curve with
`X(8)` and of the free V4 quotient used by Stage32, this identifies the fixed
Stage32 target `C0` with this Bolza genus-two curve (up to the harmless
coordinate/model isomorphism already implicit in the modular quotient).

This is a target identification only; no hypothetical carrier is imported from
Beauville.

## Jacobian endomorphism lattice

Koziarz--Rito--Roulleau, *The Bolza curve and some orbifold ball quotient
surfaces*, arXiv:1904.00793v4, Introduction and Section 4, use the Abelian
surface

`A = E x E`,  `E = C / Z[i*sqrt(2)]`,

and identify `A` with the Jacobian of the Bolza curve. Hence, as an unpolarized
complex Abelian variety,

`J(C0) ~= E^2`

and therefore

`End(J(C0)) ~= M_2(Z[sqrt(-2)])`.

The principal polarization on this product presentation is not assumed to be
the product polarization. In particular, the Rosati involution must be
source-locked in the chosen `E^2` coordinates before an integral matrix
enumeration is promoted.

## Correspondence endomorphism

Put `J=J(C0)`. For the two maps define

`T = (f1)_* (f2)^* in End(J)`,

where pushforward is the norm map on Jacobians. For a finite map of smooth
proper curves, `(fi)_*(fi)^*=[deg(fi)]`.

Let

`Phi : J x J -> J(Y)`,
`Phi(P,Q)=f1^*(P)+f2^*(Q)`.

With canonical principal polarizations, norm and pullback are Rosati adjoints.
Therefore

`Phi^dagger Phi = [[105, T], [T^dagger, 81]]`

is Rosati-positive semidefinite. Taking the Schur complement of the positive
scalar block `105` gives the exact necessary inequality

`T^dagger T <= 105*81 = 8505`

in the Rosati-positive cone of `End(J) tensor R`.

This is genuinely independent of the already-closed identity
`[2E-R_z+R_w]=0 in Pic^0(N)`: it lives on the fixed genus-two target Jacobian
and is attached to the simultaneous pair `(f1,f2)`.

Because `End(J)` is a finite-rank integral lattice and the Rosati norm is
positive definite, the inequality cuts out only finitely many integral
endomorphisms `T`. It does **not** say that every such `T` is realized by a
pair of maps.

## Exact next datum

The next executable leaf is to source-lock the principal polarization/Rosati
involution on the chosen `E^2` model (equivalently an exact positive Hermitian
matrix for the Bolza principal polarization), then enumerate the finite set

`T in M_2(Z[sqrt(-2)])` with `T^dagger T <= 8505`.

After that enumeration, only extra constraints that are independently forced by
the common quadratic cover / six Weierstrass cusp marking may be imposed.
No Abel--Jacobi coordinate instance for the already-principal divisor is needed.

## Firewalls

- `O=210` is not excluded here.
- The Bolza identification does not construct the fixed V6 carrier.
- The unpolarized product `E^2` is not silently equipped with product Rosati.
- The Rosati bound is necessary, not sufficient, for a geometric correspondence.
- The old degree-93/93 both-etale commensurator argument is not reused for the
  ramified degree-81 map.
- O186/O188 and the Abel--Jacobi-zero loop remain closed.
- FULL178 remains inactive; no receiver, route, theorem, endpoint, or
  perfect-cuboid credit follows.
