# Stage35-EX Goal4Y source lock — open receiver UPic two-class lift

Scope: lift the two exact Goal4X classes in `H^1(Gal(Q(i,sqrt(2))/Q), Pic(Ubar)) ~= (Z/2)^2` through the **open** extended Picard complex and materialize one finite boundary-residue representative for each lift. This leaf does not compute the full algebraic Brauer group, an explicit quaternion/Azumaya formula, local evaluations, or a Brauer--Manin obstruction.

## Geometry and parent locks

Current batch base main: `8a04691d03f8ec17cf2236aab3d0f0d2dbde3fc3`.

Parent Goal4X:
`stages/stage35-ex/35ex-35/goal4x-open-receiver-boundary-picard-galois-h1.json`.

The Stage35 open receiver is the smooth open surface `U={h != 0}` inside the smooth proper minimal resolution `S`. Goal4X fixes the full geometric boundary `D=S\U` as 32 irreducible curves and the exact sequence on geometric divisor classes

`Z[D_i] -> Pic(Sbar) -> Pic(Ubar) -> 0`.

The boundary map has rank 29 with Smith nonzero diagonal `1^29`; hence

`Pic(Ubar) ~= Z^35`.

Its kernel has rank `32-29=3`. This is the geometric unit lattice `U(Ubar)=kbar[U]^*/kbar^*` in the compactification divisor sequence. The exact computation below shows the induced `cc,ct` action on this rank-3 lattice is trivial. This matches the three Q-defined affine units visible directly from the equations:

`(p+x)(p-x)=1`,
`(q+y)(q-y)=1`,
`(w+z)(w-z)=1`.

The SNF kernel basis used by the verifier is an exact integral basis of the same rank-3 unit lattice; no claim is made that the arbitrary SNF basis vectors equal the three displayed units term-by-term.

## Extended Picard source

Mikhail Borovoi and Joost van Hamel, *Extended Picard complexes and linear algebraic groups*, J. reine angew. Math. 627 (2009), 53--82; arXiv `math/0612156`.

Load-bearing statements:

- Definition / Section 2: for a smooth geometrically integral variety `X`, `UPic(Xbar)` is a two-term Galois complex with
  `H^0 = kbar[Xbar]^*/kbar^*` and `H^1 = Pic(Xbar)`.
- Proposition 2.13: if `Y` is a smooth compactification of `X`, the complement-divisor permutation module enters a distinguished triangle relating `UPic(Xbar)` and `Pic(Ybar)`. In the present proper `S` / boundary `D` situation this is represented by the two-term lattice complex
  `[ Z[D_i] -> Pic(Sbar) ]`
  in degrees `0,1`.
- Corollary 2.20(ii): for smooth geometrically integral `X`, there is a canonical injection
  `Br_a(X) -> H^2(Q,UPic(Xbar))`, which is an isomorphism when `X(Q)` is nonempty (or when `H^3(Q,kbar^*)=0`).

A rational smooth point on the present `U` is

`(x,y,p,q,z,w)=(3/4,0,5/4,1,3/4,5/4)`.

It satisfies all four affine equations and is smooth because the `p,q,z,w` Jacobian columns give rank 4. Therefore `U(Q)` is nonempty and the Corollary 2.20(ii) isomorphism applies:

`Br_a(U) ~= H^2(Q,UPic(Ubar))`.

This is deliberately the extended-Picard statement; the proper shortcut `Br_a(U)=H^1(Q,Pic(Ubar))` is not used because `Ubar` has nonconstant units.

## Exact finite V4 complex

All geometric divisor/Picard/unit actions used here factor through

`G = Gal(Q(i,sqrt(2))/Q) = <cc,ct> ~= C2 x C2`,

with `cc: i -> -i` and `ct: sqrt(2) -> -sqrt(2)`.

Goal4Y uses the exact four-term lattice sequence

`0 -> K -> Z^32 -> Z^64 -> Z^35 -> 0`,

where

- `K ~= Z^3` is the unit kernel;
- `Z^32` is the permutation lattice on the 32 boundary components;
- `Z^64 = Pic(Sbar)` is the full marked Picard lattice;
- `Z^35 = Pic(Ubar)` is the Goal4X quotient.

For each of the two Smith generators of `H^1(G,Pic(Ubar))`, the verifier performs the two connecting steps explicitly:

