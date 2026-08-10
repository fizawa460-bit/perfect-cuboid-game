# Stage14-toolbox-ah — two-quadrics and genus-one geometry

## Purpose

Turn the merged Stage14 genus-one geometry into a reusable toolbox layer without strengthening any source theorem.

This stage separates two distinct models which had both begun to be described informally as “the genus-one curve”:

1. the fixed global-witness packet `C_sigma` as a smooth `(2,2)` complete intersection in `P^3`;
2. the merged 4bq diagonal-pair reduced-slope quartics used to obtain a genuine moving-family count.

It also performs ongoing toolbox maintenance after new main-track merges. The historical `41/42 -> 1/2` gap `10/21` and the intermediate 4bq `61/63` checkpoint are retained for provenance, while merged 4br supplies the current whole-family exponent `20/21`.

## Canonical source boundary

Canonical theorem sources used here are already merged:

```text
Stage14-s6-02 / PR #348 / merge 1338ee0170a6d92c26a9dd4fa21c886a8125d6db
Stage14-4bq   / PR #395 / merge aa21a3604cf72e06f797c8ba2ecff96b49e60f44
Stage14-4br   / PR #396 / merge 01afa63539e32e62070a84927bbc0530241a79e9
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

At the 4bq checkpoint the exhaustive sector maximum was `61/63`, giving the first full direct post-local saving `1/126` and remaining square-root gap `59/126`.

Merged 4br then improves the cross branch to

```text
E_cross(B)<<B^(20/21+o(1)).
```

and recombines

```text
small partner leg : 20/21,
cross branch      : 20/21,
good-cell residual: 13/14.
```

Hence the current whole-family main-track upper bound is

```text
V(B)<<B^(20/21+o(1)).
```

Exact current ledger:

```text
41/42 - 20/21 = 1/42  # cumulative proved post-local saving
20/21 - 1/2   = 19/42 # current remaining gap to sqrt scale
```

The historical cards remain linked by supersession:

```text
10/21 historical pre-post-local gap
 -> 61/63 / 59/126 checkpoint after 4bq
 -> 20/21 / 19/42 current checkpoint after 4br.
```

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
TB-LEDGER-current-main-after-4br
```

The 4bq ledger is already `SUPERSEDED`; it is counted as an ah-created canonical history card, while 4br is the current successor.

## Boundary

```text
STAGE14_TOOLBOX_AH=COMPLETE_TWO_QUADRICS_AND_GENUS_ONE_GEOMETRY
CANONICAL_NEW_CARD_COUNT=10
CANONICAL_TOTAL_CARD_COUNT=48
FIXED_PACKET_TWO_QUADRICS_MODEL_FROZEN=true
FIXED_PACKET_PENCIL_DETERMINANT_FROZEN=true
FIXED_PACKET_SMOOTH_GENUS_ONE_FROZEN=true
POSITIVE_DIMENSIONAL_COORDINATE_BOUNDARY=false
CONIC_PLUS_FOUR_BRANCH_SQUARE_LIFT_FROZEN=true
DIAGONAL_PAIR_MOVING_SLOPE_GENUS_ONE_FROZEN=true
DIAGONAL_PAIR_GENUS_ONE_GOOD_RESIDUAL_BOUND=13/14
HISTORICAL_4BQ_WHOLE_FAMILY_EXPONENT=61/63
CURRENT_WHOLE_FAMILY_EXPONENT=20/21
CUMULATIVE_POST_LOCAL_SAVING=1/42
CURRENT_REMAINING_GAP_TO_SQRT=19/42
HISTORICAL_10_21_LEDGER_SUPERSEDED_AS_CURRENT=true
HISTORICAL_4BQ_LEDGER_SUPERSEDED_AS_CURRENT=true
GENUS_ONE_ALONE_IMPLIES_MOVING_FAMILY_SAVING=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-ai compact torsion denominator and half-angle identities
```
