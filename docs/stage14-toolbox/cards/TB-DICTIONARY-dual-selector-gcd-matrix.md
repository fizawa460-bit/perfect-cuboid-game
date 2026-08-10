# Dual selector gcd matrix

```yaml
ID: TB-DICTIONARY-dual-selector-gcd-matrix
TYPE: DICTIONARY
STATUS: CURRENT
TITLE: Four good-odd half-angle gcd cells and their selector meanings
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-07
SOURCE_PR: 364
SOURCE_MERGE_SHA: c51992e2373c0f7f265275c211684f6bd5ef9ccf
SOURCE_FILES:
  - stages/stage14/14-s6-07/result.md
```

## INPUT

The exact physical transfer to a third primitive face `F3`, with half-angle roots

```text
t2-,t2+ for F2,
t3-,t3+ for F3.
```

Restrict to odd prime powers of `X2` coprime to `2H`.

## OUTPUT

Define

```text
q--=gcd(t2-,t3-),
q-+=gcd(t2-,t3+),
q+-=gcd(t2+,t3-),
q++=gcd(t2+,t3+)
```

on the good odd support. The four cells are pairwise coprime and

```text
q--*q-+*q+-*q++=X2_good.
```

Selector identification:

```text
(D_-)_good = q-+,
(k_-)_good = q--,
(D_+)_good = q+-,
(k_+)_good = q++.
```

## VARIABLE DICTIONARY

- First sign = partner `F2` half-angle column.
- Second sign = transferred `F3` half-angle column.
- `X2_good` = odd part of `X2` supported on primes not dividing `H`.

## USED BY

- Translating root signs into shared half-angle incidence.
- Identifying denominator vs cancellation prime powers.
- Avoiding repeated analysis of the same four cells under different notation.

## DO NOT USE FOR

- Cross primes dividing `2H` are not in these four cells.
- Do not assume a probability distribution among the four cells.
- A large cell does not automatically provide a fresh density factor inside an equation where it is already an exact square factor.

## PROVENANCE NOTES

Merged Stage14-s6-07 proves the exact 2x2 gcd matrix and the full good-part product identity.