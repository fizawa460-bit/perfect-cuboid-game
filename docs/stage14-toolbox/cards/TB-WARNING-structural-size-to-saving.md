# Structural-size versus counting-saving warning

```yaml
ID: TB-WARNING-structural-size-to-saving
TYPE: WARNING
STATUS: CURRENT
TITLE: A forced large modulus, denominator, gcd, or variable is not itself a saving
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bl
SOURCE_PR: 365
SOURCE_MERGE_SHA: dffc5669ca73c4bb7e4b5115e1fe238dde5605ae
SOURCE_FILES:
  - stages/stage14/14-s6-07/result.md
  - stages/stage14/14-4bl/result.md
```

## INPUT
A deterministic dichotomy forcing one object to satisfy `X>=B^eta`.

## OUTPUT
Treat `eta` as a structural scale. A count saving requires a theorem that exploits this largeness on the correct physical quantifiers.

## VARIABLE DICTIONARY
- structural scale = lower bound on a modulus/gcd/denominator/variable.
- count saving = a reduced cardinality exponent for the target family.

## USED BY
- Reading `41/420`, `10/21`, large gcd cells, and dual products correctly.

## DO NOT USE FOR
- Do not relabel a forced-variable exponent as a saving exponent.
- Do not assume `large q` means a `1/q` family density without an incidence theorem.

## PROVENANCE NOTES
s6-07 and 4bl isolate positive-power structural scales while explicitly separating them from a proved whole-family saving.