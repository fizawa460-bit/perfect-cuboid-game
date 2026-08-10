# Genus-one model and quantifier boundary

```yaml
ID: TB-WARNING-genus-one-quantifier-and-model-boundary
TYPE: WARNING
STATUS: CURRENT
TITLE: Separate witness two-quadrics, diagonal slope quartics, and moving-family transfer
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bq
SOURCE_PR: 395
SOURCE_MERGE_SHA: aa21a3604cf72e06f797c8ba2ecff96b49e60f44
SOURCE_FILES:
  - stages/stage14/14-s6-02/result.md
  - stages/stage14/14-4bq/result.md
```

## INPUT

Any argument invoking `genus one`, `elliptic`, `bounded height`, or a rational-point bound inside Stage14 main/s.

## OUTPUT

Check the model before importing a theorem.

### Model A: fixed global-witness packet

```text
C_sigma subset P^3,
Q1=Q2=0,
degree 4 complete intersection.
```

This is a fixed packet curve in `(u0,u1,u2,D)`.

### Model B: 4bq diagonal-pair slope quartic

```text
W^2=K*(A^2-B^2*t^4)
```

or the sign-reversed symmetric form. This is a moving reduced-slope curve after fixing the core and the opposite diagonal pair.

They are both genus one but are not interchangeable parameterizations.

A per-fixed-curve point bound yields a moving-family saving only after an explicit transfer mechanism controls how many curves/parameters are being summed and how a rational point recovers the original integer data.

The valid 4bq transfer uses all of:

```text
pairwise coprimality
-> reduced slope uniquely recovers integer pair,
fixed core + fixed opposite diagonal
-> B^o(1) moving-diagonal multiplicity,
UV<=B
-> smaller diagonal <=B^(1/2).
```

## VARIABLE DICTIONARY

- `per-fixed-curve` = parameters defining the curve held fixed.
- `moving-family` = count after summing over base/core/packet parameters.
- `transfer mechanism` = an injective or controlled-multiplicity map that justifies converting point bounds into the target count.

## USED BY

- Screening determinant-method and elliptic-curve black boxes before import.
- Preventing duplicate claims when two routes use different genus-one models.
- Identifying exactly which multiplicity theorem is missing when geometry alone is insufficient.

## DO NOT USE FOR

- `genus one` alone never implies `B^o(1)` points uniformly in a moving family.
- Smoothness does not imply rational solubility.
- Rational 2-torsion on one presentation must not be assumed on another without an explicit birational/Jacobian identification.
- Do not multiply a fixed-curve saving by the old unweighted packet count unless the quantifiers have been aligned.

## PROVENANCE NOTES

Merged PR #348 explicitly records that fixed-packet determinant/genus-one geometry alone does not improve the moving `B^(41/42)` packet count. Merged PR #395 supplies a successful transfer in a different genus-one model through reduced-slope injectivity and smaller-diagonal enumeration.