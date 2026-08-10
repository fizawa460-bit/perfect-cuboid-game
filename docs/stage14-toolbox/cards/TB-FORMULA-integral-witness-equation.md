# Integral global-small-point witness equation

```yaml
ID: TB-FORMULA-integral-witness-equation
TYPE: FORMULA
STATUS: CURRENT
TITLE: Exact integral witness equation and three factor differences
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
```

## INPUT

Primitive witness coordinates `Z=A/D^2`, `W=Y/D^3` on `W^2=Z(Z-S^2)(Z+X^2)`.

## OUTPUT

```text
Y^2=A(A-S^2 D^2)(A+X^2 D^2)
G0=A
G1=A-S^2 D^2
G2=A+X^2 D^2
G0-G1=S^2 D^2
G2-G0=X^2 D^2
G2-G1=H^2 D^2
G0*G1*G2=Y^2
```

For a non-torsion witness, `G0,G1,G2` are all nonzero.

## VARIABLE DICTIONARY

- `G0,G1,G2` are the three exact integral cubic factors.
- `H^2=S^2+X^2`.

## USED BY

- Squarefree-kernel extraction.
- Two-quadrics packetization.
- Pairwise gcd-support calculations.

## DO NOT USE FOR

- A solution of this cleared equation is not by itself a physical cuboid reconstruction.
- A zero `Gi` is a 2-torsion case, not an allowed non-torsion witness.

## PROVENANCE NOTES

Merged PR #345 proves these identities exactly after clearing the rational denominator.