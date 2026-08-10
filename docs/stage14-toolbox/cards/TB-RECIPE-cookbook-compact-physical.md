# Compact physical half-angle cookbook

```yaml
ID: TB-RECIPE-cookbook-compact-physical
TYPE: RECIPE
STATUS: CURRENT
TITLE: Checklist for dual compact torsion and half-angle prime routing
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bl
SOURCE_PR: 365
SOURCE_MERGE_SHA: dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
SOURCE_FILES:
  - stages/stage14/14-s6-06/result.md
  - stages/stage14/14-s6-07/result.md
  - stages/stage14/14-4bl/result.md
```

## INPUT

A physical two-face pair at receiver level `L5` with the exact compact torsion selectors available.

## OUTPUT

The dual selector/cancellation decomposition `D_-,D_+,k_-,k_+`, the product identity `QK=X2/kappa`, and deterministic good-prime routing into the four gcd cells.

## VARIABLE DICTIONARY

- `D_-`, `D_+` = compact denominator selectors.
- `k_-`, `k_+` = cancellation cofactors.
- `Q=D_+D_-`, `K=k_+k_-`.
- generic witness `D` and abstract `D_min` are different objects.

## USED BY

- Physical half-angle incidence stages.
- Deciding which divisor/cancellation factor receives a good odd prime.

## DO NOT USE FOR

- Do not assign independent Bernoulli probabilities to root signs.
- Do not identify compact selectors with the generic witness denominator.

## PROVENANCE NOTES

The recipe packages merged s6-06/s6-07/4bl identities without strengthening them.