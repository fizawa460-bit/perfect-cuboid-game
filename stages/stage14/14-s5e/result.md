# Stage14-s5e — exact Q2 Hilbert table and lifting boundary

## Purpose

Stage14-s5d closed every odd bad-prime row and reduced the remaining 2-adic problem to the 64 ordered squareclass triples `(d1,d2,d3)` with square product. Stage14-s5e now makes the 2-adic squareclass algebra exact instead of relying on finite-depth residue survival.

## Exact Q2 squareclass coordinates

Every nonzero 2-adic squareclass has a unique representative

```text
2^a * u,   a in {0,1},   u in {1,3,5,7} mod 8.
```

Hence

```text
Q2*/Q2*^2 ~= (Z/2)^3
```

with eight classes. For

```text
A = 2^alpha u,
B = 2^beta  v
```

with odd `u,v`, define

```text
epsilon(u) = (u-1)/2 mod 2
omega(u)   = (u^2-1)/8 mod 2.
```

The exact 2-adic Hilbert symbol is

```text
(A,B)_2 = (-1)^[ epsilon(u)epsilon(v) + alpha*omega(v) + beta*omega(u) ].
```

This gives the complete bilinear pairing table on the eight Q2 squareclasses. No modulus-search heuristic is used in this step.

## Product-square descent states

The full-2-descent constraint requires

```text
d1*d2*d3 in Q2*^2.
```

After choosing the first two squareclasses, the third is forced. Therefore the 2-adic descent state space has exactly

```text
8^2 = 64
```

ordered states. Each state is represented by six F2 bits and every pairwise Hilbert symbol among `d1,d2,d3`, `-1`, and `2` is an explicit bilinear form in those bits.

This is the exact finite algebra needed to encode the prime-2 place in the same Boolean language as the odd reciprocity rows from s5b-s5d.

## Relation to the Stage14 covering

Using the normalized covering variables from s5c/s5d,

```text
z1-z2 = 1
z3-z1 = t^2
z3-z2 = 1+t^2
v2(t) >= 2,
```

with `zi = di ui^2`, the prime-2 local-solubility question is now a finite problem over the 64 squareclass states plus the valuation branch of the `ui`.

The exact Hilbert table removes one ambiguity left by s5d: two states which agree only modulo a finite power of 2 but differ as Q2 squareclasses can no longer be conflated.

## Hensel boundary

For a residue solution of the two covering equations, if the Jacobian has a 2-adically invertible 2x2 minor after the chosen normalization, multivariate Hensel lifting gives a genuine Q2 solution. These nonsingular branches are therefore certifiable at finite depth.

The remaining singular residue branches require explicit valuation descent / rescaling. Stage14-s5e does **not** identify mere survival modulo `2^N` with Q2 solubility. A complete covering-specific partition of the 64 states remains the next task.

## What is closed

```text
STAGE14_S5E=COMPLETE_Q2_HILBERT_PAIRING_AND_64_STATE_ENCODING
Q2_SQUARECLASS_GROUP_SIZE=8
Q2_PRODUCT_SQUARE_DESCENT_STATE_COUNT=64
Q2_HILBERT_SYMBOL_FORMULA_LOCKED=true
Q2_PAIRING_TABLE_EXACT=true
Q2_STATES_ENCODED_AS_F2_BITS=true
NONSINGULAR_HENSEL_BRANCH_CRITERION_LOCKED=true
P2_COVERING_SPECIFIC_64_STATE_SOLUBILITY_CLASSIFIED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5f classify the 64 Q2 covering states, using exact Hilbert bits plus valuation descent for singular branches
```

## Interpretation

The important advance is that the prime-2 obstruction is no longer an open-ended p-adic search problem. It is a finite, exact 64-state covering problem over a known bilinear Hilbert pairing. Once s5f classifies those states, the entire local 2-descent system will be available as a finite Boolean/character constraint system for the family-level large-sieve step.
