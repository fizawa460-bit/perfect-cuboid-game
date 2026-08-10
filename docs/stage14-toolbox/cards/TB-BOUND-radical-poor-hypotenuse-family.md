# Radical-poor hypotenuse family bound

```yaml
ID: TB-BOUND-radical-poor-hypotenuse-family
TYPE: BOUND
STATUS: CURRENT
TITLE: Supported radical-poor hypotenuse base/classes are B^(rho+epsilon)-sparse
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bi-S
SOURCE_PR: 352
SOURCE_MERGE_SHA: a40878e2efdf17b2f151a9cf15849c001908c3a4
SOURCE_FILES:
  - stages/stage14/14-4bi-S/result.md
```

## INPUT

A threshold `rho>0`, `H<=B`, and

```text
R_H=rad_odd(H) <= B^rho.
```

## OUTPUT

Merged 4bi-S gives

```text
#{n<=B : rad(n)<=B^rho} << B^(rho+epsilon)
```

and after primitive Pythagorean representation multiplicity and closed packet multiplicity,

```text
#{supported base/classes : H<=B, R_H<=B^rho}
 << B^(rho+epsilon).
```

At the critical choice

```text
rho=1/2,
```

the radical-poor hypotenuse sector is already controlled at square-root scale.

## VARIABLE DICTIONARY

- `R_H` = odd radical of the primitive Pythagorean hypotenuse.
- `rho` = radical-size threshold exponent.

## USED BY

- Separating a globally sparse base/class family before coordinate incidence estimates.
- Main-track radical-rich/radical-poor partitioning.

## DO NOT USE FOR

- This is a base/class count, unlike the full-radical rectangle bounds; do not conflate the two quantifiers.
- Do not replace `rad(H)` by a selected kernel `c`.
- Do not infer an asymptotic or exact density from the upper bound.

## PROVENANCE NOTES

Merged PR #352 proves the Rankin-type radical-poor integer bound and transfers it to supported primitive Pythagorean base/classes.