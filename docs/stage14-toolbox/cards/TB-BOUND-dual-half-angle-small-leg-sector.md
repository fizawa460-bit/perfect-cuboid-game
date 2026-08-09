# Dual half-angle small-partner-leg sector bound

```yaml
ID: TB-BOUND-dual-half-angle-small-leg-sector
TYPE: BOUND
STATUS: CURRENT
TITLE: Stage14-4bl small-partner-leg sector exponent 20/21
SCOPE: MAIN
SOURCE_STAGE: Stage14-4bl
SOURCE_PR: 365
SOURCE_MERGE_SHA: dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
SOURCE_FILES:
  - stages/stage14/14-4bl/result.md
EXPONENT_SCALE: physical B, sectoral
EXPONENT_EXACT: 20/21
SAVING_EXACT: 1/42 versus 41/42 on this sector
CONVERSION: 41/42 - 20/21 = 1/42
```

## INPUT

- Physical ordered edges in the dual compact half-angle setup.
- Primitive partner leg satisfies `X2<=B^(20/21)`.
- The Stage14-4bl physical-edge counting and degree inputs.

## OUTPUT

```text
# {physical edges in X2<=B^(20/21) sector}
  << B^(20/21+o(1)).
```

Relative to the current whole-family `41/42` exponent, this sector alone gains exactly

```text
41/42 - 20/21 = 1/42.
```

The complementary sector `X2>B^(20/21)` carries a dual denominator or cancellation product at the critical scale `B^(10/21)` up to constants.

## VARIABLE DICTIONARY

- `X2` = nonshared leg of the primitive partner face.
- `Q=D_+D_-`, `K=k_+k_-` in Stage14-4bl, with `QK=X2/kappa`.

## USED BY

- Stage14-4 post-local dual-selector route.
- Comparisons with s6 half-angle / gcd-cell decompositions.

## DO NOT USE FOR

- This is not a whole-family `B^(20/21)` theorem.
- The complementary critical-scale product does not by itself prove a counting saving.
- `FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false` remains part of the source boundary.

## PROVENANCE NOTES

Stage14-4bl optimized the split exponent to `20/21` because half of that exponent equals the required `10/21` critical scale.
