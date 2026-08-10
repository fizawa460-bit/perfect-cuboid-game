# Conic plus degree-two square lift

```yaml
ID: TB-FORMULA-conic-square-lift
TYPE: FORMULA
STATUS: CURRENT
TITLE: Eliminate one square variable to a smooth conic with four branch points
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-02
SOURCE_PR: 348
SOURCE_MERGE_SHA: 1338ee0170a6d92c26a9dd4fa21c886a8125d6db
SOURCE_FILES:
  - stages/stage14/14-s6-02/result.md
```

## INPUT

The fixed witness system

```text
d0*u0^2-d1*u1^2=S^2*D^2,
d2*u2^2-d0*u0^2=X^2*D^2.
```

## OUTPUT

Adding the equations eliminates `u0` and gives the smooth conic

```text
K_sigma:
d2*u2^2-d1*u1^2=H^2*D^2.
```

The forgotten coordinate is recovered by

```text
d0*u0^2=d1*u1^2+S^2*D^2.
```

Thus

```text
C_sigma -> K_sigma
```

is an exact degree-two square lift. The branch locus is `u0=0`; after scaling `D=1` over the algebraic closure it consists of the four distinct geometric points

```text
u1=+/- S/sqrt(-d1),
u2=+/- X/sqrt(d2).
```

Hence the double cover is branched at four geometric points.

## VARIABLE DICTIONARY

- `K_sigma` = smooth conic obtained by eliminating `u0`.
- branch locus = points where the forgotten square coordinate vanishes.

## USED BY

- Alternative direct genus-one certificate.
- Reducing fixed-packet questions to conic arithmetic plus one square condition.
- Choosing coordinates for anisotropic counting or local analysis.

## DO NOT USE FOR

- The conic alone is a relaxation; the square-lift condition must be retained to recover `C_sigma`.
- Do not assume the four geometric branch points are rational.
- Do not identify this degree-two cover with the separate diagonal-pair quartic parameterization.

## PROVENANCE NOTES

Merged PR #348 proves the elimination and four-branch-point description; merged PR #347 records the same presentation on the main track.