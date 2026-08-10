# Rational witness square/cube denominator

```yaml
ID: TB-FORMULA-rational-witness-denominator
TYPE: FORMULA
STATUS: CURRENT
TITLE: Square/cube denominator shape for a rational Stage14 witness
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
```

## INPUT

A rational point `(Z,W)` on `W^2=Z(Z-S^2)(Z+X^2)`.

## OUTPUT

```text
Z=A/D^2
W=Y/D^3
D>0
gcd(A,D)=1
```

For every prime in the reduced denominator of `Z`, the three monic cubic factors have equal negative valuation. Since their product is a square, the denominator exponent is even; the corresponding exponent in `W` is a multiple of three.

## VARIABLE DICTIONARY

- `A,D,Y` are primitive integral witness coordinates.
- `D` is the generic rational-coordinate denominator selector, not the later compact physical `D_T`.

## USED BY

- Clearing rational small-point coordinates to an exact integer equation.
- Global witness packetization in main/s.

## DO NOT USE FOR

- Do not identify `D` with `D_min` or `D_T`.
- This denominator shape alone gives no power saving.

## PROVENANCE NOTES

Merged PR #345 proves the square/cube denominator shape directly from valuations of the monic cubic.