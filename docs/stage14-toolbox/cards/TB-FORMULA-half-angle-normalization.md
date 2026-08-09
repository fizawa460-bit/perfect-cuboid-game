# Uniform half-angle normalization

```yaml
ID: TB-FORMULA-half-angle-normalization
TYPE: FORMULA
STATUS: CURRENT
TITLE: Uniform primitive half-angle coordinates for either orientation
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-07
SOURCE_PR: 364
SOURCE_MERGE_SHA: c51992e2373c0f7f265275c211684f6bd5ef9ccf
SOURCE_FILES:
  - stages/stage14/14-s6-07/result.md
  - stages/stage14/14-s6-08/result.md
```

## INPUT

A primitive oriented Pythagorean face

```text
F=(S,X,H),
S^2+X^2=H^2.
```

## OUTPUT

There are orientation-normalized values

```text
kappa in {1,2},
t_->0,
t_+>0
```

with

```text
H-S=kappa*t_-^2,
H+S=kappa*t_+^2,
X=kappa*t_-*t_+.
```

Equivalently,

```text
S=kappa*(t_+^2-t_-^2)/2,
X=kappa*t_-*t_+,
H=kappa*(t_+^2+t_-^2)/2.
```

For Euclid parameters `m>n`:

```text
S=2mn:
  kappa=1,
  t_-=m-n,
  t_+=m+n;

S=m^2-n^2:
  kappa=2,
  t_-=n,
  t_+=m.
```

At odd primes, `t_-` and `t_+` have disjoint support.

## VARIABLE DICTIONARY

- `kappa` = finite orientation/2-adic factor.
- `t_-` = square-root parameter for `H-S`.
- `t_+` = square-root parameter for `H+S`.

## USED BY

- compact denominator selectors;
- third-face half-angle gcd matrix;
- s6-08 four-bilinear cross-square factorization;
- 14-4bl dual half-angle product formulas.

## DO NOT USE FOR

- Do not drop `kappa` when changing orientation.
- Do not identify `t_-` with `m-n` in the odd-S orientation; there `t_-=n`.
- Odd-prime disjointness does not authorize an independent Bernoulli/root-sign probability model.

## PROVENANCE NOTES

- s6-07 gives the uniform orientation definition and explicit Euclid cases.
- s6-08 reuses the same normalization for the transferred pair `(F2,F3)`.
