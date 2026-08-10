# Exact Q2 Hilbert-symbol formula

```yaml
ID: TB-FORMULA-q2-hilbert-symbol
TYPE: FORMULA
STATUS: CURRENT
TITLE: Exact Q2 squareclass coordinates and Hilbert pairing
SCOPE: BOTH
SOURCE_STAGE: Stage14-s5e
SOURCE_PR: 224
SOURCE_MERGE_SHA: ae9cf81bf049c52fb6274ae111bcb1bbdc87e910
SOURCE_FILES:
  - stages/stage14/14-s5e/result.md
```

## INPUT

Two nonzero 2-adic squareclasses written as

```text
A=2^alpha*u
B=2^beta*v
```

with `alpha,beta in {0,1}` and odd `u,v` represented modulo 8.

## OUTPUT

Define

```text
epsilon(u)=(u-1)/2 mod 2
omega(u)=(u^2-1)/8 mod 2.
```

Then

```text
(A,B)_2
 = (-1)^[epsilon(u)epsilon(v)+alpha*omega(v)+beta*omega(u)].
```

The squareclass group has representatives

```text
1,3,5,7,2,6,10,14
```

and is isomorphic to `(Z/2)^3`.

## VARIABLE DICTIONARY

- `alpha,beta` = parity of the 2-adic valuation.
- `u,v` = odd unit representatives modulo 8.
- `epsilon,omega` = the two standard F2 unit invariants appearing in the Q2 Hilbert pairing.

## USED BY

- Exact encoding of the 64 product-square Q2 descent states.
- Replacing finite-depth residue survival heuristics by exact squareclass algebra.
- Regression checks for the eight-state covering image.

## DO NOT USE FOR

- The Hilbert pairing table alone does not classify the Stage14 covering image; the covering-specific eight-state theorem is separate.
- Do not infer Q2 solubility from survival modulo one fixed `2^N`.

## PROVENANCE NOTES

- Merged PR #224 proves the exact pairing formula and 64-state algebra; PR #229 supplies the later covering-specific classification.
