# Primitive Euclid face normalization

```yaml
ID: TB-FORMULA-primitive-euclid-face
TYPE: FORMULA
STATUS: CURRENT
TITLE: Primitive Euclid core and oriented Stage14 face
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-07
SOURCE_PR: 364
SOURCE_MERGE_SHA: c51992e2373c0f7f265275c211684f6bd5ef9ccf
SOURCE_FILES:
  - stages/stage14/14-s6-07/result.md
  - stages/stage14/14-s6-01/result.md
```

## INPUT

- integers `m>n>0`;
- `gcd(m,n)=1`;
- `m,n` have opposite parity;
- an explicit orientation choice for which primitive leg is named `S`.

## OUTPUT

Define

```text
E=2mn,
O=m^2-n^2=(m-n)(m+n),
H=m^2+n^2.
```

Then `E^2+O^2=H^2`, and the oriented face is either

```text
(S,X,H)=(E,O,H)
```

or

```text
(S,X,H)=(O,E,H).
```

In the even-S orientation,

```text
S=2mn,
X=(m-n)(m+n),
H=m^2+n^2.
```

## VARIABLE DICTIONARY

- `E` = primitive even leg.
- `O` = primitive odd leg.
- `H` = primitive hypotenuse.
- `(S,X,H)` = oriented Stage14 face after choosing which leg is distinguished as `S`.

See also `TB-DICTIONARY-euclid-five-columns`.

## USED BY

- Stage14 main physical-pair parameterizations.
- Stage14-s local five-column and post-local witness parameterizations.
- Any later toolbox formula requiring explicit orientation.

## DO NOT USE FOR

- Do not write `S=2mn` without first fixing the even-S orientation.
- Do not swap `S` and `X` while keeping half-angle or local-column labels unchanged.
- Do not infer any counting theorem from the parameterization alone.

## PROVENANCE NOTES

- s6-01 uses the even-S presentation to refine squarefree support to the five historical s5 columns.
- s6-07 makes the two possible oriented Euclid cases explicit through the uniform half-angle normalization.
