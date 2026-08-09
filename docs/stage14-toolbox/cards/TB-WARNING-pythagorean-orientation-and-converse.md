# Pythagorean orientation and converse warnings

```yaml
ID: TB-WARNING-pythagorean-orientation-and-converse
TYPE: WARNING
STATUS: CURRENT
TITLE: Do not erase orientation, primitive scales, or one-way physical-image hypotheses
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-08
SOURCE_PR: 369
SOURCE_MERGE_SHA: e9916a9e21dc305fa30e240d3db962a26af1653b
SOURCE_FILES:
  - stages/stage14/14-s6-07/result.md
  - stages/stage14/14-s6-08/result.md
```

## INPUT

Any use of the primitive Euclid, half-angle, physical gluing, third-face, or transferred cross-square formulas collected in Stage14-toolbox-ad.

## OUTPUT

Before reusing a formula, preserve these distinctions:

```text
1. unordered Euclid legs E/O != oriented Stage14 labels S/X;
2. kappa=1/2 belongs to the chosen orientation;
3. primitive physical gluing uses g=gcd(S,S2);
4. primitive third-face reduction uses g*c with c=gcd(H,X2);
5. physical edge -> (F2,F3) is injective, not an asserted bijection onto all primitive pairs;
6. (S3*X2)^2-(X3*S2)^2=square is necessary on the physical image;
7. Delta0=square is the half-angle reformulation on that image, not a converse physicality theorem.
```

## VARIABLE DICTIONARY

- `E,O` = even/odd primitive Euclid legs.
- `S,X` = oriented Stage14 leg labels.
- `g` = `gcd(S,S2)`.
- `c` = `gcd(H,X2)` used in third-face primitive reduction.
- `Delta0` = four-bilinear normalized cross-square detector.

## USED BY

- all main/s stages that copy Pythagorean conversion formulas;
- toolbox formula extraction and audits;
- future proof recipes using transferred primitive faces.

## DO NOT USE FOR

Forbidden shortcuts include:

- `S=2mn` without orientation declaration;
- dropping `kappa` as if both orientations had identical 2-adic normalization;
- replacing `F3=primitive(H*S2,S*X2,G)` by division only by `g`;
- treating the transferred square condition as sufficient for physicality;
- treating the four bilinear factors as independent after physical constraints are imposed;
- treating a good gcd factor already squared inside `Delta0` as a new independent square-sieve saving.

## PROVENANCE NOTES

- s6-07 explicitly states the transfer-square condition only as a necessary condition on the physical image.
- s6-08 shows that the good gcd matrix contributes an automatic square prefactor, motivating the no-independent-density warning.
