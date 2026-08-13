# Stage14-toolbox-ad — Pythagorean / Euclid conversion formula atlas

## Purpose

Stage14-toolbox-ad packages the merged Pythagorean geometry used repeatedly by the main `14-4` and `s` routes into one reusable formula atlas.

The stage does not add a new proof theorem. Its goal is to remove repeated rediscovery and prevent orientation/scale mistakes when moving among

```text
Euclid parameters
-> oriented primitive face
-> half-angle roots
-> actual two-face physical gluing
-> third primitive Pythagorean face
-> transferred half-angle cross-square.
```

## Canonical cards added

```text
TB-FORMULA-primitive-euclid-face
TB-FORMULA-half-angle-normalization
TB-FORMULA-physical-two-face-gluing
TB-LEMMA-third-face-transfer
TB-FORMULA-half-angle-cross-square
TB-WARNING-pythagorean-orientation-and-converse
```

## Canonical conversion chain

### Primitive Euclid core

```text
E=2mn,
O=m^2-n^2,
H=m^2+n^2,
```

with explicit orientation

```text
(S,X,H)=(E,O,H) or (O,E,H).
```

### Uniform half-angle coordinates

```text
H-S=kappa*t_-^2,
H+S=kappa*t_+^2,
X=kappa*t_-*t_+,
kappa in {1,2}.
```

Inverse formulas:

```text
S=kappa*(t_+^2-t_-^2)/2,
X=kappa*t_-*t_+,
H=kappa*(t_+^2+t_-^2)/2.
```

### Physical two-face gluing

For

```text
F1=(S,X,H), F2=(S2,X2,H2),
g=gcd(S,S2), G=g*d,
```

the actual physical edges are

```text
S*S2/g,
X*S2/g,
X2*S/g,
```

and

```text
G^2=H^2*S2^2+S^2*X2^2
   =S^2*H2^2+X^2*S2^2.
```

### Primitive third-face transfer

With

```text
c=gcd(H,X2),
```

set

```text
S3=H*S2/(g*c),
X3=S*X2/(g*c),
H3=d/c.
```

Then `F3=(S3,X3,H3)` is primitive and the physical edge is injectively recoverable from `(F2,F3)`.

The transferred pair necessarily satisfies

```text
(S3*X2)^2-(X3*S2)^2=square !=0.
```

### Four-bilinear half-angle form

Let

```text
a=t2-, b=t2+, c=t3-, d=t3+.
```

Then the transferred square becomes

```text
Delta0
=(ad-bc)(ad+bc)(bd-ac)(bd+ac)
=square !=0.
```

## Safety boundary

The atlas freezes the following anti-misuse rules:

```text
ORIENTATION_IS_DATA=true
S_EQUALS_2MN_WITHOUT_ORIENTATION=false
KAPPA_MAY_BE_DROPPED=false
THIRD_FACE_PRIMITIVE_SCALE_IS_G_TIMES_C=true
F2_F3_SQUARE_CONDITION_SUFFICIENT_FOR_PHYSICALITY=false
HALF_ANGLE_DELTA_SQUARE_CONVERSE_PHYSICALITY=false
GOOD_GCD_FACTOR_AUTOMATIC_SQUARE_MAY_BE_RECOUNTED_AS_INDEPENDENT_SAVING=false
```

## Provenance

Canonical sources are merged only:

```text
Stage14-s6-01  PR #345  86b91ffcd8bae79452ef75f187c8570a3819d386
Stage14-s6-06  PR #360  42f4315b0659bd402a94adeb8822588ea153305a
Stage14-s6-07  PR #364  c51992e2373c0f7f265275c211684f6bd5ef9ccf
Stage14-s6-08  PR #369  e9916a9e21dc305fa30e240d3db962a26af1653b
```

No open PR is used as canonical provenance.

## Boundary

```text
STAGE14_TOOLBOX_AD=COMPLETE_PYTHAGOREAN_EUCLID_CONVERSION_FORMULA_ATLAS
CANONICAL_NEW_CARD_COUNT=6
PRIMITIVE_EUCLID_ORIENTATION_FORMULA_FROZEN=true
UNIFORM_HALF_ANGLE_NORMALIZATION_FROZEN=true
PHYSICAL_TWO_FACE_GLUING_FORMULAS_FROZEN=true
THIRD_PRIMITIVE_FACE_TRANSFER_FROZEN=true
HALF_ANGLE_CROSS_SQUARE_FACTORIZATION_FROZEN=true
PYTHAGOREAN_CONVERSE_AND_ORIENTATION_WARNING_FROZEN=true
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-ae local 2-descent and five-column interface
```
