# StageA1-1 — exact anchored Hilbert-cube dictionary

## Statement

For positive integers `A,B,C`, the following are equivalent.

1. `(A,B,C)` is a perfect cuboid: all three face diagonals and the space diagonal are integers.
2. The Hilbert cube

   `H(0; A^2, B^2, C^2)`

   is contained in the set of integer squares.

Indeed its eight entries are exactly

`0, A^2, B^2, C^2, A^2+B^2, A^2+C^2, B^2+C^2, A^2+B^2+C^2`.

The first four are automatically squares. The remaining four are squares exactly when the three face diagonals and the space diagonal are integral.

Conversely, any dimension-3 Hilbert cube `H(0;a1,a2,a3)` in the squares has `a1,a2,a3` themselves square because `a0=0`; write `ai=A_i^2`. Its remaining subset sums give the three face-diagonal and one space-diagonal square conditions.

Thus the anchored Hilbert-cube problem is not an analogy: it is an exact reparameterization of the perfect-cuboid problem.

## Conventions

- `A,B,C>0`; zero increments are degenerate and excluded.
- Permuting `A,B,C` gives the same cuboid geometry and permutes the Hilbert-cube increments.
- Common scaling `A,B,C -> mA,mB,mC` scales all Hilbert-cube increments by `m^2`. Primitive cuboids therefore correspond to anchored cubes after quotienting common square scale in the obvious way.
- Repeated positive edge lengths are not excluded by the dictionary, though additional elementary constraints may rule them out separately.

## Source connection

Bremner–Elsholtz–Ulas, arXiv:2604.05459 (2026), Question 1.2(2), explicitly asks whether a dimension-3 Hilbert cube in the squares with `a0=0` exists and identifies this as the perfect cuboid/Euler-brick problem.

## Boundary

This equivalence proves no existence or nonexistence statement. Its role is to make `a0=0` the exact geometric boundary that StageA1 studies.

A1_1_STATUS=PROVED_DICTIONARY
PERFECT_CUBOID_CONCLUSION=false
NEXT=A1-2 published-family anchor cuts
