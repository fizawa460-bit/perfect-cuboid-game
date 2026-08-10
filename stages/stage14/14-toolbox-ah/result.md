# Stage14-toolbox-ah — two-quadrics and genus-one geometry

## Purpose

Turn the merged Stage14 genus-one geometry into a reusable toolbox layer without strengthening any source theorem.

This stage separates two distinct models which had both begun to be described informally as “the genus-one curve”:

1. the fixed global-witness packet `C_sigma` as a smooth `(2,2)` complete intersection in `P^3`;
2. the merged 4bq diagonal-pair reduced-slope quartics used to obtain a genuine moving-family count.

It also performs maintenance required by the new merged main result: the historical `41/42 -> 1/2` gap `10/21` is retained for provenance but is no longer the current whole-family gap after 4bq proves exponent `61/63`.

## Canonical source boundary

Canonical theorem sources used here are already merged:

```text
Stage14-s6-02 / PR #348 / merge 1338ee0170a6d92c26a9dd4fa21c886a8125d6db
Stage14-4bq   / PR #395 / merge aa21a3604cf72e06f797c8ba2ecff96b49e60f44
```

Merged 4bh is recorded as an independent main-track derivation of the fixed-packet geometry, but no open PR is promoted to a canonical source.

## Fixed-packet geometry frozen

For

```text
Q1=d0*u0^2-d1*u1^2-S^2*D^2,
Q2=d2*u2^2-d0*u0^2-X^2*D^2,
```

the projective curve

```text
C_sigma={Q1=Q2=0} subset P^3
```

has exact pencil determinant

```text
d0*d1*d2*lambda*mu*(lambda-mu)*(lambda*S^2+mu*X^2).
```

The four singular pencil parameters are

```text
[0:1], [1:0], [1:1], [-X^2:S^2],
```

and are distinct. Direct Jacobian analysis proves `C_sigma` smooth, hence it is a degree-four genus-one curve.

The coordinate/torsion boundary

```text
u0*u1*u2*D=0
```

has no positive-dimensional component.

Eliminating `u0` gives the smooth conic

```text
d2*u2^2-d1*u1^2=H^2*D^2
```

with square lift

```text
d0*u0^2=d1*u1^2+S^2*D^2,
```

branched at four geometric points.

## Diagonal-pair genus-one geometry frozen

Merged 4bq uses a different genus-one model. With

```text
U=q11*q22,
V=q12*q21,
UV=Q<=B,
```

fixing one diagonal and the normalized core puts the opposite reduced slope on a smooth quartic of the form

```text
W^2=K*(A^2-B^2*t^4)
```

(up to the symmetric sign/order variant).

Pairwise coprimality makes the reduced slope injective back to the moving integer pair. The already-merged bounded-height mechanism gives `B^o(1)` opposite-diagonal multiplicity after one diagonal is fixed.

Since

```text
min(U,V)<=B^(1/2),
```

smaller-diagonal enumeration costs `B^(1/2+o(1))`, so with the `B^(3/7+o(1))` core count,

```text
E_good-res(B)<<B^(13/14+o(1)).
```

This is the important contrast with the fixed witness curve: here an explicit recovery/multiplicity/family-sum mechanism exists, so genus-one information genuinely transfers to a moving-family exponent.

## Current exponent maintenance

Merged 4bq recombines

```text
20/21,
61/63,
13/14,
```

so the current whole-family main-track upper bound is

```text
V(B)<<B^(61/63+o(1)).
```

Exact ledger:

```text
41/42 - 61/63 = 1/126  # already proved post-local saving
61/63 - 1/2   = 59/126 # current remaining gap to sqrt scale
```

Therefore the old `TB-LEDGER-post-local-sqrt-gap` is marked `SUPERSEDED` only as the current global ledger. Its historical `10/21` threshold remains valid in stages that explicitly froze parameters relative to `41/42`.

## New canonical cards

```text
TB-FORMULA-fixed-packet-two-quadrics
TB-FORMULA-two-quadric-pencil
TB-LEMMA-fixed-packet-smooth-genus-one
TB-LEMMA-coordinate-boundary-finite
TB-FORMULA-conic-square-lift
TB-LEMMA-diagonal-pair-genus-one-slope
TB-BOUND-diagonal-pair-genus-one-count
TB-WARNING-genus-one-quantifier-and-model-boundary
TB-LEDGER-current-main-after-4bq
```

## Boundary

```text
STAGE14_TOOLBOX_AH=COMPLETE_TWO_QUADRICS_AND_GENUS_ONE_GEOMETRY
CANONICAL_NEW_CARD_COUNT=9
CANONICAL_TOTAL_CARD_COUNT=47
FIXED_PACKET_TWO_QUADRICS_MODEL_FROZEN=true
FIXED_PACKET_PENCIL_DETERMINANT_FROZEN=true
FIXED_PACKET_SMOOTH_GENUS_ONE_FROZEN=true
POSITIVE_DIMENSIONAL_COORDINATE_BOUNDARY=false
CONIC_PLUS_FOUR_BRANCH_SQUARE_LIFT_FROZEN=true
DIAGONAL_PAIR_MOVING_SLOPE_GENUS_ONE_FROZEN=true
DIAGONAL_PAIR_GENUS_ONE_GOOD_RESIDUAL_BOUND=13/14
CURRENT_WHOLE_FAMILY_EXPONENT=61/63
WHOLE_FAMILY_POST_LOCAL_SAVING=1/126
CURRENT_REMAINING_GAP_TO_SQRT=59/126
HISTORICAL_10_21_LEDGER_SUPERSEDED_AS_CURRENT=true
GENUS_ONE_ALONE_IMPLIES_MOVING_FAMILY_SAVING=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-ai compact torsion denominator and half-angle identities
```