1. lift the 1-cocycle to `Pic(Sbar)` and take its coboundary in the rank-29 boundary image;
2. lift that boundary-image 2-cocycle to `Z^32`; its next coboundary lands in `K ~= Z^3`.

Both resulting normalized `K`-valued 3-cocycles are certified integral coboundaries. Hence both Goal4X `H^1` generators survive the open-surface unit transgression and admit classes in the finite `G` hypercohomology of `[Z^32 -> Pic(Sbar)]`.

Inflating the displayed cochains from `G` to the absolute Galois group preserves the cochain identities, so these are genuine classes in `H^2(Q,UPic(Ubar))`, hence in `Br_a(U)` by the cited Corollary 2.20(ii).

## Boundary residue representatives

After killing each unit-kernel 3-coboundary, the verifier obtains an actual `Z^32`-valued normalized 2-cocycle. The boundary permutation lattice has:

- 24 Q-defined fixed components, each with stabilizer `V4`, giving two residue-character bits `(cc,ct)`;
- 4 size-2 conjugate orbits, each with stabilizer `<ct>`, giving one residue-character bit.

Thus a finite residue representative has 52 F2 coordinates. For a Q-defined component, the bit pairs mean

- `(1,0)` = the quadratic character of `Q(i)/Q`, squareclass `-1`;
- `(0,1)` = the quadratic character of `Q(sqrt(2))/Q`, squareclass `2`;
- `(1,1)` = their sum, squareclass `-2`.

Boundary component ordering is the Goal4X ordering:

1. components 1--8 = known divisor indices `1..8` (strict infinity conics);
2. components 9--24 = known exceptional indices `93..108`;
3. components 25--32 = known exceptional indices `117..124` (four `cc`-conjugate pairs).

A chosen representative for the first lifted class has nonzero residues:

- known indices `1..8`: character `(-2)`;
- known exceptional indices `93..100`: character `(2)`;
- all remaining boundary orbits: zero.

A chosen representative for the second lifted class has nonzero residues:

- known indices `1..8`: character `(-1)`;
- known exceptional indices `[94,96,98,100,101,103,105,107]`: character `(-1)`;
- all remaining boundary orbits: zero.

These two 52-bit residue vectors are nonzero and F2-independent. All their nonzero entries occur on Q-defined components, whose function fields have constant field Q, so the indicated constant quadratic characters remain nontrivial after inflation. This also certifies that the two lifted algebraic Brauer classes are nonzero and independent.

The chosen residue lifts are not canonical: changing the `H^2(G,Z^32)` lift by the image of `H^2(G,K)` changes the representative by the algebraic unit-symbol layer. Goal4Y claims existence and one exact gauge-fixed residue representative for each of the two Goal4X classes, not a canonical basis of the full algebraic Brauer group.

## Existing obvious-symbol layer

The retained Stage35-EX 35EX-22 certificate already contains the three Q-defined units `p+x`, `q+y`, `w+z` among its seven linear squareclass generators and studies 28 obvious quaternion symbols. That earlier certificate explicitly did **not** compute the full Brauer group. Goal4Y therefore does not identify the two new cohomological lifts with specific members of that 28-symbol presentation without an additional exact rational-function adapter.

## Firewall and next gap

Certified here:

- the rank-3 geometric unit layer is explicit at the lattice level and has trivial `cc,ct` action;
- both Goal4X `H^1` generators have zero two-step unit transgression;
- both lift to genuine independent classes in `Br_a(U)`;
- one exact finite boundary-residue character representative is materialized for each.

Not certified here:

- the full group `Br_a(U)` (the Q-defined unit lattice permits further character-symbol classes beyond this two-dimensional lifted subspace);
- a quaternion/Azumaya/rational-function formula for either lifted class;
- an identification with the earlier 28 obvious symbols;
- local evaluation maps on the Stage35 physical adelic set;
- verticality relative to the genus-5 fibration;
- a Brauer--Manin obstruction;
- E1, R29-PESCH-E1, R29-FIB2, Stage35 closure, or any perfect-cuboid theorem.

The next exact leaf should materialize an evaluable rational-function/quaternion/cyclic-algebra representative for the two lifted classes (or prove a precise obstruction to such a presentation) before attempting local evaluation.
