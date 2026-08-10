# Physical conjugate and gap coordinate

```yaml
ID: TB-FORMULA-physical-conjugate-gap-coordinate
TYPE: FORMULA
STATUS: CURRENT
TITLE: Exact conjugate numerator and physical-gap formulas for the compact point
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-06
SOURCE_PR: 360
SOURCE_MERGE_SHA: 42f4315b0659bd402a94adeb8822588ea153305a
SOURCE_FILES:
  - stages/stage14/14-s6-06/result.md
```

## INPUT

Two primitive oriented physical faces

```text
F1=(S,X,H), F2=(S2,X2,H2),
g=gcd(S,S2), G=g*d.
```

## OUTPUT

Physical gluing:

```text
G^2=S^2*H2^2+X^2*S2^2
   =H^2*S2^2+S^2*X2^2.
```

Set

```text
R-=H2-S2,
Nphys=H*G+S^2*H2+X^2*S2,
N-=H*G-S^2*H2-X^2*S2.
```

Then

```text
Z_P=Nphys/R-,
Nphys*N-=S^2*X^2*(R-)^2,
Z_-=Z(P+(0,0))=-N-/R-.
```

With

```text
U=G-H*S2,
V=H*H2-G,
```

we also have

```text
U,V>0,
U*V=(H2+S2)*N-,
Z_-=-U*V/X2^2.
```

## VARIABLE DICTIONARY

- `G=g*d` = scaled physical space diagonal.
- `Nphys` = original physical numerator.
- `N-` = conjugate/minus compact numerator.
- `U,V` = positive physical gap variables.

## USED BY

- Converting elliptic denominators into exact partner-face arithmetic.
- Prime-by-prime denominator/cancellation analysis.
- Compact square-kernel factorizations.

## DO NOT USE FOR

- `U,V` are physical gaps, not generic dyadic box symbols used elsewhere.
- The identities require an actual physical gluing, not an arbitrary pair of primitive triples.

## PROVENANCE NOTES

Merged Stage14-s6-06 eliminates the earlier s3 auxiliary variables and derives these formulas directly in physical face coordinates.