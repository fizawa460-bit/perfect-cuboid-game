# Stage14-toolbox-ac — current exponent and saving ledger

## Purpose

Stage14-toolbox-ac turns the accumulated main/s exponent history into a reusable, scale-safe ledger. It does not prove a new Stage14 theorem.

The main failure mode being removed is numerical-looking but logical: the repository now contains whole-family exponents, Euclid-scale savings, sector-only bounds, forced variable scales, and method ceilings. Their fractions can be compared numerically while their quantifiers are incompatible.

This stage therefore freezes both the current strongest whole-family input and the historical supersession chain, then labels specialized current exponents by scope.

## Current whole-family chain

The same normalized s5 local problem improved as follows:

```text
s5s: delta_M=1/200 -> physical exponent 399/400
s5t: delta_M=1/41  -> physical exponent 81/82
s5u: delta_M=1/21  -> physical exponent 41/42   [CURRENT]
```

using

```text
M<=sqrt(B),
M^(2-delta_M) -> B^(1-delta_M/2).
```

The old cards are retained as `SUPERSEDED`; they are not deleted.

## Current square-root budget

```text
current physical whole-family exponent = 41/42
sqrt target exponent                  = 1/2
required post-local saving            = 10/21
```

Exact arithmetic:

```text
41/42 - 1/2 = 10/21.
```

No source used here proves the full post-local `10/21` saving.

## Specialized current exponents

Stage14-4bl proves only on the small-partner-leg sector

```text
X2<=B^(20/21)
=> count << B^(20/21+o(1)),
```

which is a sector-only improvement of

```text
41/42-20/21=1/42.
```

Stage14-s6-07 proves a five-factor structural dichotomy whose remaining branch forces a factor of size

```text
B^(41/420),
```

with

```text
41/420=(41/84)/5.
```

This is a forced variable/incidence scale, not a count saving.

The s5 `1/20` single-edge ceiling is likewise recorded only as a method/module ceiling, not a current whole-system theorem.

## Canonical files added

```text
docs/stage14-toolbox/exponent-ledger.md

docs/stage14-toolbox/cards/TB-BOUND-local-descent-s5s.md
docs/stage14-toolbox/cards/TB-BOUND-local-descent-s5t.md
docs/stage14-toolbox/cards/TB-BOUND-local-descent-current.md
docs/stage14-toolbox/cards/TB-LEDGER-post-local-sqrt-gap.md
docs/stage14-toolbox/cards/TB-BOUND-dual-half-angle-small-leg-sector.md
docs/stage14-toolbox/cards/TB-LEDGER-s6-07-forced-incidence-scale.md
docs/stage14-toolbox/cards/TB-WARNING-exponent-scope-and-transfer.md
```

The canonical registry now contains twelve cards total: the five toolbox-ab cards plus seven toolbox-ac cards.

## Canonical provenance

```text
s5s  PR #328  3cbdde9bc94c55c63f72946805d3315e83c35097
s5t  PR #333  9f9e74f22e80fb8432e865f3eebee8cd7c842fff
s5u  PR #338  516ffb08155e0aa618b2539efb07802a389ca219
s6-00 PR #341 b4c9408441e501cb4d8f9a98b71f809d30a25f97
s6-07 PR #364 c51992e2373c0f7f265275c211684f6bd5ef9ccf
4bl   PR #365 dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
```

All are merged sources. No open PR is canonical provenance.

## Boundary

```text
STAGE14_TOOLBOX_AC=COMPLETE_CURRENT_EXPONENT_AND_SAVING_LEDGER
CURRENT_LOCAL_M_SAVING=1/21
CURRENT_LOCAL_M_EXPONENT=41/21
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=41/42
CURRENT_PHYSICAL_WHOLE_FAMILY_SAVING_VS_B=1/42
SQRT_TARGET_EXPONENT=1/2
REQUIRED_POST_LOCAL_SAVING=10/21
S5S_1_OVER_200_STATUS=SUPERSEDED
S5T_1_OVER_41_STATUS=SUPERSEDED
S5U_1_OVER_21_STATUS=CURRENT
FOUR_BL_SMALL_PARTNER_SECTOR_EXPONENT=20/21
FOUR_BL_SECTOR_GAIN_VS_41_42=1/42
S6_07_FORCED_INCIDENCE_SCALE=41/420
SECTORAL_EXPONENT_PROMOTED_TO_WHOLE_FAMILY=false
FORCED_VARIABLE_SCALE_PROMOTED_TO_COUNT_SAVING=false
SINGLE_EDGE_1_OVER_20_PROMOTED_TO_WHOLE_SYSTEM=false
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-ad Pythagorean and Euclid conversion formulas
```
