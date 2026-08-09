# Cross-route symbol collision warning

```yaml
ID: TB-WARNING-cross-route-symbol-collisions
TYPE: WARNING
STATUS: CURRENT
TITLE: Do not identify historically reused symbols across main/s normalizations
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-06
SOURCE_PR: 360
SOURCE_MERGE_SHA: 42f4315b0659bd402a94adeb8822588ea153305a
SOURCE_FILES:
  - stages/stage14/14-s6-06/result.md
  - stages/stage14/14-s6-01/result.md
  - stages/stage14/14-4bj/result.md
```

## INPUT

- Any proof step importing formulas between Stage14 main `14-4` and `s`, especially when copying a formula without its original local definitions.

## OUTPUT

Before substitution, resolve these collisions explicitly:

```text
A:
  rational witness numerator in Z=A/D^2
  versus s5 A-column=m

D:
  chosen witness denominator square-root
  versus s5 D-column=m+n
  versus D_min (least bounded-height packet denominator)
  versus D_T (canonical compact physical denominator)

G0,G1,G2:
  denominator-cleared witness factors
  versus G=gcd(S,S2)*d (single physical gluing scale)

U,V:
  positive physical gaps G-HS2 and HH2-G
  versus generic dyadic rectangle side lengths / U_i variables in incidence bounds

d:
  physical integer space diagonal
  versus d0,d1,d2 signed squarefree witness kernels

a,b,c:
  odd edge-kernel divisors in the witness packet
  versus generic physical cuboid-edge letters outside the normalized Stage14 packet notation.
```

No substitution across these meanings is valid unless the receiving proof restates the relevant dictionary.

## VARIABLE DICTIONARY

- Use `TB-DICTIONARY-euclid-five-columns` for the Euclid/support-column layer.
- Use `TB-DICTIONARY-witness-kernel-two-quadrics` for `A,D,G_i,d_i,u_i,a,b,c,tau_i`.
- Use `TB-DICTIONARY-denominator-selectors` for `D,D_min,D_T`.
- Use `TB-DICTIONARY-physical-pair-compact-half-angle` for `g,G,R,Nplus,Nminus,U,V,t,kappa,k`.

## USED BY

- Any future Stage14-toolbox extraction.
- Main/s cross-import reviews.
- Audit scripts that compare formulas from different historical stages.

## DO NOT USE FOR

- This warning is not a theorem and does not forbid local renaming. It requires only that the mapping be explicit before a theorem or bound is imported.
- Matching letter names do not establish matching quantifiers, scales, or objects.

## PROVENANCE NOTES

- The collisions are visible across merged s6-01, 4bj, and s6-06 notation. Toolbox-ab records them as a stable maintenance warning so later routes need not rediscover the ambiguity.
