# Fixed-fiber versus active-direction warning

```yaml
ID: TB-WARNING-fixed-fiber-active-direction
TYPE: WARNING
STATUS: CURRENT
TITLE: Subpolynomial partners per direction do not imply sparse active directions
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-09
SOURCE_PR: 373
SOURCE_MERGE_SHA: 54aa839606d2ebeee8747837acec940da26a1534
SOURCE_FILES:
  - stages/stage14/14-s6-09/result.md
```

## INPUT
A fixed primitive direction/base has only `B^o(1)` compatible physical partners.

## OUTPUT
Use
```text
A_phys(B) <= E_phys(B) <= A_phys(B)*B^o(1).
```
Thus edge and active-direction counts share the same power exponent, but the active-direction exponent still has to be proved.

## VARIABLE DICTIONARY
- fixed fiber = partners above one fixed direction.
- active direction = a direction supporting at least one physical partner.

## USED BY
- Recognizing when a fiber theorem has reached its power-scale floor.

## DO NOT USE FOR
- Do not infer `A_phys(B)=B^o(1)` from subpolynomial fiber multiplicity.
- Improving an already-subpolynomial degree does not by itself improve the vertex exponent.

## PROVENANCE NOTES
s6-09 closes the fixed-fiber analytic problem and isolates active-direction sparsity as the remaining global quantity.