# Coordinate and torsion boundary is finite

```yaml
ID: TB-LEMMA-coordinate-boundary-finite
TYPE: LEMMA
STATUS: CURRENT
TITLE: Coordinate/torsion hyperplane boundary has no positive-dimensional component
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-02
SOURCE_PR: 348
SOURCE_MERGE_SHA: 1338ee0170a6d92c26a9dd4fa21c886a8125d6db
SOURCE_FILES:
  - stages/stage14/14-s6-02/result.md
```

## INPUT

The smooth degree-four fixed witness curve `C_sigma` in projective coordinates `[u0:u1:u2:D]`.

## OUTPUT

Each coordinate hyperplane

```text
u0=0,
u1=0,
u2=0,
D=0
```

meets `C_sigma` in a zero-dimensional scheme. In particular

```text
POSITIVE_DIMENSIONAL_TORSION_BOUNDARY_COMPONENT=false.
```

For example, `u0=0` gives

```text
-d1*u1^2=S^2*D^2,
d2*u2^2=X^2*D^2,
```

and over the algebraic closure `D!=0`; after scaling `D=1`, only finitely many sign choices remain. Likewise `D=0` gives

```text
d0*u0^2=d1*u1^2=d2*u2^2,
```

again finitely many projective points.

## VARIABLE DICTIONARY

- `ui=0` = coordinate boundaries corresponding to zero square factors, hence torsion-type boundary in the integral witness construction.
- `D=0` = projective infinity boundary of the denominator-cleared model.

## USED BY

- Removing coordinate/torsion boundary from accumulating-component obstruction lists.
- Justifying use of smooth irreducible curve tools without a hidden line/conic boundary component.

## DO NOT USE FOR

- Finite boundary does not mean boundary points are absent.
- Do not identify every boundary point with a physical torsion point; the statement is geometric finiteness of the relaxation boundary.
- Do not infer any quantitative moving-family saving from finiteness alone.

## PROVENANCE NOTES

Merged PR #348 proves the hyperplane sections are finite; merged PR #347 records the same main-track boundary conclusion.