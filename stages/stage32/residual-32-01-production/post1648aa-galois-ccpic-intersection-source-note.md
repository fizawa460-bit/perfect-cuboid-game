# Stage32 post1648AA — exact Galois ccPic intersection and finite fixed-support reduction

## Scope

This scratch leaf keeps the fixed Stage32 target

`g1-d186`, `d=186`, `e=266`, `genus=1`, `O=210`, `q'=4`, `Q=602`

and the current audited residue set

`[73,97,235]`.

It does not assert existence or effectivity of an integral genus-one carrier.  It asks one narrower question: for the already retained exact V6 divisor class `D`, what does source-locked complex conjugation do in the retained Picard lattice, and what is the exact numerical intersection `D.sigma(D)`?

## Exact source chain

The complex-conjugation action is not guessed from an abstract group.  The retained Stage33-07 geometry certificate

`galois-known-class-permutations.json`

source-locks complex conjugation as the field automorphism `i -> -i` in Stoll's pinned `Cuboids/cuboids.magma` geometry and records its exact permutation of the same 92 known curves and 48 exceptional classes used by the Stage32 retained marking.

`certify_actual_galois_at2_actions.py` then transports that 140-class permutation through the existing primitive `INDLIST` Picard recovery and reconstructs an integral 64x64 `ccPic` action in the same basis as the retained Stage32 intersection Gram matrix.  It checks all 140 known-class transports, Gram preservation, involutivity, unimodularity, and hyperplane invariance.  This leaf reuses that adapter runner-side; it does not expand either permanently denylisted retained payload into assistant context.

The fixed V6 class is source-locked by

`stages/stage32/32-21/post1473-v6-witness-body-recovered.json`,

canonical SHA256

`d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`.

Its exact all-140 pairing vector has self-intersection `D^2=758`.

The already retained modular-factor source note

`post1484-v6-modular-factor-bidegree-source-note.md`

uses this same recovered V6 class and proves the factor degrees

`(D.F_z,D.F_w)=(105,81)`.

## Exact Picard calculation

The verifier takes the 64 V6 pairings indexed by the primitive `INDLIST`, solves for `D` in that exact integral Picard basis using the reconstructed Gram matrix, and replays all 140 retained pairings.  It then applies the source-locked integral complex-conjugation matrix.

The exact result is

- `D^2 = 758`;
- `sigma(D)^2 = 758`;
- `D != sigma(D)`;
- `D.sigma(D) = 1116`;
- `(D-sigma(D))^2 = -716`;
- `(D+sigma(D))^2 = 3748`.

The all-140 pairing vector of `sigma(D)` agrees exactly with permutation of the original V6 vector by the retained `cc` permutation.

The modular-factor replay also gives a useful semantic check:

- `D` has bidegree `(105,81)`;
- `sigma(D)` has bidegree `(81,105)`.

Thus complex conjugation exchanges the two modular-factor degrees, so the noninvariance of `D` is visible already at the source-bound factor geometry level and is not a coordinate artifact.

## Conditional geometric consequence

Suppose an integral curve `C` actually exists in the exact V6 divisor class `D`, over a field on which the retained complex conjugation is the relevant Galois involution.  Since `[C]=D` and `[sigma(C)]=sigma(D)` are different divisor classes, `C` and `sigma(C)` are distinct integral curves.  On the resolved smooth surface they therefore have proper zero-dimensional intersection of total intersection length

`C.sigma(C)=D.sigma(D)=1116`.

Every rational point of `C` is fixed by complex conjugation.  Hence, conditionally on existence of such an integral `C`,

`C(Q) subset C intersect sigma(C)`.

This is a finite-support reduction only.  The scheme-theoretic support of the length-1116 intersection has not been materialized or source-bound, so this leaf does not exclude an isolated rational intersection point and does not prove that any rational point exists.

## Arsenal routing / firewall

The applicable formal Arsenal interface is `S30-W02`, `SEMILINEAR_GALOIS_DESCENT_ADAPTER`.  Its contract is used only as a routing firewall: the Galois automorphism and its action must be source-bound before descent-style credit is taken.  Here that semantic binding is supplied by the retained 140-class complex-conjugation certificate and exact Picard adapter.  The Arsenal card itself supplies no Stage32 arithmetic credit.

## Decision

Obtained exactly:

- a source-bound integral `ccPic` action on the retained V6 Picard class;
- the exact numerical intersection `D.sigma(D)=1116`;
- the exact bidegree swap `(105,81) -> (81,105)`;
- conditionally on integral-curve existence, the finite fixed-point support reduction `C(Q) subset C intersect sigma(C)` with total length 1116.

Not obtained:

- effectivity or existence of an integral curve in class `D`;
- the scheme-theoretic support of `C intersect sigma(C)`;
- exclusion of isolated rational intersection points;
- a residue-specific Q602 commutator;
- exclusion of any of `73,97,235`;
- `Q602` or `O210` exclusion;
- authorization of `O212+`;
- controller, receiver, route, theorem, endpoint, or perfect-cuboid credit.

The next exact Galois route is therefore to source-bind the scheme-theoretic support of `C intersect sigma(C)` or an equivalent local complex-conjugation fixed-point adapter.  The numerical intersection number alone is exhausted as an exclusion mechanism.
