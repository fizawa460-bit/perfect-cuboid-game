# Physical hit to integral global-small-point witness

```yaml
ID: TB-RECIPE-physical-to-integral-witness
TYPE: RECIPE
STATUS: CURRENT
TITLE: One-sided physical-hit to integral-witness majorant pipeline
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
```

## INPUT

A Stage14 physical active base below cutoff `B`.

## OUTPUT

Use the following one-sided pipeline:

```text
1. Take the associated non-torsion rational point in the merged logarithmic height window.
2. If it is 2-divisible, repeatedly halve it until the class is nonzero in E_F(Q)/2E_F(Q).
3. Canonical height does not increase under halving because hat_h(2R)=4 hat_h(R).
4. Write the resulting rational witness as Z=A/D^2, W=Y/D^3.
5. Form G0,G1,G2 and the exact integral witness equation.
```

At the counting level the safe majorant is

```text
V(B) <= J_C(B) <= N_local(B).
```

The intermediate `J_C` keeps global solubility and the logarithmic small-point condition but does not require reconstruction of the original physical point from the chosen maximally-halved representative.

## VARIABLE DICTIONARY

- `V(B)` = physical active-base count in this one-sided comparison.
- `J_C(B)` = globally soluble nonzero descent classes with a non-torsion representative in the fixed small-height window.
- `N_local(B)` = corresponding local-solubility majorant.

## USED BY

- Passing from physical counting to exact integral witness variables without losing an upper bound.
- Separating global-witness analysis from the already-closed local character algebra.

## DO NOT USE FOR

- Do not reverse the arrows.
- Do not require the maximally-halved witness itself to reconstruct the original physical point.
- Do not count all rational representatives of one class as distinct physical objects.

## PROVENANCE NOTES

Merged PR #345 records `PHYSICAL_RECONSTRUCTION_DROPPED_ONLY_FOR_UPPER_MAJORANT=true` and proves termination of the halving selection using finite generation.