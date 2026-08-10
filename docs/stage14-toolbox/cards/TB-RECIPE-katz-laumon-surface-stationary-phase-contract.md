# Katz--Laumon surface stationary-phase import recipe

```yaml
ID: TB-RECIPE-katz-laumon-surface-stationary-phase-contract
TYPE: RECIPE
STATUS: CURRENT
TITLE: Imported Katz--Laumon stationary-phase contract for the adjacent two-cell transform
SCOPE: S
SOURCE_STAGE: Stage14-s7-10
SOURCE_PR: 425
SOURCE_MERGE_SHA: 1fca91407117c6cf486483b49299733bbbbbd519
SOURCE_FILES:
  - stages/stage14/14-s7-10/result.md
```

## INPUT

The surface mixed trace for `H(R,S)=(1-RS)(1+RS)(S-R)(S+R)` and additive phase `hR+kS`.

## OUTPUT

Uniform `|T_p(h,k)|<<p` after splitting generic, diagonal, and axis frequencies.

## VARIABLE DICTIONARY

The imported contract uses: four multiplicity-one SNC components; nontrivial quadratic Kummer local monodromy; isolated Morse stationary points in the generic chamber; nontrivial Artin--Schreier phase at infinity; explicit treatment of positive-dimensional exceptional strata.

## USED BY

- Two-dimensional tame-Kummer plus additive-phase problems with a fixed SNC divisor.
- Auditing whether a stationary-phase theorem is uniform in additive frequency.

## DO NOT USE FOR

- Do not apply the generic chamber estimate to diagonal/axis exceptions without their separate proofs.
- Do not infer this contract from a singular highest homogeneous polynomial alone.

## PROVENANCE NOTES

Merged s7-10 proves every listed Stage14-side hypothesis and closes diagonals by exact cancellation and axes by one-dimensional estimates.