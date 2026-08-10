# Radical-rich incidence / small-denominator dichotomy

```yaml
ID: TB-RECIPE-radical-incidence-small-D-dichotomy
TYPE: RECIPE
STATUS: CURRENT
TITLE: Split a radical-rich witness into full-radical incidence or small denominator
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bj
SOURCE_PR: 355
SOURCE_MERGE_SHA: 7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7
SOURCE_FILES:
  - stages/stage14/14-4bi-S/result.md
  - stages/stage14/14-4bj/result.md
```

## INPUT

A supported exact witness on the H-edge with

```text
R_H=rad_odd(H)
U_*=max(|u1|,|u2|)
```

and thresholds `rho,nu>0`.

## OUTPUT

Use the exact two-way split

```text
R_H >= B^rho and U_* >= B^nu
  -> full-radical rectangle gain B^(-min(rho,nu)+epsilon)

R_H >= B^rho and U_* < B^nu
  -> D <= 2*U_* < 2*B^nu.
```

Together with the radical-poor base/class bound, every supported witness lies in

```text
R_H <= B^rho
OR
full-radical long-coordinate incidence
OR
D < 2*B^nu.
```

At the main-track critical thresholds

```text
rho=1/2
nu=10/21,
```

the radical-poor family is at square-root scale and the long coordinate layer carries the full missing `10/21` coordinate exponent.

## VARIABLE DICTIONARY

- `U_*` = larger square-variable magnitude on the H-edge.
- `D` = generic rational witness denominator from toolbox-af.
- `rho,nu` = independently chosen radical and coordinate thresholds.

## USED BY

- Quickly dispatching radical-rich witness boxes.
- Identifying the small-denominator receiver after incidence.
- Preserving the exact exponent ledger `1/2` and `10/21` without re-deriving it.

## DO NOT USE FOR

- Do not claim the long-coordinate gain is already a packet-existence saving.
- Do not identify `D` with compact physical denominator `D_T`.
- Do not claim the small-D branch is itself power-sparse without a separate packet-level theorem.

## PROVENANCE NOTES

Merged PR #352 proves the full-radical long/short structure. Merged PR #355 freezes the critical `rho=1/2`, `nu=10/21` main-track ledger and the remaining packet-level quantifier gap.