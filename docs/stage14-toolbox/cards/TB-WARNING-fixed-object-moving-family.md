# Fixed-object versus moving-family warning

```yaml
ID: TB-WARNING-fixed-object-moving-family
TYPE: WARNING
STATUS: CURRENT
TITLE: A fixed genus-one point bound is not a moving-family count
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bq
SOURCE_PR: 395
SOURCE_MERGE_SHA: aa21a3604cf72e06f797c8ba2ecff96b49e60f44
SOURCE_FILES:
  - stages/stage14/14-s6-02/result.md
  - stages/stage14/14-4bq/result.md
```

## INPUT
A theorem giving few bounded-height rational points on one fixed genus-one curve or fixed packet.

## OUTPUT
To obtain a family count, also supply: a bound for the moving fixed parameters, the correct height transfer, recovery multiplicity, and a summable family ledger.

## VARIABLE DICTIONARY
- fixed object = one curve/packet after all coefficients are frozen.
- moving family = the union over coefficients/cores/directions varying with B.

## USED BY
- Deciding whether elliptic/genus-one bounds affect the whole Stage14 family.

## DO NOT USE FOR
- Do not sum `B^o(1)` per fixed curve over `O(B)` curves and call it a power saving.
- Smooth genus one by itself is geometry, not a global counting theorem.

## PROVENANCE NOTES
4bq succeeds only after pairing genus-one multiplicity with diagonal enumeration, slope injectivity, and `UV<=B`; the fixed witness curve alone did not close the moving family.