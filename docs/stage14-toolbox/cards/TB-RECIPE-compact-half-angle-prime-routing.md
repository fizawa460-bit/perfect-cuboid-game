# Compact half-angle prime routing recipe

```yaml
ID: TB-RECIPE-compact-half-angle-prime-routing
TYPE: RECIPE
STATUS: CURRENT
TITLE: Route a physical partner-leg prime into denominator, cancellation, or cross support
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-07
SOURCE_PR: 364
SOURCE_MERGE_SHA: c51992e2373c0f7f265275c211684f6bd5ef9ccf
SOURCE_FILES:
  - stages/stage14/14-s6-06/result.md
  - stages/stage14/14-s6-07/result.md
  - stages/stage14/14-4bl/result.md
```

## INPUT

A physical pair `(F1,F2,d)` and a prime power `p^e||X2`.

## OUTPUT

Use this dispatch:

```text
1. If p=2 or p|H, send the prime power to X2_cross.
2. Otherwise p is good odd support.
3. Determine whether p^e lies in t2- or t2+.
4. Transfer the physical edge to F3 and determine whether p^e lies in t3- or t3+.
5. Place p^e in exactly one of q--,q-+,q+-,q++.
6. Read the selector meaning:
   q-+ -> D_- denominator,
   q-- -> k_- cancellation,
   q+- -> D_+ denominator,
   q++ -> k_+ cancellation.
```

Equivalently, for good odd primes the physical root sign is not extra data; it is the `F3` half-angle column.

## VARIABLE DICTIONARY

- `X2_cross` = 2-primary and partner-leg prime powers whose primes divide `H`.
- `q_{sign,sign}` = good odd half-angle gcd cells.

## USED BY

- Main/s physical incidence decompositions.
- Converting root-sign statements into gcd/divisor statements.
- Selecting the correct receiver without rederiving torsion formulas.

## DO NOT USE FOR

- Do not assign a free factor `2^{-omega(X2_good)}` to the root signs.
- Do not discard `X2_cross` when applying the four-cell product.
- Do not infer a whole-family saving solely from a large routed factor.

## PROVENANCE NOTES

The recipe packages the merged s6-06 denominator laws, s6-07 third-face gcd matrix, and 4bl dual-selector notation.