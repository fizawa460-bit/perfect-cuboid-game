# Stage35-EX Goal4W — proper-surface Picard H1 / algebraic Brauer source lock

## Parent module and exact scope

Goal4V identifies the **smooth proper minimal resolution** `S` of the Stage35-EX projective cuboid surface with the Stoll–Testa cuboid surface and certifies the full integral marked Picard Galois module of `S`:

- `Pic(Sbar)` has rank 64 and discriminant `-2^28`;
- the 140 known divisor classes generate `Pic(Sbar)` integrally;
- all generators are defined over `L = Q(i,sqrt(2))`;
- the absolute Galois action factors through `Gal(L/Q) ~= C2 x C2`;
- the exact integral generators are the retained 64x64 actions `cc` and `ct`.

Goal4W consumes exactly this **proper-surface** module. It does not identify the Picard group of the Stage35 affine/open receiver.

The Stage35 receiver is the retained open locus `U subset S` corresponding to `h != 0`; write `D = S \ U` for its boundary. Goal4W does **not** source-lock the full boundary divisor complex, compute `Pic(Ubar)`, transport its Galois action, or compute purity/localization residues along `D`.

## Stoll–Testa theorem lock

Source: Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, arXiv:1009.0388v2 [math.AG], revision dated 2025-02-24.

Immutable locator: `https://arxiv.org/abs/1009.0388v2`.

Load-bearing result: Theorem 10.

Applied to the smooth proper surface `S`, Theorem 10 gives

`H^1(Q,Pic(Sbar)) = 0`

and

`Br_1(S)/Br_0(S) = 0`.

It does not compute `Pic(Ubar)` or `Br_1(U)/Br_0(U)` for the Stage35 open receiver `U`.

## Exact computational source lock

Pinned verification source:

- repository: `MichaelStollBayreuth/Verification`
- commit: `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`
- path: `Cuboids/cuboids.magma`
- git blob: `0422b69847f2afb97cb7b3ed02ebef91279f61b1`

The pinned source constructs

`Gal := sub<GL(64,Integers()) | [ccPic, ctPic]>`

on the full proper-surface Picard lattice, builds the group-cohomology module, computes degree-one cohomology, and contains the exact assertion

`assert #H1 eq 1;`

followed by the diagnostic that the algebraic Brauer group of the proper cuboid surface over `Q` equals `Br_0`.

This is the same `Pic(Sbar)` module as Goal4V: Stage33-09 locally replays the integral marked basis transport and the exact `cc`,`ct` matrices from the same pinned upstream blob.

## Exact Goal4W consequence

For the smooth proper minimal resolution `S` only,

`H^1(Q,Pic(Sbar)) = 0`

and

`Br_1(S)/Br_0(S) = 0`.

Hence the **proper-S algebraic Brauer route** has no nonconstant algebraic class.

## Open-receiver firewall

No conclusion is promoted from the preceding proper statement to the Stage35 open receiver `U`.

In particular Goal4W does **not** prove any of the following:

- `Pic(Ubar) = Pic(Sbar)`;
- `H^1(Q,Pic(Ubar)) = 0`;
- `Br_1(U)/Br_0(U) = 0`;
- absence of algebraic classes with boundary residue on `D`;
- absence of a vertical/open-receiver Brauer obstruction;
- that every future Brauer route must be transcendental.

The required missing adapter is explicit: source-lock `U subset S` and `D=S\U`, compute the boundary divisor complex and `Pic(Ubar)` with Galois action, then compute the relevant localization/purity residue maps before assigning any open-receiver algebraic-Brauer credit.

## Hostile-audit repair provenance

Hostile audit review `5124106960` on exact head `24cc2973fc022c89cd240fd4a26c92637e1d2e78` returned `FAIL_SCOPE`: the proper-surface theorem was correct, but the prior Goal4W state promoted it to the open Stage35 receiver without the boundary/localization adapter.

This repair chooses the audit's option 1: retain the proper-S theorem and restore the open-receiver algebraic Brauer route to `UNTESTED`.

## Credit firewall

Goal4W does **not** claim:

- the algebraic Brauer quotient of the open receiver is zero;
- the transcendental Brauer quotient is zero;
- a nonconstant Brauer class on the open receiver exists or does not exist;
- a Brauer–Manin obstruction on the Stage35 receiver exists or does not exist;
- E1;
- `R29-PESCH-E1` closure;
- `R29-FIB2` closure;
- Stage35 closure;
- perfect-cuboid existence or nonexistence.

Only the proper-S algebraic Brauer route is closed negatively. The Stage35 open-receiver algebraic Brauer route remains untested.