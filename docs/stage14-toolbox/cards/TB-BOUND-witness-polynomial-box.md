# Polynomial box for logarithmically small global witnesses

```yaml
ID: TB-BOUND-witness-polynomial-box
TYPE: BOUND
STATUS: CURRENT
TITLE: Polynomial coordinate box from the logarithmic canonical-height window
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
```

## INPUT

A Stage14 global witness `Q` with `H<=B` and

```text
hat_h(Q) <= C(log B + log H).
```

## OUTPUT

For a fixed constant `K_C`, the merged fixed-degree height comparison gives

```text
H_Z(Q) <= B^K_C
|A| <= B^K_C
D^2 <= B^K_C.
```

The integral factors `G0,G1,G2`, `Y`, and variables obtained from their square/squarefree decomposition are therefore confined to a fixed polynomial box. Standard finite-dimensional dyadic decomposition costs `B^epsilon`.

## VARIABLE DICTIONARY

- `K_C` depends only on the fixed admissible height constant/family, not on the individual witness.
- `H_Z` is the naive multiplicative height of the rational `Z` coordinate.

## USED BY

- Dyadic decomposition of witness variables.
- Geometry-of-numbers, square-sieve, and incidence arguments after integerization.

## DO NOT USE FOR

- A polynomial box is not a positive-power counting saving.
- Do not replace an existence count by a coordinate-density count without a multiplicity/quantifier transfer.

## PROVENANCE NOTES

Merged PR #345 imports the already-merged Stage14-s3 canonical/naive height comparison and records `POLYNOMIAL_WITNESS_BOX_PROVED=true`.