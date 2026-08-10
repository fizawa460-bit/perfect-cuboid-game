# Diagonal-pair genus-one counting consequence

```yaml
ID: TB-BOUND-diagonal-pair-genus-one-count
TYPE: BOUND
STATUS: CURRENT
TITLE: Good-cell residual bound from smaller-diagonal enumeration plus genus-one multiplicity
SCOPE: MAIN
SOURCE_STAGE: Stage14-4bq
SOURCE_PR: 395
SOURCE_MERGE_SHA: aa21a3604cf72e06f797c8ba2ecff96b49e60f44
SOURCE_FILES:
  - stages/stage14/14-4bq/result.md
```

## INPUT

The 4bq diagonal products

```text
U=q11*q22,
V=q12*q21,
UV=Q<=B,
```

and the fixed-core count from the merged preceding good-cell analysis

```text
#cores << B^(3/7+o(1)).
```

For a fixed core and one fixed diagonal, the opposite diagonal has `B^o(1)` admissible choices by the merged genus-one bounded-height mechanism.

## OUTPUT

Since `UV<=B`,

```text
min(U,V)<=B^(1/2).
```

Enumerating the smaller diagonal pair costs

```text
sum_{n<=B^(1/2)} tau(n)=B^(1/2+o(1)).
```

Hence per normalized core

```text
#good-cell residual states <= B^(1/2+o(1)),
```

and globally

```text
E_good-res(B)
 << B^(3/7+1/2+o(1))
 = B^(13/14+o(1)).
```

This is an actual moving-family bound, unlike a per-fixed-curve point estimate by itself.

## VARIABLE DICTIONARY

- `E_good-res(B)` = merged 4bq good-cell residual count.
- `U,V` = diagonal products.
- `B^o(1)` = subpower multiplicity supplied after one diagonal is fixed.

## USED BY

- Closing the good-cell residual without a further largest-prime decomposition.
- Demonstrating a valid transfer from genus-one geometry to a moving-family exponent through an injective reduced-slope parameter and smaller-diagonal enumeration.

## DO NOT USE FOR

- Do not transplant `13/14` to unrelated genus-one families.
- Do not replace the `B^o(1)` bounded-height input by the bare statement `genus=1`.
- Do not forget the fixed-core exponent `3/7`; the `1/2` is only the residual multiplicative layer.

## PROVENANCE NOTES

Merged PR #395 proves this exact assembly and uses it to close the 4bq residual.