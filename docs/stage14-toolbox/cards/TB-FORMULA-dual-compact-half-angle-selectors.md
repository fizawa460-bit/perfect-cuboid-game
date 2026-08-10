# Dual compact half-angle selectors

```yaml
ID: TB-FORMULA-dual-compact-half-angle-selectors
TYPE: FORMULA
STATUS: CURRENT
TITLE: Complementary plus/minus compact torsion selectors on the two half-angle columns
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bl
SOURCE_PR: 365
SOURCE_MERGE_SHA: dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
SOURCE_FILES:
  - stages/stage14/14-4bl/result.md
  - stages/stage14/14-s6-06/result.md
```

## INPUT

A physical pair with

```text
H2+S2=kappa*s^2,
H2-S2=kappa*t^2,
X2=kappa*s*t.
```

Use the two compact rational 2-torsion translates of the same physical point.

## OUTPUT

Minus selector `T0=(0,0)`:

```text
N-=H*G-S^2*H2-X^2*S2,
Z_-=-N-/(H2-S2),
D_-|t,
k_-=t/D_-,
gcd(N-,H2-S2)=kappa*k_-^2.
```

Plus selector `T-=(-X^2,0)`:

```text
N+=H*G+X^2*S2-S^2*H2,
Z_+=-N+/(H2+S2),
D_+|s,
k_+=s/D_+,
gcd(N+,H2+S2)=kappa*k_+^2.
```

Both compact points are invertible back to the same physical point.

## VARIABLE DICTIONARY

- `D_-`,`D_+` = reduced square-denominator roots of the two compact translates.
- `k_-`,`k_+` = complementary half-angle cancellation cofactors.
- `s,t` = plus/minus half-angle roots of the partner face.

## USED BY

- Dual denominator/cancellation factorization.
- Complementary odd root-sign routing.
- Physical same-edge incidence receivers.

## DO NOT USE FOR

- Do not treat the two selectors as independent random samples.
- Do not multiply two conditioned density savings solely because both selectors exist.

## PROVENANCE NOTES

Stage14-4bl imports the merged minus selector from s6-06 and independently rederives the plus selector without depending on the then-open 4bk PR.