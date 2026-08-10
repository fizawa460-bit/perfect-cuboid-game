# Compact T0 torsion translation

```yaml
ID: TB-FORMULA-compact-t0-torsion-translation
TYPE: FORMULA
STATUS: CURRENT
TITLE: Exact compact translation of a physical point by T0=(0,0)
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-05
SOURCE_PR: 356
SOURCE_MERGE_SHA: c2273d0388b48f8fb51d9dc69d8977efbc83db37
SOURCE_FILES:
  - stages/stage14/14-s6-05/result.md
```

## INPUT

A physical point `P=(Z,W)` on

```text
E_{S,X}: W^2=Z(Z-S^2)(Z+X^2),
```

with `Z>S^2`, and the rational 2-torsion point `T0=(0,0)`.

## OUTPUT

```text
Z(P+T0)=-S^2*X^2/Z,
W(P+T0)= S^2*X^2*W/Z^2.
```

The map is an involution and sends the physical point to

```text
-X^2<Z(P+T0)<0.
```

## VARIABLE DICTIONARY

- `P` = exact physical rational point.
- `T0` = `(0,0)` rational 2-torsion.
- `Q0=P+T0` = minus-column compact selector point.

## USED BY

- Physical compact Kummer-class selection.
- Exact physical denominator extraction.
- Recovery of the physical point by the same torsion translation.

## DO NOT USE FOR

- Do not identify this translation with maximal 2-halving.
- Do not identify it with the later s7 `j=1728` twist torsion correspondence.
- The formula itself is structural and gives no counting saving.

## PROVENANCE NOTES

Merged Stage14-s6-05 derives the addition formula directly on the monic cubic and verifies involutivity.