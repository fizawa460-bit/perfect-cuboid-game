# Physical two-face gluing formulas

```yaml
ID: TB-FORMULA-physical-two-face-gluing
TYPE: FORMULA
STATUS: CURRENT
TITLE: Primitive two-face gluing to actual cuboid edges and third integral triple
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-06
SOURCE_PR: 360
SOURCE_MERGE_SHA: 42f4315b0659bd402a94adeb8822588ea153305a
SOURCE_FILES:
  - stages/stage14/14-s6-06/result.md
```

## INPUT

Two primitive oriented Pythagorean faces

```text
F1=(S,X,H),
F2=(S2,X2,H2)
```

that come from an actual Stage14 physical cuboid edge with integer space diagonal `d`.

Set

```text
g=gcd(S,S2).
```

## OUTPUT

The scale factors from primitive faces to the actual cuboid are

```text
r1=S2/g,
r2=S/g.
```

The actual cuboid edges are

```text
shared=S*S2/g,
other1=X*S2/g,
other2=X2*S/g.
```

The corresponding face diagonals are

```text
diag1=H*S2/g,
diag2=H2*S/g.
```

With

```text
G=g*d,
```

the exact gluing identities are

```text
G^2=H^2*S2^2+S^2*X2^2
   =S^2*H2^2+X^2*S2^2,
```

so in particular

```text
(H*S2)^2+(S*X2)^2=G^2.
```

## VARIABLE DICTIONARY

- `g` = `gcd(S,S2)`, the primitive shared-leg scale reducer.
- `r1,r2` = primitive-face scale factors into the physical cuboid.
- `d` = physical integer space diagonal.
- `G=g*d` = scaled hypotenuse of the induced third integral Pythagorean triple.

## USED BY

- s6-06 physical compact denominator formulas;
- s6-07 primitive third-face transfer;
- main-route physical reparameterizations after 4bj.

## DO NOT USE FOR

- Do not apply the formulas to an arbitrary pair of primitive Pythagorean faces unless physical gluing is already known.
- Do not confuse `G=g*d` with witness factors `G0,G1,G2` from the integral small-point model.
- Do not omit the factor `g` when converting primitive face coordinates to actual cuboid edges.

## PROVENANCE NOTES

- This is the exact physical gluing normalization frozen in merged s6-06.
- s6-07 subsequently primitive-reduces the induced integral triple to `F3`.
