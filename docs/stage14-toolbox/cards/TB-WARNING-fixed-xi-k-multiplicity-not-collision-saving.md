# Fixed (xi,k) multiplicity is not average collision sparsity

```yaml
ID: TB-WARNING-fixed-xi-k-multiplicity-not-collision-saving
TYPE: WARNING
STATUS: CURRENT
TITLE: Subpolynomial pointwise multiplicity for a fixed joint label does not save the off-diagonal collision energy
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-14
SOURCE_PR: 437
SOURCE_MERGE_SHA: 31c3636016f5f0ff80133f0c1b6a9cbbd91a3697
SOURCE_FILES:
  - stages/stage14/14-s7-14/result.md
```

## INPUT

The fixed-`(xi,k)` genus-one bounded-height estimate

```text
r_B(xi,k)<=B^o(1).
```

## OUTPUT

This alone does not imply a power saving for

```text
sum_xi,k r_B(xi,k)*(r_B(xi,k)-1).
```

The missing theorem is average recurrence/sparsity of the map

```text
P/Q -> (xi,k).
```

## VARIABLE DICTIONARY

Pointwise fiber size and family collision energy occupy different quantifier levels.

## USED BY

- Preventing fixed-fiber genus-one arguments from being promoted directly to a `7/8-delta` whole-family count.

## DO NOT USE FOR

- Do not multiply a `B^o(1)` pointwise bound by the number of occupied labels and call the result a power saving unless label occupancy itself has a power saving.

## PROVENANCE NOTES

Merged s7-14 includes an explicit countermodel showing bounded pointwise multiplicity can coexist with collision mass of full linear size.