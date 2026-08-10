# Shared-label support/two-cell minimax barrier at 7/8

```yaml
ID: TB-LEMMA-shared-label-7-8-minimax-barrier
TYPE: LEMMA
STATUS: CURRENT
TITLE: Shared-label support plus one adjacent two-cell receiver has exact minimax barrier 7/8
SCOPE: BOTH
SOURCE_STAGE: Stage14-4cb
SOURCE_PR: 438
SOURCE_MERGE_SHA: 3fdad0c0673526ea39fed935b4ea69fcaf52a125
SOURCE_FILES:
  - stages/stage14/14-4cb/result.md
  - stages/stage14/14-s7-14/result.md
```

## INPUT

Dyadically fix `xi~B^gamma` in the current reduced-coordinate common refinement.

## OUTPUT

Merged 4cb/s7-14 gives two valid bounds on the same shell:

```text
E_support(gamma)=1/2+gamma/2
E_2cell(gamma)=1-gamma/6
E(gamma)=min(E_support,E_2cell).
```

Their exact crossing is

```text
gamma=3/4,
E=7/8.
```

Hence

```text
SHARED_LABEL_SUPPORT_PLUS_ONE_TWO_CELL_ARCHITECTURE_BARRIER=7/8
LARGE_XI_SUPPORT_ALONE_BEATS_7_8=false.
```

## VARIABLE DICTIONARY

- `gamma`: exponent of the shared squarefree label `xi`.
- support branch: ambient realized-coordinate support with fixed-label factorization cost `B^o(1)`.
- two-cell branch: one canonically selected adjacent coefficient using the proved `C^(-1/3)` saving.

## USED BY

- Rejecting new stages that merely recount `xi` support with the same two ingredients.
- Locating the exact current critical shell `xi~B^(3/4)`.

## DO NOT USE FOR

- Do not claim no stronger future theorem can beat `7/8`.
- Do not multiply the two bounds; the valid combination is a minimum on the same restricted shell.

## PROVENANCE NOTES

4cb and s7-14 independently freeze the same shared-label barrier.