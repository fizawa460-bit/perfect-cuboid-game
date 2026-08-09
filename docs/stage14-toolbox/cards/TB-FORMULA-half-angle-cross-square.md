# Half-angle cross-square factorization

```yaml
ID: TB-FORMULA-half-angle-cross-square
TYPE: FORMULA
STATUS: CURRENT
TITLE: Four-bilinear factorization of the transferred physical square condition
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-08
SOURCE_PR: 369
SOURCE_MERGE_SHA: e9916a9e21dc305fa30e240d3db962a26af1653b
SOURCE_FILES:
  - stages/stage14/14-s6-08/result.md
```

## INPUT

A transferred physical pair `(F2,F3)` from `TB-LEMMA-third-face-transfer`.

Write its half-angle coordinates as

```text
a=t_-(F2),
b=t_+(F2),
c=t_-(F3),
d=t_+(F3).
```

## OUTPUT

With the two orientation factors `kappa2,kappa3`,

```text
S2=kappa2*(b^2-a^2)/2,
X2=kappa2*a*b,
S3=kappa3*(d^2-c^2)/2,
X3=kappa3*c*d.
```

Define

```text
A0=a*b*(d^2-c^2),
C0=c*d*(b^2-a^2).
```

Then exactly

```text
A0-C0=(a*d-b*c)*(b*d+a*c),
A0+C0=(a*d+b*c)*(b*d-a*c),
```

and therefore

```text
Delta0=A0^2-C0^2
      =(a*d-b*c)(a*d+b*c)(b*d-a*c)(b*d+a*c).
```

For every transferred physical image,

```text
Delta0 = nonzero integer square.
```

The original geometric square satisfies

```text
(S3*X2)^2-(X3*S2)^2
=(kappa2*kappa3/2)^2*Delta0.
```

## VARIABLE DICTIONARY

- `a,b` = minus/plus half-angle parameters of `F2`.
- `c,d` = minus/plus half-angle parameters of `F3`.
- `A0,C0` = unscaled cross products used only in this factorization.
- `Delta0` = normalized four-bilinear square detector.

Outside this local display, prefer `t2-`, `t2+`, `t3-`, `t3+` to avoid collisions with other Stage14 uses of `a,b,c,d`.

## USED BY

- s6-08 good-gcd square extraction and normalized kernel collision;
- 14-4bm transferred half-angle geometry;
- future same-modulus or squareclass incidence work.

## DO NOT USE FOR

- `Delta0=square` is guaranteed on the transferred physical image; no converse for arbitrary quadruples is proved.
- Do not claim that a large gcd cell creates an independent `1/q` square-density saving; s6-08 proves the complete good gcd matrix is already an automatic square factor.
- Do not tensorize the two difference-of-squares factors independently without preserving their shared physical coupling.

## PROVENANCE NOTES

- s6-08 derives the exact four-bilinear factorization and then removes the automatic gcd-matrix square factor.
