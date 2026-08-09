# Stage14-s5f — exact Q2 covering-state classification

## Purpose

Stage14-s5e fixed the exact eight-element squareclass group `Q2*/Q2*^2` and the 64 ordered product-square descent states. Stage14-s5f now classifies which of those 64 states actually occur in the Stage14 local Kummer image.

For a primitive Pythagorean first face, after dividing by the odd square `S^2`, write

```text
t = X/S,
q = Z/S^2.
```

Since `S` is odd and `v2(X)>=2`,

```text
v2(t)>=2,
v2(t^2)>=4.
```

The local Kummer triple is

```text
[q], [q-1], [q+t^2]
```

in `Q2*/Q2*^2`, with product square exactly when the corresponding elliptic point exists.

## Exact classification

Represent the eight squareclasses by

```text
1, 3, 5, 7, 2, 6, 10, 14,
```

where the odd part is reduced modulo 8 and the power of 2 is reduced modulo parity.

For every `t in Q2` with `v2(t)>=2`, the Stage14 local Kummer image consists of exactly the following eight ordered states:

```text
(1,  1,  1)
(3,  7,  5)
(5,  1,  5)
(7,  7,  1)
(2,  1,  2)
(6,  7, 10)
(10, 1, 10)
(14, 7,  2)
```

Thus only 8 of the 64 product-square states survive the covering-specific Q2 condition.

Equivalently, the middle coordinate is always `1` or `7`; the first and third coordinates are then determined by the two squareclass bits carried by the valuation parity and odd unit of `q`.

## Why the classification is finite and exact

The proof uses the elementary Q2 square criterion:

```text
x is a square in Q2
iff v2(x) is even and the odd unit of x is 1 mod 8.
```

Because `v2(t^2)>=4`, the squareclasses of `q`, `q-1`, and `q+t^2` are constant on finitely many 2-adic residue cylinders. Outside the finite critical valuation bands around `q=0`, `q=1`, and `q=-t^2`, the ratios between the relevant terms lie in `1+8 Z2` and are therefore squares. The remaining critical cylinders are resolved by the odd unit modulo 8 and valuation parity.

The deterministic audit implements this cylinder decomposition rather than treating survival modulo a fixed `2^N` as a proof. It also independently enumerates deep residue representatives for `v2(t^2)=4,6,8,10` and obtains the same eight states.

## Consequence for the s5 local system

Together with s5c/s5d, every place is now explicit:

- all odd bad-prime rows are Boolean/linear conditions in reciprocity bits;
- the prime-2 condition is membership in the fixed eight-state table above;
- good odd primes are unramified and contribute no moving local obstruction.

Hence the Stage14 full local 2-descent admissibility condition is a finite character system over the five moving Euclid factors

```text
m, n, m-n, m+n, m^2+n^2.
```

What remains is no longer local algebra. It is the analytic problem of averaging this moving character system over primitive opposite-parity Euclid pairs, while retaining the physical small-point window from s3.

## Boundary

```text
STAGE14_S5F=COMPLETE_FULL_LOCAL_CHARACTER_SYSTEM
Q2_PRODUCT_SQUARE_STATE_COUNT=64
Q2_COVERING_SOLUBLE_STATE_COUNT=8
Q2_COVERING_SPECIFIC_64_STATE_SOLUBILITY_CLASSIFIED=true
ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true
FULL_LOCAL_2_DESCENT_CHARACTER_SYSTEM_COMPLETE=true
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5g formulate and test the first global character-sum / large-sieve inequality
```
