# Optimized local descent bound at s5t

```yaml
ID: TB-BOUND-local-descent-s5t
TYPE: BOUND
STATUS: SUPERSEDED
TITLE: Reoptimized s5 local-descent saving 1/41 on Euclid scale
SCOPE: BOTH
SOURCE_STAGE: Stage14-s5t
SOURCE_PR: 333
SOURCE_MERGE_SHA: 9f9e74f22e80fb8432e865f3eebee8cd7c842fff
SOURCE_FILES:
  - stages/stage14/14-s5t/result.md
SUPERSEDED_BY: TB-BOUND-local-descent-current
EXPONENT_SCALE: M and physical B
SAVING_EXACT: 1/41 on M-scale
CONVERSION: M<=sqrt(B)
```

## INPUT

- The same actual s5 locally-soluble system as the s5s card.
- Three-case graph-escape architecture with optimized thresholds `sigma=2/41`, `lambda=5/41`.
- Physical conversion `M<=sqrt(B)`.

## OUTPUT

```text
N_local(M) << M^(2-1/41+epsilon)
#Q_B^phys << B^(81/82+epsilon)
```

The physical saving relative to exponent `1` is `1/82`.

## VARIABLE DICTIONARY

- `sigma` = long threshold exponent.
- `lambda` = very-long threshold exponent.
- `M`, `B` as in the current toolbox variable dictionary.

## USED BY

- Historical local-saving chain.
- Main-track Stage14-4bf import and refocus decision.

## DO NOT USE FOR

- Do not treat `1/41` as current; s5u improved the same local problem to `1/21`.
- Do not treat the `1/41` optimization as an arithmetic resonance theorem; it is optimization inside the then-current case architecture.

## PROVENANCE NOTES

Stage14-s5u removed the all-short positive-modulus loss and improved the same normalized local system to `1/21` on the `M` scale.
