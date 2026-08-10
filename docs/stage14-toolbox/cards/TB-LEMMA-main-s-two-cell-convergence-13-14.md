# Main/s two-cell convergence at 13/14

```yaml
ID: TB-LEMMA-main-s-two-cell-convergence-13-14
TYPE: LEMMA
STATUS: CURRENT
TITLE: Main and s independently close the adjacent two-cell Fourier gate and converge to 13/14
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-10
SOURCE_PR: 425
SOURCE_MERGE_SHA: 1fca91407117c6cf486483b49299733bbbbbd519
SOURCE_FILES:
  - stages/stage14/14-s7-10/result.md
  - stages/stage14/14-4by/result.md
```

## INPUT

Merged s7-10 and merged 4by, which use different external-theorem contracts to prove the same all-frequency adjacent two-cell transform bound.

## OUTPUT

A cross-route consistency fact:

```text
|T_p(h,k)| << p
N_2cell(R,S) << (RS)^(2/3) B^o(1)
V(B) << B^(13/14+o(1)).
```

## VARIABLE DICTIONARY

- s7-10 route: Katz--Laumon stationary phase plus explicit axis/diagonal treatment.
- 4by route: Lei Fu Newton-polyhedron theorem after four-Kummer Gauss lift plus explicit exceptions.
- `13/14` is one theorem conclusion, not two independent savings.

## USED BY

- Cross-route verification of the imported two-cell receiver.
- Current exponent provenance.

## DO NOT USE FOR

- Do not multiply the two proofs as if they were independent density events.
- Agreement of two routes does not bypass either route's individual hypothesis contract.

## PROVENANCE NOTES

Merged s7-10 and 4by independently close the same receiver and the same exact minimax `13/14`.