# Stage14-s5c — supported-prime local Hilbert rows

## Purpose

Stage14-s5b reduced the odd descent support to the five Euclid factors

```text
m, n, m-n, m+n, m^2+n^2
```

and the three nontrivial support labels

```text
12=(1,1,0), 13=(1,0,1), 23=(0,1,1).
```

Stage14-s5c now derives the exact local row forced at an **odd bad prime which is actually selected in the descent support**.  It deliberately does not identify this supported-prime row with the full bad-prime local condition: a bad prime omitted from all `d_i` has a different, disjunctive local problem and remains for the next stage.

## Symmetric covering coordinates

From s1 write

```text
z1 = d1*u1^2
z2 = d2*u2^2
z3 = d3*u3^2.
```

Then the two covering equations and the Pythagorean identity are exactly

```text
z1-z2 = S^2
z3-z1 = X^2
z3-z2 = H^2.
```

For a primitive opposite-parity Euclid pair, every odd bad prime divides exactly one of `S,X,H`:

```text
p | m or n             => p | X
p | m-n or m+n         => p | S
p | m^2+n^2            => p | H.
```

The five-factor odd pairwise-coprimality from s5b makes these alternatives exclusive.

## Valuation-parity routing of a supported prime

Suppose an odd bad prime `p` occurs in the squarefree support of the covering class.  Since `d1*d2*d3` is a square class, its valuation vector is one of `12,13,23`.

The p-divisible difference above forces the two odd-valuation coordinates to be exactly the endpoints of that difference.  Otherwise one of the other two differences has unit right hand side but its two terms have incompatible valuation parity.

Hence the support label is forced:

```text
p | S  => label 12
p | X  => label 13
p | H  => label 23.
```

Equivalently, in Euclid-factor columns,

```text
m, n                 -> 13
m-n, m+n             -> 12
m^2+n^2              -> 23.
```

This removes the apparent `3^omega` label freedom for supported odd primes: the geometric factor column already determines the label.

## Exact supported-prime residue rows

Write locally

```text
di = p^ei * ai,
```

where each `ai` is a p-adic unit and `(e1,e2,e3)` is the forced label.  Quadratic characters below are Legendre symbols on unit parts; inverse and product are identical in `F_p^*/F_p^{*2}`.

### S-prime row: label 12

For `p|S`, `p∤XH`, and label `12`, local solubility of the supported-prime normal form is equivalent to

```text
(a1*a2 | p) = +1
(a3    | p) = +1.
```

The first condition is the cancellation condition in

```text
p*a1*u1^2 - p*a2*u2^2 = S^2,
```

and the second comes from `z3=z1+X^2`, whose unit residue is the square `X^2` after the p-divisible supported terms are normalized.  Hensel lifting applies once the residue-square conditions hold.

### X-prime row: label 13

For `p|X`, `p∤SH`, and label `13`, the exact supported-prime row is

```text
(a1*a3 | p) = +1
(-a2   | p) = +1.
```

The first condition is cancellation in `z3-z1=X^2`; the second follows from

```text
z2=z1-S^2 == -S^2 (mod p)
```

at the supported integral normalization.

### H-prime row: label 23

For `p|H`, `p∤SX`, and label `23`, the exact supported-prime row is

```text
(a2*a3 | p) = +1
(a1    | p) = +1.
```

Here cancellation occurs in `z3-z2=H^2`, while

```text
z1=z2+S^2 == S^2 (mod p).
```

## Character-matrix form

The three supported-prime rows can therefore be written uniformly as two linear equations over `F2` in quadratic-character bits:

```text
S / 12 : chi_p(a1)+chi_p(a2)=0,  chi_p(a3)=0
X / 13 : chi_p(a1)+chi_p(a3)=0,  chi_p(-1)+chi_p(a2)=0
H / 23 : chi_p(a2)+chi_p(a3)=0,  chi_p(a1)=0.
```

Each `ai` is the p-unit part of a product of squarefree pieces drawn from the *other* factor columns.  Thus these equations are explicit linear functionals of the s5b reciprocity/Jacobi matrix, plus the mod-4 sign bit in the X-row.

This is the first genuinely large-sieve-ready local subsystem in the s-track.

## The prime 2

Because `S,H` are odd and `X=2mn` has `v2(X)>=2`, valuation parity eliminates supported labels `12` and `23` at `2`.  If the class uses the prime `2`, its only possible valuation label is

```text
13=(1,0,1).
```

Write then

```text
d1=2*a1, d2=a2, d3=2*a3,
```

with odd `ai`.  The second covering equation forces the odd-unit ratio `a3/a1` to lie in the 2-adic square class `1 mod 8` in the unit-unit branch.  The first equation splits according to the parity of the normalized `u1`; modulo 8 the visible branches are

```text
u1 odd  : a2 == 2*a1-1 (mod 8)
u1 even : a2 == -1       (mod 8).
```

These congruences are **necessary branch conditions**, not yet promoted to a complete Q2 local-solubility table.  In particular the `2`-unselected class and higher-valuation branch bookkeeping remain to be exhaustively closed.

## Why s5c stops here

The supported-prime rows above are exact and already convert a large subset of the Selmer local constraints into quadratic-character equations across the five Euclid factors.

Two pieces are still required before a family large sieve can be stated as a theorem:

1. the local rows at odd bad primes which are *not* selected in `d1,d2,d3`;
2. the complete Q2 squareclass lookup, including the 2-unselected state.

Treating either as automatic would overcount/undercount the Selmer image.

## Boundary

```text
STAGE14_S5C=COMPLETE_SUPPORTED_PRIME_LOCAL_HILBERT_ROWS
ODD_SUPPORTED_FACTOR_TO_LABEL_ROUTING_DERIVED=true
ODD_SUPPORTED_S_ROW=chi(a1*a2)=+1_and_chi(a3)=+1
ODD_SUPPORTED_X_ROW=chi(a1*a3)=+1_and_chi(-a2)=+1
ODD_SUPPORTED_H_ROW=chi(a2*a3)=+1_and_chi(a1)=+1
SUPPORTED_ODD_ROWS_LINEAR_IN_RECIPROCITY_BITS=true
P2_SUPPORTED_LABEL_FORCED_TO_13=true
P2_NECESSARY_MOD8_BRANCHES_DERIVED=true
ODD_UNSELECTED_BAD_PRIME_ROWS_DERIVED=false
P2_COMPLETE_LOCAL_MATRIX_DERIVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5d close unselected odd bad-prime rows and exhaustive Q2 squareclass table
```
