# s6-07 forced large-incidence scale

```yaml
ID: TB-LEDGER-s6-07-forced-incidence-scale
TYPE: LEDGER
STATUS: CURRENT
TITLE: Five-factor dichotomy and forced B^(41/420) incidence cell
SCOPE: S
SOURCE_STAGE: Stage14-s6-07
SOURCE_PR: 364
SOURCE_MERGE_SHA: c51992e2373c0f7f265275c211684f6bd5ef9ccf
SOURCE_FILES:
  - stages/stage14/14-s6-07/result.md
EXPONENT_SCALE: physical B, structural threshold
EXPONENT_EXACT: 41/420
CONVERSION: (41/84)/5 = 41/420
```

## INPUT

- The physical edge to `(F2,F3)` transfer from Stage14-s6-07.
- The exact five-factor decomposition
  `X2 = X2_cross*q--*q-+*q+-*q++`.
- The complement of the small-partner-leg sector `X2<=B^(41/84)`.

## OUTPUT

In the remaining physical edges, at least one of the five factors is larger than

```text
B^(41/420)
```

up to the strict/constant conventions of the source. The `X2<=B^(41/84)` sector is already controlled at square-root scale in the source.

## VARIABLE DICTIONARY

- `q--, q-+, q+-, q++` = pairwise-coprime good-odd half-angle gcd cells.
- `X2_cross` = complementary cross-prime overlap factor.

## USED BY

- Stage14-s6 same-modulus incidence receiver.
- Cross-route comparisons with main dual-selector variables.

## DO NOT USE FOR

- `41/420` is a forced variable-size threshold, not a proved `B^(-41/420)` count saving.
- The root-sign allocation is not an independent Bernoulli model; the source explicitly rejects `2^-omega` as an automatic power saving.
- Do not combine this threshold multiplicatively with the whole-family `41/42` count without a proved incidence theorem.

## PROVENANCE NOTES

The factor `1/5` comes from five exact multiplicative cells. This card records the structural scale only; `FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false` remains in force.
