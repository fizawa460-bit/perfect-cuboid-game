# Compact selector quantifier and notation boundary

```yaml
ID: TB-WARNING-compact-selector-quantifier-boundary
TYPE: WARNING
STATUS: CURRENT
TITLE: Keep generic, least-packet, compact, and dual half-angle denominators distinct
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bl
SOURCE_PR: 365
SOURCE_MERGE_SHA: dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
SOURCE_FILES:
  - stages/stage14/14-s6-05/result.md
  - stages/stage14/14-s6-06/result.md
  - stages/stage14/14-s6-07/result.md
  - stages/stage14/14-4bl/result.md
```

## INPUT

Any argument that uses the symbols `D`, `D_min`, `D_T`, `D_-`, `D_+`, `Q`, `K`, or a root-sign/gcd-cell condition.

## OUTPUT

Enforce the following distinctions:

```text
D       = generic rational witness denominator,
D_min   = least denominator among bounded-height representatives of an abstract packet,
D_T     = s6-05/s6-06 physical compact T0 selector = D_- in dual notation,
D_-     = minus half-angle compact selector,
D_+     = plus half-angle compact selector,
Q       = D_+D_- dual denominator product,
K       = k_+k_- dual cancellation product.
```

Also keep these quantifiers separate:

```text
exact physical identity
!= coordinate-density saving
!= packet-existence saving
!= whole-family saving.
```

## VARIABLE DICTIONARY

- `T0=(0,0)` = minus-column torsion selector.
- `T-=(-X^2,0)` = plus-column torsion selector.
- The later s7 `j=1728` torsion/self-correspondence lives on a different model and must not be identified with these selectors.

## USED BY

- Reviewing main/s imports of compact denominator formulas.
- Exponent-ledger checks.
- Preventing stale one-selector notation from being treated as a second independent condition.

## DO NOT USE FOR

Forbidden shortcuts include:

```text
D_min=D_-=D_+,
large Q -> multiply two independent 1/D savings,
large K -> automatic square-divisor density saving,
root sign -> independent Bernoulli saving,
gcd cell -> fresh saving after it has already become an automatic square factor,
historical 10/21 threshold -> current remaining sqrt gap.
```

## PROVENANCE NOTES

This warning consolidates the failure modes explicitly identified in merged s6-05/s6-06/s6-07 and 4bl. It does not add a theorem.