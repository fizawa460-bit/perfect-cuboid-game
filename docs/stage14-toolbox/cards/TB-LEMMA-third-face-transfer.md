# Primitive third-face transfer

```yaml
ID: TB-LEMMA-third-face-transfer
TYPE: LEMMA
STATUS: CURRENT
TITLE: Injective transfer from a physical edge to a third primitive Pythagorean face
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-07
SOURCE_PR: 364
SOURCE_MERGE_SHA: c51992e2373c0f7f265275c211684f6bd5ef9ccf
SOURCE_FILES:
  - stages/stage14/14-s6-07/result.md
```

## INPUT

An actual physical ordered edge with

```text
F1=(S,X,H),
F2=(S2,X2,H2),
g=gcd(S,S2),
G=g*d,
```

as in `TB-FORMULA-physical-two-face-gluing`.

## OUTPUT

Set

```text
c=gcd(H,X2).
```

Then

```text
gcd(H*S2,S*X2)=g*c,
c|d.
```

The primitive reduction

```text
S3=H*S2/(g*c),
X3=S*X2/(g*c),
H3=G/(g*c)=d/c
```

gives

```text
F3=(S3,X3,H3),
S3^2+X3^2=H3^2,
gcd(S3,X3)=1,
H3<=d.
```

The physical edge is recoverable from `(F2,F3)` by

```text
S/H=X3*S2/(S3*X2),
X=sqrt(H^2-S^2),
c=gcd(H,X2),
d=c*H3.
```

Hence the physical-edge to `(F2,F3)` map is injective.

Every physical image also satisfies the exact necessary condition

```text
(S3*X2)^2-(X3*S2)^2 = nonzero integer square.
```

## VARIABLE DICTIONARY

- `c` = cross gcd `gcd(H,X2)`.
- `F3=(S3,X3,H3)` = primitive reduction of `(H*S2,S*X2,G)`.
- `g` and `G` are from `TB-FORMULA-physical-two-face-gluing`.

## USED BY

- s6-07 half-angle gcd matrix;
- s6-08 normalized cross-square receiver;
- 14-4bm physical transferred-pair geometry.

## DO NOT USE FOR

- The square condition on `(F2,F3)` is necessary for the physical image; it is not proved sufficient for an arbitrary pair of primitive faces.
- Do not define `F3` by dividing only by `g`; the additional factor `c=gcd(H,X2)` is part of the primitive reduction.
- Do not infer graph-degree multiplicity: the merged statement is an injection from physical ordered edges to transferred pairs.

## PROVENANCE NOTES

- s6-07 proves the exact gcd scale, `c|d`, primitive reduction, recovery formula, and injectivity.
