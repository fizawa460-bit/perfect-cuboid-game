# Lei Fu Newton-polyhedron import recipe

```yaml
ID: TB-RECIPE-fu-newton-polyhedron-import-contract
TYPE: RECIPE
STATUS: CURRENT
TITLE: Imported Lei Fu Corollary 0.3 contract through the four-Kummer Gauss lift
SCOPE: MAIN
SOURCE_STAGE: Stage14-4by
SOURCE_PR: 426
SOURCE_MERGE_SHA: d04d777c5375e667af0be1ffa216fb0f79a950c4
SOURCE_FILES:
  - stages/stage14/14-4by/result.md
```

## INPUT

The adjacent two-cell mixed transform after restricting to the torus and lifting four quadratic Kummer factors.

## OUTPUT

Uniform torus `O(p)` for generic frequencies, followed by direct axis bounds and exact-zero exceptional frequency lines.

## VARIABLE DICTIONARY

The Gauss-lifted Laurent polynomial is

```text
Phi=hR+kS+U(1-RS)+V(1+RS)+W(S-R)+Z(S+R).
```

The import requires full-dimensional Newton support and nondegeneracy for every face not containing the origin. Merged 4by proves the only potential exceptional frequencies are `h=+/-k` and treats them exactly.

## USED BY

- Toric mixed-character sums that admit an exact Kummer Gauss lift.
- Checking whether a Newton-polyhedron theorem supplies the required parameter-uniform scale.

## DO NOT USE FOR

- Do not assume Newton nondegeneracy from finite-prime evidence.
- Do not include exceptional frequency lines in the generic theorem without a separate receiver.

## PROVENANCE NOTES

Merged 4by imports Lei Fu, *Twisted Exponential Sums*, Corollary 0.3 and proves the Stage14 specialization face by face.