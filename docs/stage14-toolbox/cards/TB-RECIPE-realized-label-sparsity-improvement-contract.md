# Realized shared-label sparsity improvement contract

```yaml
ID: TB-RECIPE-realized-label-sparsity-improvement-contract
TYPE: RECIPE
STATUS: CURRENT
TITLE: Any positive realized-xi sparsity exponent gives a strict improvement below 7/8
SCOPE: MAIN
SOURCE_STAGE: Stage14-4cb
SOURCE_PR: 438
SOURCE_MERGE_SHA: 3fdad0c0673526ea39fed935b4ea69fcaf52a125
SOURCE_FILES:
  - stages/stage14/14-4cb/result.md
```

## INPUT

A physical realized-label theorem on the critical shared-label family of the form

```text
#{xi~B^gamma : xi occurs physically}
 << B^((1-delta)*gamma+o(1))
```

for fixed `delta>0`.

## OUTPUT

Merged 4cb converts this to

```text
E_support,delta=1/2+gamma/2-delta*gamma
```

and, with the existing two-cell branch,

```text
gamma_delta=3/(4-6*delta)
E_delta=1-1/(8-12*delta)<7/8
```

while the crossing remains in range. In particular `delta=1/12` gives `E_delta=6/7`.

## VARIABLE DICTIONARY

- `delta`: power-saving exponent in the number of physically realized shared labels, not ambient squarefree labels.
- `E_delta`: resulting whole-family exponent after exhaustive recombination with the existing two-cell receiver.

## USED BY

- Main-line tests of realized `xi` sparsity near `xi~B^(3/4)`.
- Quantifying whether a proposed label theorem is strong enough to move the whole-family ledger.

## DO NOT USE FOR

- Ambient counting of all squarefree `xi` is not this theorem.
- A finite deficit in observed labels is not a positive uniform `delta`.

## PROVENANCE NOTES

The conversion formula and sufficiency statement are merged 4cb results.