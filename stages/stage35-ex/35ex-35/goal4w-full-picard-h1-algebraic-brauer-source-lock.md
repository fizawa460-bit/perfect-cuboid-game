# Stage35-EX Goal4W — full Picard H1 / algebraic Brauer source lock

## Parent module

Goal4V identifies the Stage35-EX minimal resolution with the Stoll–Testa cuboid surface and certifies the full integral marked Picard Galois module:

- `Pic(Xbar)` has rank 64 and discriminant `-2^28`;
- the 140 known divisor classes generate `Pic(Xbar)` integrally;
- all generators are defined over `L = Q(i,sqrt(2))`;
- the absolute Galois action factors through `Gal(L/Q) ~= C2 x C2`;
- the exact integral generators are the retained 64x64 actions `cc` and `ct`.

Goal4W consumes that exact module; it does not reopen the saturation or surface-identification questions.

## Stoll–Testa theorem lock

Source: Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, arXiv:1009.0388v2 [math.AG], revision dated 2025-02-24.

Immutable locator: `https://arxiv.org/abs/1009.0388v2`.

Load-bearing result: Theorem 10.

Theorem 10 proves that the algebraic part of the Brauer group contains no nonconstant algebraic class: the map from `Br(Q)` onto the algebraic part has trivial cokernel. Its proof identifies that cokernel with `H^1(Q,Pic(Xbar))`, reduces the latter to the finite quotient `Gal(Q(i,sqrt(2))/Q)`, and computes it to be zero.

The theorem therefore gives

`H^1(Q,Pic(Xbar)) = 0`

and

`Br_1(X)/Br_0(X) = 0`.

It does not compute the transcendental quotient `Br(X)/Br_1(X)`.

## Exact computational source lock

Pinned verification source:

- repository: `MichaelStollBayreuth/Verification`
- commit: `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`
- path: `Cuboids/cuboids.magma`
- git blob: `0422b69847f2afb97cb7b3ed02ebef91279f61b1`

The pinned source constructs

`Gal := sub<GL(64,Integers()) | [ccPic, ctPic]>`

on the full Picard lattice, builds the group-cohomology module, computes degree-one cohomology, and contains the exact assertion

`assert #H1 eq 1;`

followed by the diagnostic that the algebraic Brauer group over `Q` equals `Br_0`.

This is the same full Picard module as Goal4V: Stage33-09 locally replays the integral marked basis transport and the exact `cc`,`ct` matrices from the same pinned upstream blob.

## Exact Goal4W consequence

Because the full absolute Galois action factors through `Gal(L/Q)` and the pinned exact computation gives trivial first cohomology for that integral module,

`H^1(Q,Pic(Xbar)) = 0`.

By the Hochschild–Serre algebraic Brauer identification used in Stoll–Testa Theorem 10,

`Br_1(X)/Br_0(X) = 0`.

Hence there is no nonconstant algebraic Brauer class and no algebraic Brauer–Manin obstruction available from this surface.

## Credit firewall

Goal4W does **not** claim:

- the transcendental Brauer quotient is zero;
- a nonconstant transcendental Brauer class exists or does not exist;
- a Brauer–Manin obstruction of any kind exists;
- E1;
- `R29-PESCH-E1` closure;
- `R29-FIB2` closure;
- Stage35 closure;
- perfect-cuboid existence or nonexistence.

The algebraic Brauer route is closed negatively; any further Brauer route must be explicitly transcendental and separately source-locked.