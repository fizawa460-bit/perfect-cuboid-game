# Deterministic allocation is not randomness

```yaml
ID: TB-WARNING-deterministic-allocation-not-random
TYPE: WARNING
STATUS: CURRENT
TITLE: Physical root signs and gcd cells do not carry a free Bernoulli density
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-07
SOURCE_PR: 364
SOURCE_MERGE_SHA: c51992e2373c0f7f265275c211684f6bd5ef9ccf
SOURCE_FILES:
  - stages/stage14/14-s6-07/result.md
```

## INPUT
Good odd partner-leg prime powers routed by the physical root sign into the four half-angle gcd cells.

## OUTPUT
Interpret the sign pattern as deterministic divisor allocation:
```text
q--*q-+*q+-*q++=X2_good.
```
No independent probability law follows.

## VARIABLE DICTIONARY
- root sign = the congruence choice forced by the physical third face.
- gcd cell = the corresponding exact shared half-angle divisor.

## USED BY
- Preventing fake character/root-sign savings.

## DO NOT USE FOR
- Do not insert `2^-omega(X2_good)` as a density factor.
- Formal availability of two square roots modulo each prime is not independence on the physical set.

## PROVENANCE NOTES
s6-07 explicitly rejects the independent-Bernoulli root-sign model and replaces it by the exact gcd-matrix factorization.