# Stage35-EX Goal4X source lock — open receiver boundary and Picard quotient

Scope: the Stage35 receiver is the smooth open surface `U = {h != 0}` inside the smooth proper minimal resolution `S` of the projective cuboid surface. This lock computes the geometric boundary quotient and its finite Galois cohomology. It does **not** yet construct an explicit Brauer symbol, purity residue representative, or Brauer–Manin obstruction.

## Exact retained geometry

Current batch base main: `8a04691d03f8ec17cf2236aab3d0f0d2dbde3fc3`.

Goal4Q artifact: `stages/stage35-ex/35ex-35/goal4q-compactification-picard-galois-brauer-candidate-preflight.json`, git blob `b1795368ad35e357f7ce5a544c871c665e7b59f9`.

It fixes the projective model in `P^6_[h:x:y:p:q:z:w]`, its 48 A1 nodes, and the `h=0` boundary. On the minimal resolution the full geometric boundary over `h=0` has 32 irreducible components: 8 strict transforms of the Q-defined conics `D(eps,delta,eta)` and the 24 exceptional (-2)-curves above the infinity nodes. Its abstract incidence is the doubled 3-cube and its visible intersection rank is 29.

Goal4U fixes the exact Stoll coordinate adapter `(a1,a2,a3,b1,b2,b3,c)=(h,x,y,z,q,p,w)`. Hence the first 8 upstream known divisor classes are exactly the `a1=0`, equivalently `h=0`, strict transforms.

Goal4V fixes the full geometric Picard group as a free rank-64 lattice generated integrally by the 140 known divisor classes and fixes the exact `cc,ct` Galois action through `Gal(Q(i,sqrt(2))/Q) ~= C2 x C2`.

The Stage33 exact adapter `stages/stage33/33-07/certify_actual_galois_at2_actions.py` reconstructs all 140 known classes and the full integral 64x64 `cc,ct` actions from retained source-locked data. Goal4X identifies the 24 infinity exceptional classes intrinsically as exactly those exceptional classes among known indices 93..140 that intersect one of known classes 1..8. This avoids depending on CAS point enumeration order.

## Picard restriction to the open surface

For a regular locally Noetherian scheme, invertible sheaves on an open subset extend across a complement whose local rings are UFDs; Stacks Project Lemma 31.29.3, Tag `0BD9`. For a smooth/regular surface, combining this with the divisor-class presentation gives the standard exact quotient

`Z[irreducible components of D] -> Pic(Sbar) -> Pic(Ubar) -> 0`.

Goal4X computes the first map using the exact 32 divisor-class vectors above. Its Smith nonzero diagonal is 29 copies of `1`, so the boundary image is primitive of rank 29 and

`Pic(Ubar) ~= Z^35`.

## Exact Galois cohomology computation

The boundary image is `cc,ct` stable. Smith change-of-basis induces exact integral 35x35 `cc,ct` actions on `Pic(Ubar)`.

For `V4=<cc,ct>` a 1-cocycle is represented by `(x,y)` with

`x(1+cc)=0`, `y(1+ct)=0`, `x(1-ct)=y(1-cc)`.

Coboundaries are `(m(cc-1),m(ct-1))`.

The integer Smith computation of `Z^1/B^1` gives

`H^1(V4,Pic(Ubar)) ~= (Z/2)^2`.

Because the absolute Galois action on this marked Picard module factors through this exact V4, this is the finite-module cohomology output relevant to the algebraic-Brauer Hochschild–Serre route. Goal4X intentionally stops before promoting it to a fully materialized `Br_1(U)/Br_0(U)` certificate: the hostile-audit repair specifically requires the open-boundary/purity/localization layer to be explicit before such promotion.

## Firewall

Goal4X does not claim an explicit Brauer class, residue vector, local evaluation, Brauer–Manin obstruction, E1, R29-PESCH-E1 closure, Stage35 closure, or a perfect-cuboid theorem.
