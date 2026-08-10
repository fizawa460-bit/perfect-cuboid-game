# Dual denominator/cancellation product identity

```yaml
ID: TB-FORMULA-dual-denominator-cancellation-product
TYPE: FORMULA
STATUS: CURRENT
TITLE: Exact QK=X2/kappa factorization of the partner leg
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bl
SOURCE_PR: 365
SOURCE_MERGE_SHA: dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
SOURCE_FILES:
  - stages/stage14/14-4bl/result.md
```

## INPUT

The dual compact selectors

```text
D_+ k_+=s,
D_- k_-=t,
H2+S2=kappa*s^2,
H2-S2=kappa*t^2,
X2=kappa*s*t.
```

## OUTPUT

Define

```text
Q:=D_+*D_-,
K:=k_+*k_-.
```

Then exactly

```text
Q*K=s*t=X2/kappa.
```

The cancellation side satisfies

```text
k_+^2 | N+,
k_-^2 | N-,
K^2 | N+*N-.
```

## VARIABLE DICTIONARY

- `Q` = dual compact denominator product.
- `K` = dual square-cancellation product.
- `kappa` = orientation factor in `{1,2}`.

## USED BY

- Splitting physical arithmetic between denominator and cancellation structure.
- Critical-scale and size ledgers.
- Same-edge joint selector arguments.

## DO NOT USE FOR

- `QK=X2/kappa` is an identity, not a density theorem.
- `Q` large does not imply both `D_+` and `D_-` are large.
- `K` large does not by itself give a square-divisor counting saving.
- Historical thresholds derived from the old `41/42` checkpoint must not be promoted to the current whole-family gap without checking the current exponent ledger.

## PROVENANCE NOTES

Merged Stage14-4bl proves this exact dual factorization, including the 2-adic orientation factor.