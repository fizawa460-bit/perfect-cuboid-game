# Stage32 post1490 O210 marked tangent / infinitely-near information boundary

## Scope

This note checks only whether the already-retained fixed `g1-d186`, `O=210`, `q'=4` evidence contains first-order tangent directions, branch-direction pairings, or infinitely-near data for the hypothetical upstairs carrier `D` at the 48 marked points of `X`.

It does not construct a carrier, prove effectivity, or strengthen the multiplicity-only bounds.

## Frozen upstream source

The retained Testa--Stoll implementation is frozen at:

- repository: `MichaelStollBayreuth/Verification`
- commit: `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`
- file: `Cuboids/cuboids.magma`
- git blob SHA1: `0422b69847f2afb97cb7b3ed02ebef91279f61b1`

That source defines the box surface by four quadrics, obtains the 48 singular points as `pts := Points(SingularSubscheme(S));`, and represents exceptional intersections of a tested curve numerically by `pt in C select Multiplicity(C, pt) else 0`.

Its retained Picard machinery records intersection numbers/classes and automorphism permutations. It does not serialize a local equation, tangent cone, branch jet, strict-transform intersection on the exceptional `P^1`, or an infinitely-near cluster for an unknown curve represented only by a Picard class.

## Retained fixed-V6 witness boundary

`post1473-v6-witness-body-recovered.json` contains only numerical class/intersection data: 64 Picard coordinates, 140 pairings, self-intersection, translation vectors/hashes, and exceptional support. It contains no defining equation or local branch parametrization for an actual curve.

`post-21bl-effectivity-gap-separation.json` already locks that no actual effective curve certificate, integral irreducible curve certificate, or geometric genus-one normalization certificate is present. The numerical witness therefore cannot be promoted to an actual carrier whose tangent directions can be read off.

## What the post1490 local adapters add

The relative-H node-action certificate fixes the three nonidentity deck permutations on the 48 marked points. The local-multiplicity adapter fixes `mult_x(D)` and hence the universal bound `I_x(D,t(D)) >= mult_x(D) mult_x(t(D))`.

The marked multiplicity-only boundary proves that all such multiplicity-only information forces only `3350` of the exact `8586` defect budget, leaving `5236` unforced.

None of those retained objects contains branch tangent directions, equality of directions for `D` and `t(D)`, or next multiplicities after blowup.

## Exact information boundary

A tangent or infinitely-near refinement is not recoverable from the retained numerical class plus marked multiplicities alone. Distinct local curve germs can have the same multiplicity at a smooth point while having different tangent cones and different excess intersection after the first blowup. No positive excess over the already-used product bound may therefore be charged without new local geometric data.

The missing datum must be one of: an actual local equation/parametrization for `D`; a source-locked tangent-cone/branch-direction record with deck transport; an infinitely-near multiplicity cluster/strict-transform intersection record; or an independent global theorem/constraint that strengthens the defect budget without local jets.

Because actual effectivity/carrier existence is still open, initiating a tangent computation directly from the Picard64 witness would be a semantic category error.

## Decision

The retained-source search closes with an exact information boundary: the marked tangent/infinitely-near route is blocked on nonmaterialized carrier-local geometry. `O=210` is not excluded.

Next seek an independent global constraint or an explicit effectivity/carrier-local-jet materialization. Do not repeat Picard64, node permutations, multiplicity products, or the `8586` budget derivation.
