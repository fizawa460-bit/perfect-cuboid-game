# Fixed-packet two-quadrics witness curve

```yaml
ID: TB-FORMULA-fixed-packet-two-quadrics
TYPE: FORMULA
STATUS: CURRENT
TITLE: Projective two-quadrics model of a fixed global witness packet
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-02
SOURCE_PR: 348
SOURCE_MERGE_SHA: 1338ee0170a6d92c26a9dd4fa21c886a8125d6db
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
  - stages/stage14/14-s6-02/result.md
```

## INPUT

A primitive oriented Pythagorean base

```text
S>0, X>0, H>0,
S^2+X^2=H^2,
```

and one nonzero signed squarefree witness packet `(d0,d1,d2)` produced by the integral witness factorization.

## OUTPUT

In projective coordinates

```text
[u0:u1:u2:D] in P^3
```

define

```text
Q1 = d0*u0^2 - d1*u1^2 - S^2*D^2,
Q2 = d2*u2^2 - d0*u0^2 - X^2*D^2.
```

The fixed-packet witness curve is exactly

```text
C_sigma = {Q1=Q2=0} subset P^3.
```

Adding the equations gives the redundant third difference

```text
d2*u2^2 - d1*u1^2 = H^2*D^2.
```

## VARIABLE DICTIONARY

- `sigma` = fixed signed squarefree packet.
- `d0,d1,d2` = nonzero signed squarefree kernels.
- `u0,u1,u2` = global witness square variables.
- `D` = generic rational-witness denominator from toolbox-af.
- `C_sigma` = projective fixed-packet curve, not the moving base/class family.

## USED BY

- Smoothness/genus-one certification.
- Coordinate-boundary analysis.
- One-variable elimination to a conic plus square lift.
- Any later determinant-method or rational-point input applied per fixed packet.

## DO NOT USE FOR

- Do not identify this curve with the physical diagonal-pair quartics of Stage14-4bq.
- Do not infer a whole-family count merely from a point bound on one `C_sigma`.
- Do not drop the hypothesis that all `d_i,S,X,H` are nonzero.

## PROVENANCE NOTES

Merged PR #348 projectivizes the exact two-quadrics system from merged PR #345. Merged main-track PR #347 independently derives the same fixed-packet geometry.